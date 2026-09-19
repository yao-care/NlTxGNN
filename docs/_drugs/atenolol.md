---
layout: default
title: Atenolol
parent: Alleen modelvoorspelling (L5)
nav_order: 27
evidence_level: L5
indication_count: 9
---

# Atenolol
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **9** 
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

# Atenolol: Van hypertensie/angina naar posteroinferior myocardinfarct

## Samenvatting in één zin

Atenolol is een cardioselectieve β1-adrenerge blokker die veel wordt gebruikt voor de behandeling van hypertensie, angina pectoris en cardiale aritmieën. Het TxGNN-model voorspelt dat het mogelijk effectief is voor **posteroinferior myocardinfarct**, met **0 klinische trials** en **1 publicatie** die deze specifieke anatomische subtype ondersteunen, hoewel β-blokkers goed gevestigd zijn in de bredere infarctbehandeling. Over alle 9 voorspelde indicaties heeft de sterkste bewijsbasis betrekking op **chronische longhartziekten** (1 klinische trial, 15 publicaties), hoewel die indicatie aanzienlijke mechanistische bezwaren met zich meebrengt.

---

## Sneloverblick

| Item | Inhoud |
|------|--------|
| Bestaande indicatie | Hypertensie, angina pectoris, cardiale aritmieën (goed gevestigde β-blokker) |
| Voorspelde nieuwe indicatie | Posteroinferior myocardinfarct |
| TxGNN-voorspellingsscore | 99,87% |
| Evidentienivelau | L4 (Preclinische/mechanisme-onderzoeken) |
| Marktstatus in Nederland | Niet gevonden in evidentiebundel (Opmerking: Atenolol is widely beschikbaar in Nederland onder meerdere CBG-MEB-toestemmingen — zie afdeling hieronder) |
| Aantal toestemmingen | 0 in huidige dataset (regelgevingslacune) |
| Aanbevolen besluit | Doorgaan met waarborgen |

---

## Waarom is deze voorspelling redelijk?

Atenolol is een selectieve β1-adrenerge receptorantagonist. Het werkt door β1-receptoren competitief te blokkeren die voornamelijk in het hart liggen, waardoor het hartritme, myocardiale contractiliteit en myocardiale zuurstofvraag afnemen. Deze eigenschappen vormen de basis van het langdurige gebruik tegen hypertensie, stabiele angina en secundaire preventie na myocardinfarct (MI). Atenolol heeft geen intrinsieke sympathomimetische activiteit (ISA), wat het geschikt maakt voor het verminderen van sympathische overbelasting bij acute coronaire ereignissen.

Posteroinferior myocardinfarct is een anatomische subtype van MI dat de achter- en onderwanden van de linker ventrikel aantast, meestal veroorzaakt door occlusie van de rechter coronairarterie of de linker circumflex arterie. β-blokkers, inclusief atenolol, maken al deel uit van standaardprotocollen voor secundaire preventie van MI volgens ESC- en AHA/ACC-richtlijnen. De TxGNN-voorspelling identificeert in wezen dat het bestaande farmacologische mechanisme volledig van toepassing is op deze anatomische subtype — een logische uitbreiding gegeven dat β-blokkercardioprotectie (vermindering van infarctgrootte, preventie van reinfarctie en vermindering van plotselinge cardiache dood) niet afhankelijk is van infarctlocatie.

Het is echter belangrijk op te merken dat posteroinferior MI vaak de rechter ventrikel en het cardiale geleidingssysteem (vooral de AV-knoop) betreft, wat betekent dat β-blokkage extra voorzichtigheid vereist. Bradycardie, AV-blokade en rechterventriculaire disfunctie zijn specifieke risico's in deze patiëntenpopulatie, en klinische monitoring moet intensiever zijn dan bij anterieur MI.

---

## Bewijs uit klinische trials

Er zijn momenteel geen klinische trials die specifiek atenolol voor posteroinferior myocardinfarct onderzoeken ingeschreven.

**Opmerking:** Hoewel geen trials gericht zijn op deze specifieke anatomische subtype, is atenolol uitgebreid bestudeerd in de bredere MI-context. De baanbrekende ISIS-1-trial (1986) toonde een vermindering van 15% in vasculaire mortaliteit met vroeg IV atenolol bij acuut MI. De volgende trial uit een gerelateerde voorspelde indicatie (chronische longhartziekten) biedt indirecte context:

| Trialnummer | Fase | Status | Inschrijving | Belangrijkste bevindingen |
|---------|------|--------|------|---------|
| [NCT03278509](https://clinicaltrials.gov/study/NCT03278509) | Fase 4 | Actief, niet rekruterend | 5.000 | REDUCE-SWEDEHEART: Evalueert of langdurige β-blokker therapie na MI met behouden LVEF alle-oorzaken mortaliteit of nieuw MI vermindert. Resultaten kunnen de rol van β-blokkers in MI-subtypes informeren. |

---

## Literatuurbewijs

### Primaire indicatie: Posteroinferior myocardinfarct

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|-----|------|------|---------|
| [3901170](https://pubmed.ncbi.nlm.nih.gov/3901170/) | 1985 | Crossover RCT | Rev Med Interne | Vergeleek anti-ischemische effecten van atenolol (200 mg) vs diltiazem (240 mg) in 23 patiënten met resterende ischemie 4 weken na posteroinferior of anterieur MI. Gebruikte gecomputeriseerde inspanningstesting. |

### Gerelateerde indicatie: Septaal myocardinfarct (Rang 7)

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|-----|------|------|---------|
| [7257500](https://pubmed.ncbi.nlm.nih.gov/7257500/) | 1981 | Diagnostische studie | Z Kardiol | Bestudeerde veranderingen in regionale myocardiale perfusie met 201-Tl-stressafbeelding in 14 patiënten vóór en na IV atenolol (5 mg). Evalueerde perfusie in 6 LV-segmenten inclusief het septale gebied. |

### Gerelateerde indicatie: Chronische longhartziekten (Rang 9, meeste literatuur)

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|-----|------|------|---------|
| [31524](https://pubmed.ncbi.nlm.nih.gov/31524/) | 1978 | Klinische studie | Lille Med | Bestudeerde effecten van atenolol bij chronische longpatiënten met luchtwegobstructie. |
| [6673339](https://pubmed.ncbi.nlm.nih.gov/6673339/) | 1983 | Klinische studie | Vutreshni Bolesti | Vergeleek β-blokkers in COPD-patiënten met gelijktijdige ischemische hartziekten gedurende 14 dagen. |
| [14520850](https://pubmed.ncbi.nlm.nih.gov/14520850/) | 2003 | Vergelijkende studie | Ter Arkh | Vergeleek werkzaamheid en veiligheid van atenolol, metoprolol en bisoprolol in geïsoleerde systolische hypertensie met gelijktijdige diabetes en/of COPD. |
| [15881093](https://pubmed.ncbi.nlm.nih.gov/15881093/) | 2005 | Klinische studie | Ter Arkh | Onderzocht respiratoire aandoeningen in IHD-patiënten met COPD die langdurig atenolol gebruikten. |
| [28982831](https://pubmed.ncbi.nlm.nih.gov/28982831/) | 2017 | Observationeel | BMJ Open | Retrospectieve cohortsstudie in de bevolking over astma-COPD-overlapsyndroom en cardiovasculaire ziekteassociaties. |

---

## Marktinformatie Nederland

De huidige evidentiebundel bevat geen CBG-MEB-regelgevingsgegevens. Echter, atenolol is een goed gevestigd geneesmiddel dat wijd beschikbaar is in Nederland onder meerdere verkooptoestemmingen. Het is geregistreerd in orale formuleringen (tabletten 25 mg, 50 mg, 100 mg) en wordt al decennia in de EU op de markt gebracht.

> **Datalacune:** CBG-MEB-licentiedetails waren niet opgenomen in deze evidentiebundel. Om dit gedeelte compleet te maken, moeten CBG-MEB-autorisatiegegevens worden opgehaald uit de Geneesmiddeleninformatiebank (GIB) op [https://www.geneesmiddeleninformatiebank.nl](https://www.geneesmiddeleninformatiebank.nl).

---

## Veiligheidsoverwegingen

> Raadpleeg de SPC (Samenvatting van de Productkenmerken) voor volledige veiligheidsinformatie.

**Belangrijkste klinische overwegingen voor posteroinferior MI:**

- **AV-geleiding:** Posteroinferior MI betreft vaak de AV-knoop (gevoed door de achter afdalende arterie). Atenolol kan AV-blokade verergeren bij deze patiënten. ECG-monitoring is essentieel vóór en tijdens behandeling.
- **Rechterventriculaire betrokkenheid:** Inferieur MI kan zich uitbreiden naar de rechter ventrikel. β-blokkers kunnen de voorbellasting afhankelijke cardiale output in RV-infarctie verminderen, waardoor mogelijk hemodynamische verslechtering optreedt.
- **Bradycardie:** Patiënten met inferieur MI zijn vatbaar voor vagaal-gemedieerde bradycardie. Het negatieve chronotrope effect van atenolol kan dit risico verergeren.
- **Bronchospasme:** Hoewel β1-selectief, neemt de selectiviteit van atenolol af bij hogere doses. Patiënten met gelijktijdige reactieve luchtwegziekte moeten worden bewaakt.

---

## Overzicht van alle voorspelde indicaties

| Rang | Voorspelde indicatie | TxGNN-score | Evidentienivelau | Aanbeveling | Belangrijkste bezorgdheid |
|------|---------------------|-------------|---------------|----------------|-------------|
| 1 | Posteroinferior myocardinfarct | 99,87% | L4 | Doorgaan met waarborgen | AV-blokaderisico; sterke mechanistische grondslag |
| 2 | Posterolateraal myocardinfarct | 99,87% | L5 | Doorgaan met waarborgen | Geen direct bewijs; mechanisme is van toepassing |
| 3 | Maligne renovasculaire hypertensie | 99,85% | L4 | Wachten | β-blokker niet eerste keus; behandelt niet de oorzaak (RAS) |
| 4 | Maligne hypertensieve nierziekte | 99,85% | L5 | Wachten | Onvoldoende potentie voor hypertensieve noodtoestand |
| 5 | Pulmonale hypertensie (longziekte/hypoxie) | 99,84% | L5 | Wachten | ⛔ **Gecontraïndiceerd** — kan hemodynamische instorting veroorzaken |
| 6 | Pulmonale hypertensie (multifactorieel) | 99,84% | L5 | Wachten | ⛔ **Gecontraïndiceerd** — β-blokkers schadelijk bij PH |
| 7 | Septaal myocardinfarct | 99,84% | L4 | Doorgaan met waarborgen | Risico op geleiding bundel schade; mechanisme is van toepassing |
| 8 | Braddock-syndroom | 99,80% | L5 | Wachten | Geen mechanistische koppeling; zeldzame genetische aandoening |
| 9 | Chronische longhartziekten | 99,04% | L3 | Onderzoeksvraag | Controversieel; bewijs inconsistent |

---

## Conclusie en vervolgstappen

**Besluit: Doorgaan met waarborgen**

**Grondslag:**
De TxGNN-voorspelling voor posteroinferior myocardinfarct is mechanistisch gezond — atenolols β1-selectieve blokkade vermindert de myocardiale zuurstofvraag en voorkomt reinfarctie, en dit mechanisme is niet afhankelijk van infarctlocatie. β-blokkers zijn al standaardbehandeling voor secundaire preventie van MI volgens ESC-richtlijnen. Echter, de specifieke anatomische subtype (posteroinferior) brengt aanvullende risico's met zich mee (AV-blokade, rechterventriculaire betrokkenheid) die verhoogde monitoring vereisen, en er zijn geen speciale klinische trials voor deze specifieke subtype.

**Belangrijke veiligheidsmarkeringen in alle voorspellingen:**
- Voorspellingen #5 en #6 (pulmonale hypertensie) moeten **afgewezen** worden — β-blokkers zijn over het algemeen gecontraïndiceerd bij pulmonale hypertensie en kunnen leven-bedreigende hemodynamische verslechtering veroorzaken.
- Voorspelling #8 (Braddock-syndroom) heeft **geen mechanistische basis** en moet worden genegeerd.

**Om verder te gaan is het volgende nodig:**
- Ophalen van CBG-MEB-autorisatiedetails en SPC voor atenolol-producten beschikbaar in Nederland
- Verkrijgen van gedetailleerde mechanisme-gegevens uit DrugBank (momenteel een datalacune)
- Uitvoering van een gericht literatuuronderzoek naar β-blokkergebruik gestratificeerd naar MI-anatomische subtype (inferieur vs anterieur vs lateraal)
- Monitoring van de resultaten van de REDUCE-SWEDEHEART-trial (NCT03278509) voor bijgewerkt bewijs over voordeel van β-blokkers na MI
- Ontwikkeling van een veiligheidsmonitoringprotocol dat specifiek betrekking heeft op AV-geleiding en rechterventriculaire functie in posteroinferior MI-patiënten
- Raadplegen van SPC-waarschuwingen en contraïndicaties (momenteel een datalacune in deze evidentiebundel)

---

*Disclaimer: Dit rapport is voor onderzoeksdoeleinden en vormt geen medisch advies. Kandidaten voor hergebruik van geneesmiddelen vereisen klinische validatie vóór toepassing. Raadpleeg de SPC (Samenvatting van de Productkenmerken) voor gezaghebbende voorschrijfinformatie.*

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

