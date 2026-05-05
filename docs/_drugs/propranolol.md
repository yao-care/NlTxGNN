---
layout: default
title: Propranolol
parent: 僅模型預測 (L5)
nav_order: 108
evidence_level: L5
indication_count: 6
---

# Propranolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

The txgnn-pipeline skill applies to this task. No additional workflow overrides — I'll now generate the evaluation report following the prompt's v5 format.

---

# Propranolol: From Cardiovascular Conditions to Distal Myopathy, Tateyama Type

## One-Sentence Summary

Propranolol is a classic non-selective beta-adrenergic receptor blocker with a long-established history in cardiovascular medicine, including hypertension, arrhythmias, and hypertrophic obstructive cardiomyopathy (HOCM).
The TxGNN model predicts it may be effective for **Distal Myopathy, Tateyama Type** with a prediction score of **99.40%**,
however **no clinical trials** and **no published literature** currently support this repurposing direction — the signal is assessed as a knowledge graph artifact.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No NL marketing authorisation on file; Propranolol is a well-established non-selective beta-blocker (cardiovascular: hypertension, arrhythmia, HOCM) |
| Predicted New Indication | Distal myopathy, Tateyama type |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| NL Market Status | Not registered (CBG-MEB: 0 authorisations on file) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Propranolol is a non-selective β-adrenergic receptor blocker that competitively antagonises both β1 receptors (heart, kidney) and β2 receptors (bronchi, peripheral vasculature). Its core cardiovascular effects include reducing heart rate, myocardial contractility, cardiac output, and renin secretion — making it effective in hypertension, angina, arrhythmias, and HOCM.

Distal myopathy, Tateyama type, is a rare hereditary skeletal muscle disorder caused by pathogenic variants in the *DYSF* gene, which encodes dysferlin — a protein essential for calcium-dependent membrane repair in skeletal muscle fibres. The underlying pathophysiology (impaired sarcolemmal repair following mechanical stress) has **no established biological link** to β-adrenergic signalling or receptor blockade. There is no published preclinical or clinical hypothesis connecting propranolol's mechanism to dysferlinopathy.

The high TxGNN prediction score (99.40%) is therefore most plausibly explained by a **knowledge graph transitivity artifact**: the graph connects "myopathy" disease nodes to "cardiomyopathy" nodes (via shared muscle-disease ontology), which are themselves strongly linked to beta-blocker nodes through well-documented HOCM evidence. This indirect path generates a high score without reflecting a direct biological mechanism. This prediction requires expert biological validation before any further development steps are considered.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Netherlands Market Information

Per the current CBG-MEB database query, Propranolol has no registered marketing authorisation products on file in the Netherlands (0 RVG numbers, 0 licences). This is unexpected for a molecule with such broad international use and warrants verification directly against the [CBG-MEB online product register](https://www.cbg-meb.nl/). It is possible that available products are marketed under combination names or that the data pipeline did not capture all entries.

*(No RVG authorisation table can be generated — no licensed products found in the current data.)*

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics / Samenvatting van de Productkenmerken) for safety information.

> No key warnings, contraindications, or drug interaction data were available in this Evidence Pack. The CBG-MEB SmPC should be consulted before any clinical or research use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.40%), the mechanistic analysis identifies this as a knowledge graph transitivity artifact — there is no established biological connection between β-adrenergic receptor blockade and DYSF-related skeletal myopathy. With zero supporting clinical trials and zero published literature, the evidence level is L5 (model prediction only), and no actionable development path can be defined at this stage.

**To proceed, the following is needed:**
- Preclinical studies establishing whether β-adrenergic signalling plays any role in dysferlin-deficient muscle pathophysiology (e.g., in *dysf*-null mouse models)
- Independent graph-path audit of the TxGNN knowledge graph to confirm or rule out the transitivity artifact hypothesis
- Retrieval of propranolol's MOA from DrugBank API (data gap DG002) to enable formal plausibility scoring
- Verification of NL market status via direct CBG-MEB register query (potential data pipeline gap)
- Download and parsing of the SmPC (data gap DG001) to complete the safety profile before any S1 safety evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

