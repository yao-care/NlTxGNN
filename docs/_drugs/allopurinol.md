---
layout: default
title: Allopurinol
parent: Alleen modelvoorspelling (L5)
nav_order: 27
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Allopurinol: voorspelde nieuwe indicatie Hepatische porfyrie (bewijsniveau L5). Oorspronkelijke indicatie: Jicht (ook hyperurikemie en acute urinezuurnefropathie)"
monitor_inn: "Allopurinol"
predicted_indications: ["hepatic porphyria", "hepatopulmonary syndrome", "primitive portal vein thrombosis", "idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension", "hepatoportal sclerosis", "disorder of phenylalanine metabolism", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "idiopathic eosinophilic myositis"]
---

# Allopurinol
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

# Allopurinol: Van jicht naar hepatische porfyrie

## Samenvatting in één zin

Allopurinol is een xanthine-oxidaseremmer die oorspronkelijk wordt gebruikt voor de behandeling van jicht, hyperurikemie en acute urinezuurnefropathie. Het TxGNN-model voorspelt dat het mogelijk werkzaam is bij **hepatische porfyrie**, maar hiervoor zijn **0 klinische studies** en slechts **2 publicaties** van beperkte relevantie gevonden. De beschikbare gegevens wijzen eerder op een mogelijk veiligheidsrisico dan op therapeutisch voordeel.

---

## Snel overzicht

| Onderdeel | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Jicht (ook hyperurikemie en acute urinezuurnefropathie) |
| Voorspelde nieuwe indicatie | Hepatische porfyrie |
| TxGNN-voorspellingsscore | 99,95% |
| Evidentieniveau | L5 |
| Marktstatus in Nederland | Alleen ingetrokken registraties |
| Aantal registraties | 1 (ingetrokken) |
| Aanbevolen beslissing | Hold |

---

## Waarom is deze voorspelling (on)aannemelijk?

Gegevens over het werkingsmechanisme van allopurinol zijn in de voor dit rapport samengestelde data niet beschikbaar. Algemeen bekend is dat allopurinol het enzym xanthine-oxidase remt en zo de vorming van urinezuur verlaagt. Dat verklaart het effect bij jicht en hyperurikemie.

Voor hepatische porfyrie is er geen ondersteunend mechanisme. Integendeel: in knaagdiermodellen is beschreven dat allopurinol hepatisch 5-aminolevulinaatsynthase (ALAS1) kan induceren en het heem van cytochroom P450 kan afbreken. Dit zou porfyrie naar verwachting eerder verergeren dan behandelen. De hoge TxGNN-score is waarschijnlijk een artefact van gedeelde heem- en geneesmiddelmetabolisme-verbindingen in de kennisgraaf en mag niet worden gelezen als bewijs van werkzaamheid.

Andere hoog scorende voorspellingen (o.a. hepatopulmonair syndroom, primitieve portale veneuze trombose, idiopathische koper-geassocieerde cirrose, hepatoportale sclerose) hebben identieke of vrijwel identieke scores en geen enkel onderliggend bewijs. Dat wijst op een niet-specifiek signaal in de graaf.

---

## Bewijs uit klinische studies

Er zijn momenteel geen gerelateerde klinische studies geregistreerd.

---

## Bewijs uit de literatuur

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Review/hypothese | Medical Hypotheses | Hypothese over metabolische beïnvloeding van ALAS1 via tryptofaan en remmers van heemgebruik door tryptofaan-2,3-dioxygenase als therapie voor acute hepatische porfyrieën. Betreft allopurinol niet direct. |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Preklinisch (dierstudie) | Biochemical Pharmacology | Effecten van carbamazepine op het heemmetabolisme in rattenlever; het middel verergert hepatische porfyrie. Betreft allopurinol niet direct. |

Beide publicaties tonen geen therapeutisch voordeel van allopurinol bij porfyrie.

---

## Informatie over de Nederlandse markt

| RVG-nummer | Productnaam | Toedieningsvorm | Goedgekeurde indicatie |
|---------|------|------|-----------|
| RVG 117526 | Allopurinol Sandoz tablet 300 mg | Tablet | Niet beschikbaar (registratie ingetrokken) |

Deze enige registratie bij het CBG-MEB is ingetrokken; er is geen geldige registratie van een enkelvoudig of combinatieproduct in de data gevonden.

---

## Veiligheidsoverwegingen

- **Contra-indicaties (afgeleid uit de kennisgraaf, niet uit de productinformatie)**: leverziekte, galblaasziekte, verminderde nierfunctie, overgevoeligheidsvasculitis, cutane leukocytoclastische angiitis, allergische cutane vasculitis en anti-glomerulaire basaalmembraanziekte.
- **Geneesmiddelinteracties**: In totaal zijn 100 interacties gevonden; hieronder de belangrijkste weergegeven uit de beschikbare lijst.
  - *Matig*: aluminiumhydroxide, attapulgiet, kaolien, magaldraat, sucralfaat.
  - *Licht*: amoxicilline, chloorpropamide.
  - *Niveau onbekend*: onder andere calcitriol, vitamine A, pantoprazol, glimepiride, mesalazine, doxycycline, clotrimazol, acarbose, morfine, metformine, omeprazol, rosiglitazon, palonosetron.
- **Aanvullende zorg**: allopurinol kan overgevoeligheidsreacties veroorzaken (waaronder eosinofilie in het kader van DRESS). Daarnaast bestaat een plausibel risico op een porfyrinogeen effect, wat voor deze indicatie van directe relevantie is.

Raadpleeg voor volledige waarschuwingen en contra-indicaties de SmPC (Samenvatting van de Productkenmerken) en de bijsluiter.

---

## Conclusie en vervolgstappen

**Beslissing: Hold**

**Onderbouwing:**
- De voorspelling berust uitsluitend op een computermodel (L5). Er zijn geen klinische studies, en de enige gevonden literatuur ondersteunt geen voordeel. Er is bovendien een plausibel risico dat allopurinol porfyrie verergert. De Nederlandse registratie is ingetrokken.

**Om verder te gaan is het volgende nodig:**
- Beoordeling van de porfyrinogeniciteit van allopurinol (literatuur, porfyriedatabases, klinische casuïstiek).
- Gegevens over het werkingsmechanisme (DrugBank) en de waarschuwingen/contra-indicaties uit de productinformatie van het CBG-MEB. Het ontbreken hiervan blokkeert de veiligheidsscreening.
- Preklinisch bewijs dat een therapeutisch effect bij hepatische porfyrie aannemelijk maakt.
- Een actuele beoordeling van de registratiestatus in Nederland (andere allopurinolproducten kunnen elders zijn geregistreerd).

---

## Overige voorspelde indicaties (ter informatie)

Alle overige voorspellingen in de top 10 hebben evidentieniveau L5 en de aanbeveling **Hold**: hepatopulmonair syndroom, primitieve portale veneuze trombose, idiopathische koper-geassocieerde cirrose, vroeg beginnende familiaire niet-cirrotische portale hypertensie, hepatoportale sclerose, stoornis van het fenylalaninemetabolisme, immuungemedieerde necrotiserende myopathie, antisynthetasesyndroom en idiopathische eosinofiele myositis. Voor geen van deze zijn klinische studies gevonden; de gevonden literatuur (alleen bij fenylalaninemetabolisme) is niet relevant voor een therapeutisch effect.
## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

