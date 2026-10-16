---
layout: default
title: Lanreotide
parent: Alleen modelvoorspelling (L5)
nav_order: 197
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Lanreotide: voorspelde nieuwe indicatie Hypertrichose (bewijsniveau L5). Oorspronkelijke indicatie: Acromegalie, hyperpituïtarisme, hypofysaire gigantisme"
monitor_inn: "lanreotide"
predicted_indications: ["hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "Ambras type hypertrichosis universalis congenita"]
---

# Lanreotide
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **5** 
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

# Lanreotide: Van acromegalie naar hypertrichose

## Samenvatting in één zin

Lanreotide is een somatostatine-analoog dat oorspronkelijk wordt gebruikt bij de behandeling van acromegalie, hypofyse-hyperfunctie en hypofysaire gigantisme. Het TxGNN-model voorspelt dat het mogelijk werkzaam is bij **hypertrichose**, maar er zijn **geen geregistreerde klinische studies** en **geen publicaties** die deze richting ondersteunen; de voorspelling berust uitsluitend op een computermodel.

---

## Snel overzicht

| Item | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Acromegalie, hyperpituïtarisme, hypofysaire gigantisme (volgens de indicatierelaties in de kennisgraaf; geen geregistreerde indicatietekst beschikbaar) |
| Voorspelde nieuwe indicatie | Hypertrichose |
| TxGNN-voorspellingsscore | 99,97% |
| Bewijsniveau | L5 |
| Marktstatus in Nederland | Alleen ingetrokken (geen geldige handelsvergunning) |
| Aantal vergunningen | 1 (ingetrokken) |
| Aanbevolen beslissing | Hold |

---

## Waarom is deze voorspelling (on)aannemelijk?

Gegevens over het werkingsmechanisme van lanreotide zijn in de voor dit rapport samengestelde data niet beschikbaar. Lanreotide is een somatostatine-analoog dat de afgifte van groeihormoon (GH) en IGF-1 onderdrukt, wat de werkzaamheid bij acromegalie verklaart.

Een mogelijk verband met hypertrichose is slechts speculatief: IGF-1-signalering beïnvloedt de groei van haarfollikels. Hypertrichose is echter geen vastgesteld gevolg van somatostatinereceptormodulatie en is juist vaker een bijwerking van andere geneesmiddelen dan een aandoening die met somatostatine-analogen wordt behandeld. De zeer hoge score (0,9997) is een rekenkundige voorspelling zonder bevestiging uit studies of literatuur.

Ook de overige voorspellingen zijn mechanistisch niet onderbouwd:

| Rang | Voorspelde aandoening | Score | Beoordeling |
|------|------|------|------|
| 2 | Malformatiesyndroom met tand- en/of parodontale component | 99,96% | Geen aantoonbaar farmacologisch verband; waarschijnlijk netwerknabijheid in de kennisgraaf |
| 3 | Syndroom met Dandy-Walker-malformatie als hoofdkenmerk | 99,96% | Een structurele aangeboren afwijking reageert naar verwachting niet op een somatostatine-analoog |
| 4 | Geïsoleerde erfelijke haarschachtafwijking | 99,96% | Monogene structurele defecten; speculatief IGF-1-verband, geen correctie verwacht |
| 5 | Ambras-type hypertrichosis universalis congenita | 99,96% | Genetische oorzaak (o.a. 8q-herschikkingen, TRPS1); geen verband met somatostatinesignalering |

Alle vijf voorspellingen hebben bewijsniveau L5 en zijn uitsluitend hypothesegenererend.

---

## Klinisch trialbewijs

Momenteel zijn er geen gerelateerde klinische studies geregistreerd.

---

## Literatuurbewijs

Momenteel is er geen gerelateerde literatuur beschikbaar.

---

## Informatie over de Nederlandse markt

| RVG-nummer | Productnaam | Toedieningsvorm | Goedgekeurde indicatie |
|---------|------|------|-----------|
| RVG 120433//26303 | Somatuline AutoSolution 120 mg, oplossing voor injectie in een voorgevulde spuit | Oplossing voor injectie (voorgevulde spuit) | Niet beschikbaar |

Deze vergunning is ingetrokken. Er is momenteel dus geen geldige handelsvergunning voor lanreotide in de samengestelde CBG-MEB-gegevens.

---

## Veiligheidsoverwegingen

- **Contra-indicaties/waarschuwingen uit de kennisgraaf** (afgeleid uit relaties tussen geneesmiddel en ziekte, niet uit de bijsluitertekst): hypertensieve aandoeningen/hypertensie, leverziekte, galblaasaandoeningen, hyperglykemie, hypoglykemie, hypothyreoïdie (incl. myxoedeem en congenitale hypothyreoïdie), verminderde nierfunctie, cholelithiase, cholecystolithiase en choledocholithiase.
- **Geneesmiddelinteracties**: in totaal 196 interacties gevonden. In de weergegeven selectie gaat het om interacties van matig niveau, vooral met bloedglucoseverlagende middelen, waaronder acarbose, metformine, pioglitazon, glimepiride, chloorpropamide, alogliptine, linagliptine, canagliflozine, dapagliflozine, empagliflozine, albiglutide, dulaglutide, semaglutide en diverse insulines (aspart, degludec, detemir, glargine, glulisine, humaan isophaan en humaan regulier). Bij gelijktijdig gebruik is monitoring van de bloedglucose nodig.

Raadpleeg voor de officiële waarschuwingen en contra-indicaties de SmPC (Samenvatting van de Productkenmerken) en de bijsluiter (PIL).

---

## Conclusie en vervolgstappen

**Beslissing: Hold**

**Onderbouwing:**
- De voorspelling voor hypertrichose berust uitsluitend op een computermodel (L5), zonder klinische studies of literatuur, en het mechanistische verband is zwak. Bovendien is de enige Nederlandse vergunning ingetrokken.

**Om verder te gaan is nodig:**
- Gegevens over het werkingsmechanisme (bijv. via DrugBank) voor een mechanistische analyse
- Waarschuwingen en contra-indicaties uit de CBG-MEB-bijsluiter (SmPC) voor veiligheidsscreening
- Systematisch literatuuronderzoek en preklinisch onderzoek naar IGF-1/GH-signalering in haarfollikels
- Verduidelijking van de vergunningsstatus en beschikbare toedieningsroutes in Nederland (elders geregistreerde lanreotideproducten)
- Kritische evaluatie of de voorspelde aandoeningen klinisch relevant zijn, gezien hun vooral genetische of structurele oorsprong
## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

