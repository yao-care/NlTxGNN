---
layout: default
title: Adenosine
parent: Alleen modelvoorspelling (L5)
nav_order: 21
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Adenosine: voorspelde nieuwe indicatie Bundeltakblok (verouderde ontologieterm) (bewijsniveau L5). Oorspronkelijke indicatie: Ventriculaire tachycardie"
monitor_inn: "Adenosine"
predicted_indications: ["obsolete bundle branch block"]
---

# Adenosine
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **2** 
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

# Adenosine: Van ventriculaire tachycardie naar bundeltakblok (verouderde ziektenaam)

## Samenvatting in één oogopslag

Adenosine is een antiaritmisch middel. Volgens de kennisgraaf waarop het TxGNN-model is gebaseerd, wordt het gebruikt bij **ventriculaire tachycardie**. Het model voorspelt dat adenosine ook werkzaam kan zijn bij **bundeltakblok** (in de gebruikte ziekte-ontologie gemarkeerd als verouderde term). Hiervoor zijn **0 klinische studies** en **0 publicaties** gevonden, dus de voorspelling berust alleen op het model.

---

## Snel overzicht

| Onderdeel | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Ventriculaire tachycardie (uit de kennisgraaf; de Nederlandse registratie bevat geen indicatietekst) |
| Voorspelde nieuwe indicatie | Bundeltakblok (verouderde ontologieterm) |
| TxGNN-voorspellingsscore | 99,94% |
| Bewijsniveau | L5 |
| Marktstatus in Nederland | Alleen doorgehaalde (ingetrokken) registratie |
| Aantal registraties | 1 (0 geldig, 1 doorgehaald) |
| Aanbevolen besluit | Hold |

---

## Waarom is deze voorspelling (on)aannemelijk?

Gegevens over het werkingsmechanisme van adenosine ontbreken in de voor dit rapport verzamelde gegevens. Uit de algemene farmacologie is bekend dat adenosine werkt via A1-receptoren in de AV-knoop. Het wordt gebruikt voor de diagnose en behandeling van supraventriculaire ritmestoornissen.

Bundeltakblok is een geleidingsstoornis binnen de ventrikels, ver van de AV-knoop. Een vastgesteld mechanisme dat adenosine aan deze aandoening koppelt, ontbreekt in de beschikbare gegevens. De term is bovendien als verouderd gemarkeerd, wat wijst op een verouderd ontologie-item dat slecht aansluit op een huidige klinische diagnose. De hoge score is waarschijnlijk een artefact van de kennisgraaf, veroorzaakt door de nabijheid van andere termen voor hartgeleiding. De voorspelling is dus als hypothese zwak onderbouwd.

---

## Bewijs uit klinische studies

Momenteel zijn er geen gerelateerde klinische studies geregistreerd.

---

## Bewijs uit de literatuur

Momenteel is er geen gerelateerde literatuur beschikbaar.

---

## Informatie over de Nederlandse markt

| RVG-nummer | Productnaam | Toedieningsvorm | Status |
|---------|------|------|-----------|
| RVG 114014 | Adenosine Fresenius Kabi 3 mg/ml, oplossing voor injectie in een voorgevulde spuit | Oplossing voor injectie (voorgevulde spuit) | Doorgehaald |

Er is geen geldige registratie meer bij het CBG-MEB. De goedgekeurde indicatietekst is niet beschikbaar in de verzamelde gegevens.

---

## Veiligheidsoverwegingen

Voor waarschuwingen en contra-indicaties uit de officiële productinformatie zijn geen gegevens beschikbaar. Raadpleeg hiervoor de SmPC (Samenvatting van de Productkenmerken) en de bijsluiter.

- **Contra-indicaties volgens de kennisgraaf** (geen etikettekst, maar relaties tussen geneesmiddel en ziekte in PrimeKG): chronische obstructieve longziekte (COPD), astma (inclusief intrinsiek en allergisch), aortastenose en andere aortaklepaandoeningen, mitraalklepstenose, pulmonaalklepinsufficiëntie, hypotensie, acuut coronair syndroom, coronaire hartziekte, aandoeningen van het autonome zenuwstelsel (waaronder het syndroom van Horner), respiratoir falen, atrioventriculair blok, ziek-sinussyndroom (ook familiair), pericarditis en longemfyseem.
- **Geneesmiddelinteracties:** er zijn 100 interacties vastgelegd. De belangrijkste:
  - **Ernstig (Major):** cisapride, dolasetron, papaverine.
  - **Matig (Moderate):** famotidine, claritromycine, granisetron, levofloxacine, ondansetron, palonosetron.
  - Voor andere geneesmiddelen, zoals epinefrine, metformine en morfine, is het niveau onbekend.

---

## Aanvullende voorspelling: catecholaminerge polymorfe ventriculaire tachycardie (CPVT)

De tweede voorspelling van het model heeft een score van 99,42% en bewijsniveau **L4**. Er zijn geen klinische studies geregistreerd, maar er is wel enige literatuur.

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|-----|------|------|---------|
| [18313614](https://pubmed.ncbi.nlm.nih.gov/18313614/) | 2008 | Casuïstiek | Heart Rhythm | Adenosinetrifosfaat (ATP, een verwante stof) beëindigde bidirectionele ventriculaire tachycardie bij één CPVT-patiënt |
| [40165484](https://pubmed.ncbi.nlm.nih.gov/40165484/) | 2025 | Review (consensusverklaring) | Europace | Rol van farmacologische provocatietests in de elektrofysiologie; geen test van adenosine als behandeling |
| [18368865](https://pubmed.ncbi.nlm.nih.gov/18368865/) | 2007 | Review | J Assoc Physicians India | Herkenning en behandeling van idiopathische ventriculaire tachycardie |
| [21699856](https://pubmed.ncbi.nlm.nih.gov/21699856/) | 2011 | Cohort | Heart Rhythm | Afwijkende repolarisatie na pacing bij CPVT met een RyR2-mutatie |

Mechanistisch is er een plausibele link. CPVT wordt veroorzaakt door calciumlekkage uit het sarcoplasmatisch reticulum onder adrenerge stimulatie. Adenosine remt via A1-receptoren de door catecholaminen gestimuleerde cAMP-signalering. Het directe klinische bewijs is echter beperkt tot één casus met ATP. De standaardbehandeling (bètablokkers, flecaïnide, ICD of sympathische denervatie) blijft ongewijzigd. Het bewijs ondersteunt hooguit een hypothese over acute beëindiging van de aritmie, geen therapeutische aanbeveling.

---

## Conclusie en vervolgstappen

**Besluit: Hold**

**Onderbouwing:**
- De voorspelling voor bundeltakblok berust alleen op het model (L5), zonder klinische studies of literatuur. De ziekteterm is verouderd en er is geen aannemelijk mechanisme.
- De registratie in Nederland is doorgehaald en de veiligheidsinformatie uit de productinformatie ontbreekt.

**Om verder te gaan is nodig:**
- Veiligheidsinformatie uit de SmPC en bijsluiter van het CBG-MEB (waarschuwingen, contra-indicaties). Dit blokkeert de veiligheidsscreening.
- Gegevens over het werkingsmechanisme uit DrugBank.
- Koppeling van de verouderde ziekteterm aan een actuele klinische diagnose, of heroverweging van de voorspelling.
- Voor de CPVT-hypothese: gerichte preklinische of kleine klinische studies naar adenosine zelf (niet ATP), plus beoordeling van de ernstige interacties en kennisgraaf-contra-indicaties.
- Opheldering van de huidige marktstatus (geen geldige registratie) en de beschikbare toedieningsvorm.
## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

