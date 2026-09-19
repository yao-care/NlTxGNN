---
layout: default
title: Ramipril
parent: Alleen modelvoorspelling (L5)
nav_order: 109
evidence_level: L5
indication_count: 10
---

# Ramipril
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

# Ramipril: van Hypertensie naar Pulmonale Hypertensie met Onduidelijk Multifactorieel Mechanisme

## Samenvatting in één zin

Ramipril is een angiotensine-converterende enzym (ACE) remmer met goed gevestigde cardiovasculaire indicaties — waaronder hypertensie, hartfalen, management na myocardinfarct en nierprotectie — hoewel geen actieve CBG-MEB-marktvergunningen in de huidige dataset voor Nederland zijn geregistreerd.
Het TxGNN-model voorspelt dat het mogelijk effectief kan zijn voor **pulmonale hypertensie met onduidelijk multifactorieel mechanisme**, wat het hoogst gerangschikte hergebruikingssignaal vertegenwoordigt.
Echter, **geen klinische onderzoeken en geen publicaties** ondersteunen direct deze specifieke richting, waardoor dit op dit moment een alleen-model-voorspelling is.

---

## Snelle overzicht

| Item | Inhoud |
|------|--------|
| Originele indicatie | Geen CBG-MEB-vergunningsrecords beschikbaar (geneesmiddel niet geregistreerd volgens huidige dataset) |
| Voorspelde nieuwe indicatie | Pulmonale Hypertensie met Onduidelijk Multifactorieel Mechanisme |
| TxGNN-voorspellingsscore | 99,93% |
| Bewijsniveau | L5 |
| NL-marktStatus | Niet geregistreerd (volgens huidige CBG-MEB-records) |
| Aantal vergunningen | 0 |
| Aanbevolen besluit | Hold |

---

## Waarom is deze voorspelling redelijk?

Op dit moment zijn gedetailleerde gegevens over het werkingsmechanisme niet beschikbaar in dit bewijspakket. Op basis van bekende farmacologische informatie behoort Ramipril tot de stofklasse van ACE-remmers (ACEI). Het blokkeert de omzetting van angiotensine I naar angiotensine II binnen het renine-angiotensine-aldosteron-systeem (RAAS), waardoor systemische vaatweerstand, aldosteronafscheiding en — theoretisch — pulmonale vasculaire tonus afnemen. De werkzaamheid bij hypertensie en cardiovasculaire risicovermindering is goed aangetoond in grote oriëntatiepuntstudies (waaronder de HOPE-studie) en nierprotectie door de REIN-studie.

De theoretische basis voor de TxGNN-voorspelling berust op de gedeeltelijke overlap tussen RAAS-activering en pathofysiologie van pulmonale vaten. Angiotensine II bevordert pulmonale vasoconrictie, proliferatie van gladde spieren en endotheeldisfunctie, die allemaal bijdragen aan verhoogde pulmonale vaatweerstand. Door angiotensine II-activiteit te onderdrukken, zou Ramipril in principe één van de bijdragende pathways in multifactoriële pulmonale hypertensie kunnen verzwakken.

In de klinische praktijk is deze overlap echter onvoldoende om therapeutische werkzaamheid te stimuleren. Pulmonale hypertensie met onduidelijk multifactorieel mechanisme wordt beheerst door meerdere parallelle pathogene assen — waaronder endotheline-1 (ET-1), plaatjesafkomstige groeifactor (PDGF) en dysgereguleerde beenmorfogeenproteïne-receptortype II (BMPR2) signaaltransductie — die volledig buiten het bereik van RAAS-blokkade vallen. ACE-remming kan ook de systemische bloeddruk verlagen zonder evenredig de pulmonale vaatweerstand te verminderen, wat een risico van ongunstige compensatoire hemodynamica in deze patiëntenpopulatie introduceert. Dienovereenkomstig is de mechanistische rationale zwak, en geen klinisch signaal is geïdentificeerd ter ondersteuning van deze voorspelling.

---

## Klinisch onderzoeksbewijs

Momenteel geen gerelateerde klinische onderzoeken geregistreerd.

---

## Literatuurbewijs

Momenteel geen gerelateerde literatuur beschikbaar.

---

## Informatie Nederlandse markt

Geen CBG-MEB-marktvergunningen voor Ramipril zijn geregistreerd in de huidige dataset. Dit is waarschijnlijk een **data pipeline-hiaat** in plaats van een werkelijke afwezigheid op de Nederlandse markt — Ramipril is een veel gebruikt generiek ACE-remmermiddel dat overal in Europa beschikbaar is, en centraal of nationaal geautoriseerde producten zijn mogelijk nog niet opgenomen in dit bewijspakket.

Voordat enige regelgevingsactie wordt ondernomen, moet de huidige autorisatiestatus rechtstreeks worden geverifieerd via:
- Het **CBG-MEB openbare register** op [geneesmiddeleninformatiebank.nl](https://www.geneesmiddeleninformatiebank.nl)
- De **EMA-productdatabase** voor centraal geautoriseerde generica
- De relevante **SmPC (Samenvatting van de Productkenmerken)** voor goedgekeurde indicaties en veiligheidsgegevens

---

## Veiligheidsoverwegingen

Raadpleeg de SmPC (Samenvatting van de Productkenmerken) voor veiligheidsinformatie.

> **Opmerking:** Veiligheidsgegevens (belangrijke waarschuwingen, contra-indicaties en geneesmiddelinteracties) waren niet beschikbaar in dit bewijspakket. Voor een geneesmiddel met het profiel van Ramipril — een ACE-remmer met bekende klassieke effecten waaronder hyperkaliëmie, acuut nierfalen bij renovasculaire ziekten, angioneurotisch oedeem en teratogeniteit — is SmPC-controle **verplicht** voordat enige klinische of regelgevingsevaluatie wordt voortgezet.

---

## Conclusie en vervolgstappen

**Besluit: Hold**

**Rationale:**
Deze voorspelling wordt ingedeeld als L5 (alleen modelvoorspelling, geen ondersteunende klinische onderzoeken of publicaties). De mechanistische link tussen ACE-remming en multifactoriële pulmonale hypertensie is theoretisch aannemelijk maar farmacologisch onvoldoende — RAAS-blokkade richt zich op slechts een klein onderdeel van een complexe, multi-pathway-ziekte — en het risico van ongunstige systemische hypotensie bij PAH-patiënten is een gedocumenteerde veiligheidskwestie die verdere ontwikkelingsbetrokkenheid verder beperkt.

**Om voort te gaan is het volgende nodig:**

- **Regelgeving gegevenshipaat-resolutie**: Haal de huidige CBG-MEB-vergunningsrecords en SmPC voor Ramipril op om de NL-marktstatusstatus, goedgekeurde indicaties en formele veiligheidsgegevens te bevestigen
- **MOA-gegevens ophalen**: Query de DrugBank API (DB00178) om werkingsmechanismevelden en geneesmiddelinteractieprofiel in te vullen
- **Preclinisch bewijsonderzoek**: Identificeer of enig dier- of in vitro-onderzoek specifiek ACE-remming in multifactoriële PAH-modellen heeft onderzocht (onderscheiden van HPV-aangedreven of idiopathische PAH)
- **Comparatorcontext**: Beoordeel bestaande PAH-therapieën (endotheline-receptorantagonisten, PDE-5-remmers, prostacycline-analoga) om te beoordelen of RAAS-remming een ondersteunende rol in plaats van een primaire rol zou kunnen spelen
- **Veiligheidsmodellering**: Gezien het bekende klassieke risico van hemodynamische decompensatie in PAH, zou een gestructureerde voordeel-risicobeoordeling vereist zijn voordat enig verkennend klinisch onderzoek wordt ondernomen

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

