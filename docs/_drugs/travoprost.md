---
layout: default
title: Travoprost
parent: Alleen modelvoorspelling (L5)
nav_order: 120
evidence_level: L5
indication_count: 10
---

# Travoprost
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

# Travoprost: van Open-angle glaucoom naar Viscerale calcifylaxis

## Samenvatting in één zin

Travoprost is een agonist van prostaglandine-FP-receptoren die klinisch wordt gebruikt voor het verlagen van intraoculaire druk bij open-angle glaucoom en oculaire hypertensie.
Het TxGNN-model voorspelt dat het mogelijk effectief kan zijn voor **Viscerale calcifylaxis**,
waarbij momenteel **0 klinische trials** en **0 publicaties** deze richting ondersteunen.

---

## Korte samenvatting

| Item | Inhoud |
|------|--------|
| Oorspronkelijke indicatie | Open-angle glaucoom / Oculaire hypertensie (afgeleid van klinische trial-gegevens; geen CBG-MEB-handelstoestemming op bestand) |
| Voorspelde nieuwe indicatie | Viscerale calcifylaxis |
| TxGNN-voorspellingsscore | 99.9998% |
| Bewijsniveau | L5 |
| NL-marktpositie | Niet op de markt in Nederland |
| Aantal handelstoestemmingen | 0 |
| Aanbevolen besluit | Wachten |

---

## Waarom is deze voorspelling redelijk?

Op dit moment zijn gedetailleerde werkingsmechanisme-gegevens niet beschikbaar in het Evidence Pack. Op basis van bekende farmacologische informatie is travoprost een selectieve agonist van prostaglandine-FP-receptoren. De werkzaamheid ervan in het verlagen van intraoculaire druk bij open-angle glaucoom en oculaire hypertensie is goed aangetoond in meerdere klinische fase 3–4-onderzoeken. Het primaire mechanisme omvat verbeterde uveoschleraaluitvloeiing van humor aquosus via FP-receptorstimulatie, met een secundair vasodilatatorisch effect dat verantwoordelijk is voor de karakteristieke conjunctivale hyperemie die klinisch wordt waargenomen.

Viscerale calcifylaxis (calcifische uremische arteriolo-pathie) is een afzonderlijke pathologische entiteit die wordt gekenmerkt door mediale calcificatie en thrombotische occlusie van kleine cutane en viscerale vaten. Het komt het meest voor bij patiënten met eindstadium nierziekte en omvat dysgereguleerde calcium-fosfaat-homeostase, transdifferentiatie van vasculaire gladde spiercellen naar osteoblast-achtige cellen, en thrombotische microangiopathie. Geen van deze mechanismen zijn bekende aangrijpingspunten van het prostaglandine-FP-receptorpad.

De uitzonderlijk hoge TxGNN-score (>99,99%) weerspiegelt waarschijnlijk een artefact in de topologie van de kennisgraaf: Travoprost deelt brede 'vasculaire' en 'prostaglandine'-knooppunten van de graaf met calcifylaxis via tussenliggende graafverbindingen, in plaats van een direct mechanistisch of klinisch verband. De eigen onderbouwing van hergebruik in het Evidence Pack geeft aan dat deze voorspelling "kan voortvloeien uit voortplantingsbias bij gegeneraliseerde vasculaire knooppunten". Geen gepubliceerde literatuur of geregistreerde klinische trial ondersteunt momenteel deze richting van hergebruik.

---

## Klinische trials

Momenteel zijn geen gerelateerde klinische trials geregistreerd.

---

## Literatuurbewijzen

Momenteel is geen gerelateerde literatuur beschikbaar.

---

## Informatie over de Nederlandse markt

Travoprost beschikt momenteel over **geen handelstoestemming** van het CBG-MEB (College ter Beoordeling van Geneesmiddelen) in Nederland. Er is geen RVG-nummer toegewezen. Het geneesmiddel is daarom niet commercieel verkrijgbaar via standaard Nederlandse distributielijnen.

Voor regelgevingsverwijzing hebben travoprost-bevattende oftalmische oplossingen (bijv. Travatan®, Travatan Z®) handelstoestemmingen verkregen in andere EU-lidstaten via nationale procedures. De overeenkomstige SmPC (Samenvatting van de Productkenmerken) van die toestemmingen — met name de secties met waarschuwingen, contra-indicaties en speciale populaties — dient als primaire veiligheidsbron te worden geraadpleegd.

---

## Veiligheidsoverwegingen

Raadpleeg de SmPC (Samenvatting van de Productkenmerken) voor veiligheidsinformatie. Er zijn momenteel geen belangrijke waarschuwingen, contra-indicaties of interactiegegevens van geneesmiddelen beschikbaar in dit Evidence Pack.

---

## Conclusie en volgende stappen

**Besluit: Wachten**

**Onderbouwing:**
Er zijn geen klinische trial-gegevens, geen ondersteunende literatuur en geen gevestigde mechanistische onderbouwing die het FP-receptorpad van travoprost aan viscerale calcifylaxis koppelt. De hoge TxGNN-score kan het meest aannemelijk worden toegeschreven aan voortplantingsbias in de kennisgraaf via gedeelde vasculaire ontologieknooppunten in plaats van een werkelijk biologisch signaal.

**Om door te gaan, zou het volgende nodig zijn:**

- **Genereren van mechanistische hypothese**: Identificeer elk aannemelijk biologisch pad dat prostaglandine-FP-receptoractivering verbindt met vasculaire calcificatie of thrombotische microangiopathie (bijv. via TGF-β, Wnt/β-catenine, of inflammatie-gemedieerde calcificatiepaden).
- **Preclinisch bewijs**: In vitro- of diermodelgegevens die een effect van FP-receptoragonisme op vasculaire calcificatie of progressie van calcifylaxis-lesies aantonen vóór enige klinische overweging.
- **Opheldering van veiligheidsprofiel**: Verkrijg de volledige SmPC van een handelstoestemming van een EU-lidstaat om systeemblootstellingsrisico, contra-indicaties en relevante waarschuwingen te beoordelen — vooral gezien het feit dat patiënten met calcifylaxis doorgaans ernstige nierfunctiestoornissen hebben, wat de medicijnuitscheiding en verdraagzaamheid aanzienlijk kan beïnvloeden.
- **Status van CBG-MEB-handelstoestemming**: Bevestig of een EU-gecentraliseerde of procedure voor onderlinge erkenning is ingediend; zo niet, zou een de novo-toestemmingsprocedure nodig zijn vóór enig Nederlands klinisch gebruik.
- **Herbeoordeling van TxGNN-rangschikking**: Onderzoek of de voorspellingsscore aanhoudt na correctie voor bias in de graad van vasculaire knooppunten; een robuuste score na correctie zou escalatie naar L4 preclinisch onderzoek rechtvaardigen.

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

