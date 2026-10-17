---
layout: default
title: Alitretinoin
parent: Alleen modelvoorspelling (L5)
nav_order: 26
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Alitretinoin: voorspelde nieuwe indicatie Amenorroe (bewijsniveau L5). Oorspronkelijke indicatie: Ernstig chronisch handeczeem (bron: DrugBank-gegevens"
monitor_inn: "alitretinoin"
predicted_indications: ["amenorrhea (disease)", "acne (disease)", "atypical coarctation of aorta", "pregnancy associated osteoporosis", "aortic malformation", "postmenopausal osteoporosis", "autosomal dominant neovascular inflammatory vitreoretinopathy", "breast fibrocystic disease", "benign mammary dysplasia", "Worth syndrome"]
---

# Alitretinoin
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **10** 
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

# Alitretinoïne: Van chronisch handeczeem naar amenorroe

## Samenvatting in één zin

Alitretinoïne (9-cis-retinoïnezuur) wordt in de literatuur gebruikt bij ernstig chronisch handeczeem dat niet reageert op sterke lokale corticosteroïden, en bij Kaposi-sarcoom. Het TxGNN-model voorspelt dat het werkzaam zou kunnen zijn bij **amenorroe**, maar er zijn **0 klinische studies** en **0 publicaties** die deze richting ondersteunen. Het is dus een zuivere modelvoorspelling.

---

## Snel overzicht

| Onderdeel | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Ernstig chronisch handeczeem (bron: DrugBank-gegevens; de Nederlandse vergunning vermeldt geen indicatietekst) |
| Voorspelde nieuwe indicatie | Amenorroe |
| TxGNN-voorspellingsscore | 99,99% |
| Bewijsniveau | L5 |
| Marktstatus in Nederland | Alleen doorgehaalde (ingetrokken) vergunning |
| Aantal vergunningen | 1 (geen geldig) |
| Aanbevolen beslissing | Hold |

---

## Waarom is deze voorspelling (on)aannemelijk?

Alitretinoïne activeert de retinoïnezuurreceptoren (RAR-α, -β, -γ) en de retinoïde X-receptoren (RXR-α, -β, -γ). Deze nucleaire receptoren sturen celdifferentiatie, ook in voortplantingsweefsel. Gedetailleerde gegevens over het werkingsmechanisme zijn voor dit rapport niet beschikbaar.

De link met amenorroe is alleen door het model voorspeld. Retinoïden zijn teratogeen en kunnen de menstruatie en de hormoonhuishouding verstoren. Een therapeutische rol is daarom onwaarschijnlijk zonder aanvullend bewijs. Het oorspronkelijke gebruik (huidaandoeningen) heeft bovendien weinig overlap met een gynaecologisch-endocrien probleem.

**Overige voorspellingen (ter context):** de acne-voorspelling (score 99,92%) is biologisch plausibel, omdat retinoïden de verhoorning van de haarfollikel normaliseren en de talgproductie verminderen. Het bewijs is echter indirect: twee overzichtsartikelen over de retinoïdeklasse. Orale isotretïnoïne en lokale retinoïden zijn bovendien al beschikbaar, dus de toegevoegde waarde is onduidelijk. De overige voorspellingen (o.a. aortamalformaties, osteoporose, benigne borstaandoeningen, Worth-syndroom) hebben geen bewijs en deels een tegenstrijdig veiligheidsprofiel (teratogeniteit).

---

## Klinische studies

Er zijn momenteel geen gerelateerde klinische studies geregistreerd.

---

## Literatuurbewijs

Voor amenorroe is geen literatuur beschikbaar. Voor de tweede voorspelling (acne) zijn twee overzichtsartikelen gevonden:

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|-----|------|------|---------|
| [41692081](https://pubmed.ncbi.nlm.nih.gov/41692081/) | 2026 | Review | Clinics in Dermatology | Overzicht van vitamine A en retinoïden in de dermatologie, waaronder alitretinoïne; klasse-niveau, niet specifiek voor acne met alitretinoïne |
| [11586072](https://pubmed.ncbi.nlm.nih.gov/11586072/) | 2001 | Review | Skin Pharmacology and Applied Skin Physiology | Retinoïden werken via nucleaire receptoren; bespreking van toekomstige dermatologische indicaties |

---

## Informatie over de Nederlandse markt

| RVG-nummer | Productnaam | Toedieningsvorm | Goedgekeurde indicatie |
|---------|------|------|-----------|
| RVG 119813//100962 | Toctino 30 mg, capsules, zacht | Niet vermeld | Niet vermeld (vergunning doorgehaald) |

De enige vergunning is doorgehaald, dus er is momenteel geen geldig product op de Nederlandse markt volgens het CBG-MEB.

---

## Cytotoxiciteit

| Onderdeel | Inhoud |
|------|------|
| Cytotoxiciteitsclassificatie | Niet van toepassing als klassiek cytostaticum; gebruikt bij o.a. Kaposi-sarcoom |
| Myelosuppressierisico | Raadpleeg de SmPC (waarschuwingen en voorzorgen) |
| Emetogeniciteit | Raadpleeg de SmPC |
| Controle-items | Raadpleeg de SmPC |
| Bescherming bij hantering | Raadpleeg de SmPC |

---

## Veiligheidsaspecten

- **Contra-indicaties volgens kennisgraaf (niet uit de bijsluitertekst):** de TxGNN-kennisgraaf (PrimeKG) bevat contra-indicatierelaties met mycosis fungoides en varianten, primair cutaan T-cellymfoom, folliculotroop mycosis fungoides, gelokaliseerde pagetoïde reticulose en granulomateuze slack skin-ziekte.
- **Teratogeniteit:** retinoïden zijn teratogeen. Dit is een ernstig bezwaar voor indicaties in de voortplanting en bij zwangerschap.
- **Farmacologische interacties:** er zijn 7 farmacologische doelwitrelaties gevonden: RARA, RARB, RARG, RXRA, RXRB, RXRG en VKORC1. De VKORC1-relatie is relevant voor het vitamine K-systeem en mogelijk voor anticoagulantia, maar de klinische betekenis is niet vastgesteld.

Raadpleeg voor volledige veiligheidsinformatie de SmPC (Samenvatting van de Productkenmerken). Waarschuwingen en contra-indicaties uit de Nederlandse bijsluiter waren niet beschikbaar.

---

## Conclusie en vervolgstappen

**Beslissing: Hold**

**Onderbouwing:**
- De voorspelling voor amenorroe berust alleen op een modelscore (L5), zonder studies of publicaties, en het teratogene en endocrien verstorende profiel van retinoïden pleit tegen therapeutisch gebruik. Daar komt bij dat er geen geldige Nederlandse vergunning is.
- Acne is de enige voorspelling met enige (indirecte) steun, maar valt in categorie L4 (onderzoeksvraag) en wordt al door bestaande retinoïden gedekt.

**Voor vervolg is nodig:**
- De waarschuwingen en contra-indicaties uit de SmPC/bijsluiter (blokkerende datalacune voor de veiligheidsscreening).
- Gegevens over het werkingsmechanisme (bijv. via DrugBank).
- Direct bewijs (preklinisch of klinisch) voor alitretinoïne bij de voorgestelde indicatie.
- Een beoordeling van de toegevoegde waarde ten opzichte van bestaande retinoïden bij acne, als die richting wordt gevolgd.
- Duidelijkheid over de reden en de status van de ingetrokken vergunning (CBG-MEB).
## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

