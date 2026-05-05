---
layout: default
title: Orlistat
parent: 僅模型預測 (L5)
nav_order: 100
evidence_level: L5
indication_count: 1
---

# Orlistat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

Using the `txgnn-pipeline` skill to generate this NlTxGNN report. The skill confirms this is a Netherlands deployment — applying CBG-MEB regulatory context and the v5 report format.

---

# Orlistat: From Obesity Treatment to Hypervitaminosis

## One-Sentence Summary

Orlistat is a pancreatic and gastric lipase inhibitor, originally used to reduce dietary fat absorption as part of obesity management.
The TxGNN model predicts it may be effective for **Hypervitaminosis** — specifically by blocking the intestinal absorption of fat-soluble vitamins.
However, this direction is currently supported by **no clinical trials** and **no publications**; the prediction rests entirely on model inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Obesity management (lipase inhibitor reducing dietary fat absorption ~30%) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| NL Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Orlistat inhibits pancreatic lipase and gastric lipase, preventing the hydrolysis of dietary triglycerides and thereby reducing fat absorption by approximately 30%. Fat-soluble vitamins — A, D, E, and K — do not have independent transporter-mediated uptake in the gut; instead, they depend on co-solubilisation within lipid-bile salt micelles to cross the intestinal brush border. When Orlistat blocks fat hydrolysis, it structurally disrupts this micellar transport, incidentally suppressing fat-soluble vitamin absorption as well. This shared mechanism is the biological bridge the TxGNN knowledge graph exploits: the Orlistat → fat-soluble vitamin absorption → vitamin toxicity topological path yields a high prediction score (0.994).

In theory, for patients experiencing ongoing hypervitaminosis caused by continuous high-dose supplementation of fat-soluble vitamins — particularly Hypervitaminosis A or D from exogenous dietary sources — Orlistat could reduce further intestinal uptake and slow accumulation. This is not implausible as a mechanistic concept, and the repurposing rationale is internally coherent at the pharmacological level.

There are, however, two fundamental limitations that prevent straightforward clinical translation. First, Orlistat only intercepts vitamins currently in the gut lumen; it cannot mobilise or deplete vitamins already stored in hepatocytes or adipose tissue, which are the primary reservoir in clinically significant hypervitaminosis. For established toxicity, the mechanism is therefore insufficient. Second — and critically — fat-soluble vitamin deficiency (hypovitaminosis A, D, E, K) is itself a well-documented adverse effect of Orlistat. The proposed repurposing direction is mechanistically identical to the drug's own known side effect, meaning the "new use" is essentially the deliberate induction of a pharmacological adverse reaction. This symmetry demands careful clinical framing and stringent monitoring if any investigation were to proceed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Netherlands Market Information

No CBG-MEB marketing authorizations for Orlistat are recorded in the current dataset (0 licenses, status: not registered). No NL SmPC is available through this pipeline.

> **Note:** Orlistat (Xenical®, Alli®) holds a centrally authorised EMA marketing authorisation valid across all EU/EEA Member States, including the Netherlands. This dataset reflects CBG-MEB national authorization records only; the absence of an entry here likely reflects a data pipeline gap rather than a true market absence. The EMA-authorised SmPC should be consulted for the current approved indication, dosing, and safety information.

---

## Safety Considerations

Safety data (warnings and contraindications) was not available in this evidence pack. Please refer to the SmPC (Summary of Product Characteristics) — available via the EMA product page or the CBG-MEB register — for full safety information before any clinical or research use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model score is high (99.42%) and the mechanistic link between Orlistat and fat-soluble vitamin absorption is biologically coherent, the proposed repurposing direction mirrors Orlistat's own established adverse effect profile, applies only to ongoing absorption (not stored vitamin burden), and is entirely unsupported by clinical trial or published evidence at this time.

**To proceed, the following is needed:**

- **Resolve DG001** — Retrieve the EMA/CBG-MEB SmPC to confirm current approved indication, contraindications, and key warnings before any safety assessment
- **Resolve DG002** — Obtain full MOA data from DrugBank (DB01083) to confirm enzyme specificity and vitamin-interaction pathways
- **Clinical feasibility scoping** — Search for case reports or pharmacokinetic studies examining Orlistat's impact on serum fat-soluble vitamin levels in patients with documented hypervitaminosis A or D from supplementation
- **Clinical context definition** — Clarify whether the target use case is acute supplementation-induced toxicity (where absorption reduction is relevant) versus established storage-based toxicity (where it would not be)
- **Risk-benefit framing** — Deliberate induction of vitamin malabsorption as therapy requires an explicit risk-benefit justification; assess whether existing supportive care options (supplementation cessation, vitamin A chelation strategies) make this repurposing unnecessary
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

