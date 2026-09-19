---
layout: default
title: Ibuprofen
parent: Alleen modelvoorspelling (L5)
nav_order: 77
evidence_level: L5
indication_count: 7
---

# Ibuprofen
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **7** 
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

# Ibuprofen: Van analgeeticum/anti-inflammatoir tot Acromesomale Dysplasie, Hunter-Thompson type

## Samenvatting in één zin

Ibuprofen is een goed ingeburgerd niet-steroïdaal anti-inflammatoir geneesmiddel (NSAID), veel gebruikt voor pijnverlichting, koortsverlaging en ontstekingsaandoeningen zoals artritis. Het TxGNN-model voorspelt dat het effectief kan zijn voor **Acromesomale Dysplasie, Hunter-Thompson type** — een zeldzame autosomaal recessive skeletale dysplasie veroorzaakt door GDF5/CDMP1 verlies-van-functie mutaties — met **0 klinische onderzoeken** en **0 publicaties** die deze richting momenteel ondersteunen. Deze voorspelling steunt geheel op netwerktopologie en wordt vooralsnog niet ondersteund door enig klinisch of preklinisch bewijs.

---

## Snel Overzicht

| Item | Inhoud |
|------|--------|
| Originele Indicatie | Niet beschikbaar in het CBG-MEB register (geen NL autorisaties gevonden in dataset) |
| Voorspelde Nieuwe Indicatie | Acromesomale Dysplasie, Hunter-Thompson type |
| TxGNN Voorspellingsscore | 99.74% |
| Bewijsniveau | L5 |
| Status op Nederlandse Markt | Niet geregistreerd (geen CBG-MEB RVG autorisaties gevonden) |
| Aantal Autorisaties | 0 |
| Aanbevolen Besluit | Uitstel |

---

## Waarom is deze voorspelling redelijk?

Gedetailleerde gegevens over het werkingsmechanisme waren niet beschikbaar in dit bewijsmateriaal. Op basis van gevestigde farmacologische kennis is Ibuprofen een typisch NSAID dat beide COX-1 en COX-2 cyclo-oxygenase enzymen remt, waardoor de synthese van prostaglandines wordt onderdrukt. Dit resulteert in analgetische, anti-pyretische en anti-inflammatoire effecten. De bekende klinische toepassingen zijn onder meer musculoskeletale pijn, dysmenorroe, koorts en inflammatoire artropathieën.

Acromesomale dysplasie, Hunter-Thompson type is een uiterst zeldzame aangeboren skeletale dysplasie veroorzaakt door verlies-van-functie mutaties in het GDF5-gen (ook bekend als CDMP1). GDF5 is een lid van de bone morphogenetic protein (BMP) familie die een kritieke rol speelt in chondrocytendifferentiatie en langbeentwikkeling. De theoretische mechanische link is dat PGE2 — een downstream product van COX-2 — BMP-signalering in chondrocyten moduleert. In principe zou COX-2-remming door Ibuprofen PGE2-gemedieerde BMP-padactiviteit in kraakbeen kunnen veranderen.

Echter, de mechanische link wordt beoordeeld als uiterst zwak en richtingonzeker. Remming van COX-2/PGE2 zou tegelijkertijd lokale ontsteking kunnen verminderen en interfereren met residuele GDF5-afhankelijke beentwikkelingssignalering — tegengestelde effecten die het netto klinische resultaat onvoorspelbaar maken. Dit is een aangeboren structurale aandoening veroorzaakt door een genetische afwijking; het is geen verworven ontstekingsaandoening. De hoge TxGNN-score weerspiegelt waarschijnlijk eerder grafieknetwerktopologische nabijheid tot andere musculoskeletale aandoeningen waarin Ibuprofen een gevestigde werking heeft, in plaats van een echte op mechanisme gebaseerde hergebruikingskans. Alle 7 TxGNN-voorspelde indicaties voor Ibuprofen in deze dataset hebben hetzelfde patroon: zeldzame skeletale of ontwikkelingsdysplasieën met L5-bewijs en aanbevelingen voor uitstel.

---

## Bewijs uit Klinische Onderzoeken

Op dit moment zijn er geen gerelateerde klinische onderzoeken ingeschreven.

---

## Bewijs uit Literatuur

Op dit moment is er geen gerelateerde literatuur beschikbaar.

---

## Informatie over de Nederlandse Markt

Er zijn geen CBG-MEB RVG autorisaties voor Ibuprofen gevonden in de huidige dataset.

> **Belangrijke opmerking**: Dit weerspiegelt waarschijnlijk een lacune in gegevensverzameling in de regelgevingspijplijn in plaats van werkelijke afwezigheid op de NL markt. Ibuprofen is een veel geautoriseerd OTC- en receptgeneesmiddel in de gehele EU. Verifieer alstublieft de huidige autorisatie en RVG-status rechtstreeks via het [CBG-MEB openbare register](https://www.cbg-meb.nl/) of de [EMA productendatabase](https://www.ema.europa.eu/) voordat u conclusies trekt over beschikbaarheid op de NL markt.

---

## Veiligheidsoverwegingen

Raadpleeg alstublieft de SmPC (Samenvatting van productkenmerken) voor veiligheidsinformatie.

---

## Conclusie en Vervolgstappen

**Besluit: Uitstel**

**Reden:**
Ondanks een hoge TxGNN-voorspellingsscore (99.74%) is acromesomale dysplasie, Hunter-Thompson type een aangeboren skeletale dysplasie veroorzaakt door een specifieke genetische afwijking in het GDF5/BMP-pad. De mechanische verbinding met Ibuprofens COX-2-remmingsmechanisme is speculatief, richtingonzeker en geheel niet ondersteund door enig klinisch onderzoek, observatiegegevens of gepubliceerde literatuur (L5 — alleen modelvoorspelling). Het voortzetten zonder basiswetenschappelijk bewijs zou niet voldoen aan CBG-MEB- of EMA-normen voor hergebruiking.

**Om door te gaan is het volgende nodig:**

- **Verificatie regelgevingsgegevens**: Verkrijg werkelijke CBG-MEB RVG autorisatierecords en SmPC voor Ibuprofen om de regelgevingsbasis voor NL vast te stellen
- **MOA gegevens uit DrugBank**: Query DrugBank API (DB01050) om het volledige werkingsmechanisme en doelinteractieprofiel te verkrijgen om de COX-2 / GDF5-BMP-padhypothese formeel te beoordelen
- **Veiligheidsgegevens**: Verkrijg volledige SmPC waarschuwingen, contra-indicaties en geneesmiddelinteractiegegevens voordat verdere evaluatiestadia worden ondernomen
- **Preklinisch bewijs**: Identificeer of commissie celgebaseerde of diermodellenstudies die COX-2-remming in GDF5-deficiënte skeletmodellen onderzoeken; zonder dit kan biologische aannemelijkheid niet worden vastgesteld
- **Deskundige raadpleging**: Betrek specialisten in skeletdysplasieën en een klinisch farmacoloog om te beoordelen of anti-inflammatoire interventie enige ziekteveranderende rol zou kunnen hebben in deze aangeboren aandoening
- **Herziening van alle 7 voorspellingen**: Alle TxGNN-voorspelde indicaties voor dit geneesmiddel zijn zeldzame skelet-/ontwikkelingsdysplasieën op L5 zonder ondersteunend bewijs — een systematische beoordeling van de volledige voorspellingsverzameling wordt aanbevolen om vast te stellen of er een hoger-prioriteit hergebruikingssignaal bestaat in het bredere ziektennetwerk van Ibuprofen.

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

