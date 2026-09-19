---
layout: default
title: Amitriptyline Hydrochloride
parent: Alleen modelvoorspelling (L5)
nav_order: 25
evidence_level: L5
indication_count: 0
---

# Amitriptyline Hydrochloride
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **0** 
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

# Amitriptilline Hydrochloride: Onvoldoende gegevens voor evaluatie van geneesmiddelhergebruik

## Samenvatting in één zin

Amitriptilline hydrochloride is een goed gevestigde tricyclische antidepressivum (TCA) die wereldwijd wordt gebruikt voor de behandeling van depressie, neuropathische pijn en andere aandoeningen. Het TxGNN-model heeft echter **geen voorspelde nieuwe indicaties** voor dit geneesmiddel gegenereerd in de huidige analysecyclus, en **er is geen bewijs uit klinische onderzoeken of literatuur** verzameld. Dit rapport documenteert de huidige gegevenslacunes en schetst wat nodig is voordat een evaluatie van hergebruik kan plaatsvinden.

## Snel overzicht

| Item | Inhoud |
|------|--------|
| Geneesmiddelnaam (INN) | Amitriptilline Hydrochloride |
| Oorspronkelijke indicatie | Niet beschikbaar in huidige dataset |
| Voorspelde nieuwe indicatie | Geen — geen TxGNN-voorspellingen gegenereerd |
| TxGNN-voorspellingsscore | N/A |
| Bewijsniveau | L5 (Geen voorspellingen of ondersteunende studies beschikbaar) |
| Marketingstatus | Niet in de handel (Niet in de handel) |
| Aantal vergunningen | 0 |
| Aanbevolen besluit | **In afwachting** |

## Waarom is deze voorspelling redelijk?

Er zijn momenteel **geen TxGNN-voorspellingen** beschikbaar voor Amitriptilline Hydrochloride, dus een beoordeling van mechanistische plausibiliteit kan op dit moment niet worden uitgevoerd.

Ter referentie: Amitriptilline is een tricyclisch antidepressivum dat vooral werkt door de heropname van serotonine en noradrenaline in het centraal zenuwstelsel te remmen. Het heeft ook anticholinerge, antihistaminische en natriumkanaalblokkerende eigenschappen. Deze gevarieerde farmacologische werkingen hebben het historisch tot een kandidaat voor off-label gebruik gemaakt, waaronder neuropathische pijn, migraine-profylaxe, fibromyalgie en prikkelbaredarmsyndroom.

Momenteel zijn gedetailleerde gegevens over het werkingsmechanisme niet beschikbaar in het bewijspakket (vermeld als gegevenslacune). De DrugBank-ID is niet in kaart gebracht, en er zijn geen oorspronkelijke indicaties vastgelegd in de verstrekte regelgevingsgegevens. Een volledige DrugBank-opzoeking en integratie van regelgevingsgegevens zijn nodig voordat enige analyse van hergebruik kan plaatsvinden.

## Bewijs uit klinische onderzoeken

Momenteel zijn geen gerelateerde klinische onderzoeken geregistreerd in het bewijspakket.

> **Opmerking:** Dit betekent niet dat er wereldwijd geen klinische onderzoeken voor Amitriptilline bestaan — het betekent dat de pijplijn voor bewijsverzameling nog niet voor dit geneesmiddel is uitgevoerd. Amitriptilline heeft een uitgebreide geschiedenis van klinische onderzoeken over meerdere indicaties.

## Bewijs uit literatuur

Momenteel is geen gerelateerde literatuur beschikbaar in het bewijspakket.

> **Opmerking:** Amitriptilline heeft duizenden publicaties in PubMed. De afwezigheid van literatuur hier weerspiegelt het feit dat geen TxGNN-voorspelde indicatie is gegenereerd, dus de pijplijn voor bewijsverzameling is niet geactiveerd.

## Marketinginformatie

Er zijn geen marketingvergunningen gevonden in de huidige regelgevingsdataset. Het geneesmiddel is geregistreerd als **niet in de handel** (Niet in de handel) met **0 licenties** op bestand.

> **Opmerking:** Amitriptilline wordt in veel landen op de markt gebracht (inclusief Nederland, waar het beschikbaar is als verschillende generieke versies). De afwezigheid van vergunningsgegevens hier kan een lacune in de lokale regelgevingsgegevensbron weerspiegelen in plaats van werkelijke niet-beschikbaarheid.

## Veiligheidsbeschouwingen

> Raadpleeg de SmPC (Samenvatting van productkenmerken) voor volledige veiligheidsinformatie. Belangrijke veiligheidsgegevens (waarschuwingen, contra-indicaties en geneesmiddel-geneesmiddelinteracties) konden niet in de huidige gegevensverzamelingscyclus worden opgehaald.
>
> **Bekende algemene veiligheidsbeschouwingen voor Amitriptilline** (op basis van gevestigde farmacologische kennis):
> - **Black box-waarschuwing** (in veel rechtsgebieden): Verhoogd risico op zelfmoordgedachten en gedrag bij kinderen, tieners en jonge volwassenen
> - **Cardiaal risico**: QT-verlenging, aritmieën — ECG-monitoring aanbevolen
> - **Anticholinerge effecten**: Droge mond, urineretentie, obstipatie, wazig zien
> - **CNS-depressie**: Slaperigheid, verminderde psychomotorische prestaties
> - **Gecontra-indiceerd** met MAO-remmers (risico op serotoninsyndrroom) en na recent myocardinfarct
>
> *Deze punten worden verstrekt op basis van algemene farmacologische kennis en moeten worden geverifieerd tegen de huidige SmPC.*

## Geïdentificeerde gegevenslacunes

De volgende kritische gegevenslacunes zijn gemarkeerd tijdens de samenstelling van het bewijspakket:

| Lacune-ID | Categorie | Item | Ernst | Effect | Remedie |
|-----------|-----------|------|-------|--------|---------|
| DG001 | Geneesmiddelniveau | Regelgevingswaarschuwingen/contra-indicaties | **Blokkering** | Kan fase 1 veiligheidsbeoordeling niet starten | Product label-PDF van regelgevingsinstantie downloaden en ontleden |
| DG002 | Geneesmiddelniveau | Werkingsmechanisme (MOA) | Hoog | Beïnvloedt analyse van mechanistische relevantie | DrugBank API opvragen |

**Aanvullende lacunes waargenomen:**
- DrugBank-ID niet in kaart gebracht (ondanks succesvolle DrugBank-query geregistreerd op 2026-03-26)
- Geen oorspronkelijke indicaties vastgelegd
- Geen TxGNN-voorspellingen gegenereerd — worteloorzaak moet worden onderzocht (mogelijke mappingfout)
- Geneesmiddel-geneesmiddelinteractiequerie gaf geen resultaten, wat onverwacht is voor een veel gebruikte TCA

## Conclusie en vervolgstappen

**Besluit: In afwachting**

**Motivering:**
Er zijn geen TxGNN-voorspellingen gegenereerd voor Amitriptilline Hydrochloride, en meerdere blokkerende gegevenslacunes verhinderen enige zinvolle evaluatie van hergebruik. De afwezigheid van een DrugBank-ID-mapping is waarschijnlijk de worteloorzaak die voorkomt dat de voorspellingspijplijn wordt uitgevoerd, omdat de kennisfaaf een geldige DrugBank-identifier nodig heeft om kandidaten te genereren.

**Om door te gaan is het volgende nodig:**

1. **Zet DrugBank-mapping op** — De DrugBank-ID van Amitriptilline is [DB00321](https://go.drugbank.com/drugs/DB00321). Dit moet in het bewijspakket worden ingevuld om voorspelling op basis van KG in te schakelen
2. **Voer de TxGNN-voorspellingspijplijn opnieuw uit** zodra de DrugBank-ID correct is in kaart gebracht
3. **Haal SmPC/label-gegevens op** — Download en ontleed het productlabel om gegevenslacunes voor veiligheid in te vullen (DG001)
4. **Vul MOA-gegevens in** van DrugBank (DG002) — Doelstellingen van Amitriptilline zijn onder andere SLC6A4 (SERT), SLC6A2 (NET) en meerdere receptorsubtypes
5. **Verifieer marketingstatus** — Amitriptilline is breed beschikbaar internationally; bevestig of de status "niet in de handel" de scope van de lokale dataset weerspiegelt of een werkelijke lacune
6. **Voer bewijsverzameling opnieuw uit** (ClinicalTrials.gov, PubMed) zodra een voorspelde indicatie beschikbaar is

---

*⚠️ Disclaimer: Dit rapport is voor onderzoeksdoeleinden en vormt geen medisch advies. Kandidaten voor geneesmiddelhergebruik vereisen klinische validatie voordat toepassing. Gegevensafsnijdatum: 2026-04-03.*

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

