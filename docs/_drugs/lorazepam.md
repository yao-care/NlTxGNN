---
layout: default
title: Lorazepam
parent: Alleen modelvoorspelling (L5)
nav_order: 88
evidence_level: L5
indication_count: 10
---

# Lorazepam
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **10** 
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

# Lorazepam: van angststoornis en sedatie naar trigeminus-zenuwneoplasma

## Samenvatting in één zin

Lorazepam is een benzodiazepine dat historisch wordt gebruikt voor angststoornissen, sedatie en korte-termijnbehandeling van slapeloosheid.
Het TxGNN-model voorspelt dat het mogelijk effectief kan zijn voor **trigeminus-zenuwneoplasma**,
met **geen klinische trials** en **geen publicaties** die deze richting ondersteunen — deze voorspelling is zeer waarschijnlijk een vals-positief in de kennisgraaf en moet eerder worden beschouwd als waarschuwingssignaal dan als echte kandidaat voor geneesmiddel-herwenning.

---

## Kort overzicht

| Item | Inhoud |
|------|--------|
| Originele indicatie | Angststoornis en sedatie (benzodiazepineklasse; geen Nederlandse markttoelating op record) |
| Voorspelde nieuwe indicatie | Trigeminus-zenuwneoplasma |
| TxGNN-voorspellingsscore | 99.87% |
| Evidententieniveau | L5 |
| Status op Nederlandse markt | Niet in de handel |
| Aantal toelatingen | 0 |
| Aanbevolen besluit | Wachten |

---

## Waarom is deze voorspelling redelijk?

Momenteel zijn geen gedetailleerde werkingsmechanisme-gegevens beschikbaar in de verstrekte dataset. Op basis van bekende farmacologische informatie is Lorazepam een benzodiazepine — een positieve allosterische modulator van de GABA-A-receptor — die chloride-ioninstroom versterkt om sedatieve, anxiolytische, spierontspannende en anticonvulsieve effecten op te wekken. De klinische geschiedenis omvat korte-termijnbehandeling van angststoornissen, procedurele sedatie en controle van aanvallen.

Er bestaat **geen vastgestelde mechanistische relatie** tussen GABA-A-receptormodulatie en de biologie van trigeminus-zenuwneoplasma. Lorazepam heeft geen bekende antitumor-, anti-angiogene of antiproliferatieve activiteit. Trigeminus-zenuwneoplasma zijn ruimte-innemende laesies die vooral worden beheerd door neurochirurgie of radiotherapie; benzodiazepinen spelen geen erkende rol in hun pathofysiologie of behandeling.

De uitzonderlijk hoge TxGNN-score (0.9987, rangschikking 403) is vrijwel zeker toe te schrijven aan **kennisgraaf-ruis of overfitten van kenmerken**: de brede connectiviteit tussen geneesmiddelenknooppunten en neurologische ziekteknopen in de onderliggende kennisgraaf verhoogt systematisch scores voor zeldzame neuro-oncologische aandoeningen, waardoor valse positieven ontstaan. Dit is een erkende beperking van op graaf-gebaseerde voorspellingsmodellen en moet een kwaliteitsaudit van de graaf activeren in plaats van klinische vervolgstappen.

---

## Bewijs van klinische trials

Momenteel geen gerelateerde klinische trials geregistreerd.

---

## Bewijs uit literatuur

Momenteel geen relevante literatuur beschikbaar.

---

## Informatie over de Nederlandse markt

Lorazepam beschikt momenteel over **geen CBG-MEB-marketingtoelatingen** in Nederland en is niet geregistreerd voor enige indicatie op de Nederlandse markt. Er zijn daarom geen RVG-nummers, SmPC-documenten of goedgekeurde indicatieteksten beschikbaar van het nationaal register.

> Ter referentie: in andere jurisdicties waar Lorazepam is goedgekeurd, moeten de SmPC (Samenvatting van de Productkenmerken) en PIL (Patiëntenbijsluiter) worden geraadpleegd voor veiligheidsinformatie, goedgekeurde indicaties en voorschrijfvoorwaarden.

---

## Veiligheidsaspecten

Raadpleeg de SmPC (Samenvatting van de Productkenmerken) voor veiligheidsinformatie.

---

## Conclusie en volgende stappen

**Besluit: Wachten**

**Motivering:**
Dit is een L5-voorspelling — alleen TxGNN-modeluitvoer — zonder ondersteunend bewijs van klinische trials, geen gepubliceerde literatuur, geen mechanistische basis en geen plausibele farmacologische grondslag die Lorazepam verbindt aan trigeminus-zenuwneoplasma. De hoge numerieke score weerspiegelt vrijwel zeker systematische vals-positieve generatie in de kennisgraaf in plaats van een werkelijk geneesmiddel-ziektesignaal.

**Om door te gaan, is het volgende nodig:**

- **Kwaliteitsaudit van de graaf**: Onderzoeken of de TxGNN-kennisgraaf systematisch benzodiazepineknooppunten over-verbindt met zeldzame neurologische ziekteknopen, en scorerecalibrering of kantgewichtcorrectie toepassen
- **Generatie van mechanistische hypothese**: Identificeer een biologisch pad waardoor GABA-A-modulatie de tumor- of overlevingsgroei van trigeminus-zenuwneoplasma zou kunnen beïnvloeden — op dit moment is geen enkel voorgesteld
- **Minimale drempel voor bewijs**: Minimaal één peer-reviewed caseraport of in vitro-studie die enige benzodiazepine-activiteit relevant voor perifere zenuwneoplasma documenteert, voordat verdere investeringen in deze kandidaat gerechtvaardigd zijn
- **Aanpakken van MOA-gegevensgat**: Haal het volledige Lorazepam DrugBank-item op (DrugBank-ID: DB00186) om toekomstige beoordelingen van mechanistische plausibiliteit voor alle voorspelde indicaties te ondersteunen

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

