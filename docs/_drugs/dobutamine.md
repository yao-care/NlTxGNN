---
layout: default
title: Dobutamine
parent: Alleen modelvoorspelling (L5)
nav_order: 118
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Dobutamine: voorspelde nieuwe indicatie Alopecia (bewijsniveau L5). Oorspronkelijke indicatie: Niet beschikbaar in de voor dit rapport samengestelde gegevens"
monitor_inn: "dobutamine"
predicted_indications: ["alopecia", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "open-angle glaucoma", "Raynaud disease", "primary hereditary glaucoma", "headache disorder", "hypertrichosis (disease)", "migraine disorder"]
---

# Dobutamine
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **10** 
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

## Dobutamine: Van de oorspronkelijke indicatie naar alopecia (haaruitval)
{: .text-alpha }

## Samenvatting in één zin

Dobutamine is een bèta-1-adrenerge agonist en inotroop middel dat intraveneus wordt gebruikt. De oorspronkelijke indicatie is in de beschikbare vergunningsgegevens niet vermeld. Het TxGNN-model voorspelt dat dobutamine werkzaam kan zijn bij **alopecia**, maar er zijn **0 klinische studies** en slechts **1 publicatie** (een veterinaire casuïstiek, geen bewijs van werkzaamheid). Deze voorspelling is vermoedelijk een artefact van het model.

---

## Snel overzicht

| Item | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Niet beschikbaar in de voor dit rapport samengestelde gegevens |
| Voorspelde nieuwe indicatie | Alopecia |
| TxGNN-voorspellingsscore | 0.9985 |
| Bewijsniveau | L5 |
| Marktstatus in Nederland | In de handel (geldige vergunningen: 3 van 4) |
| Aantal vergunningen | 4 (geldig: 3) |
| Aanbevolen beslissing | Hold |

---

## Waarom is deze voorspelling (on)aannemelijk?

Volgens de rubriek ‘Clinical Pharmacology’ van de door de Amerikaanse FDA goedgekeurde productinformatie (Prescribing Information) voor Dobutamine (niet-officiële vertaling): ‘Dobutaminehydrochloride is een direct werkend inotroop middel waarvan de primaire werking voortkomt uit stimulatie van de bètareceptoren van het hart, terwijl het relatief milde chronotrope, hypertensieve, aritmogene en vaatverwijdende effecten heeft. Het veroorzaakt geen afgifte van endogeen noradrenaline, zoals dopamine wel doet.’ Oorspronkelijke Engelse tekst: "Dobutamine hydrochloride is a direct-acting inotropic agent whose primary activity results from stimulation of the beta-receptors of the heart while producing comparatively mild chronotropic, hypertensive, arrhythmogenic, and vasodilative effects. It does not cause the release of endogenous norepinephrine, as does dopamine." ([DailyMed: Dobutamine Hydrochloride In Dextrose (dobutamine hydrochloride) prescribing information, Baxter Healthcare Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6b17b98b-e06d-42ed-925f-69aa2699dead), versie van 2023-09-08; geraadpleegd op 2026-11-19). Dobutamine is een bèta-1-adrenerge agonist die de hartcontractiliteit verhoogt. Het wordt intraveneus toegediend bij acuut hartfalen en voor stressechocardiografie.

Er is **geen plausibele mechanistische link** met haarfollikelbiologie. De hoge score van 0,9985 is waarschijnlijk een grafartefact: in het kennisnetwerk ligt dobutamine dicht bij cardiovasculaire geneesmiddelen zoals minoxidil, een vaatverwijder die wél met haargroei wordt geassocieerd (ook als bijwerking, hypertrichose). Die nabijheid in het netwerk is geen bewijs dat dobutamine werkt.

Ook de overige voorspellingen met hoge scores (hypotrichosis simplex van de hoofdhuid, congenitale hypotrichosis milia, diffuse alopecia areata, glaucoom, ziekte van Raynaud, hoofdpijn, hypertrichose en migraine) kennen geen klinische of mechanistische onderbouwing.

---

## Klinisch trialbewijs

Er zijn momenteel geen gerelateerde klinische studies geregistreerd.

---

## Literatuurbewijs

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|-----|------|------|---------|
| [41046802](https://pubmed.ncbi.nlm.nih.gov/41046802/) | 2025 | Casuïstiek (veterinair) | Journal of Veterinary Cardiology | Hartfalen bij een kat door minoxidilvergiftiging; dobutamine werd gebruikt vanwege hypotensie. Geen bewijs voor werking bij haaruitval. |

---

## Informatie over de Nederlandse markt

<!-- licenses:begin -->

| Registratienummer | Productnaam | Werkzame stof(fen) | Farmaceutische vorm | Status |
|------|------|------|------|------|
| RVG 19143 | Dobutamine CF 12,5 mg/ml, concentraat voor oplossing voor intraveneuze infusie | DOBUTAMINEHYDROCHLORIDE | Concentraat voor oplossing voor infusie | Geldig |
| RVG 32409 | Dobutamine-hameln 12,5 mg/ml steriel concentraat, concentraat voor oplossing vo… | DOBUTAMINEHYDROCHLORIDE | Concentraat voor oplossing voor infusie | Geldig |
| RVG 32410 | Dobutamine-hameln 5 mg/ml i.v. infusievloeistof, oplossing voor infusie | DOBUTAMINEHYDROCHLORIDE | Oplossing voor infusie | Geldig |
| RVG 107115 | Dobutamine Claris 12,5 mg/ml, concentraat voor oplossing voor infusie | DOBUTAMINEHYDROCHLORIDE | – | Niet geregistreerd |

Bron: CBG-MEB – Geneesmiddeleninformatiebank (metadata.csv); productnaam, werkzame stoffen en farmaceutische vorm in de oorspronkelijke Nederlandse bewoording van het CBG. „Niet geregistreerd”: het registratienummer komt niet voor in de actuele Geneesmiddeleninformatiebank.

<!-- licenses:end -->

---

## Veiligheidsoverwegingen

- **Contra-indicaties volgens het kennisnetwerk** (afgeleid uit TxGNN/PrimeKG, niet uit de bijsluitertekst): hypertensieve aandoeningen, hypertensie, kaliumtekort, boezemfibrilleren, aortastenose (inclusief aortaklepaandoeningen en supravalvulaire aortastenose), myocardinfarct en coronaire trombose, hemoglobinopathie, hypertrofische cardiomyopathie (inclusief familiaire vorm).
- **Geneesmiddelinteracties**: in totaal 115 interacties gevonden; de weergegeven interacties zijn van gemiddeld niveau. Het gaat vooral om antidiabetica (o.a. acarbose, metformine, pioglitazon, repaglinide, insuline degludec en insuline aspart, GLP-1-agonisten zoals liraglutide, semaglutide, dulaglutide en albiglutide, SGLT2-remmers zoals canagliflozine, dapagliflozine en empagliflozine, en DPP-4-remmers zoals alogliptine en linagliptine), daarnaast chloorpropamide, cimetidine, diëthylpropion, fentermine en vancomycine.

Raadpleeg voor waarschuwingen en contra-indicaties volgens de officiële tekst de SmPC (Samenvatting van de Productkenmerken) en de bijsluiter van het CBG-MEB. Die gegevens ontbreken in de samengestelde gegevens.

---

## Conclusie en vervolgstappen

**Beslissing: Hold**

**Onderbouwing:**
- De voorspelling berust uitsluitend op het model (L5). Er zijn geen klinische studies, en de enige gevonden publicatie is een veterinaire casuïstiek zonder bewijs van werkzaamheid. Er is geen plausibel werkingsmechanisme, en intraveneuze toediening van een hartstimulerend middel past niet bij haaruitval.

<!-- review:begin nl-lic-20261112-dobutamine-1 -->

> **Controlecorrectie (2026-11-12)**: Oorspronkelijk stond er: “Er is geen plausibel werkingsmechanisme, en intraveneuze toediening van een hartstimulerend middel past niet bij haaruitval. Bovendien is de enige Nederlandse vergunning doorgehaald.” Verwijderd: de vermelding dat de vergunningen zijn doorgehaald of dat er geen geldige vergunning is, kwam niet overeen met de registratiegegevens van het CBG (2026-11-12). Actuele aantallen en de status per registratie staan in het snelle overzicht en in de vergunningstabel bij de marktinformatie. Bron: [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/).

<!-- review:end nl-lic-20261112-dobutamine-1 -->

**Om verder te gaan is het volgende nodig:**
- Gegevens over het werkingsmechanisme (DrugBank) en de officiële veiligheidsinformatie uit de SmPC van het CBG-MEB
- Preklinisch onderzoek naar een effect van bèta-1-agonisme op haarfollikels
- Beoordeling van de toedieningsroute (intraveneus versus lokaal), aangezien die momenteel niet bij de voorspelde indicatie past
- Een heroverweging van de modelvoorspelling, gezien het waarschijnlijke grafartefact via minoxidil

<!-- review:begin log -->

## Controlelogboek

Hieronder staat het controlelogboek van deze pagina: gegevens gecontroleerd aan de hand van de registratiegegevens van het CBG (College ter Beoordeling van Geneesmiddelen). Correcties betreffen alleen feitelijke basisgegevens; modelvoorspellingen, bewijsniveaus en conclusies zijn niet herschreven. De zin dat gegevens over het werkingsmechanisme niet beschikbaar waren, is vervangen door een uittreksel uit de aangehaalde officiële productinformatie (met niet-officiële vertaling).

| Controledatum | Onderdeel | Actie | Bron |
|------|------|------|------|
| 2026-11-12 | Verwijderd: “Bovendien is de enige Nederlandse vergunning doorgehaald” | Gecorrigeerd (herzien op 2026-11-24; eerdere versie bewaard in het record) | [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/) |
| 2026-11-12 | Tabelregel RVG 107115: “geldig” → “niet geregistreerd” | Vervangen door de door het programma gegenereerde vergunningstabel (eerder: Gecorrigeerd) | [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/) |
| 2026-11-19 | Zin ‘gegevens over het werkingsmechanisme niet beschikbaar’ vervangen door uittreksel uit de Amerikaanse productinformatie | Zin dat gegevens over het werkingsmechanisme ontbraken vervangen door een uittreksel met bron | [DailyMed: Dobutamine Hydrochloride In Dextrose (dobutamine hydrochloride) prescribing information, Baxter Healthcare Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6b17b98b-e06d-42ed-925f-69aa2699dead) |

<!-- review:end log -->

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

