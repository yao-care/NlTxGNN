---
layout: default
title: Temozolomide
parent: 僅模型預測 (L5)
nav_order: 118
evidence_level: L5
indication_count: 2
---

# Temozolomide
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

Using the `txgnn-pipeline` skill to confirm context: this is an NlTxGNN report for the Netherlands deployment. Now generating the evaluation report from the Evidence Pack.

---

# Temozolomide: From Malignant Glioma to Adult Astrocytic Tumour

## One-Sentence Summary

Temozolomide is an oral alkylating chemotherapy agent, internationally recognised as the standard of care for malignant gliomas including glioblastoma multiforme (GBM) and anaplastic astrocytoma, though it is currently not registered with the CBG-MEB in the Netherlands.
The TxGNN model predicts it may be effective for **Adult Astrocytic Tumour**,
with **2 clinical trials** and **20 publications** currently supporting this direction — including multiple landmark Phase 3 RCTs that established TMZ-based chemoradiotherapy as the global backbone of brain tumour treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glioblastoma multiforme / malignant astrocytoma (internationally approved; not registered with CBG-MEB) |
| Predicted New Indication | Adult Astrocytic Tumour |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L1 |
| NL Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Temozolomide is an imidazotetrazine-class alkylating agent that undergoes spontaneous hydrolysis at physiological pH to form its active metabolite MTIC (monomethyl triazenoimidazole carboxamide). MTIC methylates DNA at the O6-position of guanine, generating lesions that overwhelm the mismatch repair pathway and ultimately trigger apoptosis. Crucially, temozolomide achieves near-complete oral bioavailability (~100%) and penetrates the blood–brain barrier effectively — a pharmacokinetic profile that makes it uniquely suited for central nervous system malignancies where systemic agents commonly fail.

Adult astrocytic tumours — encompassing glioblastoma multiforme (WHO Grade IV), anaplastic astrocytoma (Grade III), and diffuse astrocytoma (Grade II) — are among the most proliferative primary brain tumours in adults. In tumours where the MGMT (O6-methylguanine-DNA methyltransferase) gene promoter is methylated, MGMT protein expression is suppressed, meaning the O6-guanine lesions induced by temozolomide cannot be efficiently repaired. This MGMT methylation status has become the definitive predictive biomarker for TMZ response, explaining its selective but substantial efficacy across this tumour class and enabling biomarker-driven patient selection.

The TxGNN prediction is therefore not only mechanistically well-grounded — it is directly corroborated by one of the most robust clinical evidence bases in neuro-oncology. The landmark EORTC-NCIC Phase 3 trial (Stupp et al., 2005) established concomitant and adjuvant temozolomide with radiotherapy as the international standard of care for newly diagnosed GBM, with the 5-year follow-up confirming durable OS benefit. Subsequent Phase 3 studies have validated TMZ across multiple astrocytic tumour subtypes and patient populations, including elderly patients (NOA-08 trial) and MGMT-methylated GBM receiving intensified lomustine-TMZ combinations (CeTeG/NOA-09). The current absence of a CBG-MEB registration — rather than any lack of clinical evidence — is the primary barrier to formal use within the Netherlands healthcare system.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Phase 3 | Completed | 500 | Randomised comparison of temozolomide monotherapy vs. PCV (procarbazine + lomustine + vincristine) in recurrent WHO Grade III–IV astrocytic tumours; largest head-to-head RCT in this population providing direct comparative efficacy data for TMZ |
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Phase 1 | Completed | 26 | Dose-finding study of XL184 (cabozantinib, a VEGFR2/MET/RET inhibitor) added to TMZ and radiotherapy in newly diagnosed glioblastoma; TMZ + RT served as the backbone regimen and safety and pharmacokinetic profiles were characterised for the combination |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | Phase 3 RCT | N Engl J Med | Landmark Stupp trial: RT + concomitant/adjuvant TMZ vs. RT alone in newly diagnosed GBM; established TMZ + RT as global standard of care with significantly improved median OS |
| [19269895](https://pubmed.ncbi.nlm.nih.gov/19269895/) | 2009 | Phase 3 RCT (5-yr follow-up) | Lancet Oncol | EORTC-NCIC 5-year data confirmed durable OS benefit of TMZ + RT; MGMT promoter methylation confirmed as the key predictive biomarker for response |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | Phase 3 RCT | Lancet Oncol | NOA-08 trial: dose-dense TMZ monotherapy non-inferior to RT alone in elderly patients with malignant astrocytoma; supports TMZ as a frontline option when radiotherapy is not feasible |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | Phase 3 RCT | N Engl J Med | Addition of bevacizumab to standard TMZ + RT did not improve OS in newly diagnosed GBM; reaffirmed TMZ + RT as unchanged standard of care |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | Phase 3 RCT | JAMA | EF-14 trial: Tumour Treating Fields (TTFields) + TMZ vs. TMZ alone during GBM maintenance; TTFields addition further improved OS with TMZ as the indispensable backbone |
| [25920709](https://pubmed.ncbi.nlm.nih.gov/25920709/) | 2015 | Phase 3 RCT / Cohort | J Neuro-Oncol | Anaplastic astrocytoma and anaplastic oligo-astrocytoma cohort treated with RT + TMZ; supports extension of TMZ efficacy beyond GBM to Grade III astrocytic tumours |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | Phase 3 RCT | Lancet | CeTeG/NOA-09: Lomustine + TMZ combination superior to TMZ monotherapy in MGMT-methylated newly diagnosed GBM; highlights MGMT-stratified intensified treatment as emerging standard |
| [36809318](https://pubmed.ncbi.nlm.nih.gov/36809318/) | 2023 | Review | JAMA | Comprehensive review of primary malignant brain tumours in adults; TMZ-based chemoradiotherapy confirmed as current standard; summarises evolving therapeutic landscape |
| [40779733](https://pubmed.ncbi.nlm.nih.gov/40779733/) | 2025 | Phase 3 RCT | J Clin Oncol | NRG BN007: Dual immune checkpoint blockade (ipilimumab + nivolumab) vs. TMZ in MGMT-unmethylated newly diagnosed GBM; TMZ used as active comparator arm underscoring its continued reference standard status |
| [10914698](https://pubmed.ncbi.nlm.nih.gov/10914698/) | 2000 | Early Clinical / Review | Clin Cancer Res | Foundational paper characterising TMZ's mechanism, oral pharmacokinetics, and early clinical efficacy in malignant glioma; established the pharmacological rationale for its development as the primary CNS alkylating agent |

---

## Netherlands Market Information

Temozolomide is currently **not registered** with the CBG-MEB (College ter Beoordeling van Geneesmiddelen). No RVG authorisation numbers are present in the current evidence pack.

> **Note for review:** Clinicians and pharmacists should verify whether temozolomide is accessible in the Netherlands via the EMA centrally authorised pathway, named-patient programmes, or hospital pharmacy compounding under Dutch pharmaceutical regulations. The absence of a CBG-MEB record in this evidence pack should be reconciled with EMA central authorisation databases before concluding the drug is unavailable.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — alkylating agent (imidazotetrazine / triazene class) |
| Myelosuppression Risk | Moderate to High — dose-limiting toxicities include lymphopenia (CD4+ T-cell depletion) and thrombocytopenia; *Pneumocystis jirovecii* pneumonia (PJP) prophylaxis is required during the concomitant chemoradiotherapy phase |
| Emetogenicity Classification | Moderate — prophylactic antiemetics (5-HT3 antagonist ± dexamethasone) are recommended prior to each oral dose |
| Monitoring Items | Complete blood count (CBC) including absolute lymphocyte count before each cycle; liver function tests (LFTs); renal function; MGMT promoter methylation status should be assessed before initiation for treatment planning |
| Handling Protection | Yes — temozolomide capsules must be handled according to cytotoxic drug guidelines; capsules should not be opened or crushed; PPE and closed-system handling are required for pharmacy preparation |

---

## Safety Considerations

Please refer to the SmPC (Samenvatting van de Productkenmerken) for full safety information, including key warnings, contraindications, and drug–drug interactions.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Temozolomide carries one of the strongest evidence bases in neuro-oncology, with multiple completed Phase 3 RCTs — including the definitive EORTC-NCIC Stupp trial — establishing TMZ + radiotherapy as the global standard of care for adult astrocytic tumours, particularly GBM. The L1 evidence level and high TxGNN prediction score (99.36%) fully support proceeding, provided that the identified regulatory and safety data gaps are addressed within the Dutch healthcare framework.

**To proceed, the following is needed:**

- **Regulatory verification:** Reconcile the CBG-MEB registration status with EMA centrally authorised product records for temozolomide (Temodal®); if an EMA authorisation exists, update the evidence pack accordingly and confirm SmPC accessibility for Dutch prescribers
- **Safety profiling:** Obtain the current Dutch SmPC to complete key warnings, contraindications, and drug–drug interaction assessment — currently absent from this evidence pack
- **Biomarker infrastructure:** Confirm availability of MGMT promoter methylation testing in Dutch neuropathology centres, as this biomarker is essential for guiding treatment decisions and patient selection
- **Reimbursement pathway:** If formal registration or expanded use is being pursued, engage with Zorginstituut Nederland (ZIN) to assess reimbursement eligibility under the GVS (Geneesmiddelenvergoedingssysteem)
- **Clinical governance:** Define patient eligibility criteria (performance status, age, MGMT status, tumour grade) consistent with current Dutch neuro-oncology society guidelines and align with multidisciplinary tumour board protocols
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

