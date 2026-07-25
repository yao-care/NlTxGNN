---
layout: default
title: Over ons
nav_order: 90
permalink: /about/
description: "NlTxGNN is een platform voor het voorspellen van geneesmiddelherpositionering, ontwikkeld door 藥提醒科技有限公司 (yao.care), gebouwd op het Harvard TxGNN-model en gericht op door CBG-MEB goedgekeurde geneesmiddelen in Nederland."
---

# Over ons

<div class="key-takeaway">
De validatie van bewijs voor geneesmiddelherpositionering versnellen met AI — van voorspelling tot bewijs in één oogopslag.
</div>

---

## Achtergrond

<p class="key-answer" data-question="Wat is NlTxGNN?">
<strong>NlTxGNN</strong> is een onderzoeksondersteunend platform voor geneesmiddelherpositionering, gebouwd op
het TxGNN-model dat het Zitnik Lab van Harvard University publiceerde in <em>Nature Medicine</em>. Het voorspelt
indicatie-uitbreiding voor geneesmiddelen die door CBG-MEB in Nederland zijn goedgekeurd. Naast de
voorspellingsscores van de AI integreert het platform klinisch bewijs uit ClinicalTrials.gov en PubMed, zodat
onderzoekers snel kunnen beoordelen hoe geloofwaardig elke voorspelling is.
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

## Wat is geneesmiddelherpositionering?

<p class="key-answer" data-question="Wat is geneesmiddelherpositionering?">
<strong>Geneesmiddelherpositionering</strong> betekent het vinden van nieuwe therapeutische toepassingen voor
bestaande geneesmiddelen. Vergeleken met het vanaf nul ontwikkelen van een nieuw geneesmiddel — 10 tot 15 jaar
en USD 1&ndash;2 miljard — kost herpositionering 3 tot 5 jaar en USD 100&ndash;300 miljoen, en er zijn al
veiligheidsgegevens bij mensen beschikbaar, waardoor het faalrisico lager is.
</p>

<table class="comparison-table">
<thead>
<tr><th>Aspect</th><th>Ontwikkeling van een nieuw geneesmiddel</th><th>Geneesmiddelherpositionering</th></tr>
</thead>
<tbody>
<tr><td>Doorlooptijd</td><td>10&ndash;15 jaar</td><td>3&ndash;5 jaar</td></tr>
<tr><td>Kosten</td><td>USD 1&ndash;2 miljard</td><td>USD 100&ndash;300 miljoen</td></tr>
<tr><td>Veiligheidsgegevens</td><td>Moeten nog worden opgebouwd</td><td>Gegevens bij mensen al beschikbaar</td></tr>
<tr><td>Faalrisico</td><td>Zeer hoog (&gt;90%)</td><td>Lager</td></tr>
</tbody>
</table>

---

## Wat is TxGNN?

<p class="key-answer" data-question="Wat is TxGNN?">
<a href="https://www.nature.com/articles/s41591-023-02233-x">TxGNN</a> is een deep-learningmodel dat is
ontwikkeld door het Zitnik Lab van Harvard Medical School en gepubliceerd in <em>Nature Medicine</em>.
Het voorspelt nieuwe verbanden tussen geneesmiddelen en ziekten en is het eerste foundation model voor
geneesmiddelherpositionering dat specifiek voor clinici is ontworpen.
</p>

<blockquote class="expert-quote">
"TxGNN integreert een kennisgraaf van 17.080 biomedische entiteiten en gebruikt graph neural networks
om complexe relaties tussen knooppunten te leren, waarmee de mogelijke werkzaamheid van geneesmiddelen
tegen zeldzame ziekten wordt voorspeld."
<cite>&mdash; Huang et al., Nature Medicine (2023)</cite>
</blockquote>

---

## Gegevensbronnen

<table class="comparison-table">
<thead>
<tr><th>Type</th><th>Bron</th><th>Omschrijving</th></tr>
</thead>
<tbody>
<tr><td>AI-voorspelling</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Voorspellingsmodel van Harvard op basis van een kennisgraaf</td></tr>
<tr><td>Klinische studies</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Wereldwijd register van klinische studies</td></tr>
<tr><td>Literatuur</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Biomedische literatuurdatabase</td></tr>
<tr><td>Geneesmiddelinformatie</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Database van geneesmiddelen en aangrijpingspunten</td></tr>
<tr><td>Registratiegegevens</td><td><a href="https://www.cbg-meb.nl/">CBG-MEB</a></td><td>Gegevens over geneesmiddelregistratie in Nederland</td></tr>
</tbody>
</table>

---

## Wetenschappelijke basis

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

---

## Omvang

| Onderdeel | Waarde |
|------|-------|
| Geneesmiddelrapporten | 261 |
| Registratieautoriteit | CBG-MEB |
| Uitgerolde sites | 30 landen / regio's |

---

## Contact

- **GitHub Issues**: <https://github.com/yao-care/NlTxGNN/issues>
- **Ontwikkelaar**: 藥提醒科技有限公司 (<https://www.yao.care>, service@yao.care)
- **Productoverzicht**: <https://www.yao.care/medical/txgnn/>

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
Dit rapport is uitsluitend bedoeld als naslagwerk voor wetenschappelijk onderzoek en <strong>vormt geen medisch advies</strong>. Volg altijd de aanwijzingen van uw arts op; pas nooit op eigen initiatief uw medicatie aan. Elke beslissing over geneesmiddelherpositionering vereist volledige klinische validatie en toetsing door de registratieautoriteit.
<br><br>
<small>Beoordeeld door: 藥提醒科技有限公司 (yao.care)</small>
</div>
