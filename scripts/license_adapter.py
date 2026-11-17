"""NL（CBG-MEB Geneesmiddeleninformatiebank）下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：CBG 官方 https://www.geneesmiddeleninformatiebank.nl/metadata.csv（| 分隔，免金鑰）。
站上原本用的是第三方鏡像（data.openstate.eu，2026-10-30 已連不上），這裡改用 CBG 官方檔。
這份檔只列現行登記的產品、沒有狀態欄：在列＝status「active」（與證據包原值相同）；
新檔查不到的登記號保留原狀態、列在 summary（不推定為撤銷）。
2026-11-12 起每週排程先跑 scripts/rebuild_licenses_by_ingredient.py（依成分照現行登記補收、不在現行登記的標 Niet geregistreerd），再用本檔更新狀態。
登記號：SOORT（RVG／EU…）＋ REGISTRATIENUMMER 的「//」前段，例：RVG 126327；證據包 license_id 同格式（thaifda 區塊）。
2026-11-17（用戶要求確認查不到的許可證）：2026-11-16 排程「查不到」的 309 張（331 筆紀錄）就是 11-12 重建時已標
Niet geregistreerd（cbg_not_listed）的那批：2026-03 的 CBG 清單（data/raw/geneesmiddeleninformatiebank.csv）全部有，
11 月 metadata.csv 全部沒有，CBG 產品頁（https://www.geneesmiddeleninformatiebank.nl/nl/rvg<號>）逐號確認寫「Niet geregistreerd
geneesmiddel」。CBG 沒有另一份現行登記清單（metadata.csv 已含 RVG、EU 集中許可、RVH 順勢療法、平行輸入），所以沒有「在別份清單上」的號。
confirmed_absent(id)：metadata.csv 成功下載且現行登記號不少於 MIN_CURRENT 時，不在清單的 RVG／EU 號＝CBG 確認已不列，
排程不算「查不到」、不開 issue。標註（status＝Niet geregistreerd、license_status＝cancelled、cbg_not_listed＝第一次發現日）
由排程在本檔之前跑的 scripts/rebuild_licenses_by_ingredient.py 做（同一天的 metadata.csv），本檔不重複標；又出現在清單時 update() 恢復有效。
"""
import csv
import io
import time

import requests

RAW_FILE = "raw/cbg_metadata_ids.json"
# 2026-10-30 實測證據包 518 個登記號只有 40.5% 在 CBG 現行 metadata.csv（其餘可能已不在現行登記，未查證）；
# 用戶 2026-10-30 選「沿用現有來源排程」：涵蓋門檻 35%，查不到的保留原狀態、列在 summary 並開 issue 給人判斷。
COVER_MIN = 0.35
URL = "https://www.geneesmiddeleninformatiebank.nl/metadata.csv"
CURRENT: set = set()   # fetch() 填：metadata.csv 的現行登記號；空的就不做「確認已不列」判定
MIN_CURRENT = 15000    # 現行登記號少於這個數＝下載或格式有問題，不判定（2026-11-17 有 19,601 列）


def fetch():
    for attempt in range(4):
        try:
            r = requests.get(URL, timeout=600)
            r.raise_for_status()
            break
        except Exception:
            if attempt == 3:
                raise
            time.sleep(20 * (attempt + 1))
    rows = csv.DictReader(io.StringIO(r.content.decode("utf-8", "replace")), delimiter="|")
    if "REGISTRATIENUMMER" not in (rows.fieldnames or []) or "SOORT" not in (rows.fieldnames or []):
        raise RuntimeError(f"欄位改變：{rows.fieldnames}")
    out = []
    for x in rows:
        nr = (x["REGISTRATIENUMMER"] or "").split("//")[0].strip()
        if nr:
            out.append({"id": f"{(x['SOORT'] or '').strip()} {nr}".strip()})
    CURRENT.clear()
    if len({r["id"] for r in out}) >= MIN_CURRENT:
        CURRENT.update(r["id"] for r in out)
    return out


def confirmed_absent(lid):
    """給 license_refresh：metadata.csv 有成功下載、這個 RVG／EU 號不在現行登記＝CBG 確認已不列（產品頁寫 Niet geregistreerd）"""
    lid = " ".join(str(lid or "").split("//")[0].split())
    return bool(CURRENT) and lid.startswith(("RVG ", "EU/")) and lid not in CURRENT


def validate(new, old):
    p = []
    if len(new) < 10000:
        p.append(f"只解析出 {len(new)} 筆，疑似格式改變")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def status_index(new):
    return {r["id"]: "active" for r in new}


def record_id(rec):
    return " ".join(str(rec.get("license_id") or "").split("//")[0].split())


def update(rec, new):
    # 2026-11-12：rebuild_licenses_by_ingredient.py 標成不在現行登記（cbg_not_listed）的登記號回到現行清單時，恢復有效
    if rec.get("status") == new and not rec.get("cbg_not_listed"):
        return False
    rec["status"] = new
    if rec.pop("cbg_not_listed", None):
        rec.pop("license_status", None)
    return True
