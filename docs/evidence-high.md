---
layout: default
title: Sterk bewijs (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "23 geneesmiddelen met bewijsniveau L1–L2 op deze site (Nederland), bijv. Bendamustine, Bupropion, Ribavirin, met per middel de belangrijkste voorspelde indicatie, CBG-registraties en controlelogboek."
---

# Sterk bewijs (L1-L2)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Deze pagina toont **{{ site.data.evidence_tier_facts.high.count }}** van de **{{ site.data.drug_stats.total_drugs }}** geneesmiddelen met een gepubliceerd rapport op deze site ({{ site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%): L1 **{{ site.data.evidence_tier_facts.high.by_level.L1 }}**, L2 **{{ site.data.evidence_tier_facts.high.by_level.L2 }}**.
Mediaan aandeel L1–L2 over de 30 TxGNN-sites: {{ site.data.evidence_tier_facts.high.cross.median_share }}%. {% if ev_share > site.data.evidence_tier_facts.high.cross.median_share %}Deze site zit boven de mediaan.{% elsif ev_share < site.data.evidence_tier_facts.high.cross.median_share %}Deze site zit onder de mediaan.{% else %}Deze site zit op de mediaan.{% endif %}

{% if site.data.evidence_tier_facts.high.count > 0 %}
In de lokale gegevens (CBG-registraties) hebben **{{ site.data.evidence_tier_facts.high.with_current }}** van deze geneesmiddelen minstens één actuele registratie, **{{ site.data.evidence_tier_facts.high.none_current }}** hebben registraties maar geen actuele en **{{ site.data.evidence_tier_facts.high.without_data }}** komen niet in de lokale gegevens voor. **{{ site.data.evidence_tier_facts.high.with_reviews }}** hebben vermeldingen in het controlelogboek (correcties van registratiegegevens op de geneesmiddelpagina). **{{ site.data.evidence_tier_facts.high.cross.unique_drugs }}** hebben een voorspelde indicatie die geen andere TxGNN-site voor hetzelfde geneesmiddel noemt.
{% if site.data.evidence_tier_facts.high.none_current_list.size > 0 %}

Met registraties, maar geen actuele: {% for r in site.data.evidence_tier_facts.high.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}
{% endif %}

Definitie van alle niveaus: [Methodologie]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Kandidaten die met voorrang voor klinische evaluatie in aanmerking komen
</p>

Welke van deze geneesmiddelen hebben bewijs uit studies voor hun voorspelde nieuwe indicatie, en hoeveel geregistreerde studies worden geciteerd? Zie [Geneesmiddelen in Nederland met bewijs uit klinische studies voor een nieuwe indicatie]({{ '/clinical-trial-evidence/' | relative_url }}).

---

## Criteria

| Niveau | Definitie | Klinische betekenis |
|-------|------------|------------------|
| **L1** | Meerdere fase 3-RCT's / systematische reviews | Sterke ondersteuning; klinisch gebruik kan worden overwogen |
| **L2** | Eén RCT of meerdere fase 2-studies | Matige ondersteuning; validatiestudies kunnen worden opgezet |

---

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | sort: "title" %}

### L1 ({{ site.data.evidence_tier_facts.high.by_level.L1 }} geneesmiddelen)

<!-- tier-table:start L1（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Geneesmiddel | Niveau | Belangrijkste voorspelde nieuwe indicatie | CBG-registraties: actuele / totaal | Controlelogboek | Alleen op deze site |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.high.rows %}{% if r.l == "L1" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ja ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

### L2 ({{ site.data.evidence_tier_facts.high.by_level.L2 }} geneesmiddelen)

<!-- tier-table:start L2（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Geneesmiddel | Niveau | Belangrijkste voorspelde nieuwe indicatie | CBG-registraties: actuele / totaal | Controlelogboek | Alleen op deze site |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.high.rows %}{% if r.l == "L2" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ja ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
Dit rapport is uitsluitend bedoeld als naslagwerk voor wetenschappelijk onderzoek en <strong>vormt geen medisch advies</strong>. Volg altijd de aanwijzingen van uw arts op; pas nooit op eigen initiatief uw medicatie aan. Elke beslissing over geneesmiddelherpositionering vereist volledige klinische validatie en toetsing door de registratieautoriteit.
<br><br>
<small>Beoordeeld door: 藥提醒科技有限公司 (yao.care)</small>
</div>
