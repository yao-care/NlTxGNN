---
layout: default
title: Alleen modelvoorspelling (L5)
nav_order: 23
permalink: /evidence-low/
description: "259 geneesmiddelen met bewijsniveau L5 op deze site (Nederland), bijv. Valsartan, Ezetimibe, Amlodipine, met per middel de belangrijkste voorspelde indicatie, CBG-registraties en controlelogboek."
---

# Alleen modelvoorspelling (L5)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.low.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Deze pagina toont **{{ site.data.evidence_tier_facts.low.count }}** van de **{{ site.data.drug_stats.total_drugs }}** geneesmiddelen met een gepubliceerd rapport op deze site ({{ site.data.evidence_tier_facts.low.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%): L5 **{{ site.data.evidence_tier_facts.low.by_level.L5 }}**.
Mediaan aandeel L5 over de 30 TxGNN-sites: {{ site.data.evidence_tier_facts.low.cross.median_share }}%. {% if ev_share > site.data.evidence_tier_facts.low.cross.median_share %}Deze site zit boven de mediaan.{% elsif ev_share < site.data.evidence_tier_facts.low.cross.median_share %}Deze site zit onder de mediaan.{% else %}Deze site zit op de mediaan.{% endif %}

{% if site.data.evidence_tier_facts.low.count > 0 %}
In de lokale gegevens (CBG-registraties) hebben **{{ site.data.evidence_tier_facts.low.with_current }}** van deze geneesmiddelen minstens één actuele registratie, **{{ site.data.evidence_tier_facts.low.none_current }}** hebben registraties maar geen actuele en **{{ site.data.evidence_tier_facts.low.without_data }}** komen niet in de lokale gegevens voor. **{{ site.data.evidence_tier_facts.low.with_reviews }}** hebben vermeldingen in het controlelogboek (correcties van registratiegegevens op de geneesmiddelpagina). **{{ site.data.evidence_tier_facts.low.cross.unique_drugs }}** hebben een voorspelde indicatie die geen andere TxGNN-site voor hetzelfde geneesmiddel noemt.
{% if site.data.evidence_tier_facts.low.none_current_list.size > 0 %}

Met registraties, maar geen actuele: {% for r in site.data.evidence_tier_facts.low.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}

Geneesmiddelen met een actuele lokale registratie staan bovenaan.
{% endif %}

Definitie van alle niveaus: [Methodologie]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

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

### L5 ({{ site.data.evidence_tier_facts.low.by_level.L5 }} geneesmiddelen)

<!-- tier-table:start L5（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Geneesmiddel | Niveau | Belangrijkste voorspelde nieuwe indicatie | CBG-registraties: actuele / totaal | Controlelogboek | Alleen op deze site |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.low.rows %}{% if r.l == "L5" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ja ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
Dit rapport is uitsluitend bedoeld als naslagwerk voor wetenschappelijk onderzoek en <strong>vormt geen medisch advies</strong>. Volg altijd de aanwijzingen van uw arts op; pas nooit op eigen initiatief uw medicatie aan. Elke beslissing over geneesmiddelherpositionering vereist volledige klinische validatie en toetsing door de registratieautoriteit.
<br><br>
<small>Beoordeeld door: 藥提醒科技有限公司 (yao.care)</small>
</div>
