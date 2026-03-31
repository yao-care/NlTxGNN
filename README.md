# NlTxGNN - Nederland: Herpositionering van Geneesmiddelen

[![Website](https://img.shields.io/badge/Website-nltxgnn.yao.care-blue)](https://nltxgnn.yao.care)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Voorspellingen voor herpositionering van geneesmiddelen (drug repurposing) voor Nederland met behulp van het TxGNN-model.

## Disclaimer

- De resultaten van dit project zijn uitsluitend bedoeld voor onderzoeksdoeleinden en vormen geen medisch advies.
- Kandidaten voor herpositionering van geneesmiddelen vereisen klinische validatie voor toepassing.

## Projectoverzicht

| Onderdeel | Aantal |
|-----------|--------|
| **Geneesmiddelrapporten** | 145 |
| **Totale Voorspellingen** | 2,473,755 |

## Voorspellingsmethoden

### Kennisgrafiekmethode (Knowledge Graph)
Directe bevraging van geneesmiddel-ziekterelaties in de TxGNN-kennisgrafiek, identificatie van potentiele herpositioneringskandidaten op basis van bestaande verbindingen in het biomedische netwerk.

### Deep Learning-methode
Maakt gebruik van het voorgetrainde neurale netwerkmodel van TxGNN om voorspellingsscores te berekenen, waarbij de waarschijnlijkheid van nieuwe therapeutische indicaties voor goedgekeurde geneesmiddelen wordt beoordeeld.

## Links

- Website: https://nltxgnn.yao.care
- TxGNN-publicatie: https://doi.org/10.1038/s41591-023-02233-x
