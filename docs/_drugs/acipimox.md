---
layout: default
title: Acipimox
parent: Alleen modelvoorspelling (L5)
nav_order: 17
evidence_level: L5
indication_count: 0
---

# Acipimox
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

# Acipimox: Beoordeling Herpositionering Geneesmiddel — Geen Voorspelde Indicaties Beschikbaar

## Samenvatting in Één Zin

Acipimox is een afgeleide van nicotinezuur (niacine-analoog) die in het verleden werd gebruikt als een vetverlagend middel voor de behandeling van dyslipemie. Het TxGNN-model heeft **geen herpositioneringsvoorspellingen gegenereerd** voor deze verbinding, en het geneesmiddel is **momenteel niet geregistreerd** in het geëvalueerde grondgebied. Er zijn onvoldoende gegevens beschikbaar om een herpositioneringsevaluatie op dit moment te ondersteunen.

---

## Snel Overzicht

| Item | Inhoud |
|------|--------|
| Geneesmiddel (INN) | Acipimox |
| DrugBank ID | [DB09055](https://go.drugbank.com/drugs/DB09055) |
| Oorspronkelijke Indicatie | Niet vastgelegd in evidencepakket (extern bekend: dyslipemie / hyperlipemie) |
| Voorspelde Nieuwe Indicatie | **Geen** — TxGNN heeft geen voorspellingen geretourneerd |
| TxGNN Voorspellingsscore | N/A |
| Bewijsniveau | **L5** — Geen modelvoorspelling, geen klinisch bewijs |
| Handelsstatuut | Niet geregistreerd (Niet geregistreerd) |
| Aantal Autorisaties | 0 |
| Aanbevolen Besluit | **Vasthouden** |

---

## Waarom is Deze Voorspelling Redelijk?

**Er is geen voorspelling gegenereerd door TxGNN voor Acipimox.** Daarom kan dit gedeelte de mechanistische plausibiliteit voor een nieuwe indicatie niet beoordelen.

Voor context: Acipimox is een pyrazinederivaat van nicotinezuur (niacine). Het werkt als een vetmodificerend middel dat lipolyse in vetweefsel remt, wat leidt tot verlaagde circulerende vrije vetzuren, verminderde hepatische triglyceridensynthese en verlaagde VLDL-secretie. Het verhoogt ook bescheiden HDL-cholesterol. Het werd vooral in Europa gebruikt voor de behandeling van hyperlipidemie Type IIb en Type IV.

Momenteel waren gedetailleerde werkingsmechanisme (MOA)-gegevens niet beschikbaar in het evidencepakket (gemarkeerd als Gegevensgat DG002). De afwezigheid van TxGNN-voorspellingen kan worden toegeschreven aan de beperkte aanwezigheid van het geneesmiddel in de kennissgraaf of zijn smal farmacologisch profiel. Een DrugBank API-query wordt aanbevolen om de MOA-gegevens aan te vullen voordat de voorspellingspijplijn opnieuw wordt uitgevoerd.

---

## Klinisch Onderzoeksbewijs

Momenteel zijn er geen gerelateerde klinische onderzoeken beschikbaar, aangezien er geen nieuwe indicatie is voorspeld.

---

## Literatuurbewijs

Momenteel is er geen gerelateerde literatuur beschikbaar voor een herpositioneringsrichting, aangezien er geen nieuwe indicatie is voorspeld.

---

## Marktgegevens

Acipimox heeft **geen handelsautorisaties** in het geëvalueerde grondgebied (Taiwan/TFDA). Het geneesmiddel is geclassificeerd als **niet geregistreerd** (Niet geregistreerd).

| RVG/Licentienummer | Productnaam | Galenische Vorm | Goedgekeurde Indicatie |
|---------------------|-------------|-------------|---------------------|
| — | — | — | Geen licenties op record |

> **Opmerking:** Acipimox werd historisch vermarkt in verschillende Europese landen (bijv. als Olbetam®) maar is in de meeste markten stopgezet of ingetrokken.

---

## Veiligheidsbeschouwingen

> Raadpleeg de SmPC (Samenvatting van Productkenmerken) of de originele productdocumentatie voor veiligheidsinformatie. Alle veiligheidsvelden (belangrijke waarschuwingen, contra-indicaties en geneesmiddel-geneesmiddelinteracties) zijn momenteel niet beschikbaar in het evidencepakket.

**Geïdentificeerde gegevensgaten:**
- TFDA-labelwaarschuwingen en contra-indicaties zijn niet beschikbaar (Gegevensgat DG001, ernst: **Blokkerend**)
- Geen geneesmiddel-geneesmiddelinteracties werden gevonden in de DDI-databasequery

---

## Samenvatting Gegevensgaten

De volgende kritieke gegevensgaten werden geïdentificeerd en moeten worden opgelost voordat enige herpositioneringsevaluatie kan plaatsvinden:

| Gat-ID | Categorie | Item | Ernst | Aanbevolen Herstelmaatregel |
|--------|----------|------|----------|------------------------|
| DG001 | Geneesmiddelniveau | Labelwaarschuwingen / contra-indicaties | **Blokkerend** | Download en verwerk productlabel PDF van regelgevingsinstantie |
| DG002 | Geneesmiddelniveau | Werkingsmechanisme (MOA) | **Hoog** | Query DrugBank API voor farmacodynamische gegevens |
| — | Voorspelling | TxGNN voorspelde indicaties | **Blokkerend** | Verifieer DrugBank ID-mapping in kennissgraaf; voer voorspellingspijplijn opnieuw uit |

---

## Conclusie en Vervolgstappen

**Besluit: Vasthouden**

**Motivering:**
Acipimox heeft geen TxGNN-voorspelde herpositioneringsindicaties, geen actieve handelsautorisatie in het grondgebied, en meerdere blokkerende gegevensgaten. Er is momenteel geen basis waarop een herpositioneringskans kan worden geëvalueerd.

**Om verder te gaan, is het volgende nodig:**
- Gegevensgat **DG002** oplossen: Gedetailleerde MOA- en farmacologische doelgegevens van DrugBank ophalen om de kennissgraaf aan te vullen
- Verifieer dat Acipimox (DB09055) correct is weergegeven in de TxGNN-kennissgraaf (`data/kg.csv`) en voer de voorspellingspijplijn opnieuw uit
- Gegevensgat **DG001** oplossen: Verkrijg veiligheidgegevens van de SmPC van de originele producent of EMA-beoordelingsrapporten (Olbetam® historisch dossier)
- Beoordeel of de ingetrokken status van het geneesmiddel in de meeste markten herpositionering commercieel levensvatbaar maakt voordat u verder analytische inspanning investeert
- Indien voorspellingen worden gegenereerd bij heruitvoering, verzamel klinisch onderzoeks- en literatuurbewijzen via ClinicalTrials.gov en PubMed collectors

---

*⚠️ Disclaimer: Dit rapport is bedoeld voor onderzoeksdoeleinden alleen en vormt geen medisch advies. Alle herpositioneringskandidaten voor geneesmiddelen vereisen klinische validatie vóór therapeutische toepassing.*

*🤖 Gegenereerd met [Claude Code](https://claude.com/claude-code) — Gegevenscutoff: 2026-04-03*

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

