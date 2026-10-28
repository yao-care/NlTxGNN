---
layout: default
title: Metyrapone
parent: Alleen modelvoorspelling (L5)
nav_order: 230
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Metyrapone: voorspelde nieuwe indicatie Exercise-induced malignant hyperthermia (bewijsniveau L5). Oorspronkelijke indicatie: Niet beschikbaar in de gegevens (de enige vergunning bevat geen indic…"
monitor_inn: "metyrapone"
predicted_indications: ["exercise-induced malignant hyperthermia", "King-Denborough syndrome", "central core myopathy", "moderate multiminicore disease with hand involvement", "congenital multicore myopathy with external ophthalmoplegia", "myopathy, centronuclear", "familial periodic paralysis", "renal tubular acidosis", "malignant hyperthermia of anesthesia"]
---

# Metyrapone
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **9** 
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

## Metyrapon: Van oorspronkelijke indicatie (onbekend) naar exercise-induced malignant hyperthermia
{: .text-alpha }

## Samenvatting in één zin

Metyrapon is een remmer van de cortisolsynthese. In de voor dit rapport samengestelde gegevens is geen oorspronkelijke geregistreerde indicatie opgenomen.
Het TxGNN-model voorspelt dat het werkzaam zou kunnen zijn bij **exercise-induced malignant hyperthermia**.
Hiervoor zijn **geen klinische studies** en **geen publicaties** gevonden; de voorspelling is uitsluitend computationeel (**L5**).

---

## Snel overzicht

| Item | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Niet beschikbaar in de gegevens (de enige vergunning bevat geen indicatietekst) |
| Voorspelde nieuwe indicatie | Exercise-induced malignant hyperthermia |
| TxGNN-voorspellingsscore | 0,9995 |
| Bewijsniveau | L5 |
| Marktstatus in Nederland | In de handel (geldige vergunningen: 1 van 1) |
| Aantal vergunningen | 1 (geldig: 1) |
| Aanbevolen beslissing | Hold |

---

## Waarom is deze voorspelling (on)aannemelijk?

Gedetailleerde gegevens over het werkingsmechanisme zijn momenteel niet beschikbaar in de samengestelde gegevens. Uit algemene kennis is metyrapon een remmer van 11-bèta-hydroxylase (CYP11B1) en verlaagt het de cortisolsynthese in de bijnier.

Maligne hyperthermie is daarentegen een stoornis van de calciumhuishouding in de skeletspier (RYR1/CACNA1S). Er is geen bekend biologisch verband met remming van de steroïdsynthese. De hoge score komt van het TxGNN-model (deep learning) en kan overeenkomsten weerspiegelen die het model heeft geleerd tussen verwante aandoeningen, en niet een aangetoond biologisch mechanisme. Dezelfde conclusie geldt voor de overige voorspelde aandoeningen in deze analyse, zoals gerelateerde congenitale myopathieën (o.a. King-Denborough-syndroom, central core myopathy, centronucleaire myopathie).

Een enkele aandoening, **familial periodic paralysis** (score 0,9940), heeft een indirect denkbaar fysiologisch verband via de invloed van steroïdhormonen op kaliumverschuivingen. Het enige gevonden artikel (zie hieronder) is echter een fysiologische studie uit 1971 en geen bewijs voor werkzaamheid.

---

## Klinisch trialbewijs

Momenteel zijn er geen gerelateerde klinische studies geregistreerd.

---

## Literatuurbewijs

Voor de hoofdvoorspelling (exercise-induced malignant hyperthermia) is momenteel geen gerelateerde literatuur beschikbaar.

Voor de nevenvoorspelling familial periodic paralysis is één publicatie gevonden:

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|-----|------|------|---------|
| [4322666](https://pubmed.ncbi.nlm.nih.gov/4322666/) | 1971 | Fysiologische/mechanistische studie | The Journal of Clinical Investigation | Bij een 19-jarige man met hyperkaliëmische periodieke paralyse werd verlamming uitgelokt door kaliumchloride en glucocorticoïden, maar niet door mineralocorticoïden of door ACTH plus metyrapon. Metyrapon was dus geen geteste behandeling; het betreft indirect bewijs. |

---

## Informatie over de Nederlandse markt

| RVG-nummer | Productnaam | Toedieningsvorm | Goedgekeurde indicatie |
|---------|------|------|-----------|
| RVG 113510 | Metopirone 250 mg capsules, zacht | Niet beschikbaar | Niet beschikbaar (vergunning geldig) |

Metyrapon is momenteel op de markt: in de gegevens van het CBG-MEB is 1 van de 1 vergunningen geldig.

---

## Overwegingen met betrekking tot veiligheid

- **Contra-indicaties (afgeleid uit het kennisnetwerk, niet uit de productinformatie):** bijnierinsufficiëntie in diverse vormen, waaronder de ziekte van Addison, chronische primaire bijnierinsufficiëntie, familiaire glucocorticoïddeficiëntie, X-gebonden congenitale bijnierhypoplasie, gedeeltelijke CYP11A1-deficiëntie en congenitale bijnierhyperplasie.
- **Geneesmiddelinteracties:** er zijn 12 interacties van matig niveau gevonden, vooral met oestrogenen (ethinylestradiol, estradiol, geconjugeerde oestrogenen, mestranol, veresterde oestrogenen, estronsulfaat, ook in topicale vorm) en met cyproheptadine.

De waarschuwingen en contra-indicaties uit de officiële productinformatie ontbreken. Raadpleeg de SmPC (Samenvatting van de Productkenmerken) voor volledige veiligheidsinformatie.

---

## Conclusie en vervolgstappen

**Beslissing: Hold**

**Onderbouwing:**
- De voorspelling berust uitsluitend op een model (L5), zonder klinische studies, zonder directe literatuur en zonder plausibel mechanisme. Bovendien is de enige Nederlandse vergunning doorgehaald en ontbreken de officiële veiligheidsgegevens, wat de veiligheidsscreening blokkeert.

**Om verder te gaan is nodig:**
- De bijsluiter/SmPC van het CBG-MEB ophalen en analyseren (waarschuwingen en contra-indicaties).
- Gegevens over het werkingsmechanisme aanvullen (bijv. via DrugBank).
- Een biologisch plausibel mechanisme voor de voorspelde aandoening aantonen, of de prioriteit verleggen naar kandidaten met een sterker verband (bijv. familial periodic paralysis, na gerichte literatuurstudie).
- De oorspronkelijke geregistreerde indicatie en de toedieningsvorm vaststellen.
- Preklinisch bewijs genereren voordat klinische evaluatie wordt overwogen.
## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

