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

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## Nederland: wat de bestanden nu bevatten

| Bestand | Huidige inhoud |
|---|---|
| `/data/search-index.json` | {{ site.data.local_facts.files.search_index }} geneesmiddelen met hun voorspelde indicaties |
| `/data/drugs.json` | {{ site.data.local_facts.files.drugs_json }} geneesmiddelen met bewijsniveau en oorspronkelijke indicatie |
| `/fhir/MedicationKnowledge/` | {{ site.data.local_facts.fhir.medication_knowledge }} MedicationKnowledge-resources (één per geneesmiddel) |
| `/fhir/ClinicalUseDefinition/` | {{ site.data.local_facts.fhir.clinical_use_definition }} ClinicalUseDefinition-resources (één per voorspelde indicatie) |

Hergebruik van de lokale dataset: [CBG-MEB Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/metadata.csv), gepubliceerd door College ter Beoordeling van Geneesmiddelen (CBG-MEB); hergebruik valt onder de voorwaarden van de uitgever, en deze site verleent geen aanvullende rechten.

{% if site.data.local_facts.top_licensed.size > 0 %}Geneesmiddelen met de meeste actuele CBG-registraties: {% for r in site.data.local_facts.top_licensed limit: 5 offset: 3 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.lv }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}

{% if site.data.local_facts.recent_reviews.size > 0 %}Laatste correcties in het controlelogboek: {% for r in site.data.local_facts.recent_reviews limit: 8 offset: 16 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

<!-- local-facts:end -->

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
