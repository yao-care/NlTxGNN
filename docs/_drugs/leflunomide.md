---
layout: default
title: Leflunomide
parent: Alleen modelvoorspelling (L5)
nav_order: 84
evidence_level: L5
indication_count: 2
---

# Leflunomide
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **2** 
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

# Leflunomide: Van Reumatoïde Artritis naar Brachydactylie-Syndactylie Syndroom

---

## Samenvatting in één zin

Leflunomide is een internationaal gevestigd ziekteveranderend antirevmatisch middel (DMARD) voor de behandeling van reumatoïde artritis en psoriasis arthritis.
Het TxGNN-model voorspelt dat het effectief kan zijn voor **Brachydactylie-Syndactylie Syndroom**, een ultrazeldzame aangeboren ledematen-malformatie.
Echter, **geen klinische trials of gepubliceerde literatuur** ondersteunen deze richting, en de mechanistische rationale geïdentificeerd door de kennisgraaf bevat een kritieke richtingsomkeringsfout die dit waarschijnlijk tot een vals positief maakt.

---

## Snel overzicht

| Item | Inhoud |
|------|--------|
| Oorspronkelijke indicatie | Reumatoïde artritis / psoriasis arthritis (internationaal gevestigd; geen NL-registratie vastgelegd in deze dataset) |
| Voorspelde nieuwe indicatie | Brachydactylie-Syndactylie Syndroom |
| TxGNN-voorspellingsscore | 99.93% |
| Bewijsniveau | L5 |
| Marktstatusnederlands | Niet in de handel |
| Aantal toelatingen | 0 |
| Aanbevolen beslissing | Uitstellen |

---

## Waarom is deze voorspelling redelijk?

Momenteel zijn gedetailleerde werkingsmechanisme-gegevens niet beschikbaar in dit bewijspakket. Op basis van gevestigde farmacologie is leflunomide een remmer van **dihydroorotaatdehydrogenase (DHODH)**, het snelheid-limiterende enzym in de de novo pyrimidine-biosynthese. Door intracellulaire pyrimidine-voorraden uit te putten, onderdrukt het proliferatie van geactiveerde T- en B-lymfocyten, wat zijn anti-inflammatoire werking in reumatoïde artritis produceert.

De kennisgraaf (KG) heeft waarschijnlijk het volgende pad gevolgd om deze voorspelling op te wekken: verlies-van-functie (LOF) mutaties in het *DHODH* gen staan bekend om **Miller syndroom** te veroorzaken, een zeldzame aandoening gekarakteriseerd door acrofaciale dysostose inclusief ledematen-afwijkingen. De KG kan een indirect verband tot stand hebben gebracht tussen de *DHODH*-gennode en brachydactylie/syndactylie-fenotype-nodes, wat een hoge-vertrouwen score opleverde.

**Dit verband vertegenwoordigt echter een vals positief door mechanistische richtingsomkering.** Het aangeboren fenotype ontstaat door *onvoldoende* DHODH-activiteit (LOF), terwijl leflunomide DHODH verder *remt* — wat betekent dat het medicijn in dezelfde richting werkt als het onderliggende pathologische mechanisme in plaats van het tegen te gaan. Het toepassen van een DHODH-remmer ter behandeling van een aandoening veroorzaakt door DHODH-deficiëntie is farmacologisch contraproductief. Deze voorspelling draagt geen therapeutische plausibiliteit en moet worden behandeld als een modelartefact.

---

## Klinische trial-gegevens

Momenteel geen gerelateerde klinische trials geregistreerd.

---

## Literatuurgegevens

Momenteel geen gerelateerde literatuur beschikbaar.

---

## Marktinformatie Nederland

Geen CBG-MEB nationale toelating (RVG-nummer) voor leflunomide is opgenomen in deze dataset.

> **Opmerking:** Leflunomide (merknaam Arava) is geautoriseerd in de Europese Unie via gecentraliseerde EMA-procedure. EU-brede toelatingen (EU/x/xx/xxx-format) kunnen niet worden vastgelegd in nationale RVG-datasets. Clinici en apothekers moeten de huidige toelating en beschikbaarheid op de markt rechtstreeks verifiëren via de **CBG-MEB-productdatabase** of de **EMA-geneesmiddellenportal** voordat zij conclusies trekken over NL-toegankelijkheid.

---

## Veiligheidsoverwegingen

Raadpleeg alstublieft de SmPC (Samenvatting van Product Karakteristieken) voor veiligheidsinformatie. Veiligheidsgegevens — inclusief belangrijke waarschuwingen, contra-indicaties en geneesmiddel-interacties — waren niet beschikbaar in dit bewijspakket.

> Aangezien leflunomide een gevestigde EMA-toelating voor reumatoïde artritis bezit, is een huidige SmPC beschikbaar via de EMA-website en moet deze worden geraadpleegd voor eventueel klinisch gebruik.

---

## Conclusie en volgende stappen

**Beslissing: Uitstellen**

**Rationale:**
De TxGNN-voorspelling voor brachydactylie-syndactylie syndroom is een **vals positief door mechanistische richtingsomkering**: de aandoening wordt veroorzaakt door DHODH verlies-van-functie, terwijl leflunomide DHODH remt — het medicijn zou de onderliggende pathofysiologie verergeren in plaats van te corrigeren. Gecombineerd met een bewijsniveau van L5 (nul klinische trials, nul publicaties), is er geen basis om deze indicatie vooruit te gaan.

**Om constructief verder te gaan, is het volgende nodig:**

- **Deze voorspelling markeren** als vals positief in de TxGNN-pijplijn; overweeg de implementatie van een mechanistische directionaliteitsfilter voor enzym-LOF/remmer-paren
- **Geen klinisch of translationaal onderzoek initiëren** voor deze indicatie zonder onafhankelijke mechanistische herevaluatie
- **Marktstatusnederlands verifiëren** via CBG-MEB / EMA-databases — leflunomide bezit waarschijnlijk een EU-gecentraliseerde toelating die niet in deze nationale dataset wordt vastgelegd
- **SmPC-veiligheidsgegevens ophalen** (waarschuwingen, contra-indicaties, hepatotoxiciteits-monitoringvereisten) voordat een klinische overweging van het medicijn in nederland plaatsvindt
- **Bij verkenning van leflunomide voor nieuwe indicaties**, prioriteit geven aan inflammatoire of immuun-gemedieerde ziekte-fenotypes waarbij DHODH-inhibitie mechanistisch coherent is (bijv. lupus nefritis, inflammatoire darmziekte — indicaties met bestaande onderzoeksliteratuur)

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

