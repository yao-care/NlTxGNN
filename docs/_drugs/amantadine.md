---
layout: default
title: Amantadine
parent: Alleen modelvoorspelling (L5)
nav_order: 31
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Amantadine: voorspelde nieuwe indicatie Rasmussen-encefalitis (Rasmussen subacute encefalitis) (bewijsniveau L5). Oorspronkelijke indicatie: Ziekte van Parkinson en verwante parkinsonistische aandoen…"
monitor_inn: "amantadine"
predicted_indications: ["Rasmussen subacute encephalitis", "transaldolase deficiency", "myelitis", "PLA2G6-associated neurodegeneration"]
---

# Amantadine
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

# Amantadine: Van de ziekte van Parkinson naar Rasmussen-encefalitis

## Samenvatting in één zin

Amantadine wordt oorspronkelijk gebruikt bij de ziekte van Parkinson en verwante bewegingsstoornissen. Het TxGNN-model voorspelt dat het mogelijk werkzaam is bij **Rasmussen-encefalitis** (subacute encefalitis van Rasmussen), maar op dit moment zijn er **0 klinische studies** en **0 publicaties** die deze specifieke voorspelling ondersteunen. Het is dus een zuiver modelmatige voorspelling.

---

## Snel overzicht

| Item | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Ziekte van Parkinson en verwante parkinsonistische aandoeningen (volgens de kennisgraaf; er is geen goedgekeurde indicatietekst beschikbaar in de registratiegegevens) |
| Voorspelde nieuwe indicatie | Rasmussen-encefalitis (Rasmussen subacute encefalitis) |
| TxGNN-voorspellingsscore | 99,48% |
| Bewijsniveau | L5 |
| Marktstatus in Nederland | Alleen doorgehaald (vervallen registratie) |
| Aantal vergunningen | 1 |
| Aanbevolen beslissing | Hold |

---

## Waarom is deze voorspelling aannemelijk?

Gedetailleerde gegevens over het werkingsmechanisme zijn momenteel niet beschikbaar in de voor dit rapport samengestelde data. Op basis van algemene kennis is amantadine een NMDA-receptorantagonist met dopaminerge modulerende eigenschappen, en het remt ook het M2-ionkanaal van het influenzavirus. De werkzaamheid bij de ziekte van Parkinson is bekend.

Bij Rasmussen-encefalitis worden door glutamaatreceptoren gemedieerde excitotoxiciteit en auto-immuniteit (de anti-GluR3-hypothese) als mogelijke mechanismen genoemd. Een NMDA-antagonist zou daarom mechanistisch een rol kunnen spelen. Dit blijft echter een hypothese: de voorspelling is niet klinisch gevalideerd, en de relatie met de oorspronkelijke indicaties (bewegingsstoornissen) is niet nader uitgewerkt.

---

## Bewijs uit klinische studies

Momenteel zijn er geen gerelateerde klinische studies geregistreerd.

---

## Bewijs uit de literatuur

Momenteel is er geen gerelateerde literatuur beschikbaar voor Rasmussen-encefalitis.

*Ter informatie: voor andere hoog-scorende voorspellingen is wel enige literatuur gevonden (zie hieronder bij "Overige voorspelde indicaties").*

---

## Informatie over de Nederlandse markt

| RVG-nummer | Productnaam | Toedieningsvorm | Goedgekeurde indicatie |
|---------|------|------|-----------|
| RVG 119789//05352 | Symmetrel 100 mg capsules | Capsule (volgens productnaam) | Niet beschikbaar; vergunning doorgehaald |

Deze enige vergunning heeft de status "doorgehaald". Er is dus momenteel geen geldige registratie bij het CBG-MEB in de gebruikte data.

---

## Veiligheidsoverwegingen

- **Contra-indicaties uit de kennisgraaf** (afgeleid uit TxGNN/PrimeKG, geen bijsluitertekst): multipele systeematrofie, posturaal orthostatisch tachycardiesyndroom, orthostatische hypotensie, epilepsie, nierziekte, pyoureter, congestief hartfalen, psychotische stoornis, schizofreniforme stoornis, psychische stoornis, schizoaffectieve stoornis, melanoom, hoekafsluitingsglaucoom (nauwehoekglaucoom), middelengerelateerde stoornissen/afhankelijkheid, atopisch eczeem en dermatitis.
- **Geneesmiddeleninteracties**: in totaal 117 interacties gevonden. Belangrijkste voorbeelden:
  - **Ernstig (Major)**: bupropion.
  - **Matig (Moderate)**: anticholinerge middelen en spasmolytica zoals atropine, clidinium, dicyclomine, glycopyrronium, hyoscyamine, mepenzolaat, methscopolamine, propantheline, scopolamine en trospium; daarnaast metoclopramide, macrogol (3350 met elektrolyten), picosulfaat en natriumsulfaat.

Raadpleeg voor waarschuwingen en formele contra-indicaties de SmPC (Samenvatting van de Productkenmerken) en de bijsluiter.

---

## Overige voorspelde indicaties (ter context)

| Voorspelde indicatie | Score | Bewijsniveau | Opmerking |
|------|------|------|------|
| Transaldolasedeficiëntie | 99,27% | L5 | Geen studies of literatuur; geen duidelijke mechanistische link, waarschijnlijk een netwerkartefact |
| Myelitis | 99,24% | L3 | Literatuur betreft vooral post-polio-syndroom (o.a. een dubbelblinde, placebogecontroleerde studie uit 1995 naar vermoeidheid, Cochrane-reviews uit 2011 en 2015, EFNS-richtlijn 2006); bewijs voor effect onvoldoende; link met myelitis indirect |
| PLA2G6-geassocieerde neurodegeneratie | 99,23% | L4 | Enige publicatie (PMID 31366412) betreft gangstoornis bij PKAN, een andere NBIA-subtype; indirect bewijs |

---

## Conclusie en vervolgstappen

**Beslissing: Hold**

**Onderbouwing:**
- De score is zeer hoog (99,48%), maar er zijn geen klinische studies of literatuur voor Rasmussen-encefalitis. Het bewijsniveau is L5 en de Nederlandse registratie is doorgehaald.

**Om verder te gaan is het volgende nodig:**
- Gegevens over het werkingsmechanisme (bijv. via DrugBank) en een uitgewerkte mechanistische analyse voor Rasmussen-encefalitis
- Systematische literatuursearch en preklinisch of casuïstisch bewijs bij Rasmussen-encefalitis
- Bijsluiter/SmPC-informatie van het CBG-MEB (waarschuwingen en contra-indicaties), die nu ontbreekt en een voorwaarde is voor de veiligheidsscreening
- Beoordeling van de toedieningsroute en de regulatoire haalbaarheid, gezien de doorgehaalde vergunning
## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

