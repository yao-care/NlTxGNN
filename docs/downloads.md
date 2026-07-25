---
layout: default
title: Downloads
nav_order: 94
permalink: /downloads/
description: "Open data van NlTxGNN om te downloaden: FHIR-resources, voorspellingsresultaten en de zoekindex."
---

# Downloads

<div class="key-takeaway">
Voorspellingen worden gepubliceerd in FHIR R4-formaat, klaar voor integratie met EPD-systemen.
</div>

---

## FHIR-resources

Deze site publiceert voorspellingen als FHIR R4-resources, die rechtstreeks bruikbaar zijn voor SMART on FHIR-apps:

| Resource | Pad | Omschrijving |
|----------|------|-------------|
| CapabilityStatement | `/fhir/metadata` | Capability statement van de FHIR-server |
| MedicationKnowledge | `/fhir/MedicationKnowledge/` | Geneesmiddelresources |
| ClinicalUseDefinition | `/fhir/ClinicalUseDefinition/` | Voorspelde indicaties |
| Bundle | `/fhir/Bundle/all-predictions.json` | Alle voorspellingen gebundeld |

---

## Zoekindex

`/data/search-index.json` biedt een zoekindex van geneesmiddelen en indicaties waarmee u een eigen
zoekinterface kunt bouwen.

---

## Gebruiksvoorwaarden

<ol class="actionable-steps">
<li>De gegevens op deze site zijn <strong>uitsluitend bedoeld als naslagwerk voor onderzoek</strong> en mogen niet als basis voor medische beslissingen worden gebruikt.</li>
<li>Vermeld bij citeren NlTxGNN (藥提醒科技有限公司) en citeer het oorspronkelijke TxGNN-artikel.</li>
<li>Afgeleide gegevens blijven onderworpen aan de licentievoorwaarden van elke oorspronkelijke bron (zie <a href="{{ '/sources/' | relative_url }}">Gegevensbronnen</a>).</li>
</ol>

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
