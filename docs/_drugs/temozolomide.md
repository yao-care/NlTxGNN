---
layout: default
title: Temozolomide
parent: Sterk bewijs (L1-L2)
nav_order: 118
evidence_level: L1
indication_count: 2
---

# Temozolomide
{: .fs-9 }

Bewijsniveau: **L1** | Voorspelde indicaties: **2** 
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

# Temozolomide: Van maligne glioom tot volwassen astrocytische tumor

## Samenvatting in één zin

Temozolomide is een oraal alkylerende chemotherapeuticum dat internationaal wordt erkend als standaardbehandeling voor maligne gliomen, waaronder glioblastoma multiforme (GBM) en anaplastische astrocytoom, hoewel het momenteel niet is geregistreerd bij de CBG-MEB in Nederland.
Het TxGNN-model voorspelt dat het effectief kan zijn voor **volwassen astrocytische tumor**,
met **2 klinische onderzoeken** en **20 publicaties** die deze richting momenteel ondersteunen — inclusief meerdere richtinggevende Phase 3 RCT's die TMZ-gebaseerde chemoradiotherapie als de wereldwijde ruggengraat van hersentumortherapie hebben gevestigd.

---

## Snellig overzicht

| Item | Inhoud |
|------|--------|
| Oorspronkelijke indicatie | Glioblastoma multiforme / maligne astrocytoom (internationaal goedgekeurd; niet geregistreerd bij CBG-MEB) |
| Voorspelde nieuwe indicatie | Volwassen astrocytische tumor |
| TxGNN-voorspellingsscore | 99.36% |
| Bewijsniveau | L1 |
| Markeringsstatus Nederland | Niet geregistreerd |
| Aantal autorisaties | 0 |
| Aanbevolen besluit | Doorgaan met guardrails |

---

## Waarom is deze voorspelling redelijk?

Temozolomide is een imidazotetazine-klasse alkylerende stof die door spontane hydrolyse bij fysiologische pH wordt omgezet naar zijn actieve metaboliet MTIC (monomethyl triazenoimidazole carboxamide). MTIC methyleert DNA op de O6-positie van guanine, wat letsels veroorzaakt die de mismatch repair-weg overweldigt en uiteindelijk apoptose triggert. Cruciaal is dat temozolomide bijna volledige orale biobeschikbaarheid (~100%) bereikt en effectief de bloed-hersenbarrière penetreert — een farmacokinetisch profiel dat het uniek geschikt maakt voor centraal zenuwstelsel maligniteiten waarbij systemische middelen doorgaans falen.

Volwassen astrocytische tumoren — omvattend glioblastoma multiforme (WHO klasse IV), anaplastische astrocytoom (klasse III) en diffuse astrocytoom (klasse II) — behoren tot de meest proliferatieve primaire hersentumoren bij volwassenen. In tumoren waar de MGMT (O6-methylguanine-DNA methyltransferase) genpromoter is gemethyleerd, is MGMT-eiwitexpressie onderdrukt, wat betekent dat de O6-guanineletsels die door temozolomide worden geïnduceerd niet efficiënt kunnen worden hersteld. Deze MGMT-methyleringsstatus is de definitieve voorspellende biomarker voor TMZ-respons geworden, wat zijn selectieve maar aanzienlijke werkzaamheid in deze tumorklasse verklaart en biomarker-gestuurde patiëntselectie mogelijk maakt.

De TxGNN-voorspelling is daarom niet alleen mechanistisch goed onderbouwd — zij wordt rechtstreeks ondersteund door een van de meest robuuste klinische bewijsbases in neuro-oncologie. De richtinggevende EORTC-NCIC Phase 3-studie (Stupp et al., 2005) vestigde gelijktijdige en aanvullende temozolomide met radiotherapie als de internationale standaardbehandeling voor recent gediagnosticeerde GBM, waarbij de 5-jaarsvolgup duurzaam overlevingsvoordeel bevestigde. Daaropvolgende Phase 3-studies hebben TMZ in meerdere astrocytische tumorreducties en patiëntenpopulaties gevalideerd, inclusief bejaarde patiënten (NOA-08-studie) en MGMT-gemethyleerde GBM die intensivering met lomustine-TMZ combinaties ondergaan (CeTeG/NOA-09). De huidige afwezigheid van een CBG-MEB-registratie — eerder dan enig gebrek aan klinisch bewijs — is de primaire barrière voor formeel gebruik binnen het Nederlandse gezondheidsstelsel.

---

## Klinisch onderzoeksbewijs

| Proefnummercode | Fase | Status | Aantal deelnemers | Belangrijkste bevindingen |
|---------|------|------|------|---------|
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Fase 3 | Voltooid | 500 | Gerandomiseerde vergelijking van temozolomide-monotherapie vs. PCV (procarbazine + lomustine + vincristine) in herhaalde WHO klasse III–IV astrocytische tumoren; grootste directe RCT in deze populatie met rechtstreekse vergelijkende werkzaamheidsgegevens voor TMZ |
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Fase 1 | Voltooid | 26 | Dosisvindingsstudie van XL184 (cabozantinib, een VEGFR2/MET/RET-inhibitor) toegevoegd aan TMZ en radiotherapie in recent gediagnosticeerde glioblastoma; TMZ + RT diende als het basisregime en veiligheids- en farmacokinetische profielen werden gekarakteriseerd voor de combinatie |

---

## Literatuurbewijs

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|-----|------|------|---------|
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | Phase 3 RCT | N Engl J Med | Richtinggevende Stupp-studie: RT + gelijktijdige/aanvullende TMZ vs. RT alleen in recent gediagnosticeerde GBM; vestigde TMZ + RT als wereldwijde standaardbehandeling met aanzienlijk verbeterde mediane OS |
| [19269895](https://pubmed.ncbi.nlm.nih.gov/19269895/) | 2009 | Phase 3 RCT (5-jaarsvolgup) | Lancet Oncol | EORTC-NCIC 5-jaargegevens bevestigden duurzaam overlevingsvoordeel van TMZ + RT; MGMT-promotermethylering werd bevestigd als de belangrijkste voorspellende biomarker voor respons |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | Phase 3 RCT | Lancet Oncol | NOA-08-studie: dosisintensieve TMZ-monotherapie niet inferieur aan RT alleen in bejaarde patiënten met maligne astrocytoom; ondersteunt TMZ als eerstelijnsoptie wanneer radiotherapie niet mogelijk is |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | Phase 3 RCT | N Engl J Med | Toevoeging van bevacizumab aan standaard TMZ + RT verbeterde OS niet in recent gediagnosticeerde GBM; bevestigde opnieuw TMZ + RT als onveranderde standaardbehandeling |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | Phase 3 RCT | JAMA | EF-14-studie: Tumour Treating Fields (TTFields) + TMZ vs. TMZ alleen tijdens GBM-onderhoud; TTFields-toevoeging verbeterde OS verder met TMZ als onmisbare ruggengraat |
| [25920709](https://pubmed.ncbi.nlm.nih.gov/25920709/) | 2015 | Phase 3 RCT / Cohort | J Neuro-Oncol | Cohort met anaplastische astrocytoom en anaplastische oligo-astrocytoom behandeld met RT + TMZ; ondersteunt uitbreiding van TMZ-werkzaamheid buiten GBM naar klasse III astrocytische tumoren |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | Phase 3 RCT | Lancet | CeTeG/NOA-09: Lomustine + TMZ-combinatie superieur aan TMZ-monotherapie in MGMT-gemethyleerde recent gediagnosticeerde GBM; benadrukt MGMT-gestratificeerde geïntensiveerde behandeling als ontstane standaard |
| [36809318](https://pubmed.ncbi.nlm.nih.gov/36809318/) | 2023 | Review | JAMA | Uitgebreid overzicht van primaire maligne hersentumoren bij volwassenen; TMZ-gebaseerde chemoradiotherapie bevestigd als huidige standaard; vat evoluerende therapeutische landschap samen |
| [40779733](https://pubmed.ncbi.nlm.nih.gov/40779733/) | 2025 | Phase 3 RCT | J Clin Oncol | NRG BN007: Dubbele immuuncontrolepuntblokkade (ipilimumab + nivolumab) vs. TMZ in MGMT-ongemethyleerde recent gediagnosticeerde GBM; TMZ gebruikt als actieve comparatorarm onderstreepend zijn voortgezette verwijzingsstandaardstatus |
| [10914698](https://pubmed.ncbi.nlm.nih.gov/10914698/) | 2000 | Vroege klinische / Review | Clin Cancer Res | Basisartikel karakteriserend TMZ's mechanisme, orale farmacokinetiek en vroege klinische werkzaamheid in maligne glioom; vestigde de farmacologische rationale voor haar ontwikkeling als het primaire centraal zenuwstelsel alkylerende middel |

---

## Marktinformatie Nederland

Temozolomide is momenteel **niet geregistreerd** bij de CBG-MEB (College ter Beoordeling van Geneesmiddelen). Er zijn geen RVG autorisatienummers aanwezig in het huidige bewijspakket.

> **Opmerking voor beoordeling:** Clinici en apothekers dienen te verifiëren of temozolomide beschikbaar is in Nederland via het EMA centraal geautoriseerde traject, benoemde patiëntenprogramma's of bereidingenservice van ziekenhuisapotheek onder Nederlandse farmaceutische regelgeving. De afwezigheid van een CBG-MEB-record in dit bewijspakket dient te worden afgestemd met EMA-records voor centrale autorisatie voordat u concludeert dat het geneesmiddel niet beschikbaar is.

---

## Cytotoxiciteit

| Item | Inhoud |
|------|--------|
| Cytotoxiciteitclassificatie | Conventioneel cytotoxicum — alkylerende middel (imidazotetazine / triazeen klasse) |
| Risico op myelosuppressie | Matig tot hoog — dosisverhogingbeperkende toxiciteiten omvatten lymfopenie (CD4+ T-cel depletie) en trombocytopenie; preventie van *Pneumocystis jirovecii* pneumonie (PJP) is vereist tijdens de gelijktijdige chemoradiotherapiefase |
| Emetogeniteitclassificatie | Matig — profylactische anti-emetica (5-HT3-antagonist ± dexamethason) worden aanbevolen vóór elke orale dosis |
| Controlepunten | Volledig bloedonderzoek (VBO) inclusief absoluut lymfocytenaantal vóór elke cyclus; leverinctests (LFTs); nierfunctie; MGMT-promotermethyleringstatus dient vóór aanvang te worden beoordeeld voor behandelplanning |
| Veiligheidsmaatregelen bij hantering | Ja — temozolomide-capsules moeten volgens richtlijnen voor cytotoxische medicijnen worden verwerkt; capsules mogen niet worden geopend of verbrijzeld; PSE en hantering in gesloten systeem zijn vereist voor farmacievoorbereiding |

---

## Veiligheidsbedenkingen

Raadpleeg alstublieft de SmPC (Samenvatting van de Productkenmerken) voor volledige veiligheidsinformatie, inclusief belangrijkste waarschuwingen, contra-indicaties en geneesmiddel-geneesmiddelinteracties.

---

## Conclusie en volgende stappen

**Besluit: Doorgaan met guardrails**

**Onderbouwing:**
Temozolomide bezit een van de sterkste bewijsbases in neuro-oncologie, met meerdere voltooide Phase 3 RCT's — inclusief de definitieve EORTC-NCIC Stupp-studie — die TMZ + radiotherapie als de wereldwijde standaardbehandeling voor volwassen astrocytische tumoren, met name GBM, hebben gevestigd. Het L1-bewijsniveau en de hoge TxGNN-voorspellingsscore (99.36%) ondersteunen volledig doorgaan, op voorwaarde dat de vastgestelde regelgeving en veiligheidsdatagaten binnen het Nederlandse gezondheidszorgsysteem worden aangepakt.

**Om door te gaan is het volgende nodig:**

- **Regelgevingsverificatie:** Breng de CBG-MEB registratiestatus in overeenstemming met EMA-records voor centraal geautoriseerde producten voor temozolomide (Temodal®); indien een EMA-autorisatie bestaat, werk het bewijspakket dienovereenkomstig bij en bevestig SmPC-toegankelijkheid voor Nederlandse voorschrijvers
- **Veiligheidsprofiel:** Verkrijg de huidige Nederlandse SmPC om belangrijkste waarschuwingen, contra-indicaties en geneesmiddel-geneesmiddelinteracties af te ronden — momenteel afwezig uit dit bewijspakket
- **Biomarker-infrastructuur:** Bevestig beschikbaarheid van MGMT-promotermethyleringstesten in Nederlandse neuropathologische centra, aangezien deze biomarker essentieel is voor het sturen van behandelbeslissingen en patiëntselectie
- **Terugbetalingstraject:** Indien formele registratie of uitgebreid gebruik wordt nagestreefd, betrek Zorginstituut Nederland (ZIN) om terugbetalingsberechtinging onder de GVS (Geneesmiddelenvergoedingssysteem) te beoordelen
- **Klinische governance:** Definieer criteria voor patiëntgeschiktheid (prestatiestatus, leeftijd, MGMT-status, tumorgraad) in overeenstemming met huidige richtlijnen van Nederlandse neuro-oncologieverenigingen en sluit aan bij multidisciplinaire tumorboardprotocollen

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

