---
layout: default
title: Alle geneesmiddelen
nav_order: 20
permalink: /drugs/
description: "Alle validatierapporten van geneesmiddelen en de statistieken per bewijsniveau in NlTxGNN."
---
{% assign l1_count = site.drugs | where: "evidence_level", "L1" | size %}
{% assign l2_count = site.drugs | where: "evidence_level", "L2" | size %}
{% assign l3_count = site.drugs | where: "evidence_level", "L3" | size %}
{% assign l4_count = site.drugs | where: "evidence_level", "L4" | size %}
{% assign l5_count = site.drugs | where: "evidence_level", "L5" | size %}

# Alle geneesmiddelen

{{ site.drugs.size }} validatierapporten van geneesmiddelen

---

## Verdeling per bewijsniveau

| Bewijsniveau | Geneesmiddelen | Omschrijving |
|---------|--------|------|
| **L1** | {{ l1_count }} | Meerdere RCT's / systematische reviews |
| **L2** | {{ l2_count }} | Eén RCT / fase 2-studies |
| **L3** | {{ l3_count }} | Observationele studies / grote patiëntenseries |
| **L4** | {{ l4_count }} | Preklinische / mechanistische studies |
| **L5** | {{ l5_count }} | Alleen modelvoorspelling |

---

## Volledige geneesmiddellijst

{% assign all_drugs = site.drugs | sort: 'title' %}

| Geneesmiddel | Bewijsniveau | Indicaties |
|---------|---------|---------|
{% for drug in all_drugs %}| [{{ drug.title }}]({{ drug.url | relative_url }}) | {{ drug.evidence_level }} | {{ drug.indication_count }} |
{% endfor %}

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
Dit rapport is uitsluitend bedoeld als naslagwerk voor wetenschappelijk onderzoek en <strong>vormt geen medisch advies</strong>. Volg altijd de aanwijzingen van uw arts op; pas nooit op eigen initiatief uw medicatie aan. Elke beslissing over geneesmiddelherpositionering vereist volledige klinische validatie en toetsing door de registratieautoriteit.
<br><br>
<small>Beoordeeld door: 藥提醒科技有限公司 (yao.care)</small>
</div>
