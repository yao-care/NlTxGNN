---
layout: default
title: Olanzapine
parent: 僅模型預測 (L5)
nav_order: 99
evidence_level: L5
indication_count: 3
---

# Olanzapine
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

Using the `txgnn-pipeline` skill to confirm context — this is an NL (Netherlands) drug repurposing report. The skill confirms the NL deployment and standard workflow. Now generating the report from the Evidence Pack.

---

# Olanzapine: From Schizophrenia / Bipolar Disorder to Benign Paroxysmal Torticollis of Infancy

## One-Sentence Summary

Olanzapine is a well-established second-generation (atypical) antipsychotic, approved internationally for schizophrenia and bipolar disorder.
The TxGNN model predicts it may be relevant to **Benign Paroxysmal Torticollis of Infancy (BPTI)**,
with **0 clinical trials** and **0 publications** currently supporting this direction.
Importantly, mechanistic review suggests this is likely a **reverse signal** — olanzapine's dopamine D2 antagonism is a known *cause* of drug-induced torticollis, not a treatment for it.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia; Bipolar Disorder *(NL authorisation data not retrieved — see note below)* |
| Predicted New Indication | Benign Paroxysmal Torticollis of Infancy |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| NL Market Status | Not registered *(data may be incomplete — see note below)* |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this Evidence Pack. Based on established pharmacological knowledge, Olanzapine is a multi-receptor antagonist with particularly strong affinity for dopamine D2 receptors and serotonin 5-HT2A receptors, as well as histamine H1, muscarinic, and alpha-adrenergic receptors. Its proven therapeutic role spans schizophrenia, acute bipolar mania, and — in combination with fluoxetine (as Symbyax) — bipolar depression.

Benign Paroxysmal Torticollis of Infancy (BPTI) is classified under the ICHD-3 as a childhood migraine variant. It presents as recurrent, self-limiting episodes of head tilt in infants and toddlers, with a proposed pathophysiology involving ion channel dysfunction and the trigeminovascular system — a mechanism that is distinct from the dopaminergic targets of olanzapine.

**Critical mechanistic concern:** Rather than a genuine therapeutic signal, this TxGNN prediction is most likely a **reverse mechanistic artefact**. Acute drug-induced dystonia and torticollis are well-recognised adverse effects of D2 receptor antagonists, including olanzapine. The model's high score almost certainly reflects *knowledge graph proximity* — the "torticollis" symptom node is shared between BPTI and the adverse effect profile of olanzapine — rather than any positive treatment relationship. Applying olanzapine in BPTI would be mechanistically contraindicated and could actively worsen the condition.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Netherlands Market Information

No CBG-MEB marketing authorisations for Olanzapine were retrieved in this dataset. This is likely a **data collection gap**: Olanzapine (brand name Zyprexa and multiple generic equivalents) is a centrally authorised medicinal product in the European Union and is expected to be available in the Netherlands under EMA authorisation. Prescribers should verify the current status directly via the [CBG-MEB product register](https://www.cbg-meb.nl/) or the [EMA European Public Assessment Report (EPAR)](https://www.ema.europa.eu/).

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for complete safety information. In particular, given the mechanistic concern above, the sections on **extrapyramidal adverse effects**, **acute dystonia**, and **use in paediatric populations** are especially relevant to any assessment of this predicted indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high score based on knowledge graph proximity via a shared "torticollis" symptom node, but mechanistic analysis identifies this as a **reverse signal**: olanzapine-induced acute dystonia/torticollis is a known adverse drug reaction, making the drug more likely to *cause* the condition than treat it. There is no supporting clinical trial or literature evidence. This candidate should not advance further under the current framing.

**To proceed, the following is needed:**
- Independent mechanistic review by a clinical pharmacologist to formally document the reverse signal and close this candidate
- Retrieval of NL CBG-MEB / EMA authorisation data to correct the market status record for Olanzapine
- Retrieval of the full SmPC (including extrapyramidal warnings and paediatric contraindications) to complete the safety profile
- Completion of MOA data from DrugBank (flagged as DG002) to enable robust mechanistic analysis for all predicted indications
- Consideration of the **Rank 2 (Agoraphobia, L3)** and **Rank 3 (Dysthymic Disorder, L3)** predicted indications, which carry more plausible mechanistic rationale and existing literature, and may be more productive repurposing candidates for further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

