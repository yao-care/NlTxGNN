---
layout: default
title: Azathioprine
parent: Alleen modelvoorspelling (L5)
nav_order: 28
evidence_level: L5
indication_count: 10
---

# Azathioprine
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

# Azathioprine: Van Immunosuppressie naar Inflammatoire Darmziekten

## Samenvatting in één zin

Azathioprine is een gevestigde purine-antimetaboliet immunosuppressivum, historisch gebruikt voor preventie van orgaantransplantatafstoting en auto-immuunziekten. Het TxGNN-model voorspelt dat het effectief kan zijn voor **Inflammatoire Darmziekte (IBD)**, ondersteund door **50 klinische onderzoeken** en **20 publicaties** — opmerkelijk genoeg sluit deze voorspelling aan bij azathioprines reeds goedgekeurde gebruik voor IBD in Nederland en internationaal, wat een sterke validatie van de modelnauwkeurigheid vormt.

## Snelle samenvatting

| Item | Inhoud |
|------|--------|
| Originele indicatie | Immunosuppressie (auto-immuunziekten, preventie orgaantransplantatafstoting) |
| Voorspelde nieuwe indicatie | Inflammatoire Darmziekte |
| TxGNN voorspellingsscore | 99.52% |
| Evidentiëniveau | L1 (meerdere voltooide fase 3 RCT's) |
| NL-marketstatus | Op de markt (Azathioprine is geregistreerd in Nederland; opmerking: het bewijspakket bevat regelgegevens uit Taiwan met "Niet op de markt" in Taiwan) |
| Aantal goedkeuringen | Niet beschikbaar voor NL in deze dataset |
| Aanbevolen beslissing | Voortgang met waarborgen |

## Waarom is deze voorspelling redelijk?

Azathioprine is een prodrug van 6-mercaptopurine, die purine-synthese remt, lymfocytproliferatie reduceert en pro-inflammatoire cytokines (TNF-α, IL-6) onderdrukt. Door de aangepaste immuunrespons te dempen, controleert azathioprine effectief de gedereguleerde immuunactivering die chronische darmontstekking bij IBD aandrijft.

Inflammatoire darmziekte — omvattende zowel de ziekte van Crohn als colitis ulcerosa — is fundamenteel een immuun-gemedieerde aandoening waarin het immuunsysteem van de darm (adaptief en aangeboren) een ongepaste respons toont tegen darmbacteriën en mucosale antigenen. Azathioprines mechanisme van lymfocytgedreven ontstekingsonderdrukking spreekt rechtstreeks deze kernpathologie aan, waardoor de TxGNN-voorspelling mechanistisch goed onderbouwd is.

Opmerkelijk genoeg wordt deze voorspelling al klinisch gevalideerd: azathioprine werd goedgekeurd voor langetermijntherapie van de ziekte van Crohn in Nederland en wordt wereldwijd erkend als eerste-lijns immunomodulerende onderhoudstherapie voor zowel de ziekte van Crohn als colitis ulcerosa. Meerdere Cochrane-systematische reviews en baanbrekende onderzoeken (bijv. SONIC-onderzoek, NCT00094458) hebben de werkzaamheid bevestigd. De correcte identificatie door het TxGNN-model van deze gevestigde geneesmiddel-ziekterelatie dient als sterke positieve controle voor de voorspellende nauwkeurigheid van het model.

## Klinisch onderzoeksmateriaal

| Onderzoeksnummer | Fase | Status | Aantal deelnemers | Belangrijkste bevindingen |
|---------|------|------|------|---------|
| [NCT00094458](https://clinicaltrials.gov/study/NCT00094458) | Fase 3 | Voltooid | 508 | SONIC-onderzoek: IFX + AZA-combinatie versus AZA- of IFX-monotherapie in CD naïef voor immunomodulatoren en biologica; toonde superioriteit van combinatietherapie aan |
| [NCT05040464](https://clinicaltrials.gov/study/NCT05040464) | Fase 3 | Rekruteert | 166 | Head-to-head RCT vergelijking van AZA versus MTX als combinatiepartner met adalimumab bij de ziekte van Crohn |
| [NCT03185611](https://clinicaltrials.gov/study/NCT03185611) | Fase 3 | Onbekend | 120 | Rifaximin + thiopurine versus thiopurine alleen ter voorkoming van postoperatief endoscopisch recidief bij CD |
| [NCT00976690](https://clinicaltrials.gov/study/NCT00976690) | Fase 3 | Voltooid | 83 | AZA versus mesalazine ter voorkoming van postoperatief CD-recidief; beoordeelde AZA-superioriteit |
| [NCT07424040](https://clinicaltrials.gov/study/NCT07424040) | N/A | Nog niet gerecruteerd | 154 | Infliximab-monotherapie versus IFX + AZA-combinatie bij pediatrische ziekte van Crohn |
| [NCT02852694](https://clinicaltrials.gov/study/NCT02852694) | Fase 4 | Voltooid | 192 | Risicostratificeerdeproef: MTX versus AZA ter instandhouding van remissie bij laagrisico pediatrische CD |
| [NCT00554710](https://clinicaltrials.gov/study/NCT00554710) | Fase 4 | Voltooid | 129 | Top-down (vroege immunomodulatoren/biologica) versus step-up strategie bij nieuw gediagnosticeerde CD (Benelux-onderzoek) |
| [NCT00546546](https://clinicaltrials.gov/study/NCT00546546) | Fase 4 | Voltooid | 120 | Vroeg immunosuppressivumvoorschrift versus conventionele strategie op 3-jarig CD-verloop |
| [NCT05584228](https://clinicaltrials.gov/study/NCT05584228) | N/A | Nog niet gerecruteerd | 150 | SMART-onderzoek: AZA + subkutaan IFX versus ileocecale resectie bij symptomatische stricturerende dunne darm-CD |
| [NCT03464136](https://clinicaltrials.gov/study/NCT03464136) | Fase 3b | Voltooid | 386 | Ustekinumab versus adalimumab bij biologica-naïeve CD-patiënten die conventionele therapie, inclusief AZA, niet toepasten |

## Literatuurbewijsmateriaal

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|-----|------|------|---------|
| [29293971](https://pubmed.ncbi.nlm.nih.gov/29293971/) | 2018 | Review | J Crohn's Colitis | State-of-the-art overzicht van thiopurine (AZA/MP/TG) behandeling in IBD: indicaties, werkzaamheid en veiligheid door deskundigenteam |
| [19072367](https://pubmed.ncbi.nlm.nih.gov/19072367/) | 2008 | Mechanistische review | Expert Rev Gastroenterol Hepatol | 45 jaar klinische ervaring met thiopurines in IBD; sterke gegevens van RCT's en meta-analyses die werkzaamheid documenteren |
| [30889246](https://pubmed.ncbi.nlm.nih.gov/30889246/) | 2019 | Translationeel onderzoek | Inflamm Bowel Dis | AZA induceert autofagie via mTORC1 en PERK-paden — een nieuw moleculair mechanisme relevant voor CD-behandeling |
| [37586320](https://pubmed.ncbi.nlm.nih.gov/37586320/) | 2023 | Translationeel onderzoek | Cell Rep Med | Commensale bacteriën (B. wexlerae) bevorderen AZA-therapiefalen in IBD door 6-MP-biobeschikbaarheid te verminderen |
| [22072847](https://pubmed.ncbi.nlm.nih.gov/22072847/) | 2011 | Klinische review | World J Gastroenterol | Optimaliseren van 6-MP- en AZA-therapie: 6-TGN-niveaus correleren met werkzaamheid, 6-MMP met toxiciteit |
| [16048561](https://pubmed.ncbi.nlm.nih.gov/16048561/) | 2005 | Farmacogenetica-review | J Gastroenterol Hepatol | AZA/6-MP farmacogenetica en metaboliet monitoring; TPMT-polymorfismen en doseringsgevolgen |
| [36462311](https://pubmed.ncbi.nlm.nih.gov/36462311/) | 2023 | Farmacogenetica | Biomed Pharmacother | DNA-methylering van TPMT beïnvloedt AZA-farmacokinetiek bij VEO-IBD kinderen |
| [10499471](https://pubmed.ncbi.nlm.nih.gov/10499471/) | 1999 | Uitgebreide review | Scand J Gastroenterol Suppl | AZA klinische werkzaamheid- en veiligheidsupdate — documenteert goedkeuring voor de ziekte van Crohn in Nederland |
| [15177535](https://pubmed.ncbi.nlm.nih.gov/15177535/) | 2004 | Klinische review | Gastroenterol Clin North Am | Kritische review van 6-MP en AZA werkzaamheid en toxiciteiten in IBD |
| [30954317](https://pubmed.ncbi.nlm.nih.gov/30954317/) | 2019 | Review | Gastroenterol Hepatol | Bewijsmateriaal over optimale duur en stopzetting van thiopurinetherapie in IBD |

## Colitis Ulcerosa — Secundaire Voorspelling (Rang 9)

Het TxGNN-model voorspelt onafhankelijk ook azathioprine voor **colitis ulcerosa** (score: 99.33%, Evidentiëniveau: L1), wat een subtype van IBD is. Deze voorspelling wordt ondersteund door evenzo robuust bewijsmateriaal:

| Onderzoeksnummer | Fase | Status | Aantal deelnemers | Belangrijkste bevindingen |
|---------|------|------|------|---------|
| [NCT03101800](https://clinicaltrials.gov/study/NCT03101800) | Fase 3 | Onbekend | 84 | Lage-dosis AZA + allopurinol versus AZA-monotherapie in UC — evalueert rechtstreeks AZA-doseringstrategieën |
| [NCT02425852](https://clinicaltrials.gov/study/NCT02425852) | Fase 4 | Voltooid | 65 | Vroege AZA + IFX versus corticosteroïden + AZA voor acute ernstige UC |
| [NCT00537316](https://clinicaltrials.gov/study/NCT00537316) | Fase 3 | Geëindigd | 242 | IFX-monotherapie versus IFX + AZA versus AZA-monotherapie bij matig tot ernstig actieve UC |
| [NCT07235904](https://clinicaltrials.gov/study/NCT07235904) | Fase 4 | Rekruteert | 300 | MIRACLE-onderzoek: Mirikizumab versus AZA als standaard zorg bij nieuw gediagnosticeerde matig tot ernstige UC |
| [NCT07271069](https://clinicaltrials.gov/study/NCT07271069) | N/A | Nog niet gerecruteerd | 150 | Real-world: Ozanimod versus AZA voor UC in Japan |

**Belangrijkste UC-literatuur:**

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|-----|------|------|---------|
| [40013523](https://pubmed.ncbi.nlm.nih.gov/40013523/) | 2025 | Cochrane Systematische Review | Cochrane Database Syst Rev | Bijgewerkte Cochrane-review: AZA en 6-MP voor remissieinstandhouding in UC |
| [39586616](https://pubmed.ncbi.nlm.nih.gov/39586616/) | 2025 | RCT | Gut | ACTIVE-onderzoek: Top-down IFX + AZA versus AZA alleen bij acute ernstige UC respondeerend op IV-steroïden |
| [19392869](https://pubmed.ncbi.nlm.nih.gov/19392869/) | 2009 | Meta-analyse | Aliment Pharmacol Ther | Meta-analyse bevestigend AZA/6-MP werkzaamheid in UC |
| [27192092](https://pubmed.ncbi.nlm.nih.gov/27192092/) | 2016 | Cochrane Systematische Review | Cochrane Database Syst Rev | AZA en 6-MP voor UC-remissieinstandhouding |
| [9412914](https://pubmed.ncbi.nlm.nih.gov/9412914/) | 1997 | Klinische studie | J Clin Gastroenterol | AZA bij steroïde-resistente en steroïde-afhankelijke UC: klinische uitkomsten |

## Nederlands Marktinformatie

Het bewijspakket bevat regelgegevens uit Taiwan (azathioprine weergegeven als "Niet op de markt" in Taiwan met 0 licenties). Echter, **azathioprine is goed gevestigd in Nederland**:

| Item | Inhoud |
|------|--------|
| Marketstatus (NL) | Op de markt — azathioprine is decennialang geregistreerd en veel voorgeschreven in Nederland |
| CBG-MEB Goedkeuring | Beschikbaar als Imuran® en generieke formuleringen |
| Bekende NL-goedkeuringen | Ziekte van Crohn (gedocumenteerd sinds 1999, PMID 10499471), preventie orgaantransplantatafstoting, auto-immuun hepatitis, ernstige reumatoïde artritis, SLE, dermatomyositis |
| Darreichingsvormen | Orale tabletten (25 mg, 50 mg); injecteerbare formuleringen |
| SmPC-referentie | Raadpleeg de CBG-MEB Geneesmiddeleninformatiebank voor de huidige Nederlandse SmPC |

> **Opmerking:** Gedetailleerde CBG-MEB licentienummers (RVG-nummers) waren niet opgenomen in dit bewijspakket. Raadpleeg alstublieft de [CBG-MEB database](https://www.geneesmiddeleninformatiebank.nl/) voor volledige autorisatiegegevens.

## Andere TxGNN-voorspellingen

Het TxGNN-model genereerde 10 voorspellingen voor azathioprine. Afgezien van IBD en UC (hierboven besproken), zijn de overige 8 voorspellingen allemaal geclassificeerd als **In Afwachting** vanwege gebrek aan mechanistische rationale of afwezigheid van klinisch bewijsmateriaal:

| Rang | Ziekte | TxGNN-score | Evidentiëniveau | Aanbeveling | Rationale |
|------|--------|-------------|----------------|----------------|-----------|
| 1 | Colobomateuze microfthalmie-rhizomielische dysplasie syndroom | 99.99% | L5 | In Afwachting | Congenitale ontwikkelaandoening; geen immuun-gemedieerde pathologie; geen klinisch bewijsmateriaal |
| 2 | Brachidactylie-syndactyliesyndroom | 99.99% | L5 | In Afwachting | Genetisch skeletdefect (GDF5/BMPR1B); niet ontstekingsgevoelig; geen klinisch bewijsmateriaal |
| 3 | Vatbaarheid voor artrose | 99.70% | L5 | In Afwachting | Genetische vatbaarheidsfenotype; AZA kan genetische predispositie niet wijzigen |
| 4 | WHIM-syndroom | 99.68% | L5 | In Afwachting | Primaire immunodeficiëntie (CXCR4-mutatie); immunosuppressie is **gecontra-indiceerd** |
| 6 | Chronische granulomateuze ziekte (AR type 5) | 99.41% | L5 | In Afwachting | NADPH-oxidasedeficiëntie; verdere immunosuppressie zou infectierisico verergeren |
| 7 | Artrose | 99.40% | L4 | In Afwachting | Degeneratief/mechanisch pathologie; risico's van systemische immunosuppressie wegen niet op tegen voordelen |
| 8 | Granulomateuze ziekte met neutrofiel chemotatxisdefect | 99.37% | L5 | In Afwachting | Aangeboren immuundeficiëntie; AZA zou immuunfunctie verslechteren |
| 10 | Acromesomielische dysplasie, Hunter-Thompson type | 99.27% | L5 | In Afwachting | GDF5 homozygotische mutatie; gen-gedreven ontwikkelingdefect; geen behandelingslogica |

> **Belangrijk veiligheidsbericht:** Voorspellingen voor WHIM-syndroom (Rang 4), chronische granulomateuze ziekte (Rang 6) en granulomateuze ziekte met neutrofiel chemotatxisdefect (Rang 8) vertegenwoordigen immunodeficiëntiestanden waarbij azathioprine-gebruik **mechanistisch gecontra-indiceerd** zou zijn, aangezien verdere immunosuppressie levensbedreigend infecties zou kunnen veroorzaken.

## Veiligheidsoverwegingen

Raadpleeg alstublieft de SmPC (Samenvatting van de Productkenmerken) voor uitgebreide veiligheidsinformatie. De SmPC is beschikbaar via de [CBG-MEB Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/).

Belangrijke veiligheidsoverwegingen bekend uit gevestigd klinisch gebruik omvatten:
- **Beenmergonderdrukking:** Dosisafhankelijke beenmergonderdrukking (leukopenie, trombocytopenie, bloedarmoede); TPMT- en NUDT15-genotypering aanbevolen vóór aanvang
- **Hepatotoxiciteit:** Verhoogde niveaus van 6-MMP-metaboliet gerelateerd aan leverletsel
- **Infectierisico:** Toegenomen gevoeligheid voor opportunistische infecties vanwege immunosuppressie
- **Risico op maligniteit:** Langetermijngebruik gerelateerd aan verhoogd risico op lymfoproliferatieve stoornis (in het bijzonder hepatosplene T-cellymfoom bij combinatie met anti-TNF-middelen bij jonge mannen)
- **Farmacogenetica:** TPMT- en NUDT15-polymorfismen beïnvloeden significant geneesmiddelmetabolisme; genotypering vóór behandeling aanbevolen door EMA-richtlijnen
- **Geneesmiddelinteracties:** Allopurinol verhoogt 6-TGN-niveaus aanzienlijk (dosisreductie tot 25-33% vereist); 5-aminosalicylaten kunnen thiopurine-toxiciteit verhogen

> **Opmerking:** Gedetailleerde DDI-, waarschuwings- en contra-indicatiegegevens waren niet beschikbaar in dit bewijspakket. De hierboven genoemde items zijn afgeleid van het onderzochte klinische onderzoeks- en literatuurbewijsmateriaal.

## Conclusie en Vervolgstappen

**Beslissing: Voortgang met Waarborgen**

**Rationale:**
Azathioprine voor inflammatoire darmziekte vertegenwoordigt een gevalideerde voorspelling — het geneesmiddel is reeds een goedgekeurd en richtlijnaanbevolen therapie voor zowel de ziekte van Crohn als colitis ulcerosa in Nederland en wereldwijd. Meerdere voltooide fase 3 RCT's, Cochrane-systematische reviews en meta-analyses bieden L1-niveau bewijsmateriaal ter bevestiging van de werkzaamheid in het handhaven van steroïde-vrije remissie. De correcte identificatie door het TxGNN-model van deze gevestigde geneesmiddel-ziekterelatie dient als sterke positieve controle voor de algemene voorspellende validiteit van het model.

**Voor voortgang is het volgende nodig:**
- **NL-specifieke regelgegevens verkrijgen:** Huidige CBG-MEB-autorisatiegegevens (RVG-nummers, goedgekeurde indicaties, huidige SmPC) ophalen van de Geneesmiddeleninformatiebank
- **Compleet veiligheidsprofiel:** De huidige Nederlandse SmPC downloaden en parseren voor gedetailleerde waarschuwingen, contra-indicaties en geneesmiddelinteracties
- **Werkingsmechanisme-gegevens:** DrugBank API voor gestructureerde werkingsmechanisme-gegevens opvragen (bekend: purine-antimetaboliet → 6-MP → 6-TGN → lymfocytapoptose via Rac1-remming)
- **Farmacogenetisch screeningsprotocol:** TPMT- en NUDT15-genotypering in elk voorschrijfpad integreren, volgens huidige EMA- en DPWG (Dutch Pharmacogenetics Working Group) richtlijnen
- **Therapeutische geneesmiddelmonitoring:** Protocolestablishment voor 6-TGN- en 6-MMP-metaboliet monitoring voor dosiswoptimalisatie
- **Modelprestatie evalueren:** Gebruik deze gevalideerde voorspelling als benchmark ter beoordeling van TxGNN-modelbetrouwbaarheid voor andere, minder-gevestigde geneesmiddel-ziektevoorspellingen

---

*Dit rapport dient uitsluitend voor onderzoeksdoeleinden en stelt geen medisch advies voor. Geneesmiddelherwerkingskandidaten vereisen klinische validatie vóór toepassing. Alle behandelingsbeslissingen moeten worden genomen door gekwalificeerde zorgverleners in overeenstemming met huidige klinische richtlijnen en de toepasselijke SmPC.*

*Gegevenscutoff: 2026-04-03 | Bewijspakketversie: v4 | Kandidaat-ID: TW-DB00993-multi*

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

