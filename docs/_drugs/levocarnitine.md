---
layout: default
title: Levocarnitine
parent: 僅模型預測 (L5)
nav_order: 86
evidence_level: L5
indication_count: 10
---

# Levocarnitine
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

Using `txgnn-pipeline` to confirm Netherlands (Nl) deployment context. Now generating the CBG-MEB evaluation report based on `predicted_indications[0]` (rank 1) per the report format specification.

---

# Levocarnitine: From Carnitine Deficiency to Autosomal Dominant Familial Hematuria–Retinal Arteriolar Tortuosity–Contractures Syndrome

## One-Sentence Summary

Levocarnitine is an endogenous amino acid derivative used to treat primary and secondary carnitine deficiency, supporting fatty acid transport into the mitochondrial matrix to sustain cellular energy production.
The TxGNN model predicts it may be effective for **Autosomal Dominant Familial Hematuria–Retinal Arteriolar Tortuosity–Contractures Syndrome**,
with **no clinical trials** and **no publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Carnitine deficiency (primary and secondary) |
| Predicted New Indication | Autosomal Dominant Familial Hematuria–Retinal Arteriolar Tortuosity–Contractures Syndrome |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| NL Market Status | Not on market |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Levocarnitine in this context. Based on known information, Levocarnitine is a biologically active form of carnitine that is indispensable for mitochondrial fatty acid β-oxidation (FAO): it acts as the obligatory carrier molecule that shuttles long-chain fatty acyl-CoA species across the inner mitochondrial membrane via the carnitine palmitoyltransferase 1 and 2 (CPT1/CPT2) system. Its established clinical uses include primary systemic carnitine deficiency and secondary deficiency states arising from renal dialysis or inborn errors of metabolism.

Autosomal dominant familial hematuria–retinal arteriolar tortuosity–contractures syndrome is a rare multisystem genetic disorder characterised by recurrent haematuria, tortuosity of retinal arterioles, and joint contractures. Its molecular basis and affected pathways are not well characterised in the current literature, and no mechanistic overlap with carnitine metabolism or FAO has been reported.

The TxGNN model's high score (99.94%, rank 199 of all predictions) most likely reflects indirect comorbidity or shared pathway co-occurrence patterns captured within the knowledge graph, rather than any direct drug–disease biological relationship. The model's own repurposing rationale flags this as a probable false positive arising from graph sparsity around this ultra-rare disease node. Without any preclinical, translational, or clinical data to support the hypothesis, mechanistic plausibility cannot be established at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Netherlands Market Information

Levocarnitine holds **no marketing authorisations** in the Netherlands. No RVG numbers have been granted by the CBG-MEB for any indication. Any future clinical use would require either a full marketing authorisation application (MAA) via the EMA centralised procedure or the national procedure, or a compassionate-use / hospital exemption pathway under Dutch medicines law (Geneesmiddelenwet).

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high score to this prediction, but no mechanistic link, preclinical data, or clinical evidence connects levocarnitine to the molecular pathology of autosomal dominant familial hematuria–retinal arteriolar tortuosity–contractures syndrome. This pattern is consistent with a knowledge-graph false positive driven by indirect disease associations rather than a pharmacologically actionable hypothesis.

**To proceed, the following is needed:**
- Identification of the causative gene(s) and affected molecular pathway(s) for this syndrome, to assess whether mitochondrial FAO or carnitine transport plays any role
- Expert consultation with a metabolic geneticist or rare-disease specialist
- Screening of rare-disease registries (e.g., Orphanet, OMIM) for any reported carnitine-related phenotypic overlap

---

> **⚠️ Note on higher-priority predictions within this Evidence Pack**
>
> This report addresses the top TxGNN-ranked indication. Two other predictions in this evidence pack carry substantially stronger clinical evidence and an actionable **"Proceed with Guardrails"** recommendation, and should be prioritised for separate, full evaluation:
>
> | Rank | Indication | Evidence Level | Trials | Decision |
> |------|-----------|----------------|--------|----------|
> | 4 | Rheumatoid Arthritis | L2 | 3 (incl. 1 completed Phase 2 RCT, 1 Phase 3) | Proceed with Guardrails |
> | 9 | Congestive Heart Failure | L2 | 12 (incl. 1 completed Phase 2/3 RCT, n=268) | Proceed with Guardrails |
>
> Both indications have direct clinical intervention studies examining levocarnitine, published mechanistic literature linking carnitine/FAO to disease pathology, and biologically plausible rationale. Dedicated evaluation reports for these two indications are recommended as the immediate next step.

---

*This report is intended for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All content should be reviewed against the current SmPC and CBG-MEB/EMA regulatory guidance.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

