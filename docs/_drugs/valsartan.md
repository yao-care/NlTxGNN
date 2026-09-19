---
layout: default
title: Valsartan
parent: Matig bewijs (L3-L4)
nav_order: 123
evidence_level: L4
indication_count: 7
---

# Valsartan
{: .fs-9 }

Bewijsniveau: **L4** | Voorspelde indicaties: **7** 
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

# Valsartan: Van Hypertensie naar Maligne Renovasculaire Hypertensie

## Samenvatting in één zin

Valsartan is een angiotensine II type 1 receptorblokker (ARB) gevestigd voor hypertensie- en hartfalenbehandeling, hoewel zijn Nederlandse marktgoedkeuringgegevens niet beschikbaar zijn in de huidige dataset.
Het TxGNN-model voorspelt dat het mogelijk effectief kan zijn voor **Maligne Renovasculaire Hypertensie**, met **0 klinische onderzoeken** en **1 publicatie** die deze richting momenteel ondersteunen.
De voorspelling is mechanistisch overtuigend — RAAS-overactivering is de kernfactor van deze aandoening — maar menselijk bewijs blijft afwezig.

---

## Snel Overzicht

| Item | Inhoud |
|------|--------|
| Originele Indicatie | Niet beschikbaar in huidge NL regelgeving dataset (Valsartan is een goed gevestigde ARB voor hypertensie en hartfalen) |
| Voorspelde Nieuwe Indicatie | Maligne Renovasculaire Hypertensie |
| TxGNN Voorspellingsscore | 99.97% |
| Bewijsniveau | L4 |
| NL Markt Status | Niet geregistreerd (CBG-MEB dataset retourneerde 0 goedkeuringen) |
| Aantal Goedkeuringen | 0 |
| Aanbevolen Besluit | Wachten |

---

## Waarom is Deze Voorspelling Redelijk?

Momenteel zijn gedetailleerde werkingsmechanisme-gegevens niet beschikbaar in het Bewijspakket. Op basis van wijdverbreide farmacologische kennis is Valsartan een angiotensine II type 1 (AT1) receptorblokker. Het bindt selectief aan de AT1-receptor en blokkeert daardoor de downstreameffecten van angiotensine II — inclusief vasoconstrictie, aldosteronsecretie, en renine-gedreven natriumretentie. Deze inhibitie van het renine-angiotensine-aldosteroonsysteem (RAAS) vermindert de vasculaire weerstand en bloeddruk, en verzwakt orgaanschade veroorzaakt door aanhoudende RAAS-hyperactivering.

Maligne renovasculaire hypertensie wordt gedefinieerd door renale arteriële stenose die een gevaarlijke positieve feedbacklus veroorzaakt: verminderde renale perfusie stimuleert overmatige renineafgifte → angiotensine II-piek → ernstige renale vasoconstrictie → verergering van ischemie. RAAS-hyperactivering is het centrale pathofysiologische mechanisme van deze aandoening. AT1-receptorblokking door Valsartan onderbreekt rechtstreeks deze cascade, wat uitzonderlijk sterke biologische aannemelijkheid voor de TxGNN-voorspelling oplevert — het werkingsmechanisme van het geneesmiddel wijst precies op het kernmechanisme van de ziekte.

Cruciaal is dat een preklinisch onderzoek uit 2001 in *Circulation* (Hilgers et al., PMID 11560862) aantoonde dat AT1-receptorblokking letale maligne hypertensie kan voorkomen in een diermodel, zelfs zonder een significant bloeddrukverlagend effect, wat duidt op een direct anti-inflammatoir en nierbeschermend mechanisme op het niveau van de niervasculatuur. Dit suggereert dat het voordeel van Valsartan in deze context zich verder uitstrekken kan dan eenvoudige bloeddrukcontrole, wat de voorspelling van het TxGNN-model met hoog vertrouwen verder ondersteunt. Echter, de afwezigheid van menselijke onderzoeksgegevens beperkt het bewijs tot het preklinische niveau (L4).

---

## Klinisch Onderzoeksbewijs

Momenteel geen gerelateerde klinische onderzoeken geregistreerd.

---

## Literatuurbewijs

| PMID | Jaar | Type | Tijdschrift | Belangrijkste Bevindingen |
|------|------|------|-------------|--------------------------|
| [11560862](https://pubmed.ncbi.nlm.nih.gov/11560862/) | 2001 | Dieronderzoek (Preklinisch) | Circulation | AT1-receptorblokking voorkomt letale maligne hypertensie in een rodent-model; het beschermende effect is onafhankelijk van bloeddrukdaling en is gekoppeld aan onderdrukking van nierinflamatie en niervascularaire schade |

---

## Nederland Marktinformatie

Geen marktgoedkeuringen voor Valsartan (als zelfstandig product) zijn geregistreerd in de CBG-MEB dataset voor Nederland in de huidge gegevensextractie. Opmerking: Valsartan is in Nederland beschikbaar als onderdeel van het combinatieproduct Sacubitril/Valsartan (Entresto®), dat centrale EMA-goedkeuring heeft voor hartfalen met verminderde ejectiefractie. Zelfstandige Valsartan-generieke geneesmiddelen werden in 2018–2019 teruggeroepen vanwege NDMA-besmetting; huidge beschikbaarheid moet rechtstreeks tegen het CBG-MEB-register worden geverifieerd.

---

## Veiligheidsoverwegingen

Raadpleeg alstublieft de SmPC (Summary of Product Characteristics / Samenvatting van de Productkenmerken) voor volledige veiligheidsinformatie. Geen gegevens over sleutelwaarschuwingen, contra-indicaties of geneesmiddelinteracties waren beschikbaar in het huidge Bewijspakket.

---

## Conclusie en Volgende Stappen

**Besluit: Wachten**

**Grondslag:**
De mechanistische basis voor Valsartan bij maligne renovasculaire hypertensie is sterk — RAAS-hyperactivering is het kernmechanisme van deze ziekte en AT1-blokking richt zich er rechtstreeks op — maar het enige beschikbare bewijs is slechts één preklinisch dieronderzoek (L4), zonder geregistreerde menselijke klinische onderzoeken en zonder klinische observatiegegevens. Dit bereikt niet de drempel voor een herbestemmingsaanbeveling in de Nederlandse gezondheidszorgcontext.

**Om door te gaan is het volgende nodig:**

- **Regelgevingsverificatie**: Bevestig huidig NL/EMA-marktsstatus van zelfstandig Valsartan via het CBG-MEB-register, inclusief eventueel heropgestarte generieke goedkeuringen na de NDMA-terugroep
- **MOA-gegevens**: Haal volledige DrugBank farmacologie-invoer op (DB00177) om de werkingsmechanisme-documentatie te formaliseren
- **Veiligheidsgegevens**: Download en parse de SmPC van het EMA of CBG-MEB voor sleutelwaarschuwingen, contra-indicaties, en DDI-profiel
- **Klinische bewijszoeking**: Voer doelgerichte systematische zoektocht uit naar menselijke casusseries, registergegevens, of observatiestudies over ARB-gebruik bij maligne renovasculaire hypertensie
- **Nefrologische deskundige raadpleging**: Betrek een nefroloog of klinisch farmacoloog verbonden aan CBG-MEB om te beoordelen of bestaande hypertensie-/nierbeschermingsindicaties dit gebruik al omvatten onder huidge Nederlandse voorschrijfrichtlijnen
- **Bewijsupgrade-traject**: Ontwerp een haalbaarheidsonderzoek voor een prospectief register of Phase 2 pilotstudie in Nederland als de bovenstaande stappen onvervulde behoefte en aanvaardbare veiligheidsmarges bevestigen

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

