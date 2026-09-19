---
layout: default
title: Cholecalciferol
parent: Alleen modelvoorspelling (L5)
nav_order: 41
evidence_level: L5
indication_count: 7
---

# Cholecalciferol
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **7** 
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

# Cholecalciferol: Van vitamine D-suppletie tot familiaire geïsoleerde hypoparathyroïdie door verminderde PTH-secretie

## Samenvatting in één zin

Cholecalciferol (vitamine D3) is een vetoplosbare voedingsstof en geneesmiddel dat klassiek wordt gebruikt om vitamine D-deficiëntie te corrigeren en de calcium-fosfaathuishouding en beendeelgezondheid te ondersteunen, hoewel het momenteel geen registratie bij de Nederlandse CBG-MEB heeft.
Het TxGNN-model voorspelt dat het effectief kan zijn voor **familiaire geïsoleerde hypoparathyroïdie door verminderde PTH-secretie** (wereldwijde rang #553 onder alle ziektevoorspellingen),
zonder **klinische onderzoeken** en **geen ziekte-specifieke publicaties** die deze richting momenteel ondersteunen — het bewijs blijft beperkt tot het niveau van modelvoorspelling.

---

## Snelleoverzicht

| Item | Inhoud |
|------|--------|
| Oorspronkelijke indicatie | Vitamine D-deficiëntie; ondersteuning van calcium- en fosfaatmetabolisme (geen Nederlandse registratie aanwezig) |
| Voorspelde nieuwe indicatie | Familiaire geïsoleerde hypoparathyroïdie door verminderde PTH-secretie |
| TxGNN-voorspellingsscore | 99.79% |
| Bewijsniveau | L5 |
| Nederlandse marktstand | Niet op de markt (Niet op de markt) |
| Aantal registraties | 0 |
| Aanbevolen beslissing | Uitstel |

---

## Waarom is deze voorspelling redelijk?

Formele gegevens over het werkingsmechanisme werden niet uit DrugBank opgehaald voor dit bewijspakket. De farmacologie van cholecalciferol is echter goed vastgesteld: het is een **inactieve voorloper van het vitamine D-hormoonsysteem**. Na huidzynthese of orale inname ondergaat cholecalciferol eerste-passage 25-hydroxylering in de lever (waarbij 25-hydroxyvitamine D ontstaat, de belangrijkste circulerende opslagvorm) en vervolgens een kritieke tweede hydroxylering in de nier via het enzym 1α-hydroxylase (CYP27B1), wat calcitriol [1,25(OH)₂D] oplevert — het biologisch actieve hormoon dat intestinale calcium- en fosfaatopname bevordert en werkt op bot en de bijschildklieren.

Familiaire geïsoleerde hypoparathyroïdie door verminderde PTH-secretie is een zeldzame erfelijke aandoening waarin de bijschildklieren structureel aanwezig zijn maar niet voldoende PTH uitscheiden. Dit leidt tot chronische hypocalcaemie en hyperfosfataemie. Het kritieke farmacologische probleem voor cholecalciferol in deze setting is dat **PTH een van de primaire stimulatoren van renale 1α-hydroxylase is**: PTH-deficiëntie verstoort daarom direct de conversie van cholecalciferol naar calcitriol. Het suppleren van de inactieve voorloper bij een patiënt die deze niet efficiënt kan activeren, is een mechanistisch suboptimale strategie en brengt een echt risico op onvoldoende therapeutisch effect met zich mee. Actieve vitamine D-analoga — calcitriol of alfacalcidol — omzeilen dit conversie-knelpunt volledig en vertegenwoordigen de huidige klinische standaardbehandeling voor hypoparathyroïdie.

Het TxGNN-model wijst een hoge score (99.79%) toe aan deze combinatie, waarschijnlijk omdat het model de gedeelde knooppunten vastlegt die vitamine D-metabolisme, calciumsignalering en bijschildklierbologie in het kennisgraaf verbinden, in plaats van een specifieke farmacologische superioriteit van cholecalciferol ten opzichte van bestaande actieve analoga op te sporen. De mechanistische verbinding is reëel op biologisch systeemniveau, maar zeer speculatief als therapeutische rationale voor cholecalciferol specifiek. Er zijn geen klinische onderzoeken en geen ziekte-specifieke publicaties geïdentificeerd die deze herbestemming ondersteunen.

---

## Bewijs uit klinische onderzoeken

Momenteel zijn geen gerelateerde klinische onderzoeken geregistreerd voor deze specifieke indicatie (familiaire geïsoleerde hypoparathyroïdie door verminderde PTH-secretie).

---

## Literatuurbewijs

Momenteel geen gerelateerde literatuur beschikbaar voor deze indicatie.

---

## Veiligheidsoverwegingen

Raadpleeg de SmPC (Samenvatting van productkenmerken) voor veiligheidsinformatie. Er werden geen gegevens over geneesmiddel-geneesmiddelinteracties, belangrijke waarschuwingen of contra-indicaties gevonden in de gegevensbronnen die voor dit bewijspakket werden geraadpleegd (DDI-querystatus: niet gevonden; belangrijke waarschuwingen en contra-indicaties: niet beschikbaar in de geraadpleegde bronnen).

> **Praktische noot voor clinici:** Hoewel specifieke veiligheidsgegevens niet werden opgehaald, omvatten bekende risico's van vitamine D-suppletie **hypercalcaemie** en **hypercalciurie**, die van bijzonder belang zijn bij aandoeningen waarbij de calciumhuishouding al verstoord is, zoals hypoparathyroïdie. Regelmatige bewaking van serumcalcium, urineacalcium en nierfunctie is standaardpraktijk.

---

## Conclusie en vervolgstappen

**Beslissing: Uitstel**

**Rationale:**
Dit is een voorspelling op modelniveau (L5) zonder ondersteunende klinische onderzoeken of ziekte-specifieke publicaties. Nog kritiekser is dat de mechanistische rationale farmacologisch zelflimiterend is: cholecalciferol is, als inactieve voorloper die PTH-afhankelijke 1α-hydroxylering voor activering nodig heeft, niet de geschikte medicijnvorm voor een aandoening gekenmerkt door PTH-deficiëntie. Actieve vitamine D-analoga (calcitriol, alfacalcidol) zijn de gevestigde en richtlijngesteunde standaardbehandeling voor hypoparathyroïdie en zouden de wetenschappelijk ondersteunde herbestemming-kandidaten in dit ziektegebied zijn — niet cholecalciferol.

**Om door te gaan, zou het volgende nodig zijn:**

- Opvraging van TFDA/EMA SmPC-gegevens voor formele veiligheidsevaluatie (waarschuwingen, contra-indicaties, toxicologie)
- Volledige opvraging van DrugBank MOA-gegevens om de mechanistische basis te bevestigen
- Een preklinische of mechanistische studie die specifiek aantoont dat cholecalciferol een klinisch betekenisvol voordeel **boven** calcitriol/alfacalcidol bij PTH-deficiënte patiënten biedt (bijvoorbeeld via extrarenale 1α-hydroxyleringswegen)
- Op zijn minst, caseverslagen of pilotgegevens specifiek voor familiaire geïsoleerde hypoparathyroïdie waarbij cholecalciferol als interventie wordt gebruikt
- Verduidelijking van de regelgevingsclassificatie van cholecalciferol in Nederland (voedingssupplement versus geneesmiddel), aangezien dit van invloed is op het toepasselijke regelgevingstraject onder CBG-MEB/EMA-kader

> **Onderzoeksnoot:** Indien de bredere vraag over vitamine D–hypoparathyroïdie-herbestemming van belang is, zou het onderzoek verplaatsen naar **actieve analoga die al in Nederland zijn geregistreerd** (calcitriol, alfacalcidol, paricalcitol) mechanistisch verdedigbaarder zijn en waarschijnlijk hoger kwaliteitsbewijs opleveren.

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

