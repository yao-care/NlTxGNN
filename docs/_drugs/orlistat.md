---
layout: default
title: Orlistat
parent: Alleen modelvoorspelling (L5)
nav_order: 100
evidence_level: L5
indication_count: 1
---

# Orlistat
{: .fs-9 }

Bewijsniveau: **L5** | Voorspelde indicaties: **1** 
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

# Orlistat: van Obesitasbehandeling naar Hypervitaminose

## Eenwoordige samenvatting

Orlistat is een remmer van pancreaslipase en maag-lipase, oorspronkelijk gebruikt om de absorptie van voedingsvetten als onderdeel van obesitasbehandeling te verminderen.
Het TxGNN-model voorspelt dat het effectief kan zijn voor **Hypervitaminose** — specifiek door de intestinale absorptie van vetoplosbare vitaminen te blokkeren.
Deze richting wordt echter momenteel ondersteund door **geen klinische trials** en **geen publicaties**; de voorspelling berust volledig op modelafleiding.

---

## Snel overzicht

| Item | Inhoud |
|------|--------|
| Originele indicatie | Obesitasbehandeling (lipase-remmer die vetabsorptie ~30% vermindert) |
| Voorspelde nieuwe indicatie | Hypervitaminose |
| TxGNN voorspellingsscore | 99.42% |
| Bewijsniveau | L5 |
| Status Nederlandse markt | Niet geregistreerd |
| Aantal vergunningen | 0 |
| Aanbevolen besluit | Inhouden |

---

## Waarom is deze voorspelling redelijk?

Orlistat remt pancreaslipase en maag-lipase, wat voorkomt dat dieetaire triglyceriden worden afgebroken en daardoor de vetabsorptie met ongeveer 30% vermindert. Vetoplosbare vitaminen — A, D, E en K — hebben geen onafhankelijke transporteur-gemedieerde opname in de darm; ze zijn daarentegen afhankelijk van co-solubilisatie in lipide-galzouttmicellen om de intestinale borstelzoom over te steken. Wanneer Orlistat vethydrolyse blokkeert, verstoort het structureel dit micellair transport, wat incidenteel ook de absorptie van vetoplosbare vitaminen onderdrukt. Dit gedeelde mechanisme is de biologische brug die het TxGNN-kennisgraaf benut: het Orlistat → vetoplosbare vitaminabsorptie → vitaminetoxiciteit topologisch pad levert een hoge voorspellingsscore op (0.994).

In theorie zou orlistat voor patiënten met aanhoudende hypervitaminose door continue hoge doses vetoplosbare vitaminesuppletatie — met name Hypervitaminose A of D uit exogene voedingsbronnen — verdere intestinale opname kunnen verminderen en accumulatie kunnen vertragen. Dit is niet implausibel als een mechanistisch concept, en de herpositioneringslogica is intern coherent op het farmacologische niveau.

Er zijn echter twee fundamentele beperkingen die directe klinische translatie verhinderen. Ten eerste onderschept Orlistat alleen vitaminen die momenteel in de darmlumen aanwezig zijn; het kan vitaminen die al in hepatocyten of vetweefsel zijn opgeslagen niet mobiliseren of afbouwen, wat de primaire reservoir in klinisch significante hypervitaminose zijn. Voor gevestigde toxiciteit is het mechanisme daarom onvoldoende. Ten tweede — en dit is kritiek — vitaminetekort van vetoplosbare vitaminen (hypovitaminose A, D, E, K) is zelf een goed gedocumenteerd bijwerkingsprofiel van Orlistat. De voorgestelde herpositioneringsrichting is mechanistisch identiek aan de bijwerking van het geneesmiddel zelf, wat betekent dat het "nieuwe gebruik" in wezen de opzettelijke inductie van een farmacologische bijwerking is. Deze symmetrie vereist voorzichtige klinische interpretatie en rigoureuze monitoring als onderzoek zou doorgaan.

---

## Klinische trialgegevens

Momenteel geen gerelateerde klinische trials geregistreerd.

---

## Literatuurgegevens

Momenteel geen gerelateerde literatuur beschikbaar.

---

## Informatie Nederlandse markt

Geen CBG-MEB-marketingvergunningen voor Orlistat zijn opgenomen in de huidige dataset (0 vergunningen, status: niet geregistreerd). Geen Nederlands SmPC is beschikbaar via deze pijplijn.

> **Opmerking:** Orlistat (Xenical®, Alli®) bezit een centraal goedgekeurde EMA-marketingvergunning die geldig is in alle EU/EER-lidstaten, inclusief Nederland. Deze dataset weerspiegelt alleen nationale CBG-MEB-autorisatiegegevens; de afwezigheid van een vermelding hier weerspiegelt waarschijnlijk een hiaat in de gegevenspijplijn in plaats van een werkelijke marktafwezigheid. De EMA-goedgekeurde SmPC moet worden geraadpleegd voor de huidige goedgekeurde indicatie, dosering en veiligheidsinformatie.

---

## Veiligheidsbeschouwingen

Veiligheidsgegevens (waarschuwingen en contraïndicaties) waren niet beschikbaar in dit bewijs pakket. Raadpleeg de SmPC (Samenvatting van productkenmerken) — beschikbaar via de EMA-productpagina of het CBG-MEB-register — voor volledige veiligheidsinformatie voordat u dit geneesmiddel klinisch of voor onderzoek gebruikt.

---

## Conclusie en vervolgstappen

**Besluit: Inhouden**

**Beredenering:**
Hoewel de TxGNN-modelscore hoog is (99.42%) en de mechanistische verbinding tussen Orlistat en vetoplosbare vitaminabsorptie biologisch coherent is, spiegelt de voorgestelde herpositioneringsrichting het eigen gevestigde bijwerkingsprofiel van Orlistat, is alleen van toepassing op lopende absorptie (niet op opgeslagen vitaminelast), en wordt momenteel geheel niet ondersteund door klinische trial- of gepubliceerde gegevens.

**Om door te gaan, is het volgende nodig:**

- **Oplossen DG001** — Verkrijg de EMA/CBG-MEB SmPC om de huidige goedgekeurde indicatie, contraïndicaties en belangrijke waarschuwingen te bevestigen vóór enige veiligheidsbeoordeling
- **Oplossen DG002** — Verkrijg volledige MOA-gegevens van DrugBank (DB01083) om enzymspecificiteit en vitamine-interactiepaden te bevestigen
- **Klinische haalbaarheidsonderzoek** — Zoeken naar ziektegeschiedenissen of farmacokinetische studies waarin de impact van Orlistat op serumspiegel van vetoplosbare vitaminen bij patiënten met gedocumenteerde hypervitaminose A of D uit supplementatie wordt onderzocht
- **Definitie van klinische context** — Verduidelijk of het doelgebruiksgeval acute supplementatie-geïnduceerde toxiciteit is (waarbij absorptiebeperking relevant is) versus gevestigde opslag-gebaseerde toxiciteit (waarbij dit niet het geval zou zijn)
- **Risico-batenanalyse** — Opzettelijke inductie van vitaminemalaabsorptie als therapie vereist een expliciete risico-batenrechtvaardiging; bepaal of bestaande ondersteunende zorgopties (suppletatiestaking, vitamine-A-chelatiestrategieën) deze herpositionering onnodig maken

## Disclaimer

Deze inhoud is uitsluitend bedoeld voor onderzoeksdoeleinden en vormt geen medisch advies.
Klinische validatie is vereist vóór elke klinische toepassing.

---

