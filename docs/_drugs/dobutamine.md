---
layout: default
title: Dobutamine
parent: Alleen modelvoorspelling (L5)
nav_order: 118
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Dobutamine: voorspelde nieuwe indicatie Alopecia (bewijsniveau L5). Oorspronkelijke indicatie: Niet beschikbaar in de voor dit rapport samengestelde gegevens"
monitor_inn: "dobutamine"
predicted_indications: ["alopecia", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "open-angle glaucoma", "Raynaud disease", "primary hereditary glaucoma", "headache disorder", "hypertrichosis (disease)", "migraine disorder"]
---

# Dobutamine
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **10** 
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

## Dobutamine: Van de oorspronkelijke indicatie naar alopecia (haaruitval)
{: .text-alpha }

## Samenvatting in één zin

Dobutamine is een bèta-1-adrenerge agonist en inotroop middel dat intraveneus wordt gebruikt. De oorspronkelijke indicatie is in de beschikbare vergunningsgegevens niet vermeld. Het TxGNN-model voorspelt dat dobutamine werkzaam kan zijn bij **alopecia**, maar er zijn **0 klinische studies** en slechts **1 publicatie** (een veterinaire casuïstiek, geen bewijs van werkzaamheid). Deze voorspelling is vermoedelijk een artefact van het model.

---

## Snel overzicht

| Item | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Niet beschikbaar in de voor dit rapport samengestelde gegevens |
| Voorspelde nieuwe indicatie | Alopecia |
| TxGNN-voorspellingsscore | 99,85% |
| Bewijsniveau | L5 |
| Marktstatus in Nederland | Alleen doorgehaald (vergunning ingetrokken) |
| Aantal vergunningen | 1 (0 geldig, 1 doorgehaald) |
| Aanbevolen beslissing | Hold |

---

## Waarom is deze voorspelling (on)aannemelijk?

Gedetailleerde gegevens over het werkingsmechanisme zijn momenteel niet beschikbaar. Dobutamine is een bèta-1-adrenerge agonist die de hartcontractiliteit verhoogt. Het wordt intraveneus toegediend bij acuut hartfalen en voor stressechocardiografie.

Er is **geen plausibele mechanistische link** met haarfollikelbiologie. De hoge score van 99,85% is waarschijnlijk een grafartefact: in het kennisnetwerk ligt dobutamine dicht bij cardiovasculaire geneesmiddelen zoals minoxidil, een vaatverwijder die wél met haargroei wordt geassocieerd (ook als bijwerking, hypertrichose). Die nabijheid in het netwerk is geen bewijs dat dobutamine werkt.

Ook de overige voorspellingen met hoge scores (hypotrichosis simplex van de hoofdhuid, congenitale hypotrichosis milia, diffuse alopecia areata, glaucoom, ziekte van Raynaud, hoofdpijn, hypertrichose en migraine) kennen geen klinische of mechanistische onderbouwing.

---

## Klinisch trialbewijs

Er zijn momenteel geen gerelateerde klinische studies geregistreerd.

---

## Literatuurbewijs

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|-----|------|------|---------|
| [41046802](https://pubmed.ncbi.nlm.nih.gov/41046802/) | 2025 | Casuïstiek (veterinair) | Journal of Veterinary Cardiology | Hartfalen bij een kat door minoxidilvergiftiging; dobutamine werd gebruikt vanwege hypotensie. Geen bewijs voor werking bij haaruitval. |

---

## Informatie over de Nederlandse markt

| RVG-nummer | Productnaam | Toedieningsvorm | Goedgekeurde indicatie |
|---------|------|------|-----------|
| RVG 107115 | Dobutamine Claris 12,5 mg/ml, concentraat voor oplossing voor infusie | Concentraat voor oplossing voor infusie | Niet beschikbaar (vergunning doorgehaald) |

---

## Veiligheidsoverwegingen

- **Contra-indicaties volgens het kennisnetwerk** (afgeleid uit TxGNN/PrimeKG, niet uit de bijsluitertekst): hypertensieve aandoeningen, hypertensie, kaliumtekort, boezemfibrilleren, aortastenose (inclusief aortaklepaandoeningen en supravalvulaire aortastenose), myocardinfarct en coronaire trombose, hemoglobinopathie, hypertrofische cardiomyopathie (inclusief familiaire vorm).
- **Geneesmiddelinteracties**: in totaal 115 interacties gevonden; de weergegeven interacties zijn van gemiddeld niveau. Het gaat vooral om antidiabetica (o.a. acarbose, metformine, pioglitazon, repaglinide, insuline degludec en insuline aspart, GLP-1-agonisten zoals liraglutide, semaglutide, dulaglutide en albiglutide, SGLT2-remmers zoals canagliflozine, dapagliflozine en empagliflozine, en DPP-4-remmers zoals alogliptine en linagliptine), daarnaast chloorpropamide, cimetidine, diëthylpropion, fentermine en vancomycine.

Raadpleeg voor waarschuwingen en contra-indicaties volgens de officiële tekst de SmPC (Samenvatting van de Productkenmerken) en de bijsluiter van het CBG-MEB. Die gegevens ontbreken in de samengestelde gegevens.

---

## Conclusie en vervolgstappen

**Beslissing: Hold**

**Onderbouwing:**
- De voorspelling berust uitsluitend op het model (L5). Er zijn geen klinische studies, en de enige gevonden publicatie is een veterinaire casuïstiek zonder bewijs van werkzaamheid. Er is geen plausibel werkingsmechanisme, en intraveneuze toediening van een hartstimulerend middel past niet bij haaruitval. Bovendien is de enige Nederlandse vergunning doorgehaald.

**Om verder te gaan is het volgende nodig:**
- Gegevens over het werkingsmechanisme (DrugBank) en de officiële veiligheidsinformatie uit de SmPC van het CBG-MEB
- Preklinisch onderzoek naar een effect van bèta-1-agonisme op haarfollikels
- Beoordeling van de toedieningsroute (intraveneus versus lokaal), aangezien die momenteel niet bij de voorspelde indicatie past
- Een heroverweging van de modelvoorspelling, gezien het waarschijnlijke grafartefact via minoxidil
## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

