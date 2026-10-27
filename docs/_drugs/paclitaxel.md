---
layout: default
title: Paclitaxel
parent: Alleen modelvoorspelling (L5)
nav_order: 263
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Paclitaxel: voorspelde nieuwe indicatie Borstkanker bij vrouwen (female breast carcinoma) (bewijsniveau L5). Oorspronkelijke indicatie: Ovariumkanker (de vergunningsgegevens bevatten geen indicatiete…"
monitor_inn: "Paclitaxel"
predicted_indications: ["parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
---

# Paclitaxel
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

## Paclitaxel: Van ovariumkanker naar borstkanker bij vrouwen (female breast carcinoma)
{: .text-alpha }

## Samenvatting in één oogopslag

Paclitaxel is een cytostaticum uit de taxanen. In de voor dit rapport samengestelde gegevens staat het vooral als middel bij ovariumkanker. Het TxGNN-model voorspelt effectiviteit bij **borstkanker bij vrouwen**. Dit wordt ondersteund door **44 geregistreerde klinische studies** (waaronder 7 afgeronde fase 3-studies) en **20 publicaties**. Let op: paclitaxel wordt bij borstkanker al breed gebruikt. Het gaat hier dus om een indicatie dicht bij het bestaande gebruik en niet om echte herpositionering.

---

## Snel overzicht

| Item | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Ovariumkanker (de vergunningsgegevens bevatten geen indicatietekst; deze indicatie komt uit de kennisgraaf van het model) |
| Voorspelde nieuwe indicatie | Borstkanker bij vrouwen (female breast carcinoma) |
| TxGNN-voorspellingsscore | 99,995% |
| Bewijsniveau | L1 (zie toelichting hieronder) |
| Marktstatus in Nederland | Alleen doorgehaalde (ingetrokken) vergunning |
| Aantal vergunningen | 1 (doorgehaald) |
| Aanbevolen besluit | Doorgaan met randvoorwaarden (Proceed with Guardrails) |

**Toelichting bewijsniveau:** de gegevens bevatten 7 afgeronde gerandomiseerde fase 3-studies waarin paclitaxel onderdeel is van het regime. Volgens de beoordelingsregels (≥2 afgeronde fase 3-RCT's) is dat L1. De eerder berekende classificatie was L2, met de opmerking dat er geen fase 3-studie zou zijn. Dat komt niet overeen met de studielijst. In veel van deze studies is paclitaxel het basisregime en niet de onderzochte variabele, dus L1 moet voorzichtig worden gelezen.

---

## Waarom is deze voorspelling redelijk?

Gedetailleerde werkingsmechanismegegevens (DrugBank) ontbreken in de samengestelde gegevens. Uit de bekende farmacologie volgt wel dat paclitaxel microtubuli stabiliseert en de afbraak van de mitotische spoel blokkeert. Dat leidt tot G2/M-arrest en apoptose in snel delende tumorcellen. Dit werkingsmechanisme hangt niet af van hormoonreceptoren.

Ovariumkanker en borstkanker zijn beide solide tumoren die gevoelig zijn voor taxanen. Het celdodende effect van paclitaxel is dus op beide van toepassing. Paclitaxel en nab-paclitaxel zijn bij borstkanker al gevestigde behandelingen, onder meer bij gemetastaseerde ziekte en in neoadjuvante en adjuvante regimes. De voorspelling van het model komt daarmee overeen met de klinische praktijk.

---

## Klinische studies

Er zijn 44 studies gevonden. Hieronder staan de 10 meest relevante: gerandomiseerde fase 3-studies en studies met de hoogste relevantiebeoordeling.

| Studienummer | Fase | Status | Inclusie | Belangrijkste bevindingen |
|---------|------|------|------|---------|
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Fase 3 | Afgerond | Niet vermeld | Paclitaxel met of zonder gemcitabine bij inoperabele, lokaal teruggekeerde of gemetastaseerde borstkanker |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Fase 3 | Afgerond | 652 | Taxaanchemotherapie met lapatinib versus trastuzumab als eerstelijnsbehandeling bij HER2-positieve gemetastaseerde borstkanker |
| [NCT01822314](https://clinicaltrials.gov/study/NCT01822314) | Fase 3 | Afgerond | 632 | Neoadjuvant nab-paclitaxel versus oplosmiddelgebonden paclitaxel (gevolgd door AC/EC/FEC) bij HER2-negatieve borstkanker met hoog risico; primair eindpunt pathologisch complete respons |
| [NCT00075270](https://clinicaltrials.gov/study/NCT00075270) | Fase 3 | Afgerond | 580 | Paclitaxel met lapatinib versus paclitaxel met placebo als eerstelijnsbehandeling bij gevorderde of gemetastaseerde borstkanker |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Fase 3 | Afgerond | 478 | Dose-dense FE75C gevolgd door docetaxel versus paclitaxel als adjuvante chemotherapie bij borstkanker met positieve lymfeklieren |
| [NCT00553358](https://clinicaltrials.gov/study/NCT00553358) | Fase 3 | Afgerond | 455 | Neo-ALTTO: neoadjuvant lapatinib, trastuzumab of de combinatie, elk met paclitaxel, bij HER2-positieve borstkanker |
| [NCT00513292](https://clinicaltrials.gov/study/NCT00513292) | Fase 3 | Afgerond | 280 | Neoadjuvant FEC gevolgd door paclitaxel plus trastuzumab versus de omgekeerde volgorde bij operabele HER2-positieve borstkanker |
| [NCT00272987](https://clinicaltrials.gov/study/NCT00272987) | Fase 3 | Beëindigd | 63 | Paclitaxel plus trastuzumab met lapatinib of placebo bij ErbB2-overexpresserende gemetastaseerde borstkanker; vroegtijdig beëindigd |
| [NCT00003539](https://clinicaltrials.gov/study/NCT00003539) | Fase 2 | Afgerond | 50 | Wekelijks paclitaxel (1 uur) plus anti-HER2-antilichaam bij gemetastaseerde borstkanker; toetst direct de werkzaamheid van paclitaxel |
| [NCT00006120](https://clinicaltrials.gov/study/NCT00006120) | Fase 2 | Onbekend | Niet vermeld | Gerandomiseerde vergelijking van twee schema's van docetaxel of paclitaxel bij gemetastaseerde borstkanker |

---

## Literatuur

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|-----|------|------|---------|
| [10791395](https://pubmed.ncbi.nlm.nih.gov/10791395/) | 2000 | Review | Lancet | Taxanen (paclitaxel, docetaxel) zijn bewezen onderdelen van de behandeling van gevorderde borst-, long- en ovariumkanker; in de VS goedgekeurd voor adjuvante behandeling bij borstkanker met positieve klieren |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug and Therapeutics Bulletin | Overzicht van paclitaxel en docetaxel bij borst- en ovariumkanker; vergunning uitgebreid naar gemetastaseerde borstkanker |
| [29532546](https://pubmed.ncbi.nlm.nih.gov/29532546/) | 2018 | Klinische studie (fase II) | The Breast Journal | Adjuvante metronomische AC gevolgd door wekelijks nab-paclitaxel bij vroege borstkanker met hoog risico; beoordeling van ziektevrije overleving, dosis en toxiciteit |
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Klinische studie (fase II) | Cancer | Doxorubicine plus paclitaxel bij gevorderde borstkanker; belang van eerdere adjuvante anthracyclinebehandeling |
| [11745249](https://pubmed.ncbi.nlm.nih.gov/11745249/) | 2001 | Niet geclassificeerd | Cancer | Rol van paclitaxel in multimodale behandeling van inflammatoire borstkanker |
| [23267983](https://pubmed.ncbi.nlm.nih.gov/23267983/) | 2012 | Case report | Gan to Kagaku Ryoho | Complete respons van gevorderde borstkanker met lymfekliermetastasen op nab-paclitaxel als eerstelijnsbehandeling na recidief |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | Translationeel onderzoek | Nature Communications | TEKT4-varianten zijn verrijkt in tumoren na behandeling en hangen samen met resistentie tegen paclitaxel |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | Computationeel/preklinisch | Chemical Biology & Drug Design | Paclitaxelcombinaties tegen borstkanker en identificatie van biomarkers in vivo |

---

## Informatie over de Nederlandse markt

| RVG-nummer | Productnaam | Toedieningsvorm | Geregistreerde indicatie |
|---------|------|------|-----------|
| RVG 102965 | Paclitaxel Accord 6 mg/ml concentraat voor oplossing voor infusie | Concentraat voor oplossing voor infusie | Niet vermeld in de gegevens; vergunning doorgehaald |

Er is geen geldige vergunning voor paclitaxel in de samengestelde CBG-MEB-gegevens. Of er andere paclitaxelproducten op de Nederlandse markt zijn (bijvoorbeeld via EMA-procedures), moet apart worden nagegaan.

---

## Cytotoxiciteit

| Item | Inhoud |
|------|------|
| Cytotoxiciteitsclassificatie | Conventioneel cytostaticum (taxaan, microtubulistabilisator) |
| Risico op beenmergsuppressie | Hoog (neutropenie is een belangrijke dosisbeperkende bijwerking) |
| Emetogeniciteitsclassificatie | Laag |
| Controlepunten | Volledig bloedbeeld (neutrofielen, trombocyten, hemoglobine), lever- en nierfunctie, perifere neuropathie, overgevoeligheidsreacties |
| Bescherming bij bereiding en toediening | Ja, volgens richtlijnen voor het hanteren van cytostatica |

Raadpleeg voor de definitieve gegevens de waarschuwingen en voorzorgen in de SmPC.

---

## Veiligheidsoverwegingen

**Aandoeningen uit de kennisgraaf met een tegenindicatie-relatie** (afkomstig uit de kennisgraaf van het model, niet uit de bijsluiter): onder meer leverziekte, nierziekte, trombocytopenie, neutropenie, agranulocytose, anemie, perifere neuropathie, hyperbilirubinemie, myocardinfarct, astma, diabetes mellitus, psoriasis en angststoornissen. Deze lijst is een signaal en vervangt de officiële contra-indicaties niet.

**Geneesmiddelinteracties:** er zijn 100 interacties gevonden, hieronder staan de eerste 20.
- **Matig:** aprepitant, cimetidine, claritromycine, clotrimazol, dexamethason, eliglustat, metronidazol, miconazol, rolapitant, rosuvastatine, simvastatine, tinidazol, troglitazon
- **Gering:** ascorbinezuur, levofloxacine
- **Onbekend niveau:** glimepiride, doxycycline, morfine, metformine, omeprazol

De officiële waarschuwingen en contra-indicaties uit de bijsluiter ontbreken in de samengestelde gegevens. Raadpleeg de SmPC voor volledige veiligheidsinformatie.

---

## Conclusie en vervolgstappen

**Besluit: Doorgaan met randvoorwaarden (Proceed with Guardrails)**

**Onderbouwing:**
- Er zijn veel klinische studies, waaronder 7 afgeronde fase 3-studies waarin paclitaxel deel uitmaakt van het regime, en het mechanisme is niet afhankelijk van hormoonreceptoren.
- Paclitaxel is bij borstkanker al een gevestigde behandeling, maar veel studies onderzoeken een combinatiepartner en niet paclitaxel zelf.
- De veiligheidsinformatie uit de officiële bijsluiter ontbreekt, en er is geen geldige Nederlandse vergunning.

**Om verder te gaan is nodig:**
- Veiligheidsinformatie (waarschuwingen en contra-indicaties) uit de SmPC en bijsluiter van het CBG-MEB, als basis voor de veiligheidsscreening.
- Gegevens over het werkingsmechanisme uit DrugBank.
- Controle of er in Nederland een geldig paclitaxelproduct is (nationaal of via EMA) met de indicatie borstkanker.
- Beoordeling van de fase 3-studies op de vraag of paclitaxel zelf of een combinatiepartner de onderzochte variabele was.
- Een bewakingsplan voor beenmergsuppressie, neuropathie en overgevoeligheid, plus een controle op relevante geneesmiddelinteracties (onder meer CYP-remmers).
## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

