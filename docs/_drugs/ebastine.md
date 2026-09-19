---
layout: default
title: Ebastine
parent: Alleen modelvoorspelling (L5)
nav_order: 56
evidence_level: L5
indication_count: 2
---

# Ebastine
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **2** 
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

# Ebastine: van allergische rinitis naar coronaire hartziekte

## Samenvatting in één zin

Ebastine is een H1-receptorantagonist van de tweede generatie die klassiek wordt gebruikt voor allergische rinitis en chronische urticaria.
Het TxGNN-model voorspelt dat het effectief kan zijn voor **coronaire hartziekte**, met **0 klinische onderzoeken** en **1 computationele publicatie** die momenteel beschikbaar zijn ter ondersteuning van deze richting.
Het bewijs bevindt zich volledig op het verkennende modelleringsstadium, en de mechanistische richting van effect is niet experimenteel bevestigd.

---

## Snel overzicht

| Item | Content |
|------|---------|
| Originele indicatie | Allergische rinitis / Urticaria (H1-receptorantagonist van de tweede generatie) |
| Voorspelde nieuwe indicatie | Coronaire hartziekte |
| TxGNN-voorspellingsscore | 99.18% |
| Bewijsniveau | L5 |
| Marktstatus Nederland | Niet op de markt |
| Aantal toelassingen | 0 |
| Aanbevolen besluit | Afwachten |

---

## Waarom is deze voorspelling redelijk?

Gedetailleerde informatie over het werkingsmechanisme van Ebastine is niet beschikbaar in dit bewijspakket. Gebaseerd op vastgestelde farmacologische kennis is Ebastine een selectieve, langwerkende H1-receptorantagonist met aangetoonde anti-allergische en anti-inflammatoire eigenschappen. Net als bij andere H1-receptorantagonisten van de tweede generatie passeert het niet gemakkelijk de bloed-hersenbarrière, wat een gunstig veiligheidsprofiel voor het centraal zenuwstelsel oplevert. Naast H1-blokkade is Ebastine een bekend substraat van CYP2J2 — een cytochroom P450-isoform die sterk tot expressie komt in hartspiercellen — en deze enzymrelatie lijkt het primaire mechanistische aanknopingspunt voor TxGNN's cardiovasculaire voorspelling.

CYP2J2 katalyseert de epoxidatie van arachidonzuur in epoxyeicosatrienoïnezuren (EET's), welke endogene lipidmediatoren zijn met aangetoonde cardioprotectieve eigenschappen: zij verminderen myocardiale inflammatie, bevorderen vaatverwijding, en kunnen ischemie-reperfusieschade verzwakken via ischemische preconditioning-mechanismen. TxGNN heeft waarschijnlijk een mogelijke cardiovasculaire verbinding afgeleid door Ebastine als CYP2J2-ligand te herkennen en dit enzym aan EET-gemedieerde cardiale bescherming te koppelen. Zowel coronaire hartziekte als myocardiaal ischemie (de op één na hoogste voorspelde indicatie) staan bekend onder invloed van EET-biologie.

Echter, deze mechanistische onderbouwing draagt aanzienlijke voorbehouden met zich mee. Ebastine als CYP2J2-*substraat* zou EET-productie competitief kunnen remmen in plaats van deze te verhogen — wat zou betekenen dat het netto harteffect neutraal of zelfs schadelijk zou kunnen zijn. Er zijn geen in vitro-, diermodel- of klinische gegevens die Ebastine aan enig cardiovasculair uitkomst koppelen. De enige ondersteunende publicatie is een in silico docking-studie uit 2008 die Ebastine niet therapeutisch evalueert. Tot de richting en omvang van Ebastine's interactie met de CYP2J2–EET-as experimenteel zijn vastgesteld, moet deze voorspelling als louter hypothesegenererend worden behandeld.

---

## Bewijs uit klinische onderzoeken

Op dit moment zijn er geen gerelateerde klinische onderzoeken geregistreerd.

---

## Bewijs uit de literatuur

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|------|------|-------------|-------------|
| [18004755](https://pubmed.ncbi.nlm.nih.gov/18004755/) | 2008 | In silico / Computationele modellering | *Proteins* | Homologiemodellering en flexibele moleculaire docking van humaan CYP2J2. De studie stelt vast dat door CYP2J2 gegenereerde EET's worden geassocieerd met coronaire hartziekte, hypertensie en carcinogenese. Ebastine wordt geïdentificeerd als een ligand dat bindt aan de actieve plaats van CYP2J2, maar geen therapeutische conclusies worden getrokken. |

---

## Marktinformatie Nederland

Ebastine is **momenteel niet goedgekeurd voor commercialisering in Nederland**. Er zijn geen CBG-MEB (College ter Beoordeling van Geneesmiddelen) geregistreerde producten geïdentificeerd. Er is geen SmPC of PIL beschikbaar via het Nederlandse nationale register. Mochten klinische ontwikkelingen vorderen, dan is een toelatingsprocedure voor geneesmiddelen via CBG-MEB of de EMA-centraal procedure vereist voordat Ebastine in Nederland kan worden voorgeschreven.

---

## Veiligheidsbeschouwingen

Raadpleeg de SmPC (Samenvatting van de Productkenmerken) voor veiligheidsinformatie. Aangezien Ebastine momenteel niet in Nederland is geregistreerd, zouden artsen de goedgekeurde productinformatie uit rechtsgebieden waar Ebastine is goedgekeurd (bijv. EU-lidstaten met bestaande toelassingen) als voorlopige referentie moeten raadplegen tot een Nederlandse SmPC beschikbaar is.

---

## Conclusie en vervolgstappen

**Besluit: Afwachten**

**Onderbouwing:**
Ondanks een hoge TxGNN-voorspellingsscore van 99.18% bestaat het ondersteunend bewijs uit slechts één in silico modelleringsstudie uit 2008 zonder experimentele of klinische gegevens. De voorgestelde CYP2J2–EET-mechanistische route is biologisch aannemelijk maar volledig ongevalideerd voor Ebastine, en de richting van effect (cardioprotectief vs. remmend) blijft onbepaald. Ebastine is ook niet geregistreerd in Nederland, wat een extra regelgevingsbarrière vormt voordat enige klinische toepassing mogelijk is.

**Om verder te gaan is het volgende nodig:**

- **Verduidelijking van het mechanisme**: In vitro-onderzoeken ter meting van het effect van Ebastine op CYP2J2-enzymatische activiteit en EET-metabolietproductie (competitieve remming vs. inductie)
- **Preklinische validatie**: Diermodelgegevens ter evaluatie van cardiovasculaire uitkomsten (bijv. infarctgrootte, endotheelfunctie) in aanwezigheid van Ebastine
- **Veiligheidsprofiel review**: Opvraag en analyse van de volledige SmPC uit goedgekeurde markten — inclusief belangrijke waarschuwingen, contraïndicaties, QTc-verlenging gegevens, en geneesmiddel-geneesmiddelinteractieprofiel — voordat enige menselijke studie wordt ontworpen
- **Evaluatie van regelgevingspad**: Overleg met CBG-MEB aangaande opties voor klinische ontwikkeling of compassioneel gebruik in Nederland
- **Ontwerp van fase 1/2 klinisch onderzoek**: Minimaal een proof-of-concept-onderzoek gericht op mechanistische eindpunten (bijv. EET-niveaus in plasma, markeringen van coronaire endotheelfunctie) voordat therapeutische werkzaamheid kan worden geëvalueerd

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

