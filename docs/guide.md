---
layout: default
title: Gebruikershandleiding
nav_order: 92
permalink: /guide/
description: "Gebruikershandleiding van NlTxGNN: hoe u geneesmiddelen opzoekt, bewijsniveaus leest en aanbevelingen interpreteert."
---

# Gebruikershandleiding

<div class="key-takeaway">
Kijk eerst naar het bewijsniveau, dan naar de aanbeveling en lees daarna de bronliteratuur.
</div>

---

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## Nederland: een voorbeeld van deze site

Een rapport op deze site lees je in drie stappen: bewijsniveau, lokale marktgegevens, controlelogboek.

{% assign gx = site.data.local_facts.example %}
{% if gx %}Open [{{ gx.t }}]({{ gx.u | relative_url }}): de kop toont bewijsniveau **{{ gx.l }}**; de belangrijkste voorspelde nieuwe indicatie is **{{ gx.i }}**; de lokale gegevens bevatten **{{ gx.lt }}** CBG-registraties, waarvan **{{ gx.lv }}** actuele; het controlelogboek van de pagina heeft **{{ gx.r }}** vermeldingen.{% endif %}

{% if site.data.local_facts.most_reviewed.size > 0 %}Geneesmiddelen met de meeste vermeldingen in het controlelogboek: {% for r in site.data.local_facts.most_reviewed %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.r }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}

{% if site.data.local_facts.recent_reviews.size > 0 %}Laatste correcties in het controlelogboek: {% for r in site.data.local_facts.recent_reviews limit: 8 offset: 8 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

<!-- local-facts:end -->

## Een geneesmiddel opzoeken

<ol class="actionable-steps">
<li>Gebruik het zoekvak boven aan de pagina (namen van werkzame stoffen geven betere resultaten dan merknamen).</li>
<li>Of blader door de volledige lijst op <a href="{{ '/drugs/' | relative_url }}">Alle geneesmiddelen</a>.</li>
<li>U kunt ook bladeren per bewijsniveau: <a href="{{ '/evidence-high/' | relative_url }}">sterk</a>, <a href="{{ '/evidence-medium/' | relative_url }}">matig</a>, <a href="{{ '/evidence-low/' | relative_url }}">alleen modelvoorspelling</a>.</li>
</ol>

---

## Een rapport lezen

<p class="key-answer" data-question="Wat betekenen de bewijsniveaus L1 tot en met L5?">
Elk geneesmiddelrapport bevat de voorspelde nieuwe indicaties, en elke indicatie heeft een bewijsniveau
van L1 tot en met L5. <strong>L1 betekent dat meerdere gerandomiseerde gecontroleerde fase 3-onderzoeken
het al ondersteunen; L5 betekent alleen een modelvoorspelling, zonder bewijs bij mensen.</strong> De
volledige criteria staan op de pagina <a href="{{ '/methodology/' | relative_url }}">Methodologie</a>.
</p>

| Wat u ziet | Wat het betekent | Aanbevolen actie |
|-----------|----------|------------------|
| L1 / L2 | Er is bewijs uit klinische studies | Raadpleeg de onderliggende NCT- en PMID-records |
| L3 / L4 | Observationeel of preklinisch bewijs | Beschouw dit als een aanwijzing voor onderzoek |
| L5 | Alleen modelvoorspelling | Uitsluitend voor hypothesevorming; niet als klinische referentie |

---

## Citeren en traceerbaarheid

Elk bewijsstuk in een rapport heeft een traceerbare identificatie:

- **NCT-nummer**: verwijst naar de registratie op ClinicalTrials.gov
- **PMID**: verwijst naar het record in PubMed
- **DrugBank ID**: verwijst naar gegevens over het geneesmiddel en zijn aangrijpingspunten

Lees de bronliteratuur om de context te bevestigen voordat u een conclusie van dit platform citeert.

---

## Veelgestelde vragen

<p class="key-answer" data-question="Kunnen de voorspellingen klinisch worden gebruikt?">
<strong>Nee.</strong> De voorspellingen op dit platform zijn aanwijzingen voor onderzoek, geen klinisch
advies. Elke klinische toepassing van geneesmiddelherpositionering moet volledige validatie door klinische
studies en toetsing door de registratieautoriteit doorlopen.
</p>

<p class="key-answer" data-question="Waarom kan ik een bepaald geneesmiddel niet vinden?">
Een werkzame stof moet aan het DrugBank-vocabulaire gekoppeld kunnen worden om in de voorspelling te worden
opgenomen. Plantaardige extracten, vaccins, hulpstoffen en andere zaken die niet in DrugBank zijn opgenomen,
verschijnen niet op dit platform.
</p>

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
