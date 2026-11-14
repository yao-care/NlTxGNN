---
layout: default
title: Gebruikershandleiding
nav_order: 92
permalink: /guide/
description: "Gebruikershandleiding van NlTxGNN: hoe u geneesmiddelen opzoekt, bewijsniveaus leest en aanbevelingen interpreteert."
---

# Gebruikershandleiding

<div class="key-takeaway">
Kijk eerst naar het bewijsniveau, dan naar de aanbeveling en lees daarna de bronliteratuur.
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

## Een geneesmiddel opzoeken

<ol class="actionable-steps">
<li>Gebruik het zoekvak boven aan de pagina (namen van werkzame stoffen geven betere resultaten dan merknamen).</li>
<li>Of blader door de volledige lijst op <a href="{{ '/drugs/' | relative_url }}">Alle geneesmiddelen</a>.</li>
<li>U kunt ook bladeren per bewijsniveau: <a href="{{ '/evidence-high/' | relative_url }}">sterk</a>, <a href="{{ '/evidence-medium/' | relative_url }}">matig</a>, <a href="{{ '/evidence-low/' | relative_url }}">alleen modelvoorspelling</a>.</li>
</ol>

---

## Een rapport lezen

<p class="key-answer" data-question="Wat betekenen de bewijsniveaus L1 tot en met L5?">
Elk geneesmiddelrapport bevat de voorspelde nieuwe indicaties, en elke indicatie heeft een bewijsniveau
van L1 tot en met L5. <strong>L1 betekent dat meerdere gerandomiseerde gecontroleerde fase 3-onderzoeken
het al ondersteunen; L5 betekent alleen een modelvoorspelling, zonder bewijs bij mensen.</strong> De
volledige criteria staan op de pagina <a href="{{ '/methodology/' | relative_url }}">Methodologie</a>.
</p>

| Wat u ziet | Wat het betekent | Aanbevolen actie |
|-----------|----------|------------------|
| L1 / L2 | Er is bewijs uit klinische studies | Raadpleeg de onderliggende NCT- en PMID-records |
| L3 / L4 | Observationeel of preklinisch bewijs | Beschouw dit als een aanwijzing voor onderzoek |
| L5 | Alleen modelvoorspelling | Uitsluitend voor hypothesevorming; niet als klinische referentie |

---

## Citeren en traceerbaarheid

Elk bewijsstuk in een rapport heeft een traceerbare identificatie:

- **NCT-nummer**: verwijst naar de registratie op ClinicalTrials.gov
- **PMID**: verwijst naar het record in PubMed
- **DrugBank ID**: verwijst naar gegevens over het geneesmiddel en zijn aangrijpingspunten

Lees de bronliteratuur om de context te bevestigen voordat u een conclusie van dit platform citeert.

---

## Veelgestelde vragen

<p class="key-answer" data-question="Kunnen de voorspellingen klinisch worden gebruikt?">
<strong>Nee.</strong> De voorspellingen op dit platform zijn aanwijzingen voor onderzoek, geen klinisch
advies. Elke klinische toepassing van geneesmiddelherpositionering moet volledige validatie door klinische
studies en toetsing door de registratieautoriteit doorlopen.
</p>

<p class="key-answer" data-question="Waarom kan ik een bepaald geneesmiddel niet vinden?">
Een werkzame stof moet aan het DrugBank-vocabulaire gekoppeld kunnen worden om in de voorspelling te worden
opgenomen. Plantaardige extracten, vaccins, hulpstoffen en andere zaken die niet in DrugBank zijn opgenomen,
verschijnen niet op dit platform.
</p>

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
