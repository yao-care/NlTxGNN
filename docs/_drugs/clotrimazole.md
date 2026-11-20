---
layout: default
title: Clotrimazole
parent: Alleen modelvoorspelling (L5)
nav_order: 94
evidence_level: L5
indication_count: 2
monitor_inn: "clotrimazole"
predicted_indications: ["acne (disease)", "postmenopausal atrophic vaginitis"]
last_modified_at: 2026-11-20
description: "Clotrimazole: voorspelde nieuwe indicatie acne (acne (disease)) (bewijsniveau L5). In Nederland, CBG-vergunningen: 25 (geldig: 24)"
---

# Clotrimazole
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

## Clotrimazole: acne (acne (disease))
{: .text-alpha }

## Samenvatting in één zin

Clotrimazol is een azool-antimycoticum dat lokaal wordt gebruikt bij huid- en slijmvliesinfecties door schimmels en gisten. Het TxGNN-model voorspelt dat het mogelijk werkzaam is bij **acne (acne (disease))**, maar hiervoor is slechts **1 klinische studie** beschikbaar (een combinatiepreparaat, opgeschort) en **geen publicaties**. Het bewijs is daarmee zeer beperkt.

---

## Snel overzicht

| Item | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Niet vermeld in de lokale gegevens |
| Voorspelde nieuwe indicatie | acne (acne (disease)) |
| TxGNN-voorspellingsscore | 0.9986 |
| Bewijsniveau | L5 |
| Marktstatus in Nederland | In de handel (geldige vergunningen: 24 van 25) |
| Aantal vergunningen | 25 (geldig: 24) |
| Aanbevolen beslissing | Hold (afwachten) |

Het bewijsniveau is L5: de enige geregistreerde studie onderzoekt een combinatiepreparaat bij een besmette dermatose en niet clotrimazol bij acne zelf.

---

## Waarom is deze voorspelling plausibel?

Volgens de rubriek ‘Clinical Pharmacology’ van de door de Amerikaanse FDA goedgekeurde productinformatie (Prescribing Information) voor Clotrimazole (niet-officiële vertaling): ‘Clotrimazol is een breedspectrum-antimycoticum dat de groei van pathogene gisten remt door de permeabiliteit van celmembranen te veranderen. De werking van clotrimazol is fungistatisch bij geneesmiddelconcentraties tot 20 mcg/ml en kan in vitro bij hogere concentraties fungicide zijn tegen Candida albicans en andere soorten van het geslacht Candida.’ Oorspronkelijke Engelse tekst: "Clotrimazole is a broad-spectrum antifungal agent that inhibits the growth of pathogenic yeasts by altering the permeability of cell membranes. The action of clotrimazole is fungistatic at concentrations of drug up to 20 mcg/mL and may be fungicidal in vitro against Candida albicans and other species of the genus Candida at higher concentrations." ([DailyMed: clotrimazole prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=980736aa-751a-4642-ab85-a309435fd02f), versie van 2025-03-27; geraadpleegd op 2026-11-19). Clotrimazol is een azool-antimycoticum met daarnaast enige ontstekingsremmende en antimicrobiële eigenschappen. Een betrokkenheid van *Malassezia* en *Cutibacterium* bij acneachtige huidafwijkingen zou een mogelijk verband met deze indicatie kunnen verklaren.

Dit verband is echter indirect. De enige studie is een vaste combinatie van beclometason, gentamicine en clotrimazol, waardoor de bijdrage van clotrimazol niet te isoleren is. De hoge score van 0,9986 is een computationele voorspelling en wordt niet ondersteund door klinische gegevens.

---

## Klinisch trialbewijs

| Trialnummer | Fase | Status | Inclusie | Belangrijkste bevindingen |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Fase 2/3 | Opgeschort | 80 | Combinatie van beclometason, gentamicine en clotrimazol (crème) bij besmette dermatose met symmetrische laesies; combinatieontwerp, geen betrouwbare werkzaamheidsgegevens |

---

## Literatuurbewijs

Momenteel is er geen relevante literatuur beschikbaar.

---

## Informatie over de Nederlandse markt

| RVG-nummer | Productnaam | Toedieningsvorm | Goedgekeurde indicatie |
|---------|------|------|-----------|
| RVG 119516//08935 | Canesten gyno, crème voor vaginaal gebruik 20 mg/g | Niet vermeld | Niet vermeld in de lokale gegevens |

---

## Veiligheidsoverwegingen

- **Geneesmiddelinteracties**: in de voor dit rapport samengestelde gegevens zijn 1099 interacties vermeld. Voorbeelden van ernstige (Major) interacties zijn fentanyl, alfentanil, amiodaron en hydrocodon. Matige interacties betreffen onder meer abemaciclib, paclitaxel, acalabrutinib, nifedipine, levonorgestrel, estradiol, alprazolam, apixaban en aprepitant. Bij systemische blootstelling is dit relevant; bij lokaal gebruik is de blootstelling doorgaans laag.

Raadpleeg voor waarschuwingen en contra-indicaties de SmPC (Samenvatting van de Productkenmerken) en de bijsluiter van het product, zoals beoordeeld door het CBG-MEB.

---

## Conclusie en vervolgstappen

**Beslissing: Hold**

**Onderbouwing:**
- De voorspelling berust vrijwel uitsluitend op een computationele score. De enige studie is een opgeschorte combinatiestudie, waarin de bijdrage van clotrimazol niet te onderscheiden is, en er is geen enkele publicatie over acne.

**Om verder te gaan is nodig:**
- Gerandomiseerde studies waarin clotrimazol als enkelvoudig middel wordt onderzocht bij acne.
- Gegevens over het werkingsmechanisme en een onderbouwing van de rol van *Malassezia* of *Cutibacterium*.
- Beoordeling van de SmPC op waarschuwingen en contra-indicaties, en een veiligheidsplan voor lokaal gebruik op de huid.
- Controle van de beschikbare toedieningsroutes (crème voor vaginaal gebruik versus een product voor de huid).

<!-- review:begin log -->

## Controlelogboek

Hieronder het controlelog van deze pagina. De zin dat gegevens over het werkingsmechanisme niet beschikbaar waren, is vervangen door een uittreksel uit de aangehaalde officiële productinformatie (met niet-officiële vertaling); modelvoorspellingen, bewijsniveaus en conclusies zijn niet herschreven.

| Controledatum | Onderdeel | Actie | Bron |
|------|------|------|------|
| 2026-11-19 | Zin ‘gegevens over het werkingsmechanisme niet beschikbaar’ vervangen door uittreksel uit de Amerikaanse productinformatie | Zin dat gegevens over het werkingsmechanisme ontbraken vervangen door een uittreksel met bron | [DailyMed: clotrimazole prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=980736aa-751a-4642-ab85-a309435fd02f) |

<!-- review:end log -->

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

