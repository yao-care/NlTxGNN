#!/usr/bin/env python3
"""
Generate individual drug pages for Jekyll from repurposing predictions.

Creates markdown pages for each drug with predicted indications.

Output: docs/_drugs/{drug-slug}.md
"""

import pandas as pd
from datetime import datetime
from pathlib import Path

# Project configuration
PROJECT_ROOT = Path(__file__).parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
DRUGS_DIR = DOCS_DIR / "_drugs"
DATA_DIR = PROJECT_ROOT / "data" / "processed"

# Country-specific settings
COUNTRY_CODE = "Nl"
COUNTRY_NAME = "Netherlands"
LANGUAGE = "nl"
REGULATORY_AGENCY = "CBG-MEB"
SITE_URL = "https://nltxgnn.yao.care"


def slugify(text: str) -> str:
    """Convert text to URL-safe slug."""
    import re
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def generate_drug_page(drugbank_id: str, drug_name: str, indications: list) -> str:
    """Generate markdown content for a drug page."""
    slug = slugify(drugbank_id)

    content = f"""---
layout: default
nav_exclude: true
title: {drug_name}
drugbank_id: {drugbank_id}
evidence_level: L5
permalink: /drugs/{slug}/
---

# {drug_name}

## Basic Information

| Item | Value |
|------|-------|
| DrugBank ID | [{drugbank_id}](https://go.drugbank.com/drugs/{drugbank_id}) |
| Evidence Level | L5 (Computational Prediction) |
| Number of Predicted Indications | {len(indications)} |

## Predicted Indications (TxGNN)

The following are potential new indications predicted by the TxGNN model. Higher scores indicate higher predicted relevance.

| # | Indication | Source |
|---|------------|--------|
"""

    for i, ind in enumerate(indications[:50], 1):
        ind_name = ind.get("indication", "")
        source = ind.get("source", "KG")
        content += f"| {i} | {ind_name} | {source} |\n"

    if len(indications) > 50:
        content += f"\n*(Showing top 50 of {len(indications)} predictions)*\n"

    content += f"""
## Disclaimer

These predictions are for research purposes only and do not constitute medical advice.
Clinical validation is required before any clinical application.

---

[← Back to Drug Search](/drugs/)
"""

    return content


def main():
    print("=" * 60)
    print(f"NlTxGNN - Generate Drug Pages")
    print("=" * 60)
    print()

    # Load prediction data
    candidates_path = DATA_DIR / "integrated_predictions.csv.gz"

    if not candidates_path.exists():
        print(f"Error: {candidates_path} not found")
        print("Please run run_kg_prediction.py first")
        return

    print(f"1. Loading predictions from {candidates_path}...")
    # 檔案 33-307MB（gz），全載會吃掉數 GB 記憶體，改分塊讀並即時丟掉低信心列。
    # 只留 very_high / high：integrated_predictions 仍是藥 x 疾病的全展開，
    # confidence 是唯一能把它收斂成有意義預測的欄位。
    wanted = ['drugbank_id', 'disease_name', 'potential_indication', 'source',
              'drug_ingredient', 'confidence', 'dl_score']
    parts = []
    for chunk in pd.read_csv(candidates_path,
                             usecols=lambda x: x in wanted,
                             chunksize=500_000):
        if 'confidence' in chunk.columns:
            chunk = chunk[chunk['confidence'].isin(['very_high', 'high'])]
        parts.append(chunk)
    candidates = pd.concat(parts, ignore_index=True) if parts else pd.DataFrame()
    print(f"   Loaded {len(candidates)} high-confidence predictions")

    # 同一個藥同一個適應症會因多筆許可證重複出現，先去重
    if 'potential_indication' in candidates.columns:
        candidates = candidates.drop_duplicates(
            subset=['drugbank_id', 'potential_indication'])

    # very_high 優先；某個藥完全沒有 very_high 時才退回它的 high
    if 'confidence' in candidates.columns:
        vh = candidates[candidates['confidence'] == 'very_high']
        covered = set(vh['drugbank_id'])
        rest = candidates[(candidates['confidence'] == 'high')
                          & (~candidates['drugbank_id'].isin(covered))]
        candidates = pd.concat([vh, rest], ignore_index=True)
        print(f"   After confidence filter: {len(candidates)}")

    # 頁面只列前 50，先按分數排序，讓列出的是最相關的那些
    if 'dl_score' in candidates.columns:
        candidates = candidates.sort_values('dl_score', ascending=False)

    # Determine column names
    drug_col = "drugbank_id" if "drugbank_id" in candidates.columns else candidates.columns[0]
    indication_col = "potential_indication" if "potential_indication" in candidates.columns else "disease_name"
    has_source = "source" in candidates.columns

    print()
    print("2. Grouping by drug (optimized)...")

    # Get unique drugs efficiently
    unique_drugs = candidates[drug_col].dropna().unique()
    print(f"   Found {len(unique_drugs)} unique drugs")

    # Build drugs dictionary efficiently using groupby
    drugs = {}
    grouped = candidates.groupby(drug_col)

    for drug_id in unique_drugs:
        drug_id_str = str(drug_id)
        group = grouped.get_group(drug_id)

        # Get indications (limit to first 100 for efficiency)
        indications = []
        for _, row in group.head(100).iterrows():
            ind = row.get(indication_col, "")
            if pd.notna(ind):
                source = str(row.get("source", "KG")) if has_source and pd.notna(row.get("source")) else "KG"
                indications.append({"indication": str(ind), "source": source})

        # 原本寫死 drug_id_str，導致 title 只有 DrugBank ID
        drug_name = drug_id_str
        if "drug_ingredient" in group.columns:
            vals = group["drug_ingredient"].dropna()
            if len(vals) and str(vals.iloc[0]).strip():
                # 站內既有藥名頁的慣例是 Title Case（如 Alfentanil Hcl）
                drug_name = str(vals.iloc[0]).strip().title()

        drugs[drug_id_str] = {
            "name": drug_name,
            "indications": indications
        }

    # Create output directory
    DRUGS_DIR.mkdir(parents=True, exist_ok=True)

    print()
    print("3. Generating drug pages...")
    pages_created = 0
    for drug_id, drug_data in drugs.items():
        slug = slugify(drug_id)
        content = generate_drug_page(drug_id, drug_data["name"], drug_data["indications"])

        page_path = DRUGS_DIR / f"{slug}.md"
        with open(page_path, "w", encoding="utf-8") as f:
            f.write(content)
        pages_created += 1

    print(f"   Created {pages_created} drug pages")
    print()
    print("=" * 60)
    print("Done!")
    print(f"Output: {DRUGS_DIR}")


if __name__ == "__main__":
    main()
