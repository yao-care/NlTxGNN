"""NL 證據包依成分、照 CBG 現行登記重建許可證紀錄（2026-11-12，用戶決定「用現行 CBG 清單重建 Nl 事實層」；全程不用 AI）。

原本的紀錄來自第三方鏡像（data.openstate.eu，2026-10-30 已連不上），每個藥大多只收到 1 張登記，且都標 active：
atorvastatin 現行 CBG 有 212 張、證據包只有 1 張（而且那張已不在現行登記）；518 個登記號只有 215 個在現行清單。
頁面的「In de handel (geldige vergunningen: 1 van 1)」、正文的「唯一許可…」都建立在這份不完整的資料上。

來源：CBG 官方 Geneesmiddeleninformatiebank 的 metadata.csv（https://www.geneesmiddeleninformatiebank.nl/metadata.csv，
| 分隔，免金鑰；同 scripts/license_adapter.py）。這份檔只列現行登記的產品、沒有狀態欄。
登記號不在檔裡時，CBG 網站的產品頁寫「Niet geregistreerd geneesmiddel — Het registratienummer … komt niet voor in de
Geneesmiddeleninformatiebank」，所以這類登記照 CBG 原文標「Niet geregistreerd」（license_status＝cancelled，不另外推定為撤銷或過期）。

做法：
1. 本藥成分名：證據包原有紀錄的成分欄（荷蘭文，例 TRAMADOLHYDROCHLORIDE）去掉鹽類／酯類／水合物寫法得到主體，
   取各紀錄共有、且跟頁名最接近的那個（tramadol → TRAMADOL）。原本沒有紀錄的證據包不動（不知道荷蘭文成分名，不猜）。
2. CBG 現行登記（排除順勢療法 RVH）的 WERKZAMESTOFFEN（# 分隔）任一成分主體等於本藥主體 → 收（含複方；kind 依不同成分主體數）。
3. 原有紀錄：在現行清單的照 CBG 更新欄位、status＝active；不在的保留、標 Niet geregistreerd（cbg_not_listed＝下載日）。只加不刪。
4. total_matches＝紀錄數（全部收，不截斷），所以頁面張數是確定值。排序：有效單方、有效複方、不在現行登記。
5. 新收紀錄 source＝SOURCE。可重複執行（每週許可證排程在 license_refresh 前跑；登記號回到現行清單時恢復 active）。
用法（repo 根目錄）：python3 scripts/rebuild_licenses_by_ingredient.py [--download] [--csv 路徑] [--date YYYY-MM-DD] [--dry-run] [--report out.tsv]
"""
import collections
import csv
import difflib
import io
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUNDLES = ROOT / "data/bundles"
CSV = ROOT / "data/raw/cbg_metadata.csv"
URL = "https://www.geneesmiddeleninformatiebank.nl/metadata.csv"
SOURCE = "CBG Geneesmiddeleninformatiebank metadata.csv by ingredient (WERKZAMESTOFFEN, 2026-11-12 rebuild)"
NOT_LISTED = "Niet geregistreerd (komt niet voor in de Geneesmiddeleninformatiebank van het CBG)"

# 荷蘭文鹽類／酯類寫法（連寫或空格分開；長的在前）
SALT = ("DIHYDROCHLORIDE MONOHYDROCHLORIDE HYDROCHLORIDE HYDROBROMIDE DIBROMIDE BROMIDE JODIDE WATERSTOFSULFAAT SULFAAT "
        "DINATRIUMFOSFAAT NATRIUMFOSFAAT FOSFAAT DIACETAAT ACETAAT DIHYDROGEENCITRAAT CITRAAT WATERSTOFTARTRAAT BITARTRAAT TARTRAAT "
        "WATERSTOFMALEAAT MALEAAT WATERSTOFFUMARAAT HEMIFUMARAAT FUMARAAT WATERSTOFSUCCINAAT NATRIUMSUCCINAAT SUCCINAAT MESILAAT BESILAAT "
        "TOSILAAT ESILAAT LACTAAT GLUCONAAT NITRAAT DIPROPIONAAT PROPIONAAT VALERAAT BUTYRAAT PALMITAAT FUROAAT XINAFOAAT PAMOAAT EMBONAAT "
        "STEARAAT OLEAAT DIETHYLAMINE EPOLAMINE ARGININE BUTYLAMINE TERT CILEXETIL MEDOXOMIL AXETIL DINATRIUM NATRIUM KALIUM CALCIUM "
        "MAGNESIUM TROMETAMOL MEGLUMINE ERBUMINE BENZATHINE CHLORIDE").split()
# 無機鹽、元素本身就是藥（NATRIUMCHLORIDE、MAGNESIUMSULFAAT…）：不去字尾
INORGANIC = re.compile(r"^(NATRIUM|KALIUM|CALCIUM|MAGNESIUM|ZINK|IJZER|FERRO|LITHIUM|ALUMINIUM|AMMONIUM|BARIUM|ZILVER)")
# 英荷拼法不同的成分（證據包原紀錄是英文寫法時）
SYN = {"COLISTIMETHATE SODIUM": "COLISTIMETHAAT", "COLISTIMETHATE": "COLISTIMETHAAT"}


def norm(c):
    c = str(c or "").upper().replace("Ï", "I").replace("Ë", "E").replace("É", "E")
    for _ in range(2):
        c = re.sub(r"\([^()]*\)", " ", c)  # (E 300)、(L-)、(Component A en B)
    c = re.sub(r"\b[\d,\.X]+-WATER\b|\bWATERVRIJ\b|\bMONOHYDRAAT\b|\bDIHYDRAAT\b", " ", c)
    c = re.sub(r",\s*(DL|L|D)-?\s*$", " ", c)
    return " ".join(re.sub(r"[^A-Z0-9 ]+", " ", c).split())


def base(c):
    t = norm(c)
    t = SYN.get(t, t)
    if INORGANIC.match(t):
        return t
    for _ in range(3):
        for s in SALT:
            if t.endswith(" " + s) and len(t) - len(s) - 1 >= 5:
                t = t[:-len(s) - 1]
                break
            if t.endswith(s) and len(t) - len(s) >= 5 and " " not in t[-len(s) - 1:]:
                t = t[:-len(s)]
                break
        else:
            break
    return SYN.get(t.strip(), t.strip())


def bundle_parts(s):
    """證據包成分欄是逗號分隔（「TRAMADOLHYDROCHLORIDE, PARACETAMOL」），但胺基酸寫法本身帶逗號（「ARGININE, (L-)」）"""
    return [p.strip() for p in re.split(r",\s+(?!\(|L\b|DL\b|D\b|L-|DL-)", str(s or "")) if p.strip()]


def rid(x):
    return " ".join(str(x or "").split("//")[0].split())


def load_csv(path):
    rows = list(csv.DictReader(io.StringIO(Path(path).read_text(encoding="utf-8", errors="replace")), delimiter="|"))
    if not rows or "WERKZAMESTOFFEN" not in rows[0] or len(rows) < 10000:
        raise SystemExit(f"{path}：欄位或筆數不對（{len(rows)} 筆）")
    idx = collections.defaultdict(list)
    for r in rows:
        if (r.get("SOORT") or "").strip() == "RVH":  # 順勢療法登記
            continue
        nr = (r.get("REGISTRATIENUMMER") or "").strip()
        if not nr:
            continue
        lid = f"{(r.get('SOORT') or '').strip()} {nr}".strip()
        comps = {base(c) for c in (r.get("WERKZAMESTOFFEN") or "").split("#") if c.strip()}
        rec = {"license_id": lid, "brand_name_zh": r.get("PRODUCTNAAM") or "", "brand_name_en": r.get("PRODUCTNAAM") or "",
               "ingredients": (r.get("WERKZAMESTOFFEN") or "").replace("#", ", "), "indication": "",
               "dosage_form": (r.get("FARMACEUTISCHEVORM") or "").strip(), "manufacturer": r.get("HANDELSVERGUNNINGHOUDER") or "",
               "license_holder": r.get("HANDELSVERGUNNINGHOUDER") or "", "approval_date": (r.get("INSCHRIJVINGSDATUM") or "").replace("/", "-"),
               "expiry_date": "", "status": "active", "kind": "single" if len(comps) <= 1 else "combo",
               "route": (r.get("TOEDIENINGSWEG") or "").strip(), "atc": (r.get("ATC") or "").strip()}
        for b in comps:
            idx[b].append(rec)
    cur = {rid(r["license_id"]) for v in idx.values() for r in v}
    return idx, cur, len(rows)


def drug_key(name, recs):
    sets = [{base(p) for p in bundle_parts(r.get("ingredients"))} - {""} for r in recs]
    sets = [s for s in sets if s]
    if not sets:
        return None
    common = set.intersection(*sets)
    if not common:  # 寫法不一（DICLOFENAC DIETHYLAMINE／DICLOFENAC）：取出現最多的
        cnt = collections.Counter(b for s in sets for b in s)
        top = max(cnt.values())
        common = {b for b, n in cnt.items() if n == top}
    return max(sorted(common), key=lambda k: difflib.SequenceMatcher(None, k.lower().replace(" ", ""), name.replace("_", "")).ratio())


def rebuild(b, name, idx, cur, today):
    reg = b.get("thaifda") or {}
    recs = reg.get("records") or []
    if not recs:
        return None
    key = drug_key(name, recs)
    hits = {}
    for r in idx.get(key, []) if key else []:
        hits.setdefault(rid(r["license_id"]), r)
    out, seen, stat = [], set(), collections.Counter()
    for r in recs:
        k = rid(r.get("license_id"))
        if k in seen:
            continue
        seen.add(k)
        new = dict(r)
        if k in cur:
            if k in hits:
                h = hits[k]
                new.update({x: h[x] for x in ("kind", "dosage_form", "route", "atc") if h.get(x)})
            new["status"] = "active"
            if new.pop("cbg_not_listed", None):
                new.pop("license_status", None)
                stat["relisted"] += 1
            stat["kept_current"] += 1
        else:
            if not new.get("cbg_not_listed"):
                stat["not_listed_new"] += 1
            new["status"] = NOT_LISTED
            new["license_status"] = "cancelled"
            new["cbg_not_listed"] = new.get("cbg_not_listed") or today
            new.setdefault("kind", "single" if len(bundle_parts(r.get("ingredients"))) <= 1 else "combo")
            stat["not_listed"] += 1
        out.append(new)
    for k, h in hits.items():
        if k not in seen:
            out.append(dict(h, source=SOURCE))
            seen.add(k)
            stat["added"] += 1
    order = {("valid", "single"): 0, ("valid", "combo"): 1}
    out.sort(key=lambda r: (order.get(("cancelled" if r.get("license_status") == "cancelled" else "valid", r.get("kind") or "single"), 2),
                            r.get("brand_name_en") or ""))
    changed = out != recs or reg.get("total_matches") != len(out)
    reg["records"] = out
    reg["total_matches"] = len(out)
    reg["found"] = True
    b["thaifda"] = reg
    return {"key": key, "changed": changed, "total": len(out), "valid": sum(1 for r in out if r.get("license_status") != "cancelled"), **stat}


def main(argv):
    path = Path(argv[argv.index("--csv") + 1]) if "--csv" in argv else CSV
    today = argv[argv.index("--date") + 1] if "--date" in argv else date.today().isoformat()
    if "--download" in argv:
        import requests
        r = requests.get(URL, timeout=600)
        r.raise_for_status()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(r.content)
    idx, cur, n_rows = load_csv(path)
    rep, tot = [], collections.Counter()
    for f in sorted(BUNDLES.glob("*/drug_bundle.json")):
        b = json.loads(f.read_text(encoding="utf-8"))
        res = rebuild(b, f.parent.name, idx, cur, today)
        if res is None:
            tot["no_records"] += 1
            continue
        tot["bundles"] += 1
        tot.update({k: v for k, v in res.items() if type(v) is int and k not in ("total", "valid")})
        if res["changed"]:
            tot["changed"] += 1
            if "--dry-run" not in argv:
                f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
        rep.append((f.parent.name, res["key"] or "", res["total"], res["valid"], res.get("added", 0), res.get("not_listed", 0)))
    if "--report" in argv:
        Path(argv[argv.index("--report") + 1]).write_text(
            "bundle\tkey\ttotal\tvalid\tadded\tnot_listed\n" + "\n".join("\t".join(map(str, x)) for x in rep) + "\n", encoding="utf-8")
    print(f"CBG metadata.csv {n_rows} 筆（{path}）；證據包 {tot['bundles']} 個有紀錄（{tot['no_records']} 個沒有紀錄不動），"
          f"改 {tot['changed']} 個：新收 {tot['added']} 張、不在現行登記 {tot['not_listed']} 張（本次新標 {tot['not_listed_new']}）、"
          f"回到現行登記 {tot['relisted']} 張{'（dry-run，沒寫檔）' if '--dry-run' in argv else ''}")


if __name__ == "__main__":
    main(sys.argv[1:])
