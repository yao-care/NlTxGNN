---
layout: default
title: Dienogest
parent: Matig bewijs (L3-L4)
nav_order: 53
evidence_level: L3
indication_count: 10
---

# Dienogest
{: .fs-9 }

Bewijsniveau: **L3** | Voorspelde indicaties: **10** 
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

# Dienogest: Van Endometriose naar Amenorroe

## Samenvatting in één zin

Dienogest is een vierde-generatie selectieve progestine die veel gebruikt wordt voor de behandeling van endometriose en werkt door onderdrukking van de hypothalamus-hypofyse-eierstok (HPO) as om estrogeen-gedreven ectopische endometriale groei te verminderen.
Het TxGNN-model voorspelt dat het effectief kan zijn voor **Amenorroe**, met **4 klinische onderzoeken** en **6 publicaties** die momenteel zijn opgehaald — echter, mechanistische analyse onthult dat dit bijna zeker een **contra-directionele voorspelling** is: Dienogest *veroorzaakt* amenorroe als een opzettelijk therapeutisch effect in endometriose-management, in plaats van primaire amenorroe als aandoening te behandelen.

## Snel overzicht

| Item | Inhoud |
|------|--------|
| Originele indicatie | Endometriose (bekende standaard klinische toepassing; geen CBG-MEB markttoelating in Nederland op record) |
| Voorspelde nieuwe indicatie | Amenorroe |
| TxGNN-voorspellingsscore | 99.71% |
| Bewijsniveau | L3 |
| NL-marktpositie | Niet op de markt in Nederland |
| Aantal toelatingsdossiers | 0 |
| Aanbevolen besluit | In onderzoek houden |

## Waarom is deze voorspelling redelijk?

Op dit moment zijn gedetailleerde werkingsmechanisme-gegevens niet beschikbaar in het verstrekte bewijspakket. Op basis van gevestigde farmacologische kennis is Dienogest een vierde-generatie synthetische progestine met zeer selectieve progesteronreceptor-agonist activiteit en minimale androgene, estrogenische of glucocorticoïde effecten. Het behandelt endometriose door onderdrukking van de HPO-as: inhibitie van ovulatie en follikelrijping, verlaging van endogene oestradiolconcentraties, en inductie van endometriale decidualisatie en atrofie — waarbij amenorroe een direct en beoogd therapeutisch resultaat is.

Dit is precies waar de mechanistische paradox ligt. Amenorroe is geen aandoening die Dienogest is ontworpen om *te behandelen* — het is een aandoening die Dienogest *veroorzaakt*, opzettelijk, als hoeksteen van zijn werkzaamheid tegen ectopisch endometraal weefsel. Het voorschrijven van Dienogest om primaire of secundaire amenorroe te behandelen bij een patiënt die al geen menstruatie heeft, zou farmacologisch tegenstrijdig zijn en zou de onderliggende hormonale onderdrukking kunnen verergeren.

Het TxGNN-model heeft waarschijnlijk de statistische co-voorkomen van Dienogest, endometriose en amenorroe in de kennisgraaf vastgesteld zonder onderscheid te maken tussen de oorzakelijke richting van de relatie. Dit is een erkende beperking van op grafen gebaseerde herpositioneringsmodellen: ze kunnen sterk geassocieerde nodenparen identificeren zonder af te leiden of het geneesmiddel de ziekte veroorzaakt, behandelt of gewoon correleert met de ziekte. **Deze voorspelling moet worden geclassificeerd als een contra-directioneel modelartefact, geen echte herpositioneringskans, en kan waardevol zijn om aan te vlaggen als signaal voor pipelinekwaliteit.**

## Klinisch onderzoeksbewijs

> **Belangrijk context**: Alle opgehaalde klinische onderzoeken betreffen de gevestigde endometriose-indicatie van Dienogest, niet het behandelen van amenorroe. Amenorroe in deze onderzoeken verschijnt als uitkomstmaat of ongewenst effect — niet als het therapeutische doel. Geen onderzoeken naar het behandelen van amenorroe met Dienogest werden geïdentificeerd.

| Onderzoeksnummer | Fase | Status | Inschrijving | Belangrijkste bevindingen |
|---------|------|------|------|---------|
| [NCT07164183](https://clinicaltrials.gov/study/NCT07164183) | Fase 3 | Werving aan de gang | 290 | Niet-inferioriteits RCT vergelijking van Indinol Forto® 200 mg versus Visanne® (Dienogest 2 mg) voor endometriose; amenorroe-percentage waarschijnlijk secundaire uitkomstmaat |
| [NCT02425462](https://clinicaltrials.gov/study/NCT02425462) | N/A | Voltooid | 895 | Grote prospectieve observationele cohort die Visanne® werkzaamheid en langetermijnveiligheid beoordeelt voor kwaliteit van leven bij Aziatische vrouwen met endometriose in routinematige klinische settings |
| [NCT04495855](https://clinicaltrials.gov/study/NCT04495855) | N/A | Voltooid | 968 | Real-world observationele studie van Dienogest bij endometriose; evalueert symptoomcontrole, recidief na behandeling stoppen, en verdraagzaamheidsprofiel |
| [NCT07204093](https://clinicaltrials.gov/study/NCT07204093) | N/A | Actief, geen werving aan de gang | 138 | Vergelijking van Dienogest versus drospirenon gecombineerd met transdermaal oestradiol bij endometriose; evalueert patiënttevredenheid en verdraagzaamheid |

## Literatuurbewijzen

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|------|------|------|---------|
| [39090694](https://pubmed.ncbi.nlm.nih.gov/39090694/) | 2024 | Systematische review | BMC Pharmacology & Toxicology | Bayesiaanse analyse van Dienogest bijwerkingen in meerdere onderzoeken; identificeert onregelmatige bloedingen en amenorroe als frequente uitkomsten — wat amenorroe als effect *van* het geneesmiddel bevestigt, niet als behandelde aandoening |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Narratieve review | Reviews in Endocrine & Metabolic Disorders | Overzicht van hormonale endometriose-behandelingen; beschrijft oestrogeenafhankelijkheid en progesteronresistentie als sleutelgebeurtenissen in pathogenese; behandelt Dienogest's HPO-as onderdrukking mechanisme |
| [41329046](https://pubmed.ncbi.nlm.nih.gov/41329046/) | 2026 | Farmacologische studie | European Journal of Contraception & Reproductive Health Care | Kwantitatieve farmacologische analyse van Dienogest 2 mg inhibitieratio; amenorroe-inductie expliciet beschreven als mechanisme van therapeutische actie bij endometriose |
| [29161960](https://pubmed.ncbi.nlm.nih.gov/29161960/) | 2018 | Prospectieve cohort | Reproductive Sciences | Retrospectieve cohort van 514 vrouwen met ovariale endometrioom in 7 ziekenhuizen; evalueert langetermijnwerkzaamheid en veiligheid van Dienogest voorbij 12 maanden inclusief recidiefpercentages |
| [34918698](https://pubmed.ncbi.nlm.nih.gov/34918698/) | 2021 | Case report | Medicine | Ovariale granulosaceltumor bij patiënt met PCOS; minimale directe relevantie voor Dienogest of amenorroe als behandelingsdoel |
| [40543564](https://pubmed.ncbi.nlm.nih.gov/40543564/) | 2025 | Review/Beeldvorming | Journal of Pediatric and Adolescent Gynecology | Geavanceerde 3D-visualisatietechnieken voor obstructieve Müllerische anomalieën; minimale directe relevantie voor Dienogest-herpositionering |

## Informatie Nederlandse markt

Dienogest heeft momenteel **geen markttoelating** van het CBG-MEB (College ter Beoordeling van Geneesmiddelen) in Nederland. Geen RVG-nummers zijn op record.

> Dienogest wordt op de markt gebracht als Visanne® 2 mg in meerdere EU-lidstaten (goedgekeurd via nationale procedures en EMA scientific opinion), evenals in Japan, Zuid-Korea en Australië. Elk gebruik in Nederland zou ofwel een nieuwe CBG-MEB markttoelatingsprocedure vereisen, een EMA gecentraliseerde procedure indiening, of een compassionate use (benoemde patiënt) route onder Nederlandse geneesmiddelenwetgeving.

## Veiligheidsopmerkingen

Raadpleeg de SmPC (Samenvatting van de Productkenmerken) voor volledige veiligheidsinformatie. Er waren geen waarschuwingen, contra-indicaties of geneesmiddelen interactiegegevens beschikbaar in het huidige bewijspakket.

> Voor oriëntatie: op basis van EMA openbare beoordelingsrapporten voor Visanne® in andere EU-lidstaten, omvat het bekende veiligheidsprofiel van Dienogest onregelmatige uterusbloeding, hoofdpijn, depressieve stemming, verminderde libido, acne, gewichtstoename, en potentiële impact op botmineraaldichtheid bij langdurig gebruik. Gebruik tijdens zwangerschap en bij patiënten met niet-gediagnosticeerde abnormale vaginale bloeding is tegen-geïndiceerd volgens het originele SmPC.

## Conclusie en volgende stappen

**Besluit: In onderzoek houden**

**Motivering:**
De TxGNN-voorspelling voor amenorroe wordt beoordeeld als een **contra-directioneel modelartefact** — Dienogest induceert farmacologisch amenorroe als onderdeel van zijn endometriose-mechanisme, en er is geen klinisch bewijs voor gebruik als behandeling voor primaire of secundaire amenorroe. Voortgang met deze indicatie als herpositioneringskans zou farmacologisch ongerechtvaardigd zijn op basis van huidig bewijs.

**Om voort te gaan, is het volgende nodig:**

- **Verplicht**: Beoordeling door klinische farmacoloog om de contra-directionele classificatie formeel te bevestigen en deze kandidaat in de pijplijn te sluiten
- **Pipelinekwaliteitsactie**: Markeer dit voorspellingspaar (Dienogest ↔ Amenorroe) als een bekend modelartefact voor de NlTxGNN contra-directionele voorspellingsaudit
- **Voor volledigheid**: Extraheer het volledige MOA-profiel uit DrugBank (DB09123) en EMA SmPC om voor toekomstige vergelijkbare progestinekanidaten te documenteren
- **Indien enig amenorroe-subtype verdere beoordeling rechtvaardigt** (bijv. progesterone-uitdagingstest bij evaluatie van amenorroe-etiologie), moet een aparte, nauw omschreven klinische vraag met een gynaecoloog worden geformuleerd voordat herbeoordeling wordt overwogen

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

