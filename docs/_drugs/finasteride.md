---
layout: default
title: Finasteride
parent: Alleen modelvoorspelling (L5)
nav_order: 69
evidence_level: L5
indication_count: 6
---

# Finasteride
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **6** 
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

# Finasteride: Van androgenetische alopecia/BPH naar Ambras Type Hypertrichosis Universalis Congenita

## Samenvatting in één zin

Finasteride is een 5-alfa-reductase-remmer met gevestigde klinische toepassing bij benigne prostaataandoening (BPH) en mannelijk patroonhaaruitval (androgenetische alopecia), werkend door dihydrotestosteron (DHT)-spiegels te verlagen.
Het TxGNN-model voorspelt dat het effectief kan zijn voor **Ambras Type Hypertrichosis Universalis Congenita**, een zeldzame aangeboren aandoening met overmatige haargroei gekoppeld aan TRPS1-gen-herschikkingen,
met **0 klinische trials** en **0 publicaties** die deze specifieke toepassing ondersteunen — bewijsniveau L5.

---

## Beknopt overzicht

| Item | Inhoud |
|------|--------|
| Oorspronkelijke indicatie | Benigne prostaataandoening (BPH); mannelijk patroonhaaruitval (androgenetische alopecia) |
| Voorspelde nieuwe indicatie | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN-voorspellingsscore | 99.99% |
| Bewijsniveau | L5 |
| NL-marktsstatus | Niet geregistreerd (CBG-MEB-gegevens: 0 toestemmingen gevonden) |
| Aantal toestemmingen | 0 |
| Aanbevolen besluit | In afwachting |

---

## Waarom is deze voorspelling redelijk?

Gedetailleerde gegevens over het werkingsmechanisme zijn momenteel niet beschikbaar in dit Evidence Pack. Op basis van goed gevestigde farmacologische kennis is finasteride een competitieve remmer van 5-alfa-reductase (isovormen type 1 en 2), het enzym dat testosteron in het potentere androgeen dihydrotestosteron (DHT) omzet. Door DHT-concentraties in weefsels te verlagen, onderdrukt finasteride androgeen-gestuurde verkleining van haarvollicels bij androgenetische alopecia en vermindert het prostaatcelproliferatie bij BPH. De werkzaamheid bij androgeen-afhankelijke aandoeningen is farmacologisch goed gekarakteriseerd.

Ambras Type Hypertrichosis Universalis Congenita is echter een onderscheidende biologische entiteit. Het wordt veroorzaakt door chromosoomherschikkingen op 8q22–24 die de transcriptiefactor TRPS1 dysreguleren, wat leidt tot gegeneraliseerde, dichte hypertrichose aanwezig vanaf de geboorte. Deze aandoening is **niet androgeen-afhankelijk**: het pathomechanisme betreft onevenwichtigheid van transcriptiefactoren in plaats van overmatige DHT-signalering. Het primaire werkingsmechanisme van finasteride — DHT-onderdrukking — mist daarom een duidelijke farmacologische onderbouwing voor het omkeren of moduleren van dit aangeboren fenotype.

De zeer hoge score van het TxGNN-model (0.9999) weerspiegelt vrijwel zeker de topologische nabijheid van de bekende haarziekteknopen van finasteride tot hypertrichose-ziekteknopen binnen de kennisgraaf, in plaats van een echte mechanistische link. Dit is een goed erkende beperking van op grafen gebaseerde herbestemmingsmodellen: zeldzame aangeboren aandoeningen die brede fenotypische labels (bijv. "haarziekte") delen met goed bestudeerde medicijnendoelen kunnen hoge scores genereren zonder betekenisvolle biologische overlap. Bij afwezigheid van enig preklinisch of klinisch bewijs moet deze voorspelling als zuiver computationele hypothese worden beschouwd en is **niet klaar voor klinische toepassing**.

---

## Bewijs uit klinische trials

Er zijn momenteel geen gerelateerde klinische trials geregistreerd.

---

## Bewijs uit literatuur

Momenteel is geen gerelateerde literatuur beschikbaar.

---

## Marktinformatie Nederland

Er zijn geen CBG-MEB-marketingtoestemmingsregisters gevonden voor Finasteride in deze dataset. Dit kan een gegevensophaalleemte aangeven in plaats van werkelijke afwezigheid op de Nederlandse markt — Finasteride-producten (bijv. Propecia 1 mg voor androgenetische alopecia en Proscar 5 mg voor BPH) zijn EMA-goedgekeurd en hebben naar verwachting nationale registratie of wederzijdse erkenningsprocedure in Nederland.

**Actie vereist:** Controleer de huidige NL-toestemmingsstatus rechtstreeks via de [CBG-MEB Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/) of de [EMA-medicijnendatabase](https://www.ema.europa.eu/en/medicines).

---

## Veiligheidsoverwegingen

Raadpleeg de SmPC (Samenvatting van de Productkenmerken) voor volledige veiligheidsinformatie. Geen veiligheidsgegevens — inclusief waarschuwingen, contra-indicaties of geneesmiddelinteracties — waren beschikbaar in dit Evidence Pack.

> Voor EMA-goedgekeurde producten is de SmPC toegankelijk via de [EMA-medicijnendatabase](https://www.ema.europa.eu/en/medicines). Voor nationaal goedgekeurde producten kan de SmPC worden verkregen van de CBG-MEB.

---

## Conclusie en vervolgstappen

**Besluit: In afwachting**

**Onderbouwing:**
Ambras Type Hypertrichosis Universalis Congenita is een TRPS1-gemedieerde aangeboren aandoening zonder gevestigde verbinding met DHT-signalering of androgeen-pathway's. De TxGNN-voorspelling (L5) wordt volledig niet ondersteund door enige klinische trial, preklinische studie of gepubliceerde literatuur, en de hoge modelscore weerspiegelt hoogstwaarschijnlijk een kennisgraaf-topologie-artefact in plaats van een farmacologisch geldige aanwijzing.

**Om verder te gaan is het volgende nodig:**

- **Mechanistische validatie:** Vakblokgerefereerde bewijzen dat aantonen dat DHT of 5-alfa-reductase-activiteit een rol speelt in TRPS1-gerelateerde dysfunctie van haarvollicels
- **Preklinische studies:** In vitro- of in vivo-gegevens die finasteride-activiteit aantonen in relevante modellen voor aangeboren hypertrichose
- **CBG-MEB / EMA-toestemmingscontrole:** Bevestig huidige NL-marktsstatus en haal de volledige SmPC op voor veiligheidsprofiel
- **MOA-gegevenslacune sluiten:** Haal volledige DrugBank-entry (DB01216) op om werkingsmechanisme- en veiligheidsvelden in te vullen voor een juiste S1-niveau veiligheidsevaluatie
- **Regelgevingsbeoordeling:** Als mechanistische bewijzen opduiken, raadpleeg CBG-MEB-richtlijnen voor off-label gebruik of wees-aanwijzingspaden, gezien de ultra-zeldzame aard van deze aandoening

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

