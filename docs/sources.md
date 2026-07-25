---
layout: default
title: Gegevensbronnen
nav_order: 93
permalink: /sources/
description: "De gegevensbronnen achter NlTxGNN: registratiegegevens van CBG-MEB, TxGNN, ClinicalTrials.gov, PubMed en DrugBank."
---

# Gegevensbronnen

<div class="key-takeaway">
Elke conclusie is te herleiden tot een openbare gegevensbron — niets is een black box.
</div>

---

## Overzicht van de bronnen

<table class="comparison-table">
<thead>
<tr><th>Type</th><th>Bron</th><th>Gebruikt voor</th></tr>
</thead>
<tbody>
<tr><td>Registratiegegevens</td><td><a href="https://www.cbg-meb.nl/">CBG-MEB</a></td><td>Lijst van goedgekeurde geneesmiddelen en werkzame stoffen in Nederland</td></tr>
<tr><td>Voorspellingsmodel</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Voorspelling van verbanden tussen geneesmiddel en ziekte</td></tr>
<tr><td>Klinische studies</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Bewijsgradering (NCT)</td></tr>
<tr><td>Literatuur</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Bewijsgradering (PMID)</td></tr>
<tr><td>Geneesmiddelinformatie</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Koppeling van werkzame stoffen en gegevens over aangrijpingspunten</td></tr>
<tr><td>Interacties</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>Gegevens over interacties tussen geneesmiddelen</td></tr>
</tbody>
</table>

---

## Licenties

Elke bron heeft zijn eigen licentie — controleer deze voordat u citeert:

- **TxGNN**: academisch gebruik; citeer Huang et al. (2023)
- **ClinicalTrials.gov / PubMed**: openbare gegevens van de Amerikaanse NIH
- **DrugBank**: niet-commercieel gebruik, onder de eigen licentievoorwaarden
- **CBG-MEB**: onder de opendatavoorwaarden van de Nederlandse registratieautoriteit

---

## Updatefrequentie

| Gegevens | Frequentie |
|------|-----------|
| Registratiegegevens | Zoals gepubliceerd door de registratieautoriteit |
| Bewijs uit studies / literatuur | Periodiek opnieuw verzameld |
| Interactiegegevens | Elk kwartaal beoordeeld |

---

## Wetenschappelijke citatie

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

---

## Over de ontwikkelaar

Dit platform wordt ontwikkeld en beheerd door **藥提醒科技有限公司** (yao.care, inschrijvingsnummer
83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

NlTxGNN is de Nederlandse site van de productlijn "TxGNN Drug Repurposing" van het bedrijf.
Hetzelfde systeem is uitgerold in 30 landen en regio's, elk met de naam `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN, enzovoort) op `{cc}txgnn.yao.care`.
Productoverzicht: <https://www.yao.care/medical/txgnn/>.

Het TxGNN-model zelf is ontwikkeld door het Zitnik Lab van Harvard Medical School en gepubliceerd
in *Nature Medicine*. Dit platform is het productiesysteem dat 藥提醒科技有限公司 op dat model heeft
gebouwd; het omvat de integratie van nationale geneesmiddelregistratiegegevens, dubbele voorspelling
met kennisgraaf en deep learning, bewijsgradering op basis van PubMed / ClinicalTrials, en integratie
met elektronische patiëntendossiers via SMART on FHIR.

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
Dit rapport is uitsluitend bedoeld als naslagwerk voor wetenschappelijk onderzoek en <strong>vormt geen medisch advies</strong>. Volg altijd de aanwijzingen van uw arts op; pas nooit op eigen initiatief uw medicatie aan. Elke beslissing over geneesmiddelherpositionering vereist volledige klinische validatie en toetsing door de registratieautoriteit.
<br><br>
<small>Beoordeeld door: 藥提醒科技有限公司 (yao.care)</small>
</div>
