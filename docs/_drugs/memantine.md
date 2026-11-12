---
layout: default
title: Memantine
parent: Alleen modelvoorspelling (L5)
nav_order: 221
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-12
description: "Memantine: voorspelde nieuwe indicatie Pulmonale hypertensie (bewijsniveau L5). Oorspronkelijke indicatie: Niet vermeld in de vergunningsgegevens (algemeen bekend: matige tot e…"
monitor_inn: "memantine"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "kyphoscoliotic heart disease", "migraine with brainstem aura"]
---

# Memantine
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **4** 
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

## Memantine: van de oorspronkelijke indicatie naar pulmonale hypertensie
{: .text-alpha }

## Samenvatting in één zin

Memantine is een NMDA-receptorantagonist die algemeen wordt gebruikt bij dementie van het Alzheimer-type (deze indicatie staat niet in de vergunningsgegevens, maar komt uit algemene farmacologische kennis). Het TxGNN-model voorspelt dat memantine werkzaam kan zijn bij **pulmonale hypertensie**. Daar staan **geen klinische studies** en **2 publicaties** tegenover, die geen van beide de werkzaamheid van memantine bij deze aandoening aantonen.

---

## Snel overzicht

| Item | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Niet vermeld in de vergunningsgegevens (algemeen bekend: matige tot ernstige ziekte van Alzheimer) |
| Voorspelde nieuwe indicatie | Pulmonale hypertensie |
| TxGNN-voorspellingsscore | 0.9954 |
| Bewijsniveau | L5 |
| Marktstatus in Nederland | In de handel (geldige vergunningen: 31 van 32) |
| Aantal vergunningen | 32 (geldig: 31) |
| Aanbevolen beslissing | Hold |

---

## Waarom is deze voorspelling aannemelijk?

Voor memantine zijn in de data die voor dit rapport zijn samengesteld geen gegevens over het werkingsmechanisme beschikbaar. Memantine staat bekend als NMDA-receptorantagonist. Het bewijs voor een link met pulmonale hypertensie is beperkt. Eén publicatie (2021, preklinisch) vermeldt dat de glutamaat/NMDA-receptor-as een rol zou kunnen spelen bij acute longschade, pulmonale arteriële hypertensie en diabetes. Dat onderzoek richtte zich echter vooral op insulinegevoeligheid en vetstofwisseling en is slechts zijdelings relevant.

Een tweede publicatie betreft MN-08, een nitraatderivaat van memantine dat wordt ontwikkeld voor pulmonale arteriële hypertensie. Dit is een fase 1-studie bij gezonde vrijwilligers (farmacokinetiek en veiligheid). Zij laat niet zien dat memantine zelf effectief is bij pulmonale hypertensie. Het geeft wel aan dat een afgeleide stof in deze richting wordt ontwikkeld.

De hoge TxGNN-score is dus vooralsnog een modelvoorspelling zonder klinische onderbouwing. Een verband tussen de oorspronkelijke indicatie en pulmonale hypertensie is op basis van deze data niet vast te stellen.

---

## Bewijs uit klinische studies

Momenteel geen gerelateerde klinische studies geregistreerd.

---

## Bewijs uit de literatuur

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|-----|------|------|---------|
| [33500723](https://pubmed.ncbi.nlm.nih.gov/33500723/) | 2021 | Preklinisch/basaal onderzoek | Theranostics | Activatie van de NMDA-receptor reguleert insulinegevoeligheid en vetstofwisseling. Het glutamaat/NMDA-receptor-mechanisme wordt in verband gebracht met pulmonale arteriële hypertensie, maar dit is niet het hoofdonderwerp. |
| [41739394](https://pubmed.ncbi.nlm.nih.gov/41739394/) | 2026 | Fase 1 farmacokinetiek/veiligheid | Clinical Drug Investigation | MN-08 (nitraatderivaat van memantine, in ontwikkeling voor pulmonale arteriële hypertensie) werd getest bij gezonde Chinese vrijwilligers op veiligheid, verdraagbaarheid en farmacokinetiek. Niet indicatiespecifiek. |

---

## Informatie over de Nederlandse markt

| RVG-nummer | Productnaam | Toedieningsvorm | Goedgekeurde indicatie |
|---------|------|------|-----------|
| RVG 114719 | Memantine 10 mg/ml Focus, drank | Drank (volgens productnaam) | Niet beschikbaar (niet geregistreerd) |

<!-- review:begin nl-lic-20261112-memantine-3 -->

> **Controlecorrectie (2026-11-12)**: Oorspronkelijk stond er: “RVG 114719 / Memantine 10 mg/ml Focus, drank / Drank (volgens productnaam) / Niet beschikbaar (vergunning geldig)” Gecorrigeerd: registratienummer RVG 114719 komt niet voor in de actuele Geneesmiddeleninformatiebank van het CBG (metadata.csv, 2026-11-12); de CBG-website vermeldt bij dit nummer “Niet geregistreerd geneesmiddel”. De vermelding “geldig” in deze tabelregel is daarom vervangen door “niet geregistreerd”; actuele aantallen staan in het snelle overzicht. Bron: [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/).

<!-- review:end nl-lic-20261112-memantine-3 -->

---

## Veiligheidsoverwegingen

- **Aandoeningen met een mogelijke contra-indicatie (uit kennisgraaf)**: leverziekte, galblaasziekte en verminderde nierfunctie. Deze komen uit de TxGNN-kennisgraaf (PrimeKG) en niet uit de officiële productinformatie.
- **Geneesmiddelinteracties**: in totaal zijn 122 interacties gevonden. De belangrijkste zijn:
  - **Matig**: anticholinerge middelen, namelijk hyoscyamine, atropine, glycopyrronium, clidinium, dicyclomine, methscopolamine, propantheline, scopolamine, trospium en mepenzolaat.
  - **Gering**: ranitidine, metformine, cimetidine en kaliumcitraat.
  - **Onbekend niveau**: onder andere glimepiride, doxycycline, lansoprazol, loperamide, famotidine en acetylsalicylzuur.

Raadpleeg voor waarschuwingen en contra-indicaties de SmPC (Samenvatting van de Productkenmerken) en de bijsluiter van een geregistreerd memantineproduct. De productinformatie van het CBG-MEB voor deze vergunning was niet beschikbaar.

---

## Conclusie en vervolgstappen

**Beslissing: Hold**

**Onderbouwing:**
- De voorspelling berust vrijwel alleen op een hoge modelscore, zonder klinische studies of direct ondersteunende literatuur (bewijsniveau L5).

<!-- review:begin nl-lic-20261112-memantine-1 -->

> **Controlecorrectie (2026-11-12)**: Oorspronkelijk stond er: “De voorspelling berust vrijwel alleen op een hoge modelscore, zonder klinische studies of direct ondersteunende literatuur (bewijsniveau L5). / De enige Nederlandse vergunning is ingetrokken, waardoor er geen actief geregistreerd product is.” Verwijderd: de vermelding dat de vergunningen zijn doorgehaald of dat er geen geldige vergunning is, kwam niet overeen met de registratiegegevens van het CBG (2026-11-12). Aantal vergunningen in de gegevens: 32, waarvan geldig: 31; actuele aantallen staan in het snelle overzicht en bij de marktinformatie. Bron: [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/).

<!-- review:end nl-lic-20261112-memantine-1 -->

**Om verder te gaan is het volgende nodig:**
- Gegevens over het werkingsmechanisme van memantine, en preklinisch bewijs voor een rol van NMDA-antagonisme bij pulmonale hypertensie.
- Een systematische literatuurstudie naar memantine en pulmonale hypertensie, ook met het oog op de ontwikkeling van MN-08.
- De officiële productinformatie (waarschuwingen en contra-indicaties) via het CBG-MEB.

<!-- review:begin nl-lic-20261112-memantine-2 -->

> **Controlecorrectie (2026-11-12)**: Oorspronkelijk stond er: “De officiële productinformatie (waarschuwingen en contra-indicaties) via het CBG-MEB. / Een beoordeling van de regulatoire route, gezien de ingetrokken vergunning en de ontbrekende vergunde indicatie in de data.” Verwijderd: de vermelding dat de vergunningen zijn doorgehaald of dat er geen geldige vergunning is, kwam niet overeen met de registratiegegevens van het CBG (2026-11-12). Aantal vergunningen in de gegevens: 32, waarvan geldig: 31; actuele aantallen staan in het snelle overzicht en bij de marktinformatie. Bron: [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/).

<!-- review:end nl-lic-20261112-memantine-2 -->

**Opmerking over andere voorspellingen:** voor dezelfde stof is in de data ook **migraine** voorspeld (TxGNN-score 0,9952, bewijsniveau L1). Hiervoor is een afgeronde fase 3-studie (NCT04698525, n=33, memantine versus natriumvalproaat) en een meta-analyse van gerandomiseerde studies beschikbaar. De steekproef is klein en de beoordelaars noemen het bewijs "veelbelovend maar beperkt". Daarom wordt deze indicatie als onderzoeksvraag beschouwd. Zij heeft op dit moment een sterkere bewijsbasis dan pulmonale hypertensie.

<!-- review:begin log -->

## Controlelogboek

Hieronder staat het controlelogboek van deze pagina: gegevens gecontroleerd aan de hand van de registratiegegevens van het CBG (College ter Beoordeling van Geneesmiddelen). Correcties betreffen alleen feitelijke basisgegevens; modelvoorspellingen, bewijsniveaus en conclusies zijn niet herschreven.

| Controledatum | Onderdeel | Actie | Bron |
|------|------|------|------|
| 2026-11-12 | Verwijderd: “De enige Nederlandse vergunning is ingetrokken, waardoor er geen actief geregistreerd product is” | Gecorrigeerd | [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/) |
| 2026-11-12 | Verwijderd: “Een beoordeling van de regulatoire route, gezien de ingetrokken vergunning en de ontbrekende vergunde indicatie in de data” | Gecorrigeerd | [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/) |
| 2026-11-12 | Tabelregel RVG 114719: “geldig” → “niet geregistreerd” | Gecorrigeerd | [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/) |

<!-- review:end log -->

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

