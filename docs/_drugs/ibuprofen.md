---
layout: default
title: Ibuprofen
parent: Alleen modelvoorspelling (L5)
nav_order: 181
evidence_level: L5
indication_count: 7
---

# Ibuprofen
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **7** 
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

# Ibuprofen: Van reumatoïde artritis naar acromesomelische dysplasie, type Hunter-Thompson

## Samenvatting in één zin

Ibuprofen is een niet-selectieve COX-remmer (NSAID) die oorspronkelijk wordt gebruikt bij reumatoïde artritis, artrose en andere gewrichtsaandoeningen, hoofdpijn en een open ductus arteriosus. Het TxGNN-model voorspelt dat het mogelijk werkzaam is bij **acromesomelische dysplasie, type Hunter-Thompson**, maar hiervoor zijn **geen klinische studies** en **geen publicaties** gevonden. De voorspelling berust uitsluitend op een modelscore.

## Snel overzicht

| Item | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Reumatoïde artritis, artrose, juveniele idiopathische artritis, hoofdpijn en open ductus arteriosus (op basis van de kennisgraaf; er is geen geregistreerde indicatietekst beschikbaar) |
| Voorspelde nieuwe indicatie | Acromesomelische dysplasie, type Hunter-Thompson |
| TxGNN-voorspellingsscore | 99,74% |
| Bewijsniveau | L5 |
| Marktstatus in Nederland | Alleen doorgehaalde registratie (vervallen) |
| Aantal vergunningen | 1 (geen geldige) |
| Aanbevolen beslissing | Hold |

## Waarom is deze voorspelling (on)aannemelijk?

Gegevens over het werkingsmechanisme van ibuprofen zijn voor dit rapport niet beschikbaar. Algemeen bekend is dat ibuprofen een niet-selectieve COX-remmer is met ontstekingsremmende en pijnstillende werking.

Acromesomelische dysplasie, type Hunter-Thompson is een zeldzame skeletdysplasie. De oorzaak is functieverlies van CDMP1/GDF5, wat de aanleg van kraakbeen en bot verstoort. Ibuprofen werkt niet op GDF5/BMP-signalering. Er is dus **geen onderbouwd mechanistisch verband**.

De hoge modelscore (0,997) komt waarschijnlijk voort uit nabijheid in de kennisgraaf tot gewrichts- en skeletaandoeningen zoals artropathie en artrose, en niet uit een biologische rationale. Hooguit zou ibuprofen symptomatisch pijn kunnen verlichten, maar dat is niet aangetoond.

## Klinisch trialbewijs

Momenteel zijn er geen gerelateerde klinische studies geregistreerd.

## Literatuurbewijs

Momenteel is er geen gerelateerde literatuur beschikbaar.

## Informatie over de Nederlandse markt

| RVG-nummer | Productnaam | Toedieningsvorm | Goedgekeurde indicatie |
|---------|------|------|-----------|
| RVG 119085 | Etos Ibuprofen Liquid Caps 200 mg, zachte capsules (vervallen) | Zachte capsule | Niet beschikbaar |

## Veiligheidsoverwegingen

Voor de veiligheid is geen tekst uit de bijsluiter of SmPC verwerkt in de data die voor dit rapport is samengesteld. Raadpleeg daarom de SmPC (Samenvatting van de Productkenmerken) en de bijsluiter via het CBG-MEB.

- **Contra-indicaties en aandoeningen met voorzichtigheid (uit de kennisgraaf, geen labeltekst)**: de kennisgraaf koppelt ibuprofen aan onder meer de volgende aandoeningen:
  - hypertensie en hypotensie;
  - lever-, nier- en galblaasaandoeningen;
  - maagzweer en inflammatoire darmziekte;
  - bloedstollingsstoornissen en trombocytopenie;
  - beroerte, hersenaandoeningen en myocardinfarct;
  - COPD, epilepsie en systemische lupus erythematodes;
  - diabetes mellitus, diabetische ketoacidose en kaliumtekort;
  - hypothyreoïdie, benigne prostaathyperplasie en middelenmisbruik.
- **Geneesmiddelinteracties**: 100 interacties gevonden; hieronder de belangrijkste uit de weergegeven selectie.
  - **Ernstig (Major)**: acetylsalicylzuur.
  - **Matig (Moderate)**: corticosteroïden (dexamethason, hydrocortison, betamethason, budesonide), sulfonylureumderivaten (glimepiride, glipizide, glibenclamide, chloorpropamide, acetohexamide), exenatide, levofloxacine, kanamycine, aprepitant, balsalazide, fenfluramine en dexfenfluramine.
  - **Licht (Minor)**: H2-blokkers (famotidine, ranitidine, cimetidine).
- **Zwangerschap**: bij de voorspelde aangeboren afwijkingen speelt mee dat NSAID-gebruik in de zwangerschap veiligheidsrisico's voor de foetus kent.

## Overige voorspelde indicaties (ter volledigheid)

Alle onderstaande voorspellingen hebben bewijsniveau L5 en de aanbeveling Hold. Er zijn voor geen enkele klinische studies of literatuur gevonden.

| Rang | Aandoening | Score | Beoordeling mechanistisch verband |
|---|---|---|---|
| 2 | Brachyolmie-amelogenesis imperfecta-syndroom | 99,71% | Geen onderbouwd verband |
| 3 | Myosclerose | 99,68% | Zwak, speculatief (hooguit symptomatische pijnverlichting) |
| 4 | Brachyolmie | 99,67% | Geen onderbouwd verband |
| 5 | Brachydactylie-syndactylie-syndroom | 99,66% | Geen onderbouwd verband; foetale veiligheidszorgen |
| 6 | Pseudoachondroplasie | 99,66% | Indirect en alleen symptomatisch (gewrichtspijn) |
| 7 | Colobomateuze microftalmie-rizomele dysplasie-syndroom | 99,60% | Geen onderbouwd verband |

## Conclusie en vervolgstappen

**Beslissing: Hold**

**Onderbouwing:**
- De voorspelling berust alleen op een modelscore (bewijsniveau L5), zonder klinische studies of literatuur en zonder aannemelijk mechanistisch verband met de onderliggende genetische oorzaak.
- De enige Nederlandse registratie is vervallen, en gegevens over waarschuwingen en contra-indicaties ontbreken. Daardoor kan de veiligheidsscreening niet worden afgerond.

**Om verder te gaan is nodig:**
- Bijsluitertekst van het CBG-MEB (waarschuwingen en contra-indicaties) ophalen en verwerken.
- Gegevens over het werkingsmechanisme aanvullen, bijvoorbeeld via DrugBank.
- Preklinisch of mechanistisch bewijs verzamelen dat COX-remming relevant is voor de ziekte.
- Beoordelen of symptomatisch gebruik (pijnbestrijding) klinisch zinvol en veilig is, met aandacht voor kinderen en zwangerschap.
- De actuele marktstatus en beschikbare toedieningsvormen in Nederland verifiëren.
## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

