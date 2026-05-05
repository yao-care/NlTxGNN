---
layout: default
title: Haloperidol
parent: 僅模型預測 (L5)
nav_order: 75
evidence_level: L5
indication_count: 10
---

# Haloperidol
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

Using the `txgnn-pipeline` skill to guide this NL drug repurposing report. The most clinically actionable predicted indication is **rank 10 (manic bipolar affective disorder)** — with L1 evidence and a "Proceed with Guardrails" recommendation — rather than ranks 1–9 which are all L5/Hold with no supporting evidence. The report focuses accordingly.

---

# Haloperidol: From Acute Psychosis to Manic Bipolar Affective Disorder

## One-Sentence Summary

Haloperidol is a first-generation (typical) antipsychotic, long used for the management of acute psychosis and schizophrenia, acting as a potent dopamine D2 receptor antagonist. The TxGNN model predicts it may be effective for **manic bipolar affective disorder**, with **9 clinical trials** and **20 publications** currently supporting this direction. Notably, two completed Phase 3 RCTs used Haloperidol as a primary active comparator in bipolar mania, providing substantial direct efficacy data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from NL CBG-MEB registry (known clinical use: schizophrenia and acute psychosis) |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L1 |
| NL Market Status | Not registered (likely data gap — Haloperidol generics are in wide international use) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on NL market data:** The CBG-MEB query returned 0 registered products. Haloperidol (e.g., Haldol) is a well-established generic that holds marketing authorizations in numerous EU member states. This zero result likely reflects a data retrieval gap rather than genuine non-availability. A direct CBG-MEB registry check is recommended before drawing regulatory conclusions.

---

## Why Is This Prediction Reasonable?

Haloperidol is a high-affinity dopamine D2 receptor antagonist (Ki ≈ 1 nM), the pharmacological hallmark of first-generation antipsychotics. Although detailed SmPC/MOA data was not returned in the current evidence package, its core mechanism is among the most extensively documented in clinical pharmacology: by blocking D2 receptors in the mesolimbic pathway, it suppresses dopaminergic hyperactivity — the same pathway that drives psychotic symptoms in schizophrenia.

The mechanistic bridge to bipolar mania is direct and well-established. Acute manic episodes are characterised by hyperactivation of the mesolimbic dopamine system, manifesting as psychomotor agitation, grandiosity, pressured speech, and reduced need for sleep. This dopaminergic excess is pharmacologically indistinguishable from the hyperdopaminergic state targeted in acute psychosis, meaning Haloperidol's mechanism is immediately applicable. Multiple international treatment guidelines — including BAP (British Association for Psychopharmacology), CANMAT, and WFSBP — include Haloperidol as a treatment option for acute mania on exactly this basis.

The TxGNN prediction is therefore not a novel repurposing hypothesis but a confirmation of an already-established off-label and guideline-supported use. The prediction score of 99.83% and L1 evidence level together reflect decades of real-world clinical evidence. The primary clinical consideration for the Netherlands context is that CBG-MEB authorisation specifically for bipolar mania may need to be verified, and that Haloperidol's extrapyramidal side-effect (EPS) burden makes it second-line to atypical antipsychotics in most contemporary guidelines.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT00253162](https://clinicaltrials.gov/study/NCT00253162) | Phase 3 | Completed | 439 | Risperidone vs Placebo vs **Haloperidol** in bipolar I manic episodes; provides direct 3-week and 12-week haloperidol efficacy and safety data |
| [NCT00253149](https://clinicaltrials.gov/study/NCT00253149) | Phase 3 | Completed | 158 | Risperidone vs Placebo vs **Haloperidol** as add-on to mood stabilisers in bipolar mania; direct head-to-head comparative data |
| [NCT00129220](https://clinicaltrials.gov/study/NCT00129220) | Phase 3 | Completed | 224 | Olanzapine vs Placebo vs **Haloperidol** (active comparator) in bipolar I manic/mixed episode; haloperidol benchmark efficacy data |
| [NCT00097266](https://clinicaltrials.gov/study/NCT00097266) | Phase 3 | Completed | 615 | Aripiprazole monotherapy vs Placebo in bipolar I mania over 12 weeks; provides indirect comparison context against a D2-active agent class |
| [NCT00126009](https://clinicaltrials.gov/study/NCT00126009) | Phase 2 | Completed | 120 | Valproate + Amisulpride vs Valproate + **Haloperidol** (5–15 mg/day) in bipolar I manic episode over 3 months; combination therapy safety comparison |
| [NCT04327843](https://clinicaltrials.gov/study/NCT04327843) | Phase 3 | Completed | 22 | Long-acting injectable antipsychotics (including haloperidol decanoate) in chronic psychotic disorders including bipolar disorder in Tanzania; real-world adherence and effectiveness data |
| [NCT03541031](https://clinicaltrials.gov/study/NCT03541031) | N/A | Unknown | 120 | Micronutrient supplement as adjunct to conventional medications (including antipsychotics) in bipolar disorder; haloperidol used as background medication |
| [NCT06049953](https://clinicaltrials.gov/study/NCT06049953) | N/A | Recruiting | 200 | Observational study of antenatal antipsychotic exposure and infant development in severe mental illness; safety surveillance context |
| [NCT00767715](https://clinicaltrials.gov/study/NCT00767715) | Phase 4 | Terminated | 11 | Olanzapine vs conventional antipsychotics (including haloperidol) in acute mania in Sweden; early termination limits conclusions |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [34642461](https://pubmed.ncbi.nlm.nih.gov/34642461/) | 2022 | Systematic Review + Network Meta-Analysis | Molecular Psychiatry | Comprehensive NMA comparing pharmacological treatments for acute bipolar mania across double-blind RCTs; haloperidol included as a benchmark comparator |
| [22134043](https://pubmed.ncbi.nlm.nih.gov/22134043/) | 2012 | RCT | Journal of Affective Disorders | Randomised double-blind study of olanzapine vs placebo vs haloperidol in Japanese bipolar I manic/mixed episode patients; direct haloperidol efficacy confirmed |
| [3312180](https://pubmed.ncbi.nlm.nih.gov/3312180/) | 1987 | RCT | Journal of Clinical Psychiatry | Double-blind controlled trial comparing clonazepam with haloperidol in acutely manic patients; advantages of benzodiazepines over neuroleptics discussed |
| [369472](https://pubmed.ncbi.nlm.nih.gov/369472/) | 1979 | RCT | Archives of General Psychiatry | Double-blind 5-week trial of lithium carbonate + haloperidol vs placebo + haloperidol in excited schizo-affective illness (N=36); statistically significant benefit of combination |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Clinical Review | Acta Psychiatrica Scandinavica | Evidence-based treatment recommendations for bipolar mania; haloperidol positioned as add-on option for partial responders to mood stabilisers |
| [22070611](https://pubmed.ncbi.nlm.nih.gov/22070611/) | 2012 | Review | CNS Neuroscience & Therapeutics | Treatment of refractory bipolar disorder; haloperidol cited as a recommended add-on for acutely manic patients with partial response to lithium/valproate/carbamazepine |
| [36789916](https://pubmed.ncbi.nlm.nih.gov/36789916/) | 2023 | Comparative Analysis | BMJ Mental Health | Comparison of antipsychotic dose equivalents for acute bipolar mania vs schizophrenia; provides practical dosing reference for haloperidol in mania context |
| [18344731](https://pubmed.ncbi.nlm.nih.gov/18344731/) | 2008 | Systematic Review | Journal of Clinical Psychopharmacology | Systematic review of antipsychotic-induced EPS in bipolar disorder and schizophrenia; haloperidol consistently shows higher EPS burden vs atypicals — key safety consideration |
| [39756485](https://pubmed.ncbi.nlm.nih.gov/39756485/) | 2025 | Retrospective Study | Journal of Affective Disorders | Real-world effectiveness of long-acting injectable antipsychotics (including haloperidol decanoate) in reducing rehospitalisation during bipolar manic episodes |
| [10343182](https://pubmed.ncbi.nlm.nih.gov/10343182/) | 1999 | Clinical Study | Neuropsychobiology | Investigation of lithium and haloperidol effects on Gαs protein levels in bipolar affective disorder; mechanistic insights into combined pharmacotherapy |

---

## Netherlands Market Information

No CBG-MEB marketing authorizations were returned by the current data query (market status recorded as "not registered", 0 licenses).

This result is inconsistent with Haloperidol's status as a long-established generic medicine available across EU member states. Haloperidol and its decanoate long-acting injectable formulation have EMA/national marketing authorizations in multiple EU countries. A direct search of the CBG-MEB public registry (https://www.cbg-meb.nl) is recommended to retrieve current RVG numbers, approved SmPC texts, and registered indications before any clinical or regulatory proceeding.

---

## Safety Considerations

All safety fields (key warnings, contraindications, drug interactions) were not retrieved in the current evidence package.

> Please refer to the current SmPC (Samenvatting van de Productkenmerken) for Haloperidol via the CBG-MEB registry for full warnings, contraindications, and drug interaction data.

The following safety signal is consistently highlighted in the retrieved literature and warrants particular attention for this indication:

- **Extrapyramidal side effects (EPS):** Multiple systematic reviews (PMID 18344731) confirm that Haloperidol carries a substantially higher EPS burden than second-generation antipsychotics. This is the primary reason contemporary bipolar mania guidelines position it as a second-line agent despite proven efficacy. Monitoring for akathisia, parkinsonism, and tardive dyskinesia is essential.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Haloperidol's use in acute bipolar mania is not a novel repurposing hypothesis — it is a guideline-supported indication with direct evidence from at least two completed Phase 3 RCTs in which it served as the primary active comparator (NCT00253162, NCT00253149), qualifying this as L1 evidence. The D2 receptor antagonism mechanism maps directly onto the dopaminergic hyperactivity pathophysiology of acute mania. The TxGNN model prediction is concordant with established clinical knowledge.

**To proceed, the following is needed:**

1. **Confirm NL regulatory status:** Verify current CBG-MEB registration and approved indications for Haloperidol via direct registry search — the 0-license result is likely a data pipeline gap, not true non-registration.
2. **Retrieve current SmPC:** Download the Dutch SmPC to extract approved indications, contraindications, and current warnings (addresses data gaps DG001 and DG002).
3. **Clarify indication scope:** Determine whether the CBG-MEB SmPC already includes bipolar mania, or whether this constitutes off-label use requiring pharmacovigilance documentation.
4. **EPS risk management plan:** Given the higher EPS burden vs. atypical antipsychotics, a clinical monitoring protocol (baseline neurological assessment, AIMS scale follow-up) should be included in any prescribing guidance.
5. **Consider second-line positioning:** For NL guideline alignment, evaluate whether Haloperidol should be positioned as first-line monotherapy or as an add-on/alternative for patients who fail or cannot tolerate atypical antipsychotics (e.g., olanzapine, quetiapine, aripiprazole).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

