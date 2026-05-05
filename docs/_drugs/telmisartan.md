---
layout: default
title: Telmisartan
parent: 僅模型預測 (L5)
nav_order: 116
evidence_level: L5
indication_count: 10
---

# Telmisartan
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

Proceeding to generate the report based on the Evidence Pack. No matching skill tools were returned, so I'll follow the system prompt instructions directly.

---

# Telmisartan: From Hypertension to Prinzmetal Angina

## One-Sentence Summary

Telmisartan is an angiotensin II type 1 receptor blocker (ARB) widely used in the management of hypertension and cardiovascular risk reduction.
The TxGNN model predicts it may be effective for **Prinzmetal Angina** (variant angina due to coronary vasospasm),
with **no clinical trials** and **no publications** currently supporting this specific direction.
The model prediction score is extremely high (99.98%), but all supporting evidence remains at the model-prediction-only level (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension (standard ARB class indication; no NL marketing authorisation on file) |
| Predicted New Indication | Prinzmetal Angina |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| NL Market Status | Not marketed (CBG-MEB: 0 authorisations) |
| Number of Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Telmisartan is an AT1 receptor blocker (ARB) that also acts as a partial agonist of peroxisome proliferator-activated receptor gamma (PPAR-γ) — a dual mechanism that distinguishes it from other ARBs and has led to its informal designation as a "metabosartan." By blocking AT1R, Telmisartan reduces angiotensin II–mediated vasoconstriction; its PPAR-γ agonism may additionally enhance coronary endothelial function and reduce vascular oxidative stress.

Prinzmetal (variant) angina arises from transient reversible coronary artery spasm rather than fixed atherosclerotic obstruction. In this context, AT1R blockade could theoretically attenuate endothelin-1 release and reactive oxygen species that sensitise coronary smooth muscle to vasospasm, while PPAR-γ activation may upregulate endothelial nitric oxide synthase (eNOS) expression, improving coronary vasomotor tone. These mechanistic steps are biologically coherent but remain highly indirect: established first-line agents for Prinzmetal angina (calcium channel blockers, long-acting nitrates) act directly on vascular smooth muscle, whereas Telmisartan's pathway operates several steps upstream.

At present, no in vitro, in vivo, or clinical studies specifically test Telmisartan in coronary vasospasm. The high TxGNN score most likely reflects shared cardiovascular graph nodes (e.g., vascular tone, AT1R signalling) in the knowledge graph rather than a curated mechanistic pathway. This indication is therefore best treated as a model-generated hypothesis pending experimental validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Telmisartan in Prinzmetal angina.

---

## Literature Evidence

Currently no related literature available for Telmisartan in Prinzmetal angina.

---

## Netherlands Market Information

Telmisartan currently holds **no marketing authorisations** registered with the CBG-MEB in this dataset. No RVG numbers, product names, or approved indications are on file.

> **Note for practitioners:** Telmisartan is known internationally under brand names such as *Micardis* (Boehringer Ingelheim) and is widely authorised in other jurisdictions (EMA, FDA). The absence of entries in this dataset may reflect a data pipeline gap rather than a true regulatory absence. Please consult the CBG-MEB public register and the EMA Product database directly to confirm the current authorisation status in the Netherlands before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for comprehensive safety information.

> As a general reference pending SmPC retrieval (Data Gap DG001), the following ARB class-effect cautions are widely documented:
> - **Renal risk:** Acute kidney injury risk in patients with bilateral renal artery stenosis or solitary functioning kidney — AT1R blockade removes the efferent arteriolar tone that sustains GFR in these settings.
> - **Hyperkalaemia:** Particularly when combined with ACE inhibitors, potassium-sparing diuretics, or in patients with renal impairment.
> - **First-dose hypotension:** Especially in volume-depleted or sodium-depleted patients.
> - **Pregnancy contraindication:** ARBs are contraindicated in the second and third trimester (fetotoxicity).
>
> These are general class considerations and must be verified against the current Telmisartan SmPC before any clinical or research use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns an exceptionally high prediction score (99.98%), indicating strong knowledge-graph connectivity between Telmisartan and Prinzmetal angina. However, there is currently zero empirical evidence — no clinical trials, no animal models, and no observational data — specifically testing Telmisartan in coronary vasospasm. The mechanistic pathway is theoretically plausible but indirect, and effective first-line treatments for Prinzmetal angina are already approved and available. Proceeding without any experimental basis would carry unacceptable uncertainty.

**To proceed, the following is needed:**

- **Preclinical validation:** In vitro coronary smooth muscle relaxation assays and/or animal coronary vasospasm models to establish direct mechanistic evidence for AT1R blockade in this specific disease context.
- **Mechanism of action retrieval:** Resolve Data Gap DG002 (query DrugBank API for full MOA) to enable a more rigorous mechanistic analysis.
- **Safety profile review:** Resolve Data Gap DG001 (retrieve and parse SmPC/PIL from the EMA/CBG-MEB register) to complete the S1 safety screening gate before any feasibility study design.
- **Class-level evidence survey:** Conduct a systematic review of ARBs or renin-angiotensin system (RAS) agents in coronary vasospasm to determine whether any class-level signal exists that could support translational plausibility.
- **Clinical differentiation assessment:** Evaluate whether Telmisartan could offer a meaningful clinical advantage over existing therapies (calcium channel blockers, nitrates) before committing resources to a prospective study.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

