---
layout: default
title: Metformin
parent: Alleen modelvoorspelling (L5)
nav_order: 223
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
monitor_inn: "metformin"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy"]
description: "Metformin: voorspelde nieuwe indicatie Focal stiff limb syndrome (bewijsniveau L5). Oorspronkelijke indicatie: Niet vermeld in de lokale gegevens"
---

# Metformin
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **5** 
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

## Metformin: Focal stiff limb syndrome
{: .text-alpha }

## Samenvatting in één zin

Metformine is een bloedsuikerverlagend middel dat oorspronkelijk wordt gebruikt bij **type 2 diabetes mellitus**. Het TxGNN-model voorspelt dat het mogelijk werkzaam is bij **focal stiff limb syndrome** (focaal stijve-ledemaatsyndroom). Er zijn echter **0 klinische studies** en **0 publicaties** die deze richting ondersteunen; het betreft uitsluitend een modelvoorspelling.

---

## Snel overzicht

| Item | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Niet vermeld in de lokale gegevens |
| Voorspelde nieuwe indicatie | Focal stiff limb syndrome |
| TxGNN-voorspellingsscore | 0.9945 |
| Bewijsniveau | L5 |
| Marktstatus in Nederland | In de handel (geldige vergunningen: 3 van 3) |
| Aantal vergunningen | 3 (geldig: 3) |
| Aanbevolen beslissing | Hold |

---

## Waarom is deze voorspelling redelijk?

Voor deze voorspelling zijn geen gegevens over het werkingsmechanisme van metformine beschikbaar in de voor dit rapport verzamelde data. Uit algemene kennis is bekend dat metformine de AMPK-route activeert, de glucoseproductie in de lever remt en mogelijk een milde immuunmodulerende werking heeft.

Er is **geen klinisch onderbouwd mechanistisch verband** gevonden. Focal stiff limb syndrome is een zeldzame variant binnen het stiff-person-spectrum, met een vermoedelijk auto-immuun of neurologische oorzaak (verstoorde GABA-erge remming, in sommige gevallen anti-GAD65-antistoffen). De bekende werking van metformine sluit hier niet duidelijk op aan. De voorspelling komt waarschijnlijk voort uit een gedeelde diabetes-gerelateerde auto-immuniteit (anti-GAD65 komt ook voor bij type 1 diabetes) en niet uit een therapeutisch mechanisme.

**Overige voorspellingen** in dezelfde analyse (allemaal bewijsniveau L5, beslissing Hold):

| Rang | Voorspelde indicatie | Score | Korte beoordeling |
|------|------|------|------|
| 2 | Classic stiff person syndrome | 0,9945 | Identieke score als rang 1, wijst op een gedeeld grafsignaal. Metformine heeft geen bekend effect op het anti-GAD-auto-immuunmechanisme. |
| 3 | Opsismodysplasia | 0,9940 | Theoretisch verband via insuline/PI3K/AKT-signalering (SHIP2), maar speculatief en zonder preklinische of klinische data. |
| 4 | Thiamine-responsive dysfunction syndrome | 0,9940 | Diabetes maakt deel uit van het fenotype; de behandeling is thiaminesuppletie. Geen therapeutische rationale voor metformine. |
| 5 | Drug-induced localized lipodystrophy | 0,9906 | Meest aannemelijke indirecte link (insulineresistentie), maar geen bewijs dat metformine lokaal vetverlies herstelt. |

---

## Bewijs uit klinische studies

Er zijn momenteel geen gerelateerde klinische studies geregistreerd.

---

## Bewijs uit de literatuur

Er is momenteel geen gerelateerde literatuur beschikbaar.

---

## Informatie over de Nederlandse markt

| RVG-nummer | Productnaam | Toedieningsvorm | Goedgekeurde indicatie |
|---------|------|------|-----------|
| RVG 112562 | Metfocell 1000 mg, filmomhulde tabletten | Filmomhulde tablet | Niet beschikbaar |
| RVG 103395 | Metformine HCl/Glibenclamide Sandoz 500/5 mg, filmomhulde tabletten | Filmomhulde tablet | Niet beschikbaar |
| RVG 119302//27246 | Glucovance 500 mg/5 mg filmomhulde tabletten | Filmomhulde tablet | Niet beschikbaar |

Het middel is in Nederland op de markt: 3 van de 3 vergunningen zijn geldig.

---

## Veiligheidsoverwegingen

- **Contra-indicaties volgens de kennisgraaf** (afgeleid uit de TxGNN-kennisgraaf, niet uit de officiële productinformatie): onder meer leverfalen, nierziekte, pancreatitis, leverziekte, galblaasaandoening, congestief hartfalen, hypofyse-insufficiëntie (diverse vormen, waaronder hypopituïtarisme en het syndroom van Sheehan), hypogonadotroop hypogonadisme (waaronder Kallmann-syndroom), thymusaandoeningen en bijnierschorsinsufficiëntie.
- **Geneesmiddelinteracties**: in totaal zijn 907 interacties gevonden. Voorbeelden:
  - **Ernstig (Major)**: acetazolamide, ethanol (alcohol)
  - **Matig (Moderate)**: o.a. dolutegravir, abemaciclib, fenylefrine, ranitidine, formoterol, pseudo-efedrine, ketorolac, nifedipine, epinefrine, ibuprofen, ethinylestradiol, hydrocortison, salbutamol, hydrochloorthiazide, acetohexamide
  - **Licht (Minor)**: acarbose, topische hydrocortison, topisch alclometason

Voor officiële waarschuwingen en contra-indicaties: raadpleeg de SmPC (Samenvatting van de Productkenmerken) en de bijsluiter.

---

## Conclusie en vervolgstappen

**Beslissing: Hold**

**Onderbouwing:**
De voorspelling berust uitsluitend op een modelscore (bewijsniveau L5), zonder klinische studies of publicaties en zonder aannemelijk mechanistisch verband.

**Om verder te gaan is het volgende nodig:**
- Productinformatie van het CBG-MEB (SmPC/bijsluiter) met waarschuwingen en contra-indicaties; dit is een blokkerende ontbrekende gegevensbron voor de veiligheidsscreening
- Gegevens over het werkingsmechanisme van metformine (bijvoorbeeld uit DrugBank)
- Preklinisch of mechanistisch onderzoek naar een mogelijk effect bij het stiff-person-spectrum
- Een systematisch literatuuronderzoek naar metformine bij stiff-person-syndroom
- Duidelijkheid over de registratiestatus en beschikbare toedieningsvormen in Nederland
## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

