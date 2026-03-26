# NlTxGNN - Netherlands Drug Repurposing Predictions

Drug repurposing predictions for medicines authorized in the Netherlands using TxGNN knowledge graph and deep learning models.

## Overview

NlTxGNN analyzes medicines registered with the Dutch College ter Beoordeling van Geneesmiddelen (CBG-MEB) and predicts potential new therapeutic indications based on:

- **TxGNN Knowledge Graph**: Relationships between drugs and diseases from biomedical knowledge bases
- **Deep Learning Model**: Neural network predictions based on drug-disease embeddings
- **Evidence Collection**: Clinical trials from ClinicalTrials.gov and literature from PubMed

## Data Source

Drug data is obtained from the [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/):
- CSV export via [Open State Foundation](https://data.openstate.eu/dataset/geneesmiddeleninformatiebank/)
- License: CC0 (Public Domain)

## Installation

```bash
# Clone the repository
git clone https://github.com/yao-care/NlTxGNN.git
cd NlTxGNN

# Install dependencies
uv sync

# Download TxGNN data
python scripts/download_data.py
```

## Usage

### 1. Download Dutch Drug Data

```bash
uv run python scripts/download_dutch_data.py
```

### 2. Prepare External Data

```bash
uv run python scripts/prepare_external_data.py
```

### 3. Run KG Prediction

```bash
uv run python scripts/run_kg_prediction.py
```

### 4. Run Deep Learning Prediction (optional)

```bash
source ~/miniforge3/bin/activate txgnn
PYTHONPATH=src python -m nltxgnn.predict.txgnn_model
```

## Project Structure

```
NlTxGNN/
├── data/
│   ├── raw/                    # Raw Dutch drug data
│   ├── processed/              # Prediction results
│   ├── external/               # TxGNN vocabularies
│   └── news/                   # News monitoring data
├── docs/                       # Jekyll website
├── prompts/                    # LLM report prompts
├── scripts/
│   ├── download_dutch_data.py  # Data download script
│   ├── prepare_external_data.py # Vocabulary extraction
│   ├── run_kg_prediction.py    # KG prediction
│   └── fetchers/               # News fetchers
└── src/nltxgnn/
    ├── data/                   # Data loading
    ├── mapping/                # DrugBank/disease mapping
    ├── predict/                # Prediction modules
    └── collectors/             # Evidence collectors
```

## Regulatory Agency

- **CBG-MEB**: College ter Beoordeling van Geneesmiddelen (Medicines Evaluation Board)
- **Website**: https://www.cbg-meb.nl/
- **Language**: Dutch / English

## Disclaimer

This project is for research purposes only and does not constitute medical advice. All drug repurposing predictions require clinical validation before any therapeutic application.

## License

MIT License

## Links

- Website: https://nltxgnn.yao.care/
- GitHub: https://github.com/yao-care/NlTxGNN
