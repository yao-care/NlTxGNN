---
layout: default
title: Colchicine
parent: Alleen modelvoorspelling (L5)
nav_order: 96
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Colchicine: voorspelde nieuwe indicatie Plasmodium falciparum-malaria (bewijsniveau L5). Oorspronkelijke indicatie: Jicht"
monitor_inn: "Colchicine"
predicted_indications: ["Plasmodium falciparum malaria", "dermatofibrosarcoma protuberans"]
---

# Colchicine
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

## Colchicine: Van jicht en familiaire mediterrane koorts naar Plasmodium falciparum-malaria
{: .text-alpha }

## Samenvatting in één zin

Colchicine wordt van oudsher gebruikt bij jicht en familiaire mediterrane koorts (FMF). Het TxGNN-model voorspelt dat het mogelijk werkzaam is bij **Plasmodium falciparum-malaria**, maar er zijn **geen klinische studies** en slechts **2 publicaties** met alleen indirecte, preklinische ondersteuning. Het bewijs berust dus vrijwel uitsluitend op een computationele voorspelling.

---

## Snel overzicht

| Item | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Jicht; familiaire mediterrane koorts (FMF) |
| Voorspelde nieuwe indicatie | Plasmodium falciparum-malaria |
| TxGNN-voorspellingsscore | 0,9960 |
| Bewijsniveau | L5 |
| Marktstatus in Nederland | In de handel (geldige vergunningen: 1 van 1) |
| Aantal vergunningen | 1 (geldig: 1) |
| Aanbevolen besluit | Hold |

In de Nederlandse vergunningsgegevens is geen indicatietekst beschikbaar.*

---

## Waarom is deze voorspelling redelijk?

Colchicine is een stof die microtubuli verstoort: het bindt aan tubuline en remt de polymerisatie. Plasmodium falciparum heeft microtubuli nodig voor celdeling, intracellulaire ontwikkeling en invasie van gastheercellen. Een tubuline-gericht mechanisme is daarom biologisch denkbaar.

De opgehaalde literatuur ondersteunt dit slechts indirect. Eén artikel onderzoekt curcumine (niet colchicine) en de verstoring van parasitaire microtubuli. Het andere artikel beschrijft dat expressie van het pfmdr1-gen in zoogdiercellen de gevoeligheid voor chloroquine verandert; colchicine is daarin vermoedelijk gebruikt als P-glycoproteïne-substraat. Geen van beide laat antimalariawerking van colchicine bij patiënten zien.

Daar komt bij dat colchicine een smalle therapeutische breedte heeft. De doses die nodig zouden zijn om parasitair tubuline te beïnvloeden, geven waarschijnlijk toxiciteit bij de gastheer. Gegevens over het precieze werkingsmechanisme van colchicine zijn in de voor dit rapport samengestelde data niet beschikbaar; bovenstaande mechanistische redenering is algemene kennis en geen onderdeel van de aangeleverde gegevens.

---

## Klinisch trialbewijs

Momenteel geen gerelateerde klinische studies geregistreerd.

---

## Literatuurbewijs

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|-----|------|------|---------|
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | Preklinisch (in vitro) | PLoS One | Curcumine verstoort microtubuli van P. falciparum; betreft curcumine, niet colchicine |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | Preklinisch (celgebaseerd) | Molecular and Cellular Biology | Expressie van pfmdr1 in zoogdiercellen gaat gepaard met grotere gevoeligheid voor chloroquine |

---

## Informatie over de Nederlandse markt

| RVG-nummer | Productnaam | Toedieningsvorm | Goedgekeurde indicatie |
|---------|------|------|-----------|
| RVG 115060 | Colchicine Tiofarma 1 mg, tabletten | Niet beschikbaar | Niet beschikbaar (vergunning geldig) |

---

## Cytotoxiciteit

Colchicine is geen antineoplastisch middel in zijn geregistreerde indicaties (jicht, FMF). Dit onderdeel is daarom niet van toepassing op de hoofdvoorspelling.

---

## Veiligheidsoverwegingen

- **Contra-indicaties volgens de kennisgraaf** (afgeleid uit relaties tussen geneesmiddel en ziekte in het model, niet uit de officiële productinformatie): onder meer leverfalen, nierfunctiestoornissen, bloedziekten (trombocytopenie, leukopenie, agranulocytose, neutropenie, aplastische anemie), maagzweer, spier- en myopathieaandoeningen (waaronder rabdomyolyse), diarree-aandoeningen en acute urinezuurnefropathie.
- **Geneesmiddelinteracties**: in totaal 100 interacties gevonden; hieronder een selectie.
  - *Ernstig (Major)*: aprepitant, claritromycine, eliglustat, rolapitant, rosuvastatine, simvastatine, cobicistat, deferipron.
  - *Matig (Moderate)*: metronidazol, cimetidine, eluxadoline, miconazol, tinidazol, deferasirox, strontiumchloride Sr-89, fostamatinib, ticagrelor, chloroquine, benznidazol, disulfiram.
  - Het is relevant dat chloroquine, een standaard antimalariamiddel, een matige interactie heeft met colchicine.

Raadpleeg voor de officiële waarschuwingen en contra-indicaties de SmPC (Samenvatting van de Productkenmerken) en de bijsluiter. De productinformatie van het CBG-MEB was voor dit rapport niet beschikbaar.

---

## Overige voorspelde indicaties (ter volledigheid)

| Voorspelde indicatie | TxGNN-score | Bewijsniveau | Opmerking |
|------|------|------|------|
| Dermatofibrosarcoma protuberans | 0,9937 | L5 | Geen trials of literatuur. Theoretisch zou de antimitotische werking proliferende tumorcellen kunnen beïnvloeden, maar er is geen bewijs voor werking op de COL1A1-PDGFB-driver en de systemische toxiciteit pleit tegen gebruik. |

---

## Conclusie en vervolgstappen

**Besluit: Hold**

**Onderbouwing:**
- De hoge TxGNN-score (0,9960) is een puur computationele voorspelling. Er zijn geen klinische studies en het preklinische bewijs is indirect (curcumine, chloroquine-gevoeligheid). De smalle therapeutische breedte van colchicine maakt de benodigde dosering voor antiparasitaire werking onwaarschijnlijk veilig. Colchicine is in Nederland op de markt, met 1 geldige vergunning van 1.

**Om verder te gaan is nodig:**
- Preklinische gegevens over de directe werking van colchicine op P. falciparum (in vitro en in vivo, inclusief concentraties ten opzichte van de toxische gastheerdosis).
- Gegevens over het werkingsmechanisme uit DrugBank.
- De officiële waarschuwingen en contra-indicaties uit de CBG-MEB-productinformatie (SmPC), nodig voor een veiligheidsscreening.
- Een beoordeling van de veiligheid bij combinatie met standaard antimalariamiddelen, zoals chloroquine.
- Besluit over de vergunningsstatus in Nederland (de enige vergunning is ingetrokken).
## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

