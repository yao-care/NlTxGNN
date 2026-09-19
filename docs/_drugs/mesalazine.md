---
layout: default
title: Mesalazine
parent: Alleen modelvoorspelling (L5)
nav_order: 93
evidence_level: L5
indication_count: 7
---

# Mesalazine
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

# Mesalazine: van inflammatoire darmziekten naar congenitale hypotrichosis met juveniele maculaire dystrofie

## Samenvatting in één zin

Mesalazine (5-aminosalicylzuur, 5-ASA) is een goed gevestigd ontstekingsremmend geneesmiddel dat decennialang wordt gebruikt voor de behandeling van inflammatoire darmziekten, met name ulcereuze colitis. De best gerangschikte voorspelling van het TxGNN-model is **congenitale hypotrichosis met juveniele maculaire dystrofie** met een score van 99,65%, maar deze richting wordt momenteel ondersteund door **geen klinische onderzoeken** en **geen gepubliceerde literatuur**. De hoge modelscore is waarschijnlijk een artefact van de topologie van de kennisgraaf in plaats van een echt farmacologisch signaal, en een Hold-besluit is gerechtvaardigd voor deze specifieke indicatie.

---

## Snelle samenvatting

| Item | Inhoud |
|------|--------|
| Originele indicatie | Inflammatoire darmziekten (ulcereuze colitis) |
| Voorspelde nieuwe indicatie | Congenitale hypotrichosis met juveniele maculaire dystrofie |
| TxGNN-voorspellingsscore | 99,65% |
| Bewijsniveau | L5 |
| Nederlandse marktpositie | Geen CBG-MEB-autorisaties gevonden in huige gegevens |
| Aantal autorisaties | 0 |
| Aanbevolen besluit | Hold |

---

## Waarom is deze voorspelling redelijk?

Momenteel zijn gedetailleerde gegevens over het werkingsmechanisme niet beschikbaar in deze evidence pack. Op basis van bekende farmacologie is Mesalazine (5-ASA) het actieve ontstekingsremmende bestanddeel van sulfasalazine. Het werkt vooral door inhibitie van de NF-κB-signaalroute, onderdrukking van prostaglandine- en leukotrienesynthese, en vangen van reactieve zuurstofsoorten — vooral op mucosale oppervlakken in het maagdarmkanaal. De werkzaamheid ervan bij inflammatoire darmziekten is in talrijke klinische onderzoeken over verschillende decennia gevalideerd.

Congenitale hypotrichosis met juveniele maculaire dystrofie (CHIJMD) is een zeldzaam autosomaal recessief aandoening veroorzaakt door mutaties in het *LIPA*-gen (lysosomale lipase A). De ziekte manifesteert zich als progressief haarverlies en vroeg optredende maculaire degeneratie. Kritiek punt is dat de onderliggende pathologie **structureel en genetisch** van aard is — aangedreven door lysosomale enzymdeficiëntie en lipideaccumulatie — en **niet primair door ontstekking wordt gemedieerd**. Er is geen ingestelde biologische route die Mesalazine's ontstekingsremmende werkingsmechanisme verbindt met de *LIPA*-genroute of met de structurele integriteit van het netvlies/haarzakjes.

De hoge voorspellingsscore van het TxGNN-model (99,65%) voor deze indicatie weerspiegelt waarschijnlijk gedeelde verbindingen op graafniveau in de kennisgraaf — zoals "huid" of "oogheelkunde" ziekteknopen — in plaats van een echt farmacologisch grondslag. Deze voorspelling moet worden behandeld als een computersignaal dat biologische validatie vereist voordat verdere investeringen worden gedaan. Er is geen mechanistische rechtvaardiging voor het verder gaan op dit moment.

---

## Bewijs uit klinische onderzoeken

Momenteel geen gerelateerde klinische onderzoeken geregistreerd.

---

## Bewijs uit literatuur

Momenteel geen gerelateerde literatuur beschikbaar.

---

## Informatie Nederlandse markt

Geen CBG-MEB-marketingautorisaties zijn geregistreerd in de huige evidence pack voor Mesalazine in Nederland. De evidence pack bevat kandidaat-ID `TW-DB00244-multi`, wat aangeeft dat het regelgevingsgegevensveld werd gevuld met Taiwan (TFDA) gegevens in plaats van Nederlandse CBG-MEB-registergegevens.

> ⚠️ **Belangrijk:** Mesalazine is een veelgebruikt geneesmiddel waarvan wordt verwacht dat het CBG-MEB-autorisaties in Nederland draagt (bijvoorbeeld onder merknamen als Pentasa, Asacol, of Salofalk). Een rechtstreekse opvraag bij het CBG-MEB-register is vereist om de werkelijke Nederlandse marktpositie te bevestigen voordat regelgevingsconclussies worden getrokken.

---

## Veiligheidsoverwegingen

Raadpleeg de SmPC (Samenvatting van de Productkenmerken) voor veiligheidsinformatie. Geen belangrijke waarschuwingen, contra-indicaties, of geneesmiddelinteractiegegevens waren beschikbaar in de huige evidence pack.

> ⚠️ Ophalen van de Nederlandse SmPC wordt geclassificeerd als een **Blokkerende** gegevenslacune (DG001) — veiligheidsevaluatie kan niet plaatsvinden totdat dit document wordt verkregen van het CBG-MEB of via de productinformatieportal van het EMA.

---

## Conclusie en vervolgstappen

**Besluit: Hold**

**Rationale:**
De best gerangschikte TxGNN-voorspelling voor Mesalazine — congenitale hypotrichosis met juveniele maculaire dystrofie — heeft geen ondersteunende klinische onderzoeken, geen gepubliceerde literatuur, en geen aannemelijk mechanistisch verband. De *LIPA*-gen-aangedreven structurele ziektepatologie is fundamenteel onverenigbaar met Mesalazine's ontstekingsremmende werkingsmechanisme, waardoor dit een L5-computersignaal is dat niet voldoet aan de drempel voor verdere evaluatie op dit moment.

**Om verder te gaan, is het volgende nodig:**

- **CBG-MEB-registeropvraag**: Bevestig de werkelijke Nederlandse marketingautorisatiestatus voor alle Mesalazine-formuleringen (lost de regelgevingsgegevenslacune op)
- **SmPC-ophaling**: Verkrijg de nu geldende Nederlandse SmPC om belangrijke waarschuwingen, contra-indicaties, en geneesmiddelinteractie-evaluatie te voltooien (lost DG001 — Blokkerende lacune op)
- **Mechanistische voorscreening**: Als enig nieuw bewijs opduikt dat Mesalazine aan lysosomale lipasebiologie of retinale/folliculaire structurele routes bindt, heroverweeg de bruikbaarheid van de voorspelling
- **Overweeg alternatieve indicaties**: De evidence pack bevat twee andere voorspellingen met sterker biologisch bewijs — **osteoartritis** (rang 2, L4, 1 × 2024 Nature Communications preklinisch onderzoek via OSCAR-PPARγ-as) en **reumatoïde artritis** (rang 3, L3, historisch Sulfasalazine DMARD-bewijs) — die geschiktere kandidaten kunnen zijn voor specifieke evaluatierapporten voor geneesmiddelherbestemming

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

