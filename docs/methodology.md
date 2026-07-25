---
layout: default
title: Methodologie
nav_order: 91
permalink: /methodology/
description: "Hoe NlTxGNN voorspellingen produceert en valideert: voorspelling met de TxGNN-kennisgraaf, verzameling van bewijs, gradering L1-L5 en beslissingsaanbevelingen."
---

# Methodologie

<div class="key-takeaway">
Van AI-voorspelling tot bewijsgradering — elke kandidaat heeft een traceerbare onderbouwing voor zijn beoordeling.
</div>

---

## Het volledige proces

<p class="key-answer" data-question="Hoe komt NlTxGNN tot zijn voorspellingen?">
Het platform gebruikt een proces in vier fasen: het TxGNN-kennisgraafmodel voorspelt mogelijke verbanden
tussen geneesmiddelen en ziekten, vervolgens wordt voor elk voorspeld paar automatisch bewijs verzameld,
dat bewijs wordt gegradeerd van L1 tot L5, en ten slotte wordt een beslissingsaanbeveling afgegeven.
</p>

<ol class="actionable-steps">
<li><strong>TxGNN-voorspelling</strong>: relaties tussen geneesmiddelen en ziekten worden voorspeld met een kennisgraaf in combinatie met graph neural networks.</li>
<li><strong>Verzameling van bewijs</strong>: voor elk voorspeld paar wordt bewijs verzameld uit ClinicalTrials.gov, PubMed, DrugBank en CBG-MEB.</li>
<li><strong>Bewijsgradering</strong>: gegradeerd van L1 tot L5, waarbij L1 het sterkst is (meerdere fase 3-RCT's) en L5 alleen een modelvoorspelling betreft.</li>
<li><strong>Beslissingsaanbeveling</strong>: Go, Proceed, Consider, Explore of Hold, op basis van het bewijsniveau.</li>
</ol>

---

## Criteria voor bewijsgradering

<table class="comparison-table">
<thead>
<tr><th>Niveau</th><th>Definitie</th><th>Klinische betekenis</th></tr>
</thead>
<tbody>
<tr><td><strong>L1</strong></td><td>Meerdere fase 3-RCT's / systematische reviews</td><td>Sterke ondersteuning; klinisch gebruik kan worden overwogen</td></tr>
<tr><td><strong>L2</strong></td><td>Eén RCT of meerdere fase 2-studies</td><td>Matige ondersteuning; validatiestudies kunnen worden opgezet</td></tr>
<tr><td><strong>L3</strong></td><td>Observationele studies / grote patiëntenseries</td><td>Voorlopige ondersteuning; verdere validatie nodig</td></tr>
<tr><td><strong>L4</strong></td><td>Preklinische / mechanistische studies</td><td>Theoretische ondersteuning; nog ver van klinisch gebruik</td></tr>
<tr><td><strong>L5</strong></td><td>Alleen modelvoorspelling</td><td>Hypothesefase; nog geen bewijs bij mensen</td></tr>
</tbody>
</table>

---

## Voorspelling met twee engines

Twee methoden draaien parallel; een betrouwbaarheidslabel legt vast of zij het met elkaar eens zijn:

| Methode | Snelheid | Precisie | Omschrijving |
|--------|-------|-----------|-------------|
| Kennisgraaf (KG) | Snel | Lager | Inferentie op basis van DrugBank-relaties en graafstructuur |
| Deep learning (DL) | Langzaam | Hoger | Het TxGNN graph-neural-network-model |

| Betrouwbaarheid | Bron | Betekenis |
|------------|--------|---------|
| very_high | KG + DL | Beide methoden zijn het eens |
| high | Alleen DL | Ondersteuning door deep learning met een hoge score |
| medium | Alleen KG | Ondersteuning door de kennisgraaf |

---

## Integratie van registratiegegevens

De gegevens over goedgekeurde geneesmiddelen in Nederland komen van CBG-MEB. Namen van werkzame stoffen
worden gekoppeld aan het DrugBank-vocabulaire; stoffen die niet gekoppeld kunnen worden — plantaardige
extracten, vaccins, hulpstoffen en andere zaken die niet in DrugBank zijn opgenomen — worden uitgesloten
van voorspelling.

---

## Beperkingen

<ol class="actionable-steps">
<li>Voorspellingen zijn statistische verbanden en <strong>impliceren geen oorzakelijk verband of klinische werkzaamheid</strong>.</li>
<li>Een L5-beoordeling betekent alleen een modelvoorspelling, zonder ondersteunend bewijs bij mensen.</li>
<li>De verzameling van bewijs is afhankelijk van openbare databases; niet-gepubliceerde of niet-geïndexeerde studies worden niet meegenomen.</li>
<li>Door verschillen in naamgeving kunnen bij de koppeling van werkzame stoffen items worden gemist.</li>
</ol>

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
