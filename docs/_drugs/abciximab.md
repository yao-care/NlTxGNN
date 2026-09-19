---
layout: default
title: Abciximab
parent: Alleen modelvoorspelling (L5)
nav_order: 12
evidence_level: L5
indication_count: 0
---

# Abciximab
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

# ABCIXIMAB: Evaluatie voor Herbestemming van Geneesmiddelen — Geen Kandidaat-indicaties Geïdentificeerd

## Samenvatting in Één Zin

Abciximab (DrugBank: DB00054) is een glycoproteïne IIb/IIIa-receptorinhibitor die historisch wordt gebruikt als antitrombocytair middel tijdens percutane coronaire interventies. Het TxGNN-model genereerde **geen voorspelde nieuwe indicaties** voor dit geneesmiddel, en het bewijspakket bevat **geen klinische onderzoeken** of **publicaties** ter ondersteuning van een herbestemmingsrichting op dit moment.

## Snel Overzicht

| Item | Waarde |
|------|------|
| Drug (INN) | Abciximab |
| DrugBank ID | [DB00054](https://go.drugbank.com/drugs/DB00054) |
| Oorspronkelijke Indicatie | Niet opgenomen in bewijspakket (zie opmerking hieronder) |
| Voorspelde Nieuwe Indicatie | **Geen** — geen TxGNN-voorspellingen beschikbaar |
| TxGNN Prediction Score | N/A |
| Bewijsniveau | **L5** (Geen modelvoorspellingen, geen ondersteunende studies) |
| Marktstatus NL | Niet op de markt (Niet op de markt) |
| Aantal Autorisaties | 0 |
| Aanbevolen Besluit | **In Wacht** |

> **Opmerking over oorspronkelijke indicatie:** Het bewijspakket bevat geen geautoriseerde indicatietekst. Volgens gevestigde farmacologische verwijzingen is abciximab (merknaam ReoPro) een chimeer monoklonaal antilichaam Fab-fragment dat glycoproteïne IIb/IIIa op trombocyten remt, en is gebruikt als aanvullend antitrombocytair middel tijdens percutane coronaire interventie (PCI) en beheer van instabiele angina. Het product is echter in veel markten wereldwijd stopgezet.

## Waarom is deze Voorspelling Redelijk?

Geen TxGNN-voorspellingen werden gegenereerd voor abciximab. Dit kan het gevolg zijn van een of meer van de volgende redenen:

1. **Beperkte connectiviteit van kennisgraaf:** Abciximab is een biologisch geneesmiddel (monoklonaal antilichaam-fragment) in plaats van een kleine molecule. De TxGNN-kennisgraaf kan onvoldoende relatiegegevens voor biologische geneesmiddelen bevatten, wat resulteert in geen herbestemmingskandidaten met hoge betrouwbaarheid.

2. **Markttrekking:** Abciximab (ReoPro) is in veel wereldwijde markten stopgezet of teruggeroepen, inclusief Nederland. Zijn afwezigheid uit actieve regelgevingsdatabases kan zijn connectiviteit binnen het geneesmiddel-ziekte-netwerk van het voorspellingsmodel verminderen.

3. **Beperkt werkingsmechanisme:** Als een zeer specifieke GPIIb/IIIa-inhibitor die werkt op trombocytaire aggregatie, kan het farmacologische mechanisme niet gemakkelijk extrapoleren naar niet-cardiovasculaire ziektegebieden binnen de scoringsdrempel van het model.

Momenteel werden geen gedetailleerde gegevens over werkingsmechanisme in het bewijspakket verstrekt. Op basis van gevestigde farmacologische kennis is abciximab een chimeer humaan-murien monoklonaal antilichaam Fab-fragment dat bindt aan de glycoproteïne IIb/IIIa-receptor op geactiveerde trombocyten, waarbij fibrinogeen-binding wordt voorkomen en daarmee trombocytaire aggregatie wordt geremd. Dit mechanisme is goed gekarakteriseerd maar zeer specifiek voor de stollings-/tromboseroute.

## Bewijs van Klinische Onderzoeken

Momenteel geen gerelateerde klinische onderzoeken geregistreerd voor herbestemmingskandidaten (geen voorspelde indicaties beschikbaar).

## Bewijzen uit Literatuur

Momenteel geen gerelateerde literatuur beschikbaar voor herbestemmingskandidaten (geen voorspelde indicaties beschikbaar).

## Marktinformatie Nederland

Abciximab heeft **geen huidige marketingautorisaties** geregistreerd in het bewijspakket. Het geneesmiddel staat vermeld als **niet op de markt** (Niet op de markt).

> **Regelgevingscontext:** Geen CBG-MEB (College ter Beoordeling van Geneesmiddelen)-registraties of EMA centraal geautoriseerde productrecords werden geïdentificeerd voor dit geneesmiddel. Historisch gezien werd abciximab vermarkt als ReoPro maar is stopgezet in veel rechtsgebieden. Elke toekomstige herbestemmingsconsideratie zou een nieuwe aanvraag om marketinggoedkeuring vereisen.

## Veiligheidsconsideraties

> Zie het SmPC (Samenvatting van de Kenmerken van het Geneesmiddel) voor veiligheidsinformatie. Het bewijspakket bevat geen waarschuwingen, contra-indicaties of geneesmiddel-interactiegegevens voor abciximab. Voor historische referentie documenteerde het ReoPro SmPC belangrijke risico's, waaronder bloeding, trombocytopenie en overgevoeligheidsreacties.

## Conclusie en Vervolgstappen

**Besluit: In Wacht**

**Reden:**
Het TxGNN-model identificeerde geen herbestemmingskandidaten voor abciximab. Dit, gecombineerd met het gebrek aan huidige marketingautorisatie van het geneesmiddel in Nederland en aanzienlijke gegevensgaten (geen MOA-gegevens, geen veiligheidsconsideraties, geen regelgevingsdossiers in het bewijspakket), biedt onvoldoende grondslag om dit geneesmiddel in enig evaluatiepad voor herbestemming verder te brengen.

**Ter voortgang zou het volgende nodig zijn:**
- Hernieuwde evaluatie van het TxGNN-model met bijgewerkte kennisgraafgegevens om te bepalen of voorspellingen naar voren komen
- Opvraging van werkingsmechanisme-gegevens uit de DrugBank API (geïdentificeerd als gegevensgat DG002)
- Verduidelijking van wereldwijde regelgevingsstatus en commerciële beschikbaarheid
- Evaluatie of een biologisch-specifiek herbestemmingsmodel verschillende resultaten zou opleveren
- Indien een kandidaat-indicatie uiteindelijk wordt geïdentificeerd: opvraging van SmPC-veiligheidsconsideraties (geïdentificeerd als blokkerend gegevensgat DG001)

---

*Dit rapport werd gegenereerd op 2026-04-03 op basis van Bewijspakket v4. Resultaten zijn alleen bestemd voor onderzoeksdoeleinden en vormen geen medisch advies. Alle kandidaten voor geneesmiddelherbestemming vereisen klinische validatie vóór toepassing.*

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

