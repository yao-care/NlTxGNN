---
layout: default
title: Ritonavir
parent: Alleen modelvoorspelling (L5)
nav_order: 294
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Ritonavir: voorspelde nieuwe indicatie Felien verworven immunodeficiëntiesyndroom (kattenaids) (bewijsniveau L5). Oorspronkelijke indicatie: Hiv-infectie/aids en chronische hepatitis C-infectie"
---

# Ritonavir
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **3** 
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

# Ritonavir: Van hiv/aids naar felien verworven immunodeficiëntiesyndroom

## Samenvatting in één zin

Ritonavir is een proteaseremmer die oorspronkelijk wordt gebruikt voor de behandeling van hiv-infectie/aids en hepatitis C-infectie (volgens de kennisgraaf waarop het model is gebaseerd). Het TxGNN-model voorspelt dat het werkzaam kan zijn bij **felien verworven immunodeficiëntiesyndroom (kattenaids)**. Voor deze voorspelling zijn **geen klinische studies** en **geen publicaties** beschikbaar; het gaat om een puur computationele voorspelling.

---

## Snel overzicht

| Item | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Hiv-infectie/aids en chronische hepatitis C-infectie (afkomstig uit de kennisgraaf; de geregistreerde indicatietekst van de Nederlandse vergunning is niet beschikbaar) |
| Voorspelde nieuwe indicatie | Felien verworven immunodeficiëntiesyndroom (kattenaids) |
| TxGNN-voorspellingsscore | 99,92% |
| Bewijsniveau | L5 |
| Marktstatus in Nederland | Alleen doorgehaalde registraties (geen geldige vergunning) |
| Aantal vergunningen | 1 (doorgehaald) |
| Aanbevolen beslissing | Hold |

---

## Waarom is deze voorspelling aannemelijk?

Gegevens over het werkingsmechanisme zijn momenteel niet beschikbaar in de voor dit rapport samengestelde data. Bekend is dat ritonavir een hiv-proteaseremmer is (die ook CYP3A4 remt), waarvan de werkzaamheid bij hiv/aids is aangetoond.

Het feline immunodeficiëntievirus (FIV) is een lentivirus dat verwant is aan hiv. De protease ervan is structureel vergelijkbaar, dus een proteaseremmer als ritonavir is bij analogie denkbaar. De FIV-protease verschilt echter van de hiv-1-protease in substraatspecificiteit en gevoeligheid voor remmers, zodat werkzaamheid niet vanzelfsprekend is.

De hoge score (0,999) wordt waarschijnlijk vooral veroorzaakt door de sterke koppeling tussen ritonavir en hiv/aids in de kennisgraaf. Het is dus een modelvoorspelling zonder directe onderbouwing.

---

## Bewijs uit klinische studies

Momenteel zijn er geen gerelateerde klinische studies geregistreerd.

---

## Bewijs uit de literatuur

Momenteel is er geen gerelateerde literatuur beschikbaar voor de voorspelde indicatie kattenaids.

*Ter context:* voor de verwante indicatie **simian immunodeficiëntievirus (SIV)-infectie** (rang 2 in de voorspellingen) is wel preklinische literatuur gevonden, bijvoorbeeld een in-vitrostudie waarin SIV door ritonavir werd geremd (PMID [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/), 2003). Dit betreft echter een andere diersoort en een ander virus en vormt dus geen direct bewijs voor kattenaids.

---

## Informatie over de Nederlandse markt

| RVG-nummer | Productnaam | Toedieningsvorm | Goedgekeurde indicatie |
|---------|------|------|-----------|
| RVG 115127 | Ritonavir Sandoz 100 mg, filmomhulde tabletten (doorgehaald) | Niet beschikbaar | Niet beschikbaar |

---

## Veiligheidsoverwegingen

**Contra-indicaties volgens de kennisgraaf** (afgeleid uit relaties tussen geneesmiddel en ziekte, niet uit de bijsluitertekst): onder andere het lange-QT-syndroom (ook familiair), torsades de pointes, plotselinge hartstilstand, geleidingsstoornissen van het hart, atrioventriculair blok, cardiomyopathie, coronairlijden en myocardischemie; pancreatitis; leverziekte en levercirrose; galblaasaandoeningen; hyperglykemie, diabetes mellitus en diabetische ketoacidose; hypertriglyceridemie en familiaire gecombineerde hyperlipidemie; hyperbilirubinemie en het syndroom van Gilbert; jicht en hyperurikemie; kaliumdeficiëntie; chronische hepatitis B; hemofilie.

**Geneesmiddelinteracties:** in totaal zijn 100 interacties gevonden. Voorbeelden uit de beschikbare lijst:
- **Ernstig (Major):** loperamide, triamcinolon, budesonide
- **Matig (Moderate):** onder andere acarbose, hydrocortison, metformine, dexamethason, bupropion, aprepitant, clarithromycine, metronidazol, canagliflozine

Raadpleeg voor volledige veiligheidsinformatie (waarschuwingen en contra-indicaties) de SmPC (Samenvatting van de Productkenmerken) en de bijsluiter. De bijsluiterteksten van het CBG-MEB zijn niet in de gegevens opgenomen.

---

## Conclusie en vervolgstappen

**Beslissing: Hold**

**Onderbouwing:**
- De voorspelling berust uitsluitend op een model (bewijsniveau L5), zonder klinische studies of literatuur. De score lijkt vooral voort te komen uit de bekende hiv-indicatie van ritonavir.
- Kattenaids is een diergeneeskundige indicatie, buiten de humane geneesmiddelregistratie van het CBG-MEB. Bovendien is er in Nederland geen geldige vergunning voor ritonavir (alleen een doorgehaalde registratie).

**Om verder te gaan is nodig:**
- Gegevens over het werkingsmechanisme (onder andere uit DrugBank)
- Laboratoriumstudies naar de remming van FIV-protease door ritonavir
- Veiligheidsinformatie uit de SmPC/bijsluiter (waarschuwingen en contra-indicaties)
- Beoordeling van een veterinair registratiekader en van de veiligheid bij katten
- Een plan voor het beheersen van de omvangrijke interacties met andere geneesmiddelen

---

*Aanvullende opmerking over de andere voorspellingen:* de voorspelling voor **SIV-infectie** (bewijsniveau L4, "onderzoeksvraag") is vooral relevant als translationeel diermodel voor hiv, een reeds bestaande indicatie. De voorspelling voor de **neurologische ontwikkelingsstoornis met ataxie, afwezige spraak en verminderde corticale witte stof** (L5, Hold) heeft geen aanwijsbare mechanistische relatie met ritonavir en lijkt een artefact van de kennisgraaf.
## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

