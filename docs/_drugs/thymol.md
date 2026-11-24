---
layout: default
title: Thymol
parent: Alleen modelvoorspelling (L5)
nav_order: 320
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Thymol: voorspelde nieuwe indicatie Interventriculair septumaneurysma (bewijsniveau L5). Oorspronkelijke indicatie: Niet beschikbaar in de vergunningsgegevens"
monitor_inn: "thymol"
predicted_indications: ["interventricular septum aneurysm", "pulmonary valve disease", "Laubry-Pezzi syndrome", "genetic syndromic Pierre Robin syndrome", "orofacial clefting syndrome", "partial deletion of the long arm of chromosome 22", "Pierre Robin syndrome associated with a chromosomal anomaly", "disorder of fucoglycosan synthesis", "partial deletion of the long arm of chromosome 7", "Jeune syndrome situs inversus"]
---

# Thymol
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

## Thymol: Van een niet-vastgelegde oorspronkelijke indicatie naar interventriculair septumaneurysma
{: .text-alpha }

## Samenvatting in één alinea

Thymol is een natuurlijke fenolische monoterpeen die in de Nederlandse markt voorkwam als bestanddeel van een inhalatiezalf (Vicks VapoRub). Voor die vergunning is in de samengestelde gegevens geen goedgekeurde indicatietekst opgenomen. Het TxGNN-model voorspelt dat thymol mogelijk werkzaam is bij **interventriculair septumaneurysma**, met een zeer hoge modelscore. Er zijn echter **0 klinische studies** en **0 publicaties** die specifiek deze indicatie ondersteunen. De voorspelling berust uitsluitend op een grafiekmodel.

---

## Snel overzicht

| Item | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Niet beschikbaar in de vergunningsgegevens |
| Voorspelde nieuwe indicatie | Interventriculair septumaneurysma |
| TxGNN-voorspellingsscore | 0,9925 |
| Bewijsniveau | L5 |
| Marktstatus in Nederland | In de handel (geldige vergunningen: 2 van 3) |
| Aantal vergunningen | 3 (geldig: 2) |
| Aanbevolen beslissing | Hold |

---

## Waarom is deze voorspelling (on)aannemelijk?

Gegevens over het werkingsmechanisme van thymol in de oorspronkelijke indicatie zijn momenteel niet beschikbaar. Op basis van algemene kennis heeft thymol antioxidatieve, antimicrobiële en ontstekingsremmende eigenschappen. Het wordt van oudsher gebruikt in producten voor luchtwegklachten en mondverzorging.

Er is geen mechanistisch verband gevonden tussen deze eigenschappen en een structurele hartafwijking zoals een septumaneurysma. Zo'n afwijking is een anatomisch defect dat niet aannemelijk door een kleinmoleculair monoterpenoïde wordt beïnvloed. De hoge score (0,9925) komt van het TxGNN-model (deep learning) en weerspiegelt waarschijnlijk overeenkomsten die het model heeft geleerd tussen verwante aandoeningen, niet biologisch bewijs, en is geen klinisch argument. Ook de overige top-10-voorspellingen betreffen vooral aangeboren of structurele aandoeningen (o.a. pulmonalisklepaandoening, Laubry-Pezzi-syndroom, Pierre Robin-syndroom, chromosomale deleties) zonder enig onderbouwend bewijs. Dit wijst op een patroon in het model en niet op een gericht therapeutisch signaal.

---

## Bewijs uit klinische studies

Momenteel zijn er geen gerelateerde klinische studies geregistreerd.

---

## Bewijs uit de literatuur

Momenteel is er geen gerelateerde literatuur beschikbaar voor interventriculair septumaneurysma.

Ter context: voor de achtste voorspelling (stoornis in de fucoglycaansynthese) zijn wel 20 publicaties gevonden, maar dit betreft algemene thymol- en etherischeoliestudies (antioxidatief, antimicrobieel, wondgenezing, ontstekingsremming, nanoformuleringen), geen onderzoek naar de voorspelde aandoening. Dit aantal weerspiegelt zoeken op trefwoord en is geen indicatiespecifiek bewijs.

---

## Informatie over de Nederlandse markt

<!-- licenses:begin -->

| Registratienummer | Productnaam | Werkzame stof(fen) | Farmaceutische vorm | Registratiehouder | Status |
|------|------|------|------|------|------|
| RVG 03088 | Vicks Vaporub, zalf voor inhalatiedamp | EUCALYPTUSOLIE, KAMFER, (D,L-Vorm), LEVOMENTHOL, TERPENTIJNOLIE, Gerectificeerd… | Zalf voor inhalatiedamp | Procter & Gamble Nederland B.V. | Geldig |
| RVG 129750//03088 | Vicks Vaporub, zalf voor inhalatiedamp | EUCALYPTUSOLIE, KAMFER, (D,L-Vorm), LEVOMENTHOL, TERPENTIJNOLIE, Gerectificeerd… | Zalf voor inhalatiedamp | Top-Pharma B.V. | Geldig |
| RVG 120425//03088 | Vicks Vaporub, zalf voor inhalatiedamp | THYMOL, KAMFER, (D,L-VORM), TERPENTIJNOLIE, GERECTIFICEERD, EUCALYPTUSOLIE, LEV… | – | – | Niet geregistreerd |

Bron: CBG-MEB – Geneesmiddeleninformatiebank (metadata.csv); productnaam, werkzame stoffen, farmaceutische vorm en registratiehouder in de oorspronkelijke Nederlandse bewoording van het CBG. „Niet geregistreerd”: het registratienummer komt niet voor in de actuele Geneesmiddeleninformatiebank.

<!-- licenses:end -->

---

## Veiligheidsoverwegingen

Raadpleeg de SmPC (Samenvatting van de Productkenmerken) en de bijsluiter voor veiligheidsinformatie. In de gegevens voor dit rapport zijn geen waarschuwingen, contra-indicaties of geneesmiddelinteracties vastgelegd. Dit is een kennislacune en geen bewijs van veiligheid.

---

## Conclusie en vervolgstappen

**Beslissing: Hold**

**Onderbouwing:**
- De voorspelling is uitsluitend computationeel (L5), zonder klinische studies, zonder specifieke literatuur en zonder aannemelijk mechanisme.

<!-- review:begin nl-lic-20261112-thymol-1 -->

> **Controlecorrectie (2026-11-12)**: Oorspronkelijk stond er: “De voorspelling is uitsluitend computationeel (L5), zonder klinische studies, zonder specifieke literatuur en zonder aannemelijk mechanisme. De enige Nederlandse vergunning is bovendien doorgehaald.” Verwijderd: de vermelding dat de vergunningen zijn doorgehaald of dat er geen geldige vergunning is, kwam niet overeen met de registratiegegevens van het CBG (2026-11-12). Actuele aantallen en de status per registratie staan in het snelle overzicht en in de vergunningstabel bij de marktinformatie. Bron: [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/).

<!-- review:end nl-lic-20261112-thymol-1 -->

**Om verder te gaan is nodig:**
- De SmPC/bijsluiter van het CBG-MEB ophalen en verwerken (waarschuwingen, contra-indicaties). Dit is een blokkerende kennislacune voor de veiligheidsscreening.
- Gegevens over het werkingsmechanisme van thymol aanvullen, bijvoorbeeld uit DrugBank.
- Een biologisch plausibel mechanisme onderbouwen voor een structurele hartafwijking, of overwegen om kandidaat-indicaties te prioriteren met meer biologische aannemelijkheid.
- Toedieningsroutes beoordelen, aangezien het product voor inhalatie/lokaal gebruik was bedoeld en systemische blootstelling voor een hartindicatie niet is onderzocht.

<!-- review:begin log -->

## Controlelogboek

Hieronder staat het controlelogboek van deze pagina: gegevens gecontroleerd aan de hand van de registratiegegevens van het CBG (College ter Beoordeling van Geneesmiddelen). Correcties betreffen alleen feitelijke basisgegevens; modelvoorspellingen, bewijsniveaus en conclusies zijn niet herschreven.

| Controledatum | Onderdeel | Actie | Bron |
|------|------|------|------|
| 2026-11-12 | Verwijderd: “De enige Nederlandse vergunning is bovendien doorgehaald” | Gecorrigeerd (herzien op 2026-11-24; eerdere versie bewaard in het record) | [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/) |
| 2026-11-12 | Tabelregel RVG 120425//03088: “geldig” → “niet geregistreerd” | Vervangen door de door het programma gegenereerde vergunningstabel (eerder: Gecorrigeerd) | [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/) |

<!-- review:end log -->

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

