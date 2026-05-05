---
layout: default
title: Felodipine
parent: 僅模型預測 (L5)
nav_order: 67
evidence_level: L5
indication_count: 7
---

# Felodipine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

Now let me generate the full evaluation report based on the Evidence Pack.

---

# Felodipine: From Hypertension to Pulmonary Hypertension (Multifactorial Mechanism)

## One-Sentence Summary

Felodipine is a dihydropyridine calcium channel blocker (DHP-CCB) used internationally for essential hypertension and stable angina, though it is **currently not registered or marketed in the Netherlands**.
The TxGNN model ranks **pulmonary hypertension with unclear multifactorial mechanism** as its top predicted new indication with a score of 99.91%,
however **no supporting clinical trials or literature** exist for this specific direction — this remains a model-only signal (L5) with documented safety concerns for broad patient populations.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in the Netherlands; internationally known for hypertension and stable angina |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| NL Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## All Predicted Indications — Summary

| Rank | Indication | TxGNN Score | Evidence Level | Decision |
|------|-----------|-------------|----------------|---------|
| 1 | Pulmonary hypertension (multifactorial mechanism) | 99.91% | L5 | Hold |
| 2 | Pulmonary hypertension (lung disease / hypoxia) | 99.91% | L5 | Hold |
| 3 | Malignant hypertensive renal disease | 99.90% | L5 | Hold |
| 4 | Malignant renovascular hypertension | 99.90% | L5 | Hold |
| 5 | Braddock syndrome | 99.88% | L5 | Hold |
| 6 | Chronic pulmonary heart disease | 99.19% | L4 | Research Question |
| **7** | **Prinzmetal angina** | **99.07%** | **L2** | **Proceed with Guardrails** |

> **Key observation**: Although Prinzmetal angina ranks 7th by TxGNN score, it carries the strongest clinical evidence (L2) and is the most immediately actionable repurposing candidate. See the dedicated section below.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank for this candidate. Based on known pharmacology, Felodipine belongs to the dihydropyridine (DHP) subclass of calcium channel blockers (CCBs). It acts primarily by blocking L-type voltage-gated calcium channels in vascular smooth muscle, producing vasodilation and reducing systemic vascular resistance. This mechanism is established for hypertension management and coronary spasm prevention.

The connection between Felodipine and pulmonary hypertension has a historical basis: CCBs have been used in a select minority (<10%) of pulmonary arterial hypertension (PAH, WHO Group 1) patients who demonstrate a positive acute vasoreactivity test. In these responders, CCBs can significantly reduce pulmonary vascular resistance and improve functional class. This explains why the TxGNN model — which operates over a broad pharmacological knowledge graph — identifies a mechanistic link.

However, the predicted indication specifically involves "multifactorial mechanism" pulmonary hypertension, where the underlying pathophysiology is heterogeneous and poorly characterised. In the large majority of PAH patients who are non-responders to vasoreactivity testing, CCBs can worsen prognosis by dropping systemic blood pressure without adequately relieving pulmonary vascular resistance, potentially increasing right heart strain and mortality. Current EMA-aligned clinical guidelines explicitly caution against CCB use in non-vasoreactive PAH. This signal should be treated as a mechanistic hypothesis only and requires substantial preclinical and clinical validation before any progression.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Netherlands Market Information

Felodipine is **not registered or marketed in the Netherlands**. No CBG-MEB marketing authorisations (RVG numbers) have been issued for any Felodipine product. Any clinical use in the Netherlands would require either:

- An off-label use framework under Dutch pharmaceutical law, or
- A new marketing authorisation application to CBG-MEB (or centralised EMA procedure)

For comparator context: related DHP-CCBs (e.g., Amlodipine, Nifedipine) are registered in the Netherlands and their SmPCs can serve as a safety benchmarking reference for regulatory discussions.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for complete safety information.

> As a class-level note: DHP calcium channel blockers carry known risks of peripheral vasodilation-related adverse effects (flushing, peripheral oedema, reflex tachycardia) and clinically significant interactions with CYP3A4 inhibitors (including grapefruit juice, azole antifungals, and certain HIV protease inhibitors). For any pulmonary hypertension application specifically, the risk of systemic hypotension and worsening of ventilation-perfusion mismatch requires careful patient selection and haemodynamic monitoring. Formal SmPC documentation must be obtained before any clinical application in the Netherlands.

---

## Notable Finding: Prinzmetal Angina (Rank 7 — Strongest Evidence)

Although TxGNN ranks this indication 7th, **Prinzmetal angina (vasospastic angina)** is the single most clinically evidenced repurposing opportunity for Felodipine in this evaluation. It carries an evidence level of **L2** and a **"Proceed with Guardrails"** recommendation.

**Why the mechanism fits**: Prinzmetal angina is caused by spontaneous spasm of coronary artery smooth muscle, producing transient ST-segment elevation. DHP-CCBs block L-type calcium channels directly in coronary smooth muscle, preventing vasospasm. Felodipine shares this mechanism with Nifedipine, which is already approved for this indication in multiple countries. Multiple controlled studies from 1989–1995 directly evaluated Felodipine in this setting.

### Literature Evidence — Prinzmetal Angina

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1746458](https://pubmed.ncbi.nlm.nih.gov/1746458/) | 1991 | RCT (active-controlled) | Am J Cardiology | Felodipine 10–20 mg once daily vs. Nifedipine 20 mg four times daily in 30 Prinzmetal patients; comparable anti-ischaemic efficacy confirmed by 24-hour Holter monitoring |
| [8013514](https://pubmed.ncbi.nlm.nih.gov/8013514/) | 1994 | Controlled Trial (ergonovine challenge) | Eur Heart J | Extended-release Felodipine 20 mg once daily significantly suppressed ergonovine-induced myocardial ischaemia in 14 patients at both 4 h and 24 h post-dose |
| [2909138](https://pubmed.ncbi.nlm.nih.gov/2909138/) | 1989 | Controlled Trial (hyperventilation challenge) | Am J Cardiology | Felodipine reduced hyperventilation-induced ischaemic ST changes in variant angina patients |
| [7744087](https://pubmed.ncbi.nlm.nih.gov/7744087/) | 1995 | RCT (double-blind, 3-way crossover) | Eur Heart J | Felodipine ER 10 mg vs. Nifedipine SR 20 mg vs. placebo in 43 stable angina patients; Felodipine improved exercise duration by 66 seconds (p < 0.05) at end of dosing interval |
| [7728649](https://pubmed.ncbi.nlm.nih.gov/7728649/) | 1995 | Review (Felodipine-focused) | Can J Cardiology | Comprehensive review of Felodipine across angina syndromes; confirms CCBs as first-line for Prinzmetal angina via anti-vasospastic mechanism |
| [14689111](https://pubmed.ncbi.nlm.nih.gov/14689111/) | 2003 | Review | Herz | Differential CCB therapy across cardiovascular indications; supports DHP-CCBs for vasospastic angina |
| [3345765](https://pubmed.ncbi.nlm.nih.gov/3345765/) | 1988 | Case Series | Eur Heart J | Exercise-induced intermittent ST elevation in Prinzmetal angina documented; illustrates clinical presentation spectrum |
| [19052677](https://pubmed.ncbi.nlm.nih.gov/19052677/) | 2008 | Case Report | Can J Cardiology | Vasospasm-induced polymorphic ventricular tachycardia; highlights severity of untreated coronary spasm |
| [15222138](https://pubmed.ncbi.nlm.nih.gov/15222138/) | 2004 | Case Report | Orvosi Hetilap | Nicergoline-induced Prinzmetal angina in a hypertensive patient; reinforces vasospasm aetiology recognition |

---

## Conclusion and Next Steps

### Top Prediction (Rank 1 — Pulmonary Hypertension, Multifactorial)

**Decision: Hold**

**Rationale:**
The top TxGNN prediction lacks any supporting clinical trials or literature, and the underlying indication encompasses a heterogeneous patient population in whom CCBs have documented potential for harm. This signal does not meet the threshold for further development at this stage.

**To re-evaluate this prediction in the future:**
- Obtain a positive acute vasoreactivity test result profile for the specific patient subgroup of interest
- Identify mechanistic research establishing CCB efficacy in the multifactorial PH subtype
- Review WHO/ESC pulmonary hypertension guidelines for updated CCB positioning

---

### Prinzmetal Angina (Rank 7 — Most Actionable Candidate)

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple controlled trials (including double-blind RCTs and provocation challenge studies) conducted between 1989 and 1995 directly confirm Felodipine's efficacy in Prinzmetal angina. The mechanism is shared with Nifedipine, which is already approved for this indication. This constitutes the strongest repurposing signal in this evaluation.

**To proceed, the following is needed:**
- Retrieve complete MOA documentation from DrugBank (currently absent) to complete mechanistic dossier
- Obtain full SmPC from a comparable registered DHP-CCB (e.g., Nifedipine) for cross-reference safety benchmarking
- Consult CBG-MEB on the appropriate regulatory pathway: off-label use guidance vs. new marketing authorisation application for Felodipine in the Netherlands
- Conduct a systematic literature update (2000–present) to capture any post-1995 Felodipine data in vasospastic angina
- Prepare a pharmacovigilance plan before any clinical introduction

---

### Summary of All Predictions

| Rank | Indication | Decision | Priority |
|------|-----------|---------|---------|
| 1 | Pulmonary hypertension (multifactorial) | Hold | Low |
| 2 | Pulmonary hypertension (lung disease/hypoxia) | Hold | Low |
| 3 | Malignant hypertensive renal disease | Hold | Low |
| 4 | Malignant renovascular hypertension | Hold | Low |
| 5 | Braddock syndrome | Hold | Very Low |
| 6 | Chronic pulmonary heart disease | Research Question | Medium (basic research) |
| **7** | **Prinzmetal angina** | **Proceed with Guardrails** | **High** |

> **Disclaimer**: This report is produced for research purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before therapeutic application. Content is intended to support regulatory and research discussions within the Netherlands healthcare system under CBG-MEB oversight.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

