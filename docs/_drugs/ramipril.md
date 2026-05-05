---
layout: default
title: Ramipril
parent: 僅模型預測 (L5)
nav_order: 109
evidence_level: L5
indication_count: 10
---

# Ramipril
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

Using the Drug Repurposing Evaluation Report Prompt (v5) already loaded as my system prompt, I'll proceed directly to generate the report.

---

# Ramipril: From Hypertension to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

Ramipril is an angiotensin-converting enzyme (ACE) inhibitor with well-established cardiovascular indications — including hypertension, heart failure, post-myocardial infarction management, and renal protection — though no active CBG-MEB marketing authorizations are recorded in the current dataset for the Netherlands.
The TxGNN model predicts it may be effective for **pulmonary hypertension with unclear multifactorial mechanism**, representing the highest-ranked repurposing signal.
However, **no clinical trials and no publications** directly support this specific direction, making this a model-only prediction at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No CBG-MEB authorization records available (drug not registered per current dataset) |
| Predicted New Indication | Pulmonary Hypertension with Unclear Multifactorial Mechanism |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| NL Market Status | Not registered (per current CBG-MEB records) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, Ramipril belongs to the ACE inhibitor (ACEI) drug class. It blocks the conversion of angiotensin I to angiotensin II within the renin-angiotensin-aldosterone system (RAAS), thereby reducing systemic vascular resistance, aldosterone secretion, and — theoretically — pulmonary vascular tone. Its efficacy in hypertension and cardiovascular risk reduction is well established through large landmark trials (including the HOPE trial) and renal protection through the REIN study.

The theoretical basis for the TxGNN prediction rests on the partial overlap between RAAS activation and pulmonary vascular pathophysiology. Angiotensin II promotes pulmonary vasoconstriction, smooth muscle proliferation, and endothelial dysfunction, all of which contribute to elevated pulmonary vascular resistance. By suppressing angiotensin II activity, Ramipril could, in principle, attenuate one of the contributing pathways in multifactorial pulmonary hypertension.

In clinical reality, however, this overlap is insufficient to drive therapeutic efficacy. Pulmonary hypertension with unclear multifactorial mechanism is governed by multiple parallel pathogenic axes — including endothelin-1 (ET-1), platelet-derived growth factor (PDGF), and dysregulated bone morphogenetic protein receptor type II (BMPR2) signalling — that are entirely outside the scope of RAAS blockade. ACE inhibition may also lower systemic blood pressure without proportionally reducing pulmonary vascular resistance, introducing a risk of adverse compensatory haemodynamics in this patient population. Accordingly, the mechanistic rationale is weak, and no clinical signal has been identified to support this prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Netherlands Market Information

No CBG-MEB marketing authorizations for Ramipril are recorded in the current dataset. This is likely a **data pipeline gap** rather than a true absence from the Dutch market — Ramipril is a widely used generic ACE inhibitor available throughout Europe, and centrally or nationally authorized products may not yet be captured in this evidence pack.

Before any regulatory action, the current authorization status should be verified directly via:
- The **CBG-MEB public register** at [geneesmiddeleninformatiebank.nl](https://www.geneesmiddeleninformatiebank.nl)
- The **EMA product database** for centrally authorized generics
- The relevant **SmPC (Samenvatting van de Productkenmerken)** for approved indications and safety data

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information.

> **Note:** Safety data (key warnings, contraindications, and drug interactions) were not available in this evidence pack. For a drug of Ramipril's profile — an ACE inhibitor with known class effects including hyperkalaemia, acute kidney injury in renovascular disease, angioedema, and teratogenicity — SmPC review is **mandatory** before any clinical or regulatory evaluation proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is rated L5 (model prediction only, no supporting clinical trials or publications). The mechanistic link between ACE inhibition and multifactorial pulmonary hypertension is theoretically plausible but pharmacologically insufficient — RAAS blockade addresses only a minor component of a complex, multi-pathway disease — and the risk of adverse systemic hypotension in PAH patients is a documented safety concern that further limits development interest.

**To proceed, the following is needed:**

- **Regulatory data gap resolution**: Retrieve the current CBG-MEB authorization records and SmPC for Ramipril to confirm NL market status, approved indications, and formal safety data
- **MOA data retrieval**: Query the DrugBank API (DB00178) to populate mechanism of action fields and drug interaction profile
- **Preclinical evidence review**: Identify whether any animal or in vitro studies have investigated ACE inhibition specifically in multifactorial PAH models (distinct from HPV-driven or idiopathic PAH)
- **Comparator context**: Review existing PAH therapies (endothelin receptor antagonists, PDE-5 inhibitors, prostacyclin analogues) to assess whether RAAS inhibition could play an adjunctive rather than primary role
- **Safety modelling**: Given the known class risk of haemodynamic decompensation in PAH, a structured benefit-risk assessment would be required before any exploratory clinical investigation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

