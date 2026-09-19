---
layout: default
title: Olanzapine
parent: Alleen modelvoorspelling (L5)
nav_order: 99
evidence_level: L5
indication_count: 3
---

# Olanzapine
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

# Olanzapine: van schizofrenie/bipolaire stoornis naar benigne paroxismale torticollis van zuigelingen

## Samenvatting in één zin

Olanzapine is een gevestigde tweede generatie (atypische) antipsychoticum, internationaal goedgekeurd voor schizofrenie en bipolaire stoornis.
Het TxGNN-model voorspelt dat het relevant kan zijn voor **benigne paroxismale torticollis van zuigelingen (BPTI)**,
met momenteel **0 klinische trials** en **0 publicaties** die deze richting ondersteunen.
Belangrijk is dat een mechanistische review aangeeft dat dit waarschijnlijk een **omgekeerd signaal** is — de dopamine D2-antagonisme van olanzapine is een bekende *oorzaak* van geneesmiddel-geïnduceerde torticollis, niet een behandeling ervoor.

---

## Snelle samenvatting

| Item | Inhoud |
|------|--------|
| Originele indicatie | Schizofrenie; Bipolaire stoornis *(NL-autorisatiegegevens niet opgehaald — zie opmerking hieronder)* |
| Voorspelde nieuwe indicatie | Benigne paroxismale torticollis van zuigelingen |
| TxGNN-voorspellingsscore | 99.54% |
| Evidentiëniveau | L5 |
| NL-marktstatus | Niet geregistreerd *(gegevens kunnen incompleet zijn — zie opmerking hieronder)* |
| Aantal autorisaties | 0 |
| Aanbevolen besluit | Wacht |

---

## Waarom is deze voorspelling redelijk?

Gedetailleerde mechanisme-van-werkingsgegevens waren niet beschikbaar in dit Evidence Pack. Op basis van gevestigde farmacologische kennis is olanzapine een multi-receptorantagonist met bijzonder sterke affiniteit voor dopamine D2-receptoren en serotonine 5-HT2A-receptoren, evenals histamine H1-, muscarinische en alfa-adrenerge receptoren. De bewezen therapeutische toepassing omvat schizofrenie, acute bipolaire manie, en — in combinatie met fluoxetine (als Symbyax) — bipolaire depressie.

Benigne paroxismale torticollis van zuigelingen (BPTI) wordt volgens de ICHD-3 geclassificeerd als een migraine-variant bij kinderen. Het presenteert zich als herhaalde, zelf-limiterende episodes van hoofdkanteling bij zuigelingen en peuters, met een veronderstelde pathofysiologie waarbij ionkanaal-dysfunctie en het trigeminovasculaire systeem betrokken zijn — een mechanisme dat verschilt van de dopaminerge aangrijpingspunten van olanzapine.

**Kritische mechanistische overweging:** In plaats van een echt therapeutisch signaal is deze TxGNN-voorspelling hoogstwaarschijnlijk een **omgekeerd mechanistisch artefact**. Acute geneesmiddel-geïnduceerde dystonie en torticollis zijn goed erkende bijwerkingen van D2-receptorantagonisten, waaronder olanzapine. De hoge score van het model weerspiegelt vrijwel zeker *nabijheid in de kennisgraaf* — het "torticollis"-symptoomknooppunt wordt gedeeld tussen BPTI en het bijwerkingenprofiel van olanzapine — in plaats van enige positieve behandelingsrelatie. Het toepassen van olanzapine bij BPTI zou mechanistisch gecontra-indiceerd zijn en zou de aandoening actief kunnen verergeren.

---

## Bewijs van klinische trials

Momenteel geen gerelateerde klinische trials geregistreerd.

---

## Literatuurbewijzen

Momenteel geen gerelateerde literatuur beschikbaar.

---

## Informatie over de Nederlandse markt

Er werden geen CBG-MEB-marketingautorisaties voor olanzapine opgehaald in deze dataset. Dit is waarschijnlijk een **lacune in de gegevensverzameling**: olanzapine (merknaam Zyprexa en meerdere generieke equivalenten) is een centraal geautoriseerd geneesmiddel in de Europese Unie en wordt naar verwachting in Nederland beschikbaar gesteld onder EMA-autorisatie. Voorschrijvers moeten de huidige status rechtstreeks verifiëren via het [CBG-MEB-productregister](https://www.cbg-meb.nl/) of de [EMA European Public Assessment Report (EPAR)](https://www.ema.europa.eu/).

---

## Veiligheidsconsideraties

Raadpleeg de SmPC (Samenvatting van de productkenmerken) voor volledige veiligheidsinformatie. In het bijzonder, gezien de mechanistische overweging hierboven, zijn de secties over **extrapiramidale bijwerkingen**, **acute dystonie** en **gebruik in pediatrische populaties** vooral relevant voor elke beoordeling van deze voorspelde indicatie.

---

## Conclusie en volgende stappen

**Besluit: Wacht**

**Argumentatie:**
Het TxGNN-model kent een hoge score toe op basis van nabijheid in de kennisgraaf via een gedeeld "torticollis"-symptoomknooppunt, maar mechanistische analyse identificeert dit als een **omgekeerd signaal**: olanzapine-geïnduceerde acute dystonie/torticollis is een bekende ongewenste geneesmiddelreactie, waardoor het middel eerder de aandoening zal *veroorzaken* dan behandelen. Er is geen ondersteunend bewijs van klinische trials of literatuur. Deze kandidaat mag onder de huidige formulering niet verder gaan.

**Voor vervolg is het volgende nodig:**
- Onafhankelijke mechanistische review door een klinisch farmacoloog om het omgekeerde signaal formeel te documenteren en deze kandidaat af te sluiten
- Ophaaling van NL CBG-MEB-/EMA-autorisatiegegevens om het marktstatusrecord voor olanzapine te corrigeren
- Ophaaling van de volledige SmPC (inclusief waarschuwingen voor extrapiramidale effecten en pediatrische contra-indicaties) om het veiligheidsprofiel aan te vullen
- Aanvulling van MOA-gegevens van DrugBank (gemarkeerd als DG002) voor robuuste mechanistische analyse van alle voorspelde indicaties
- Overweging van de **Rank 2 (Agorafobie, L3)** en **Rank 3 (Dysthyme stoornis, L3)** voorspelde indicaties, die een plausibeler mechanistisch rationale en bestaande literatuur hebben, en meer veelbelovende herpositioneringskandidaten voor verdere evaluatie kunnen zijn

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

