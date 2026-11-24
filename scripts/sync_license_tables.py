#!/usr/bin/env python3
"""市場段落的許可證表由程式產生（2026-11-24，用戶決定「程式產生許可證表」；範本 DETxGNN／FRTxGNN 同名檔、UkTxGNN／SgTxGNN）。

為什麼：「## Informatie over de Nederlandse markt」（或「Marktinformatie Nederland」）段落的許可證表原本是 AI 寫的自由格式表
（多數表頭「RVG-nummer | Productnaam | Toedieningsvorm | Goedgekeurde indicatie」，依 10-31 前舊證據包只列 1～5 張，
號碼格或品名格夾「(niet geregistreerd)」）。CBG 現行登記每週變，AI 表不會跟著改；而且 2026-11-12 依成分重建後，
很多藥有上百張登記，表上的 1～5 張不能代表本藥。改成程式依證據包（data/bundles/<藥>/drug_bundle.json 的 thaifda.records，
CBG Geneesmiddeleninformatiebank metadata.csv；scripts/rebuild_licenses_by_ingredient.py 收的）產生，每週排程
（license_adapter.sync_tables）自動同步。

表的內容（全程不用 AI；文字照 CBG 原文（荷蘭文），不翻譯）：
  | Registratienummer | Productnaam | Werkzame stof(fen) | Farmaceutische vorm | Registratiehouder | Status |
  （Registratiehouder＝證據包 license_holder，CBG 原文；2026-11-24 第二輪加回：母目錄 checker 已豁免「GmbH … KG」公司名（295dd578））
  狀態欄：現行登記＝「Geldig」；不在 CBG 現行清單（cbg_not_listed、license_status cancelled）＝「Niet geregistreerd」（照 CBG 網站原文，
  不寫 ingetrokken／doorgehaald；字樣與 .claude/license_labels/NlTxGNN.json 相同）。
  排序：有效在前；同狀態時單方（kind=single）在前，再依登記號數字；最多 MAX_ROWS 列，超過時表下一句 SHOW（顯示 N／共 M）。
  表後一行來源句（SOURCE）；證據包沒有任何紀錄時整個區塊只有 NONE_LINE。
  區塊前後各一行 <!-- licenses:begin --> <!-- licenses:end -->（查核紀錄、刪句工具與 gate 用來分辨程式寫的字）。
放在哪：市場段落（## 或 ### 標題＝site.MARKET_SECTIONS）取代段落的第一張表（表頭有 RVG 或 Registratie）；段落沒有表時放在段落開頭。
  沒有市場段落的頁不加。表以外的文字不動（正文張數由 scripts/rewrite_license_counts.py 依快照改寫）。
資料來源：預設讀快照 snapshots/nl_licenses.json.gz 的 rows／total（scripts/build_license_snapshot.py 依證據包算好，用 rows_of）；
  --bundles 改讀 data/bundles（每週排程用）。gate（src/nltxgnn/regulatory/licenses.py）檢查程式區塊＝快照重算的結果。
誰會跑：scripts/apply_drug_reviews.py（非 --check）結尾、scripts/build_license_snapshot.py 結尾、每週排程 license_adapter.sync_tables
  （--bundles）。sync_notes_to_docs.py 整頁重寫後會跑 apply_drug_reviews.py，所以也會重新產生。

第一次換表（--migrate，2026-11-24 一次性）另做兩件事：
  - 市場段落裡只講「舊表列了幾筆／清單是否完整」的句子（CAPTION）與句首子句（CAP_LEAD）拿掉（程式表有自己的 SHOW 句，
    舊說明的筆數跟新表對不上）；查核紀錄的更正文字／錨點所在的句子不動。
  - 錨在被取代的表或說明上的查核紀錄標 status: superseded＋superseded_by（紀錄保留、頁面不顯示框，同 Tw 慣例）。
用法（repo 根目錄）：python3 scripts/sync_license_tables.py [--bundles] [--check] [--migrate [--dry-run]] [頁 ...]
"""
import datetime as dt
import gzip
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAP = ROOT / "snapshots" / "nl_licenses.json.gz"
MARKET = ("Informatie over de Nederlandse markt", "Marktinformatie Nederland")  # ＝site.MARKET_SECTIONS
BEGIN = "<!-- licenses:begin -->"
END = "<!-- licenses:end -->"
HEAD = ["| Registratienummer | Productnaam | Werkzame stof(fen) | Farmaceutische vorm | Registratiehouder | Status |",
        "|------|------|------|------|------|------|"]
VALID, NOT_LISTED = "Geldig", "Niet geregistreerd"
SOURCE = ("Bron: CBG-MEB – Geneesmiddeleninformatiebank (metadata.csv); productnaam, werkzame stoffen, farmaceutische vorm en registratiehouder "
          "in de oorspronkelijke Nederlandse bewoording van het CBG. „Niet geregistreerd”: het registratienummer "
          "komt niet voor in de actuele Geneesmiddeleninformatiebank.")
SHOW = "Getoond worden {n} van de {m} registraties in de gegevens (geldige eerst, enkelvoudige middelen vóór combinatiepreparaten)."
NONE_LINE = "In de gebruikte CBG-gegevens is voor dit middel geen registratie vastgelegd."
MAX_ROWS = 20
SUPERSEDED_BY = "Programmatisch gegenereerde vergunningstabel (scripts/sync_license_tables.py, 2026-11-24, op basis van de CBG-registratiegegevens)"
# 每週排程 3b 的自我檢查（license_refresh）：改到的行除了表格列只能是這些（license_adapter.PAGE_NOTE 用同一份）
PAGE_NOTE = (r"^(" + "|".join(re.escape(x) for x in (BEGIN, END, SOURCE, NONE_LINE)) +
             r"|Getoond worden \d+ van de \d+ registraties in de gegevens \(geldige eerst, enkelvoudige middelen vóór combinatiepreparaten\)\.)$")

NUMW = r"(?:\d+|een|één|twee|drie|vier|vijf|zes|zeven|acht|negen|tien)"
# 只講舊表列了幾筆／清單是否完整的整句（--migrate 時拿掉）
CAPTION = re.compile(
    r"^\*?(?:"
    rf"Hieronder (?:staan|volgen) de eerste {NUMW} (?:vergunningen|registraties)(?: \(CBG-MEB\))?\."
    rf"|Hieronder een overzicht van de eerste {NUMW} (?:vergunningen|registraties)(?: \(CBG-MEB\))?\."
    r"|De lijst(?: hierboven| hieronder)? is volledig(?: volgens de beschikbare gegevens)?(?: \(\d+ van \d+ (?:vergunningen|registraties)\))?\."
    r"|De lijst (?:met vergunningen )?(?:is mogelijk niet volledig weergegeven|kan onvolledig zijn)(?:; raadpleeg [^.]*)?\."
    r"|De lijst kan uitsluitend de in de lokale CBG-MEB-gegevens vastgelegde vergunningen bevatten\."
    r"|Er is één registratie in de lijst opgenomen\."
    r")\*?$", re.I)
# 句首只講舊表列了幾筆的子句（「De lijst toont de eerste 5 van de beschikbare vergunningen; indicatieteksten …」）：只拿掉子句
CAP_LEAD = re.compile(rf"^De lijst toont de eerste {NUMW} van de beschikbare (?:vergunningen|registraties);\s*", re.I)
# 句尾只講舊表完整的子句（「Er is één vergunning (CBG-MEB) en de lijst is volledig.」）：只拿掉子句
CAP_TAIL = re.compile(r"\s+en de lijst is volledig(?=\.$)", re.I)
SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-ZÀ-Ý*\[(«„“\"])")


def cell(x, n=90):
    t = re.sub(r"\s+", " ", str(x or "").replace("|", "/")).strip()
    return (t if len(t) <= n else t[:n - 1].rstrip() + "…") or "–"


def status_label(r):
    return NOT_LISTED if (r.get("cbg_not_listed") or r.get("license_status") == "cancelled") else VALID


def _num(k):
    m = re.search(r"\d+", k)
    return int(m.group(0)) if m else 0


def rows_of(tf, fc=None):
    """證據包 thaifda → (表格列（全部，已排序）, 總數)。總數＝total_matches 與收錄筆數取大者。"""
    seen, keyed = set(), []
    for r in tf.get("records") or []:
        k = str(r.get("license_id") or "").strip()
        if not k or k in seen:
            continue
        seen.add(k)
        lab = status_label(r)
        row = (f"| {k} | {cell(r.get('brand_name_zh') or r.get('brand_name_en'), 80)} | {cell(r.get('ingredients'), 80)} | "
               f"{cell(r.get('dosage_form'), 50)} | {cell(r.get('license_holder'), 60)} | {lab} |")
        keyed.append(((lab != VALID, r.get("kind") != "single", k.split()[0] if " " in k else "", _num(k), k), row))
    rows = [row for _, row in sorted(keyed)]
    return rows, max(len(rows), int(tf.get("total_matches") or 0))


def program_block(rows, total):
    if not rows:
        return [NONE_LINE]
    out = HEAD + rows[:MAX_ROWS] + [""]
    if total > min(len(rows), MAX_ROWS):
        out += [SHOW.format(n=min(len(rows), MAX_ROWS), m=total), ""]
    return out + [SOURCE]


def wrap(block):
    return [BEGIN, ""] + block + ["", END]


def _sections(lines):
    out = []
    for i, ln in enumerate(lines):
        m = re.match(r"^(#{2,3}) (.+?)\s*$", ln)
        if m and m.group(2) in MARKET:
            lv = len(m.group(1))
            j = next((k for k in range(i + 1, len(lines)) if re.match(rf"^#{{1,{lv}}} ", lines[k])), len(lines))
            out.append((i, j))
    return out


def _is_license_table_head(lines, k):
    return lines[k].startswith("|") and (k == 0 or not lines[k - 1].startswith("|")) and re.search(r"RVG|Registratie", lines[k]) \
        and k + 1 < len(lines) and re.match(r"\|\s*:?-", lines[k + 1])


def _splice(lines, x, y, blk):
    """lines[x:y] 換成 blk，前後各留恰好一行空行（只動接縫處的空行）"""
    head, tail = lines[:x], lines[y:]
    while head and not head[-1].strip():
        head.pop()
    while tail and not tail[0].strip():
        tail.pop(0)
    return head + [""] + blk + ([""] + tail if tail else [""])


def _caption_trim(line, protect=()):
    """拿掉行裡只講舊表筆數／完整性的整句（CAPTION）與句首子句（CAP_LEAD）：回 (新行, 拿掉的文字)"""
    if not line.strip() or line.startswith(("|", "#", "<!--", "---", ">")):
        return line, []
    out, gone = [], []
    for x in SPLIT.split(line.strip()):
        if any(p and (x.strip() in p or p in x) for p in protect):
            out.append(x)
            continue
        if CAPTION.match(x.strip()):
            gone.append(x.strip())
            continue
        m = CAP_LEAD.match(x)
        if m:
            gone.append(m.group(0).strip())
            x = x[m.end():]
            x = x[:1].upper() + x[1:]
        m = CAP_TAIL.search(x)
        if m:
            gone.append(m.group(0).strip())
            x = x[:m.start()] + x[m.end():]
        out.append(x)
    return (" ".join(out), gone) if gone else (line, [])


def process(text, rows, total, migrate=False, protect=()):
    """回傳 (新內容, 拿掉的文字)。沒有市場段落時原樣。可重複執行。"""
    lines = text.replace("\r\n", "\n").split("\n")
    blk = wrap(program_block(rows, total))
    gone = []
    if BEGIN in lines and END in lines:
        out = _splice(lines, lines.index(BEGIN), lines.index(END) + 1, blk)
    else:
        secs = _sections(lines)
        if not secs:
            return text, ""
        out = None
        for a, b in secs:
            tb = [k for k in range(a + 1, b) if _is_license_table_head(lines, k)]
            if tb:
                y = tb[0]
                while y + 1 < b and lines[y + 1].startswith("|"):
                    y += 1
                gone += lines[tb[0]:y + 1]
                out = _splice(lines, tb[0], y + 1, blk)
                break
        if out is None:
            a = secs[0][0]
            out = _splice(lines, a + 1, a + 1, blk)
        if migrate:
            for a, b in _sections(out):
                i0 = out.index(BEGIN) if BEGIN in out else -1
                i1 = out.index(END) if END in out else -1
                for k in range(a + 1, b):
                    if i0 <= k <= i1:
                        continue
                    nl, cap = _caption_trim(out[k], protect)
                    if cap:
                        out[k] = nl
                        gone += cap
    t2 = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
    return t2, "\n".join(gone)


def _snapshot():
    return json.loads(gzip.open(SNAP).read().decode("utf-8")).get("drugs", {}) if SNAP.exists() else {}


def _bundle(stem):
    for key in (stem, stem.replace("-", "_"), stem.replace("_", "-")):
        f = ROOT / "data/bundles" / key / "drug_bundle.json"
        if f.exists():
            return json.loads(f.read_text(encoding="utf-8"))
    return None


def is_redirect(text):
    h = text[:3000]
    return 'http-equiv="refresh"' in h or bool(re.search(r"^layout:\s*id_redirect", h, re.M))


def _protect():
    out = {}
    f = ROOT / "docs/_data/drug_reviews.json"
    if f.exists():
        for r in json.loads(f.read_text(encoding="utf-8")).get("records", []):
            if r.get("status"):
                continue
            out.setdefault(r["file"][:-3], []).extend(x.strip() for x in (r.get("replacement"), r.get("anchor")) if x and x.strip())
    return out


def run(from_bundles=False, check=False, only=None, migrate=False):
    """回傳改到的頁（檔名）；migrate 時回 (改到的頁, {頁: 拿掉的文字})。快照或證據包沒有的頁不動。"""
    snap = {} if from_bundles else _snapshot()
    prot = _protect() if migrate else {}
    changed, removed = [], {}
    for p in sorted((ROOT / "docs/_drugs").glob("*.md")):
        if only and p.name not in only and p.stem not in only:
            continue
        raw = p.read_bytes().decode("utf-8")
        if is_redirect(raw):
            continue
        if from_bundles:
            b = _bundle(p.stem)
            if b is None:
                continue
            rows, total = rows_of(b.get("thaifda") or {})
        else:
            e = snap.get(p.stem)
            if not e or "rows" not in e:
                continue
            rows, total = e["rows"], e["total"]
        crlf = "\r\n" in raw[:500]
        t0 = raw.replace("\r\n", "\n")
        new, gone = process(t0, rows, total, migrate, prot.get(p.stem, ()))
        if gone:
            removed[p.stem] = gone
        if new != t0:
            changed.append(p.name)
            if not check:
                p.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
    return (changed, removed) if migrate else changed


def supersede(removed_by_page, today=None):
    """--migrate 時：錨在拿掉的文字上、新頁面上也找不到的查核紀錄標 superseded（紀錄保留）。回傳標記的 id"""
    data = ROOT / "docs/_data/drug_reviews.json"
    doc = json.loads(data.read_text(encoding="utf-8"))
    today = today or dt.date.today().isoformat()
    marked = []
    for r in doc["records"]:
        gone = removed_by_page.get(r["file"][:-3])
        if not gone or r.get("status") or r.get("action") not in ("correct", "annotate", "rereview"):
            continue
        page = (ROOT / "docs/_drugs" / r["file"]).read_text(encoding="utf-8")
        page = re.sub(r"<!-- review:begin (\S+) -->.*?<!-- review:end \1 -->", "", page, flags=re.S)
        page = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), "", page, flags=re.S)  # 程式表裡的號碼不算錨點
        keys = [x.strip() for x in (r.get("anchor"), r.get("replacement"), r.get("claim")) if x and x.strip()]
        loc = (r.get("anchor") or (r.get("replacement") if r["action"] == "correct" else r.get("claim")) or r.get("claim") or "").strip()
        if not keys or (loc and loc in page):
            continue  # 錨點還在頁面上：照舊套用
        gl = [g.strip() for g in gone.split("\n") if g.strip()]
        if any(k in gone or any(k in g or g in k for g in gl) for k in keys):
            r["status"] = "superseded"
            r["superseded_by"] = SUPERSEDED_BY
            r["superseded_on"] = today
            marked.append(r["id"])
    if marked:
        data.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return marked


def block_problems(sec_lines, entry):
    """gate 用：段落裡的程式區塊＝快照重算的結果（licenses.page_problems 呼叫）"""
    has_b, has_e = BEGIN in sec_lines, END in sec_lines
    if has_b != has_e:
        return ["程式許可證區塊標記不成對"]
    if not has_b or "rows" not in entry:
        return []
    i, j = sec_lines.index(BEGIN), sec_lines.index(END)
    got = [x for x in sec_lines[i + 1:j] if x.strip()]
    want = [x for x in program_block(entry["rows"], entry["total"]) if x.strip()]
    if got != want:
        k = next((k for k, (x, y) in enumerate(zip(got, want)) if x != y), min(len(got), len(want)))
        return [f"程式許可證區塊第 {k + 1} 行跟快照重算的結果不同（程式表被手改或資料已更新：跑 python3 scripts/sync_license_tables.py）"]
    return []


if __name__ == "__main__":
    a = sys.argv[1:]
    only = {x for x in a if not x.startswith("--")} or None
    if "--migrate" in a:
        ch, rm = run(from_bundles="--bundles" in a, check="--dry-run" in a, only=only, migrate=True)
        print(f"程式許可證表：{'待改' if '--dry-run' in a else '改'} {len(ch)} 頁；拿掉舊表／舊表說明的頁 {len(rm)}")
        for k, v in rm.items():
            caps = [x for x in v.split("\n") if x and not x.startswith("|")]
            if caps:
                print(f"  {k}：說明句 {caps}")
        if "--dry-run" not in a:
            ids = supersede(rm)
            print(f"錨在被取代的表或表說明上的查核紀錄標 superseded：{len(ids)} 筆")
            for i in ids:
                print("  ", i)
        sys.exit(0)
    ch = run(from_bundles="--bundles" in a, check="--check" in a, only=only)
    print(f"程式許可證表：{'待改' if '--check' in a else '改'} {len(ch)} 頁")
    if "--check" in a:
        sys.exit(1 if ch else 0)
