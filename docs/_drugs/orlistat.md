---
layout: default
title: Orlistat
parent: Alleen modelvoorspelling (L5)
nav_order: 256
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "Orlistat"
predicted_indications: ["hypervitaminosis"]
description: "Orlistat: voorspelde nieuwe indicatie Hypervitaminose (hypervitaminosis) (bewijsniveau L5). In Nederland, CBG-vergunningen: 3 (geldig: 3)"
---

# Orlistat
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **1** 
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

## Orlistat: Hypervitaminose (hypervitaminosis)
{: .text-alpha }

## Samenvatting in één zin

Orlistat is een lipaseremmer die oorspronkelijk wordt gebruikt voor de behandeling van obesitas (waaronder monogene obesitas). Het TxGNN-model voorspelt dat het mogelijk werkzaam is bij **hypervitaminose**, maar op dit moment zijn er **geen geregistreerde klinische studies** en **geen publicaties** die deze richting ondersteunen.

---

## Snel overzicht

| Item | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Niet vermeld in de lokale gegevens |
| Voorspelde nieuwe indicatie | Hypervitaminose (hypervitaminosis) |
| TxGNN-voorspellingsscore | 0.9942 |
| Bewijsniveau | L5 |
| Marktstatus in Nederland | In de handel (geldige vergunningen: 3 van 3) |
| Aantal vergunningen | 3 (geldig: 3) |
| Aanbevolen beslissing | Hold |

---

## Waarom is deze voorspelling aannemelijk?

Volgens de rubriek ‘Mechanism of Action’ van de door de Amerikaanse FDA goedgekeurde productinformatie (Prescribing Information) voor Orlistat (niet-officiële vertaling): ‘Orlistat is een reversibele remmer van gastro-intestinale lipasen. Het oefent zijn therapeutische werking uit in het lumen van de maag en de dunne darm door een covalente binding te vormen met de actieve serineresidu-plaats van maag- en pancreaslipasen.’ Oorspronkelijke Engelse tekst: "Orlistat is a reversible inhibitor of gastrointestinal lipases. It exerts its therapeutic activity in the lumen of the stomach and small intestine by forming a covalent bond with the active serine residue site of gastric and pancreatic lipases." ([DailyMed: Xenical (orlistat) prescribing information, H2-Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6240792b-9224-2d10-e053-2a91aa0a2c3e), versie van 2026-09-30; geraadpleegd op 2026-11-19). Op basis van algemene farmacologische kennis is orlistat een remmer van maag- en alvleesklierlipase en verlaagt het de opname van voedingsvet met ongeveer 30%.

Vetoplosbare vitamines (A, D, E en K) worden samen met voedingsvet opgenomen. Een verminderde vetopname kan daardoor ook hun opname verlagen. Dit is de basis van de bekende bijwerking van orlistat: een tekort aan vetoplosbare vitamines. Een theoretische link met hypervitaminose is dat een verminderde opname de toxiciteit zou kunnen beperken bij overmatige suppletie.

Deze redenering is uitsluitend een hypothese die voortkomt uit de TxGNN-score en wordt niet ondersteund door klinisch of literatuurbewijs in de beschikbare data. De beperkingen zijn aanzienlijk:

- Het geldt alleen voor vetoplosbare vitamines, niet voor wateroplosbare.
- Het lost reeds opgeslagen overmaat niet op, met name van vitamine A en D, die zich ophopen in lever en vetweefsel.
- Het effect van orlistat op de opname is gedeeltelijk en wisselend.

---

## Bewijs uit klinische studies

Er zijn momenteel geen gerelateerde klinische studies geregistreerd.

---

## Bewijs uit de literatuur

Er is momenteel geen gerelateerde literatuur beschikbaar.

---

## Marktinformatie Nederland

<!-- licenses:begin -->

| Registratienummer | Productnaam | Werkzame stof(fen) | Farmaceutische vorm | Registratiehouder | Status |
|------|------|------|------|------|------|
| EU/1/07/401 | Alli 60 mg, harde capsules | ORLISTAT | Capsule, hard | GlaxoSmithKline Dungarvan Limited | Geldig |
| EU/1/98/071 | Xenical, capsules 120 mg | ORLISTAT | Capsule, hard | CHEPLAPHARM Arzneimittel GmbH | Geldig |
| RVG 105761 | Orlistat Sandoz 120 mg, harde capsules | ORLISTAT | Capsule, hard | – | Geldig |

Bron: CBG-MEB – Geneesmiddeleninformatiebank (metadata.csv); productnaam, werkzame stoffen, farmaceutische vorm en registratiehouder in de oorspronkelijke Nederlandse bewoording van het CBG. „Niet geregistreerd”: het registratienummer komt niet voor in de actuele Geneesmiddeleninformatiebank.

<!-- licenses:end -->

Eventuele toepassing zou daarom ook een nieuwe registratiestap vereisen.

---

## Veiligheidsoverwegingen

- **Contra-indicaties uit de kennisgraaf (geen productinformatietekst):** In de kennisgraaf (PrimeKG) zijn contra-indicaties aangemerkt voor: leverfalen, primaire hyperoxalurie, anorexia nervosa, boulimia nervosa, vitaminedeficiëntie, cholestase, benigne recidiverende intrahepatische cholestase, familiaire intrahepatische cholestase en geneesmiddelgeïnduceerd leverletsel. Deze zijn niet geverifieerd aan de hand van de officiële SmPC.
- **Geneesmiddelinteracties:** Er zijn 100 mogelijke interacties gevonden (bron: DDInter). Voorbeelden van interacties van gemiddeld niveau (Moderate): abacavir, lamivudine, emtricitabine, atazanavir, acarbose, albiglutide, alogliptine, canagliflozine, metformine, chloorpropamide, amiodaron, cannabidiol, asparaginase, brentuximab vedotin, calaspargase pegol en clofarabine. Interacties van laag niveau (Minor) betreffen cholecalciferol, calcifediol en calcitriol; deze zijn relevant gezien de vetoplosbare vitamines.

Raadpleeg voor volledige veiligheidsinformatie (waarschuwingen en contra-indicaties) de SmPC en de bijsluiter (PIL).

---

## Conclusie en vervolgstappen

**Beslissing: Hold**

**Onderbouwing:**
- De voorspelling berust uitsluitend op een modelscore (bewijsniveau L5), zonder klinische studies of literatuur. Het mechanisme is slechts theoretisch en beperkt, en de vitaminedeficiëntie als bekende bijwerking en contra-indicatie in de kennisgraaf pleit tegen een gunstige baten-risicoverhouding.

**Om verder te gaan is het volgende nodig:**
- Gegevens over het werkingsmechanisme uit DrugBank
- De waarschuwingen en contra-indicaties uit de SmPC van het CBG-MEB (essentieel voor veiligheidsscreening)
- Preklinisch of klinisch bewijs voor effect van orlistat bij hypervitaminose, inclusief een systematische literatuursearch
- Beoordeling van de geschiktheid van toedieningsroutes en vergelijking met de oorspronkelijke indicatie

<!-- review:begin nl-lic-20261106-orlistat-1 -->

> **Controlecorrectie (2026-11-06)**: Oorspronkelijk stond er: “Beoordeling van de geschiktheid van toedieningsroutes en vergelijking met de oorspronkelijke indicatie / Verduidelijking van de regulatoire route, gezien de ingetrokken vergunning” Verwijderd: de vermelding dat de vergunningen zijn doorgehaald of dat er geen geldige vergunning is, kwam niet overeen met de registratiegegevens van het CBG (2026-11-06). Actuele aantallen en de status per registratie staan in het snelle overzicht en in de vergunningstabel bij de marktinformatie. Bron: [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/).

<!-- review:end nl-lic-20261106-orlistat-1 -->

<!-- review:begin log -->

## Controlelogboek

Hieronder staat het controlelogboek van deze pagina: gegevens gecontroleerd aan de hand van de registratiegegevens van het CBG (College ter Beoordeling van Geneesmiddelen). Correcties betreffen alleen feitelijke basisgegevens; modelvoorspellingen, bewijsniveaus en conclusies zijn niet herschreven. De zin dat gegevens over het werkingsmechanisme niet beschikbaar waren, is vervangen door een uittreksel uit de aangehaalde officiële productinformatie (met niet-officiële vertaling).

| Controledatum | Onderdeel | Actie | Bron |
|------|------|------|------|
| 2026-11-06 | Verwijderd: “Verduidelijking van de regulatoire route, gezien de ingetrokken vergunning” | Gecorrigeerd (herzien op 2026-11-24; eerdere versie bewaard in het record) | [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/) |
| 2026-11-19 | Zin ‘gegevens over het werkingsmechanisme niet beschikbaar’ vervangen door uittreksel uit de Amerikaanse productinformatie | Zin dat gegevens over het werkingsmechanisme ontbraken vervangen door een uittreksel met bron | [DailyMed: Xenical (orlistat) prescribing information, H2-Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6240792b-9224-2d10-e053-2a91aa0a2c3e) |

<!-- review:end log -->

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

