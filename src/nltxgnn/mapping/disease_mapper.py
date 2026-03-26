"""Disease mapping module - English indications to TxGNN disease ontology

Since Dutch drug data often contains English active ingredients,
we use English pattern matching similar to EuTxGNN.
Main function extracts disease keywords and maps to TxGNN disease IDs.
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd


# Dutch medicines often have English ingredient names
# We use English disease patterns for mapping
DISEASE_DICT: Dict[str, str] = {}


def load_disease_vocab(filepath: Optional[Path] = None) -> pd.DataFrame:
    """Load TxGNN disease vocabulary"""
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "disease_vocab.csv"
    return pd.read_csv(filepath)


def build_disease_index(disease_df: pd.DataFrame) -> Dict[str, Tuple[str, str]]:
    """Build disease name index (keyword -> (disease_id, disease_name))"""
    index = {}

    for _, row in disease_df.iterrows():
        disease_id = row["disease_id"]
        disease_name = row["disease_name"]
        name_upper = row["disease_name_upper"]

        # Full name
        index[name_upper] = (disease_id, disease_name)

        # Extract keywords (split by space and comma)
        keywords = re.split(r"[,\s\-]+", name_upper)
        for kw in keywords:
            kw = kw.strip()
            if len(kw) > 3 and kw not in index:
                index[kw] = (disease_id, disease_name)

    return index


def extract_indications(indication_str: str) -> List[str]:
    """Extract individual indications from indication text

    Dutch indications may be in Dutch or English format:
    "Behandeling van epilepsie bij volwassenen"
    "Treatment of epilepsy in adults"
    """
    if not indication_str:
        return []

    text = indication_str.strip()

    # Split by period, semicolon, or newlines
    parts = re.split(r"[.;\n]", text)

    indications = []
    for part in parts:
        part = part.strip()
        if part and len(part) >= 5:
            indications.append(part)

    return indications


def translate_indication(indication: str) -> List[str]:
    """Extract disease keywords from indication text

    Works with both Dutch and English text.
    """
    keywords = []

    # Common disease keyword patterns
    disease_patterns = [
        # Cancer
        r"\b(\w+\s+)?cancer\b",
        r"\b(\w+\s+)?carcinoma\b",
        r"\b(\w+\s+)?lymphoma\b",
        r"\b(\w+\s+)?leukemia\b",
        r"\b(\w+\s+)?melanoma\b",
        r"\b(\w+\s+)?myeloma\b",
        r"\b(\w+\s+)?tumor\b",
        r"\b(\w+\s+)?tumour\b",
        # Infections
        r"\b(\w+\s+)?infection\b",
        r"\b(hiv|aids)\b",
        r"\bhepatitis\s*[a-c]?\b",
        # Cardiovascular
        r"\bhypertension\b",
        r"\bheart\s+failure\b",
        r"\batrial\s+fibrillation\b",
        r"\bcoronary\s+artery\s+disease\b",
        # Neurological
        r"\bepilepsy\b",
        r"\bparkinson\b",
        r"\balzheimer\b",
        r"\bmultiple\s+sclerosis\b",
        r"\bmigraine\b",
        # Psychiatric
        r"\bdepression\b",
        r"\bschizophrenia\b",
        r"\bbipolar\b",
        r"\banxiety\b",
        # Metabolic/Endocrine
        r"\bdiabetes\b",
        r"\bobesity\b",
        r"\bhyperlipidemia\b",
        r"\bhypothyroidism\b",
        # Autoimmune/Rheumatic
        r"\brheumatoid\s+arthritis\b",
        r"\bpsoriasis\b",
        r"\blupus\b",
        r"\bcrohn\b",
        r"\bulcerative\s+colitis\b",
        # Respiratory
        r"\basthma\b",
        r"\bcopd\b",
        r"\bpulmonary\s+fibrosis\b",
        # Other
        r"\bhemophilia\b",
        r"\bcystic\s+fibrosis\b",
        r"\bosteoporosis\b",
        r"\bglaucoma\b",
    ]

    indication_lower = indication.lower()

    for pattern in disease_patterns:
        matches = re.findall(pattern, indication_lower)
        for match in matches:
            if isinstance(match, tuple):
                kw = " ".join(m for m in match if m).strip().upper()
            else:
                kw = match.strip().upper()
            if kw:
                keywords.append(kw)

    return keywords


def map_indication_to_disease(
    indication: str,
    disease_index: Dict[str, Tuple[str, str]],
) -> List[Tuple[str, str, float]]:
    """Map a single indication to TxGNN disease

    Returns:
        [(disease_id, disease_name, confidence), ...]
    """
    results = []

    # Extract disease keywords
    keywords = translate_indication(indication)

    # Also try direct search in indication text
    indication_upper = indication.upper()

    for kw in keywords:
        # Exact match
        if kw in disease_index:
            disease_id, disease_name = disease_index[kw]
            results.append((disease_id, disease_name, 1.0))
            continue

        # Partial match
        for index_kw, (disease_id, disease_name) in disease_index.items():
            if kw in index_kw or index_kw in kw:
                results.append((disease_id, disease_name, 0.8))

    # Additional: search for index keywords in indication text
    for index_kw, (disease_id, disease_name) in disease_index.items():
        if len(index_kw) > 5 and index_kw in indication_upper:
            results.append((disease_id, disease_name, 0.7))

    # Deduplicate and sort by confidence
    seen = set()
    unique_results = []
    for disease_id, disease_name, conf in sorted(results, key=lambda x: -x[2]):
        if disease_id not in seen:
            seen.add(disease_id)
            unique_results.append((disease_id, disease_name, conf))

    return unique_results[:5]


def map_fda_indications_to_diseases(
    fda_df: pd.DataFrame,
    disease_df: Optional[pd.DataFrame] = None,
    indication_field: str = "Indication",
    license_field: str = "License_Number",
    brand_field: str = "Product_Name",
) -> pd.DataFrame:
    """Map Dutch drug indications to TxGNN diseases"""
    if disease_df is None:
        disease_df = load_disease_vocab()

    disease_index = build_disease_index(disease_df)

    results = []

    for _, row in fda_df.iterrows():
        indication_str = row.get(indication_field, "")
        if not indication_str or pd.isna(indication_str):
            continue

        # Extract individual indications
        indications = extract_indications(str(indication_str))

        for ind in indications:
            # Map
            matches = map_indication_to_disease(ind, disease_index)

            if matches:
                for disease_id, disease_name, confidence in matches:
                    results.append({
                        "license_id": row.get(license_field, ""),
                        "brand_name": row.get(brand_field, ""),
                        "original_indication": str(indication_str)[:200],
                        "extracted_indication": ind[:100],
                        "disease_id": disease_id,
                        "disease_name": disease_name,
                        "confidence": confidence,
                    })
            else:
                results.append({
                    "license_id": row.get(license_field, ""),
                    "brand_name": row.get(brand_field, ""),
                    "original_indication": str(indication_str)[:200],
                    "extracted_indication": ind[:100],
                    "disease_id": None,
                    "disease_name": None,
                    "confidence": 0,
                })

    return pd.DataFrame(results)


def get_indication_mapping_stats(mapping_df: pd.DataFrame) -> dict:
    """Calculate indication mapping statistics"""
    total = len(mapping_df)
    mapped = mapping_df["disease_id"].notna().sum()
    unique_indications = mapping_df["extracted_indication"].nunique()
    unique_diseases = mapping_df[mapping_df["disease_id"].notna()]["disease_id"].nunique()

    return {
        "total_indications": total,
        "mapped_indications": int(mapped),
        "mapping_rate": mapped / total if total > 0 else 0,
        "unique_indications": unique_indications,
        "unique_diseases": unique_diseases,
    }
