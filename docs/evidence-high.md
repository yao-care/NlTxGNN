---
layout: default
title: Sterk bewijs (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "L1-L2-kandidaten voor geneesmiddelherpositionering in NlTxGNN, ondersteund door klinische studies of systematische reviews."
---

# Sterk bewijs (L1-L2)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Kandidaten die met voorrang voor klinische evaluatie in aanmerking komen
</p>

---

## Criteria

| Niveau | Definitie | Klinische betekenis |
|-------|------------|------------------|
| **L1** | Meerdere fase 3-RCT's / systematische reviews | Sterke ondersteuning; klinisch gebruik kan worden overwogen |
| **L2** | Eén RCT of meerdere fase 2-studies | Matige ondersteuning; validatiestudies kunnen worden opgezet |

---

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | sort: "title" %}

### L1 ({{ l1_drugs.size }} geneesmiddelen)

| Geneesmiddel | Indicaties | Link |
|---------|---------|------|
{% for drug in l1_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Rapport bekijken]({{ drug.url | relative_url }}) |
{% endfor %}

### L2 ({{ l2_drugs.size }} geneesmiddelen)

| Geneesmiddel | Indicaties | Link |
|---------|---------|------|
{% for drug in l2_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Rapport bekijken]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
Dit rapport is uitsluitend bedoeld als naslagwerk voor wetenschappelijk onderzoek en <strong>vormt geen medisch advies</strong>. Volg altijd de aanwijzingen van uw arts op; pas nooit op eigen initiatief uw medicatie aan. Elke beslissing over geneesmiddelherpositionering vereist volledige klinische validatie en toetsing door de registratieautoriteit.
<br><br>
<small>Beoordeeld door: 藥提醒科技有限公司 (yao.care)</small>
</div>
