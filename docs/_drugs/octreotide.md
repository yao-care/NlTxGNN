---
layout: default
title: Octreotide
parent: Alleen modelvoorspelling (L5)
nav_order: 250
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
monitor_inn: "octreotide"
predicted_indications: ["vulvar inverted follicular keratosis", "seborrheic keratosis"]
description: "Octreotide: voorspelde nieuwe indicatie Vulvaire inverted follicular keratosis (vulvar inverted follicular keratosis) (bewijsniveau L5). Oorspronkelijke indicatie: Niet vermeld in de lokale gegevens"
---

# Octreotide
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **2** 
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

## Octreotide: Vulvaire inverted follicular keratosis (vulvar inverted follicular keratosis)
{: .text-alpha }

## Samenvatting in één zin

Octreotide is een somatostatine-analoog die oorspronkelijk wordt gebruikt bij acromegalie, hyperpituïtarisme en het carcinoïdsyndroom. Het TxGNN-model voorspelt dat het mogelijk werkzaam is bij **vulvaire inverted follicular keratosis** (en als tweede voorspelling bij **seborrheic keratosis**). Hiervoor zijn **geen klinische studies** en **geen publicaties** gevonden; de voorspelling berust uitsluitend op het model.

---

## Snel overzicht

| Item | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Niet vermeld in de lokale gegevens |
| Voorspelde nieuwe indicatie | Vulvaire inverted follicular keratosis (vulvar inverted follicular keratosis) |
| TxGNN-voorspellingsscore | 0.9958 |
| Evidentieniveau | L5 |
| Marktstatus in Nederland | In de handel (geldige vergunningen: 1 van 1) |
| Aantal vergunningen | 1 (geldig: 1) |
| Aanbevolen besluit | Hold |

---

## Waarom is deze voorspelling aannemelijk?

Gedetailleerde gegevens over het werkingsmechanisme zijn momenteel niet beschikbaar in de voor dit rapport samengestelde data. Octreotide is bekend als somatostatine-analoog die vooral aan somatostatinereceptoren (SSTR2/SSTR5) bindt en hormoonafgifte remt. Het is werkzaam bij acromegalie en neuro-endocriene tumoren.

Een mogelijk verband met de voorspelde indicatie zou een remmend effect op groeifactorsignalering (zoals IGF-1/EGFR) of op de proliferatie van keratinocyten kunnen zijn. Dit is **speculatief** en wordt door geen enkel gegeven ondersteund. Inverted follicular keratosis is een goedaardige, zelflimiterende huidafwijking die meestal door eenvoudige excisie wordt behandeld, en de vulvaire locatie is zeer zeldzaam. De behoefte aan een systemische peptidetherapie is dus zeer laag.

De tweede voorspelling, seborrheic keratosis (score 0,9955), is eveneens een veelvoorkomende goedaardige afwijking met effectieve lokale behandelingen (cryotherapie, curettage, waterstofperoxide topisch). De bijna identieke scores en de gelijksoortige ziekteklasse wijzen er mogelijk op dat de score van het TxGNN-model (deep learning) overeenkomsten weerspiegelt die het model heeft geleerd tussen verwante ziekten (goedaardige epidermale neoplasie), en niet op biologisch bewijs of een geneesmiddelspecifiek signaal.

---

## Klinische studies

Momenteel zijn er geen gerelateerde klinische studies geregistreerd.

---

## Literatuur

Momenteel is er geen gerelateerde literatuur beschikbaar.

<!-- review:begin nl-lic-20261106-octreotide-1 -->

> **Controlecorrectie (2026-11-06)**: Oorspronkelijk stond er: “Er is één vergunning, en deze is doorgehaald.” Verwijderd: de vermelding dat de vergunningen zijn doorgehaald of dat er geen geldige vergunning is, kwam niet overeen met de registratiegegevens van het CBG (2026-11-06). Aantal vergunningen in de gegevens: 1, waarvan geldig: 1; actuele aantallen staan in het snelle overzicht en bij de marktinformatie. Bron: [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/).

<!-- review:end nl-lic-20261106-octreotide-1 -->

---

## Informatie over de Nederlandse markt

| RVG-nummer | Productnaam | Toedieningsvorm | Goedgekeurde indicatie |
|---------|------|------|-----------|
| RVG 120241//18236 | Sandostatine LAR 20 mg | Niet vermeld | Niet vermeld (status: geldig) |

---

## Veiligheidsoverwegingen

**Contra-indicaties volgens de kennisgraaf** (afgeleid uit de TxGNN-kennisgraaf, niet uit de officiële productinformatie):
hyperglykemie, hypothyreoïdie, myxoedeem, congenitale hypothyreoïdie, levercirrose, diabetes mellitus, diabetische ketoacidose, galblaasaandoeningen, leveraandoeningen, ileus, darmobstructie, plotselinge hartstilstand, hartgeleidingsstoornissen, hypoglykemie, cholelithiasis, cholecystolithiasis, choledocholithiasis, nierfalen, uremie en vitamine B12-deficiëntie.

**Geneesmiddelinteracties:** In totaal zijn 423 interacties gevonden. De weergegeven interacties zijn van gemiddeld niveau en betreffen vooral bloedglucoseverlagende middelen:
- Orale antidiabetica en incretine-gerelateerde middelen: acarbose, albiglutide, alogliptine, metformine, canagliflozine, chloorpropamide, dapagliflozine, dulaglutide, empagliflozine, glimepiride, semaglutide, linagliptine
- Insulines: aspart, degludec, detemir, glargine, glulisine, humane insuline (isophane, inhalatie, regular)

Voor de officiële waarschuwingen en contra-indicaties raadpleeg de SmPC en de bijsluiter (PIL) via het CBG-MEB.

---

## Conclusie en vervolgstappen

**Besluit: Hold**

**Onderbouwing:**
- De voorspelling steunt alleen op een hoge modelscore, zonder klinische studies of literatuur (L5).

<!-- review:begin nl-lic-20261106-octreotide-2 -->

> **Controlecorrectie (2026-11-06)**: Oorspronkelijk stond er: “De voorspelling steunt alleen op een hoge modelscore, zonder klinische studies of literatuur (L5). Daarbij is de voorspelde indicatie goedaardig met effectieve lokale behandelingen, is er een grote interactielast en is de enige Nederlandse vergunning doorgehaald.” Verwijderd: de vermelding dat de vergunningen zijn doorgehaald of dat er geen geldige vergunning is, kwam niet overeen met de registratiegegevens van het CBG (2026-11-06). Aantal vergunningen in de gegevens: 1, waarvan geldig: 1; actuele aantallen staan in het snelle overzicht en bij de marktinformatie. Bron: [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/).

<!-- review:end nl-lic-20261106-octreotide-2 -->

**Om verder te gaan is het volgende nodig:**
- Productinformatie (SmPC/bijsluiter) van het CBG-MEB om de veiligheid te beoordelen; dit ontbreekt nu en blokkeert verdere veiligheidsscreening
- Gegevens over het werkingsmechanisme (bijv. uit DrugBank) om een mechanistisch verband te toetsen
- Preklinisch of literatuurbewijs dat somatostatinereceptoren een rol spelen bij keratinocytproliferatie
- Een beoordeling van de behoefte en het voordeel-risicoprofiel ten opzichte van bestaande lokale behandelingen
- Duidelijkheid over de beschikbare toedieningswegen en de huidige vergunningsstatus in Nederland

<!-- review:begin log -->

## Controlelogboek

Hieronder staat het controlelogboek van deze pagina: gegevens gecontroleerd aan de hand van de registratiegegevens van het CBG (College ter Beoordeling van Geneesmiddelen). Correcties betreffen alleen feitelijke basisgegevens; modelvoorspellingen, bewijsniveaus en conclusies zijn niet herschreven.

| Controledatum | Onderdeel | Actie | Bron |
|------|------|------|------|
| 2026-11-06 | Verwijderd: “Er is één vergunning, en deze is doorgehaald” | Gecorrigeerd | [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/) |
| 2026-11-06 | Verwijderd: “Daarbij is de voorspelde indicatie goedaardig met effectieve lokale behandelingen, is er een grote interactielast en is de enige Nederlandse” | Gecorrigeerd | [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/) |

<!-- review:end log -->

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

