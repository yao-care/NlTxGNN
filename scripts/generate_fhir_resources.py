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
        hash_suffix = hashlib.md5(raw_id.encode()).hexdigest()[:12]
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
                        "system": "http://purl.obolibrary.org/obo/mondo.owl",
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
    candidates_df = pd.read_csv(candidates_file)
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

    # Limit in KG-only mode
    if KG_ONLY_MODE and len(candidates_df) > MAX_CUD_RESOURCES:
        print(f"  KG-only mode: limiting to {MAX_CUD_RESOURCES} resources")
        candidates_df = candidates_df.head(MAX_CUD_RESOURCES)

    cud_count = 0
    for _, row in candidates_df.iterrows():
        drug_id = row['drugbank_id']
        disease_id = row['disease_id']
        disease_name = row.get('disease_name', disease_id)
        drug_name = drug_names.get(drug_id, drug_id)

        resource = create_clinical_use_definition(
            drug_id=drug_id,
            drug_name=drug_name,
            disease_id=disease_id,
            disease_name=disease_name,
            prediction_type="KG"
        )

        output_file = cud_dir / f"{resource['id']}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(resource, f, indent=2, ensure_ascii=False)
        cud_count += 1

        if cud_count % 10000 == 0:
            print(f"  Progress: {cud_count}/{len(candidates_df)}")

    print(f"  Generated: {cud_count} ClinicalUseDefinition resources")

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
