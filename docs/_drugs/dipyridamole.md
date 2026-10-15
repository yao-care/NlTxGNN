---
layout: default
title: Dipyridamole
parent: Alleen modelvoorspelling (L5)
nav_order: 116
evidence_level: L5
indication_count: 10
---

# Dipyridamole
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **10** 
{: .fs-6 .fw-300 }

---

## Inhoudsopgave
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Farmaceutisch beoordelingsrapport

</div>

# Dipyridamol: Van voorkamerfibrillatie naar Prinzmetal-angina

## Samenvatting in één zin

Dipyridamol is een bloedplaatjesaggregatieremmer en vaatverwijder die in de kennisgrafiek van het model is gekoppeld aan voorkamerfibrillatie als oorspronkelijke indicatie. Het TxGNN-model voorspelt dat het werkzaam kan zijn bij **Prinzmetal-angina**, maar hiervoor zijn **geen geregistreerde klinische studies** en slechts **10 publicaties** van beperkte kwaliteit beschikbaar. Opmerkelijk is dat een andere voorspelling, **beroerte (stroke disorder)**, wél sterk wordt ondersteund (o.a. 8 klinische studies en 19 publicaties). Deze wordt hieronder als belangrijkste alternatief toegelicht.

---

## Snel overzicht

| Onderdeel | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Voorkamerfibrillatie (afkomstig uit de kennisgrafiek; in de Nederlandse registraties is geen indicatietekst beschikbaar) |
| Voorspelde nieuwe indicatie | Prinzmetal-angina |
| TxGNN-voorspellingsscore | 99,99% |
| Bewijsniveau | L4 (voor Prinzmetal-angina); ter vergelijking L1 voor beroerte en TIA |
| NL-marktstatus | Alleen doorgehaald (ingetrokken registraties) |
| Aantal vergunningen | 2 (beide ingetrokken) |
| Aanbevolen beslissing | Hold (Prinzmetal-angina); Proceed with Guardrails voor beroerte en TIA |

---

## Waarom is deze voorspelling redelijk?

Gedetailleerde gegevens over het werkingsmechanisme ontbreken in de voor dit rapport verzamelde data. Op basis van algemeen bekende informatie remt dipyridamol de heropname van adenosine en de activiteit van fosfodiësterase. Hierdoor stijgen de cAMP- en cGMP-niveaus, wat leidt tot verwijding van de kransslagvaten en remming van de bloedplaatjesaggregatie.

Voor **Prinzmetal-angina** is het therapeutische verband zwak en mogelijk ongunstig. In de literatuur komt dipyridamol vooral voor als stressmiddel bij diagnostische tests. Zo kan het beëindigen van een dipyridamol-stresstest met aminofylline vaatspasmen uitlokken bij variant angina. De vaatverwijdende werking kan bij gevoelige patiënten zelfs spasmen of coronaire "steal" veroorzaken. De hoge modelscore heeft hier dus geen duidelijke klinische onderbouwing.

Voor **beroerte en TIA** is het mechanisme wél goed passend. De remming van de bloedplaatjesaggregatie, aangevuld met mogelijke antioxidatieve, ontstekingsremmende en neuroprotectieve effecten, ondersteunt het gebruik, meestal in combinatie met acetylsalicylzuur, bij secundaire preventie na een ischemische beroerte of TIA.

---

## Bewijs uit klinische studies

Voor Prinzmetal-angina is momenteel geen gerelateerde klinische studie geregistreerd.

Ter vergelijking volgen hieronder de belangrijkste studies voor het sterkst onderbouwde alternatief, **beroerte**:

| Studienummer | Fase | Status | Inclusie | Belangrijkste bevindingen |
|---------|------|------|------|---------|
| [NCT00161070](https://clinicaltrials.gov/study/NCT00161070) | Fase 4 | Afgerond | 4500 | ESPRIT: acetylsalicylzuur plus dipyridamol of milde antistolling versus alleen acetylsalicylzuur na TIA of lichte beroerte (directe evidentie) |
| [NCT00562588](https://clinicaltrials.gov/study/NCT00562588) | Fase 4 | Afgerond | 551 | EARLY: Aggrenox binnen 24 uur na een beroerte versus start na 7 dagen acetylsalicylzuur |
| [NCT00238667](https://clinicaltrials.gov/study/NCT00238667) | Fase 3 | Afgerond | 250 | Haalbaarheidsstudie naar antistolling versus bloedplaatjesremmers bij cervicale arteriedissectie (indirect) |
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Fase 3 | Afgerond | 664 | Sluiting van PFO of antistolling versus bloedplaatjesremmers ter voorkoming van een nieuwe beroerte (indirect) |
| [NCT00738894](https://clinicaltrials.gov/study/NCT00738894) | N.v.t. | Afgerond | 664 | GORE REDUCE: PFO-sluiting plus bloedplaatjesremmers versus alleen bloedplaatjesremmers (indirect) |
| [NCT02630862](https://clinicaltrials.gov/study/NCT02630862) | N.v.t. | Afgerond | 240 | Oxidatieve stress en oxysterolen na carotisrevascularisatie; mechanistisch onderzoek |
| [NCT06053021](https://clinicaltrials.gov/study/NCT06053021) | N.v.t. | Onbekend | 1200 | Bloedplaatjesremmers bij acute ischemische beroerte met trombocytopenie (indirect) |
| [NCT06983795](https://clinicaltrials.gov/study/NCT06983795) | N.v.t. | Nog niet gestart met werven | 1000 | Register van PFO en ischemische beroerte in de Azië-Pacific (indirect) |

---

## Bewijs uit de literatuur

Voor Prinzmetal-angina (10 publicaties, geen RCT's):

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|-----|------|------|---------|
| [633593](https://pubmed.ncbi.nlm.nih.gov/633593/) | 1978 | Review | Japanese Circulation Journal | Reactie van angina in rust (waaronder Prinzmetal) op verschillende middelen, waaronder dipyridamol 50 mg |
| [3421166](https://pubmed.ncbi.nlm.nih.gov/3421166/) | 1988 | Kleine klinische studie | American Journal of Cardiology | Aminofylline-beëindiging van dipyridamol-stress kan coronaire vasospasme uitlokken bij variant angina |
| [3190956](https://pubmed.ncbi.nlm.nih.gov/3190956/) | 1988 | Cohort | British Heart Journal | Reproduceerbaarheid van inspanningstests bij ST-elevatie en wisselende reacties op de dipyridamoltest |
| [16630456](https://pubmed.ncbi.nlm.nih.gov/16630456/) | 2006 | Cohort | Zhonghua Xin Xue Guan Bing Za Zhi | Klinische kenmerken van typische en atypische coronaire spasme |
| [14060538](https://pubmed.ncbi.nlm.nih.gov/14060538/) | 1963 | Casuïstiek | Naika | Een geval van variant angina pectoris |

Voor beroerte (sterkste bewijs, meta-analyses en systematische reviews):

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|-----|------|------|---------|
| [11786451](https://pubmed.ncbi.nlm.nih.gov/11786451/) | 2002 | Meta-analyse | BMJ | Bloedplaatjesremming voorkomt overlijden, hartinfarct en beroerte bij hoogrisicopatiënten |
| [17636684](https://pubmed.ncbi.nlm.nih.gov/17636684/) | 2007 | Cochrane-review | Cochrane Database Syst Rev | Toevoeging van dipyridamol aan acetylsalicylzuur gaf in één studie 22% risicoreductie; in de totale evidentie weinig verschil met acetylsalicylzuur alleen |
| [15569877](https://pubmed.ncbi.nlm.nih.gov/15569877/) | 2005 | Meta-analyse (individuele patiëntdata) | Stroke | Dipyridamol voor het voorkomen van een nieuwe ischemische beroerte; eerdere RCT's gaven tegenstrijdige resultaten |
| [23871093](https://pubmed.ncbi.nlm.nih.gov/23871093/) | 2013 | Meta-analyse van RCT's | J Neurol Sci | Effectiviteit en veiligheid van acetylsalicylzuur plus dipyridamol versus acetylsalicylzuur na TIA of beroerte |
| [34211246](https://pubmed.ncbi.nlm.nih.gov/34211246/) | 2021 | Review | Australian Prescriber | Acetylsalicylzuur, clopidogrel of acetylsalicylzuur plus dipyridamol zijn eerstelijnsopties bij secundaire preventie zonder voorkamerfibrillatie |
| [20955428](https://pubmed.ncbi.nlm.nih.gov/20955428/) | 2010 | Review | Ann N Y Acad Sci | Mogelijke neuroprotectieve en ontstekingsremmende voordelen van dipyridamol bij acute beroerte |

---

## Informatie over de Nederlandse markt

| RVG-nummer | Productnaam | Toedieningsvorm | Goedgekeurde indicatie |
|---------|------|------|-----------|
| RVG 113461 | Dipyridamol Sandoz retard 200 mg, capsules met gereguleerde afgifte, hard | Capsule met gereguleerde afgifte | Niet beschikbaar (registratie doorgehaald) |
| RVG 109873 | Dipyridamol/Acetylsalicylzuur Sandoz 200/25 mg, capsules met gereguleerde afgifte, hard | Capsule met gereguleerde afgifte | Niet beschikbaar (registratie doorgehaald) |

Beide registraties bij het CBG-MEB zijn doorgehaald. Beschikbaarheid en formulering moeten daarom eerst worden bevestigd.

---

## Veiligheidsoverwegingen

- **Contra-indicaties (afgeleid uit de kennisgrafiek, niet uit de bijsluitertekst)**: o.a. nier- en leverziekte, trombocytopenie, maagzweer (ook actief), hypotensie, jicht, acuut coronair syndroom, hartinfarct, hemofilie, bloedarmoede, Reye-syndroom, neuspoliepen en gastritis. Deze lijst is niet geverifieerd aan de SmPC en kan deels de acetylsalicylzuurcomponent van de combinatie weerspiegelen.
- **Geneesmiddelinteracties**: 451 interacties geregistreerd. Matig ernstig zijn onder meer dexfenfluramine, sibutramine en fenfluramine. Overige genoemde interacties (o.a. acetylsalicylzuur, cimetidine, omeprazol, pantoprazol, metformine, morfine, simvastatine) hebben een onbekend ernstniveau.
- **Bij gebruik bij beroerte/TIA**: let op hoofdpijn en bloedingsrisico.

Raadpleeg voor de volledige waarschuwingen en contra-indicaties de SmPC.

---

## Conclusie en vervolgstappen

**Beslissing voor Prinzmetal-angina: Hold**

**Onderbouwing:**
- Het bewijs is beperkt tot oude, kleine studies en casuïstiek, zonder geregistreerde klinische studies. De vaatverwijdende werking kan juist vasospasme of coronaire steal uitlokken, waardoor het therapeutische verband zwak en mogelijk ongunstig is.

**Aanbeveling voor het alternatief (beroerte en TIA): Proceed with Guardrails**
- Er is bewijsniveau L1 (o.a. ESPRIT, meta-analyses en Cochrane-reviews). Gebruik uitsluitend als combinatie met acetylsalicylzuur volgens richtlijnen voor secundaire preventie.

**Om verder te gaan is nodig:**
- Verificatie van beschikbaarheid en formulering, gezien de ingetrokken registraties bij het CBG-MEB
- Volledige SmPC-gegevens over waarschuwingen en contra-indicaties (momenteel ontbrekend, wat een blokkerende leemte is voor de veiligheidsscreening)
- Gegevens over het werkingsmechanisme uit DrugBank
- Een plan voor het beheersen van hoofdpijn, bloedingsrisico en de interactielast
- Voor Prinzmetal-angina: gecontroleerde klinische studies en een veiligheidsbeoordeling van het risico op vasospasme voordat verdere stappen worden overwogen

Overige voorspellingen (o.a. sicksinussyndroom, sarcoglycanopathie, Wildervanck-syndroom) hebben uitsluitend modelbewijs (L5) en vragen om een Hold. Voor trombotische ziekte (L3) en sinustrombose is nader onderzoek nodig.
## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

