#!/usr/bin/env python3
"""Dutch CBG-MEB drug data loader.

This module loads drug data from the Dutch Medicines Evaluation Board (CBG-MEB)
via the Geneesmiddeleninformatiebank dataset.

Data source: https://data.openstate.eu/dataset/geneesmiddeleninformatiebank/
"""

import json
import re
from pathlib import Path
from typing import Optional

import pandas as pd


def load_dutch_csv(filepath: Path) -> pd.DataFrame:
    """Load Dutch medicines CSV file.

    Args:
        filepath: Path to geneesmiddeleninformatiebank.csv

    Returns:
        DataFrame with Dutch medicines data
    """
    # The CSV may have varying encoding, try utf-8 first
    # Use on_bad_lines='skip' to handle incomplete downloads
    try:
        df = pd.read_csv(filepath, encoding="utf-8", low_memory=False, on_bad_lines="skip")
    except UnicodeDecodeError:
        df = pd.read_csv(filepath, encoding="latin-1", low_memory=False, on_bad_lines="skip")

    return df


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize column names for consistency.

    Dutch column names from Geneesmiddeleninformatiebank:
    - RVG_nummer: Registration number
    - Productnaam: Product name
    - Werkzame_stof: Active substance(s)
    - Farmaceutische_vorm: Dosage form
    - Sterkte: Strength
    - Houder: Marketing authorization holder
    - ATC_code: ATC code
    - Status: Authorization status
    """
    # Normalize column names (remove spaces, lowercase)
    df.columns = [col.strip() for col in df.columns]

    # Map Dutch column names to standard names
    # First, detect the actual column names in the file
    column_map = {}

    for col in df.columns:
        col_lower = col.lower()
        if "rvg" in col_lower or "nummer" in col_lower or "registratienummer" in col_lower:
            column_map[col] = "License_Number"
        elif "productnaam" in col_lower or "naam" in col_lower or "merknaam" in col_lower:
            column_map[col] = "Product_Name"
        elif "werkzame" in col_lower or "stof" in col_lower or "ingredient" in col_lower:
            column_map[col] = "Active_Ingredients"
        elif "farmaceutische" in col_lower or "vorm" in col_lower or "dosage" in col_lower:
            column_map[col] = "Dosage_Form"
        elif "sterkte" in col_lower or "strength" in col_lower:
            column_map[col] = "Strength"
        elif "houder" in col_lower or "holder" in col_lower or "fabrikant" in col_lower:
            column_map[col] = "Manufacturer"
        elif "atc" in col_lower:
            column_map[col] = "ATC_Code"
        elif "status" in col_lower:
            column_map[col] = "Status"
        elif "indicatie" in col_lower or "indication" in col_lower:
            column_map[col] = "Indication"

    if column_map:
        df = df.rename(columns=column_map)

    return df


def extract_ingredient_from_name(name: str) -> str:
    """Extract active ingredient from medicine name.

    Dutch medicine names may follow patterns like:
    - "Paracetamol 500 mg tabletten"
    - "Metformine HCl 850 mg"
    """
    if pd.isna(name):
        return ""

    name = str(name)

    # Remove dosage patterns like "500 mg", "10 ml", etc.
    name = re.sub(r"\s+\d+[\.,]?\d*\s*(mg|ml|mcg|g|iu|%).*$", "", name, flags=re.IGNORECASE)

    # Remove content in parentheses
    name = re.sub(r"\s*\([^)]*\)", "", name)

    # Remove common form suffixes
    form_suffixes = [
        "tabletten", "capsules", "injectie", "siroop", "crème", "zalf",
        "oplossing", "filmomhulde", "tablet", "capsule", "injection",
        "cream", "ointment", "solution", "film-coated", "retard"
    ]
    for suffix in form_suffixes:
        name = re.sub(rf"\s+{suffix}.*$", "", name, flags=re.IGNORECASE)

    # Clean up
    name = name.strip()

    return name


def load_fda_drugs(filepath: Optional[Path] = None) -> pd.DataFrame:
    """Load and process Dutch drug data.

    This is the main entry point, compatible with the standard TxGNN interface.

    Args:
        filepath: Optional path to Dutch data file. If not provided,
                  looks for data in standard locations.

    Returns:
        DataFrame with columns:
            - License_Number: Marketing Authorization number
            - Product_Name: Drug product name
            - Active_Ingredients: Active ingredients
    """
    base_dir = Path(__file__).parent.parent.parent.parent
    data_dir = base_dir / "data"
    raw_dir = data_dir / "raw"

    # First, try to load from processed JSON (nl_fda_drugs.json)
    json_file = raw_dir / "nl_fda_drugs.json"
    if json_file.exists():
        print(f"Loading Dutch medicines from JSON: {json_file}")
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        drugs = data.get("drugs", [])
        df = pd.DataFrame(drugs)

        # Map JSON fields to standard columns
        if "license_id" in df.columns:
            df["License_Number"] = df["license_id"]
        if "brand_name" in df.columns:
            df["Product_Name"] = df["brand_name"]
        if "ingredients" in df.columns:
            df["Active_Ingredients"] = df["ingredients"].apply(
                lambda x: x[0] if isinstance(x, list) and len(x) > 0 else (x if isinstance(x, str) else "")
            )
            df["ingredients"] = df["Active_Ingredients"]
            df["brand_name"] = df.get("Product_Name", "")

        print(f"  Total medicines: {len(df)}")
        print(f"  Unique ingredients: {df['Active_Ingredients'].nunique()}")

        # Remove duplicates by ingredient
        df = df[df["Active_Ingredients"].notna() & (df["Active_Ingredients"] != "")]
        df = df.drop_duplicates(subset=["Active_Ingredients"]).reset_index(drop=True)

        return df

    # Fallback: Try to find Dutch CSV file
    if filepath is None:
        possible_files = [
            raw_dir / "geneesmiddeleninformatiebank.csv",
            raw_dir / "dutch_medicines.csv",
            data_dir / "geneesmiddeleninformatiebank.csv",
        ]

        for f in possible_files:
            if f.exists():
                filepath = f
                break

    if filepath is None or not filepath.exists():
        print("Warning: No Dutch medicines data found.")
        print("Please run: uv run python scripts/download_dutch_data.py")
        print("Expected file: data/raw/geneesmiddeleninformatiebank.csv")
        return pd.DataFrame(columns=["License_Number", "Product_Name", "Active_Ingredients"])

    print(f"Loading Dutch medicines from CSV: {filepath}")

    # Load and process CSV
    df = load_dutch_csv(filepath)
    print(f"  Raw records: {len(df)}")
    print(f"  Columns: {list(df.columns)}")

    df = normalize_columns(df)

    # Use Active_Ingredients if available, otherwise extract from product name
    if "Active_Ingredients" in df.columns:
        df["Active_Ingredients"] = df["Active_Ingredients"].fillna("")
        # For empty ingredients, try to extract from product name
        if "Product_Name" in df.columns:
            mask = df["Active_Ingredients"] == ""
            df.loc[mask, "Active_Ingredients"] = df.loc[mask, "Product_Name"].apply(extract_ingredient_from_name)
    elif "Product_Name" in df.columns:
        # Fallback: extract from medicine names
        df["Active_Ingredients"] = df["Product_Name"].apply(extract_ingredient_from_name)
    else:
        df["Active_Ingredients"] = ""

    # Also add to 'ingredients' column for compatibility
    df["ingredients"] = df["Active_Ingredients"]
    if "Product_Name" in df.columns:
        df["brand_name"] = df["Product_Name"]

    # Ensure required columns exist
    required_cols = ["License_Number", "Product_Name", "Active_Ingredients"]
    for col in required_cols:
        if col not in df.columns:
            df[col] = ""

    # Remove duplicates by ingredient
    df = df[df["Active_Ingredients"].notna() & (df["Active_Ingredients"] != "")]
    df = df.drop_duplicates(subset=["Active_Ingredients"]).reset_index(drop=True)

    print(f"  Total medicines: {len(df)}")
    print(f"  Unique ingredients: {df['Active_Ingredients'].nunique()}")

    return df


def filter_active_drugs(df: pd.DataFrame) -> pd.DataFrame:
    """Filter active drugs with valid ingredients.

    Args:
        df: Drug DataFrame

    Returns:
        Filtered DataFrame
    """
    col = "Active_Ingredients" if "Active_Ingredients" in df.columns else "ingredients"
    active = df[df[col].notna() & (df[col] != "")].copy()

    # If Status column exists, filter for active status
    if "Status" in df.columns:
        # Dutch status terms for active medicines
        active_statuses = ["actief", "active", "geregistreerd", "registered", "geldig", "valid"]
        # Only filter if we can identify status patterns
        status_col = df["Status"].str.lower().fillna("")
        has_active_status = status_col.str.contains("|".join(active_statuses), na=False)
        if has_active_status.any():
            active = active[has_active_status]

    active = active.reset_index(drop=True)
    return active


def get_drug_summary(df: pd.DataFrame) -> dict:
    """Get drug data summary statistics.

    Args:
        df: Drug DataFrame

    Returns:
        Summary statistics dictionary
    """
    all_ingredients = set()
    ing_col = "Active_Ingredients" if "Active_Ingredients" in df.columns else "ingredients"
    name_col = "Product_Name" if "Product_Name" in df.columns else "brand_name"

    for ing_str in df[ing_col].dropna():
        all_ingredients.add(str(ing_str).strip())

    return {
        "total_count": len(df),
        "with_ingredient": df[ing_col].notna().sum(),
        "unique_products": df[name_col].nunique() if name_col in df.columns else 0,
        "unique_ingredients": len(all_ingredients),
    }


def get_unique_ingredients(df: pd.DataFrame) -> list[str]:
    """Extract unique ingredients from loaded data."""
    all_ingredients = []

    col = "Active_Ingredients" if "Active_Ingredients" in df.columns else "ingredients"
    for ing_str in df[col].dropna():
        all_ingredients.append(str(ing_str).strip())

    return sorted(set(all_ingredients))


if __name__ == "__main__":
    # Test loading
    df = load_fda_drugs()
    print(f"\nLoaded {len(df)} drugs")

    if len(df) > 0:
        ingredients = get_unique_ingredients(df)
        print(f"Unique ingredients: {len(ingredients)}")
        print(f"\nSample ingredients: {ingredients[:10]}")
