---
layout: default
title: Telmisartan
parent: Alleen modelvoorspelling (L5)
nav_order: 116
evidence_level: L5
indication_count: 10
---

# Telmisartan
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

# Telmisartan: Van hypertensie naar Prinzmetal-angina

## Samenvatting in één zin

Telmisartan is een angiotensine II type 1 receptorblokker (ARB) die veel gebruikt wordt in de behandeling van hypertensie en cardiovasculaire risicoreductie.
Het TxGNN-model voorspelt dat het effectief kan zijn voor **Prinzmetal-angina** (variant-angina pectoris door coronaire vasospasme),
zonder dat er momenteel **geen klinische proeven** en **geen publicaties** deze specifieke richting ondersteunen.
De modelvoorspellingsscore is uitzonderlijk hoog (99.98%), maar alle ondersteunend bewijs blijft op het niveau van alleen modelvoorspelling (L5).

---

## Snel overzicht

| Item | Inhoud |
|------|--------|
| Originele indicatie | Hypertensie (standaard ARB-klasindicatie; geen autorisatie op het Nederlandse marktregister) |
| Voorspelde nieuwe indicatie | Prinzmetal-angina |
| TxGNN-voorspellingsscore | 99.98% |
| Bewijsniveau | L5 |
| Status Nederlandse markt | Niet op de markt (CBG-MEB: 0 autorisaties) |
| Aantal autorisaties | 0 |
| Aanbevolen besluit | In afwachting |

---

## Waarom is deze voorspelling redelijk?

Op dit moment zijn gedetailleerde gegevens over het werkingsmechanisme niet beschikbaar in dit Evidence Pack. Gebaseerd op vastgestelde farmacologie is Telmisartan een AT1-receptorblokker (ARB) die ook fungeert als een gedeeltelijke agonist van peroxisoomproliferator-geactiveerde receptor gamma (PPAR-γ) — een duaal mechanisme dat het onderscheidt van andere ARB's en heeft geleid tot de informele aanduiding "metabosartan". Door AT1R te blokkeren, vermindert Telmisartan de door angiotensine II veroorzaakte vaatvernauwing; de PPAR-γ agonisme kan bovendien coronaire endotheelfunctie verbeteren en vasculaire oxidatieve stress verminderen.

Prinzmetal-angina (variant-angina pectoris) ontstaat door voorbijgaande reversibele coronaire arteriële vasospasme in plaats van vaste atherosclerotische obstructie. In deze context zou AT1R-blokkade theoretisch de afgifte van endotheline-1 en reactieve zuurstofsoorten (ROS) kunnen verminderen die coronaire gladde spier gevoelig maken voor vasospasme, terwijl PPAR-γ activering de expressie van endotheliale salpeterzuuroxide synthase (eNOS) kan verhogen en de coronaire vasomotorische tonus kan verbeteren. Deze mechanistische stappen zijn biologisch coherent, maar blijven zeer indirect: gevestigde eerstelijns middelen voor Prinzmetal-angina (calciumkanaalblokkers, langwerkende nitraten) werken direct op vasculaire gladde spier, terwijl het werkingspad van Telmisartan verschillende stappen hogerop werkt.

Op dit moment testen geen in vitro-, in vivo- of klinische studies specifiek Telmisartan bij coronaire vasospasme. De hoge TxGNN-score weerspiegelt waarschijnlijk gedeelde cardiovasculaire grafische knooppunten (bijvoorbeeld vasculaire spanning, AT1R-signalering) in de kennisgraaf in plaats van een samengesteld mechanistisch pad. Deze indicatie moet daarom het beste worden behandeld als een door model gegenereerde hypothese in afwachting van experimentele validatie.

---

## Bewijs uit klinische proeven

Momenteel zijn geen gerelateerde klinische proeven voor Telmisartan in Prinzmetal-angina geregistreerd.

---

## Bewijs uit literatuur

Momenteel is geen gerelateerde literatuur beschikbaar voor Telmisartan in Prinzmetal-angina.

---

## Informatie over de Nederlandse markt

Telmisartan heeft momenteel **geen marketingautorisaties** die bij de CBG-MEB zijn geregistreerd in deze dataset. Er zijn geen RVG-nummers, productnamen of goedgekeurde indicaties in het dossier.

> **Opmerking voor beoefenaren:** Telmisartan is internationaal bekend onder merknamen zoals *Micardis* (Boehringer Ingelheim) en is wijd geautoriseerd in andere rechtsgebieden (EMA, FDA). De afwezigheid van vermeldingen in deze dataset kan wijzen op een gegevenspijplijn-hiaat in plaats van echte regelgevinsgafwezigheid. Raadpleeg alstublieft het openbare register van CBG-MEB en de EMA-productdatabase rechtstreeks om de huidige autorisatiestatus in Nederland te bevestigen alvorens regelgevingsconclusies te trekken.

---

## Veiligheidsobservaties

Raadpleeg de SmPC (Samenvatting van Productkenmerken) voor uitgebreide veiligheidsinformatie.

> Als algemene referentie in afwachting van SmPC-ophaling (Data Gap DG001) zijn de volgende ARB-klasseneffect waarschuwingen veel gedocumenteerd:
> - **Nierrisico:** Risico op acuut nierschade bij patiënten met bilaterale nierarteriële stenose of alleenstaande werkende nier — AT1R-blokkade verwijdert de afferente arteriaire spanning die de GFR in deze situaties onderhoudt.
> - **Hyperkaliëmie:** Met name in combinatie met ACE-inhibitoren, kaliumsparende diuretica, of bij patiënten met nierfunctiestoornissen.
> - **Eerste-dosisshypotensie:** Met name bij patiënten met volumedepletie of natriumdepletie.
> - **Contraïndicatie in zwangerschap:** ARB's zijn contraïndiceerd in het tweede en derde trimester (fetotoxiciteit).
>
> Dit zijn algemene klassenobservaties en moeten tegen de huidige Telmisartan-SmPC worden geverifieerd alvorens enig klinisch of onderzoeksgebruik.

---

## Conclusie en vervolgstappen

**Besluit: In afwachting**

**Rationale:**
Het TxGNN-model wijst een uitzonderlijk hoge voorspellingsscore toe (99.98%), wat sterke kennisgraaf-connectiviteit tussen Telmisartan en Prinzmetal-angina aangeeft. Echter, er is momenteel nul empirisch bewijs — geen klinische proeven, geen diermodellen, en geen waarnemingsgegevens — die specifiek Telmisartan bij coronaire vasospasme testen. Het mechanistische pad is theoretisch plausibel maar indirect, en effectieve eerstelijns middelen voor Prinzmetal-angina zijn al goedgekeurd en beschikbaar. Voortgaan zonder enige experimentele basis zou onacceptabele onzekerheid met zich meebrengen.

**Om verder te gaan is het volgende nodig:**

- **Preklinische validatie:** In vitro tests voor coronaire gladde spierrelaxatie en/of diermodellen voor coronaire vasospasme om direct mechanistisch bewijs voor AT1R-blokkade in deze specifieke ziektecontext vast te stellen.
- **Ophaling van werkingsmechanisme:** Gegevensgat DG002 oplossen (DrugBank API opvragen voor volledige MOA) om een meer rigoureuze mechanistische analyse mogelijk te maken.
- **Beoordeling van veiligheidsprofiel:** Gegevensgat DG001 oplossen (SmPC/PIL ophalen en analyseren van het EMA/CBG-MEB register) om de S1 veiligheidsscreeningpoort af te ronden alvorens ontwerp van haalbaarheidsonderzoek.
- **Enquête naar bewijs op klasseniveau:** Een systematisch onderzoek naar ARB's of renine-angiotensinesysteemdeelnemers (RAS) bij coronaire vasospasme uitvoeren om te bepalen of enig signaalniveau op klasseniveau bestaat dat translationele plausibiliteit zou kunnen ondersteunen.
- **Beoordeling van klinische differentiatie:** Beoordeel of Telmisartan een zinvol klinisch voordeel ten opzichte van bestaande therapieën (calciumkanaalblokkers, nitraten) zou kunnen bieden alvorens middelen aan een prospectief onderzoek toe te wijzen.

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

