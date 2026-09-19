---
layout: default
title: Abacavir
parent: Alleen modelvoorspelling (L5)
nav_order: 11
evidence_level: L5
indication_count: 3
---

# Abacavir
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **3** 
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

# Abacavir: Van HIV-behandeling naar infectie met Simian Immunodeficiency Virus

## Samenvatting in één zin

Abacavir is een reverse-transcriptaseremmer van het nucleosidetype (NRTI) die veel wordt gebruikt als onderdeel van combinatie-antiretrovirale therapie voor HIV-1-infectie. Het TxGNN-model voorspelt dat het effectief kan zijn voor **infectie met Simian Immunodeficiency Virus (SIV)**, met **0 klinische onderzoeken** en **1 publicatie** momenteel beschikbaar. Echter, alle drie voorspellingen op de bovenste rijen betreffen ziekten bij niet-menselijke dieren of zeldzame genetische aandoeningen zonder mechanistische basis, waardoor ze **niet klinisch toepasbaar zijn** in de geneeskunde voor mensen.

## Snel overzicht

| Item | Inhoud |
|------|--------|
| Originele indicatie | HIV-1-infectie (antiretrovirale combinatietherapie) |
| Voorspelde nieuwe indicatie | Infectie met Simian Immunodeficiency Virus |
| TxGNN-voorspellingsscore | 99,79% |
| Bewijsniveau | L4 — Preklinisch / in vitro-onderzoek alleen |
| Status Nederlandse markt | Niet geregistreerd (geen CBG-MEB-licenties in gegevensset) |
| Aantal autorisaties | 0 (Opmerking: Abacavir is EMA-goedgekeurd als Ziagen®; afwezigheid weerspiegelt waarschijnlijk de reikwijdte van de gegevensbron) |
| Aanbevolen beslissing | **Aangehouden** |

## Waarom is deze voorspelling redelijk?

Abacavir is een nucleosideanaloog reverse-transcriptaseremmer (NRTI) die, nadat het intracellulair is gefosforyleerd tot zijn actieve metaboliet carbovirtriphosphaat, competitief reverse-transcriptase van HIV-1 remt en de kettingverlengering van proviral DNA beëindigt. Het is een hoeksteen van moderne HIV-1-combinatie-antiretrovirale therapie, meestal samen met lamivudine (als Kivexa®/Epzicom®) of met lamivudine en dolutegravir (als Triumeq®). Gedetailleerde informatie over het werkingsmechanisme was niet beschikbaar in dit bewijspakket, maar het werkingsmechanisme van de NRTI-klasse is goed vastgesteld in de literatuur.

De TxGNN-voorspelling die abacavir linkt aan SIV-infectie heeft een duidelijke mechanistische rationale: SIV behoort tot hetzelfde Lentivirus-geslacht als HIV en deelt het reverse-transcriptase-enzym dat door NRTI's wordt gericht. Een in vitro-onderzoek (PMID 15040537) heeft aangetoond dat SIV-stammen gevoeligheid hebben voor meerdere anti-HIV-1-verbindingen, inclusief abacavir. Vanuit een zuiver moleculair standpunt is de voorspelling farmacologisch onderbouwd.

**Kritieke beperking:** SIV infecteert uitsluitend niet-menselijke primaten en veroorzaakt geen ziekte bij mensen. Daarom heeft deze voorspelling, ondanks de hoge TxGNN-score en geldige mechanistische basis, **geen rechtstreekse waarde voor klinische toepassing** voor geneesmiddelhergebruik bij mensen. Hetzelfde geldt voor de tweede-gerangschikte voorspelling (verworven feline immunodeficiëntiestoornis, een uitsluitend feliene ziekte) en de derde-gerangschikte voorspelling (een zeldzame monogene neuronale ontwikkelingsstoornis zonder bekend mechanistisch verband met NRTI-activiteit). Dit geval benadrukt een bekende beperking van op kennisgrafieken gebaseerde modellen: voorspellingen met hoge scores kunnen echte biologische relaties weerspiegelen die desondanks geen menselijke therapeutische relevantie hebben.

## Klinische onderzoeksevidentie — Indicatie 1: SIV-infectie

Momenteel geen gerelateerde klinische onderzoeken geregistreerd.

## Literatuurevidentie — Indicatie 1: SIV-infectie

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|------|------|------------|--------------------------|
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro gevoeligheidsonderzoek | Antiviral Therapy | Evalueerde 16 goedgekeurde antiretrovirale middelen (inclusief abacavir) tegen HIV-2, SIV (mac251, B670) en SHIV-stammen. Aangetoond dat SIV-stammen gevoelig zijn voor meerdere anti-HIV-1 NRTI's, wat een preklinische rationale biedt voor overwegingen van post-blootstellingsprofylaxe in laboratoriumomgevingen. |

## Klinische onderzoeksevidentie — Indicatie 2: Verworven feline immunodeficiëntiestoornis

> **Opmerking:** Alle vier klinische onderzoeken die zijn opgehaald, zijn menselijke HIV-1-onderzoeken die zijn geretourneerd door trefwoordovereenkomst op "Abacavir." Geen daarvan is relevant voor feline immunodeficiëntiavirus (FIV). Ze worden hieronder voor volledigheid vermeld met relevantiegradering.

| Onderzoeksnummer | Fase | Status | Inschrijvingen | Belangrijkste bevindingen |
|---------|------|--------|---------|--------------------------|
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Fase 2 | Voltooid | 208 | Dosisbepaling studie voor dolutegravir + ABC/3TC bij antiretrovirale-naïeve HIV-1-patiënten. **Niet relevant voor FIV** (Graad C). |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Fase 3 | Voltooid | 844 | SINGLE-onderzoek: DTG + ABC/3TC vs Atripla bij antiretrovirale-naïeve HIV-1-volwassenen over 96 weken. **Niet relevant voor FIV** (Graad C). |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Fase 3 | Voltooid | 828 | SPRING-2-onderzoek: DTG vs raltegravir met dubbele NRTI-ruggengraat bij antiretrovirale-naïeve HIV-1-volwassenen. **Niet relevant voor FIV** (Graad C). |
| [NCT01499199](https://clinicaltrials.gov/study/NCT01499199) | Fase 3 | Voltooid | 13 | Farmacokinetiek van CNS en plasma van DTG + ABC/3TC bij antiretrovirale-naïeve HIV-1-onderwerpen. **Niet relevant voor FIV** (Graad C). |

## Literatuurevidentie — Indicatie 2: Verworven feline immunodeficiëntiestoornis

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|------|------|------------|--------------------------|
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | Dierenonderzoek (in vitro, feline model) | Antiviral Research | Onderzocht gecombineerde ZDV + 3TC + abacavir triple therapie tegen FIV-replicatie in vitro. Aangetoond dat NRTI's die effectief zijn tegen HIV ook FIV remmen, wat de binnenhuiskat als diermodel voor HIV-geneesmiddelenonderzoek ondersteunt. Niet van toepassing op menselijk geneesmiddelhergebruik. |

## Klinische onderzoeks- en literatuurevidentie — Indicatie 3: Neuronale ontwikkelingsstoornis met atactische gang, afwezige spraak en verminderde corticale witte stof

Momenteel geen gerelateerde klinische onderzoeken geregistreerd.

Momenteel geen gerelateerde literatuur beschikbaar.

## Informatie over Nederlandse markt

Er werden geen CBG-MEB-marktgoedkeuringen in de gegevensset voor abacavir gevonden.

> **Opmerking:** Abacavir staat bekend als EMA-goedgekeurd in de EU via gecentraliseerde procedure als **Ziagen®** (ViiV Healthcare) en is in Nederland beschikbaar in meerdere vaste-dosis combinaties (Kivexa®, Triumeq®). De afwezigheid in deze gegevensset weerspiegelt waarschijnlijk de reikwijdte van de gegevensbron (Taiwan TFDA) in plaats van werkelijke onbeschikbaarheid in Nederland. Voorschrijvers moeten de [CBG-MEB Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/) raadplegen voor de huidige Nederlandse autorisatiestatus.

## Veiligheidsopmerkingen

Raadpleeg de SmPC (Samenvatting van de Productkenmerken) voor uitgebreide veiligheidsinformatie.

> **Bekend veiligheidsprobleem (niet uit bewijspakket):** Abacavir draagt een goed gevestigd risico van **overgevoelighheidsreactie (HSR)** geassocieerd met HLA-B*5701-allel. HLA-B*5701-screening is verplicht voordat abacavir-therapie wordt gestart volgens EMA- en Nederlandse richtlijnen. Deze HSR kan fataal zijn bij herintroductie en is een zwarte doos-waarschuwing in de meeste rechtsgebieden.

## Conclusie en volgende stappen

**Beslissing: Aangehouden**

**Rationale:**
Alle drie door TxGNN voorspelde indicaties voor abacavir zijn ongeschikt voor hergebruik van menselijke geneesmiddelen. De twee beste voorspellingen (SIV-infectie en feline AIDS) betreffen ziekteverwekkers die uitsluitend niet-menselijke soorten infecteren — terwijl de mechanistische link werkelijk is (gedeelde lentivirus reverse-transcriptase-doelen), is er geen klinisch omzettingspad naar menselijke geneeskunde. De derde voorspelling (een zeldzame monogene neuronale ontwikkelingsstoornis) heeft geen mechanistische basis, geen ondersteunend bewijs en vertegenwoordigt een modelartefact. Deze kandidaat mag niet verder voortgang in de hergebruikspijplijn.

**Wat nodig zou zijn om door te gaan:**
- Herbeoordeling van TxGNN-modeloutput met een **filter voor uitsluitend menselijke ziekten** om dierenartsenijkundige en niet-menselijke primaatziekten uit de kandidaatrangschikking uit te sluiten
- Indien abacavir voor hergebruik moet worden overwogen, concentratie op opkomende hypothesen met menselijke relevantie (bijvoorbeeld NRTI-effecten op LINE-1 retrotransposon-activiteit in leeftijdgerelateerde ziekten, of NLRP3 inflammasom-modulatie), die niet in de huidige TxGNN-voorspellingen zijn vastgelegd
- Voltooiing van Nederlandse regelgevingsgegevens door de CBG-MEB Geneesmiddeleninformatiebank te raadplegen
- Oplossing van gegevensgaten: MOA-details uit DrugBank API en SmPC-veiligheidsinformatie (waarschuwingen, contra-indicaties, interacties)

---

*Dit rapport is gegenereerd op 2026-04-03. Resultaten zijn alleen voor onderzoeksdoeleinden en vormen geen medisch advies. Alle kandidaten voor geneesmiddelhergebruik vereisen klinische validatie voordat therapeutische toepassing. Raadpleeg de SmPC (Samenvatting van de Productkenmerken) via de [CBG-MEB](https://www.cbg-meb.nl/) voor gezaghebbende voorschrijfsinformatie.*

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

