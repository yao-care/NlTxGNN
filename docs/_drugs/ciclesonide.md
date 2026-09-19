---
layout: default
title: Ciclesonide
parent: Alleen modelvoorspelling (L5)
nav_order: 42
evidence_level: L5
indication_count: 6
---

# Ciclesonide
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **6** 
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

# Ciclesonide: van Astma naar Atopisch Eczeem

## Samenvatting in één zin

Ciclesonide is een ingeademde/intranasale corticosteroïde (ICS) bedoeld voor de behandeling van astma en allergische rhinitis; in het CBG-MEB-register werden geen Nederlandse handelsvergunningen gevonden.
Het TxGNN-model voorspelt dat het mogelijk effectief kan zijn voor **atopisch eczeem** met een voorspellingsscore van **99.96%**, maar dit wordt momenteel ondersteund door **0 klinische trials** en **0 publicaties** — een puur modelvoorspelling.
De mechanistische grondslag is twijfelachtig: de ingeademde/intranasale toedieningsweg van ciclesonide is fundamenteel onverenigbaar met de topicale vereisten voor de behandeling van een huidaandoening, wat suggereert dat dit een vals-positief kan zijn aangestuurd door de generalisatie van de glucocorticoïde-geneesmiddelklasse door het model.

---

## Snel overzicht

| Item | Inhoud |
|------|--------|
| Oorspronkelijke indicatie | Astma en allergische rhinitis (ingeademde/intranasale corticosteroïde; geen goedgekeurde indicatietekst beschikbaar uit NL-register) |
| Voorspelde nieuwe indicatie | Atopisch eczeem |
| TxGNN-voorspellingsscore | 99.96% |
| Bewijsniveau | L5 |
| NL-marketstatus | Niet geregistreerd (niet op de markt) |
| Aantal handelsvergunningen | 0 |
| Aanbevolen beslissing | Voorbehoud |

---

## Waarom is deze voorspelling redelijk?

Momenteel zijn gedetailleerde werkingsmechanisme-gegevens niet beschikbaar in dit Evidence Pack. Op basis van bekende farmacologische informatie is ciclesonide een prodrug ingeademde/intranasale corticosteroïde die lokaal in de luchtwegen wordt omgezet in haar actieve metaboliet des-ciclesonide. Het werkt door binding aan de glucocorticoïde-receptor en onderdrukking van luchtwegontsteking — vermindering van eosinofielenactiviteit, mestceldegranulatie en pro-inflammatoire cytokines waaronder IL-4, IL-5 en IL-13.

De voorspelling van het TxGNN-model stamt waarschijnlijk uit een gedeeld biologisch pad: atopisch eczeem (atopische dermatitis, ICD-10: L20) is een ontstekingsziekte van de huid waarin corticosteroïden de hoeksteen van de behandeling vormen. Op klasseniveau is de logica oppervlakkig coherent — glucocorticoïden onderdrukken ontsteking en atopisch eczeem is een ontstekingssituatie aangestuurd door Th2-cytokine-dysregulatie, precies hetzelfde pad dat ciclesonide in de luchtwegen aanvalt.

Dit is echter vrijwel zeker een modelartefact in plaats van een echt signaal voor herpositionering. Ciclesonide is specifiek ontworpen voor minimale systemische biologische beschikbaarheid en heeft geen topicale huidformulering. De toedieningsweg (ingeademd of intranasaal) kan de huid niet bereiken waar de ziekte zich voordoet. Bovendien vervullen goed gevestigde topicale corticosteroïden (betamethason, triamcinolone, mometason) al deze therapeutische rol met robuuste bewijzen. De combinatie van nul klinisch bewijs, onverenigbaarheid van toedieningswegen en geen onvervulde medische behoefte maakt deze voorspelling duidelijk een **voorbehoud**.

---

## Bewijs uit klinische trials

Momenteel zijn er geen gerelateerde klinische trials geregistreerd.

---

## Bewijs uit literatuur

Momenteel is er geen gerelateerde literatuur beschikbaar.

---

## Informatie over de Nederlandse markt

Geen handelsvergunningen voor ciclesonide werden gevonden in het Nederlands CBG-MEB-register voor deze gegevensnijding (2026-05-01).

> **Opmerking voor reviewers:** Ciclesonide (merknaam Alvesco®) bezit een gecentraliseerde EMA-handelsvergunning die geldig is in de EU/EER. De huidige beschikbaarheid en SmPC-status in Nederland moeten rechtstreeks worden geverifieerd via de [CBG-MEB-productdatabase](https://www.cbg-meb.nl/) of de [EMA-productpagina](https://www.ema.europa.eu/en/medicines/human/EPAR/alvesco). Het ontbreken van een RVG-nummer in deze dataset kan een gegevensverzamelingsgat weerspiegelen in plaats van een ware afwezigheid van handelsvergunning.

---

## Veiligheidsoverkwegingen

Er waren geen veiligheidsgegevens (belangrijke waarschuwingen, contra-indicaties of geneesmiddelinteracties) beschikbaar in dit Evidence Pack.

Raadpleeg de SmPC (Samenvatting van de Productkenmerken) voor volledige veiligheidsinformatie, inclusief effecten van corticosteroïde-klasse zoals HPA-as-onderdrukking, groeivertraging bij kinderen en risico op systemische absorptie bij hoge doses.

---

## Conclusie en vervolgstappen

**Beslissing: Voorbehoud**

**Grondslag:**
Ondanks een hoge TxGNN-voorspellingsscore (99.96%) is er geen klinisch of preklinisch bewijs dat ciclesonide ondersteunt voor atopisch eczeem, en — meer kritiek nog — is de ingeademde/intranasale toedieningsweg van ciclesonide mechanisch onverenigbaar met de behandeling van een huidaandoening. Deze voorspelling wordt het best geïnterpreteerd als een vals-positief model voortvloeiend uit de brede associatie tussen de glucocorticoïde-geneesmiddelklasse en ontstekingsziekten.

**Om verder te gaan, zou het volgende nodig zijn:**

- **Beoordeling van routehaalbaarheid**: Zou een topicale dermatologische formulering van ciclesonide kunnen worden ontwikkeld, en zou deze voordelen bieden ten opzichte van gevestigde topicale corticosteroïden?
- **Oplossing van MOA-gat**: Verkrijg volledige DrugBank-gegevens (momenteel DG002 — Hoge ernst) om het receptorbindingsprofiel formeel te documenteren en de redenering op klasseniveau te bevestigen.
- **Verificatie van NL/EMA-registratie**: Bevestig de huidige beschikbaarheid op de Nederlandse markt van Alvesco® via directe CBG-MEB-query, omdat de bevinding van nul handelsvergunningen een gegevensgat kan weerspiegelen.
- **Differentiatieanalyse**: Indien de formuleringhaalbaarheid is bevestigd, is een vergelijkende effectiviteits-/veiligheidsbeoordeling tegen bestaande topicale corticosteroïden vereist voordat verdere investeringen worden gedaan.

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

