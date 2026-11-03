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

{% assign items = site.news | where_exp: "n", "n.layout != 'id_redirect'" | sort: 'title' %}
{% if items.size == 0 %}
Nog geen passende berichten.
{% else %}
{% for item in items %}- [{{ item.title }}]({{ item.url | relative_url }})
{% endfor %}
{% endif %}

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
