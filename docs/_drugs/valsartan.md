---
layout: default
title: Valsartan
parent: 僅模型預測 (L5)
nav_order: 123
evidence_level: L5
indication_count: 7
---

# Valsartan
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

Using **txgnn-pipeline** context to guide the NL report generation. Now I'll produce the full evaluation report based on the Evidence Pack.

---

# Valsartan: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Valsartan is an angiotensin II type 1 receptor blocker (ARB) established for hypertension and heart failure treatment, though its NL marketing authorization data is not available in the current dataset.
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**, with **0 clinical trials** and **1 publication** currently supporting this direction.
The prediction is mechanistically compelling — RAAS overactivation is the core driver of this condition — but human evidence remains absent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current NL regulatory dataset (Valsartan is a well-established ARB for hypertension and heart failure) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| NL Market Status | Not registered (CBG-MEB dataset returned 0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on widely established pharmacological knowledge, Valsartan is an angiotensin II type 1 (AT1) receptor blocker. It selectively binds the AT1 receptor, blocking the downstream effects of angiotensin II — including vasoconstriction, aldosterone release, and renin-driven sodium retention. This inhibition of the renin-angiotensin-aldosterone system (RAAS) reduces vascular resistance and blood pressure, and attenuates end-organ damage caused by sustained RAAS hyperactivation.

Malignant renovascular hypertension is defined by renal artery stenosis triggering a dangerous positive feedback loop: reduced renal perfusion stimulates excessive renin release → angiotensin II surge → profound renal vasoconstriction → worsening ischemia. RAAS overactivation is the central pathophysiological mechanism of this condition. AT1 receptor blockade by Valsartan directly interrupts this cascade, providing exceptionally strong biological plausibility for the TxGNN prediction — the drug's mechanism maps precisely onto the disease's molecular driver.

Critically, a 2001 preclinical study in *Circulation* (Hilgers et al., PMID 11560862) demonstrated that AT1 receptor blockade can prevent lethal malignant hypertension in an animal model even in the absence of a significant blood pressure-lowering effect, implicating a direct anti-inflammatory and renoprotective mechanism at the kidney vascular level. This suggests Valsartan's benefit in this context may extend beyond simple blood pressure control, further supporting the TxGNN model's high-confidence prediction. However, the absence of human trial data limits the evidence to preclinical level (L4).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11560862](https://pubmed.ncbi.nlm.nih.gov/11560862/) | 2001 | Animal Study (Preclinical) | Circulation | AT1 receptor blockade prevents lethal malignant hypertension in a rodent model; the protective effect is independent of blood pressure reduction and is linked to suppression of kidney inflammation and renal vascular injury |

---

## Netherlands Market Information

No marketing authorizations for Valsartan (as a standalone product) are recorded in the CBG-MEB dataset for the Netherlands in the current data extract. Note that Valsartan is available in the Netherlands as a component of the combination product Sacubitril/Valsartan (Entresto®), which holds EMA central authorization for heart failure with reduced ejection fraction. Standalone Valsartan generics were subject to recall actions in 2018–2019 due to NDMA contamination; current availability should be verified against the CBG-MEB register directly.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics / Samenvatting van de Productkenmerken) for complete safety information. No key warnings, contraindications, or drug interaction data were available in the current Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis for Valsartan in malignant renovascular hypertension is strong — RAAS hyperactivation is the core disease driver and AT1 blockade directly targets it — but the sole available evidence is a single preclinical animal study (L4), with no registered human clinical trials and no clinical observational data. This does not meet the threshold for a repurposing recommendation in the Dutch healthcare context.

**To proceed, the following is needed:**

- **Regulatory verification**: Confirm current NL/EMA market status of standalone Valsartan via the CBG-MEB register, including any reinstated generic authorizations post-NDMA recall
- **MOA data**: Retrieve full DrugBank pharmacology entry (DB00177) to formalize the mechanism of action documentation
- **Safety data**: Download and parse the SmPC from the EMA or CBG-MEB for key warnings, contraindications, and DDI profile
- **Clinical evidence search**: Conduct a targeted systematic search for human case series, registry data, or observational studies on ARB use in malignant renovascular hypertension
- **Nephrology expert consultation**: Engage a CBG-MEB-affiliated nephrologist or clinical pharmacologist to assess whether existing hypertension/renal protection indications already encompass this use under current Dutch prescribing guidelines
- **Evidence upgrade pathway**: Design a feasibility assessment for a prospective registry or Phase 2 pilot study in the Netherlands if the above steps confirm unmet need and acceptable safety margins
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

