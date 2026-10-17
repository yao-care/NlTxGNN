---
layout: default
title: Tropicamide
parent: Alleen modelvoorspelling (L5)
nav_order: 333
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Tropicamide: voorspelde nieuwe indicatie Caudaequinasyndroom (bewijsniveau L5). Oorspronkelijke indicatie: Cycloplegie"
monitor_inn: "Tropicamide"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome"]
---

# Tropicamide
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **3** 
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

# Tropicamide: Van cycloplegie naar caudaequinasyndroom

## Samenvatting in één zin

Tropicamide is een kortwerkend oogmiddel dat oorspronkelijk wordt gebruikt voor cycloplegie (het tijdelijk verlammen van de accommodatiespier van het oog) en pupilverwijding bij oogonderzoek.
Het TxGNN-model voorspelt dat het mogelijk werkzaam is bij **caudaequinasyndroom**,
maar er zijn **0 klinische studies** en **0 publicaties** die deze richting ondersteunen. De voorspelling berust uitsluitend op een modelscore.

---

## Snel overzicht

| Item | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Cycloplegie (volgens de indicatiekoppelingen in de TxGNN-kennisgraaf; de geregistreerde indicatietekst is niet beschikbaar) |
| Voorspelde nieuwe indicatie | Caudaequinasyndroom |
| TxGNN-voorspellingsscore | 99,53% |
| Bewijsniveau | L5 |
| Marktstatus in Nederland | Alleen ingetrokken registratie |
| Aantal handelsvergunningen | 1 |
| Aanbevolen beslissing | Hold |

---

## Waarom is deze voorspelling redelijk?

Voor het werkingsmechanisme zijn in de voor dit rapport samengestelde gegevens geen uitgewerkte mechanismegegevens beschikbaar. Wel is bekend dat tropicamide een muscarine-antagonist is. Farmacologische gegevens tonen binding aan de muscarinereceptoren M2, M3, M4 en M5. De M3-receptor in het oog zorgt voor pupilverwijding en cycloplegie.

De relatie met het caudaequinasyndroom is indirect. Anticholinerge middelen kunnen in theorie blaasfunctiestoornissen (overactiviteit van de blaasspier) verminderen, die na dit syndroom kunnen optreden. Dit is een afleiding uit de modelvoorspelling en algemene antimuscarine-farmacologie, niet uit studiegegevens.

Er zijn belangrijke kanttekeningen:
- Het caudaequinasyndroom is een chirurgisch spoedgeval (zenuwwortelcompressie). De hoofdbehandeling is decompressie. Een anticholinergicum kan hooguit secundaire urinewegklachten behandelen, niet de onderliggende aandoening.
- Tropicamide is een oogmiddel met minimale systemische blootstelling. Het is twijfelachtig of therapeutische systemische concentraties haalbaar zijn.

Ter volledigheid voorspelde het model ook twee andere indicaties, eveneens zonder enig bewijs (L5, Hold):
- **Neurogene blaas** (score 99,13%; de aandoening is in de ontologie als "obsoleet" gemarkeerd, wat wijst op een koppelingsprobleem dat eerst moet worden opgelost). Antimuscarinica zoals oxybutynine en tolterodine zijn hier al beschikbaar.
- **Prikkelbare darmsyndroom** (score 99,12%). Antimuscarinica worden klassegewijs gebruikt tegen krampen, maar systemische anticholinerge bijwerkingen en de ingetrokken registratie pleiten tegen haalbaarheid.

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
| RVG 56688 | Tropicamide 0,5% m/v, oogdruppels | Oogdruppels (volgens productnaam) | Niet beschikbaar |

Deze registratie is **ingetrokken**; er is geen actieve vergunning in Nederland (CBG-MEB).

---

## Veiligheidsoverwegingen

- **Contra-indicaties volgens de kennisgraaf (geen productteksten):** hypertensie, openhoekglaucoom, hoekafsluitingsglaucoom (gesloten kamerhoek), oculaire hypertensie, diabetes mellitus, diabetische ketoacidose, plotselinge hartstilstand, geleidingsstoornissen van het hart, hyperthyreoïdie (inclusief ziekte van Graves en thyreotoxicose), myocardischemie en coronaire hartziekte. Deze koppelingen zijn afkomstig uit een kennisgraaf en moeten aan de officiële SmPC worden getoetst.
- **Geneesmiddelinteracties:** 10 interacties zijn gevonden in DDInter, zonder ernstniveau: atropine, kaliumchloride, vancomycine, simvastatine, prednisolon, famotidine, warfarine, lidocaïne, fluconazol en brimonidine. Daarnaast zijn er bindingen aan de muscarinereceptoren M2, M3, M4 en M5.
- **Verwachte systemische anticholinerge effecten bij hogere dosering:** droge mond, obstipatie, tachycardie en urineretentie.

Raadpleeg voor de officiële waarschuwingen en contra-indicaties de SmPC (Samenvatting van de Productkenmerken) en de bijsluiter.

---

## Conclusie en vervolgstappen

**Beslissing: Hold**

**Onderbouwing:**
- De voorspelling berust alleen op een modelscore (L5) zonder klinische studies of literatuur. De indicatie is mechanistisch zwak, de systemische blootstelling bij een oogmiddel is twijfelachtig en de enige Nederlandse registratie is ingetrokken.

**Om verder te gaan is nodig:**
- De SmPC-waarschuwingen en contra-indicaties van het CBG-MEB (ontbrekend, blokkerend voor de veiligheidsscreening)
- Gegevens over het werkingsmechanisme uit DrugBank
- Preklinisch of farmacokinetisch bewijs dat voldoende systemische blootstelling haalbaar is
- Oplossing van het ontologieprobleem rond "obsolete neurogenic bladder"
- Een vergelijking met bestaande standaardbehandelingen en een beoordeling van de route van toediening (nu niet beoordeeld)
## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

