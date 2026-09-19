---
layout: default
title: Meloxicam
parent: Alleen modelvoorspelling (L5)
nav_order: 92
evidence_level: L5
indication_count: 10
---

# Meloxicam
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **10** 
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

# Meloxicam: Van osteoartritis naar Acromesomale dysplasie, Hunter-Thompson-type

## Samenvatting in één zin

Meloxicam is een selectieve COX-2-remmer (NSAID) die veel wordt gebruikt voor pijn- en ontstekingsbestrijding bij musculoskeletale aandoeningen zoals osteoartritis en reumatoïde artritis.
Het TxGNN-model voorspelt dat het mogelijk relevant is voor **Acromesomale dysplasie, Hunter-Thompson-type**,
echter wordt deze voorspelling momenteel ondersteund door **0 klinische trials en 0 publicaties**, wat het op het laagste bewijsniveau (L5) plaatst met een **Hold**-aanbeveling.

---

## Snel overzicht

| Item | Inhoud |
|------|--------|
| Oorspronkelijke indicatie | Geen gegevens over autorisatie in Nederland (CBG-MEB) beschikbaar |
| Voorspelde nieuwe indicatie | Acromesomale dysplasie, Hunter-Thompson-type |
| TxGNN-voorspellingsscore | 99.92% |
| Bewijsniveau | L5 |
| NL-markeringsstatus | Niet geregistreerd (0 autorisaties gevonden) |
| Aantal autorisaties | 0 |
| Aanbevolen beslissing | Hold |

---

## Waarom is deze voorspelling redelijk?

Momenteel zijn gedetailleerde gegevens over het werkingsmechanisme niet beschikbaar in deze Evidence Pack. Op basis van goed gevestigd farmacologisch kennis is meloxicam een preferentiële COX-2-remmer van de oxicamklasse. Het onderdrukt prostaglandinesynthese — met name PGE₂ — door selectief cyclooxygenase-2 (COX-2) te remmen, waardoor ontstekingen, pijn en koorts worden verminderd. Zijn klinische rol is goed vastgesteld bij ontstekelijke musculoskeletale aandoeningen, waaronder osteoartritis, reumatoïde artritis en ankyloserende spondylitis. In Nederland worden NSAID's van deze klasse gereguleerd onder toezicht van CBG-MEB en voorgeschreven volgens de SmPC.

Acromesomale dysplasie, Hunter-Thompson-type (ACMSD) is een zeldzame autosomaal recessieve skeletdysplasie veroorzaakt door verliesfunctiemutaties in het *GDF5*-gen (dat Cartilage-Derived Morphogenetic Protein-1, CDMP1 codeert). De aandoening wordt gekenmerkt door ernstige verkorting van de middel- en distale ledematen, als gevolg van verstoord bot-morfogenetisch proteïnesignalering tijdens skeletale ontwikkeling. Cruciaal is dat **dit een structurele genetische aandoening is zonder een vastgesteld ontstekings- of COX-pad-gedreven pathomechanisme**. Er is geen biologische grondslag voor COX-2-remming om het ziektebeloop te wijzigen.

De hoge voorspellingsscore (99.92%) van het TxGNN-model weerspiegelt waarschijnlijk **netwerknauwheid** tussen Meloxicam en skeletziekteknooppunten binnen de kennisgraaf — een erkende beperking van graafgebaseerde voorspellingsmodellen — in plaats van een echt therapeutische relatie. Deze voorspelling moet worden beschouwd als een computationeel artefact in plaats van een klinisch bruikbaar signaal. Voor context: meer mechanistisch plausibele repositioningskandidaten in deze Evidence Pack zijn onder meer **spondyloartropatie (rang 6)**, waar NSAID's een eerste-lijnsbehandeling zijn, en **RF-positieve polyarticulaire juveniele idiopathische artritis (rang 8)**, waarbij indirecte NSAID-veiligheidsliteratuur bestaat (PMID: 25057265).

---

## Bewijs uit klinische trials

Momenteel zijn geen gerelateerde klinische trials geregistreerd.

---

## Literatuurbewijs

Momenteel is geen gerelateerde literatuur beschikbaar.

---

## Informatie over de Nederlandse markt

Er werden geen CBG-MEB-marketingautorisaties in de huidige dataset opgehaald (0 records). Meloxicam is een veel vermarkt NSAID in Europa, en dit resultaat is waarschijnlijk een **gegevensverzamelingsleemte** in plaats van een werkelijke weerspiegeling van de beschikbaarheid op de Nederlandse markt. Onafhankelijke verificatie via het openbare CBG-MEB-register wordt sterk aanbevolen voordat regelgevingsconclusions worden getrokken.

---

## Veiligheidsbeschouwingen

Raadpleeg de SmPC (Samenvatting van het Productkenmerk) voor volledige veiligheidsinformatie, inclusief waarschuwingen, contra-indicaties en geneesmiddelinteracties. Opmerking: als NSAID draagt meloxicam klassenniveauoverwegingen met zich mee (bijvoorbeeld gastro-intestinale, cardiovasculaire en renale risico's) die relevant zijn ongeacht de indicatie die wordt geëvalueerd.

---

## Conclusie en vervolgstappen

**Beslissing: Hold**

**Rationale:**
De best geclassificeerde TxGNN-voorspelling — acromesomale dysplasie, Hunter-Thompson-type — is een genetische structurele aandoening zonder bekende ontstekings- of COX-2-padweg betrokkenheid. Met nul klinische trials, nul ondersteunende publicaties (L5-bewijs) en een mechanistisch mismatch, is er geen basis om verder te gaan voor deze specifieke indicatie.

**Om verder te gaan, is het volgende nodig:**

- **Verificatie van de NL-markeringsstatus** via het openbare CBG-MEB-register (https://www.cbg-meb.nl/) — huidige gegevens weerspiegelen waarschijnlijk een verzamelingsleemte
- **Verkrijg de Meloxicam SmPC** om volledige waarschuwingen, contra-indicaties en geneesmiddelinteractiegegevens op te halen (momenteel allemaal vermeld als gegevensleemten)
- **MOA-gegevens ophalen** van DrugBank (DB00814) om formeel het COX-2-selectiviteitsprofiel voor mechanistische analyse vast te leggen
- **Herbepaal de prioritering van repositioningsevaluatie** naar kandidaten met hogere waarde in dezelfde Evidence Pack:
  - **Rang 6 — Spondyloartropatie**: NSAID's zijn een eerste-lijnstherapie; mechanistisch geldig; vereist bevestigend onderzoek in bredere literatuurdatabases
  - **Rang 8 — RF-positieve polyarticulaire juveniele idiopathische artritis**: Indirecte NSAID-veiligheidsbewijs bestaat ([PMID: 25057265](https://pubmed.ncbi.nlm.nih.gov/25057265/)); Meloxicam is goedgekeurd voor JIA in sommige markten (bijv. USA); NL-goedkeuringsstatus moet worden geverifieerd
- **Voer gerichte literatuarzoekopdrachten** uit voor Meloxicam in SpA- en JIA-populaties om vast te stellen of voldoende bewijs bestaat voor een L3- of hoger bewijsdesignatie

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

