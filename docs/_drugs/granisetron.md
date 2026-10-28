---
layout: default
title: Granisetron
parent: Alleen modelvoorspelling (L5)
nav_order: 175
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Granisetron: voorspelde nieuwe indicatie Manische bipolaire stoornis (bewijsniveau L5). Oorspronkelijke indicatie: Niet beschikbaar in de samengestelde data (de vergunningstekst is lee…"
monitor_inn: "granisetron"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "acute contagious conjunctivitis", "angioedema", "allergic urticaria", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "bronchitis", "cold urticaria", "conjunctivitis"]
---

# Granisetron
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

## Granisetron: Van een antiemeticum naar manische bipolaire stoornis
{: .text-alpha }

## Samenvatting in één zin

Granisetron is een selectieve 5-HT3-receptorantagonist. Het wordt klassiek gebruikt tegen misselijkheid en braken, maar de data die voor dit rapport zijn samengesteld bevatten geen geregistreerde indicatietekst. Het TxGNN-model voorspelt dat het werkzaam kan zijn bij **manische bipolaire stoornis**, maar er zijn **geen klinische studies** en **geen publicaties** die deze richting ondersteunen: het is een zuivere modelvoorspelling.

---

## Snel overzicht

| Item | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Niet beschikbaar in de samengestelde data (de vergunningstekst is leeg) |
| Voorspelde nieuwe indicatie | Manische bipolaire stoornis |
| TxGNN-voorspellingsscore | 0,9962 |
| Bewijsniveau | L5 |
| Marktstatus in Nederland | In de handel (geldige vergunningen: 1 van 1) |
| Aantal vergunningen | 1 (geldig: 1) |
| Aanbevolen beslissing | Hold |

---

## Waarom is deze voorspelling redelijk?

Gegevens over het werkingsmechanisme van granisetron zijn in de samengestelde data niet beschikbaar. Granisetron is een selectieve 5-HT3-receptorantagonist, en dat is de basis voor de onderstaande redenering.

Bij manie wordt een ontregeling van het serotonerge en dopaminerge systeem verondersteld, en 5-HT3-antagonisme is in neuropsychiatrische aandoeningen onderzocht. Daarom is een mechanistisch verband denkbaar. Dit blijft echter speculatief: de TxGNN-score is een modelvoorspelling, er zijn geen studies of publicaties aangeleverd, en de overeenkomst met de oorspronkelijke indicatie is niet beoordeeld.

### Overige voorspelde indicaties (ter context)

Alle onderstaande voorspellingen hebben bewijsniveau L5 en de aanbeveling Hold.

| Rang | Voorspelde indicatie | Score | Mechanistische plausibiliteit |
|---|---|---|---|
| 2 | Syndroom van Gilles de la Tourette | 0,9952 | Plausibel (dopaminerge/serotonerge circuits; vergelijkbaar onderzoek met ondansetron) |
| 3 | Acute besmettelijke conjunctivitis | 0,9949 | Geen duidelijke onderbouwing |
| 4 | Angio-oedeem | 0,9936 | Zwak, speculatief |
| 5 | Allergische urticaria | 0,9932 | Speculatief (mestcellen/jeuk) |
| 6 | Nefrogeen syndroom van inadequate antidiurese | 0,9932 | Niet onderbouwd (AVPR2-mutaties) |
| 7 | Trichotillomanie | 0,9923 | Plausibel (OCD-spectrum, serotonerge betrokkenheid) |
| 8 | Bronchitis | 0,9918 | Geen duidelijke onderbouwing |
| 9 | Koude-urticaria | 0,9910 | Speculatief |
| 10 | Conjunctivitis | 0,9909 | Zwak voor allergische vorm, geen voor infectieuze vormen |

---

## Klinisch trialbewijs

Er zijn momenteel geen gerelateerde klinische studies geregistreerd.

---

## Literatuurbewijs

Er is momenteel geen gerelateerde literatuur beschikbaar.

---

## Informatie over de Nederlandse markt

| RVG-nummer | Productnaam | Toedieningsvorm | Goedgekeurde indicatie |
|---------|------|------|-----------|
| RVG 113483 | Granisetron Claris 1 mg/ml, oplossing voor injectie (status: geldig) | Niet vermeld | Niet vermeld |

Er is 1 geldige vergunning (van 1) voor granisetron bij het CBG-MEB in de data aangetroffen; het middel is in Nederland op de markt.

---

## Veiligheidsoverwegingen

**Contra-indicaties uit de kennisgraaf** (afgeleid uit geneesmiddel-ziekte-relaties in de TxGNN-kennisgraaf PrimeKG, niet uit de bijsluitertekst):
- Lange-QT-syndroom
- Familiair lange-QT-syndroom
- Kaliumtekort
- Plotselinge hartstilstand
- Geleidingsstoornissen van het hart

**Geneesmiddelinteracties:** in totaal 654 interacties gevonden. Hieronder een selectie van de ernstige (Major) interacties:
- Fentanyl
- Dextromethorfan
- Tramadol
- Alfentanil
- Almotriptan
- Sumatriptan
- Amiodaron
- Amisulpride
- Amitriptyline
- Anagrelide

Daarnaast zijn er interacties van matig niveau (Moderate), onder andere met abametapir (topisch), abirateron, dihydrocodeïne, codeïne, famotidine, formoterol, adenosine, salbutamol, alfuzosine, propofol.

Veel van deze combinaties hangen samen met serotonerge effecten of QT-verlenging, wat past bij de hierboven genoemde cardiale contra-indicaties in de kennisgraaf.

Voor volledige veiligheidsinformatie (waarschuwingen en contra-indicaties volgens de vergunning) raadpleeg de SmPC (Samenvatting van de Productkenmerken).

---

## Conclusie en vervolgstappen

**Beslissing: Hold**

**Onderbouwing:**
- De voorspelling voor manische bipolaire stoornis is uitsluitend gebaseerd op een model (L5), zonder klinische studies of literatuur. Het middel is in Nederland wel op de markt (1 geldige vergunning van 1), maar de oorspronkelijke indicatietekst en de officiële veiligheidsinformatie ontbreken.

**Om verder te gaan is het volgende nodig:**
- De bijsluiter/SmPC-gegevens (waarschuwingen en contra-indicaties) van het CBG-MEB ophalen; dit is een blokkerende leemte voor de veiligheidsscreening
- Gegevens over het werkingsmechanisme aanvullen vanuit DrugBank
- Systematisch zoeken naar preklinische en klinische studies naar granisetron bij manie
- Beoordelen of er een toedieningsroute beschikbaar is die past bij de beoogde indicatie (orale vorm voor psychiatrisch gebruik), gezien de enige bekende vergunning een injectievloeistof betrof
- Een cardiale veiligheidsbeoordeling (QT-verlenging) en een plan voor interactiebewaking, gezien de vele ernstige interacties
## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

