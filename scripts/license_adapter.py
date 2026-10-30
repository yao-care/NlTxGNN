"""NL（CBG-MEB Geneesmiddeleninformatiebank）下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：CBG 官方 https://www.geneesmiddeleninformatiebank.nl/metadata.csv（| 分隔，免金鑰）。
站上原本用的是第三方鏡像（data.openstate.eu，2026-10-30 已連不上），這裡改用 CBG 官方檔。
這份檔只列現行登記的產品、沒有狀態欄：在列＝status「active」（與證據包原值相同）；
新檔查不到的登記號保留原狀態、列在 summary（不推定為撤銷）。
登記號：SOORT（RVG／EU…）＋ REGISTRATIENUMMER 的「//」前段，例：RVG 126327；證據包 license_id 同格式（thaifda 區塊）。
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
    return out


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
    if rec.get("status") == new:
        return False
    rec["status"] = new
    return True
