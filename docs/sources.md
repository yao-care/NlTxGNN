---
layout: default
title: Gegevensbronnen
nav_order: 93
permalink: /sources/
description: "De gegevensbronnen achter NlTxGNN: de Geneesmiddeleninformatiebank van CBG-MEB (metadata.csv), TxGNN, ClinicalTrials.gov, PubMed en DrugBank."
---

# Gegevensbronnen

<div class="key-takeaway">
Elke conclusie is te herleiden tot een openbare gegevensbron — niets is een black box.
</div>

---

<!-- site-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
## Nederland: gegevens van deze site

Deze site publiceert rapporten over **{{ site.data.drug_stats.total_drugs }}** geneesmiddelen uit de registratiegegevens van [CBG-MEB](https://www.cbg-meb.nl/) (Nederland).

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

## Overzicht van de bronnen

<table class="comparison-table">
<thead>
<tr><th>Type</th><th>Bron</th><th>Gebruikt voor</th></tr>
</thead>
<tbody>
<tr><td>Registratiegegevens</td><td>Geneesmiddeleninformatiebank van CBG-MEB: <a href="https://www.geneesmiddeleninformatiebank.nl/metadata.csv">metadata.csv</a></td><td>In Nederland geregistreerde geneesmiddelen (RVG- en EU-nummers), werkzame stoffen en of een registratie nog in het bestand staat</td></tr>
<tr><td>Voorspellingsmodel</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Voorspelling van verbanden tussen geneesmiddel en ziekte</td></tr>
<tr><td>Klinische studies</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Bewijsgradering (NCT)</td></tr>
<tr><td>Literatuur</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Bewijsgradering (PMID)</td></tr>
<tr><td>Geneesmiddelinformatie</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Koppeling van werkzame stoffen en gegevens over aangrijpingspunten</td></tr>
<tr><td>Interacties</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>Gegevens over interacties tussen geneesmiddelen</td></tr>
</tbody>
</table>

De geneesmiddelenlijst van de site is oorspronkelijk opgebouwd uit een kopie van dezelfde databank bij
Open State Foundation (data.openstate.eu); de registratiestatus komt sinds oktober 2026 rechtstreeks uit het CBG-bestand.

---

## Licenties

Elke bron heeft zijn eigen licentie — controleer deze voordat u citeert:

- **TxGNN**: academisch gebruik; citeer Huang et al. (2024)
- **ClinicalTrials.gov / PubMed**: openbare gegevens van de Amerikaanse NIH
- **DrugBank**: niet-commercieel gebruik, onder de eigen licentievoorwaarden
- **CBG-MEB Geneesmiddeleninformatiebank**: openbaar bestand van de registratieautoriteit, zonder registratie te downloaden; de kopie bij Open State Foundation valt onder CC0

---

## Updatefrequentie

| Gegevens | Frequentie |
|------|-----------|
| Registratiestatus | Elke week (maandag) automatisch bijgewerkt uit metadata.csv |
| Bewijs uit studies / literatuur | Periodiek opnieuw verzameld |
| Interactiegegevens | Elk kwartaal beoordeeld |

---

## Wetenschappelijke citatie

> Huang, K., et al. (2024). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)

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
