---
layout: default
title: Carvedilol
parent: 僅模型預測 (L5)
nav_order: 39
evidence_level: L5
indication_count: 5
---

# Carvedilol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Carvedilol: From Hypertension/Heart Failure to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Carvedilol is a non-selective β1/β2 and α1 adrenoceptor blocker, clinically established for the treatment of hypertension and heart failure.
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**,
with **no clinical trials** and **no directly relevant publications** currently supporting this specific direction — placing this prediction at evidence level L5.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension and heart failure (established pharmacological use; no NL authorizations on record) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 |
| NL Market Status | Not authorised in the Netherlands |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, Carvedilol is a third-generation non-selective β1/β2 adrenoceptor blocker with additional α1-adrenoceptor blocking activity. This dual mechanism simultaneously reduces cardiac output (via β1 blockade) and systemic vascular resistance (via α1 blockade), providing a more comprehensive blood pressure reduction than selective β-blockers alone. Carvedilol also possesses antioxidant properties and has demonstrated renoprotective effects in chronic heart failure models.

Malignant hypertensive renal disease is defined by severely elevated blood pressure (typically MAP >150 mmHg) accompanied by acute renal injury. The pathophysiology involves renal arteriolar damage, fibrinoid necrosis, and a vicious cycle of ischaemia-driven renin-angiotensin activation. In the chronic management phase — once the acute hypertensive crisis has been controlled with intravenous agents — an oral antihypertensive with vasodilatory and renoprotective properties such as Carvedilol is theoretically attractive, particularly if renal function (eGFR) has stabilised.

However, it is important to note that in the acute setting, oral Carvedilol has an onset of action that is too slow for first-line use, and the standard of care relies on intravenous agents (e.g., Labetalol IV, Nicardipine IV). The TxGNN prediction likely reflects the mechanistic overlap between Carvedilol's haemodynamic properties and the blood pressure control needs of this condition, rather than a validated clinical application. Dose adjustment would be required in patients with impaired renal function (eGFR <30 ml/min/1.73 m²).

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Carvedilol in malignant hypertensive renal disease.

---

## Literature Evidence

Currently no related literature available for Carvedilol in malignant hypertensive renal disease.

---

## Netherlands Market Information

Carvedilol currently holds no marketing authorisation registered in the CBG-MEB dataset used for this analysis (market status: not authorised). There are no RVG numbers on record.

> **Note for reviewers:** Carvedilol is a long-established generic medicine. If this absence from the NL registry reflects a data gap rather than a genuine lack of authorisation, the regulatory data should be verified directly against the CBG-MEB public register prior to any further evaluation.

---

## Other Top TxGNN Predictions (Summary)

For completeness, the remaining four TxGNN-predicted indications are summarised below. All are rated L5 and all carry a **Hold** or **Research Question** recommendation:

| Rank | Disease | TxGNN Score | Recommendation | Rationale Summary |
|------|---------|-------------|---------------|-------------------|
| 2 | Malignant Renovascular Hypertension | 99.55% | Hold | β-blockade may acutely reduce GFR in bilateral renal artery stenosis; safety concerns outweigh theoretical benefit |
| 3 | Pulmonary Hypertension — Multifactorial (Group 5) | 99.54% | Research Question | Emerging data (COMPASS-2) suggests possible benefit on right ventricular remodelling when added to targeted PAH therapy; requires careful patient selection |
| 4 | Pulmonary Hypertension — Lung Disease/Hypoxia (Group 3) | 99.54% | Hold | Risk of bronchospasm (β2 blockade), masking of compensatory tachycardia, and worsening right ventricular decompensation; 20 retrieved publications address general hypoxia biology only, with no Carvedilol-specific data |
| 5 | Braddock Syndrome | 99.37% | Hold | SETD1B epigenetic pathway has no known intersection with adrenoceptor blockade; high TxGNN score likely reflects non-specific graph topology artefact |

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information. No key warnings, contraindications, or drug interaction data were retrievable from the current Evidence Pack.

> **Data gap:** TFDA/CBG-MEB SmPC warning and contraindication data (DG001) and detailed MOA information (DG002) are flagged as outstanding items. These must be resolved before progressing to formal safety screening (Stage S1).

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The TxGNN model produces a high prediction score (99.55%) for Carvedilol in malignant hypertensive renal disease, which is mechanistically plausible given the drug's dual adrenoceptor blockade and theoretical renoprotective properties in the chronic post-crisis management phase. However, there is currently zero clinical trial or literature evidence specific to this drug-disease combination, placing this at the lowest evidence tier (L5). The ranking does not yet constitute a sufficient basis for clinical development or off-label use, but it merits a structured preclinical and literature review.

**To proceed, the following is needed:**

- **Resolve DG001**: Retrieve the SmPC (Samenvatting van de Productkenmerken) via the CBG-MEB public register to obtain contraindications, key warnings, and dose-adjustment guidance for renal impairment
- **Resolve DG002**: Obtain confirmed MOA data from DrugBank (DB01136) to complete the mechanistic linkage analysis
- **Verify NL market status**: Cross-check CBG-MEB register to confirm whether Carvedilol holds existing RVG authorisations that were absent from the current dataset
- **Targeted literature search**: Conduct a focused PubMed/EMBASE search using MeSH terms `Carvedilol AND (malignant hypertension OR hypertensive nephropathy OR hypertensive emergency)` to identify any case series or retrospective studies
- **Renal function sub-analysis**: Evaluate available evidence on Carvedilol pharmacokinetics and safety in patients with eGFR <30 ml/min/1.73 m²
- **Expert consultation**: Seek input from a nephrologist and cardiologist specialising in hypertensive emergencies before designing any prospective investigation

> *This report is intended for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application. All content should include appropriate YMYL disclaimers when published.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

