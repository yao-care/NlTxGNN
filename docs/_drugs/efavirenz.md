---
layout: default
title: Efavirenz
parent: Alleen modelvoorspelling (L5)
nav_order: 57
evidence_level: L5
indication_count: 3
---

# Efavirenz
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

# Efavirenz: van HIV-1-infectie naar Simian Immunodeficiency Virus-infectie

## Samenvatting in één zin

Efavirenz is een remmer van non-nucleoside reverse transcriptase (NNRTI), klinisch vastgesteld als eerstelijns antiretrovirale stof voor HIV-1-infectie bij mensen.
Het TxGNN-model voorspelt dat het mogelijk werkzaam kan zijn voor **Simian Immunodeficiency Virus (SIV)-infectie** met een voorspellingsscore van **99.80%**,
maar er zijn momenteel **0 klinische trials** en **0 publicaties** die deze richting specifiek ondersteunen — de voorspelling berust volledig op mechanistische en grafische gevolgtrekking.

---

## Snelüberzicht

| Item | Inhoud |
|------|--------|
| Originele indicatie | HIV-1-infectie (wereldwijd vastgesteld; geen Nederlandse handelstoestemming op bestand) |
| Voorspelde nieuwe indicatie | Simian Immunodeficiency Virus-infectie |
| TxGNN-voorspellingsscore | 99.80% |
| Bewijsniveau | L5 — alleen modelvoorspelling, geen feitelijke onderzoeken |
| Status op Nederlandse markt | Niet geregistreerd (niet op de markt gebracht) |
| Aantal autorisaties | 0 |
| Aanbevolen besluit | In afwachting |

---

## Waarom is deze voorspelling redelijk?

Momenteel zijn gedetailleerde gegevens over het werkingsmechanisme niet beschikbaar in dit Evidence Pack. Op basis van vastgestelde farmacologische kennis is efavirenz een selectieve NNRTI die direct bindt aan en remming van HIV-1 reverse transcriptase bewerkstelligt — een enzym dat het virus nodig heeft om zijn RNA-genoom om te zetten in DNA voor integratie in de gascel. Dit werkingsmechanisme is geheel virusspecifiek: efavirenz remt geen humane DNA-polymerase.

De biologische koppeling aan SIV-infectie is structureel overtuigend. Simian Immunodeficiency Virus is een lentivirus dat significante genomische en enzymatische homologie deelt met HIV-1; beide virussen zijn afhankelijk van reverse transcriptase voor replicatie, en de actieve plaatsen van hun respectieve polymerasen zijn structureel geconserveerd. De TxGNN-kennisgraaf vangt waarschijnlijk deze fylogenetische en enzymatische relatie in bij het genereren van een voorspellingsscore met hoog vertrouwen.

Dat gezegd hebbende, betekenen soortspecifieke verschillen in reverse transcriptase-conformatie dat NNRTI's die zijn geoptimaliseerd tegen HIV-1 RT niet automatisch hun werkzaamheid behouden tegen SIV RT. SIV-modellen in niet-menselijke primaten worden veel gebruikt in onderzoek naar HIV-vaccins en antivirale middelen, dus elk potentieel nut zou liggen in preklinisch/translationeel onderzoek in plaats van directe klinische toepassing bij patiënten.

---

## Klinisch onderzoeksbewijs

Er zijn momenteel geen gerelateerde klinische trials geregistreerd voor efavirenz bij Simian Immunodeficiency Virus-infectie.

---

## Literatuurbewijs

Er is momenteel geen gerelateerde literatuur beschikbaar voor efavirenz bij Simian Immunodeficiency Virus-infectie.

---

## Informatie over de Nederlandse markt

Efavirenz heeft momenteel **geen handelstoestemming** in Nederland. Er zijn geen CBG-MEB (College ter Beoordeling van Geneesmiddelen) geregistreerde producten op bestand. Artsen die efavirenz in Nederland willen gebruiken, zouden dit moeten benaderen via een benoemd-patiëntprocedure of humanitair gebruiksprocedure, of als onderdeel van een door de EMA geautoriseerd combinatieproduct (bijvoorbeeld Atripla, dat efavirenz/emtricitabine/tenofovirdisoproxilfumarat bevat en EMA-gecentraliseerde toestemming heeft, maar buiten het bereik van deze herbeschouwing valt).

---

## Veiligheidsbeschouwingen

Raadpleeg alstublieft de SmPC (Summary of Product Characteristics/Samenvatting van Productkenmerken) voor veiligheidsinformatie. Er waren geen belangrijke waarschuwingen, contra-indicaties of geneesmiddelinteractiegegevens beschikbaar in dit Evidence Pack.

---

## Conclusie en vervolgstappen

**Besluit: In afwachting**

**Reden:**
Het TxGNN-model wijst een bijna maximale betrouwbaarheidsscore toe aan deze herbeschouwingscandidate op basis van de mechanistische overlap tussen HIV-1 en SIV reverse transcriptasen; echter is er momenteel **geen ondersteunend klinisch onderzoek of gepubliceerde literatuurevidentie** voor efavirenz bij SIV-infectie, wat dit stellig op bewijsniveau L5 plaatst. Bovendien is SIV-infectie een ziekte bij niet-menselijke primaten — elke translationale toepassing zou plaatsvinden in preklinische onderzoeksinstellingen, niet directe patiëntenzorg binnen het Nederlandse gezondheidssysteem. Het ontbreken van een Nederlandse (of EMA) handelstoestemming voor efavirenz als zelfstandig product bemoeilijkt het regelgevingstraject verder.

**Om verder te gaan is het volgende nodig:**

- **MOA-gegevensgat oplossing**: Haal volledige Efavirenz SmPC / DrugBank-invoer op om NNRTI-werkingsmechanisme en bekend RT-remmingsspectrum, inclusief vergelijkende activiteit tegen SIV RT, te documenteren
- **Preklinisch bewijsonderzoek**: Voer een systematisch onderzoek uit van literatuur over in vitro- en primatenmodelonderzoeken naar efavirenz-activiteit tegen SIV-stammen (dit Evidence Pack retourneerde nul resultaten, maar gerichte biochemische literatuur kan beschikbaar zijn)
- **Regelgevingsopheldering**: Bepaal of de beoogde gebruikscontext is (a) een veterinair/primatenmodelonderzoeksinstrument of (b) een klinische toepassing bij mensen — het regelgevingstraject verschilt aanzienlijk
- **Veiligheidsdocumentatie**: Verkrijg volledige SmPC-waarschuwingen en contra-indicaties om de S1-veiligheidsbeveiligingsstap te voltooien (momenteel geblokkeerd door Data Gap DG001)
- **Evaluatie van rangorde-2 indicatie**: De op één na hoogste voorspelling in het Evidence Pack (feline verworven immunodeficiëntie, dezelfde score van 99.80%) heeft één ondersteunende biochemische studie (PMID [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/)) waarin NNRTI-activiteit tegen FIV en HIV-1 reverse transcriptasen wordt vergeleken — dit kan een meer concreet aanknopingspunt voor nader onderzoek vertegenwoordigen

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

