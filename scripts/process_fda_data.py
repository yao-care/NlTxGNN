#!/usr/bin/env python3
"""Process Dutch medicine data (CBG-MEB) for NlTxGNN.

This script processes the geneesmiddeleninformatiebank.csv file and converts it
to the standard format expected by the TxGNN pipeline.
"""

import csv
import json
from pathlib import Path

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
OUTPUT_FILE = RAW_DATA_DIR / "nl_fda_drugs.json"


def process_dutch_data():
    """Process Dutch medicine CSV data."""
    csv_file = RAW_DATA_DIR / "geneesmiddeleninformatiebank.csv"
    
    if not csv_file.exists():
        print(f"Error: {csv_file} not found")
        print("Please run download_dutch_data.py first")
        return
    
    drugs = []
    seen_ingredients = set()
    
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            license_id = (row.get("registratienummer") or "").strip()
            brand_name = (row.get("productnaam") or "").strip()
            atc_code = (row.get("ATC") or "").strip()
            ingredient = (row.get("werkzame_stof") or "").strip()
            
            if not ingredient:
                continue
            
            # Normalize ingredient name
            ingredient_upper = ingredient.upper()
            
            # Skip duplicates
            key = f"{license_id}:{ingredient_upper}"
            if key in seen_ingredients:
                continue
            seen_ingredients.add(key)
            
            # Extract ATC name if present
            atc_name = ""
            if " - " in atc_code:
                atc_parts = atc_code.split(" - ", 1)
                atc_code = atc_parts[0].strip()
                atc_name = atc_parts[1].strip()
            
            drugs.append({
                "license_id": license_id,
                "brand_name": brand_name,
                "atc_code": atc_code,
                "atc_name": atc_name,
                "ingredients": [ingredient_upper],
                "indication": "",  # Not available in this dataset
                "status": "active",
            })
    
    # Save to JSON
    output = {
        "metadata": {
            "source": "CBG-MEB Geneesmiddeleninformatiebank",
            "country": "NL",
            "total_count": len(drugs),
        },
        "drugs": drugs,
    }
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"Processed {len(drugs)} drugs")
    print(f"Output saved to: {OUTPUT_FILE}")
    
    # Show sample
    print("\nSample drugs:")
    for drug in drugs[:5]:
        print(f"  - {drug['brand_name']}: {drug['ingredients']}")


if __name__ == "__main__":
    process_dutch_data()
