---
layout: default
title: Tadalafil
parent: 僅模型預測 (L5)
nav_order: 115
evidence_level: L5
indication_count: 8
---

# Tadalafil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

以下是根據 Evidence Pack 產生的完整評估報告：

---

# Tadalafil: From Erectile Dysfunction to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Tadalafil is a selective PDE5 (phosphodiesterase type 5) inhibitor, approved in the European Union for erectile dysfunction, benign prostatic hyperplasia, and pulmonary arterial hypertension.
The TxGNN model predicts it may be effective for **Ambras Type Hypertrichosis Universalis Congenita**, a rare genetic hair disorder; however, this prediction is currently supported by **0 clinical trials** and **0 publications** — indicating the model score reflects knowledge graph topology rather than confirmed biological plausibility.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in CBG-MEB database (no registered products found — see note below) |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| NL Market Status | Not Registered (data gap suspected — see note below) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

> ⚠️ **Data Gap Notice**: Tadalafil (Cialis®, Adcirca®) holds EMA central marketing authorizations valid across all EU member states including the Netherlands. The CBG-MEB records showing 0 licenses most likely reflect an incomplete data pull rather than actual non-registration. **Direct verification via the CBG-MEB public register is required before drawing any regulatory conclusions.**

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on publicly known information, Tadalafil is a selective inhibitor of phosphodiesterase type 5 (PDE5). By blocking PDE5, it prevents degradation of cyclic guanosine monophosphate (cGMP), leading to smooth muscle relaxation and vasodilation. Its established therapeutic areas — erectile dysfunction, pulmonary arterial hypertension (PAH), and benign prostatic hyperplasia — all share this PDE5-mediated vascular mechanism.

Ambras type hypertrichosis universalis congenita is an exceptionally rare genetic disorder caused by mutations in the TRPS1 gene (tricho-rhino-phalangeal syndrome locus on chromosome 8q24), resulting in diffuse excessive hair growth across the entire body. The pathological mechanism involves dysregulation of hair follicle activation — a process with no established connection to the PDE5/cGMP signalling axis. Although cGMP signalling has been explored in basic hair follicle biology, no therapeutic link to Tadalafil has been proposed or demonstrated in any published study.

The high TxGNN prediction score (99.98%) most likely reflects **topological clustering** within the knowledge graph — "hair-related disease" nodes sharing graph neighbours with diseases already connected to Tadalafil — rather than true biological plausibility. This interpretation is consistent with the complete absence of supporting clinical or pre-clinical evidence. Notably, among all 8 TxGNN-predicted indications in this Evidence Pack, **kyphoscoliotic heart disease** (rank 7, score 99.43%) carries the most mechanistically coherent rationale: kyphoscoliosis → restrictive lung disease → chronic hypoxia → secondary PAH (WHO Group 3) — an indirect extrapolation of Tadalafil's approved PAH indication (Adcirca®, Group 1), which merits separate investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Tadalafil in Ambras type hypertrichosis universalis congenita.

---

## Literature Evidence

Currently no related literature available for Tadalafil in Ambras type hypertrichosis universalis congenita.

---

## Netherlands Market Information

No CBG-MEB marketing authorizations were retrieved for Tadalafil in the current dataset. This is inconsistent with known EU regulatory status and is attributed to a data collection gap.

| RVG Number | Product Name | Dosage Form | Approved Indication |
|-----------|-------------|-------------|-------------------|
| — | — | — | No records retrieved. Verify directly at cbg-meb.nl |

For authoritative registration details, consult:
- CBG-MEB public register: [https://www.cbg-meb.nl/](https://www.cbg-meb.nl/)
- EMA product page for Cialis® / Adcirca®: [https://www.ema.europa.eu/](https://www.ema.europa.eu/)

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information.

> No safety data (warnings, contraindications, drug interactions) was returned in this Evidence Pack. The SmPC for Tadalafil is available via the EMA website and the CBG-MEB product database.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite the high TxGNN prediction score (99.98%), there is a complete absence of clinical or pre-clinical evidence connecting Tadalafil to Ambras type hypertrichosis universalis congenita, and no biologically plausible mechanistic pathway has been identified. The prediction is assessed as a knowledge graph artefact, not a drug repurposing opportunity.

**To proceed, the following is needed:**

- **Regulatory data**: Verify CBG-MEB authorizations for Tadalafil directly at cbg-meb.nl; retrieve the current Dutch SmPC for Cialis® and Adcirca®
- **Safety review**: Obtain full contraindications, key warnings, and DDI profile from the SmPC before any further clinical evaluation
- **Re-prioritise predictions**: Redirect investigation to **kyphoscoliotic heart disease** (rank 7), which has a mechanistically grounded PAH pathway and represents the most actionable repurposing hypothesis in this pack
- **Mechanistic research**: If pursuing the hypertrichosis indication, a dedicated pre-clinical investigation into cGMP/PDE5 roles in TRPS1-related hair follicle pathology would be required as a first step
- **Original MOA documentation**: Retrieve Tadalafil MOA data from DrugBank (DB00820) to complete the mechanistic analysis for all predicted indications

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. — NlTxGNN Evidence Pack v4 | Data cutoff: 2026-05-05*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

