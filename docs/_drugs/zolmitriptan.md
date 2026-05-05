---
layout: default
title: Zolmitriptan
parent: 僅模型預測 (L5)
nav_order: 125
evidence_level: L5
indication_count: 3
---

# Zolmitriptan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Using the `txgnn-pipeline` skill for context, and now generating the report from the Evidence Pack.

---

# Zolmitriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Zolmitriptan (brand name: Zomig) is a selective serotonin 5-HT1B/1D receptor agonist (triptan) established in multiple jurisdictions for the acute treatment of migraine attacks with or without aura.
The TxGNN model predicts it may also be effective for **Migraine with Brainstem Aura** (formerly basilar-type migraine), with **no registered clinical trials** but **19 publications** currently supporting this direction.
A pivotal AHS 2015 guideline revision has substantially weakened the historical theoretical contraindication for triptan use in this subtype, reinforcing the plausibility of this prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute migraine (no NL authorization on record; established in other jurisdictions) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| NL Market Status | Not registered in the Netherlands |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Zolmitriptan is a lipophilic, selective 5-HT1B/1D receptor agonist with a **dual mode of action** that sets it apart from earlier triptans. Peripherally, it inhibits CGRP and substance P release at trigeminal vascular terminals, blocking pain signal transmission from intracranial blood vessels. Centrally — and critically for this prediction — its lipophilicity allows it to cross the blood–brain barrier (BBB) and directly modulate neurons in the brainstem trigeminal nuclei. This central action is a feature not shared by all triptans and is directly relevant to the pathophysiology of migraine with brainstem aura.

Migraine with brainstem aura (MBA) is characterised by cortical spreading depression (CSD) extending posteriorly into brainstem regions, producing symptoms such as diplopia, vertigo, dysarthria, tinnitus, and impaired consciousness. Because zolmitriptan's central mechanism targets brainstem trigeminal hyperexcitability — the pathophysiological core of MBA — the mechanistic link underpinning the TxGNN prediction is particularly coherent. The drug is not simply being proposed for an unrelated condition; it is already active in the same neural circuits implicated in this specific migraine subtype.

Historically, triptans were listed as contraindicated in basilar-type migraine (pre-2004 guidelines), based on a theoretical concern that basilar artery vasoconstriction could worsen brainstem ischaemia. However, the American Headache Society's 2015 evidence assessment (PMID 25600718) formally revised this position, concluding that accumulated real-world data have not identified a meaningful ischaemic risk signal, and that the prior contraindication lacked robust clinical evidence. This guideline evolution — combined with zolmitriptan's unique centrally active pharmacology — provides a strong mechanistic and regulatory basis for this repurposing prediction.

---

## Clinical Trial Evidence

Currently no clinical trials related to zolmitriptan in migraine with brainstem aura are registered on ClinicalTrials.gov or the WHO ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Clinical Practice Guideline | *Headache* | AHS systematic evidence assessment of acute migraine pharmacotherapies; formally revised the prior theoretical contraindication of triptans in brainstem aura migraine, noting the absence of real-world ischaemic signal |
| [11903526](https://pubmed.ncbi.nlm.nih.gov/11903526/) | 2001 | Clinical Study | *Headache* | Reports real-world triptan use — including zolmitriptan — in basilar migraine and migraine with prolonged aura; the most directly indication-specific publication in this pack |
| [25916333](https://pubmed.ncbi.nlm.nih.gov/25916333/) | 2015 | Meta-analysis | *The Journal of Headache and Pain* | Comparative meta-analysis of frovatriptan vs rizatriptan, zolmitriptan, and almotriptan in migraine with aura; supports triptan class efficacy across aura subtypes |
| [22644173](https://pubmed.ncbi.nlm.nih.gov/22644173/) | 2012 | RCT Subgroup Analysis | *Neurological Sciences* | Double-blind, randomized, multicenter crossover study; zolmitriptan 2.5 mg vs frovatriptan 2.5 mg in migraine with aura (IHS criteria); direct head-to-head RCT subgroup data for zolmitriptan in aura |
| [27329280](https://pubmed.ncbi.nlm.nih.gov/27329280/) | 2016 | RCT | *Headache* | TEENZ Study (NCT01211145): randomized, double-blind, multicenter trial of zolmitriptan nasal spray in adolescent migraine (ages 12–17); demonstrates efficacy and tolerability across patient populations |
| [12864759](https://pubmed.ncbi.nlm.nih.gov/12864759/) | 2003 | Interventional Clinical Study | *Headache* | Transcranial Doppler study assessing intracranial blood flow velocity during migraine attacks before and after oral zolmitriptan or sumatriptan; provides haemodynamic context relevant to brainstem vascular concerns |
| [18624801](https://pubmed.ncbi.nlm.nih.gov/18624801/) | 2008 | Clinical Study | *Cephalalgia* | Randomized study in migraine patients with and without aura examining early allodynia; zolmitriptan showed significant pain reduction, with implications for central sensitisation in aura-related attacks |
| [12083998](https://pubmed.ncbi.nlm.nih.gov/12083998/) | 2002 | Narrative Review | *Expert Opinion on Pharmacotherapy* | Comprehensive review of zolmitriptan pharmacology and clinical applications; covers efficacy in migraine with and without aura, onset of action within 45 minutes, and sustained 2-hour response |
| [25538676](https://pubmed.ncbi.nlm.nih.gov/25538676/) | 2014 | Review | *Frontiers in Neurology* | Summarises treatment options for vestibular migraine — a brainstem-overlap syndrome — noting emerging evidence and guideline gaps for triptan use across the brainstem aura spectrum |
| [9399012](https://pubmed.ncbi.nlm.nih.gov/9399012/) | 1997 | Preclinical Pharmacology | *Cephalalgia* | Foundational preclinical study demonstrating zolmitriptan's lipophilicity, BBB penetration, and ability to inhibit trigeminovascular activation both centrally (brainstem) and peripherally — the mechanistic backbone of this prediction |

---

## Netherlands Market Information

Zolmitriptan currently holds **no marketing authorizations** issued by the CBG-MEB (College ter Beoordeling van Geneesmiddelen) in the Netherlands. No RVG (Registratienummer) entries are on record.

> For prescribing information, refer to the SmPC (Samenvatting van de Productkenmerken) from jurisdictions where zolmitriptan is authorized — for example, the UK MHRA (Zomig) or EMA-affiliated product information — as the regulatory basis for safety evaluation pending any NL authorization.

---

## Safety Considerations

Complete safety data (key warnings, contraindications, drug–drug interactions) are not available in this Evidence Pack.

> Please refer to the SmPC (Samenvatting van de Productkenmerken) for full safety information.

**Indication-specific caution:** Although the AHS 2015 guideline (PMID 25600718) has revised the historical blanket contraindication for triptans in brainstem aura downward, clinical prudence remains warranted. Patients with elevated thromboembolism risk — including those with CADASIL, familial hemiplegic migraine (FHM), or patent foramen ovale (PFO) — should be excluded from triptan use in this context pending further dedicated study.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Zolmitriptan's established 5-HT1B/1D dual central-peripheral mechanism is directly and specifically relevant to the pathophysiology of migraine with brainstem aura, and a high-quality AHS clinical practice guideline (2015) has formally walked back the prior theoretical contraindication. Multiple supporting publications — including a meta-analysis, RCT subgroup data, and a dedicated clinical study on triptans in basilar migraine — provide L2-level evidence. However, no dedicated prospective trial exists for this precise indication, and the drug is not registered in the Netherlands, requiring regulatory action before clinical use.

**To proceed, the following is needed:**
- Obtain the full SmPC from an authorizing jurisdiction (UK MHRA or equivalent) to complete the NL safety dossier and DDI assessment — particularly regarding MAO-B inhibitors and other serotonergic agents
- Implement a structured patient-selection protocol explicitly excluding CADASIL, FHM, and high thromboembolism risk profiles
- Initiate a prospective observational registry for MBA patients treated with zolmitriptan to generate NL-specific real-world safety and efficacy data
- Consult CBG-MEB regarding the regulatory pathway for a non-registered medicinal product (e.g., named-patient use or hospital exemption under Article 3(1) of Directive 2001/83/EC)
- Commission a dedicated Phase 2 proof-of-concept RCT in migraine with brainstem aura to elevate evidence to L1 and support a formal label extension submission
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

