---
layout: default
title: Rivastigmine
parent: Alleen modelvoorspelling (L5)
nav_order: 295
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Rivastigmine: voorspelde nieuwe indicatie Glaucoom (bewijsniveau L5). Oorspronkelijke indicatie: Ziekte van Alzheimer (en verwante aandoeningen…"
monitor_inn: "Rivastigmine"
predicted_indications: ["glaucoma"]
---

# Rivastigmine
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **1** 
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

## Rivastigmine: Van de ziekte van Alzheimer naar glaucoom
{: .text-alpha }

## Samenvatting in één zin

Rivastigmine is een cholinesteraseremmer die oorspronkelijk wordt gebruikt bij de ziekte van Alzheimer en verwante hersenaandoeningen.
Het TxGNN-model voorspelt dat het werkzaam kan zijn bij **glaucoom**, maar er zijn **geen geregistreerde klinische studies** en slechts **3 publicaties** (een dierstudie, een computationele analyse en een overzichtsartikel) die deze richting ondersteunen.

---

## Snel overzicht

| Item | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Ziekte van Alzheimer (en verwante aandoeningen, o.a. de ziekte van Pick, cerebellaire degeneratie) |
| Voorspelde nieuwe indicatie | Glaucoom |
| TxGNN-voorspellingsscore | 0,9927 |
| Bewijsniveau | L5 |
| Marktstatus in Nederland | In de handel (geldige vergunningen: 38 van 38) |
| Aantal vergunningen | 38 (geldig: 38) |
| Aanbevolen beslissing | Hold |

---

## Waarom is deze voorspelling aannemelijk?

Rivastigmine remt zowel acetylcholinesterase als butyrylcholinesterase. Daardoor wordt acetylcholine minder snel afgebroken en neemt de cholinerge signalering toe. Gegevens over het werkingsmechanisme in de data die voor dit rapport zijn samengesteld ontbreken; het mechanisme hier is afgeleid uit de geneesmiddelklasse.

Bij glaucoom kan versterkte cholinerge signalering in de ciliaire spier en het trabeculair netwerk de afvoer van kamerwater vergroten en zo de oogdruk verlagen. Dit is dezelfde basis als bij klassieke parasympathicomimetica zoals pilocarpine en fysostigmine. Een preklinische studie (PMID 10673128, 2000) toonde aan dat topisch rivastigmine de oogdruk verlaagde bij konijnen. Een analyse uit 2024 (PMID 39130374) geeft aanvullende computationele en mechanistische ondersteuning.

Let op: de hoge TxGNN-score is slechts een modelvoorspelling en geen klinisch bewijs. Er zijn geen humane glaucoomgegevens beschikbaar. Cholinesterseremmers hebben bovendien bekende oculaire en systemische cholinerge bijwerkingen (o.a. miosis, bradycardie, maag-darmklachten).

---

## Bewijs uit klinische studies

Momenteel zijn er geen gerelateerde klinische studies geregistreerd.

---

## Bewijs uit de literatuur

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|-----|------|------|---------|
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | Preklinische dierstudie (konijn, topisch) | J Ocul Pharmacol Ther | Topisch rivastigmine, een selectieve acetylcholinesteraseremmer, verlaagde de oogdruk bij normotensieve konijnen. |
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | Computationele/systeemgenetische analyse | Front Mol Biosci | Onderzoek naar cholinerge middelen voor oogdrukverlaging; wijst op beperkingen van bestaande M3-agonisten door systemische cholinerge bijwerkingen. |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | Review (octrooiliteratuur) | Expert Opin Ther Pat | Overzicht van acetylcholinesteraseremmers en reactivatoren; milde remming heeft therapeutische relevantie bij o.a. Alzheimer, myasthenia gravis en glaucoom. |

---

## Informatie over de Nederlandse markt

| RVG-nummer | Productnaam | Toedieningsvorm | Goedgekeurde indicatie |
|---------|------|------|-----------|
| RVG 115384 | Rivastigmine Sandoz 13,3 mg/24 uur, pleisters voor transdermaal gebruik (geldig) | Transdermale pleister | Niet beschikbaar in de data |

Dit kan de beschikbaarheid van een geschikte formulering voor oculair gebruik beperken.

<!-- review:begin nl-lic-20261106-rivastigmine-1 -->

> **Controlecorrectie (2026-11-06)**: Oorspronkelijk stond er: “De enige bekende vergunning is ingetrokken. Dit kan de beschikbaarheid van een geschikte formulering voor oculair gebruik beperken.” Verwijderd: de vermelding dat de vergunningen zijn doorgehaald of dat er geen geldige vergunning is, kwam niet overeen met de registratiegegevens van het CBG (2026-11-06). Aantal vergunningen in de gegevens: 1, waarvan geldig: 1; actuele aantallen staan in het snelle overzicht en bij de marktinformatie. Bron: [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/).

<!-- review:end nl-lic-20261106-rivastigmine-1 -->

---

## Veiligheidsoverwegingen

- **Contra-indicaties uit de kennisgraaf (geen productteksten):** de TxGNN-kennisgraaf koppelt rivastigmine aan onder meer epilepsie, astma, chronische obstructieve longziekte (COPD), actieve maagzweer, urinewegobstructie, hartgeleidingsstoornissen (waaronder sick-sinussyndroom en atrioventriculair blok), plotselinge hartstilstand, ziekte van Parkinson en andere parkinsonistische aandoeningen, basaalganglialaandoeningen, focale handdystonie, blefarospasme, diarree en anorexia nervosa. Deze koppelingen zijn niet afkomstig van de officiële bijsluiter en moeten worden geverifieerd.
- **Geneesmiddelinteracties:** 100 interacties gevonden, waarvan hier de belangrijkste:
  - **Ernstig (Major):** bupropion.
  - **Matig (Moderate):** onder meer anticholinergica (atropine, hyoscyamine, glycopyrronium, dicyclomine, trospium, clidinium, mepenzolaat), H2-blokkers (famotidine, ranitidine, cimetidine), loperamide, metronidazol, claritromycine, levofloxacine, dolasetron en palonosetron, en enkele darmspoelmiddelen (picosulfaat, macrogol, natriumsulfaat).

Voor volledige veiligheidsinformatie, waarschuwingen en contra-indicaties: raadpleeg de SmPC (Samenvatting van de Productkenmerken) en de bijsluiter van het CBG-MEB.

---

## Conclusie en vervolgstappen

**Beslissing: Hold**

**Onderbouwing:**
Het bewijs bestaat uitsluitend uit een dierstudie, een computationele analyse en een overzichtsartikel (bewijsniveau L4), zonder humane gegevens of klinische studies.

<!-- review:begin nl-lic-20261106-rivastigmine-2 -->

> **Controlecorrectie (2026-11-06)**: Oorspronkelijk stond er: “Het bewijs bestaat uitsluitend uit een dierstudie, een computationele analyse en een overzichtsartikel (bewijsniveau L4), zonder humane gegevens of klinische studies. Bovendien is de enige Nederlandse vergunning ingetrokken en ontbreekt productgebonden veiligheidsinformatie, waardoor verdere beoordeling nu niet verantwoord is.” Verwijderd: de vermelding dat de vergunningen zijn doorgehaald of dat er geen geldige vergunning is, kwam niet overeen met de registratiegegevens van het CBG (2026-11-06). Aantal vergunningen in de gegevens: 1, waarvan geldig: 1; actuele aantallen staan in het snelle overzicht en bij de marktinformatie. Bron: [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/).

<!-- review:end nl-lic-20261106-rivastigmine-2 -->

**Om verder te gaan is het volgende nodig:**
- Productinformatie (SmPC/bijsluiter) van het CBG-MEB ophalen en analyseren op waarschuwingen en contra-indicaties (blokkerende gegevenslacune)
- Gegevens over het werkingsmechanisme aanvullen, bijvoorbeeld via DrugBank
- Humane gegevens verzamelen, zoals een klein fase 1/2-onderzoek naar oogdrukverlaging bij glaucoom
- Een veiligheidsbeoordeling uitvoeren van oculaire en systemische cholinerge bijwerkingen (o.a. bradycardie, miosis, maag-darmklachten), mede gezien de in de kennisgraaf genoemde contra-indicaties

<!-- review:begin nl-lic-20261106-rivastigmine-3 -->

> **Controlecorrectie (2026-11-06)**: Oorspronkelijk stond er: “Beoordelen of een geschikte oculaire formulering mogelijk is en hoe de ingetrokken vergunning daarop van invloed is / Een veiligheidsbeoordeling uitvoeren van oculaire en systemische cholinerge bijwerkingen (o.a. bradycardie, miosis, maag-darmklachten), mede gezien de in de kennisgraaf genoemde contra-indicaties” Verwijderd: de vermelding dat de vergunningen zijn doorgehaald of dat er geen geldige vergunning is, kwam niet overeen met de registratiegegevens van het CBG (2026-11-06). Aantal vergunningen in de gegevens: 1, waarvan geldig: 1; actuele aantallen staan in het snelle overzicht en bij de marktinformatie. Bron: [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/).

<!-- review:end nl-lic-20261106-rivastigmine-3 -->

<!-- review:begin log -->

## Controlelogboek

Hieronder staat het controlelogboek van deze pagina: gegevens gecontroleerd aan de hand van de registratiegegevens van het CBG (College ter Beoordeling van Geneesmiddelen). Correcties betreffen alleen feitelijke basisgegevens; modelvoorspellingen, bewijsniveaus en conclusies zijn niet herschreven.

| Controledatum | Onderdeel | Actie | Bron |
|------|------|------|------|
| 2026-11-06 | Verwijderd: “De enige bekende vergunning is ingetrokken” | Gecorrigeerd | [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/) |
| 2026-11-06 | Verwijderd: “Bovendien is de enige Nederlandse vergunning ingetrokken en ontbreekt productgebonden veiligheidsinformatie, waardoor verdere beoordeling nu” | Gecorrigeerd | [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/) |
| 2026-11-06 | Verwijderd: “Beoordelen of een geschikte oculaire formulering mogelijk is en hoe de ingetrokken vergunning daarop van invloed is” | Gecorrigeerd | [CBG-MEB – Geneesmiddeleninformatiebank (metadata)](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); [Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/) |

<!-- review:end log -->

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

