---
layout: default
title: "Alleen bekend gebruik (geen nieuwe voorspellingen)"
nav_order: 24
permalink: /known-uses/
description: "Voor deze geneesmiddelen zijn alle kandidaten van het TxGNN-model al bekend gebruik (vastgelegd in de kennisgraaf of in een vergunning), dus er is geen nie…"
---

# Alleen bekend gebruik (geen nieuwe voorspellingen)

Voor deze geneesmiddelen zijn alle kandidaten van het TxGNN-model al bekend gebruik (vastgelegd in de kennisgraaf of in een vergunning), dus er is geen nieuwe voorspelde indicatie. Elke pagina toont het bekende gebruik en de lokale marktstatus.

{% assign known_drugs = site.drugs | where: "evidence_level", "N/A" | sort: "title" %}

**{{ known_drugs.size }} geneesmiddelen**

| Geneesmiddel | Rapport |
|------|------|
{% for drug in known_drugs %}| **{{ drug.title }}** | [Bekijk pagina]({{ drug.url | relative_url }}) |
{% endfor %}
