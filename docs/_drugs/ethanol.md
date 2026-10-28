---
layout: default
title: Ethanol
parent: Alleen modelvoorspelling (L5)
nav_order: 140
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Ethanol: voorspelde nieuwe indicatie Migraine (migraine disorder) (bewijsniveau L5). Oorspronkelijke indicatie: Niet beschikbaar in de vergunningsgegevens"
monitor_inn: "ethanol"
predicted_indications: ["migraine disorder", "migraine with brainstem aura"]
---

# Ethanol
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

## Ethanol: Van oorspronkelijke indicatie (niet vastgelegd) naar migraine
{: .text-alpha }

## Samenvatting in één zin

Ethanol (ethylalcohol) is een bekende stof die onder meer als ontsmettingsmiddel in huidoplossingen wordt gebruikt. In de Nederlandse vergunningsgegevens is geen oorspronkelijke indicatie vastgelegd.
Het TxGNN-model voorspelt dat ethanol mogelijk werkzaam is bij **migraine**, maar er zijn **geen klinische studies** en **geen literatuur die ethanol als behandeling van migraine ondersteunt**. De gevonden publicaties beschrijven ethanol vooral als *uitlokkende factor* van migraine.

---

## Snel overzicht

| Item | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Niet beschikbaar in de vergunningsgegevens |
| Voorspelde nieuwe indicatie | Migraine (migraine disorder) |
| TxGNN-voorspellingsscore | 0,9929 |
| Bewijsniveau | L5 (alleen modelvoorspelling) |
| Marktstatus in Nederland | In de handel (geldige vergunningen: 1 van 1) |
| Aantal vergunningen | 1 (geldig: 1) |
| Aanbevolen beslissing | Hold |

---

## Waarom is deze voorspelling (on)aannemelijk?

Gedetailleerde gegevens over het werkingsmechanisme van ethanol ontbreken in de data die voor dit rapport zijn verzameld. De beschikbare literatuur wijst er juist op dat ethanol bij migraine een **uitlokkende rol** speelt, geen therapeutische:

- Een preklinische muizenstudie laat zien dat ethanol wordt omgezet in acetaldehyde, dat via CGRP-receptor en TRPA1 in Schwann-cellen pijnovergevoeligheid rond het oog veroorzaakt (PMID 37101198).
- Andere mechanistische publicaties beschrijven het openen van ATP-gevoelige kaliumkanalen die meningeale nociceptoren activeren (PMID 40785517) en 'spreading depression'-modellen (PMID 31231207).
- Genetische associatiestudies (o.a. ADH2, GABA-receptoren) gaan over gevoeligheid voor migraine, niet over een behandeleffect.

De hoge TxGNN-score (0,9929) komt van het TxGNN-model (deep learning) en kan overeenkomsten weerspiegelen die het model heeft geleerd tussen verwante aandoeningen, niet biologisch bewijs. Gezien de rol als trigger, de toxiciteit en het uitgebreide interactieprofiel (1085 geneesmiddelinteracties) is ethanol geen aannemelijke kandidaat voor herpositionering bij migraine.

De tweede voorspelling, **migraine met hersenstamaura** (score 0,9914), heeft geen specifiek ondersteunend bewijs. De gevonden literatuur betreft algemene migrainegenetica en andere stoffen (carisbamaat, menthol, palmitoylethanolamide). Palmitoylethanolamide is een andere verbinding en telt niet als bewijs voor ethanol.

---

## Bewijs uit klinische studies

Momenteel zijn er geen gerelateerde klinische studies geregistreerd.

---

## Bewijs uit literatuur

Alleen publicaties die direct over ethanol en migraine gaan, zijn hieronder opgenomen. Geen ervan toont een therapeutisch effect van ethanol.

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|-----|------|------|---------|
| [36373782](https://pubmed.ncbi.nlm.nih.gov/36373782/) | 2022 | Review | Headache | Overzicht van de complexe relatie tussen alcohol en migraine (alcohol als trigger) |
| [37101198](https://pubmed.ncbi.nlm.nih.gov/37101198/) | 2023 | Preklinisch (muis) | J Biomed Sci | Acetaldehyde via CGRP-receptor en TRPA1 veroorzaakt door ethanol geïnduceerde allodynie; relevant voor migraine als trigger |
| [19486361](https://pubmed.ncbi.nlm.nih.gov/19486361/) | 2010 | Genetische associatiestudie | Headache | Onderzoek naar ADH2-genotype en migrainerisico |
| [40785517](https://pubmed.ncbi.nlm.nih.gov/40785517/) | 2025 | Preklinisch (mechanistisch) | Cephalalgia | Opening van KATP-kanalen activeert meningeale nociceptoren; implicaties voor het ontstaan van migraine |
| [31231207](https://pubmed.ncbi.nlm.nih.gov/31231207/) | 2019 | Review | Front Aging Neurosci | Spreading depression-model en hersenveroudering |
| [42153521](https://pubmed.ncbi.nlm.nih.gov/42153521/) | 2026 | Scoping review | Drug Alcohol Rev | CGRP-signalering bij alcoholgebruiksstoornissen |

De overige gevonden publicaties gaan over andere stoffen of algemene migrainegenetica en zijn niet als bewijs voor ethanol meegeteld.

---

## Informatie over de Nederlandse markt

| RVG-nummer | Productnaam | Toedieningsvorm | Goedgekeurde indicatie |
|---------|------|------|-----------|
| RVG 117752 | Chloorhexidinetinctuur Fresenius Kabi, rood, oplossing voor cutaan gebruik 5 mg/ml / 70% v/v (status: geldig) | Oplossing voor cutaan gebruik | Niet beschikbaar |

---

## Veiligheidsoverwegingen

**Geneesmiddelinteracties**: In totaal zijn 1085 interacties bekend. Voorbeelden:

- **Ernstig (Major)**: eluxadoline
- **Matig (Moderate)**: o.a. acarbose, albiglutide, acetohexamide, alogliptine, acetylsalicylzuur, atropine, bupropion, canagliflozine, chloorpropamide, dapagliflozine, dulaglutide, empagliflozine
- **Gering (Minor)**: doxycycline, cimetidine

Voor waarschuwingen en contra-indicaties: raadpleeg de SmPC (Samenvatting van de Productkenmerken) en de bijsluiter. Deze gegevens waren niet beschikbaar in de data die voor dit rapport zijn verzameld.

---

## Conclusie en vervolgstappen

**Beslissing: Hold**

**Onderbouwing:**
- Er is alleen een modelvoorspelling (bewijsniveau L5), zonder klinische studies. De literatuur beschrijft ethanol als migrainetrigger, niet als behandeling. Samen met de toxiciteit en het brede interactieprofiel is herpositionering voor migraine niet aannemelijk.

**Om verder te gaan, is het volgende nodig:**
- Bijsluiter- en SmPC-gegevens van het CBG-MEB (waarschuwingen, contra-indicaties) om veiligheidsscreening mogelijk te maken
- Gegevens over het werkingsmechanisme uit DrugBank
- Prospectief klinisch bewijs dat een therapeutisch effect van ethanol bij migraine aantoont (momenteel afwezig)
- Een heroverweging van de voorspelling, waarbij de rol van ethanol als trigger expliciet wordt meegenomen
## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

