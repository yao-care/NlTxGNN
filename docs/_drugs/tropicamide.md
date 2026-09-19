---
layout: default
title: Tropicamide
parent: Alleen modelvoorspelling (L5)
nav_order: 122
evidence_level: L5
indication_count: 3
---

# Tropicamide
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

# Tropicamide: Van Oogheelkunde (Mydriasis) naar Cauda Equina Syndroom

## Samenvatting in Één Zin

Tropicamide is een goed gevestigde antimuscarinerge (anticholinerge) stof, vooral gebruikt in de oogheelkunde om pupilverwijding (mydriasis) en tijdelijke accommodatieverlammung (cycloplegia) tijdens oogonderzoeken op te wekken. Het TxGNN-model voorspelt dat het mogelijk effectief kan zijn voor **Cauda Equina Syndroom**, hoewel momenteel **0 klinische onderzoeken** en **0 publicaties** deze richting ondersteunen.

---

## Snel Overzicht

| Item | Inhoud |
|------|--------|
| Oorspronkelijke Indicatie | Geen CBG-MEB-registratie bekend; klassiek gebruikt voor oogheelkundige mydriasis/cycloplegia |
| Voorspelde Nieuwe Indicatie | Cauda Equina Syndroom |
| TxGNN Voorspellingsscore | 99.53% |
| Bewijsniveau | L5 (alleen modelvoorspelling, geen ondersteunende studies) |
| NL-Marktpositie | Niet geregistreerd |
| Aantal Autorisaties | 0 |
| Aanbevolen Besluit | Aanhouden |

---

## Waarom is Deze Voorspelling Redelijk?

Op dit moment zijn gedetailleerde mechanisme-van-werking gegevens niet beschikbaar in het Evidence Pack. Op basis van gevestigde farmacologische kennis is tropicamide een competitieve antagonist van muscarinerge acetylcholine-receptoren — met name M3 en M4-subtypen. Bij topicale toediening in het oog ontspant deze antimuscarinerge werking de irissluitspier en ciliairspier, wat mydriasis en cycloplegia teweegbrengt. Buiten de oogheelkunde zijn antimuscarinerge middelen farmacologisch actief in het autonoom zenuwstelsel, waar zij de gladde spiertoon in de blaas, darm en andere viscerale organen beïnvloeden.

Cauda equina syndroom (CES) is een ernstige neurologische noodsituatie veroorzaakt door compressie van het lumbosacraal zenuwortelwantje. Een kenmerkend kenmerk van CES is verstoring van de autonome banen die mictie (urinelozing), defecatie en geslachtsfunctie reguleren — gebieden waar muscarinerge receptormodulatie juist farmacologisch relevant is. Anticholinerge geneesmiddelen zijn al gevestigd bij het beheer van neurogene blaasdisfunctie, een frequent gevolg van CES. TxGNN kan daarom een mechanistische overlap detecteren tussen het receptorprofiel van tropicamide en de autonome dysfunctiecomponent van CES, eerder dan een direct effect op zenuwortelcompressie zelf.

Dat gezegd hebbende, CES is primair een structurele/chirurgische aandoening: zenuworteldecompressie blijft de hoeksteen van de behandeling. Het nut van tropicamide zou op zijn best de symptomatische autonome complicaties aanpakken in plaats van de onderliggende pathologie. De hoge TxGNN-score weerspiegelt waarschijnlijk een graph-neighbourhood-associatie door gedeelde autonome-pathway-knooppunten. Zonder klinische bewijzen moet deze voorspelling alleen als een hypothesis-generatief signaal worden behandeld.

---

## Bewijsvoering uit Klinische Onderzoeken

Op dit moment zijn geen gerelateerde klinische onderzoeken geregistreerd.

---

## Bewijsvoering uit Literatuur

Op dit moment is geen gerelateerde literatuur beschikbaar.

---

## Nederlands Marktinformatie

Tropicamide heeft momenteel geen verkoopvergunningen van de CBG-MEB (College ter Beoordeling van Geneesmiddelen) en is volgens dit Evidence Pack niet commercieel verkrijgbaar op de Nederlandse markt. Er zijn geen RVG-nummers geregistreerd.

> **Opmerking voor beoordelaars:** Oogheelkundige tropicamideoplossingen zijn ruim verspreid geautoriseerd in EU-lidstaten onder verschillende merknamen. Een gerichte zoeken in het CBG-MEB-register wordt aanbevolen om te verifiëren of er wederzijdse erkennings- of gedecentraliseerde procedureautorisaties bestaan die mogelijk nog niet in deze dataset zijn vastgelegd.

---

## Veiligheidsoverwegingen

Raadpleeg de SmPC (Samenvatting van Productkenmerken) voor veiligheidsinformatie. Belangrijke waarschuwingen, contraïndicaties en geneesmiddel-interactiegegevens zijn niet beschikbaar in het huidige Evidence Pack en moeten worden opgehaald uit het CBG-MEB/EMA-productdossier of TFDA SmPC PDF voordat deze kandidaat naar een formele veiligheidscreeningsfase kan gaan.

---

## Conclusie en Vervolgstappen

**Besluit: Aanhouden**

**Motivering:**
De bewijsbasis bevindt zich op niveau L5 — de laagste schaal, bestaande uit alleen een TxGNN-modelvoorspelling zonder ondersteunende klinische onderzoeken of gepubliceerde literatuur. Gecombineerd met nul Nederlandse marktautorisaties en onopgeloste gegevenslacunes in zowel werkingsmechanisme als veiligheidsgegevens, is er onvoldoende informatie om enige verdere aanbeveling in dit stadium te ondersteunen.

**Om voort te gaan, is het volgende nodig:**

- **MOA-verificatie:** Haal volledige DrugBank-vermelding (DB00809) op om receptordoelen, farmacodynamica en bekende off-target effecten te bevestigen
- **SmPC-beoordeling:** Download en bestudeer de relevante SmPC (EMA of nationale CBG-MEB) voor belangrijke waarschuwingen, contraïndicaties en voorzorgsmaatregelen voor speciale populaties
- **DDI-beoordeling:** Doorzoek drug-interactiedatabases opnieuw zodra SmPC-gegevens beschikbaar zijn
- **Indicatieverduidelijking:** Verduidelijk of de TxGNN-voorspelling gericht is op CES zelf, of op zijn autonome gevolgen (bijv. neurogene blaas); laatstgenoemde heeft veel sterker farmacologische aannemelijkheid
- **Gericht literatuuronderzoek:** Verbreed PubMed-query voorbij exacte ziektematching — zoeken naar "tropicamide autonomic neuropathy", "anticholinergic neurogenic bladder cauda equina" en gerelateerde termen
- **NL-marktstatusverificatie:** Bevestig via het openbare CBG-MEB-register of oogheelkundige tropicamideproducten een RVG-nummer hebben onder wederzijdse erkenningsprocedures

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

