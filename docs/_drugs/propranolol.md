---
layout: default
title: Propranolol
parent: Alleen modelvoorspelling (L5)
nav_order: 108
evidence_level: L5
indication_count: 6
---

# Propranolol
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

# Propranolol: Van cardiovasculaire aandoeningen naar distale myopathie, Tateyama-type

## Samenvatting in één zin

Propranolol is een klassieke niet-selectieve bètaadrenergische receptorblokker met een lang erkende geschiedenis in cardiovasculaire geneeskunde, inclusief hypertensie, aritmieën en hypertrofische obstructieve cardiomyopathie (HOCM).
Het TxGNN-model voorspelt dat het effectief kan zijn voor **distale myopathie, Tateyama-type** met een voorspellingsscore van **99.40%**,
maar **geen klinische onderzoeken** en **geen gepubliceerde literatuur** ondersteunen momenteel deze herpositioneringsrichting — het signaal wordt beoordeeld als een artefact van de kennisgraaf.

---

## Snel overzicht

| Item | Inhoud |
|------|--------|
| Oorspronkelijke indicatie | Geen NL-marktautorisatie in dossier; Propranolol is een goed gevestigde niet-selectieve bètablokker (cardiovasculair: hypertensie, aritmie, HOCM) |
| Voorspelde nieuwe indicatie | Distale myopathie, Tateyama-type |
| TxGNN-voorspellingsscore | 99.40% |
| Bewijsniveau | L5 |
| NL-marktstatuts | Niet geregistreerd (CBG-MEB: 0 autorisaties in dossier) |
| Aantal autorisaties | 0 |
| Aanbevolen besluit | Afwachten |

---

## Waarom is deze voorspelling redelijk?

Momenteel zijn gedetailleerde gegevens over het werkingsmechanisme niet beschikbaar in deze Evidence Pack. Op basis van gevestigde pharmacologische kennis is propranolol een niet-selectieve β-adrenergische receptorblokker die β1-receptoren (hart, nier) en β2-receptoren (bronchiën, perifeer vaatbed) competitief antagoniseert. De belangrijkste cardiovasculaire effecten zijn verlaging van hartslag, myocardiale contractiliteit, hartminuutvolume en renineverscheiding — waardoor het effectief is bij hypertensie, angina, aritmieën en HOCM.

Distale myopathie, Tateyama-type, is een zeldzame erfelijke skeletspieraandoening veroorzaakt door pathogene varianten in het *DYSF*-gen, dat dysferlin codeert — een eiwit essentieel voor calciumafhankelijke membraanreparatie in skeletspiezvezels. De onderliggende pathofysiologie (gestoorde sarcolemmale reparatie na mechanische stress) heeft **geen gevestigde biologische link** naar β-adrenergische signalering of receptorblokking. Er is geen gepubliceerde preklinische of klinische hypothese die propranolols werkingsmechanisme met dysferlinopathie verbindt.

De hoge TxGNN-voorspellingsscore (99.40%) wordt daarom het meest aannemelijk verklaard door een **artefact van kennisgraaf-transitiviteit**: de graaf verbindt "myopathie"-ziekteknopen met "cardiomyopathie"-knopen (via gedeelde spier-ziekte-ontologie), die zelf sterk zijn verbonden met beta-blokkerknopen door goed gedocumenteerde HOCM-bewijs. Dit indirecte pad genereert een hoge score zonder een direct biologisch mechanisme weer te geven. Deze voorspelling vereist validatie door een biologisch expert voordat verdere ontwikkelingsstappen worden overwogen.

---

## Bewijs van klinische onderzoeken

Momenteel geen gerelateerde klinische onderzoeken geregistreerd.

---

## Literatuurbewijs

Momenteel geen gerelateerde literatuur beschikbaar.

---

## Informatie over de Nederlandse markt

Volgens de huidige CBG-MEB-databasequery heeft propranolol geen geregistreerde marktautorisatieprodukten in dossier in Nederland (0 RVG-nummers, 0 licenties). Dit is onverwacht voor een molecuul met zo'n breed internationaal gebruik en rechtvaardigt verificatie rechtstreeks tegen het [online CBG-MEB-productregister](https://www.cbg-meb.nl/). Het is mogelijk dat beschikbare producten onder combinatienamen in de handel zijn of dat de gegevenspijplijn niet alle invoeren heeft vastgelegd.

*(Er kan geen RVG-autorisatietabel worden gegenereerd — geen gelicentieerde producten in de huidige gegevens)*

---

## Veiligheidsoverwegingen

Raadpleeg de SmPC (Summary of Product Characteristics / Samenvatting van de Productkenmerken) voor veiligheidsinformatie.

> Er waren geen belangrijke waarschuwingen, contra-indicaties of geneesmiddelinteractiegegevens beschikbaar in deze Evidence Pack. De SmPC van CBG-MEB moet worden geraadpleegd voordat klinisch of onderzoeksgebruik plaatsvindt.

---

## Conclusie en volgende stappen

**Besluit: Afwachten**

**Motivering:**
Ondanks een hoge TxGNN-voorspellingsscore (99.40%) identificeert de mechanistische analyse dit als een artefact van kennisgraaf-transitiviteit — er is geen gevestigde biologische verbinding tussen β-adrenergische receptorblokking en DYSF-gerelateerde skeletmyopathie. Met nul ondersteunende klinische onderzoeken en nul gepubliceerde literatuur is het bewijsniveau L5 (alleen modelvoorspelling), en kan op dit moment geen uitvoerbaar ontwikkelingstraject worden gedefinieerd.

**Om door te gaan, is het volgende nodig:**
- Preklinische onderzoeken die bepalen of β-adrenergische signalering enige rol speelt in dysferlin-deficiënte spierpatofysiologie (bijv. in *dysf*-null-muismodellen)
- Onafhankelijke audit van het graafpad van de TxGNN-kennisgraaf om de transitiviteitsartefacthypothese te bevestigen of uit te sluiten
- Ophalen van het werkingsmechanisme van propranolol van de DrugBank API (gegevensgat DG002) om formele plausibiliteitsscoring in te schakelen
- Verificatie van NL-marktstatuts via directe CBG-MEB-registerquery (mogelijk gegevenspijplijnsgat)
- Download en parsing van de SmPC (gegevensgat DG001) om het veiligheidsprofiel te voltooien voordat enige S1-veiligheidsevaluatie plaatsvindt

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

