---
layout: default
title: Matig bewijs (L3-L4)
nav_order: 22
permalink: /evidence-medium/
description: "40 geneesmiddelen met bewijsniveau L3–L4 op deze site (Nederland), bijv. Acitretin, Alprazolam, Calcipotriol, met per middel de belangrijkste voorspelde indicatie, CBG-registraties en controlelogboek."
---

# Matig bewijs (L3-L4)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Deze pagina toont **{{ site.data.evidence_tier_facts.medium.count }}** van de **{{ site.data.drug_stats.total_drugs }}** geneesmiddelen met een gepubliceerd rapport op deze site ({{ site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%): L3 **{{ site.data.evidence_tier_facts.medium.by_level.L3 }}**, L4 **{{ site.data.evidence_tier_facts.medium.by_level.L4 }}**.
Mediaan aandeel L3–L4 over de 30 TxGNN-sites: {{ site.data.evidence_tier_facts.medium.cross.median_share }}%. {% if ev_share > site.data.evidence_tier_facts.medium.cross.median_share %}Deze site zit boven de mediaan.{% elsif ev_share < site.data.evidence_tier_facts.medium.cross.median_share %}Deze site zit onder de mediaan.{% else %}Deze site zit op de mediaan.{% endif %}

{% if site.data.evidence_tier_facts.medium.count > 0 %}
In de lokale gegevens (CBG-registraties) hebben **{{ site.data.evidence_tier_facts.medium.with_current }}** van deze geneesmiddelen minstens één actuele registratie, **{{ site.data.evidence_tier_facts.medium.none_current }}** hebben registraties maar geen actuele en **{{ site.data.evidence_tier_facts.medium.without_data }}** komen niet in de lokale gegevens voor. **{{ site.data.evidence_tier_facts.medium.with_reviews }}** hebben vermeldingen in het controlelogboek (correcties van registratiegegevens op de geneesmiddelpagina). **{{ site.data.evidence_tier_facts.medium.cross.unique_drugs }}** hebben een voorspelde indicatie die geen andere TxGNN-site voor hetzelfde geneesmiddel noemt.
{% if site.data.evidence_tier_facts.medium.none_current_list.size > 0 %}

Met registraties, maar geen actuele: {% for r in site.data.evidence_tier_facts.medium.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}
{% endif %}

Definitie van alle niveaus: [Methodologie]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Kandidaten met voorlopig bewijs die verdere validatie vereisen
</p>

---

## Criteria

| Niveau | Definitie | Klinische betekenis |
|-------|------------|------------------|
| **L3** | Observationele studies / grote patiëntenseries | Voorlopige ondersteuning; verdere validatie nodig |
| **L4** | Preklinische / mechanistische studies | Theoretische ondersteuning; nog ver van klinisch gebruik |

---

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | sort: "title" %}
{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | sort: "title" %}

### L3 ({{ site.data.evidence_tier_facts.medium.by_level.L3 }} geneesmiddelen)

<!-- tier-table:start L3（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Geneesmiddel | Niveau | Belangrijkste voorspelde nieuwe indicatie | CBG-registraties: actuele / totaal | Controlelogboek | Alleen op deze site |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L3" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ja ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

### L4 ({{ site.data.evidence_tier_facts.medium.by_level.L4 }} geneesmiddelen)

<!-- tier-table:start L4（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Geneesmiddel | Niveau | Belangrijkste voorspelde nieuwe indicatie | CBG-registraties: actuele / totaal | Controlelogboek | Alleen op deze site |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L4" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ja ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
Dit rapport is uitsluitend bedoeld als naslagwerk voor wetenschappelijk onderzoek en <strong>vormt geen medisch advies</strong>. Volg altijd de aanwijzingen van uw arts op; pas nooit op eigen initiatief uw medicatie aan. Elke beslissing over geneesmiddelherpositionering vereist volledige klinische validatie en toetsing door de registratieautoriteit.
<br><br>
<small>Beoordeeld door: 藥提醒科技有限公司 (yao.care)</small>
</div>
