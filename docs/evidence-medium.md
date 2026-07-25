---
layout: default
title: Matig bewijs (L3-L4)
nav_order: 22
permalink: /evidence-medium/
description: "L3-L4-kandidaten voor geneesmiddelherpositionering in NlTxGNN, onderbouwd met observationeel of preklinisch bewijs."
---

# Matig bewijs (L3-L4)

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

### L3 ({{ l3_drugs.size }} geneesmiddelen)

| Geneesmiddel | Indicaties | Link |
|---------|---------|------|
{% for drug in l3_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Rapport bekijken]({{ drug.url | relative_url }}) |
{% endfor %}

### L4 ({{ l4_drugs.size }} geneesmiddelen)

| Geneesmiddel | Indicaties | Link |
|---------|---------|------|
{% for drug in l4_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Rapport bekijken]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
Dit rapport is uitsluitend bedoeld als naslagwerk voor wetenschappelijk onderzoek en <strong>vormt geen medisch advies</strong>. Volg altijd de aanwijzingen van uw arts op; pas nooit op eigen initiatief uw medicatie aan. Elke beslissing over geneesmiddelherpositionering vereist volledige klinische validatie en toetsing door de registratieautoriteit.
<br><br>
<small>Beoordeeld door: 藥提醒科技有限公司 (yao.care)</small>
</div>
