"""正文許可證張數的程式改寫（2026-11-24 建，用戶決定「正文張數自動改寫」；做法移植 KrTxGNN／MyTxGNN／DETxGNN 同名檔，規則是本站荷蘭文句型）。

正文裡「Van de M registraties … zijn er N geldig」「N van de M vergunningen zijn geldig」「N geldige vergunningen」
「In totaal N vergunningen」這類 CBG 登記張數敘述，由程式依許可證快照（snapshots/nl_licenses.json.gz 的 facts）改寫，
每週資料更新後跟著改，不逐筆寫查核紀錄（同 Kr／My／Tw：程式改寫的張數敘述是程式產生的正文）。

只改「句型明確、數字確定是本藥 CBG 登記張數」的地方，其餘一律不動：
  - 句子要有登記字樣（vergunning、registratie、inschrijving），且沒有試驗、文獻、病人、劑量、年份等字樣（NOT_LICENSE）。
  - 跳過：查核框（<!-- review -->）、程式許可證區塊（<!-- licenses -->）、表格列、標題、front matter；
    查核紀錄 replacement／anchor 所在的句子（改了紀錄會對不上）。
  - 整句不動（skipped）：有保留（minstens、mogelijk、onvolledig…）、講證據包或查詢、相對數（andere、overige、extra、daarnaast、waaronder）、
    劑型或單方／複方子集（enkelvoudig、combinatie、tabletten…）、平行輸入、廠商、EMA／FDA／獸用、講表格或清單顯示筆數
    （tabel、lijst、hieronder、getoond…，reason＝display）；事實層 partial 或總數 0 的頁整頁不動。
角色：「X van (de) Y」的 X 看後面的狀態字（geldig→有效；niet geregistreerd／doorgehaald／ingetrokken→非有效），Y＝總數；
「Van de M … zijn er N geldig」M＝總數、N＝有效；「N geldige …」有效；「N niet-geregistreerde／doorgehaalde …」非有效；
「N vergunningen／registraties」總數（後面接「zijn geldig」算有效、接「zijn niet geregistreerd」算非有效）；其餘數字不動。
數字可寫成阿拉伯數字或 twee～twaalf；「één／een」只在緊接（geldige）vergunning／registratie 時算 1。改寫時保留原寫法
（文字數字改成文字，超過 12 用阿拉伯數字）。
同一行只要有一句含登記數字而被略過，整行都不動（免得前後句數字對不上）。
數字已等於該角色的任一合理讀法（沒有限定詞的總數＝總數或有效數）就不動；不等於時兩種讀法相同才改，不同列為 ambiguous。
不改、列出（要改請寫查核紀錄）：原數字 0（zero-premise）、新數字 0（zero-result）、1 跟非 1 之間的改動或「beide」（荷蘭文
名詞單複數、動詞、指示詞要跟著改，grammar）、句子說「alle／beide／de enige … geldig」或「geen … doorgehaald／niet geregistreerd」而事實不符（premise）。
"""
from __future__ import annotations

import re

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-ZÀ-Ý*\[(>„“\"-])")
WORDS = {"twee": 2, "drie": 3, "vier": 4, "vijf": 5, "zes": 6, "zeven": 7, "acht": 8, "negen": 9, "tien": 10,
         "elf": 11, "twaalf": 12, "beide": 2}
W_OUT = {v: k for k, v in WORDS.items() if k != "beide"}
NOUN = r"(?:(?:handels)?vergunning(?:en)?|registratie(?:s|nummers?)?|inschrijving(?:en)?)"
ONE = r"(?:één|een)"
NUM = re.compile(r"(?<![\w.,/-])(\d{1,4}|" + "|".join(sorted(WORDS, key=len, reverse=True)) + r"|" + ONE +
                 r"(?=\s+(?:(?:geldige|enige|actuele)\s+)*(?:Nederlandse\s+)?(?:CBG-)?" + NOUN + r"\b(?!-)))(?![\w%-])", re.I)
LICENSE = re.compile(r"vergunning|registratie|inschrijving", re.I)
NOT_LICENSE = re.compile(r"studie|trial|patiënt|deelnemer|PMID|NCT|publicatie|artikel|casus|\bmg\b|\bml\b|%|\bjaar|maand|week|dosis|score|"
                         r"indicaties|fase|\b(?:19|20)\d\d\b|"
                         r"\bof er\b|vaststellen|nagaan|beoordel|bevestig|controle|controleer|nodig|vereis", re.I)  # 待辦／假設句：「een geldige vergunning」是泛稱
HEDGED = re.compile(r"minstens|ten minste|minimaal|onvolledig|gedeeltelijk|mogelijk|waarschijnlijk|vermoedelijk|"
                    r"evidence pack|bewijspakket|zoekopdracht|zoekactie|\bquery\b|opgevraagd|leverde|"
                    r"\bandere\b|\boverige\b|\bextra\b|aanvullend|daarnaast|waaronder|bovendien|"
                    r"enkelvoudig|monopreparaat|eencomponent|combinatie|samengesteld|"
                    r"tablet|capsule|injectie|infusie|oplossing|poeder|spray|druppel|crème|creme|zalf|gel\b|inhal|pleister|implantaat|zetpil|"
                    r"parallelimport|parallel|fabrikant|houder|leverancier|"
                    r"\bEMA\b|\bFDA\b|\bEU\b|\bEU/|centra(?:al|le)|diergenee|veterinair|homeopath|RVH", re.I)
DISPLAY = re.compile(r"tabel|\blijst|hieronder|hierboven|getoond|weergegeven|\btoont\b|\beerste\b|volgende|overzicht", re.I)
CANC = r"(?:doorgehaald\w*|ingetrokken\w*|vervallen\w*|geschrapt\w*|geannuleerd\w*|niet(?:\s+meer)?[\s-]+geregistreerd\w*)"
VALID = r"(?:geldig\w*|actief\w*)"
ADJ = r"(?:(?:geregistreerde|vastgelegde|bekende|Nederlandse|actuele|lopende|afzonderlijke)\s+)*(?:CBG-)?"
BLOCK = re.compile(r"<!-- (review|licenses):begin.*?<!-- \1:end[^>]*-->", re.S)


def _val(tok):
    t = tok.lower()
    if t.isdigit():
        return int(t)
    if t in WORDS:
        return WORDS[t]
    return 1


def _fmt(tok, v):
    if tok.isdigit() or v not in W_OUT:
        return str(v)
    w = W_OUT[v]
    return w.capitalize() if tok[:1].isupper() else w


def _role(s, a, b):
    left, right = s[max(0, a - 45):a], s[b:b + 80]
    # 「X van (de) Y」的 Y＝總數（前面是數字或「geldige vergunningen」）；「Van de M vergunningen …」的 M＝總數；其他「van N」不動
    if re.search(r"\bvan\s+(?:de\s+|in totaal\s+|totaal\s+)?$", left, re.I):
        pre = re.sub(r"\bvan\s+(?:de\s+|in totaal\s+|totaal\s+)?$", "", left, flags=re.I)
        if re.search(r"(\d+|" + "|".join(WORDS) + r"|" + ONE + r")\s*$", pre, re.I) or \
                re.search(r"(geldige|" + CANC + r")\s+(?:" + NOUN + r"\s*)?\(?$", pre, re.I):
            return "total"
        if re.search(r"(?:^|[(;,]\s*|\.\s+)$", pre) and re.match(r"\s+" + ADJ + NOUN + r"\b", right, re.I):
            return "total"  # 「Van de 5 registraties zijn er 4 geldig」
        return None
    # 「X van (de) Y …」的 X：看後面的狀態字
    m = re.match(r"\s+van\s+(?:de\s+)?\S+\s+" + ADJ + r"(?:" + NOUN + r")?\s*(?:\([^)]*\)\s*)?(?:(?:is|zijn|blijft|blijven|er|momenteel|nog|thans)\s+){0,3}(" + VALID + "|" + CANC + ")", right, re.I)
    if m:
        return "cancelled" if re.match(CANC, m.group(1), re.I) else "valid"
    if re.match(r"\s+van\s+", right, re.I):
        return None
    if re.match(r"\s+geldige\s+" + ADJ + NOUN + r"\b", right, re.I):
        return "valid"
    if re.match(r"\s+(?:niet[\s-]geregistreerde|doorgehaalde|ingetrokken|vervallen)\s+" + ADJ + NOUN + r"\b", right, re.I):
        return "cancelled"
    m = re.match(r"\s+" + ADJ + NOUN + r"\b([^.;,:]{0,40})", right, re.I)
    if m:
        tail = m.group(1)
        if re.search(r"\b(zijn|is|werden|werd)\s+(?:\w+\s+){0,2}" + CANC, tail, re.I):
            return "cancelled"
        if re.search(r"\b(zijn|is)\s+(?:\w+\s+){0,2}geldig\b", tail, re.I) and not re.search(r"\b(alle|beide)\s*$", left, re.I):
            return "valid"
        return "total"
    # 「Van de 5 registraties zijn er 4 geldig」的 4
    if re.search(r"\b(?:zijn|is)\s+(?:er\s+)?(?:momenteel\s+|nog\s+|thans\s+)?$", left, re.I) and re.match(r"\s+" + VALID, right, re.I):
        return "valid"
    return None


def _readings(role, f, explicit):
    t, v, c = f.get("total"), f.get("valid"), f.get("cancelled")
    if role == "cancelled":
        return {c}, c
    if role == "valid":
        return {v}, v
    if explicit:
        return {t}, t
    return {t, v}, (t if t == v else None)


def _premise_ok(sent, f):
    lo = sent.lower()
    if re.search(r"\b(alle|beide|de enige|het enige|enige)\b[^.;]{0,60}" + VALID, lo) and f.get("valid") != f.get("total"):
        return False
    if re.search(r"\bgeen\b[^.;]{0,40}" + CANC, lo) and f.get("cancelled"):
        return False
    return True


def rewrite_sentence(sent, f):
    """回傳 (新句子, 跳過理由或 None)。"""
    if not LICENSE.search(sent) or not NUM.search(sent):
        return sent, None
    found = [(m, _role(sent, m.start(), m.end())) for m in NUM.finditer(sent)]
    found = [(m, r) for m, r in found if r]
    if not found:
        return sent, None
    if NOT_LICENSE.search(sent):
        return sent, None
    if HEDGED.search(sent):
        return sent, "hedged/subset"
    explicit = any(r in ("valid", "cancelled") for _, r in found)
    if DISPLAY.search(sent):  # 講表格顯示筆數：不改；數字跟事實對不上時列出（reason＝display）
        bad = any(_val(m.group(1)) not in _readings(r, f, explicit)[0] for m, r in found)
        return sent, ("display" if bad else "display-ok")
    subs = []
    for m, role in found:
        old = _val(m.group(1))
        ok, v = _readings(role, f, explicit)
        if old in ok:
            continue
        if v is None:
            return sent, "ambiguous"
        if old == 0:
            return sent, "zero-premise"
        if v == 0:
            return sent, "zero-result"
        if (old == 1) != (v == 1) or m.group(1).lower() == "beide":
            return sent, "grammar"
        subs.append((m, v))
    if not subs:
        return sent, None
    if not _premise_ok(sent, f):
        return sent, "premise"
    out, pos = [], 0
    for m, v in subs:
        out.append(sent[pos:m.start(1)])
        out.append(_fmt(m.group(1), v))
        pos = m.end(1)
    out.append(sent[pos:])
    return "".join(out), None


def _line(ln, f, protect, skipped):
    if ln.startswith(("|", "#", "{:")) or not ln.strip():
        return ln
    parts = SENT_SPLIT.split(ln)
    seps = SENT_SPLIT.findall(ln)
    new, held = [], False
    for s in parts:
        if any(p and (p in s or s in p) for p in protect):
            new.append(s)
            continue
        ns, why = rewrite_sentence(s, f)
        if why:
            skipped.append((why, s.strip()))
            held = True
        new.append(ns)
    if held:  # 同一行有句子判斷不了：整行不動
        return ln
    out = new[0]
    for sep, s in zip(seps, new[1:]):
        out += sep + s
    return out


def rewrite(text, facts, protect=()):
    """text：整頁 markdown。facts：快照的 facts。回傳 (新內容, skipped)。front matter、查核框、程式區塊、表格不動。"""
    skipped = []
    if not facts or facts.get("partial") or not facts.get("total"):
        return text, skipped
    protect = [p.strip() for p in protect if p and len(p.strip()) >= 6]
    fm_end = 0
    if text.startswith("---"):
        j = text.find("\n---", 3)
        fm_end = j + 4 if j > 0 else 0
    body = text[fm_end:]
    keep = []

    def hold(m):
        keep.append(m.group(0))
        return f"\x00{len(keep) - 1}\x00"
    body = BLOCK.sub(hold, body)
    lines = [ln if "\x00" in ln else _line(ln, facts, protect, skipped) for ln in body.split("\n")]
    body = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], "\n".join(lines))
    return text[:fm_end] + body, skipped
