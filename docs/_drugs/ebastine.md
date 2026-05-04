---
layout: default
title: Ebastine
parent: 僅模型預測 (L5)
nav_order: 56
evidence_level: L5
indication_count: 2
---

# Ebastine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

The skill is about pipeline operations (training, deployment) — not applicable to report generation. Proceeding directly with the evaluation report per the system prompt specifications.

---

# Ebastine: From Allergic Rhinitis to Coronary Artery Disease

## One-Sentence Summary

Ebastine is a second-generation H1 receptor antagonist classically used for allergic rhinitis and chronic urticaria.
The TxGNN model predicts it may be effective for **Coronary Artery Disease**, with **0 clinical trials** and **1 computational publication** currently available to support this direction.
Evidence remains entirely at the exploratory modelling stage, and the mechanistic direction of effect has not been confirmed experimentally.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic rhinitis / Urticaria (second-generation H1 antihistamine) |
| Predicted New Indication | Coronary Artery Disease |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L5 |
| NL Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Ebastine is not available in this Evidence Pack. Based on established pharmacological knowledge, Ebastine is a selective, long-acting H1 receptor antagonist with demonstrated anti-allergic and anti-inflammatory properties. As with other second-generation antihistamines, it does not readily cross the blood-brain barrier, giving it a favourable central nervous system safety profile. Beyond H1 blockade, Ebastine is a known substrate of CYP2J2 — a cytochrome P450 isoform highly expressed in cardiac myocytes — and this enzyme relationship appears to be the primary mechanistic hook for TxGNN's cardiovascular prediction.

CYP2J2 catalyses the epoxidation of arachidonic acid into epoxyeicosatrienoic acids (EETs), which are endogenous lipid mediators with established cardioprotective properties: they reduce myocardial inflammation, promote vasodilation, and can attenuate ischaemia-reperfusion injury through ischaemic preconditioning pathways. TxGNN likely inferred a potential cardiovascular link by recognising Ebastine as a CYP2J2 ligand and connecting this enzyme to EET-mediated cardiac protection. Both coronary artery disease and myocardial ischaemia (the second-ranked predicted indication) are known to be influenced by EET biology.

However, this mechanistic rationale carries significant caveats. Ebastine acting as a CYP2J2 *substrate* could competitively inhibit EET production rather than enhance it — meaning the net cardiac effect could be neutral or even detrimental. No in vitro, animal-model, or clinical data currently links Ebastine to any cardiovascular outcome. The sole supporting publication is a 2008 in silico docking study that does not evaluate Ebastine therapeutically. Until the direction and magnitude of Ebastine's interaction with the CYP2J2–EET axis are established experimentally, this prediction must be treated as hypothesis-generating only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18004755](https://pubmed.ncbi.nlm.nih.gov/18004755/) | 2008 | In silico / Computational modelling | *Proteins* | Homology modelling and flexible molecular docking of human CYP2J2. The study notes that CYP2J2-generated EETs are associated with coronary artery disease, hypertension, and carcinogenesis. Ebastine is identified as a ligand that binds the CYP2J2 active site, but no therapeutic conclusions are drawn. |

---

## Netherlands Market Information

Ebastine is **not currently authorised for marketing in the Netherlands**. No CBG-MEB (College ter Beoordeling van Geneesmiddelen) registered products were identified. There is no SmPC or PIL available through the Dutch national register. Should clinical development advance, a market authorisation application via CBG-MEB or the EMA centralised procedure would be required before Ebastine could be prescribed in the Netherlands.

---

## Safety Considerations

Please refer to the SmPC (Samenvatting van de Productkenmerken) for safety information. As Ebastine is not currently registered in the Netherlands, clinicians should consult the authorised product information from jurisdictions where Ebastine is approved (e.g., EU member states with existing authorisations) as a preliminary reference until a Dutch SmPC is available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score of 99.18%, the supporting evidence consists of a single in silico modelling study from 2008 with no experimental or clinical data. The proposed CYP2J2–EET mechanistic pathway is biologically plausible but entirely unvalidated for Ebastine, and the direction of effect (cardioprotective vs. inhibitory) remains undetermined. Ebastine is also unregistered in the Netherlands, creating an additional regulatory barrier before any clinical application.

**To proceed, the following is needed:**

- **Mechanistic clarification**: In vitro studies measuring the effect of Ebastine on CYP2J2 enzymatic activity and EET metabolite production (competitive inhibition vs. induction)
- **Preclinical validation**: Animal model data evaluating cardiovascular outcomes (e.g., infarct size, endothelial function) in the presence of Ebastine
- **Safety profile review**: Retrieval and analysis of the full SmPC from authorised markets — including key warnings, contraindications, QTc prolongation data, and drug–drug interaction profile — before any human study is designed
- **Regulatory pathway assessment**: Consultation with CBG-MEB regarding options for clinical development or compassionate use in the Netherlands
- **Phase 1/2 clinical trial design**: At minimum, a proof-of-concept trial targeting mechanistic endpoints (e.g., plasma EET levels, coronary endothelial function markers) before therapeutic efficacy can be evaluated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

