---
layout: default
title: Irbesartan
parent: 僅模型預測 (L5)
nav_order: 80
evidence_level: L5
indication_count: 4
---

# Irbesartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Using `txgnn-pipeline` skill — confirmed this is the NlTxGNN (Netherlands) pipeline. Proceeding to generate the report from the Evidence Pack.

---

# Irbesartan: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Irbesartan is an angiotensin II receptor blocker (ARB) widely used for hypertension and diabetic nephropathy, acting by selectively blocking the AT1 receptor to reduce blood pressure and protect kidney function.
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**, with a prediction score of **99.31%**.
However, no clinical trials or publications specifically addressing this indication were identified in the current evidence search — the prediction rests on mechanistic plausibility alone.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension and diabetic nephropathy (inferred from drug class; no NL authorisation data available) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| NL Market Status | Not Marketed (per current dataset) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the Evidence Pack. Based on established pharmacology, Irbesartan is an angiotensin II receptor blocker (ARB) that selectively antagonises the AT1 receptor, thereby blocking the downstream effects of angiotensin II — including systemic vasoconstriction, aldosterone-driven sodium retention, and efferent arteriolar constriction within the glomerulus. The net effect is a reduction in both systemic blood pressure and glomerular capillary pressure, which slows progressive hypertensive kidney injury.

Malignant hypertensive renal disease shares precisely this pathological axis: severe, uncontrolled hypertension drives glomerular ischaemia, fibrinoid necrosis of arterioles, and rapid deterioration of renal function. ARBs have demonstrated renal-protective efficacy in adjacent conditions — the landmark IDNT trial showed irbesartan itself slows progression of diabetic nephropathy, and the RENAAL trial supported losartan in a comparable setting. Malignant hypertensive nephropathy represents an accelerated, high-pressure variant of this same mechanism, making the extension of ARB therapy conceptually coherent.

That said, the current evidence search returned zero clinical trials and zero publications directly studying irbesartan in malignant hypertensive renal disease. The TxGNN prediction is mechanistically plausible and algorithmically high-confidence, but it currently has no direct empirical backing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Netherlands Market Information

No CBG-MEB marketing authorisations are recorded for Irbesartan in the current dataset.

> **Note:** This likely reflects a data gap rather than the true market situation. Irbesartan (Aprovel® and multiple generics) is a well-established ARB in the Netherlands. Please verify current authorisation status directly via the [CBG-MEB Geneesmiddelenrepertorium](https://www.geneesmiddelenrepertorium.nl/) before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics / Samenvatting van de Productkenmerken) for complete safety information. Given the target indication (malignant hypertensive renal disease), the following drug class–level cautions are clinically relevant and should be confirmed against the current SmPC before any use:

- **Risk of acute kidney injury** in patients with bilateral renal artery stenosis or a solitary functioning kidney — AT1R blockade removes the compensatory efferent arteriolar tone, potentially causing acute GFR collapse (directly relevant to rank 2 indication as well).
- **Hyperkalaemia** risk in patients with advanced renal impairment or concurrent use of potassium-sparing agents.
- **First-dose hypotension** in volume-depleted patients, which is particularly relevant in the acute management of malignant hypertension.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high mechanistic prediction score (99.31%), and the pathophysiological link between AT1R blockade and malignant hypertensive renal injury is conceptually well-grounded. However, the complete absence of supporting clinical trials or direct literature evidence places this at Evidence Level L5 — model prediction only — which is insufficient to advance to clinical application without further investigation.

**To proceed, the following is needed:**

- **Literature gap-fill:** Targeted search for class-wide ARB evidence (irbesartan, losartan, valsartan) specifically in malignant or accelerated-phase hypertension with renal involvement, to assess whether L5 can be upgraded to L3 or L4.
- **MOA data:** Resolve the DrugBank data gap (DG002) by querying the DrugBank API for irbesartan's full mechanism, targets, and pharmacodynamic profile.
- **NL regulatory verification:** Confirm actual CBG-MEB authorisation status; the current dataset records 0 licences, which conflicts with Irbesartan's known European market presence.
- **SmPC review:** Obtain and parse the irbesartan SmPC (DG001) to complete contraindication and warning profiling — currently a blocking data gap for safety assessment (DG001, Severity: Blocking).
- **Nephrology expert consultation:** Assess clinical feasibility in the malignant hypertension setting, including whether emergent blood pressure management protocols would allow ARB use or would favour alternative agents (e.g., IV labetalol, nitroprusside) in the acute phase.
- **Safety monitoring plan:** Define renal function and potassium monitoring protocol appropriate for patients with existing hypertensive renal injury.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

