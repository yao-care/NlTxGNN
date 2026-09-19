---
layout: default
title: Pimecrolimus
parent: Alleen modelvoorspelling (L5)
nav_order: 104
evidence_level: L5
indication_count: 4
---

# Pimecrolimus
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

# Pimecrolimus: Van Atopische Dermatitis naar Seborrheïsche Dermatitis

## Samenvatting in één zin

Pimecrolimus (merknaam: Elidel) is een topische calcineurine-remmer, oorspronkelijk ontwikkeld voor de behandeling van atopische dermatitis (eczeem), die lokale huidontsteking onderdrukt door T-cel-activatie te blokkeren zonder de huidverdunning-bijwerkingen van corticosteroïden.
Het TxGNN-model voorspelt dat het mogelijk effectief kan zijn voor **Seborrheïsche Dermatitis**,
met **1 klinisch onderzoek** en **18 publicaties** die deze richting momenteel ondersteunen.

---

## Snelle Overzicht

| Item | Inhoud |
|------|--------|
| Oorspronkelijke indicatie | Atopische dermatitis (mild tot matig; contextueel – geen CBG-MEB-registratie gevonden) |
| Voorspelde nieuwe indicatie | Seborrheïsche Dermatitis |
| TxGNN-voorspellingsscore | 99.73% |
| Bewijsniveau | L2 (1 voltooid fase 2 RCT) |
| NL-marktatus | Niet in de handel (geen CBG-MEB nationale autorisaties in dossier) |
| Aantal autorisaties | 0 |
| Aanbevolen Besluit | Doorgaan met Waarborgen |

> **Opmerking over marktatus:** Pimecrolimus (Elidel) beschikt over een centraal geautoriseerde EMA-handelstoestemming (geldig in alle EU/EEA-lidstaten, inclusief Nederland) voor atopische dermatitis. De CBG-MEB-dataset toont 0 nationale autorisaties, wat waarschijnlijk het ontbreken van een *nationale* procedure weerspiegelt — dit moet worden gekruisverwijzerd met de EMA-productendatabase alvorens tot enige regelgevingsaanvraag over te gaan.

---

## Waarom is deze voorspelling redelijk?

Pimecrolimus is een lid van de calcineurine-remmers (TCI). Het werkt door binding aan macrophyline-12 (FKBP-12) en inhibitie van calcineurine, waardoor de defosforylering van NFAT (Nuclear Factor of Activated T-cells) wordt voorkomen. Dit blokkeert de transcriptie van pro-inflammatoire cytokines — inclusief IL-2, IL-4, IFN-γ en TNF-α — selectief in T-cellen en mestcellen. Kritisch is dat het geen dermale atrofie veroorzaakt, wat het bijzonder geschikt maakt voor langdurig gebruik op gevoelige gezichtsgebieden.

Seborrheïsche dermatitis omvat een Th1/Th17-immuunonbalans, uitgelokt door commensale levens van het *Malassezia*-geslacht in de huid, wat leidt tot verstoring van de epidermale barrière en lokale cytokineuitscheiding. Deze immuun-gedreven ontstekingscomponent is mechanistisch afgestemd op pimecrolimus's werkingsmechanisme: door onderdukking van de lokale cytokinine-cascade kan pimecrolimus de erytheem, schilfers en jeuk die de aandoening karakteriseren verminderen. Het steroïdenvrije profiel is een aanvullend klinisch voordeel, aangezien seborrheïsche dermatitis vaak het gezicht en de hoofdhuid aantast — gebieden waar aan corticosteroïdgerelateerde bijwerkingen (teleangiëctasie, rosacea-achtige erupties, huidatrofie) een echt risico vormen.

Zowel atopische dermatitis als seborrheïsche dermatitis zijn chronische, relapserend verlopen ontstekingsziekten van de huid waarin immuun-gemedieerde huidbarrièredysfunctie een centrale rol speelt. Hoewel *Malassezia*-kolonisatie een schimmelcomponent aan seborrheïsche dermatitis toevoegt die in atopische dermatitis niet bestaat, is het ontstekingspad dat door pimecrolimus wordt aangetast gedeeld. Meerdere onafhankelijke systematische reviews hebben geconcludeerd dat pimecrolimus 1% crème vergelijkbare werkzaamheid biedt aan antimycotica en milde corticosteroïden in seborrheïsche dermatitis, met een gunstig tolerabiliteitsprofiel voor herhaald gebruik — wat sterke biologische en klinische plausibiliteit aan deze TxGNN-voorspelling geeft.

---

## Klinisch Onderzoeksbewijs

| Onderzoeksnummer | Fase | Status | Inschrijving | Belangrijkste bevindingen |
|---|---|---|---|---|
| [NCT00403559](https://clinicaltrials.gov/study/NCT00403559) | Fase 2 | Voltooid | 113 | 4-weken gerandomiseerd, dubbelblind, actief-comparatorgericht verkennend onderzoek waarin Elidel (pimecrolimus 1% crème) werd vergeleken met een actieve comparator voor seborrheïsche dermatitis. Dit is het enige voltooide fase 2 RCT dat pimecrolimus rechtstreeks in deze indicatie evalueert. De resultaten hebben daaropvolgende bewijssynthese geïnformeerd. |

---

## Literatuurbewijs

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|---|---|---|---|---|
| [36072203](https://pubmed.ncbi.nlm.nih.gov/36072203/) | 2022 | Systematische review | Cureus | Kritische beoordeling van RCT's die de werkzaamheid en veiligheid van pimecrolimus in *faciale* seborrheïsche dermatitis evalueren; concludeert dat pimecrolimus een levensvatbaar topisch alternatief is voor corticosteroïden en antimycotica in deze indicatie. |
| [22142161](https://pubmed.ncbi.nlm.nih.gov/22142161/) | 2012 | Systematische review van RCT's | Expert Review of Clinical Pharmacology | Pimecrolimus 1% crème toont vergelijkbare werkzaamheid met corticosteroïden en antimycotica in seborrheïsche dermatitis met goede verdraagbaarheid; gepositioneerd als een goed verdraagbaar alternatief voor langdurig beheer. |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematische review | American Journal of Clinical Dermatology | Uitgebreide review van topische behandelingen voor faciale seborrheïsche dermatitis; pimecrolimus opgenomen in de bewijsbasis naast antimycotica en corticosteroïden. |
| [34910320](https://pubmed.ncbi.nlm.nih.gov/34910320/) | 2022 | RCT | Clinical and Experimental Dermatology | Gerandomiseerd blind onderzoek waarin pimecrolimus 1% crème werd vergeleken met sertaconazool 2% crème in faciale seborrheïsche dermatitis; evalueert langdurige behandeling in een chronisch relapserend verlopende aandoening. |
| [23715821](https://pubmed.ncbi.nlm.nih.gov/23715821/) | 2013 | RCT | Irish Journal of Medical Science | Directe vergelijking van sertaconazool 2% versus pimecrolimus 1% crème in seborrheïsche dermatitis; draagt vergelijkende werkzaamheidsgegevens bij. |
| [18677657](https://pubmed.ncbi.nlm.nih.gov/18677657/) | 2009 | Gerandomiseerd open-label onderzoek | Journal of Dermatological Treatment | Open gerandomiseerde prospectieve vergelijking van pimecrolimus 1% crème versus ketoconazool 2% crème in seborrheïsche dermatitis. |
| [20000875](https://pubmed.ncbi.nlm.nih.gov/20000875/) | 2010 | Open-label onderzoek | American Journal of Clinical Dermatology | Open-label onderzoek van pimecrolimus 1% crème in corticosteroïdresistente faciale seborrheïsche dermatitis; bevestigt werkzaamheid en goede verdraagbaarheid in een moeilijk-te-behandelen subgroep. |
| [23441238](https://pubmed.ncbi.nlm.nih.gov/23441238/) | 2013 | Klinisch onderzoek | Journal of Clinical and Aesthetic Dermatology | Beoordeelt klinisch bewijs dat topische pimecrolimus ondersteunt als een veilig, steroïdenvrij alternatief voor seborrheïsche dermatitis, vooral voor langdurig faciaalgbruik. |
| [16033622](https://pubmed.ncbi.nlm.nih.gov/16033622/) | 2005 | Narratieve review | International Journal of Clinical Practice | Basiswerk mechanistische review beschrijvend pimecrolimus's selectieve inhibitie van T-cel- en mestcelcytokineuitscheiding (IL-2, IL-4, IFN-γ, TNF-α); bespreekt toepassingen buiten atopische dermatitis, inclusief seborrheïsche dermatitis. |
| [15700745](https://pubmed.ncbi.nlm.nih.gov/15700745/) | 2004 | Klinisch onderzoek | Drugs Under Experimental and Clinical Research | Vroege prospectieve beoordeling van pimecrolimus 1% crème in seborrheïsche dermatitis van het gezicht en bovenkant romp; rapporteert werkzaamheid, verdraagbaarheid en veiligheid in een klinische patïëntenpopulatie. |

---

## Informatie Nederlandse Markt

Pimecrolimus beschikt momenteel over **geen nationale handelstoestemming** via CBG-MEB. Echter, Elidel (pimecrolimus 1% crème) is een **centraal geautoriseerd EMA-product** (goedgekeurd voor mild tot matig ernstige atopische dermatitis) en is daarom rechtmatig verhandelbaar in Nederland zonder een aparte CBG-MEB nationale procedure. Verificatie tegen de EMA-productendatabase wordt aanbevolen alvorens tot enige off-label gebruiksbeoordeling over te gaan.

| RVG-nummer | Productnaam | Doseringsvorm | Goedgekeurde indicatie |
|---|---|---|---|
| — | Geen CBG-MEB nationale registratie geregistreerd | — | — |

> Clinici en apotheken dienen raadpleging van de **EMA-goedgekeurde SmPC voor Elidel** (beschikbaar via de EMA-website) als referentiedocument voor geautoriseerde indicaties, contra-indicaties en speciale waarschuwingen die van toepassing zijn in Nederland.

---

## Veiligheidsbeschouwingen

Gedetailleerde veiligheidsgegevens (waarschuwingen, contra-indicaties, geneesmiddelinteracties) zijn niet beschikbaar in dit Evidence Pack voor de Nederlandse context.

> Raadpleeg alstublieft de **SmPC (Samenvatting van de Productkenmerken)** voor Elidel, beschikbaar via de EMA en/of CBG-MEB-databases, voor volledige veiligheidsinformatie alvorens enig klinisch gebruik of off-label toepassing.

Een specifieke veiligheidsnota uit de literatuur verdient aandacht: er is een onopgelost langetermijnvraagstuk met betrekking tot **maligniteitsrisico** met topische calcineurine-remmers. Een systematische review en meta-analyse uit 2023 (PMID 36370744, *The Lancet Child & Adolescent Health*) beoordeelde kankerrisico in patiënten met atopische dermatitis behandeld met pimecrolimus en tacrolimus. Regelgevingsautoriteiten in de EU hebben een waarschuwing voor dit theoretische risico gehandhaafd, vooral bij patiënten in de pediaätrie. Dit moet expliciet worden aangepakt in enig off-label gebruiksprotocol voor seborrheïsche dermatitis.

---

## Conclusie en Vervolgstappen

**Besluit: Doorgaan met Waarborgen**

**Onderbouwing:**
De TxGNN-modelvoorspelling wordt sterk ondersteund door mechanistische plausibiliteit (calcineurine-inhibitie richt zich rechtstreeks op de T-cel-gedreven ontstekingscascade relevant voor seborrheïsche dermatitis), en door een betekenisvol lichaam van klinisch bewijs — inclusief een voltooid fase 2 RCT, twee head-to-head RCT's tegen sertaconazool, ten minste twee systematische reviews en meerdere prospectieve open-label onderzoeken — allemaal aantonend dat pimecrolimus 1% crème werkzaam en goed verdraagbaar is in seborrheïsche dermatitis. De afwezigheid van een groot fase 3 bevestigingsonderzoek verhindert escalatie naar L1, en het ontbreken van CBG-MEB registratie vereist regelgevingsverheldering alvorens het gebruik in Nederland formeel in te stellen.

**Voor verdergaan is het volgende nodig:**

1. **Regelgevingsverificatie**: Bevestig de EMA-centrale autorisatiestatus voor Elidel en de toepasbaarheid ervan in Nederland voor off-label gebruik bij seborrheïsche dermatitis; bepaal of een labeluitbreiding of formeel off-label voorschrijfprotocol (magistrale bereiding/off-label beleid) vereist is door de CBG-MEB.
2. **SmPC-review**: Verkrijg de huidige Elidel SmPC om de veiligheidsbeoordeling af te ronden — specifiek belangrijke waarschuwingen, contra-indicaties en eventuele leeftijdgerelateerde beperkingen relevant voor seborrheïsche dermatitis-patïëntenpopulaties.
3. **Maligniteitsrisicoprotocol**: Stel een monitoringskader op dat het langetermijntheoretische maligniteitsrisico aanpakt dat door EMA is geïdentificeerd, vooral voor pediaätrie of langdurige gebruiksscenario's.
4. **MOA-documentatie**: Verkrijg volledig farmacologisch profiel uit DrugBank (DB00337) om het werkingsmechanisme voor het klinische dossier formeel vast te leggen.
5. **Fase 3-hiatenanalyse**: Evalueer of het bestaande fase 2- en vergelijkend RCT-bewijs voldoende is voor de beoogde gebruikscontext, of dat een fase 3 bevestigingsonderzoek zou worden vereist door Nederlandse/EMA-normen voor eventuele formele indicatieuitbreiding.

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

