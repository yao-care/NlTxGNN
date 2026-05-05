---
layout: default
title: Everolimus
parent: 僅模型預測 (L5)
nav_order: 65
evidence_level: L5
indication_count: 10
---

# Everolimus
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

Using the `txgnn-pipeline` skill to guide report generation for the NlTxGNN project. Now generating the evaluation report from the Evidence Pack.

---

# Everolimus: From Advanced Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Everolimus is an mTOR (mechanistic target of rapamycin) inhibitor, established in oncology for its use in advanced renal cell carcinoma, hormone receptor-positive breast cancer, and pancreatic neuroendocrine tumours.
The TxGNN model predicts it may be effective for **liposarcoma**, with **1 Phase 2 clinical trial** and **4 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from NL registry data (CBG-MEB records empty in dataset) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| NL Market Status | Not registered (per dataset — see note below) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

> ⚠️ **Dataset Note:** This dataset records zero CBG-MEB authorisations for Everolimus. This likely reflects a data pipeline gap rather than the actual market situation. Everolimus (Afinitor®, Votubia®, Certican®) holds EMA centralised marketing authorisations and is expected to be commercially available in the Netherlands. Please verify the current status directly via the [CBG-MEB medicines register](https://www.geneesmiddeleninformatiebank.nl/) before acting on this field.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not included in this Evidence Pack (data gap DG002). Based on established pharmacological knowledge, Everolimus is a first-generation mTOR inhibitor (rapalog class) that acts by binding intracellularly to FKBP12, which then inhibits the mTORC1 complex. This blocks downstream translation of proteins controlling cell-cycle progression (notably S6K1 and 4E-BP1), arresting tumour cells in the G1 phase and suppressing angiogenesis via reduced HIF-1α/VEGF signalling. Its efficacy across multiple solid tumours — including renal cell carcinoma and breast cancer — has been clinically validated.

The biological rationale for liposarcoma is well-grounded. Dedifferentiated liposarcoma (DDL), the most clinically aggressive subtype, demonstrates frequent co-activation of the Akt/mTOR and MAPK pathways, as confirmed by immunohistochemical analysis of 99 DDL specimens (Ishii et al., 2016, PMID 26518767). In vitro studies in the same report showed antitumour activity with mTOR inhibitors in DDL cell lines, directly implicating mTORC1 as a druggable target. This mechanistic overlap with Everolimus's established activity forms the core basis of the TxGNN prediction.

The current clinical strategy builds on this by pairing Everolimus with ribociclib — a CDK4/6 inhibitor — exploiting the fact that DDL is characterised by MDM2 and CDK4 amplification while leiomyosarcoma (LMS) is particularly mTOR-dependent. Multiple tumour models have demonstrated synergistic growth inhibition when CDK4/6 and mTOR pathways are co-targeted, which further strengthens the mechanistic plausibility of this repurposing prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, Not Recruiting | 48 | Two-centre, 2-arm study evaluating ribociclib + everolimus in advanced DDL (Arm A) and leiomyosarcoma (Arm B) following ≥1 prior systemic therapy; ribociclib 300 mg/day 3 weeks on/1 week off + everolimus 2.5 mg; primary endpoint is anti-tumour activity; completion expected December 2025 |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase 2 Trial Report | Clinical Cancer Research | Published results of NCT03114527 (SAR-096); ribociclib + everolimus in advanced DDL and LMS; CDK4/6 + mTOR co-targeting rationale; synergistic growth inhibition confirmed in multiple tumour models |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Translational Study | Tumour Biology | Akt/mTOR and MAPK pathway activation confirmed immunohistochemically in 99 DDL specimens; in vitro antitumour effect of mTOR inhibitor demonstrated in DDL cell lines — key mechanistic support for mTOR targeting in liposarcoma |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Frontiers in Oncology | Review of CDK inhibitor (palbociclib) combinations in sarcoma PDOX models; supports co-targeting of CDK and mTOR pathways as an effective strategy for liposarcoma and other soft-tissue sarcomas |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical Study | Anticancer Research | Broad-spectrum preclinical evaluation of eribulin in combination with mechanistically different anticancer agents across liposarcoma xenograft models; contextualises mTOR inhibitor combination rationale |

---

## Netherlands Market Information

No RVG numbers or CBG-MEB authorisations are recorded for Everolimus in the current dataset. This is likely a data pipeline issue. Clinicians and pharmacists should verify the current Dutch registration status directly:

- **CBG-MEB Medicines Register:** [https://www.geneesmiddeleninformatiebank.nl/](https://www.geneesmiddeleninformatiebank.nl/)
- **EMA EPAR (Afinitor — centrally authorised):** [https://www.ema.europa.eu/](https://www.ema.europa.eu/)

The SmPC (Samenvatting van de Productkenmerken) for the relevant authorised product should be consulted for full prescribing information.

---

## Cytotoxicity

Everolimus is an antineoplastic targeted therapy used in oncology. This section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — mTOR inhibitor (rapalog class); not a conventional cytotoxic |
| Myelosuppression Risk | Low to moderate — anaemia, thrombocytopenia and neutropenia are reported; less severe than conventional chemotherapy agents |
| Emetogenicity Classification | Low (oral mTOR inhibitors carry minimal to low emetogenic risk per MASCC/ASCO guidelines) |
| Monitoring Items | Full blood count (FBC/CBC), liver function tests (ALT, AST, bilirubin), renal function (creatinine, eGFR), fasting blood glucose, serum lipids (cholesterol/triglycerides), pulmonary function assessment (non-infectious pneumonitis is a class effect of mTOR inhibitors) |
| Handling Protection | Standard precautions for oral antineoplastic agents; follow local cytotoxic drug handling regulations (e.g., NIOSH guidelines or equivalent Dutch pharmacy standards) |

---

## Safety Considerations

Please refer to the SmPC (Samenvatting van de Productkenmerken) for complete safety information, including warnings, contraindications, and drug interactions.

> Drug interaction data was not found in the current Evidence Pack query (DDI query status: not found). A dedicated DDI review should be performed before clinical use, particularly given Everolimus's known CYP3A4/P-gp metabolism profile and narrow therapeutic index.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Everolimus has a mechanistically coherent and biologically well-supported basis for activity in liposarcoma — particularly dedifferentiated subtypes — through mTOR pathway dependence, with an active Phase 2 clinical trial (48 patients enrolled) and published trial data meeting L2 evidence threshold. However, the absence of CBG-MEB registry data, incomplete safety records, and an ongoing (not yet completed) Phase 2 trial require resolution before clinical adoption.

**To proceed, the following is needed:**

- **Regulatory verification:** Confirm current NL market authorisation status via the CBG-MEB medicines register; dataset currently shows zero authorisations, which contradicts known EMA approval status
- **SmPC review:** Retrieve and review the current EMA/CBG-MEB SmPC for Everolimus (Afinitor) to assess labelled warnings, contraindications, and special population restrictions (data gap DG001)
- **MOA data:** Complete DrugBank API query for detailed mechanism of action (data gap DG002)
- **DDI assessment:** Perform a full drug-drug interaction review — everolimus is a CYP3A4 and P-gp substrate with known clinically significant interactions
- **Trial completion data:** Await and review final results from NCT03114527 (Phase 2; completion expected December 2025; currently active, not recruiting)
- **Histological subtype specification:** Define eligible patient population by histological subtype (DDL vs LMS vs other), as efficacy signals in the trial are subtype-specific
- **Pharmacovigilance plan:** Develop a monitoring protocol specifically addressing non-infectious pneumonitis, stomatitis, and metabolic toxicities (hyperglycaemia, hyperlipidaemia) characteristic of mTOR inhibitor therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

