---
layout: default
title: Allopurinol
parent: Alleen modelvoorspelling (L5)
nav_order: 21
evidence_level: L5
indication_count: 10
---

# Allopurinol
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

# Allopurinol: Van Jicht/Hyperuricemie naar Hepatale Porfyrie

## Samenvatting in één zin

Allopurinol is een xanthine oxidase (XO)-inhibitor, veel gebruikt voor de behandeling van jicht en hyperuricemie.
Het TxGNN-model voorspelt dat het effectief kan zijn voor **hepatale porfyrie**,
maar met slechts **0 klinische trials** en **2 publicaties** (hypothese-niveau en dieronderzoek), rust deze voorspelling momenteel op minimaal bewijs en vraagt om grote voorzichtigheid — vooral omdat allopurinol naar verluidt mogelijk **porfyrie kan verergeren**.

## Snel overzicht

| Item | Inhoud |
|------|--------|
| Originele indicatie | Jicht, hyperuricemie (goed gevestigd wereldwijd; geen lokale vergunningen in huidi dataset) |
| Voorspelde nieuwe indicatie | Hepatale porfyrie |
| TxGNN-voorspellingsscore | 99.95% |
| Bewijsniveau | L4 — Alleen preklinische/mechanismestudies |
| Marktstatus | Niet op de markt (Niet op de markt) in huidden regelgevingsdataset |
| Aantal vergunningen | 0 (in huidden dataset) |
| Aanbevolen besluit | **In afwachting** |

## Waarom is deze voorspelling redelijk?

Allopurinol is een purinederivaat waarvan de actieve metaboliet, oxipurinol, xanthine oxidase (XO) remt, het enzym dat verantwoordelijk is voor de omzetting van hypoxanthine naar xanthine en xanthine naar urinezuur. Dit mechanisme is decennia lang klinisch gevalideerd voor de behandeling van jicht en hyperuricemie. XO-remming vermindert ook de opwekking van reactieve zuurstofsoorten (ROS) als bijproduct van purinemetabolisme.

Hepatale porfyrieën zijn een groep stofwisselingsstoornissen veroorzaakt door enzymdeficiënties in de heem-biosyntheseroute, wat leidt tot opeenstapeling van toxische porfyrineprecursoren (zoals ALA en PBG) in de lever. Het snelheidsbepalende enzym, 5-aminolevulinaat synthase (ALAS1), staat onder negatieve terugkoppelingscontrole door een kleine regelende heem-pool. Theoretisch zou XO-remming indirecte substraatbeschikbaarheid voor ALAS1 kunnen veranderen of de redoxomgeving van hepatocyten kunnen beïnvloeden. Deze mechanistische link is echter volledig hypothetisch en heeft geen directe experimentele validatie.

Van cruciaal belang is dat de repurposingrationale uit het bewijsdossier zelf een groot veiligheidsprobleem signaleert: **allopurinol zou naar verluidt porfiyrische aanvallen kunnen verergeren**. Dit gaat in tegen de therapeutische hypothese en onderstreept de noodzaak van extreme voorzichtigheid. De TxGNN-voorspellingsscore (99.95%) is hoog, maar het model zou structurele nabijheid in de kennisgraaf tussen purinemetabolisme en heem-biosyntheseroutes kunnen vastleggen in plaats van een echte therapeutische relatie. Vijf van de top zes voorspelde indicaties zijn levergebonden aandoeningen met bijna identieke scores, wat duidt op een mogelijk buureffect in de kennisgraaf.

## Bewijs uit klinische trials

Momenteel zijn er geen gerelateerde klinische trials geregistreerd voor allopurinol bij hepatale porfyrie.

## Bewijsmateriaal uit literatuur

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|------|------|----------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothese/Commentaar | Medical Hypotheses | Stelt metabolisch gericht optreden tegen lever-ALAS voor door remming van heem-gebruik door tryptofaan 2,3-dioxigenase (TDO) als therapie voor acute hepatale porfyrieën. Bespreekt regelingsdynamica van heem-pool — onderzoekt allopurinol niet rechtstreeks maar verschaft mechanistische context voor heem-routemodulering. |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Dieronderzoek | Biochemical Pharmacology | Onderzocht effecten van carbamazepine op heem-metabolisme in rattenlever, met name hoe het hepatale porfyrieën verergert. Verschaft een screeningsmodel voor medicijngeïnduceerde porfyrie-verergering — relevant als raamwerk voor evaluatie van allopurinols porfyrie-risico. |

**Opmerking:** Geen van beide publicaties onderzoekt allopurinol rechtstreeks als behandeling voor hepatale porfyrie. De eerste is een hypothesepaper over heem-routemodulering; de tweede onderzoekt een ander geneesmiddel (carbamazepine) als porfyrie-verergering.

## Informatie Nederlandse markt

Er zijn geen CBG-MEB-vergunningen voor markttoelating gevonden in de huidge dataset voor allopurinol. Allopurinol is echter een goed gevestigd WHO-essentieel geneesmiddel en is overal in Europa, inclusief Nederland, beschikbaar onder meerdere merknamen (bijv. Zyloric). De afwezigheid van vergunningen in deze dataset weerspiegelt waarschijnlijk een beperking van de gegevensdekking in plaats van echte marktafwezigheid.

## Veiligheidsbeschouwingen

Raadpleeg de SmPC (Samenvatting van de productkenmerken) voor uitgebreide veiligheidsinformatie.

**Belangrijk veiligheidssignaal voor deze specifieke repurposingkandidaat:**
- De mechanistische rationale merkt zelf op dat allopurinol naar verluidt mogelijk **porfiyrische aanvallen kan veroorzaken of verergeren**, wat het gebruik voor de voorspelde indicatie (hepatale porfyrie) rechtstreeks zou contraïndiceren. Dit moet grondig onderzocht worden voordat verdere evaluatie plaatsvindt.
- Allopurinol staat bekend om ernstige overgevoeligheidsreacties (inclusief Stevens-Johnson-syndroom en DRESS-syndroom), met name bij patiënten met de HLA-B*5801-allel.

## Aanvullende voorspelde indicaties (Gerangschikt 2–10)

Het TxGNN-model voorspelde ook de volgende indicaties. Alle krijgen een **L5-beoordeling (alleen modelvoorspelling)** met een **In afwachting**-aanbeveling, omdat geen klinische trial- of literatuurondersteuning hebben:

| Rang | Voorspelde indicatie | TxGNN-score | Bewijsniveau | Aanbeveling |
|------|---------------------|-------------|----------------|-------------|
| 2 | Hepatopulmonaal syndroom | 99.94% | L5 | In afwachting |
| 3 | Primitieve portale venetrombose | 99.94% | L5 | In afwachting |
| 4 | Idiopathische kopperassocieerde cirrose | 99.94% | L5 | In afwachting |
| 5 | Familiaire non-cirrhotische portale hypertensie met vroeg begin | 99.94% | L5 | In afwachting |
| 6 | Hepatoportale sclerose | 99.94% | L5 | In afwachting |
| 7 | Stoornis van fenylalanine-metabolisme | 99.89% | L4 | In afwachting |
| 8 | Immuungemedieerde necrotiserende myopathie | 99.86% | L5 | In afwachting |
| 9 | Antisyntetase-syndroom | 99.85% | L5 | In afwachting |
| 10 | Idiopathische eosinofiele myositis | 99.85% | L5 | In afwachting |

**Waarnemingspatroon:** Rangen 2–6 delen bijna identieke TxGNN-scores (99.94%) en zijn allemaal hepatale/portalevene-aandoeningen. Deze clustering suggeert sterk dat de voorspellingen voortkomen uit een **kennisgraafbuurteffect** — het model herkent allopurinols metabolische link met leverfunctie en voorspelt breed over levergerelateerde ziekte-knooppunten, in plaats van specifieke therapeutische mechanismen aan te duiden.

## Conclusie en volgende stappen

**Besluit: In afwachting**

**Rationale:**
Ondanks een hoge TxGNN-voorspellingsscore (99.95%) is het bewijsmateriaal voor allopurinol bij hepatale porfyrie kritiek zwak: nul klinische trials, slechts twee marginaal gerelateerde publicaties (geen van beide studeert allopurinol rechtstreeks voor porfyrie), en een significant veiligheidsprobleem dat allopurinol porfiyrische aanvallen eigenlijk kan **verergeren**. De clustering van vijf levergebonden voorspellingen op bijna identieke scores suggereert een kennisgraaf-artefact in plaats van een echt therapeutisch signaal.

**Om door te gaan, zou het volgende nodig zijn:**
- Preklinisch onderzoek naar allopurinols directe effecten op de heem-biosyntheseroute (ALAS1, PBG-deaminase)
- Een definitieve beoordeling van of allopurinol porfyrie induceert of verergert in gevalideerde diermodellen
- Karakterisering van het werkingsmechanisme (MOA) relevant voor porfyrinemetabolisme
- Opsporing van SmPC-veiligheidsgegevens (belangrijke waarschuwingen, contraïndicaties, geneesmiddelinteracties) uit CBG-MEB- of EMA-bronnen
- Farmacogenomische beoordeling (prevalentie van HLA-B*5801 in doelpopulatie)

---

*Dit rapport is gegenereerd op 2026-04-03 op basis van bewijsdossier v4 (gegevenscutoff: 2026-04-03). Resultaten zijn uitsluitend voor onderzoeksdoeleinden en vormen geen medisch advies. Alle kandidaten voor geneesmiddelhercombinatie vereisen klinische validatie vóór toepassing.*

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

