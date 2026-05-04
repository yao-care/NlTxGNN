---
layout: default
title: Calcitriol
parent: 僅模型預測 (L5)
nav_order: 37
evidence_level: L5
indication_count: 7
---

# Calcitriol
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

# Calcitriol: From Hypoparathyroidism and Renal Osteodystrophy to Hereditary Hypophosphatemic Rickets

## One-Sentence Summary

Calcitriol (1,25-dihydroxyvitamin D3) is the biologically active form of vitamin D, globally recognized for treating calcium-phosphate metabolism disorders including hypoparathyroidism and renal osteodystrophy, though it currently holds no marketing authorization in the Netherlands.
The TxGNN model identifies 7 predicted repurposing candidates across this evidence pack; among these, **Hereditary Hypophosphatemic Rickets** carries the strongest actionable evidence, supported by **7 clinical trials** and **20 publications**.
This indication is graded at Evidence Level 2 with a **Proceed with Guardrails** recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not currently registered in the Netherlands; globally recognized for hypoparathyroidism, renal osteodystrophy, and vitamin D-dependent rickets |
| Predicted New Indication | Hereditary Hypophosphatemic Rickets |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L2 |
| NL Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Calcitriol is 1,25-dihydroxyvitamin D3, the hormonally active end-metabolite of vitamin D produced in the proximal renal tubule by the enzyme CYP27B1 (1α-hydroxylase). It acts through the vitamin D receptor (VDR), a nuclear receptor widely expressed in the intestine, kidney, bone, and parathyroid glands. Core pharmacological effects include stimulation of intestinal calcium and phosphate absorption, suppression of parathyroid hormone (PTH) secretion, and direct promotion of bone mineralisation. Although formal DrugBank mechanism-of-action data was not available in this evidence pack, calcitriol's pharmacology is extensively characterised in the scientific literature cited below.

In hereditary hypophosphatemic rickets — most commonly X-linked hypophosphatemia (XLH, caused by loss-of-function mutations in *PHEX*) — excess FGF23 production from bone simultaneously suppresses renal phosphate reabsorption and inhibits CYP27B1 activity. The result is a paradoxical state: hypophosphatemia combined with inappropriately low or normal calcitriol levels, despite the anticipated compensatory upregulation. This dual deficiency drives defective growth plate cartilage mineralisation and osteomalacia. Exogenous calcitriol supplementation directly bypasses FGF23-mediated 1α-hydroxylase suppression, restores intestinal phosphate and calcium uptake, reduces compensatory secondary hyperparathyroidism, and thereby improves skeletal mineralisation.

Calcitriol combined with neutral phosphate supplementation served as the standard of care for hereditary hypophosphatemic rickets for several decades, until the 2018 EMA approval of burosumab — an anti-FGF23 monoclonal antibody targeting the upstream pathophysiology. The TxGNN prediction at rank 7 is therefore mechanistically well-grounded and consistent with established clinical practice. Within the Dutch healthcare context, this represents a repositioning opportunity particularly for patients in whom burosumab is inaccessible, contraindicated, or for whom conventional therapy remains the preferred approach.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03748966](https://clinicaltrials.gov/study/NCT03748966) | Early Phase 1 | Active, Not Recruiting | 20 | Calcitriol monotherapy (without phosphate supplementation) in children and adults with XLH over 1 year with dose escalation; tests hypothesis that calcitriol alone improves serum phosphate levels and skeletal mineralisation without increasing nephrocalcinosis |
| [NCT03820518](https://clinicaltrials.gov/study/NCT03820518) | Phase 4 | Unknown | 100 | Head-to-head comparison of high-dose vs. low-dose calcitriol combined with neutral phosphate in children with XLH; aims to establish evidence-based weight-adjusted dosing guidelines |
| [NCT04846647](https://clinicaltrials.gov/study/NCT04846647) | N/A (Observational) | Completed | 260 | Prospective observational study characterising FGF23 hypersecretion in 260 hypophosphatemia patients; provides mechanistic evidence that FGF23 inhibits calcitriol synthesis, directly supporting the rationale for calcitriol supplementation |
| [NCT06046820](https://clinicaltrials.gov/study/NCT06046820) | Phase 3 | Active, Not Recruiting | 27 | Phase 3 RCT of INZ-701 (ENPP1 enzyme replacement therapy) in children with ENPP1 deficiency; provides treatment landscape context for FGF23-related phosphate disorders; calcitriol may function as an adjunct or comparator arm |
| [NCT06921720](https://clinicaltrials.gov/study/NCT06921720) | N/A | Not Yet Recruiting | 65 | Mechanistic study using ³¹P-MRS spectroscopy to measure ATP concentrations in phosphate diabetes (XLH); explores energy metabolism pathophysiology in hypophosphatemia relevant to calcitriol's therapeutic target |
| [NCT01526304](https://clinicaltrials.gov/study/NCT01526304) | N/A (Observational) | Unknown | 150 | Cross-sectional study of FGF23, Klotho, and sclerostin in kidney stone formers; indirectly explores the phosphate–vitamin D regulatory axis central to calcitriol's mechanism of action |
| [NCT00844740](https://clinicaltrials.gov/study/NCT00844740) | N/A | Withdrawn | 0 | Planned study of cinacalcet add-on to standard calcitriol + phosphate in familial hypophosphatemic rickets; withdrawn before enrollment — included for completeness; no evidential value |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [40295317](https://pubmed.ncbi.nlm.nih.gov/40295317/) | 2025 | Clinical Guideline Review | Calcified Tissue International | Comprehensive XLH diagnosis and therapy review: FGF23 excess reduces calcitriol synthesis; calcitriol + phosphate remains standard care in many clinical settings; monitoring recommendations included |
| [39181153](https://pubmed.ncbi.nlm.nih.gov/39181153/) | 2024 | Review | Lancet | Authoritative X-linked hypophosphataemia primer: PHEX mutation → FGF23 excess → decreased calcitriol synthesis → impaired intestinal phosphate absorption → defective bone mineralisation |
| [36446330](https://pubmed.ncbi.nlm.nih.gov/36446330/) | 2022 | Review | Hormone Research in Paediatrics | Historical and mechanistic review of rickets and vitamin D therapy; places calcitriol in the treatment hierarchy for hereditary hypophosphatemic rickets subtypes and outlines metabolic management |
| [38988138](https://pubmed.ncbi.nlm.nih.gov/38988138/) | 2024 | Cohort/Review | J Bone and Mineral Research | Clinical case series with narrative review of hypophosphatemic rickets and short stature; illustrates the biochemical profile (low phosphorus, elevated ALP, low/normal calcitriol) typical of XLH requiring active vitamin D intervention |
| [17117305](https://pubmed.ncbi.nlm.nih.gov/17117305/) | 2006 | Review | Arq Bras Endocrinol Metab | Pathophysiology review of hereditary hypophosphatemic conditions including XLH, ADHR, and ARHR; confirms inappropriately normal or low calcitriol as a shared feature across subtypes, requiring supplementation |
| [6252463](https://pubmed.ncbi.nlm.nih.gov/6252463/) | 1980 | Clinical Trial | New England Journal of Medicine | Landmark comparative trial in 11 children: phosphate alone vs. phosphate + ergocalciferol vs. phosphate + calcitriol; calcitriol combination was superior in enhancing intestinal phosphate absorption and reducing total phosphate requirements |
| [3839245](https://pubmed.ncbi.nlm.nih.gov/3839245/) | 1985 | Clinical Study | Journal of Clinical Investigation | High-dose calcitriol heals osteomalacia in XLH patients unresponsive to conventional vitamin D; demonstrates that the active metabolite — not precursor forms — is required to correct the mineralisation defect in XLH |
| [35226335](https://pubmed.ncbi.nlm.nih.gov/35226335/) | 2022 | Longitudinal Cohort | J Endocrinological Investigation | Growth trajectory from birth to adulthood in hereditary hypophosphatemic rickets; contextualises long-term treatment goals for calcitriol therapy, including disproportion in limb growth |
| [29292875](https://pubmed.ncbi.nlm.nih.gov/29292875/) | 2017 | Multicenter Cohort | Pediatric Endocrinology Reviews | Height data from 127 XLH patients across 49 centres before and after initiation of calcitriol + phosphate therapy; supports early treatment initiation to optimise adult height outcomes |
| [2492895](https://pubmed.ncbi.nlm.nih.gov/2492895/) | 1989 | Longitudinal Cohort | Calcified Tissue International | Bone mineral density measured at baseline and every 6 months in 17 children with familial hypophosphatemia on calcitriol + phosphate therapy; quantifies the skeletal mineralisation response to treatment |

---

## Netherlands Market Information

Calcitriol is **not currently registered** with the CBG-MEB (College ter Beoordeling van Geneesmiddelen) in the Netherlands. There are no active RVG authorisations on record. Prescribers wishing to use calcitriol for Dutch patients should consider the following regulatory pathways:

- **EU cross-border supply**: Calcitriol products (e.g., Rocaltrol®) hold national authorisations in other EU member states including Germany and France; supply under Article 3.17 of the Dutch Medicines Act (*Geneesmiddelenwet*) may be applicable
- **Compounding (magistrale bereiding)**: Available through licensed Dutch compounding pharmacies under CBG-MEB oversight; suitable for individualised dosing in paediatric patients
- **EMA centralised pathway**: No centrally authorised calcitriol product currently exists via EMA

The SmPC (Samenvatting van de Productkenmerken) from a relevant EU reference country should be consulted for authorised prescribing information until a Dutch authorisation is in place.

---

## Safety Considerations

Formal pharmacovigilance data (regulatory warnings, contraindications, and drug-drug interactions) were not available in this evidence pack. Please refer to the SmPC for complete safety information.

Based on established pharmacology, the following considerations are particularly relevant when using calcitriol for hereditary hypophosphatemic rickets:

- **Hypercalcaemia and hypercalciuria**: The most clinically significant adverse effects; calcitriol has a narrow therapeutic window. Regular monitoring of serum calcium and 24-hour urinary calcium is required, especially during dose titration and in growing children.
- **Nephrocalcinosis**: A well-documented long-term complication of calcitriol + phosphate therapy in XLH. Renal ultrasound surveillance at regular intervals is recommended throughout treatment.
- **Secondary and tertiary hyperparathyroidism**: Overtreatment or prolonged therapy can paradoxically drive PTH dysregulation. Serial PTH monitoring is essential.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Calcitriol's role in hereditary hypophosphatemic rickets is mechanistically well-established and supported by decades of clinical data, including a landmark NEJM trial, multiple cohort studies, and an ongoing Phase 4 dose-comparison trial. The TxGNN prediction is consistent with established clinical practice, and the evidence level of L2 justifies moving forward. However, calcitriol is not registered in the Netherlands, and the newer targeted therapy burosumab (anti-FGF23) is now EMA-approved for XLH — requiring careful clinical and health-economic positioning before deployment in the Dutch healthcare context.

**To proceed, the following is needed:**
- Obtain the SmPC from an EU reference country (Germany or France recommended) to confirm approved dosing, safety monitoring requirements, and contraindications
- Clarify the regulatory pathway with CBG-MEB: Article 3.17 import, compounding, or initiating a formal NL/EU registration procedure
- Review final results of NCT03820518 (Phase 4 high vs. low dose) when published to inform weight-based dosing decisions for paediatric patients
- Conduct a comparative health technology assessment (calcitriol + phosphate vs. burosumab) for the Dutch patient population with hereditary hypophosphatemic rickets, including cost-effectiveness and access equity considerations
- Establish a prospective safety monitoring protocol covering serum calcium, urinary calcium, PTH, renal function, and renal ultrasound prior to clinical deployment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

