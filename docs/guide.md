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

Dit platform wordt ontwikkeld en beheerd door **藥提醒科技有限公司** (yao.care, inschrijvingsnummer
83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

NlTxGNN is de Nederlandse site van de productlijn "TxGNN Drug Repurposing" van het bedrijf.
Hetzelfde systeem is uitgerold in 30 landen en regio's, elk met de naam `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN, enzovoort) op `{cc}txgnn.yao.care`.
Productoverzicht: <https://www.yao.care/medical/txgnn/>.

Het TxGNN-model zelf is ontwikkeld door het Zitnik Lab van Harvard Medical School en gepubliceerd
in *Nature Medicine*. Dit platform is het productiesysteem dat 藥提醒科技有限公司 op dat model heeft
gebouwd; het omvat de integratie van nationale geneesmiddelregistratiegegevens, dubbele voorspelling
met kennisgraaf en deep learning, bewijsgradering op basis van PubMed / ClinicalTrials, en integratie
met elektronische patiëntendossiers via SMART on FHIR.

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
Dit rapport is uitsluitend bedoeld als naslagwerk voor wetenschappelijk onderzoek en <strong>vormt geen medisch advies</strong>. Volg altijd de aanwijzingen van uw arts op; pas nooit op eigen initiatief uw medicatie aan. Elke beslissing over geneesmiddelherpositionering vereist volledige klinische validatie en toetsing door de registratieautoriteit.
<br><br>
<small>Beoordeeld door: 藥提醒科技有限公司 (yao.care)</small>
</div>
