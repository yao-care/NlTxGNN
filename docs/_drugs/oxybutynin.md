---
layout: default
title: Oxybutynin
parent: Alleen modelvoorspelling (L5)
nav_order: 260
evidence_level: L5
indication_count: 3
---

# Oxybutynin
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

# Oxybutynine: Van overactieve blaas naar rustelozebenensyndroom

## Samenvatting in één zin

Oxybutynine is een antimuscarinisch middel dat oorspronkelijk wordt gebruikt bij overactieve blaas, neurogene blaas en caudaequinasyndroom. Het TxGNN-model voorspelt dat het mogelijk werkzaam is bij **rustelozebenensyndroom** (restless legs syndrome), maar hiervoor zijn **geen klinische studies** en **geen publicaties** beschikbaar. De voorspelling berust uitsluitend op een grafmodel.

---

## Snel overzicht

| Item | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Overactieve blaas, neurogene blaas, caudaequinasyndroom (afkomstig uit de TxGNN-kennisgraaf; de vergunningstekst bevat geen indicatie) |
| Voorspelde nieuwe indicatie | Rustelozebenensyndroom |
| TxGNN-voorspellingsscore | 99,74% |
| Bewijsniveau | L5 |
| Marktstatus in Nederland | Alleen doorgehaald (geen geldige vergunning) |
| Aantal vergunningen | 1 (doorgehaald) |
| Aanbevolen beslissing | Hold |

---

## Waarom is deze voorspelling aannemelijk?

Gegevens over het werkingsmechanisme van oxybutynine zijn in de voor dit rapport samengestelde data niet beschikbaar. Oxybutynine staat bekend als antimuscarinisch middel met anticholinerge werking; de werkzaamheid bij overactieve blaas is vastgesteld.

Een mechanistisch verband met rustelozebenensyndroom is op basis van de beschikbare gegevens **niet aangetoond**. Dit syndroom wordt vooral in verband gebracht met dopaminerge disfunctie en ijzertekort in de hersenen, niet met antimusc­arinische werking. Anticholinergica kunnen bij sommige patiënten de klachten zelfs verergeren. De hoge score is dus een statistische voorspelling uit het kennisgraafmodel en geen bevestiging van werkzaamheid.

Twee andere voorspelde indicaties verdienen vermelding als context:
- **Gastroduodenitis** (score 99,62%): geen klinische studies of literatuur. Antimuscarinica verminderen van oudsher de maagzuursecretie en darmmotiliteit, wat een losse farmacologische rationale biedt, maar anticholinergica zijn hiervoor geen huidige standaardbehandeling.
- **Maagzweerziekte** (score 99,31%): bewijsniveau L4, met drie oude, indirecte publicaties (zie hieronder). Moderne zuurremming (PPI's, eradicatie van *H. pylori*) heeft anticholinerge therapie bij deze indicatie grotendeels verdrongen.

---

## Bewijs uit klinische studies

Momenteel geen gerelateerde klinische studies geregistreerd voor rustelozebenensyndroom.

---

## Bewijs uit de literatuur

Momenteel geen gerelateerde literatuur beschikbaar voor rustelozebenensyndroom.

Ter context: voor de derde voorspelde indicatie (maagzweerziekte) zijn wel drie oude publicaties gevonden:

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|-----|------|------|---------|
| [14173506](https://pubmed.ncbi.nlm.nih.gov/14173506/) | 1964 | Klinische evaluatie (waarschijnlijk ongecontroleerd/observationeel) | Current Therapeutic Research | Klinische evaluatie van oxybutynine bij gastro-intestinale aandoeningen; samenvatting en resultaten niet beschikbaar |
| [4380481](https://pubmed.ncbi.nlm.nih.gov/4380481/) | 1965 | Farmacologisch overzicht/mechanisme | Arch Int Pharmacodyn Ther | Beschrijft oxybutynine als musculotroop spasmolyticum met matige anticholinerge werking |
| [2360335](https://pubmed.ncbi.nlm.nih.gov/2360335/) | 1990 | Casuïstiek (bijwerking) | DICP (Ann Pharmacother) | Oxybutynine-geïnduceerde refluxoesofagitis door verlaagde tonus van de onderste slokdarmsfincter |

---

## Informatie over de Nederlandse markt

| RVG-nummer | Productnaam | Toedieningsvorm | Goedgekeurde indicatie |
|---------|------|------|-----------|
| RVG 104980 | Oxybutynine HCl 5 mg ICC, tabletten (doorgehaald) | Niet vermeld | Niet vermeld |

Er is geen geldige vergunning voor oxybutynine in de data van het CBG-MEB. De enige geregistreerde vergunning is doorgehaald.

---

## Veiligheidsoverwegingen

- **Contra-indicaties (afkomstig uit de kennisgraaf, niet uit de officiële productinformatie):** hypertensie, nierziekte, pyouereter, leverziekte, galblaasziekte, benigne prostaathyperplasie, coronaire hartziekte, plotselinge hartstilstand, geleidingsstoornissen van het hart, gesloten-kamerhoekglaucoom, myasthenia gravis (waaronder die met volwassen aanvang) en andere aandoeningen van de neuromusculaire overgang, colitis ulcerosa, inflammatoire darmziekte, hyperthyreoïdie (ziekte van Graves, thyreotoxicose), hiatushernia, congenitale hernia diaphragmatica, paralytische ileus, darmobstructie, familiaire viscerale myopathie, obstructie van de blaashals, toxisch megacolon, gastro-oesofageale reflux en oesofagitis.
- **Geneesmiddelinteracties:** 243 interacties gevonden. Als **ernstig (Major)** zijn aangemerkt:
  - Kaliumcitraat
  - Kaliumchloride

  Voorbeelden van **matige** interacties: andere anticholinergica (hyoscyamine, atropine, glycopyrronium, trospium, dicyclomine, propantheline, methscopolamine), loperamide, morfine, opium, aprepitant, metoclopramide, eluxadoline en pramlintide.
- **Specifiek signaal bij gebruik in de bovenste tractus digestivus:** een casus uit 1990 beschrijft refluxoesofagitis door oxybutynine.

Voor volledige waarschuwingen en contra-indicaties: raadpleeg de SmPC (Samenvatting van de Productkenmerken) en de bijsluiter. De productinformatie van het CBG-MEB was voor dit rapport niet beschikbaar.

---

## Conclusie en vervolgstappen

**Beslissing: Hold**

**Onderbouwing:**
- De voorspelling voor rustelozebenensyndroom berust uitsluitend op een grafmodel (bewijsniveau L5), zonder studies of literatuur. Een plausibel mechanisme ontbreekt, en anticholinergica kunnen de klachten mogelijk verergeren. Bovendien is er in Nederland geen geldige vergunning meer.

**Om verder te gaan is nodig:**
- Productinformatie (SmPC) van het CBG-MEB voor waarschuwingen en contra-indicaties, nodig voor een veiligheidsscreening
- Gegevens over het werkingsmechanisme van oxybutynine (bijv. via DrugBank)
- Systematisch literatuuronderzoek naar anticholinergica en rustelozebenensyndroom, inclusief het risico op verergering van klachten
- Preklinisch of klinisch bewijs dat een verband met rustelozebenensyndroom ondersteunt
- Beoordeling van de vergunningsstatus en beschikbare toedieningsvormen bij eventuele heroverweging
## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

