---
layout: default
title: Flavoxate
parent: Alleen modelvoorspelling (L5)
nav_order: 153
evidence_level: L5
indication_count: 8
---

# Flavoxate
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **8** 
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

# Flavoxaat: Van urologische indicaties naar prikkelbaredarmsyndroom (IBS)

## Samenvatting in één zin

Flavoxaat is een spierverslappend middel (antispasmodicum) voor de urinewegen, geregistreerd in Nederland onder de naam Urispas. Het TxGNN-model voorspelt dat het mogelijk werkzaam is bij **prikkelbaredarmsyndroom (IBS)**, maar er zijn in de voor dit rapport verzamelde gegevens **geen klinische studies** en **geen publicaties** die deze voorspelling ondersteunen.

> Opmerking: het rapport volgt de eerstgerangschikte voorspelling (ADHD, inattentief type) als formele hoofdvoorspelling in de brongegevens. Omdat die voorspelling mechanistisch niet onderbouwd is, wordt hieronder IBS belicht als de meest coherente kandidaat. De overige voorspellingen staan in een aparte tabel.

---

## Snel overzicht

| Item | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Niet beschikbaar in de gegevens (geen goedgekeurde indicatietekst in de vergunning) |
| Voorspelde nieuwe indicatie (rang 1 in model) | ADHD, inattentief type |
| Mechanistisch meest coherente voorspelling | Prikkelbaredarmsyndroom (IBS) |
| TxGNN-voorspellingsscore | ADHD inattentief type: 99,75%; IBS: 99,74% |
| Bewijsniveau | L5 (alleen modelvoorspelling) |
| Marktstatus in Nederland | Alleen doorgehaald (vergunning ingetrokken) |
| Aantal vergunningen | 1 (0 geldig, 1 ingetrokken) |
| Aanbevolen besluit | Hold (aanhouden) |

---

## Waarom is deze voorspelling redelijk?

Gegevens over het werkingsmechanisme van flavoxaat ontbreken momenteel in de dataset. Uit algemene farmacologische kennis (niet uit de verzamelde gegevens) is flavoxaat een urologisch spasmolyticum met gladde-spierrelaxerende, fosfodiësterase-remmende en zwakke anticholinerge en calciumantagonistische eigenschappen.

**IBS:** Gladde-spierrelaxatie en milde antimuscarinerge activiteit lijken conceptueel op die van antispasmodica die bij IBS worden gebruikt. Dit is de meest coherente van de modelvoorspellingen, maar het blijft biologisch plausibel en niet geverifieerd.

**ADHD (inattentief type en algemeen):** Er is geen ondersteunde mechanistische link. Een centraal-zenuwstelselrationale via PDE-remming of anticholinerge werking is speculatief en niet getest. De hoge score (0,997) is een grafiekgebaseerde associatie en geen klinisch bewijs. De term "ADHD" is bovendien grotendeels redundant met "ADHD, inattentief type".

**Overige voorspellingen:** zie de tabel hieronder.

### Overzicht van alle voorspellingen

| Rang | Voorspelde indicatie | TxGNN-score | Bewijsniveau | Beoordeling |
|----|------|------|------|------|
| 1 | ADHD, inattentief type | 99,75% | L5 | Geen onderbouwde mechanistische link |
| 2 | Prikkelbaredarmsyndroom | 99,74% | L5 | Plausibel, niet geverifieerd |
| 3 | Specifieke ontwikkelingsstoornis | 99,56% | L5 | Geen identificeerbare link; waarschijnlijk modelartefact |
| 4 | ADHD | 99,39% | L5 | Redundant met rang 1; modelartefact tot validatie |
| 5 | Caudaequinasyndroom | 99,27% | L5 | Neurochirurgisch spoedgeval; hooguit symptomatische verlichting van blaasklachten |
| 6 | Neurogene blaas (term verouderd) | 99,13% | L5 | Past het best bij de bekende farmacologie, maar niet bevestigd door de gegevens |
| 7 | Gastroduodenitis | 99,12% | L5 | Zwak |
| 8 | Maagzweer (ulcus pepticum) | 99,10% | L5 | Zwak; moderne therapie (PPI's, H. pylori-eradicatie) maakt vervolgonderzoek onwaarschijnlijk |

---

## Klinisch trialbewijs

Er zijn momenteel geen gerelateerde klinische studies geregistreerd.

---

## Literatuurbewijs

Er is momenteel geen gerelateerde literatuur beschikbaar.

---

## Informatie over de Nederlandse markt

| RVG-nummer | Productnaam | Toedieningsvorm | Goedgekeurde indicatie |
|---------|------|------|-----------|
| RVG 117414//08322 | Urispas, omhulde tabletten 200 mg | Omhulde tabletten | Niet beschikbaar (vergunning ingetrokken) |

De enige bekende vergunning is ingetrokken; er is op dit moment geen geldig geregistreerd flavoxaatproduct in de gegevens van het CBG-MEB.

---

## Veiligheidsoverwegingen

**Contra-indicaties volgens de kennisgrafiek (TxGNN/PrimeKG).** Dit zijn relaties uit een kennisgrafiek en geen bijsluitertekst. Ze zijn bedoeld als signaal en moeten worden geverifieerd aan de hand van de SmPC:
- Gesloten-hoekglaucoom
- Pylorusstenose
- Paralytische ileus
- Intestinale obstructie
- Familiaire viscerale myopathie
- Actieve maagzweer
- Obstructie van de urinewegen

**Geneesmiddelinteracties:** in totaal zijn 86 interacties gevonden; hieronder de belangrijkste uit de verstrekte lijst.
- **Ernstig (Major):** kaliumcitraat, kaliumchloride
- **Matig (Moderate):** onder andere hyoscyamine, atropine, scopolamine, glycopyrronium, clidinium, dicyclomine, trospium, mepenzolaat, methscopolamine, propantheline (aanvullende anticholinerge werking), loperamide, morfine, eluxadoline, metoclopramide, prucalopride, pramlintide, dronabinol en nabilon

Voor waarschuwingen en contra-indicaties volgens de officiële productinformatie: raadpleeg de SmPC. Deze tekst van het CBG-MEB was niet beschikbaar voor dit rapport.

---

## Conclusie en vervolgstappen

**Besluit: Hold**

**Onderbouwing:**
- Alle voorspellingen berusten uitsluitend op een grafiekmodel (bewijsniveau L5), zonder klinische studies of publicaties. De enige vergunning is ingetrokken en de veiligheidsinformatie uit de productinformatie ontbreekt.

**Om verder te gaan is nodig:**
- De SmPC/bijsluiter van het CBG-MEB ophalen en verwerken (waarschuwingen en contra-indicaties); dit blokkeert de veiligheidsscreening.
- Gegevens over het werkingsmechanisme aanvullen (bijvoorbeeld via DrugBank).
- Een gerichte literatuur- en trialzoekopdracht voor flavoxaat bij IBS en neurogene blaas.
- De oorspronkelijke indicatie en de actuele marktstatus (ingetrokken vergunning, mogelijke beschikbaarheid van alternatieven) bevestigen.
- Voor een vervolg bij IBS: het anticholinerge interactieprofiel en de contra-indicaties (o.a. obstructie, glaucoom) beoordelen in de beoogde patiëntengroep.
## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

