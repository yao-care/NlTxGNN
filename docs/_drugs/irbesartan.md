---
layout: default
title: Irbesartan
parent: Alleen modelvoorspelling (L5)
nav_order: 80
evidence_level: L5
indication_count: 4
---

# Irbesartan
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **4** 
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

# Irbesartan: van hypertensie naar maligne hypertensieve nierziekte

## Samenvatting in één zin

Irbesartan is een angiotensine II-receptorblokker (ARB) die veel wordt gebruikt voor hypertensie en diabetische nefropathie en werkt door selectief de AT1-receptor te blokkeren om de bloeddruk en nierfunctie te beschermen.
Het TxGNN-model voorspelt dat het mogelijk effectief kan zijn voor **maligne hypertensieve nierziekte**, met een voorspellingsscore van **99.31%**.
Er werden echter geen klinische onderzoeken of publicaties gevonden die specifiek gericht zijn op deze indicatie in dit bewijsonderzoek — de voorspelling berust uitsluitend op mechanistische aannemelijkheid.

---

## Snelle blik

| Item | Inhoud |
|------|--------|
| Oorspronkelijke indicatie | Hypertensie en diabetische nefropathie (afgeleid van medicijnklasse; geen NL-autorisatiegegevens beschikbaar) |
| Voorspelde nieuwe indicatie | Maligne hypertensieve nierziekte |
| TxGNN-voorspellingsscore | 99.31% |
| Bewijsniveau | L5 |
| Status op NL-markt | Niet op de markt (volgens de actuele gegevensverzameling) |
| Aantal autorisaties | 0 |
| Aanbevolen beslissing | In afwachting |

---

## Waarom is deze voorspelling redelijk?

Gedetailleerde gegevens over het werkingsmechanisme zijn momenteel niet beschikbaar in het Evidence Pack. Op basis van gevestigde farmacologie is irbesartan een angiotensine II-receptorblokker (ARB) die selectief de AT1-receptor antagoniseert, waardoor de downstreameffecten van angiotensine II worden geblokkeerd — inclusief systeemse vasoconrictie, aldosterongestuurde natriumretentie en efferente arteriële vernauwing binnen het glomerulus. Het netto-effect is een verlaging van zowel de systeemse bloeddruk als de glomerulaire capillairdruk, wat progressieve hypertensieve nierschade vertraagt.

Maligne hypertensieve nierziekte deelt precies deze pathologische as: ernstige, ongecontroleerde hypertensie veroorzaakt glomerulaire ischemie, fibrinoïde necrose van arteriolen en snelle verslechtering van de nierfunctie. ARB's hebben aangetoonde renaalbeschermende werking in aangrenzende aandoeningen — de IDNT-studie toonde aan dat irbesartan zelf de progressie van diabetische nefropathie vertraagt, en de RENAAL-studie ondersteunde losartan in een vergelijkbare setting. Maligne hypertensieve nefropathie vertegenwoordigt een versnelde, hogedrukvariant van dit dezelfde mechanisme, wat de uitbreiding van ARB-therapie conceptueel coherent maakt.

Dat gezegd hebbende, de bewijszoeking leverde nul klinische onderzoeken en nul publicaties op die irbesartan in maligne hypertensieve nierziekte rechtstreeks bestudeerden. De TxGNN-voorspelling is mechanistisch aannemelijk en algoritmisch zeker van een hoge graad, maar heeft momenteel geen directe empirische ondersteuning.

---

## Klinische onderzoeksbewijs

Momenteel zijn er geen gerelateerde klinische onderzoeken geregistreerd.

---

## Literatuurbewijs

Momenteel is er geen gerelateerde literatuur beschikbaar.

---

## Informatie over de Nederlandse markt

In de actuele gegevensverzameling zijn geen CBG-MEB-markttoestemmingen voor irbesartan geregistreerd.

> **Opmerking:** Dit weerspiegelt waarschijnlijk een gegevensgat in plaats van de werkelijke marktsituatie. Irbesartan (Aprovel® en meerdere generieke preparaten) is een goed gevestigde ARB in Nederland. Controleer de actuele autorisatiestatus rechtstreeks via het [CBG-MEB Geneesmiddelenrepertorium](https://www.geneesmiddelenrepertorium.nl/) voordat u regelgevingsconclusies trekt.

---

## Veiligheidsbeschouwingen

Raadpleeg de SmPC (Samenvatting van de Productkenmerken) voor volledige veiligheidsinformatie. Gezien de doelstellingsindicatie (maligne hypertensieve nierziekte), zijn de volgende voorzorgsmaatregelen op het niveau van de medicijnklasse klinisch relevant en dienen ze te worden bevestigd tegen de actuele SmPC voordat enig gebruik:

- **Risico op acute nierschade** bij patiënten met bilaterale nierslagaderstenostis of een enkele functionerende nier — AT1-receptorblokking verwijdert de compensatoire efferente arteriële tonus, wat mogelijk leidt tot acuut GFR-instorten (eveneens rechtstreeks relevant voor de 2de indicatie).
- **Hyperkaliëmie** risico bij patiënten met gevorderde nierinsufficiëntie of gelijktijdig gebruik van kaliumsparende middelen.
- **Hypotensie na eerste dosis** bij volumetisch uitgeputte patiënten, wat bijzonder relevant is in de acute behandeling van maligne hypertensie.

---

## Conclusie en vervolgstappen

**Beslissing: In afwachting**

**Motivering:**
Het TxGNN-model wijst een hoge mechanistische voorspellingsscore toe (99.31%), en de pathofysiologische link tussen AT1-receptorblokking en maligne hypertensieve nierschade is conceptueel goed gefundeerd. De volledige afwezigheid van ondersteunend klinisch bewijs of directe literatuurbewijs plaatst dit echter op bewijsniveau L5 — alleen modelvoorspelling — wat onvoldoende is om naar klinische toepassing over te gaan zonder nader onderzoek.

**Om door te gaan is het volgende nodig:**

- **Vullen van literatuurgaten:** Gericht onderzoek naar bewijzen op klassebasis (irbesartan, losartan, valsartan) specifiek bij maligne of versnelde hypertensie met betrokkenheid van nieren, om te beoordelen of L5 kan worden opgewaardeerd naar L3 of L4.
- **MOA-gegevens:** Los het DrugBank-gegevensgat op (DG002) door het DrugBank-API te bevragen voor het volledige mechanisme, doelen en farmacodynische profiel van irbesartan.
- **NL regelgevingsverificatie:** Bevestig de werkelijke CBG-MEB-autorisatiestatus; de actuele gegevensverzameling registreert 0 licenties, wat in tegenspraak is met de bekende aanwezigheid van irbesartan op de Europese markt.
- **SmPC-review:** Verkrijg en analyseer de irbesartan SmPC (DG001) om de contra-indicatie en waarschuwingsprofilering af te ronden — momenteel een blokkend gegevensgat voor veiligheidsbeoordeling (DG001, Prioriteit: Blokkend).
- **Raadpleging van nefrologieexpert:** Beoordeel klinische haalbaarheid in de maligne hypertensiesetting, inclusief of noodlottige bloeddrukmanagementsprotocollen het gebruik van ARB's zouden toestaan of zouden kiezen voor alternatieve middelen (bijv. IV labetalol, nitroprusside) in de acute fase.
- **Plan voor veiligheidsbewaking:** Bepaal een protocol voor nierfunctie- en kaliummonitoring dat geschikt is voor patiënten met bestaande hypertensieve nierschade.

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

