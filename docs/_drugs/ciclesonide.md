---
layout: default
title: Ciclesonide
parent: Alleen modelvoorspelling (L5)
nav_order: 84
evidence_level: L5
indication_count: 6
---

# Ciclesonide
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **6** 
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

# Ciclesonide: Van astma naar atopisch eczeem

## Samenvatting in één zin

Ciclesonide is een inhalatiecorticosteroïd dat oorspronkelijk wordt gebruikt bij astma en allergische rinitis. Het TxGNN-model voorspelt dat het mogelijk werkzaam is bij **atopisch eczeem**. Hiervoor zijn **geen klinische studies** en **geen specifieke publicaties** beschikbaar, dus de voorspelling berust alleen op een computermodel.

---

## Snel overzicht

| Item | Inhoud |
|------|------|
| Oorspronkelijke indicatie | Astma, allergische astma, allergische rinitis, vasomotore rinitis (afkomstig uit de kennisgraaf; de geregistreerde indicatietekst van de Nederlandse vergunning ontbreekt) |
| Voorspelde nieuwe indicatie | Atopisch eczeem |
| TxGNN-voorspellingsscore | 99,96% |
| Bewijsniveau | L5 |
| Marktstatus in Nederland | Alleen doorgehaald (vergunning ingetrokken) |
| Aantal vergunningen | 1 |
| Aanbevolen beslissing | Hold |

---

## Waarom is deze voorspelling aannemelijk?

Ciclesonide is een prodrug van een inhalatiecorticosteroïd. Esterasen in het lichaam zetten het om in des-ciclesonide, een agonist van de glucocorticoïdreceptor. Gedetailleerde gegevens over het werkingsmechanisme zijn in de voor dit rapport verzamelde data niet beschikbaar; bovenstaande beschrijving is gebaseerd op de klasse van het middel.

Corticosteroïden zijn een gevestigde ontstekingsremmende behandeling bij atopisch eczeem. Er is dus een rationale op klasseniveau. Er zijn echter geen studies of publicaties specifiek voor ciclesonide bij deze aandoening. De hoge score is uitsluitend een computationele voorspelling.

Daarnaast beperken de inhalatievorm en de lage systemische blootstelling van ciclesonide de directe vertaling naar huidziekte. Een geschikte toedieningsroute en formulering zijn nog niet beoordeeld.

De lijst met voorspellingen bevat ook "dermatitis, atopic". Dit is in wezen dezelfde aandoening (dubbele ontologietermen) en moet als één indicatie worden behandeld.

### Overige voorspelde indicaties (ter context)

| Rang | Aandoening | Score | Bewijsniveau | Opmerking |
|------|------|------|------|------|
| 2 | Sensibilisatie voor 2-hydroxyethylmethacrylaat (HEMA) | 99,76% | L5 | Geen bewijs; behandeling bestaat vooral uit vermijden van het allergeen |
| 3 | Dermatitis, atopisch | 99,73% | L5 | Duplicaat van atopisch eczeem |
| 4 | Bronchitis | 99,70% | L4 | Alleen indirecte context via een COPD-richtlijn |
| 5 | Contactdermatitis | 99,25% | L4 | Het enige artikel is een veiligheidssignaal, geen werkzaamheidsbewijs |
| 6 | Astma-gerelateerde eigenschappen (gevoeligheid) | 99,13% | L5 | Genetische term, geen op zichzelf staande behandelbare indicatie |

---

## Bewijs uit klinische studies

Momenteel geen gerelateerde klinische studies geregistreerd.

---

## Bewijs uit de literatuur

Voor atopisch eczeem is momenteel geen gerelateerde literatuur beschikbaar. Voor andere voorspelde indicaties is de volgende literatuur gevonden (indirect, geen directe ondersteuning van werkzaamheid):

| PMID | Jaar | Type | Tijdschrift | Belangrijkste bevindingen |
|------|-----|------|------|---------|
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Richtlijn/review | Basic & Clinical Pharmacology & Toxicology | Finse richtlijn voor diagnose en farmacotherapie van stabiele COPD; biedt alleen indirecte context over inhalatiecorticosteroïden bij chronische obstructieve luchtwegziekte (relevant voor bronchitis) |
| [22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/) | 2012 | Casusbeschrijving | Contact Dermatitis | Systemische allergische dermatitis door ingeademd budesonide, met kruisreactiviteit in plakproeven met ciclesonide; een veiligheidssignaal (relevant voor contactdermatitis) |

---

## Informatie over de Nederlandse markt

| RVG-nummer | Productnaam | Toedieningsvorm | Goedgekeurde indicatie |
|---------|------|------|-----------|
| RVG 119131//31633 | Alvesco 160 inhalator, aërosol, oplossing 160 microgram/dosis | Niet vermeld | Niet vermeld (status: doorgehaald) |

Het enige Nederlandse product is doorgehaald; er is momenteel geen geldige vergunning voor ciclesonide in de verzamelde gegevens.

---

## Veiligheidsoverwegingen

**Contra-indicaties uit de kennisgraaf** (afgeleid uit relaties in de TxGNN-kennisgraaf, niet uit de productinformatie):
- Herpes-simplex-keratitis
- Bijnierinsufficiëntie en ziekte van Addison
- Osteoporose en postmenopauzale osteoporose
- Schimmelinfecties en dermatofytose
- Oculaire hypertensie en glaucoom
- Parasitaire infecties

**Geneesmiddelinteracties:** in totaal 63 interacties gevonden. Voorbeelden uit de verzamelde gegevens:
- **Ernstig (Major):** cladribine
- **Matig (Moderate):** claritromycine, miconazol, cobicistat, atazanavir, fosamprenavir, amprenavir, boceprevir, ceritinib, fostamatinib, conivaptan, abametapir (cutaan), inhalatie-insuline
- **Licht (Minor):** formoterol, salbutamol, arformoterol
- Daarnaast interacties met onbekend niveau, onder meer met omeprazol, lansoprazol, famotidine en prednisolon

Veel van de matige interacties betreffen CYP3A4-remmers; dit is een algemene aanname en niet uit de data bevestigd.

**Aanvullend signaal:** een casusbeschrijving laat kruisreactiviteit voor contactallergie zien tussen budesonide en ciclesonide. Dit weegt tegen gebruik bij huidaandoeningen zonder verdere beoordeling.

Raadpleeg voor waarschuwingen en contra-indicaties de SmPC (Samenvatting van de Productkenmerken) en de bijsluiter (PIL), aangezien de productinformatie van het CBG-MEB niet in de verzamelde data is opgenomen.

---

## Conclusie en vervolgstappen

**Beslissing: Hold**

**Onderbouwing:**
- De voorspelling voor atopisch eczeem berust uitsluitend op een model (bewijsniveau L5) zonder klinische studies of specifieke literatuur. De inhalatievorm sluit slecht aan bij huidziekte, en de enige Nederlandse vergunning is doorgehaald.

**Om verder te gaan is nodig:**
- Productinformatie van het CBG-MEB (SmPC) voor waarschuwingen en contra-indicaties; dit ontbrak in de verzamelde data en blokkeert de veiligheidsscreening
- Gegevens over het werkingsmechanisme uit DrugBank
- Beoordeling van de routecompatibiliteit (een topicale of systemische formulering is nodig voor huidindicaties)
- Preklinisch of klinisch bewijs voor ciclesonide bij atopisch eczeem
- Beoordeling van het risico op contactallergie en kruisreactiviteit tussen corticosteroïden
- Opheldering van de marktstatus in Nederland, aangezien er geen geldige vergunning is
## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

