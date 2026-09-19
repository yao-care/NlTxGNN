---
layout: default
title: Lactulose
parent: Alleen modelvoorspelling (L5)
nav_order: 81
evidence_level: L5
indication_count: 8
---

# Lactulose
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

# Lactulose: Van Hepatische Encefalopatie naar Acute Uraat Nefropathie

## Samenvatting in één zin

Lactulose is een niet-absorbeerbare synthetische disaccharide met een tientallen jaren durende klinische staat van dienst in de behandeling van hepatische encefalopatie en obstipatie, werkend via osmotische effecten in het maagdarmkanaal en modulatie van de microbiota.
Het TxGNN-model voorspelt dat het mogelijk effectief kan zijn voor **Acute Uraat Nefropathie**,
echter **geen klinische onderzoeken** en **geen publicaties** ondersteunen momenteel deze specifieke indicatie — wat het bewijs plaatst op niveau **L5 (alleen modelvoorspelling)**.

---

## Snelle Samenvatting

| Item | Inhoud |
|------|--------|
| Oorspronkelijke Indicatie | Hepatische encefalopatie / Obstipatie (gevestigde klinische toepassing; geen NL registratiegegevens gevonden in deze bewijsvoering) |
| Voorspelde Nieuwe Indicatie | Acute Uraat Nefropathie |
| TxGNN Voorspellingsscore | 99.89% |
| Bewijsniveau | L5 |
| NL Marktbeschikbaarheid | Niet Geregistreerd |
| Aantal Toelatingingen | 0 |
| Aanbevolen Besluit | Wachten |

---

## Waarom is Deze Voorspelling Redelijk?

Momenteel zijn gedetailleerde werkingsmechanisme-gegevens niet beschikbaar in de bewijsvoering. Op basis van gevestigde klinische kennis is Lactulose een niet-absorbeerbare disaccharide waarvan de primaire werkingen zijn: **(1)** een osmotisch laxatief effect dat de darmdoorgang versnelt, **(2)** verzuring van de coloniale inhoud die gramnegatieve bacteriën die ammonia produceren onderdrukten, en **(3)** vermindering van de systemische endotoxinebelasting door beperking van bacteriële translokatie. Zijn werkzaamheid bij hepatische encefalopatie is bewezen en wordt bevestigd door meerdere onafhankelijke publicaties in deze bewijsvoering (bijv. PMID 9145459, PMID 28875419).

Acute uraat nefropathie is een afzonderlijke aandoening veroorzaakt door de plotselinge kristallisatie van uraat in de niertubuli — meestal geactiveerd door tumorcellysis syndroom of ernstige hyperuricemie — wat leidt tot tubulaire obstructie en acuut nierfalen. Dit mechanisme heeft geen rechtstreekse farmacologische overlap met de bekende werkingen van Lactulose.

De theoretische brug die door TxGNN wordt voorgesteld — **modificatie van de darmflora → veranderde purinemetabolisme → verminderde uraat productie** — is een uiterst indirect traject dat momenteel geen ondersteunend preklinisch of klinisch bewijs heeft. De hoge score van het model van 99.89% weerspiegelt waarschijnlijk het meest plausibel een overbegeneralisatie van de kennisgraaf tussen nierschade-knooppunten eerder dan een echt therapeutisch signaal. Deze voorspelling is consistent met een modelartefact en moet op dit moment niet prioritair worden gesteld voor klinische ontwikkeling.

---

## Klinisch Onderzoeksmateriaal

Momenteel geen gerelateerde klinische onderzoeken geregistreerd.

---

## Literatuurbewijzen

Momenteel geen gerelateerde literatuur beschikbaar.

---

## Marktinformatie Nederland

Geen CBG-MEB (College ter Beoordeling van Geneesmiddelen) markttoelatingingen voor Lactulose werden in deze bewijsvoering geïdentificeerd.

> **Belangrijk opmerking:** Lactulose is een lang gevestigd generiek geneesmiddel met wijdverbreid gebruik in heel Europa. De afwezigheid van RVG-dossiers in deze dataset is waarschijnlijk een gegevensverzamelingsgat en weerspiegelt **niet** noodzakelijk de werkelijke marktsituatie in Nederland. Voordat u regelgevingsconclusies trekt, wordt sterk aanbevolen direct verificatie via het **CBG-MEB online register** (geneesmiddeleninformatiebank.nl) en de **EMA productdatabase**. Het relevante regelgevingsdocument dat moet worden geraadpleegd, is de **SmPC (Samenvatting van de Productkenmerken)** voor het toegelaten product.

---

## Veiligheidsbeschouwingen

Raadpleeg de SmPC (Samenvatting van de Productkenmerken) voor veiligheidsinformatie.

---

## Conclusie en Volgende Stappen

**Besluit: Wachten**

**Grondslag:**
De TxGNN-voorspelling voor acute uraat nefropathie ligt op bewijsniveau L5 — met nul ondersteunende publicaties, nul klinische onderzoeken, en geen mechanistisch aannemelijk traject dat Lactulose's darmaangeslagen farmacologie verbindt met uraat-kristal nefropathie. Het vooruitgang van deze indicatie zou vereisen dat een geheel nieuw bewijs van grond af wordt opgebouwd zonder sterke wetenschappelijke grondslag om de investering te rechtvaardigen.

**Om door te gaan, is het volgende nodig:**
- Preklinische onderzoeken (dier- of in vitro) die enig effect van Lactulose op uraat metabolisme, xanthine oxidase activiteit, of renale tubulaire bescherming onder hyperuricemische omstandigheden aantonen
- Mechanistische gegevens die expliciet de modificatie van de darmflora koppelen aan purineafbraak en uraat productie
- MOA-gegevens ophaling van DrugBank (DB00581) om een volledig farmacologisch profiel vast te stellen en biologische plausibiliteit te beoordelen
- Verificatie van de werkelijke NL markttoelatingsstatus via het CBG-MEB register
- Beoordeling van de toegelaten SmPC voor contra-indicaties, waarschuwingen, en geneesmiddelinteracties voordat enig studieontwerp wordt overwogen

---

> **Contextopmerking over andere TxGNN-voorspellingen:** Hoewel dit rapport zich richt op de hoogst geclassificeerde TxGNN-voorspelling, is het belangrijk aan te geven dat andere voorspelde indicaties voor Lactulose aanzienlijk sterker bewijs hebben en beter zijn gepositioneerd voor nabije evaluatie in de Nederlandse gezondheidszorgcontext:
>
> | Rang | Indicatie | Bewijsniveau | Aanbeveling | Onderzoeken | Publicaties |
> |------|-----------|--------------|------------|-------------|-------------|
> | 3 | Obstructieve Icterus | L3 | Doorgaan met Waarborgen | 1 | 20 |
> | 4 | Galwegziekte | L3 | Onderzoeksvraag | 0 | 20 |
> | 5 | Galbewegziekte | L3 | Onderzoeksvraag | 0 | 20 |
>
> De indicatie **obstructieve icterus** (rang 3) is bijzonder opvallend: een direct klinisch onderzoek (NCT01090193) en een gerandomiseerde gecontroleerde multicentrische studie uit 1991 (PMID 2032107) bestaan, en de mechanistische basis — Lactulose vermindert perioperatieve endotoxemie en postoperatief nierfalen bij gele niergebrekkige chirurgische patiënten — is goed beschreven. Een afzonderlijk, gericht rapport voor die indicatie wordt aanbevolen als de volgende stap.

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

