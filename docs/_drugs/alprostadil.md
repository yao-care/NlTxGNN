---
layout: default
title: Alprostadil
parent: 僅模型預測 (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
---

# Alprostadil
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

# Alprostadil: From Duct-Dependent Congenital Heart Disease to Aortic Malformation

## One-Sentence Summary

Alprostadil (prostaglandin E1) is a potent vasodilator used to maintain ductus arteriosus patency in neonates with duct-dependent congenital heart disease, as well as for peripheral arterial occlusive disease and erectile dysfunction. The TxGNN model predicts it may be effective for **Aortic Malformation**, with **2 clinical trials** and **20 publications** currently supporting this direction. Notably, the majority of TxGNN's top-10 predictions cluster around congenital heart defects, reinforcing the biological coherence of these predictions.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Duct-dependent congenital heart disease (maintaining ductus arteriosus patency), peripheral arterial occlusive disease, erectile dysfunction |
| Predicted New Indication | Aortic Malformation |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 — Observational studies and clinical case series |
| NL Market Status | Not marketed (no CBG-MEB authorizations identified in this evidence pack) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Alprostadil is the synthetic form of prostaglandin E1 (PGE1). It acts directly on EP receptors on the smooth muscle of the ductus arteriosus, preventing ductal constriction and maintaining patency. Additionally, PGE1 is a potent vasodilator that increases blood flow in the pulmonary and systemic circulations. Since the late 1970s, PGE1 infusion has been the cornerstone of initial medical management for neonates born with duct-dependent cardiac lesions, buying critical time before surgical intervention.

Aortic malformations — including interrupted aortic arch, aortic atresia, critical aortic stenosis, and coarctation of the aorta — are classic examples of duct-dependent systemic circulation lesions. In these conditions, the descending aorta receives its blood supply through a patent ductus arteriosus. Without PGE1 to maintain ductal patency, systemic perfusion collapses, leading to metabolic acidosis, organ failure, and death. The literature confirms that PGE1 introduction in the late 1970s "revolutionized the management of interrupted aortic arch" (Jonas, 2015).

The TxGNN prediction is therefore highly mechanistically coherent. In fact, the use of alprostadil for aortic malformations is already well-established clinical practice in neonatal cardiology worldwide, although it may not appear as a specifically labelled indication in all regulatory jurisdictions. This represents a case where TxGNN has independently rediscovered an established off-label use through knowledge graph analysis.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04054115](https://clinicaltrials.gov/study/NCT04054115) | Phase 1 | Terminated | 10 | Studied acute effects of alprostadil on cerebral and pulmonary blood flow after bidirectional cavopulmonary connection (Glenn procedure). Confirmed clinical interest in PGE1 haemodynamic effects in congenital heart disease. Limited conclusions due to early termination. |
| [NCT02042092](https://clinicaltrials.gov/study/NCT02042092) | N/A | Completed | 39 | Cross-sectional imaging comparison (CDUS vs MRA) in large vessel vasculitis involving the aorta. Not a drug treatment trial; relevance limited to overlapping patient population with aortic pathology. |

> **Note:** The limited number of registered clinical trials reflects the fact that PGE1 use in duct-dependent aortic malformations is already accepted standard of care rather than an experimental intervention, reducing the need for prospective trials.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26686446](https://pubmed.ncbi.nlm.nih.gov/26686446/) | 2015 | Review | Semin Thorac Cardiovasc Surg | PGE1 introduction in the late 1970s revolutionized management of interrupted aortic arch. Direct arch anastomosis with VSD closure is preferred. |
| [6763200](https://pubmed.ncbi.nlm.nih.gov/6763200/) | 1982 | Clinical series | Pharmacotherapy | Landmark evaluation of alprostadil in congenital heart disease. PGE1 dilates ductus, increases pulmonary blood flow, and improves systemic perfusion in aortic arch obstruction. |
| [16368373](https://pubmed.ncbi.nlm.nih.gov/16368373/) | 2006 | Retrospective | Ann Thorac Surg | Outcomes of closed transventricular aortic valvotomy for critical neonatal aortic stenosis. PGE1 used as preoperative stabilization. |
| [25647388](https://pubmed.ncbi.nlm.nih.gov/25647388/) | 2014 | Review | Cardiol Young | Preoperative management of critical aortic stenosis in neonates. PGE1 infusion is essential for haemodynamic stabilization before intervention. |
| [19080093](https://pubmed.ncbi.nlm.nih.gov/19080093/) | 2008 | Clinical study | Zhonghua Yi Xue Za Zhi | Alprostadil (Lipo-PGE1) and ulinastatin attenuate inflammatory response and lung injury after CPB in paediatric congenital heart disease. |
| [32184038](https://pubmed.ncbi.nlm.nih.gov/32184038/) | 2020 | Retrospective | Asian J Surg | Staged surgical repair for interrupted aortic arch. PGE1 used for preoperative ductal maintenance. |
| [7201134](https://pubmed.ncbi.nlm.nih.gov/7201134/) | 1982 | Case series | Pediatr Cardiol | PGE1 infusion in 7 infants with hypoplastic left ventricle and aortic atresia. Transient metabolic and circulatory improvement demonstrated. |
| [6537955](https://pubmed.ncbi.nlm.nih.gov/6537955/) | 1984 | Case series | J Am Coll Cardiol | Long-term PGE1 therapy (avg 39 days) in 17 neonates with congenital heart defects including aortic coarctation. |
| [30347623](https://pubmed.ncbi.nlm.nih.gov/30347623/) | 2019 | Retrospective | J Neonatal Perinatal Med | Enteral feeding strategies in duct-dependent congenital heart disease patients on PGE1 infusion. |
| [1926911](https://pubmed.ncbi.nlm.nih.gov/1926911/) | 1991 | Review | DICP Ann Pharmacother | PGE1 use prior to neonatal transport for suspected duct-dependent cardiac defects. Recommends early stabilization with PGE1. |

## Netherlands Market Information

No CBG-MEB marketing authorizations for alprostadil were identified in this evidence pack. However, alprostadil is available in many EU member states under various brand names (e.g., Prostin VR for neonatal use, Caverject for erectile dysfunction, Alprostadil Alfadex for peripheral arterial disease). A search of the CBG-MEB Geneesmiddeleninformatiebank and/or the EMA centralized register is recommended to confirm current Dutch market availability.

## Safety Considerations

> Please refer to the SmPC (Summary of Product Characteristics) for comprehensive safety information.

**Known safety profile from literature (for clinical context):**

Alprostadil (PGE1) has a well-characterized safety profile from decades of clinical use in neonatal cardiology. Commonly reported adverse effects include:
- **Apnoea** (10–12% of neonates; ventilatory support should be immediately available)
- **Fever, flushing, and bradycardia**
- **Hypertrophic pyloric stenosis** with prolonged use (>5 days)
- **Cortical bone proliferation** with prolonged use
- **Hypotension** (dose-dependent vasodilatory effect)

Detailed warnings, contraindications, and drug interaction data were not available in this evidence pack. The treating physician should consult the relevant SmPC before use.

## Additional Predicted Indications

The TxGNN model predicted multiple congenital heart defects for alprostadil. The table below summarizes all predictions for a comprehensive view:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|---------------------|-------------|----------------|----------------|
| 1 | Aortic malformation | 99.98% | L3 | Proceed with Guardrails |
| 2 | Congenital tricuspid stenosis | 99.94% | L4 | Proceed with Guardrails |
| 3 | Congenital valvular dysplasia | 99.93% | L5 | Hold |
| 4 | Straddling/overriding tricuspid valve | 99.93% | L5 | Research Question |
| 5 | Tricuspid valve agenesis | 99.93% | L4 | Proceed with Guardrails |
| 6 | Tricuspid valve prolapse | 99.92% | L5 | Hold |
| 7 | Anomaly of tricuspid subvalvular apparatus | 99.92% | L5 | Hold |
| 8 | DORV with AVSD, PS, heterotaxy | 99.91% | L5 | Research Question |
| 9 | Heart septal defect | 99.39% | L4 | Proceed with Guardrails |
| 10 | Endemic goiter | 99.34% | L5 | Hold |

> **Interpretation:** 9 of 10 predictions involve congenital heart defects, which is highly consistent with alprostadil's known pharmacology. Predictions ranked 1, 2, 5, and 9 have supporting literature. The endemic goiter prediction (rank 10) appears to be a false positive with no mechanistic basis.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Alprostadil's use in aortic malformations is already a well-established clinical practice in neonatal cardiology worldwide. The TxGNN prediction is mechanistically sound and supported by extensive clinical literature spanning over four decades. This represents a case of computational validation of existing off-label practice rather than a novel repurposing discovery. The lack of formal regulatory indication labelling for this specific use in the Netherlands presents an opportunity for label alignment with clinical reality.

**To proceed, the following is needed:**
- Confirm current CBG-MEB/EMA marketing authorization status for alprostadil in the Netherlands (neonatal formulation)
- Obtain the SmPC to complete the safety profile (key warnings, contraindications, drug interactions)
- Retrieve detailed mechanism of action data from DrugBank to complete the pharmacological dossier
- Conduct a systematic review of alprostadil use in aortic malformations to formally quantify efficacy and safety
- Engage with paediatric cardiologists in the Netherlands to document current clinical practice patterns and any unmet regulatory needs

---

*This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. Data cutoff: 2026-04-03.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

