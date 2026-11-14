---
layout: default
title: Alleen modelvoorspelling (L5)
nav_order: 23
permalink: /evidence-low/
description: "L5-kandidaten in NlTxGNN: alleen een modelvoorspelling, nog zonder klinisch bewijs of literatuur."
---

# Alleen modelvoorspelling (L5)

<!-- page-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
{% assign pd_m = site.data.drug_stats.level_counts.L5 %}
Deze pagina toont **{{ pd_m }}** van de **{{ site.data.drug_stats.total_drugs }}** geneesmiddelen met een gepubliceerd rapport op deze site ({{ pd_m | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%). Definitie van de niveaus: [Methodologie]({{ '/methodology/' | relative_url }}).
<!-- page-data:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Kandidaten met alleen een modelvoorspelling en nog geen bewijs bij mensen
</p>

---

## Criteria

| Niveau | Definitie | Klinische betekenis |
|-------|------------|------------------|
| **L5** | Alleen modelvoorspelling | Hypothesefase; nog geen bewijs bij mensen |

---

{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | sort: "title" %}

### L5 ({{ l5_drugs.size }} geneesmiddelen)

| Geneesmiddel | Indicaties | Link |
|---------|---------|------|
{% for drug in l5_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Rapport bekijken]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
Dit rapport is uitsluitend bedoeld als naslagwerk voor wetenschappelijk onderzoek en <strong>vormt geen medisch advies</strong>. Volg altijd de aanwijzingen van uw arts op; pas nooit op eigen initiatief uw medicatie aan. Elke beslissing over geneesmiddelherpositionering vereist volledige klinische validatie en toetsing door de registratieautoriteit.
<br><br>
<small>Beoordeeld door: 藥提醒科技有限公司 (yao.care)</small>
</div>
