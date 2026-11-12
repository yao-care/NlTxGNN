---
layout: default
title: Emtricitabine
parent: Alleen modelvoorspelling (L5)
nav_order: 129
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-12
description: "Emtricitabine: voorspelde nieuwe indicatie Feline acquired immunodeficiency syndrome (kattenaids) (bewijsniveau L5). Oorspronkelijke indicatie: Hiv-infectie en aids (de gegevens over de Nederlandse v…"
monitor_inn: "Emtricitabine"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Emtricitabine
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **3** 
{: .fs-6 .fw-300 }

---

## Inhoudsopgave
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmaceutisch beoordelingsrapport

</div>

## Emtricitabine: Van hiv/aids naar feline acquired immunodeficiency syndrome (kattenaids)
{: .text-alpha }

## Samenvatting in één zin

Emtricitabine is een remmer van het omgekeerde transcriptase (NRTI), oorspronkelijk gebruikt voor de behandeling van hiv-infectie en aids. Het TxGNN-model voorspelt dat het werkzaam kan zijn tegen **feline acquired immunodeficiency syndrome** (een diergeneeskundige indicatie), maar hiervoor zijn **0 klinische studies** en slechts **1 publicatie** (een preklinische studie bij katten) beschikbaar. Het bewijs is daarmee beperkt tot modelvoorspelling en indirect preklinisch onderzoek.

---

## Snel overzicht

| Item | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Hiv-infectie en aids (de gegevens over de Nederlandse vergunning bevatten geen indicatietekst) |
| Voorspelde nieuwe indicatie | Feline acquired immunodeficiency syndrome (kattenaids) |
| TxGNN-voorspellingsscore | 0,9992 |
| Bewijsniveau | L5 |
| Marktstatus in Nederland | In de handel (geldige vergunningen: 41 van 42) |
| Aantal vergunningen | 42 (geldig: 41) |
| Aanbevolen beslissing | Hold |

---

## Waarom is deze voorspelling aannemelijk?

Gedetailleerde gegevens over het werkingsmechanisme zijn momenteel niet beschikbaar in de voor dit rapport samengestelde data. Op basis van algemene kennis is emtricitabine een nucleosidenalogon dat na intracellulaire fosforylering het omgekeerde transcriptase van hiv-1 remt door ketenterminatie. De werkzaamheid bij hiv/aids is aangetoond.

Het felien immunodeficiëntievirus (FIV) is een lentivirus dat bij katten een progressieve immuundisfunctie veroorzaakt, vergelijkbaar met hiv bij de mens. Omdat het virus een verwant omgekeerd transcriptase heeft, bestaat er een mechanistische redenering. De enige ondersteunende publicatie onderzocht een combinatie van antiretrovirale middelen (dolutegravir, tenofovir en emtricitabine) bij met FIV geïnfecteerde katten. De hoge TxGNN-score weerspiegelt waarschijnlijk vooral de gelijkenis van deze indicatie met hiv, en niet onafhankelijk bewijs.

Het is een diergeneeskundige indicatie; de relevantie voor humane hergebruikstrajecten is beperkt.

> Ter volledigheid: het model voorspelde ook "simian immunodeficiency virus infection" (rang 2, score 0,9992, bewijsniveau L4) en een zeldzame neurodevelopmentele aandoening (rang 3, score 0,9992, bewijsniveau L5, zonder enig mechanistisch of klinisch bewijs). Dit rapport richt zich op de hoogst gerangschikte voorspelling.

---

## Bewijs uit klinische studies

Momenteel zijn er geen gerelateerde klinische studies geregistreerd.

---

## Bewijs uit de literatuur

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Preklinische/veterinaire studie | Viruses | Onderzocht de farmacokinetiek en klinische uitkomsten van combinatie-antiretrovirale therapie (dolutegravir 2,5 mg/kg, tenofovir 20 mg/kg, emtricitabine 40 mg/kg) bij FIV-geïnfecteerde huiskatten. De samenvatting is afgekapt, dus de uitkomsten zijn uit de beschikbare gegevens niet vast te stellen. |

---

## Informatie over de Nederlandse markt

| RVG-nummer | Productnaam | Toedieningsvorm | Goedgekeurde indicatie |
|---------|------|------|-----------|
| RVG 117316 (ingetrokken) | Ictastan 200mg/245mg, filmomhulde tabletten | Niet vermeld | Niet vermeld |

Raadpleeg de actuele SmPC en bijsluiter voor productinformatie.

<!-- review:begin nl-lic-20261112-emtricitabine-1 -->

> **Controlecorrectie (2026-11-12)**: Oorspronkelijk stond er: “Dit middel is in Nederland geregistreerd en op de markt: 1 geldige vergunning van de 1 vergunning(en) (CBG-MEB). Raadpleeg de actuele SmPC en bijsluiter voor productinformatie.” Verwijderd: het aantal of de status van de vergunningen kwam niet overeen met de registratiegegevens van het CBG (2026-11-12). Aantal vergunningen in de gegevens: 42, waarvan geldig: 41; actuele aantallen staan in het snelle overzicht en bij de marktinformatie. Bron: [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/).

<!-- review:end nl-lic-20261112-emtricitabine-1 -->

---

## Veiligheidsoverwegingen

**Contra-indicaties volgens de kennisgraaf** (afgeleid uit TxGNN/PrimeKG-relaties tussen geneesmiddel en aandoening, niet uit de bijsluitertekst; ter oriëntatie en niet als vastgestelde contra-indicaties te beschouwen):
- Hart: lange-QT-syndroom (ook familiair), torsades de pointes
- Lever: leverfalen, leverziekte, leververvetting, niet-alcoholische steatohepatitis, chronische hepatitis B en C
- Nier en metabool: nierziekte, Fanconi-syndroom, lactaatacidose, hypofosfatemie, osteomalacie, rachitis, hypertriglyceridemie, obesitas
- Overig: epilepsie, angststoornis, neurotische stoornis, dysthyme stoornis, waanstoornis, paranoïde schizofrenie, galblaasziekte

**Geneesmiddelinteracties** (20 gevonden; belangrijkste):
- **Ernstig (Major):** leflunomide, teriflunomide
- **Matig (Moderate):** onder meer orlistat, naltrexon, cobicistat, methotrexaat, cladribine, clofarabine, epirubicine, idelalisib, cabozantinib, brentuximab vedotin, tioguanine, trabectedine, asparaginase, pegaspargase, interferon-bèta-1a/1b en peginterferon-bèta-1a
- **Gering (Minor):** eribuline

Voor waarschuwingen en formele contra-indicaties: raadpleeg de SmPC.

---

## Conclusie en vervolgstappen

**Beslissing: Hold**

**Onderbouwing:**
- De voorspelling betreft een diergeneeskundige indicatie, wordt ondersteund door slechts één preklinische studie zonder duidelijke uitkomsten, en er zijn geen klinische studies. De hoge TxGNN-score (0,9992) komt van het TxGNN-model (deep learning) en kan gelijkenissen weerspiegelen die het model heeft geleerd tussen verwante ziekten, niet biologisch bewijs.

**Om verder te gaan is het volgende nodig:**
- Volledige tekst van PMID 37112803 om te beoordelen of en hoe emtricitabine bijdroeg aan de uitkomsten
- Gegevens over het werkingsmechanisme (o.a. uit DrugBank)
- Waarschuwingen en contra-indicaties uit de CBG-MEB-bijsluiter (nu ontbrekend; dit blokkeert de veiligheidsscreening)
- Beoordeling of een diergeneeskundige indicatie binnen de scope van humane hergebruikstrajecten valt (diergeneesmiddelen vallen onder een ander regelgevend kader)

<!-- review:begin log -->

## Controlelogboek

Hieronder staat het controlelogboek van deze pagina: gegevens gecontroleerd aan de hand van de registratiegegevens van het CBG (College ter Beoordeling van Geneesmiddelen). Correcties betreffen alleen feitelijke basisgegevens; modelvoorspellingen, bewijsniveaus en conclusies zijn niet herschreven.

| Controledatum | Onderdeel | Actie | Bron |
|------|------|------|------|
| 2026-11-12 | Verwijderd: “Dit middel is in Nederland geregistreerd en op de markt: 1 geldige vergunning van de 1 vergunning(en) (CBG-MEB)” | Gecorrigeerd | [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/) |

<!-- review:end log -->

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

