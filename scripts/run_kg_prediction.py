#!/usr/bin/env python3
"""Run Knowledge Graph predictions - Netherlands version

Uses TxGNN knowledge graph for drug repurposing predictions.

Usage:
    uv run python scripts/run_kg_prediction.py

Prerequisites:
    1. Downloaded Dutch data (data/raw/geneesmiddeleninformatiebank.csv)
    2. Ran prepare_external_data.py

Output files:
    data/processed/drug_mapping.csv
    data/processed/repurposing_candidates.csv
"""

from pathlib import Path

import pandas as pd

from nltxgnn.data.loader import load_fda_drugs, filter_active_drugs, get_drug_summary
from nltxgnn.mapping.drugbank_mapper import map_fda_drugs_to_drugbank
from nltxgnn.predict.repurposing import load_drug_disease_relations


def main():
    print("=" * 60)
    print("NlTxGNN - Knowledge Graph Prediction")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent

    # 1. Load drug data
    print("1. Loading Netherlands drug data...")
    fda_df = load_fda_drugs()
    active_df = filter_active_drugs(fda_df)
    summary = get_drug_summary(active_df)
    print(f"   Total drugs: {summary['total_count']}")
    print(f"   With ingredients: {summary['with_ingredient']}")
    print(f"   Unique ingredients: {summary['unique_ingredients']}")

    # 2. DrugBank mapping
    print()
    print("2. Running DrugBank mapping...")
    # Prepare DataFrame with mapper column names (using Taiwan-style column names for compatibility)
    mapper_df = active_df.rename(columns={
        'License_Number': '許可證字號',
        'Product_Name': '中文品名',
        'Active_Ingredients': '主成分略述'
    })
    drug_mapping = map_fda_drugs_to_drugbank(mapper_df)
    mapped_count = drug_mapping['drugbank_id'].notna().sum()
    total_count = len(drug_mapping)
    mapping_rate = mapped_count/total_count*100 if total_count > 0 else 0
    print(f"   Mapped successfully: {mapped_count}/{total_count} ({mapping_rate:.1f}%)")

    # Save drug mapping
    output_dir = base_dir / "data" / "processed"
    output_dir.mkdir(parents=True, exist_ok=True)
    drug_mapping.to_csv(output_dir / "drug_mapping.csv", index=False)
    print(f"   Saved drug mapping: {output_dir / 'drug_mapping.csv'}")

    # 3. Find repurposing candidates
    print()
    print("3. Finding repurposing candidates...")
    print("   (Generating all possible drug-disease pairs)")

    # Load drug-disease relations
    relations_df = load_drug_disease_relations()

    # Get successfully mapped unique drugs
    mapped_drugs = drug_mapping[drug_mapping['drugbank_id'].notna()]['drugbank_id'].unique()
    print(f"   Mapped unique drugs: {len(mapped_drugs)}")

    # Load disease vocabulary
    diseases_df = pd.read_csv(base_dir / "data" / "external" / "disease_vocab.csv")
    diseases = diseases_df['disease_id'].unique()
    print(f"   Diseases in TxGNN: {len(diseases)}")

    # Get known drug-disease relations (x_id = drug, y_id = disease)
    known_relations = set(zip(relations_df['x_id'], relations_df['y_id']))

    # Build drugbank_id -> drug info mapping
    drug_info = drug_mapping[drug_mapping['drugbank_id'].notna()].drop_duplicates(subset=['drugbank_id'])
    drug_info_map = {}
    for _, row in drug_info.iterrows():
        drug_info_map[row['drugbank_id']] = {
            'license_id': row.get('license_id', row.get('許可證字號', '')),
            'brand_name': row.get('brand_name', row.get('中文品名', '')),
            'drug_ingredient': row.get('normalized_ingredient', row.get('標準化成分', '')),
        }

    # Generate candidate pairs (excluding known relations)
    disease_name_map = dict(zip(diseases_df['disease_id'], diseases_df['disease_name']))
    candidates_list = []
    for drug in mapped_drugs:
        info = drug_info_map.get(drug, {})
        for disease in diseases:
            if (drug, disease) not in known_relations:
                candidates_list.append({
                    'license_id': info.get('license_id', ''),
                    'brand_name': info.get('brand_name', ''),
                    'drug_ingredient': info.get('drug_ingredient', ''),
                    'drugbank_id': drug,
                    'potential_indication': disease_name_map.get(disease, disease),
                    'source': 'TxGNN Knowledge Graph',
                })

    candidates = pd.DataFrame(candidates_list)
    print(f"   Candidates: {len(candidates)}")
    print(f"   Drugs involved: {candidates['drugbank_id'].nunique()}")
    print(f"   Potential new indications: {candidates['potential_indication'].nunique()}")

    # 4. Save results
    print()
    print("4. Saving results...")
    candidates.to_csv(output_dir / "repurposing_candidates.csv.gz", index=False)
    print(f"   Saved to: {output_dir / 'repurposing_candidates.csv.gz'}")

    print()
    print("=" * 60)
    print("Complete!")
    print("=" * 60)
    print()
    print("Summary:")
    print(f"  - NL registered medicines: {summary['total_count']}")
    print(f"  - DrugBank mapped: {mapped_count}")
    print(f"  - Mapping rate: {mapping_rate:.1f}%")
    print(f"  - Repurposing candidates: {len(candidates)}")
    print()
    print("Next step: Run deep learning prediction")
    print("  source ~/miniforge3/bin/activate txgnn")
    print("  PYTHONPATH=src python -m nltxgnn.predict.txgnn_model")


if __name__ == "__main__":
    main()
