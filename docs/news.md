---
layout: default
title: Gezondheidsnieuws
nav_order: 30
permalink: /news/
has_children: true
description: "Gezondheidsnieuws dat NlTxGNN volgt voor de geneesmiddelen en indicaties op deze site."
---

# Gezondheidsnieuws

<div class="key-takeaway">
Automatisch gevolgde nieuwsberichten over de geneesmiddelen en voorspelde indicaties op deze site.
</div>

---

## Alle berichten

{% assign items = site.news | sort: 'title' %}
{% if items.size == 0 %}
Nog geen passende berichten.
{% else %}
{% for item in items %}- [{{ item.title }}]({{ item.url | relative_url }})
{% endfor %}
{% endif %}

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
gebouwd; het omvat de integratie van nationale geneesmiddelregistratiegegevens, voorspelling met deep learning waarbij toepassingen die al in de kennisgraaf staan zijn uitgesloten, bewijsgradering op basis van PubMed / ClinicalTrials, en integratie
met elektronische patiëntendossiers via SMART on FHIR.

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
Dit rapport is uitsluitend bedoeld als naslagwerk voor wetenschappelijk onderzoek en <strong>vormt geen medisch advies</strong>. Volg altijd de aanwijzingen van uw arts op; pas nooit op eigen initiatief uw medicatie aan. Elke beslissing over geneesmiddelherpositionering vereist volledige klinische validatie en toetsing door de registratieautoriteit.
<br><br>
<small>Beoordeeld door: 藥提醒科技有限公司 (yao.care)</small>
</div>
