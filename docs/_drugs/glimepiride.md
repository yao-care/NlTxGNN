---
layout: default
title: Glimepiride
parent: Alleen modelvoorspelling (L5)
nav_order: 74
evidence_level: L5
indication_count: 9
---

# Glimepiride
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **9** 
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

# Glimepiride: van type 2 diabetes mellitus naar focaal stijf-ledematensyndroom

## Samenvatting in één zin

Glimepiride is een antidiabetica-middel van de derde generatie sulfonylurea, vastgesteld voor de behandeling van type 2 diabetes mellitus bij volwassenen.
Het TxGNN-model voorspelt dat het effectief kan zijn voor **focaal stijf-ledematensyndroom** (voorspellingsscore: 99.75%), maar er bestaan momenteel **geen klinische onderzoeken** en **geen ondersteunende publicaties** voor deze indicatie.
De voorspelling is uitsluitend modelgestuurd (Bewijsniveau L5), en onafhankelijke preklinische en klinische verificatie zijn vereist voordat verdere consideratie kan plaatsvinden.

---

## Snel overzicht

| Onderdeel | Inhoud |
|-----------|--------|
| Oorspronkelijke indicatie | Type 2 diabetes mellitus (geen CBG-MEB-handelstoelating voor Nederland geregistreerd) |
| Voorspelde nieuwe indicatie | Focaal stijf-ledematensyndroom |
| TxGNN-voorspellingsscore | 99.75% |
| Bewijsniveau | L5 |
| Marktpositie NL | Niet geregistreerd |
| Aantal autorisaties | 0 |
| Aanbevolen beslissing | In afwachting |

---

## Waarom is deze voorspelling redelijk?

Momenteel zijn gedetailleerde gegevens over het werkingsmechanisme niet beschikbaar in het Evidence Pack. Op basis van gevestigde farmacologische kennis behoort glimepiride tot de derde generatie sulfonylurea. De glucoseverlagende werkzaamheid ervan wordt bereikt door binding aan de SUR1-subunit van ATP-gevoelige kaliumkanalen (K_ATP) op β-cellen van de pancreas, waardoor het kanaal sluit, membraandepolarisatie optreedt en daaropvolgende insulinesecretie. Het vertoont ook zwakke partieel-agonistische activiteit op PPAR-γ, wat bescheiden bijdraagt aan verbetering van de insulinegevoeligheid.

Focaal stijf-ledematensyndroom is een zeldzame auto-immuun neurologische aandoening waarbij anti-GAD65-antilichamen selectief GABAerge remmende interneuronen in het ruggenmerg beschadigen, wat leidt tot focale onwillekeurige spierstijfheid. De mechanistische verbinding met glimepiride is indirect: SUR1 (ABCC8) — de sulfonylurea-receptor — komt niet alleen tot expressie in β-cellen van de pancreas, maar ook in centrale neuronen, waaronder GABAerge interneuronen. In theorie zou modulering van neuronale K_ATP-kanaalactiviteit membraanprikkelbaarheid en de stroomafwaarts GABA-gemedieerde remming kunnen beïnvloeden, waardoor mogelijk de hyperprikkelbaarheid in het stijf-ledematensyndroom wordt tegengegaan.

Deze verbinding is echter zeer speculatief. Er zijn geen in vitro- of in vivo-gegevens die het gebruik van sulfonylurea's bij GABAerge of auto-immuun neurologische aandoeningen ondersteunen. De hoge TxGNN-score weerspiegelt waarschijnlijk een structureel kennisgrafiek-artefact: GAD65 komt tot expressie in zowel pancreasislets (waar het deelneemt aan GABA-synthese voor paracriene signalering) als in ruggenmerg-remmende neuronen, wat een gedeeld grafiekpunt creëert dat co-associatiescores verhoogt. Dit is een erkend fout-positief risicopatroon in geneesmiddelherbestemming via grafiek neurale netwerken, en dient voorzichtig te worden geïnterpreteerd.

---

## Klinisch onderzoeksbewijs

Momenteel zijn geen gerelateerde klinische onderzoeken geregistreerd.

---

## Literatuurbewijs

Momenteel is geen gerelateerde literatuur beschikbaar.

---

## Informatie over de Nederlandse markt

Glimepiride heeft momenteel **geen handelstoelating** bij de CBG-MEB (College ter Beoordeling van Geneesmiddelen) in Nederland. Er zijn geen RVG-nummers geregistreerd. Elk klinisch gebruik in Nederland zou off-label of op named-patient-basis moeten plaatsvinden, onder voorbehoud van toepasselijke Nederlandse en EMA-regelgeving.

---

## Veiligheidsverwachtingen

Raadpleeg de SmPC (Samenvatting van de Productkenmerken) voor volledige veiligheidsinformatie, inclusief belangrijke waarschuwingen, contra-indicaties en gegevens over geneesmiddel-geneesmiddelinteracties.

---

## Conclusie en vervolgstappen

**Beslissing: In afwachting**

**Motivering:**
Ondanks een hoge TxGNN-voorspellingsscore (99.75%) wordt deze score waarschijnlijk aangestuurd door kennisgrafiek-topologie — specifiek de dubbele expressie van GAD65 in pancreas- en neuronaal weefsel — in plaats van echte biologische plausibiliteit. Zonder ondersteunende klinische onderzoeken, zonder relevante publicaties en met een puur speculatieve mechanistische verbinding, is er onvoldoende basis om deze kandidaat op dit moment in de Nederlandse gezondheidszorgcontext verder te brengen.

**Om voort te gaan, is het volgende nodig:**
- Preklinische in vitro- en/of in vivo-gegevens die aantonen dat K_ATP-kanaalmodulatie van de sulfonylureaklasse meetbare effecten op de prikkelbaarheid van ruggenmerg GABAerge interneuronen oplevert
- Deskundigenonderzoek door een neurofarmacolog en een neuroloog gespecialiseerd in auto-immuun bewegingsstoornissen om echte biologische plausibiliteit te beoordelen
- Formeel onderzoek naar of de TxGNN-voorspelling voortkomt uit een structureel GAD65 kennisgrafiek-artefact (identificatie van fout-positieven)
- Volledige opvraging en beoordeling van de SmPC voor glimepiride om het veiligheidsprofiel vast te stellen, inclusief belangrijke waarschuwingen, contra-indicaties en belangrijke geneesmiddel-geneesmiddelinteracties relevant voor eventueel toekomstig onderzoeksontwerp
- Overleg met regelgeving (CBG-MEB) over het ontbreken van NL-handelstoelating en mogelijke opties voor named-patient of compassioneel gebruik, mocht preklinisch bewijs naar voren komen

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

