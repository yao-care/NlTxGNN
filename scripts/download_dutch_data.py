#!/usr/bin/env python3
"""Download Dutch medicine data from CBG-MEB Geneesmiddeleninformatiebank.

Data source: https://data.openstate.eu/dataset/geneesmiddeleninformatiebank/
License: CC0 (Public Domain)

Usage:
    uv run python scripts/download_dutch_data.py

Output:
    data/raw/geneesmiddeleninformatiebank.csv
"""

import sys
from pathlib import Path

import requests


# CSV download URL from Open State Foundation
DATA_URL = "https://data.openstate.eu/dataset/2e0055db-6f28-4b05-920b-a648ba026baa/resource/1efaa651-add9-40f5-8b0c-2c2f2d352e11/download/geneesmiddeleninformatiebank.csv"


def download_file(url: str, output_path: Path, chunk_size: int = 8192) -> bool:
    """Download a file with progress indication."""
    try:
        print(f"Downloading from: {url}")
        print(f"Saving to: {output_path}")

        headers = {
            "User-Agent": "NlTxGNN/1.0 (Drug Repurposing Research Project)"
        }

        response = requests.get(url, headers=headers, stream=True, timeout=60)
        response.raise_for_status()

        total_size = int(response.headers.get("content-length", 0))
        downloaded = 0

        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size:
                        pct = downloaded / total_size * 100
                        print(f"\r  Progress: {downloaded:,} / {total_size:,} bytes ({pct:.1f}%)", end="")

        print()  # New line after progress
        return True

    except requests.RequestException as e:
        print(f"Error downloading file: {e}")
        return False


def main():
    print("=" * 60)
    print("Download Dutch Medicine Data (CBG-MEB)")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    raw_dir = base_dir / "data" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    output_path = raw_dir / "geneesmiddeleninformatiebank.csv"

    # Check if file already exists
    if output_path.exists():
        print(f"File already exists: {output_path}")
        print("To re-download, delete the existing file first.")
        return

    # Download the data
    print("Downloading Dutch medicine database...")
    print()

    success = download_file(DATA_URL, output_path)

    if success:
        # Verify file size
        file_size = output_path.stat().st_size
        print()
        print("=" * 60)
        print("Download Complete!")
        print("=" * 60)
        print(f"  File: {output_path}")
        print(f"  Size: {file_size:,} bytes ({file_size / 1024 / 1024:.2f} MB)")
        print()
        print("Next step: Run data processing")
        print("  uv run python scripts/prepare_external_data.py")
    else:
        print()
        print("Download failed. Please check your internet connection.")
        sys.exit(1)


if __name__ == "__main__":
    main()
