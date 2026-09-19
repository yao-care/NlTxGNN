---
layout: default
title: Ritonavir
parent: Matig bewijs (L3-L4)
nav_order: 110
evidence_level: L4
indication_count: 3
---

# Ritonavir
{: .fs-9 }

Bewijsniveau: **L4** | Voorspelde indicaties: **3** 
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

# Ritonavir: Van HIV-infectie naar Feline Acquired Immunodeficiency Syndrome

## Samenvatting in één zin

Ritonavir is een protease remmer die is ontwikkeld voor HIV-1-behandeling, en wordt ook veel gebruikt als farmacokinetische booster in combinatieantiretrovirale regimes.
Het TxGNN-model voorspelt dat het mogelijk effectief is voor **Feline Acquired Immunodeficiency Syndrome (FIV)**, met **0 direct relevante klinische onderzoeken** en **0 publicaties** die deze specifieke richting ondersteunen.
Het ene opgehaalde klinische onderzoek werd foutief geclassificeerd door de datapipeline en vormt geen ondersteuning voor bewijs.

---

## Snel overzicht

| Item | Inhoud |
|------|--------|
| Oorspronkelijke indicatie | HIV-infectie (NL-regelgeversverslag niet beschikbaar; gebaseerd op vastgestelde geneesmiddelklasse-context uit herbestemming-rationale) |
| Voorspelde nieuwe indicatie | Feline Acquired Immunodeficiency Syndrome (FIV) |
| TxGNN-voorspellingsscore | 99.92% |
| Bewijsniveau | L4 |
| NL-marktpositie | Niet geregistreerd in Nederland |
| Aantal machtigingen | 0 |
| Aanbevolen besluit | Wachten |

---

## Waarom is deze voorspelling redelijk?

Gedetailleerde gegevens over het werkingsmechanisme zijn momenteel niet beschikbaar in dit Evidence Pack. Gebaseerd op de mechanistische context gedocumenteerd in de herbestemming-rationale, is Ritonavir een HIV-1 protease remmer die virale polyproteïnebewerking blokkeert en daardoor virale replicatie stopt. Het is ook een krachtige CYP3A4-remmer, die veelvuldig samen wordt gegeven als farmacokinetische booster om de plasmaconcentratie van partner-antiretroviralen te versterken.

FIV (Feline Immunodeficiency Virus) en HIV-1 zijn beide leden van de lentivirussen-subfamilie, en hun proteasen delen gedeeltelijke structurele homologie. Deze biologische relatie vormt de mechanistische basis voor de voorspelling van het TxGNN-model: als Ritonavir de HIV-1-protease kan remmen, kan het theoretisch activiteit tegen de structureel gerelateerde FIV-protease uitoefenen. In vitro-gevoeligheidsgegevens hebben aangetoond dat HIV-proteaseremmers de FIV-protease in enige mate kunnen remmen.

De vertaling naar de kliniek is echter aanzienlijk beperkt om twee redenen. Ten eerste heeft FIV-protease andere substraatspecificiteit dan HIV-1-protease, en remmers die voor HIV-1 zijn geoptimaliseerd, zullen naar verwachting geen gelijkwaardige in vivo-effectiviteit tegen FIV bereiken. Ten tweede, en veel fundamenteler, **FIV is een veterinaire indicatie** — de regelgeversweg voor diergeneesmiddelen in Nederland valt onder NVWA/Vet-MEB, die geheel gescheiden is van de autoriteit voor geneesmiddelen voor mensen (CBG-MEB). Deze voorspelling valt daarom buiten de werkingssfeer van het Nederlandse gezondheidssysteem voor mensen en kan niet voortgang maken door het standaard evaluatietraject voor geneesmiddelherbestemming voor mensen.

---

## Bewijs uit klinische onderzoeken

| Proefnummer | Fase | Status | Inschrijving | Belangrijkste bevindingen |
|---------|------|------|------|---------|
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Fase 4 | Voltooid | 145 | ⚠️ **Foutief geclassificeerd — niet relevant voor FIV.** Dit onderzoek vergelijkt Ritonavir-geboostte Darunavir + Lamivudine versus standaard duaal/triple regimes in ARV-naïeve **menselijke** HIV-1-geïnfecteerde volwassenen. Ritonavir dient hier als farmacokinetische booster, niet als directe antivirale stof tegen felien lentivirus. De pipeline haalde dit onderzoek op door onjuist het sleutelwoord "geboostte (Ritonavir-geboostte)" op de feline AIDS-query af te stemmen. Dit onderzoek draagt nul bewijskracht bij voor de FIV-indicatie. |

---

## Bewijs uit literatuur

Op dit moment is er geen gerelateerde literatuur die direct het gebruik van Ritonavir bij Feline Acquired Immunodeficiency Syndrome ondersteunt.

---

## Informatie over de Nederlandse markt

Ritonavir is momenteel niet geregistreerd in Nederland volgens dit Evidence Pack. Er zijn geen CBG-MEB-marktingmachtigingen geregistreerd.

> **Opmerking voor beoordelaar:** Ritonavir (Norvir®) heeft een gecentraliseerde EMA-marktingmachtiging en is commercieel beschikbaar in alle EU-lidstaten. Er is een verschil tussen deze dataset en de verwachte marktrealiteit. Beoordelaars moeten de huidige machtigingsstatus rechtstreeks bevestigen via het [CBG-MEB publiek register](https://www.cbg-meb.nl) of de [EMA-productdatabase](https://www.ema.europa.eu) voordat zij tot regelgevingsconclusies overgaan.

---

## Veiligheidsconsideraties

Raadpleeg alstublieft het SmPC (Samenvatting van de producteigenschappen) voor veiligheidsinformatie.

> Ritonavir is een krachtige CYP3A4- en CYP2D6-remmer met een van de breedste geneesmiddel-geneesmiddel-interactieprofielen onder alle goedgekeurde geneesmiddelen. Formele DDI-gegevens en contraïndicaties zijn niet vastgelegd in dit Evidence Pack. Klinische beoordelaars moeten het volledige EMA SmPC en een gevalideerde geneesmiddel-interactiedatabase (bijv. Liverpool HIV Interactions, Lexicomp) raadplegen alvorens tot een voorschrijf- of protocolbesluit over te gaan, vooral bij patiënten die statines, anticoagulantia, antimycotica, immunosuppressiva of QT-verlengde geneesmiddelen gebruiken.

---

## Conclusie en volgende stappen

**Besluit: Wachten**

**Rationale:**
De top TxGNN-voorspelde indicatie voor Ritonavir is een **veterinaire aandoening** (FIV / Feline AIDS), die geheel buiten de werkingssfeer van de Nederlandse gezondheidszorg en het geneesmiddelenevaluatiekader beheerd door CBG-MEB valt. Het enige opgehaalde klinische onderzoek was een pipelinefout en verleent geen geldig bewijs; er bestaat geen ondersteunende literatuur voor deze specifieke indicatie.

**Om voort te gaan, is het volgende nodig:**

- **Pipelinecorrectie:** Implementeer een veterinaire-indicatiefilter in de TxGNN-voorspellingspipeline om ziekten die alleen bij dieren voorkomen (FIV, enz.) uit rapporten over geneesmiddelherbestemming voor CBG-MEB-beoordeling uit te sluiten.
- **Prioriteer volgende gerangschikte indicaties:** Overweeg herstart van beoordeling tegen **Rang 2 — Simian Immunodeficiency Virus infectie (L3, Research Question)**, die 12 vakkundig beoordeelde publicaties heeft die mechanistische en in vivo-aannemelijkheid in niet-menselijke primaten-modellen ondersteunen.
- **MOA-gegevensopvraging:** Verkrijg Ritonavirs volledige werkingsmechanisme van DrugBank (DB00503) ter ondersteuning van eventuele toekomstige mechanistische-koppelinganalyse.
- **SmPC-veiligheidsinformatie:** Download en parse het EMA SmPC voor Ritonavir om waarschuwingen, contraïndicaties en DDI-secties in te vullen alvorens tot een S1-veiligheidsscreening over te gaan.
- **Verificatie van marktpositie:** Verzoek om verzoening van de "niet geregistreerd" datasetpositie tegen bekende EMA gecentraliseerde machtiging om de huidige CBG-MEB-beschikbaarheid te bevestigen.

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

