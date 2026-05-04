---
layout: default
title: Amlodipine
parent: 僅模型預測 (L5)
nav_order: 26
evidence_level: L5
indication_count: 10
---

# Amlodipine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Amlodipine: From Hypertension to Intracerebral Hemorrhage (Secondary Prevention)

## One-Sentence Summary

Amlodipine is a long-acting dihydropyridine calcium channel blocker (CCB), widely used for the treatment of hypertension and angina pectoris. The TxGNN model predicts it may be effective for **intracerebral hemorrhage (ICH) secondary prevention**, with **6 clinical trials** (including a completed Phase 3 RCT with 1,671 patients) and **8 publications** currently supporting this direction. Among 10 predicted new indications, ICH prevention has the strongest evidence base and the most direct mechanistic rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, angina pectoris |
| Predicted New Indication | Intracerebral Hemorrhage (secondary prevention) |
| TxGNN Prediction Score | 99.79% (rank 563) |
| Evidence Level | L2 — 1 completed Phase 3 RCT (TRIDENT, n=1,671) |
| NL Market Status | Not registered in current dataset (note: amlodipine is widely available in the EU under EMA/CBG-MEB authorizations) |
| Number of Authorizations | 0 in current dataset |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Amlodipine is a third-generation dihydropyridine calcium channel blocker that selectively inhibits L-type calcium channels in vascular smooth muscle. By reducing calcium influx, it causes arterial vasodilation and lowers systemic vascular resistance, resulting in sustained blood pressure reduction. Its long plasma half-life (~30–50 hours) provides stable 24-hour blood pressure control with once-daily dosing — a property particularly valuable in stroke prevention, where blood pressure variability is an independent risk factor for cerebrovascular events.

Intracerebral hemorrhage (ICH) is the most lethal form of stroke, and hypertension is its strongest modifiable risk factor. Blood pressure control is the cornerstone of ICH secondary prevention. The mechanistic link between amlodipine and ICH prevention is direct and well-established: (1) sustained blood pressure lowering reduces the mechanical stress on small cerebral arteries that causes rupture; (2) calcium channel blockers may provide additional cerebrovascular protection beyond blood pressure reduction by improving cerebral blood flow autoregulation; and (3) amlodipine's antioxidative properties may attenuate vascular remodeling in hypertensive cerebral vasculopathy.

The TRIDENT trial (NCT02699645) — a completed, international, double-blinded, Phase 3 RCT with 1,671 patients — directly tested a fixed low-dose combination ("Triple Pill") strategy containing amlodipine for preventing recurrent stroke in patients with a history of ICH. This represents high-quality clinical evidence that strongly supports the TxGNN prediction. Additionally, a new trial (NCT07458880, TRICH) is currently recruiting to further evaluate triple antihypertensive therapy including amlodipine after ICH. It is important to note that this indication refers to *secondary prevention* of ICH, not acute management — in the acute setting, intravenous antihypertensive agents are preferred.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | Completed | 1,671 | **Core evidence.** TRIDENT main trial: fixed low-dose triple pill (including amlodipine) vs. placebo on top of standard care for prevention of recurrent stroke in ICH patients. International, double-blinded RCT. |
| [NCT07458880](https://clinicaltrials.gov/study/NCT07458880) | N/A | Recruiting | 140 | TRICH trial: triple antihypertensive medication after ICH for blood pressure control, using a TRICH scoring system. Directly studies amlodipine's role post-ICH. |
| [NCT03264352](https://clinicaltrials.gov/study/NCT03264352) | Phase 4 | Recruiting | 11,414 | IPAD trial: antihypertensive intervention for high-normal BP in type 2 diabetes patients. ICH is a secondary endpoint. Large-scale trial. |
| [NCT00134160](https://clinicaltrials.gov/study/NCT00134160) | Phase 4 | Completed | 1,000 | CASE-J related trial: high-dose ARB monotherapy vs. ARB + CCB combination in elderly high-risk hypertensive patients. ICH is part of the cardiovascular composite endpoint. |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT Cognitive Sub-Study: triple pill strategy for slowing memory decline in ICH patients. Terminated early with minimal enrollment. |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | N/A | Terminated | 4 | TRIDENT MRI Sub-Study: imaging substudy of the TRIDENT trial. Terminated early, limited data available. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | Trial Protocol | Int J Stroke | TRIDENT trial rationale and design: single-pill combination BP-lowering strategy (including amlodipine) for ICH secondary prevention. Establishes the scientific basis for the trial. |
| [23053838](https://pubmed.ncbi.nlm.nih.gov/23053838/) | 2013 | Clinical Study | Neurol Sci | Evaluates antihypertensive strategies in acute ICH (n=138). Examines role of beta-blockers vs. other agents in reducing mortality and SIRS in hypertensive ICH. |
| [14717341](https://pubmed.ncbi.nlm.nih.gov/14717341/) | 2003 | Trial Protocol | Hypertens Res | CASE-J trial protocol: compares ARB vs. CCB (amlodipine) in high-risk hypertensive patients for cardiovascular event reduction including cerebrovascular events. |
| [17077518](https://pubmed.ncbi.nlm.nih.gov/17077518/) | 2006 | Preclinical | Biol Pharm Bull | Dihydropyridine CCB improves cerebral blood flow autoregulation in spontaneously hypertensive rats, supporting the cerebrovascular protective mechanism of CCBs. |
| [3154329](https://pubmed.ncbi.nlm.nih.gov/3154329/) | 1988 | Review | Cardiovasc Drugs Ther | Comprehensive review of calcium channel antagonists in hypertension: mechanisms of action include vascular smooth muscle relaxation and improved cerebral perfusion. |
| [19299323](https://pubmed.ncbi.nlm.nih.gov/19299323/) | 2009 | Case Report | Ann Pharmacother | Reports amlodipine-associated angioedema in a patient with hemorrhagic stroke — relevant safety signal to monitor. |
| [26698202](https://pubmed.ncbi.nlm.nih.gov/26698202/) | 2015 | Case Report | BMJ Case Rep | PRES following rapid withdrawal of antihypertensives (including amlodipine) in a patient with history of ICH — highlights importance of continued BP control. |
| [37489780](https://pubmed.ncbi.nlm.nih.gov/37489780/) | 2024 | Case Report | Curr Drug Saf | Reports tizanidine-induced hypotension in stroke patients on concurrent antihypertensives — relevant drug interaction consideration for ICH patients with spasticity. |

## Netherlands Market Information

Amlodipine is not currently listed in this dataset's regulatory records. However, amlodipine is one of the most widely prescribed antihypertensive drugs globally and is available in the Netherlands under multiple CBG-MEB and EMA-authorized marketing authorizations (including generic formulations). Healthcare professionals should consult the CBG-MEB Geneesmiddeleninformatiebank for current Dutch product registrations and SmPC documents.

## Additional Predicted Indications Overview

The TxGNN model identified 10 potential new indications for amlodipine. The table below summarizes all predictions ranked by evidence strength:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Trials | Publications | Recommendation |
|------|---------------------|------------|---------------|--------|-------------|---------------|
| 10 | **Intracerebral hemorrhage** | 99.79% | **L2** | 6 | 8 | **Proceed with Guardrails** |
| 6 | Cerebral artery occlusion | 99.89% | L3 | 5 | 5 | Proceed with Guardrails |
| 4 | Malignant hypertensive renal disease | 99.90% | L4 | 0 | 0 | Proceed with Guardrails |
| 2 | Pulmonary hypertension (lung disease/hypoxia) | 99.91% | L4 | 0 | 20 | Research Question |
| 5 | Malignant renovascular hypertension | 99.90% | L4 | 0 | 2 | Research Question |
| 8 | MRI defined brain infarct | 99.86% | L4 | 1 | 0 | Research Question |
| 1 | Brain stem infarction | 99.94% | L5 | 0 | 0 | Hold |
| 3 | Pulmonary hypertension (unclear multifactorial) | 99.91% | L5 | 0 | 0 | Hold |
| 7 | Braddock syndrome | 99.88% | L5 | 0 | 0 | Hold |
| 9 | ABri amyloidosis | 99.84% | L5 | 0 | 0 | Hold |

**Key patterns:** The strongest predictions cluster around cerebrovascular and hypertension-related conditions, which aligns with amlodipine's known pharmacology. Predictions for rare genetic conditions (Braddock syndrome, ABri amyloidosis) lack biological plausibility and likely reflect graph-topological artifacts rather than true therapeutic potential.

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics, Dutch: Samenvatting van de Productkenmerken) for comprehensive safety information on amlodipine.

**Important clinical considerations for the ICH prevention indication:**
- In *acute* ICH, oral amlodipine is not first-line — rapid-acting intravenous agents (e.g., nicardipine, labetalol) are preferred for acute blood pressure management
- Amlodipine's long half-life provides stable chronic BP control, which is advantageous for *secondary prevention* but limits dose titration flexibility in acute settings
- Angioedema has been reported rarely with amlodipine use (see PMID 19299323)
- Drug interactions with other antihypertensives and anti-spasticity agents (e.g., tizanidine) should be monitored in post-stroke patients

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Amlodipine's role in ICH secondary prevention is supported by strong mechanistic reasoning and high-quality clinical evidence. The completed TRIDENT trial (Phase 3, n=1,671) directly evaluated a fixed-dose combination including amlodipine for preventing recurrent cerebrovascular events in ICH patients, representing L2 evidence. Additional trials (TRICH, IPAD) are actively recruiting, indicating ongoing clinical interest. The drug's well-established safety profile in chronic hypertension management further supports feasibility.

**To proceed, the following is needed:**
- Full results publication of the TRIDENT trial (NCT02699645) to confirm efficacy outcomes
- Detailed mechanism of action data specific to cerebrovascular protection (currently listed as data gap)
- CBG-MEB/EMA SmPC review to confirm that ICH secondary prevention falls within or near currently approved indications in the Netherlands
- Safety monitoring plan addressing the distinction between acute ICH management (where amlodipine is not first-line) and chronic secondary prevention
- Assessment of existing Dutch clinical guidelines (NHG-Standaard) for post-ICH blood pressure management and positioning of amlodipine within the treatment algorithm
- Drug-drug interaction evaluation for common co-medications in post-ICH patients (antiplatelets, anticoagulants, anti-spasticity agents)

---

*Disclaimer: This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before clinical application. All predictions are generated by the TxGNN model and should be interpreted by qualified healthcare professionals.*

*Data cutoff: 2026-04-03 | Evidence Pack version: v4*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

