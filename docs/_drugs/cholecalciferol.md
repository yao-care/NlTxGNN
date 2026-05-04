---
layout: default
title: Cholecalciferol
parent: 僅模型預測 (L5)
nav_order: 41
evidence_level: L5
indication_count: 7
---

# Cholecalciferol
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

# Cholecalciferol: From Vitamin D Supplementation to Familial Isolated Hypoparathyroidism Due to Impaired PTH Secretion

## One-Sentence Summary

Cholecalciferol (Vitamin D3) is a fat-soluble nutrient and pharmaceutical agent classically used to correct vitamin D deficiency and support calcium-phosphorus homeostasis and bone health, though it currently holds no marketing authorisation with the Dutch CBG-MEB.
The TxGNN model predicts it may be effective for **Familial Isolated Hypoparathyroidism Due to Impaired PTH Secretion** (global rank #553 across all disease predictions),
with **no clinical trials** and **no disease-specific publications** currently supporting this direction — evidence remains at model-prediction level only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vitamin D deficiency; calcium and phosphorus metabolism support (no NL marketing authorisation on record) |
| Predicted New Indication | Familial isolated hypoparathyroidism due to impaired PTH secretion |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| NL Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Formal mechanism of action data was not retrieved from DrugBank for this Evidence Pack. However, the pharmacology of Cholecalciferol is well established: it is an **inactive precursor of the vitamin D hormone system**. Following skin synthesis or oral intake, cholecalciferol undergoes first-pass 25-hydroxylation in the liver (producing 25-hydroxyvitamin D, the main circulating storage form) and then a critical second hydroxylation in the kidney via the enzyme 1α-hydroxylase (CYP27B1), yielding calcitriol [1,25(OH)₂D] — the biologically active hormone that promotes intestinal calcium and phosphate absorption and acts on bone and the parathyroid glands.

Familial isolated hypoparathyroidism due to impaired PTH secretion is a rare hereditary condition in which the parathyroid glands are structurally present but fail to secrete adequate PTH. This results in chronic hypocalcaemia and hyperphosphataemia. The critical pharmacological problem for cholecalciferol in this setting is that **PTH is one of the primary stimulators of renal 1α-hydroxylase**: PTH deficiency therefore directly impairs the conversion of cholecalciferol to calcitriol. Supplementing the inactive precursor in a patient who cannot efficiently activate it is a mechanistically suboptimal strategy, and carries a genuine risk of therapeutic underperformance. Active vitamin D analogues — calcitriol or alfacalcidol — bypass this conversion bottleneck entirely and represent the current clinical standard of care for hypoparathyroidism.

The TxGNN model assigns a high score (99.79%) to this pairing, most likely because the model captures the shared nodes connecting vitamin D metabolism, calcium signalling, and parathyroid biology in the knowledge graph, rather than detecting a specific pharmacological superiority of cholecalciferol over established active analogues. The mechanistic connection is real at a biological systems level but highly speculative as a therapeutic rationale for cholecalciferol specifically. No clinical trials and no disease-specific publications have been identified to support this repurposing direction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific indication (familial isolated hypoparathyroidism due to impaired PTH secretion).

---

## Literature Evidence

Currently no related literature available specific to this indication.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information. No drug-drug interaction data, key warnings, or contraindications were identified in the data sources queried for this Evidence Pack (DDI query status: not found; key warnings and contraindications: unavailable from the queried sources).

> **Practical note for clinicians:** Although specific safety data was not retrieved, well-known class-level risks of vitamin D supplementation include **hypercalcaemia** and **hypercalciuria**, which are of particular concern when used in conditions where calcium homeostasis is already impaired, such as hypoparathyroidism. Close monitoring of serum calcium, urine calcium, and renal function is standard practice.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a model-level prediction (L5) with zero supporting clinical trials or disease-specific publications. More critically, the mechanistic rationale is pharmacologically self-limiting: cholecalciferol, as an inactive precursor requiring PTH-dependent 1α-hydroxylation for activation, is not the appropriate drug form in a condition defined by PTH deficiency. Active vitamin D analogues (calcitriol, alfacalcidol) are the established and guideline-supported standard of care for hypoparathyroidism and would be the scientifically coherent repurposing candidates in this disease area — not cholecalciferol.

**To proceed, the following would be needed:**

- Retrieval of TFDA/EMA SmPC data for formal safety assessment (warnings, contraindications, toxicology)
- Full DrugBank MOA data retrieval to confirm the mechanistic basis
- A preclinical or mechanistic study specifically demonstrating that cholecalciferol provides a clinically meaningful benefit **beyond or above** calcitriol/alfacalcidol in PTH-deficient patients (e.g., via extrarenal 1α-hydroxylation pathways)
- At minimum, case reports or pilot data specifically in familial isolated hypoparathyroidism using cholecalciferol as the intervention
- Clarification of cholecalciferol's regulatory classification in the Netherlands (food supplement vs. medicinal product), as this affects the applicable regulatory pathway under CBG-MEB/EMA framework

> **Research note:** If the broader vitamin D–hypoparathyroidism repurposing question is of interest, pivoting the investigation to **active analogues already registered in the Netherlands** (calcitriol, alfacalcidol, paricalcitol) would be mechanistically more defensible and likely to yield higher-quality evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

