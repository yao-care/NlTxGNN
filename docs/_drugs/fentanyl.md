---
layout: default
title: Fentanyl
parent: Alleen modelvoorspelling (L5)
nav_order: 68
evidence_level: L5
indication_count: 2
---

# Fentanyl
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

# Fentanyl: van behandeling van ernstige pijn naar Nefrogeen syndroom van inadequate antidiurese

## Samenvatting in één zin

Fentanyl is een potente μ-opiöïdereceptoragonist die veel gebruikt wordt in de klinische praktijk voor de behandeling van matig-ernstige acute en chronische pijn.
Het TxGNN-model voorspelt dat het effectief kan zijn voor **Nefrogeen syndroom van inadequate antidiurese (NSIAD)**, met momenteel **0 klinische onderzoeken** en **0 publicaties** die deze richting ondersteunen.
Kritisch gezegd suggereren pharmacologische analyses dat deze voorspelling waarschijnlijk een vals positief is: het opiöïde-ADH-pad vastgelegd in de kennisgraaf staat in tegengestelde richting ten opzichte van het therapeutische doel in NSIAD.

---

## Snelle Overzicht

| Item | Inhoud |
|------|--------|
| Originele indicatie | Behandeling van ernstige pijn (opiöïdanalgeticum; geen NL-autorisatie op record) |
| Voorspelde nieuwe indicatie | Nefrogeen syndroom van inadequate antidiurese (NSIAD) |
| TxGNN-voorspellingsscore | 99.46% |
| Bewijsniveau | L5 |
| Marktstatus Nederland | Niet geregistreerd |
| Aantal autorisaties | 0 |
| Aanbevolen besluit | Aanhouden |

---

## Waarom is deze voorspelling redelijk?

Fentanyl is een krachtige μ-opiöïdereceptor (MOR) agonist met snelle werking en hoge lipofiliciteit. Opiöïdmiddelen zijn goed gevestigd in de literatuur als stimulatoren van de afscheiding van hypothalamisch antidiuretisch hormoon (ADH/vasopressine), wat een directe pharmacologische verbinding creëert met de as van de waterhuishouding van het lichaam. Dit mechanistische pad — **opiöïdereceptor → ADH-afscheiding → renale waterbinding** — is de topologische verbinding vastgelegd door de TxGNN-kennisgraaf, wat de hoge betrouwbaarheidsscore (0.9946) verklaart.

NSIAD is een zeldzame ziekte veroorzaakt door gain-of-function mutaties in het *AVPR2* gen (V2-vasopressinereceptor), resulterend in constitutieve receptoractivering, ongereguleerde renale waterreabsorptie, en aanhoudende hyponatriëmie — allemaal optredend **onafhankelijk van circulerend ADH-niveaus**. De therapeutische strategie in NSIAD is het verminderen van waterbinding en het corrigeren van hyponatriëmie, niet het verder activeren van de ADH-as.

Dit creëert een fundamentaal pharmacologisch mismatch: toediening van fentanyl aan een NSIAD-patiënt zou waarschijnlijk **ADH-gemedieerde effecten versterken en hyponatriëmie verergeren**, wat het tegenovergestelde is van het therapeutische doel. Dit is een erkende beperking van op kennisgraaf gebaseerde modellen voor herontdekking van geneesmiddelen — biologische connectiviteit tussen knooppunten impliceert geen therapeutisch voordeel, en directionaliteit is belangrijk. De hoge TxGNN-score hier weerspiegelt vrijwel zeker een vals positief geval vanwege de topologische nabijheid tussen opiöïdsysteem- en waterhuishoudingsziekteknopen in de kennisgraaf.

---

## Klinisch onderzoeksbewijs

Momenteel geen gerelateerde klinische onderzoeken geregistreerd.

---

## Literatuurbewijs

Momenteel geen gerelateerde literatuur beschikbaar.

---

## Marktinformatie Nederland

Geen marktautorisaties voor fentanylbevattende producten zijn opgenomen in de CBG-MEB-gegevensset die in dit bewijspakket is opgenomen. Opgemerkt dient te worden dat fentanylproducten kunnen bestaan onder gecentraliseerde EMA-autorisatie (bijv. transdermale pleisters, buccale films voor doorbraakpijn bij kanker) of nationale RVG-registraties die niet in de actuele gegevensextractie zijn opgenomen. Beroepsbeoefenaren dienen rechtstreeks het openbare CBG-MEB-register te raadplegen voor de actuele autorisatiestatus.

---

## Veiligheidsoverwegingen

Raadpleeg de SmPC (Samenvatting van de Productkenmerken) voor volledige veiligheidsinformatie over fentanyl. Gezien de indeling van fentanyl als een Schedule II krachtige opiöïd met een smalle therapeutische index, moet bijzondere aandacht worden besteed aan het risico op respiratoire depressie, afhankelijkheid- en misbruikpotentieel, en interacties met CNS-depressiva en CYP3A4-inhibitoren.

---

## Conclusie en Vervolgstappen

**Besluit: Aanhouden**

**Grondslag:**
Dit is een L5-voorspelling zonder ondersteunend klinisch onderzoek of gepubliceerde literatuur, en mechanistische analyse identificeert waarschijnlijk een vals positief geval: stimulatie van ADH-afscheiding door fentanyl zou hyponatriëmie in NSIAD waarschijnlijk kunnen verergeren in plaats van deze te behandelen, wat betekent dat het biologische pad dat door TxGNN is geïdentificeerd in tegengestelde richting werkt.

**Om verder te gaan, is het volgende nodig:**
- Systematische literatuurreview om vast te stellen of opiöïdverbindingen ooit therapeutisch (in plaats van causaal) in NSIAD of SIADH zijn onderzocht
- Nefrologie-expertconsultatie om te beoordelen of er enig klinisch scenario bestaat waarin MOR-agonisme NSIAD-patiënten zou kunnen baten
- Mechanistische modellering van het netto-effect van fentanyl op V2R-onafhankelijke waterbinding in de context van gain-of-function AVPR2-mutaties
- Herevaluatie van de TxGNN-graafkanten die het opiöïdesysteem aan NSIAD koppelen om vast te stellen of directionaliteitsmetagegevens van kanten kunnen worden opgenomen om vals-positieve voorspellingen van dit type te verminderen

> **Opmerking:** De tweede TxGNN-voorspelling — **Tourette-syndroom** (score 99.05%) — draagt eveneens een L5-bewijsniveau en een aanhoudingsaanbeveling mee. Terwijl er een indirecte mechanistische verbinding bestaat via opiöïdmodulatie van striatale dopaminergische circuits (CSTC-lus), maken fentanyls hoge afhankelijkheidsrisico en extreem smalle therapeutische breedte het totaal ongeschikt voor langdurige behandeling van een chronische neuroontwikkelingsstoornis. Die voorspelling lijkt ook een topologisch vals positief geval te zijn en wordt niet aanbevolen voor verdere ontwikkeling.

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

