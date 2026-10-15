---
layout: default
title: Iohexol
parent: Alleen modelvoorspelling (L5)
nav_order: 184
evidence_level: L5
indication_count: 2
---

# Iohexol
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

# Iohexol: Van contrastmiddel voor beeldvorming naar insomnia (voorspelde nieuwe indicatie)

## Samenvatting in het kort

Iohexol is een jodiumhoudend, niet-ionisch röntgencontrastmiddel dat wordt gebruikt voor diagnostische beeldvorming. Het TxGNN-model voorspelt dat het mogelijk werkzaam is bij **insomnia** (slapeloosheid), maar voor deze richting zijn **geen klinische studies** en **geen publicaties** beschikbaar. Voor de tweede voorspelling, **angst (anxiety)**, zijn **4 publicaties** gevonden, maar geen daarvan onderbouwt een therapeutisch effect.

## Snel overzicht

| Onderdeel | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Niet beschikbaar in de gegevens van de Nederlandse vergunning (diagnostisch röntgencontrastmiddel) |
| Voorspelde nieuwe indicatie | Insomnia |
| TxGNN-voorspellingsscore | 99,87% |
| Bewijsniveau | L5 |
| Marktstatus in Nederland | Alleen doorgehaalde (ingetrokken) vergunning |
| Aantal vergunningen | 1 (0 geldig, 1 doorgehaald) |
| Aanbevolen beslissing | Hold |

## Waarom is deze voorspelling (on)aannemelijk?

Er is geen plausibele farmacologische verklaring gevonden. Iohexol is een in water oplosbaar, niet-ionisch jodiumhoudend contrastmiddel dat farmacologisch inert is en onveranderd via de nieren wordt uitgescheiden. Het heeft geen bekende werking op slaapregulerende systemen (GABA-erg, orexinerg, melatonerg of histaminerg).

De zeer hoge score (0,9987) lijkt een artefact van de kennisgraaf, bijvoorbeeld door gedeelde interactieburen van geneesmiddelen, en wordt niet ondersteund door een farmacologische rationale. Gegevens over het oorspronkelijke werkingsmechanisme ontbreken in de voor dit rapport verzamelde gegevens.

Hetzelfde geldt voor de tweede voorspelling, angst (score 99,25%): iohexol heeft geen anxiolytische farmacologie. Angst komt in de gevonden literatuur alleen voor als procedurele context of als bijwerking van het onderzoek, niet als behandeldoel.

## Klinisch trialbewijs

Er zijn momenteel geen gerelateerde klinische studies geregistreerd, voor zowel insomnia als angst.

## Literatuurbewijs

Voor insomnia is momenteel geen gerelateerde literatuur beschikbaar. Voor de tweede voorspelling (angst) zijn de volgende publicaties gevonden; geen ervan ondersteunt een behandeling van angst met iohexol:

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|-----|------|------|---------|
| [8883531](https://pubmed.ncbi.nlm.nih.gov/8883531/) | 1996 | RCT | Academic Radiology | Dubbelblinde vergelijking van iodixanol en iohexol bij flebografie van de extremiteiten (werkzaamheid, veiligheid, injectiegerelateerd ongemak); niet relevant voor behandeling van angst |
| [2352635](https://pubmed.ncbi.nlm.nih.gov/2352635/) | 1990 | Cohortstudie | Neuroradiology | Bijwerkingen na lumbale myelografie met iohexol bij 200 patiënten (o.a. hoofdpijn, misselijkheid, duizeligheid, lichte psychische klachten zoals angst of depressie); angst als bijwerking, niet als doel |
| [2125805](https://pubmed.ncbi.nlm.nih.gov/2125805/) | 1990 | Fysiologische klinische studie | Acta Neurochirurgica | Hemodynamiek van de hersenen tijdens angiografie, gemeten met transcraniële Doppler; niet relevant voor angst als indicatie |
| [39861464](https://pubmed.ncbi.nlm.nih.gov/39861464/) | 2025 | Review/observationeel | Nutrients | Voeding en lichaamsbeweging in de onco-nefrologie; niet relevant voor de koppeling tussen geneesmiddel en indicatie |

## Informatie over de Nederlandse markt

| RVG-nummer | Productnaam | Toedieningsvorm | Goedgekeurde indicatie |
|---------|------|------|-----------|
| RVG 117156 | Nitigraf 350 mg I/ml, oplossing voor injectie (status: doorgehaald) | Niet vermeld | Niet vermeld |

## Veiligheidsoverwegingen

Voor waarschuwingen en contra-indicaties uit de bijsluiter zijn in de verzamelde gegevens geen bruikbare gegevens beschikbaar. Raadpleeg de SmPC (Samenvatting van de Productkenmerken) en de bijsluiter via het CBG-MEB voor veiligheidsinformatie.

**Geneesmiddelinteracties:** De interactieverkenning leverde in totaal 100 interacties op. Het overzicht in de gegevens bevat 20 interacties, waarvan de meeste het niveau "Major" hebben. Voorbeelden:

- Corticosteroïden: hydrocortison, dexamethason, betamethason, triamcinolon
- Metformine
- Amfotericine B (inclusief de lipidecomplexvorm)
- Aminoglycosiden en glycopeptiden: kanamycine, neomycine, vancomycine
- Levofloxacine
- Morfine
- Bupropion
- Mesalazine en balsalazide
- Metoclopramide
- Dronabinol
- Fentermine en diethylpropion

Mannitol is geclassificeerd als "Moderate". Dit is een selectie uit de beschikbare lijst en geen volledig overzicht.

## Conclusie en vervolgstappen

**Beslissing: Hold**

**Onderbouwing:**
- Er is geen plausibel werkingsmechanisme, geen klinische studie en geen relevante literatuur voor insomnia of angst. De hoge TxGNN-scores zijn waarschijnlijk een artefact van de kennisgraaf.
- Bovendien is de enige Nederlandse vergunning doorgehaald, en ontbreken de veiligheidsgegevens uit de bijsluiter.

**Om verder te kunnen gaan is het volgende nodig:**
- Bijsluitertekst van het CBG-MEB (waarschuwingen en contra-indicaties) ophalen en verwerken
- Gegevens over het werkingsmechanisme aanvullen via DrugBank
- Een farmacologisch onderbouwde hypothese opstellen die verder gaat dan de modelscore, voordat verdere evaluatie plaatsvindt
- Preklinisch of mechanistisch bewijs voor effecten op slaap- of angstregulatie, indien beschikbaar
## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

