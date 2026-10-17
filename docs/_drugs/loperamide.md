---
layout: default
title: Loperamide
parent: Alleen modelvoorspelling (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Loperamide: voorspelde nieuwe indicatie Acute besmettelijke conjunctivitis (bewijsniveau L5). Oorspronkelijke indicatie: Diarree en dysenterie (afkomstig uit de TxGNN-kennisgraaf"
monitor_inn: "loperamide"
predicted_indications: ["acute contagious conjunctivitis", "conjunctivitis", "gastroduodenitis", "pseudomembranous conjunctivitis", "chronic follicular conjunctivitis", "conjunctival folliculosis", "serous conjunctivitis except viral", "parasitic conjunctivitis", "Angelucci syndrome"]
---

# Loperamide
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **10** 
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

# Loperamide: Van diarree naar acute besmettelijke conjunctivitis

## Samenvatting in één zin

Loperamide wordt van oudsher gebruikt om diarree en dysenterie symptomatisch te behandelen. Het TxGNN-model voorspelt dat het werkzaam zou kunnen zijn bij **acute besmettelijke conjunctivitis**, maar hiervoor zijn **geen klinische studies** en **geen publicaties** gevonden. Deze voorspelling berust uitsluitend op het model en heeft geen onderbouwing in de praktijk.

---

## Snel overzicht

| Item | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Diarree en dysenterie (afkomstig uit de TxGNN-kennisgraaf; in de vergunningsgegevens is geen indicatietekst beschikbaar) |
| Voorspelde nieuwe indicatie | Acute besmettelijke conjunctivitis |
| TxGNN-voorspellingsscore | 99,97% |
| Bewijsniveau | L5 |
| Marktstatus in Nederland | Alleen doorgehaalde (ingetrokken) vergunningen |
| Aantal vergunningen | 3 (alle doorgehaald) |
| Aanbevolen besluit | Hold |

---

## Waarom is deze voorspelling (on)aannemelijk?

Voor loperamide zijn in de samengestelde gegevens geen mechanistische gegevens beschikbaar. Uit algemene farmacologische kennis is loperamide een perifere agonist van de mu-opioïdreceptor. Het werkt op de zenuwcellen in de darmwand en remt zo de darmmotiliteit. Daardoor vermindert het diarree als symptoom.

Er is **geen plausibele mechanistische link** tussen deze werking en een infectieuze ontsteking van het bindvlies van het oog. De zeer hoge score (0,9997) lijkt een artefact van de kennisgraaf: dezelfde score komt terug bij meerdere subtypen conjunctivitis, wat wijst op een gedeeld propagatie-effect in het netwerk en niet op een biologisch signaal.

Ook de andere voorspelde indicaties in de gegevens bieden weinig steun:
- **Conjunctivitis en subtypen** (o.a. pseudomembraneuze, chronisch folliculaire, parasitaire conjunctivitis, het syndroom van Angelucci): geen studies, geen literatuur, geen mechanistische onderbouwing.
- **Amoebendysenterie**: loperamide heeft geen antiparasitaire werking tegen *Entamoeba histolytica*. De literatuur wijst eerder op schade (zie hieronder).
- **Gastroduodenitis**: loperamide kan diarree verlichten, maar behandelt de onderliggende ontsteking niet.

---

## Klinisch studiebewijs

Momenteel geen gerelateerde klinische studies geregistreerd voor de voorspelde indicatie acute besmettelijke conjunctivitis.

---

## Literatuurbewijs

Momenteel is er geen gerelateerde literatuur beschikbaar voor acute besmettelijke conjunctivitis.

Voor andere hoog gescoorde voorspellingen zijn wel enkele publicaties gevonden. Deze duiden op veiligheidsrisico's en niet op werkzaamheid:

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|-----|------|------|---------|
| [17241255](https://pubmed.ncbi.nlm.nih.gov/17241255/) | 2007 | Case report | Journal of Travel Medicine | Fulminante amoebencolitis (toxisch megacolon) na zwaar loperamidegebruik; vertraging van de darmpassage kan het beloop bij invasieve dysenterie verslechteren (voorspelde indicatie: amoebendysenterie) |
| [41924411](https://pubmed.ncbi.nlm.nih.gov/41924411/) | 2026 | Case report | Cureus | Loperamide-geïnduceerde ademhalingsdepressie bij ernstige gastro-intestinale ontsteking na chemotherapie, door verhoogde systemische opname bij een aangetaste darmbarrière (voorspelde indicatie: gastroduodenitis) |
| [3893119](https://pubmed.ncbi.nlm.nih.gov/3893119/) | 1985 | Review | The American Journal of Medicine | Overzicht van niet-vochtgerelateerde therapie en chemoprofylaxe bij acute diarree; symptomatische middelen kunnen diarree en klachten verminderen (voorspelde indicatie: amoebendysenterie) |

---

## Informatie over de Nederlandse markt

Alle drie de vergunningen zijn doorgehaald; er is momenteel geen geldige vergunning voor een loperamide-monopreparaat in de samengestelde gegevens. Gegevens over farmaceutische vorm en goedgekeurde indicatie ontbreken.

| RVG-nummer | Productnaam | Status |
|---------|------|------|
| RVG 116627//08423 | Imodium 0,2 mg/ml drank | Doorgehaald |
| RVG 114697 | Loperuma 2 mg/125 mg, kauwtabletten | Doorgehaald |
| RVG 113192 | Losiveca 2mg/ 125mg, tabletten | Doorgehaald |

---

## Veiligheidsoverwegingen

- **Contra-indicaties volgens de kennisgraaf** (afkomstig uit het TxGNN-netwerk, geen bijsluitertekst): leverziekte, galblaasaandoening, paralytische ileus, darmobstructie, familiaire viscerale myopathie, dysenterie, diarree, infectieuze diarree en infectieuze darmziekten.
- **Geneesmiddelinteracties**: in totaal 842 interacties gevonden (DDInter). Voorbeelden van ernstige (Major) interacties: abirateron, ranitidine, fosamprenavir en gemfibrozil. Voorbeelden van matige (Moderate) interacties: codeïne, dihydrocodeïne, tramadol, chloorfeniramine, cetirizine, salbutamol en ethanol.
- **Signalen uit de literatuur**: gevallen van toxisch megacolon bij invasieve infectieuze diarree en van ademhalingsdepressie bij een aangetaste darmbarrière (zie hierboven).

Raadpleeg voor de officiële waarschuwingen en contra-indicaties de SmPC (Samenvatting van de Productkenmerken) en de bijsluiter (PIL), aangezien deze niet in de samengestelde gegevens beschikbaar waren.

---

## Conclusie en vervolgstappen

**Besluit: Hold**

**Onderbouwing:**
- De voorspelling voor acute besmettelijke conjunctivitis is uitsluitend modelgebaseerd (L5), zonder studies, literatuur of plausibele werkingsmechanisme. De hoge score lijkt een artefact van de kennisgraaf. Voor amoebendysenterie en gastroduodenitis wijst de beschikbare literatuur op veiligheidsrisico's en niet op werkzaamheid.
- Alle Nederlandse vergunningen zijn doorgehaald, en de veiligheidsgegevens uit de SmPC ontbreken, waardoor veiligheidsscreening nog niet mogelijk is.

**Om verder te gaan is het volgende nodig:**
- SmPC/bijsluitertekst van het CBG-MEB (waarschuwingen en contra-indicaties) ophalen en verwerken.
- Gegevens over het werkingsmechanisme aanvullen vanuit DrugBank.
- Een plausibele biologische hypothese met preklinisch bewijs voordat verdere evaluatie zinvol is; gezien de oogindicatie ook een beoordeling van de toedieningsroute (lokaal oogpreparaat versus oraal).
- Een kritische heroverweging van de kennisgraafvoorspellingen voor conjunctivitis, gezien de identieke scores voor meerdere subtypen.
## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

