---
layout: default
title: Sorbitol
parent: Alleen modelvoorspelling (L5)
nav_order: 112
evidence_level: L5
indication_count: 1
---

# Sorbitol
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **1** 
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

# Sorbitol: van osmotisch middel tot trainingsinduceerde maligne hyperthermie

## Samenvatting in één zin

Sorbitol is een suiker-alcohol die veel wordt gebruikt als osmotisch laxativum, vochtbinder en farmaceutische hulpstof; er is geen formeel goedgekeurde indicatie geregistreerd in de Nederlandse regelgevingsdatabase.
Het TxGNN-model voorspelt dat het effectief kan zijn voor **trainingsinduceerde maligne hyperthermie**,
echter met momenteel **0 klinische onderzoeken** en **0 publicaties** die deze richting ondersteunen, bestaat de bewijsbasis volledig uit een computationele modelvoorspelling.

---

## Snel overzicht

| Item | Inhoud |
|------|--------|
| Originele indicatie | Geen goedgekeurde indicatie geregistreerd |
| Voorspelde nieuwe indicatie | Trainingsinduceerde maligne hyperthermie |
| TxGNN-voorspellingsscore | 99.40% |
| Bewijsniveau | L5 |
| Status op NL-markt | Niet geregistreerd |
| Aantal autorisaties | 0 |
| Aanbevolen beslissing | Afwachting |

---

## Waarom is deze voorspelling redelijk?

Momenteel zijn gedetailleerde werkingsmechanisme-gegevens voor Sorbitol niet beschikbaar in dit bewijspakket. Op basis van vastgestelde farmacologie is Sorbitol een osmotisch suiker-alcohol dat zijn primaire therapeutische effect uitoefent door osmotische drukregulering in het gastro-intestinale tractus. Het metabole traject ervan — Sorbitol → Fructose → glycolyse — is goed gekarakteriseerd in intermediair metabolisme, maar heeft geen bekende directe farmacologische relevantie voor skeletspierpatofysiologie.

Trainingsinduceerde maligne hyperthermie is een zeldzame, potentieel levensbedreigende aandoening veroorzaakt door gain-of-function mutaties in het *RYR1*-gen, dat codeert voor de ryanodine-receptor die de calciumafgifte uit het sarcoplasmatisch reticulum van skeletspier regelt. Tijdens een acuut episode leidt ongecontroleerde intracellulair calciumuitstroom tot aanhoudende spiercontractie, ernstige hyperthermie en metabolische acidose. De gevestigde eerstelijnbehandeling is dantroleen, dat direct RYR1-gemedieerde calciumafgifte onderdrukt — een volledig ander mechanisme dan osmotische modulatie.

Er is geen erkende mechanistische brug tussen Sorbitols osmotische eigenschappen en RYR1-gemedieerde calciumdysregulatie. De hoge TxGNN-score (0.994) weerspiegelt waarschijnlijk meest indirecte nabijheid van knooppunten in de kennisgraaf via gedeelde paden in het skeletspiermetabolisme, in plaats van een echte geneesmiddel-ziekte farmacologische verbinding. Deze voorspelling wordt beoordeeld als waarschijnlijk computationeel vals-positief zonder huidige klinische translationele basis, en mag niet worden voortgezet zonder preklinisch mechanistisch bewijs.

---

## Bewijs uit klinische onderzoeken

Momenteel zijn geen gerelateerde klinische onderzoeken geregistreerd.

---

## Bewijzen uit literatuur

Momenteel is geen gerelateerde literatuur beschikbaar.

---

## Informatie over de Nederlandse markt

Sorbitol beschikt momenteel over geen marketingvergunning geregistreerd bij de **CBG-MEB** (College ter Beoordeling van Geneesmiddelen) in Nederland. Er zijn geen RVG-genummerde producten geregistreerd. Mocht toekomstig bewijs regelgevingsoverweging rechtvaardigen, dan zou een nieuwe vergunningsaanvraag of procedure voor uitbreiding van indicatie van het begin af aan nodig zijn.

---

## Veiligheidsbeschouwingen

Raadpleeg alstublieft de SmPC (Samenvatting van de Productkenmerken) voor veiligheidsinformatie. Aangezien momenteel geen producten in Nederland zijn geregistreerd, zou de relevante referentiedocumentatie afkomstig moeten zijn uit vergelijkbare jurisdicties (bijv. EMA-geautoriseerde producten die Sorbitol als werkzame stof bevatten).

---

## Conclusie en vervolgstappen

**Beslissing: Afwachting**

**Rationale:**
Deze repositioneringskandidat wordt geclassificeerd als **L5** (alleen modelvoorspelling) — er zijn geen geregistreerde klinische onderzoeken, geen gepubliceerde literatuur, en geen vastgesteld mechanistisch verband tussen Sorbitols osmotische farmacologie en de RYR1-gedreven calciumdysregulatie die aan trainingsinduceerde maligne hyperthermie ten grondslag ligt. De voorspelling wordt beoordeeld als waarschijnlijk vals-positief afkomstig uit kennisgraafanalyse.

**Voor voortgang is het volgende nodig:**
- Formele werkingsmechanisme-documentatie voor Sorbitol ophalen via DrugBank API om eventueel over het hoofd geziene secundaire farmacologie uit te sluiten
- Een aannemelijke mechanistische hypothese vaststellen die Sorbitol verbindt met RYR1-gemedieerde calciumhantering (bijv. osmotische effecten op intracellulair calciumdynamiek, of fructose-route-interacties met spierenergetiek)
- Genereer minimaal bewijsniveau L4: in vitro- of diermodelgegevens die enig betekenisvol effect op trainingsinduceerde hyperthermie-paden aantonen
- Indien preklinisch bewijs naar voren komt, initieer CBG-MEB presubmissieconsultatie — met opmerking dat momenteel geen productpresence op de Nederlandse markt bestaat en volledige vergunningsprocedure zou vereist zijn
- Voer een concurrentielandschapanalyse uit tegen dantroleen en andere RYR1-doelgerichte middelen om het potentieel voor klinische differentiatie in te schatten

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

