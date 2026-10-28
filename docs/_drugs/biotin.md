---
layout: default
title: Biotin
parent: Alleen modelvoorspelling (L5)
nav_order: 58
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Biotin: voorspelde nieuwe indicatie Dyspepsie (bewijsniveau L5). Oorspronkelijke indicatie: Voedingsgerelateerd biotinetekort"
monitor_inn: "biotin"
predicted_indications: ["dyspepsia", "gastroparesis (disease)"]
---

# Biotin
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **2** 
{: .fs-6 .fw-300 }

---

## Inhoudsopgave
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmaceutisch beoordelingsrapport

</div>

## Biotine: Van voedingsgerelateerd biotinetekort naar dyspepsie
{: .text-alpha }

## Samenvatting in één zin

Biotine (vitamine B7) wordt van oudsher gebruikt bij een voedingsgerelateerd biotinetekort. Het TxGNN-model voorspelt dat het mogelijk werkzaam is bij **dyspepsie**, maar er zijn **geen geregistreerde klinische studies** en **geen literatuur die deze richting direct onderbouwt**; de voorspelling berust vooralsnog uitsluitend op het model.

---

## Snel overzicht

| Item | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Voedingsgerelateerd biotinetekort |
| Voorspelde nieuwe indicatie | Dyspepsie |
| TxGNN-voorspellingsscore | 0,9943 |
| Bewijsniveau | L5 |
| Marktstatus in Nederland | In de handel (geldige vergunningen: 1 van 1) |
| Aantal vergunningen | 1 (geldig: 1) |
| Aanbevolen besluit | Hold |

---

## Waarom is deze voorspelling aannemelijk?

Er zijn momenteel geen gedetailleerde gegevens over het werkingsmechanisme beschikbaar. Bekend is dat biotine een co-factor is voor carboxylasen die betrokken zijn bij het vetzuur-, glucose- en aminozuurmetabolisme. Het werd oorspronkelijk gebruikt bij biotinetekort.

Een tekort aan biotine kan maag-darmklachten geven, zoals misselijkheid en verminderde eetlust. Dat biedt slechts een zwakke, indirecte onderbouwing voor dyspepsie, en alleen wanneer er sprake is van een tekort. Een direct mechanistisch verband is niet vastgesteld. De hoge modelscore (0,9943) is een computationele voorspelling en wordt niet ondersteund door klinische gegevens.

Voor de tweede voorspelde indicatie, **gastroparese**, zijn evenmin studies of literatuur gevonden. Een mogelijke rol van biotine in het glucosemetabolisme bij diabetische gastroparese is speculatief.

---

## Klinisch studiebewijs

Momenteel zijn er geen gerelateerde klinische studies geregistreerd.

---

## Literatuurbewijs

De gevonden publicaties zijn allemaal van lage bewijskracht (casuïstiek of observationeel onderzoek) en onderzoeken biotine niet als behandeling van dyspepsie.

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|-----|------|------|---------|
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Casuïstiek | The Journal of Dermatology | Biotinetekort bij een zuigeling van 5 maanden die uitsluitend aminozuurvoeding kreeg en als neonaat met dyspepsie was gediagnosticeerd; typische huidafwijkingen en lage biotinespiegels in serum en urine |
| [25110039](https://pubmed.ncbi.nlm.nih.gov/25110039/) | 2014 | Observationeel | International Journal of Molecular Medicine | Endocriene cellen in het maagantrum bij prikkelbaredarmsyndroom; biotine niet als behandeling onderzocht |
| [24891930](https://pubmed.ncbi.nlm.nih.gov/24891930/) | 2014 | Observationeel | World Journal of Gastrointestinal Endoscopy | Endocriene cellen in de oxyntische maagmucosa bij prikkelbaredarmsyndroom; biotine niet als behandeling onderzocht |
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Klinische observatie | Eksperimental'naia i klinicheskaia gastroenterologiia | Supplement met prebiotica en vitamines (waaronder biotine) bij darmmicrobiotastoornissen bij longpatiënten na antibiotica; indirect verband |
| [11304845](https://pubmed.ncbi.nlm.nih.gov/11304845/) | 2001 | Observationeel | Journal of Clinical Pathology | IL-10 bij gastritis door *H. pylori*; niet relevant voor biotine |
| [10354275](https://pubmed.ncbi.nlm.nih.gov/10354275/) | 1999 | Observationeel | Kidney International | T-cellen in de dunne darm bij IgA-nefropathie; niet relevant voor biotine |

---

## Informatie over de Nederlandse markt

| RVG-nummer | Productnaam | Toedieningsvorm | Goedgekeurde indicatie |
|---------|------|------|-----------|
| RVG 117795//15333 (doorgehaald) | Cernevit, poeder voor oplossing voor injectie of voor intraveneuze infusie | Niet vermeld | Niet vermeld |

---

## Veiligheidsoverwegingen

Voor biotine zijn in de voor dit rapport samengestelde gegevens geen waarschuwingen, contra-indicaties of geneesmiddelinteracties uit de bijsluitertekst (SmPC) beschikbaar. Raadpleeg de SmPC voor veiligheidsinformatie.

Aanvullend noemt de kennisgraaf van TxGNN (afgeleid uit modelrelaties, niet uit officiële productteksten) mogelijke aandoeningen waarbij voorzichtigheid geboden kan zijn, waaronder:

- Nier- en calciumgerelateerde aandoeningen: nierziekte, nefrolithiasis, nefrocalcinose, acute urinezuurnefropathie, hypercalciëmie
- Bijschildklier- en botaandoeningen: hyperparathyreoïdie, osteïtis fibrosa, lytische botmetastasen
- Overige: sarcoïdose, fosfaatstofwisselingsstoornis, pyoureter, obstipatie

Deze signalen zijn niet geverifieerd aan de hand van de officiële productinformatie en moeten met de nodige terughoudendheid worden geïnterpreteerd.

---

## Conclusie en vervolgstappen

**Besluit: Hold**

**Onderbouwing:**
Er zijn geen klinische studies en geen direct relevante literatuur voor biotine bij dyspepsie (bewijsniveau L5). De voorspelling steunt alleen op het TxGNN-model (deep learning). Bovendien is het product in Nederland op de markt, met 1 geldige vergunning van de 1 geregistreerde, en ontbreken de veiligheidsgegevens uit de officiële productinformatie.

**Om verder te gaan is nodig:**
- Veiligheidsinformatie uit de SmPC en bijsluiter (CBG-MEB) ophalen en beoordelen; dit is een blokkerende ontbrekende gegevensbron
- Gegevens over het werkingsmechanisme aanvullen (bijvoorbeeld via DrugBank)
- Systematisch literatuuronderzoek naar biotine bij dyspepsie en gastroparese, en zo nodig een proof-of-conceptstudie
- Beoordelen of er een geschikte toedieningsvorm beschikbaar is op de Nederlandse markt, aangezien de enige vergunning is doorgehaald
## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

