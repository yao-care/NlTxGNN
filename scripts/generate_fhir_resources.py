#!/usr/bin/env python3
"""Generate FHIR R4 resources for NlTxGNN predictions.

This script generates MedicationKnowledge and ClinicalUseDefinition
resources for the Australia drug repurposing predictions.
"""

import json
import hashlib
from pathlib import Path
from datetime import datetime, timezone

import pandas as pd

# Australia-specific configuration
BASE_URL = "https://nltxgnn.yao.care"
JURISDICTION = "NL"
PUBLISHER = "yao.care"
VERSION = "0.1.0"

# KG-only mode limits ClinicalUseDefinition resources
KG_ONLY_MODE = True
MAX_CUD_RESOURCES = 50000


TOP_PER_DRUG = 50


def _indication_slug(text):
    """疾病名 -> URL/檔名安全的 slug。"""
    import re
    return re.sub(r"[^a-z0-9]+", "-", str(text).lower()).strip("-") or "unknown"


def _load_predictions(processed_dir):
    """載入預測，收斂成每個藥最多 TOP_PER_DRUG 筆。

    repurposing_candidates 在部分站是未過濾的 KG 笛卡爾積（每個藥配上整個疾病
    詞彙表），直接取前 N 列會讓資源全集中在少數幾個藥。改以 integrated_predictions
    為主，用 confidence 收斂（very_high 優先，某藥若無才退回其 high），
    再依 dl_score 排序。
    """
    import pandas as pd

    integrated = processed_dir / "integrated_predictions.csv.gz"
    candidates = processed_dir / "repurposing_candidates.csv.gz"

    if integrated.exists():
        wanted = ["drugbank_id", "potential_indication", "disease_name", "source",
                  "drug_ingredient", "confidence", "dl_score"]
        parts = []
        # 檔案可達數百 MB，分塊讀並即時丟掉低信心列
        for chunk in pd.read_csv(integrated, usecols=lambda c: c in wanted,
                                 chunksize=500_000):
            if "confidence" in chunk.columns:
                chunk = chunk[chunk["confidence"].isin(["very_high", "high"])]
            parts.append(chunk)
        df = pd.concat(parts, ignore_index=True) if parts else pd.DataFrame()
    else:
        df = pd.read_csv(candidates)

    if df.empty:
        return df

    ind_col = "potential_indication" if "potential_indication" in df.columns else "disease_name"
    df = df.dropna(subset=["drugbank_id", ind_col])
    df = df.drop_duplicates(subset=["drugbank_id", ind_col])

    if "confidence" in df.columns:
        vh = df[df["confidence"] == "very_high"]
        rest = df[(df["confidence"] == "high")
                  & (~df["drugbank_id"].isin(set(vh["drugbank_id"])))]
        df = pd.concat([vh, rest], ignore_index=True)
    if "dl_score" in df.columns:
        df = df.sort_values("dl_score", ascending=False)

    return df.groupby("drugbank_id", sort=False).head(TOP_PER_DRUG)


def create_medication_knowledge(drug_id: str, drug_name: str) -> dict:
    """Create a FHIR MedicationKnowledge resource."""
    return {
        "resourceType": "MedicationKnowledge",
        "id": drug_id.replace(":", "-"),
        "meta": {
            "profile": [
                "http://hl7.org/fhir/StructureDefinition/MedicationKnowledge"
            ],
            "lastUpdated": datetime.now(timezone.utc).isoformat()
        },
        "code": {
            "coding": [
                {
                    "system": "https://www.drugbank.ca",
                    "code": drug_id,
                    "display": drug_name
                }
            ],
            "text": drug_name
        },
        "status": "active",
        "manufacturer": {
            "display": "Various"
        },
        "jurisdiction": [
            {
                "coding": [
                    {
                        "system": "urn:iso:std:iso:3166",
                        "code": JURISDICTION,
                        "display": "Netherlands"
                    }
                ]
            }
        ]
    }


def create_clinical_use_definition(
    drug_id: str,
    drug_name: str,
    disease_id: str,
    disease_name: str,
    prediction_type: str = "KG"
) -> dict:
    """Create a FHIR ClinicalUseDefinition resource."""
    raw_id = f"{drug_id.replace(':', '-')}-{disease_id.replace(':', '-')}"
    # Truncate if too long (macOS max filename is 255 chars)
    if len(raw_id) > 200:
        hash_suffix = hashlib.sha256(raw_id.encode()).hexdigest()[:12]
        resource_id = f"{drug_id.replace(':', '-')}-{hash_suffix}"
    else:
        resource_id = raw_id

    return {
        "resourceType": "ClinicalUseDefinition",
        "id": resource_id,
        "meta": {
            "profile": [
                "http://hl7.org/fhir/StructureDefinition/ClinicalUseDefinition"
            ],
            "lastUpdated": datetime.now(timezone.utc).isoformat()
        },
        "type": "indication",
        "subject": [
            {
                "reference": f"MedicationKnowledge/{drug_id.replace(':', '-')}",
                "display": drug_name
            }
        ],
        "indication": {
            "diseaseSymptomProcedure": {
                "coding": [
                    {
                        # 舊版宣告 MONDO 卻填入 row index，改用站內 CodeSystem
                        "system": f"{BASE_URL}/fhir/CodeSystem/predicted-indication",
                        "code": disease_id,
                        "display": disease_name
                    }
                ],
                "text": disease_name
            }
        },
        "extension": [
            {
                "url": f"{BASE_URL}/fhir/StructureDefinition/prediction-source",
                "valueString": f"TxGNN-{prediction_type}"
            },
            {
                "url": f"{BASE_URL}/fhir/StructureDefinition/research-only",
                "valueBoolean": True
            }
        ]
    }


def main():
    print("=" * 60)
    print("NlTxGNN - Generate FHIR R4 Resources")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    processed_dir = base_dir / "data" / "processed"
    fhir_dir = base_dir / "docs" / "fhir"

    # Check for prediction data
    candidates_file = processed_dir / "repurposing_candidates.csv.gz"
    drug_mapping_file = processed_dir / "drug_mapping.csv"

    if not candidates_file.exists():
        print("Error: repurposing_candidates.csv not found")
        print("Please run run_kg_prediction.py first")
        return

    # Load data
    print("Loading prediction data...")
    candidates_df = _load_predictions(processed_dir)
    print(f"  Candidates: {len(candidates_df)}")

    # Load drug mapping for names
    drug_names = {}
    if drug_mapping_file.exists():
        drug_mapping_df = pd.read_csv(drug_mapping_file)
        for _, row in drug_mapping_df.iterrows():
            if pd.notna(row.get('drugbank_id')):
                drug_names[row['drugbank_id']] = row.get('中文品名', row['drugbank_id'])

    # Create output directories
    mk_dir = fhir_dir / "MedicationKnowledge"
    cud_dir = fhir_dir / "ClinicalUseDefinition"
    mk_dir.mkdir(parents=True, exist_ok=True)
    cud_dir.mkdir(parents=True, exist_ok=True)

    # Generate MedicationKnowledge resources
    print()
    print("Generating MedicationKnowledge resources...")
    unique_drugs = candidates_df['drugbank_id'].unique()
    mk_count = 0

    for drug_id in unique_drugs:
        drug_name = drug_names.get(drug_id, drug_id)
        resource = create_medication_knowledge(drug_id, drug_name)

        output_file = mk_dir / f"{drug_id.replace(':', '-')}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(resource, f, indent=2, ensure_ascii=False)
        mk_count += 1

    print(f"  Generated: {mk_count} MedicationKnowledge resources")

    # Generate ClinicalUseDefinition resources
    print()
    print("Generating ClinicalUseDefinition resources...")

    # _load_predictions 已將每個藥收斂到 TOP_PER_DRUG 筆；
    # 這裡只留總量上限當保險，不再用 head() 截斷（會讓資源集中在少數幾個藥）。
    if len(candidates_df) > MAX_CUD_RESOURCES:
        print(f"  Warning: {len(candidates_df)} > {MAX_CUD_RESOURCES}, 請調整 TOP_PER_DRUG")

    # 重建目錄，避免上一版留下的資源變成孤兒
    import shutil
    if cud_dir.exists():
        shutil.rmtree(cud_dir)
    cud_dir.mkdir(parents=True, exist_ok=True)

    cud_count = 0
    _used_stems = set()
    _cud_collisions = 0
    for _, row in candidates_df.iterrows():
        drug_id = row['drugbank_id']
        # 候選檔沒有 disease_id 欄位，原本直接取會 KeyError；
        # 改用適應症名稱，並以其 slug 當識別碼
        disease_name = row.get('potential_indication') or row.get('disease_name') or ''
        if not disease_name:
            continue
        disease_id = _indication_slug(disease_name)
        drug_name = drug_names.get(drug_id, drug_id)

        resource = create_clinical_use_definition(
            drug_id=drug_id,
            drug_name=drug_name,
            disease_id=disease_id,
            disease_name=disease_name,
            prediction_type="KG"
        )

        # 標點不同的適應症可能 slug 相同，不處理會讓後者覆蓋前者而靜默少檔
        _stem = resource['id']
        if _stem in _used_stems:
            _cud_collisions += 1
            _n = 2
            while f"{_stem}-{_n}" in _used_stems:
                _n += 1
            _stem = f"{_stem}-{_n}"
            resource['id'] = _stem
        _used_stems.add(_stem)

        output_file = cud_dir / f"{_stem}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(resource, f, indent=2, ensure_ascii=False)
        cud_count += 1

        if cud_count % 10000 == 0:
            print(f"  Progress: {cud_count}/{len(candidates_df)}")

    print(f"  Generated: {cud_count} ClinicalUseDefinition resources"
          f"（slug 碰撞另加後綴 {_cud_collisions} 筆）")

    # Generate CapabilityStatement
    print()
    print("Generating CapabilityStatement...")
    capability = {
        "resourceType": "CapabilityStatement",
        "id": "nltxgnn-server",
        "url": f"{BASE_URL}/fhir/metadata",
        "version": VERSION,
        "name": "NlTxGNNServer",
        "title": "NlTxGNN FHIR Server",
        "status": "active",
        "experimental": True,
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "publisher": PUBLISHER,
        "description": "FHIR R4 server for Australia drug repurposing predictions using TxGNN",
        "jurisdiction": [
            {
                "coding": [
                    {
                        "system": "urn:iso:std:iso:3166",
                        "code": JURISDICTION,
                        "display": "Netherlands"
                    }
                ]
            }
        ],
        "kind": "instance",
        "fhirVersion": "4.0.1",
        "format": ["json"],
        "rest": [
            {
                "mode": "server",
                "resource": [
                    {
                        "type": "MedicationKnowledge",
                        "profile": "http://hl7.org/fhir/StructureDefinition/MedicationKnowledge",
                        "interaction": [
                            {"code": "read"},
                            {"code": "search-type"}
                        ]
                    },
                    {
                        "type": "ClinicalUseDefinition",
                        "profile": "http://hl7.org/fhir/StructureDefinition/ClinicalUseDefinition",
                        "interaction": [
                            {"code": "read"},
                            {"code": "search-type"}
                        ]
                    }
                ]
            }
        ]
    }

    with open(fhir_dir / "metadata.json", 'w', encoding='utf-8') as f:
        json.dump(capability, f, indent=2, ensure_ascii=False)

    print()
    print("=" * 60)
    print("Complete!")
    print("=" * 60)
    print()
    print(f"Output directory: {fhir_dir}")
    print(f"  MedicationKnowledge: {mk_count}")
    print(f"  ClinicalUseDefinition: {cud_count}")


if __name__ == "__main__":
    main()
