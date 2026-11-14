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

<!-- site-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
## Nederland: gegevens van deze site

Deze site publiceert rapporten over **{{ site.data.drug_stats.total_drugs }}** geneesmiddelen uit de registratiegegevens van [CBG-MEB](https://www.cbg-meb.nl/) (Nederland).

Dataset: [CBG-MEB Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); wordt elke week (op maandag) automatisch gedownload en vergeleken. Details: [Gegevensbronnen]({{ '/sources/' | relative_url }}).

Rapporten per bewijsniveau:

| Bewijsniveau | Rapporten | Aandeel |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

<!-- site-data:end -->

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

Dit platform is ontwikkeld en wordt beheerd door **藥提醒科技有限公司** (yao.care). Gegevens over het bedrijf,
de achtergrond van het TxGNN-model en alle sites van de productlijn staan op de pagina
<a href="{{ '/about/' | relative_url }}">Over ons</a>.

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
Dit rapport is uitsluitend bedoeld als naslagwerk voor wetenschappelijk onderzoek en <strong>vormt geen medisch advies</strong>. Volg altijd de aanwijzingen van uw arts op; pas nooit op eigen initiatief uw medicatie aan. Elke beslissing over geneesmiddelherpositionering vereist volledige klinische validatie en toetsing door de registratieautoriteit.
<br><br>
<small>Beoordeeld door: 藥提醒科技有限公司 (yao.care)</small>
</div>
