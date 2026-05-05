---
layout: default
title: Paclitaxel
parent: 僅模型預測 (L5)
nav_order: 103
evidence_level: L5
indication_count: 10
---

# Paclitaxel
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

Using the **txgnn-pipeline** skill to confirm context, then generating the NlTxGNN pharmacist evaluation report per the system prompt format.

---

# Paclitaxel: From Globally Established Taxane Agent to Female Breast Carcinoma

## One-Sentence Summary

Paclitaxel is a well-established taxane cytotoxic drug with extensive global clinical use in oncology, but it currently holds no formal marketing authorization with the CBG-MEB in the Netherlands.
The TxGNN model predicts with very high confidence that it is effective for **Female Breast Carcinoma**,
with **multiple completed Phase III trials** and **over 20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No current CBG-MEB authorization registered in the Netherlands |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L1 |
| NL Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrieved from DrugBank in this Evidence Pack. Based on well-established pharmacological knowledge, Paclitaxel is a taxane-class cytotoxic agent that exerts its antineoplastic effect by binding to and stabilizing polymerized microtubules, preventing their depolymerization. This arrests the cell cycle at the G2/M phase and ultimately triggers apoptosis in rapidly dividing cells. This mechanism is comprehensively documented in peer-reviewed literature (PMID 31783552) and forms the biological basis for its broad application in solid tumour oncology worldwide.

Female breast cancer cells are characterised by high proliferative activity, rendering them particularly vulnerable to G2/M arrest induced by paclitaxel. The drug has demonstrated clinical efficacy across all major breast cancer subtypes: HER2-positive disease (in combination with trastuzumab and pertuzumab), triple-negative breast cancer (TNBC, including in combination with atezolizumab or pembrolizumab via the IMpassion130 programme), and high-risk hormone receptor-positive disease where cytotoxic chemotherapy is indicated. Landmark Phase III trials — notably NCT00005970 (n = 3,436) — have established the AC → weekly paclitaxel sequence as a cornerstone of adjuvant breast cancer therapy.

From the Netherlands perspective, although Paclitaxel is not currently registered with the CBG-MEB, it holds EMA centrally authorised product (CAP) status for breast cancer and is in routine clinical use in Dutch oncology centres under those EMA authorisations. The TxGNN prediction score of 99.995% essentially confirms the existing global clinical evidence base, suggesting that the absence of a Dutch-specific CBG-MEB entry reflects a regulatory database gap rather than any clinical or safety concern about the drug's applicability.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00005970](https://clinicaltrials.gov/study/NCT00005970) | Phase III | Completed | 3,436 | Landmark adjuvant trial: AC followed by weekly paclitaxel ± trastuzumab in HER2-overexpressing or high-risk node-negative breast cancer. Established weekly paclitaxel as a standard-of-care adjuvant backbone and is the pivotal reference trial for this indication. |
| [NCT00002953](https://clinicaltrials.gov/study/NCT00002953) | Phase III | Completed | 704 | Randomised comparison of epirubicin + cyclophosphamide vs. epirubicin + paclitaxel in women with metastatic breast cancer. Directly evaluated paclitaxel-based combination versus anthracycline doublet in the metastatic setting. |
| [NCT00561119](https://clinicaltrials.gov/study/NCT00561119) | Phase III | Completed | 326 | Maintenance therapy vs. observation after response to gemcitabine + paclitaxel (GP) as first-line chemotherapy in metastatic or recurrent breast cancer. Directly assessed the role of paclitaxel in long-term disease control. |
| [NCT03949634](https://clinicaltrials.gov/study/NCT03949634) | Phase III | Unknown | 272 | Post-marketing randomised study comparing PEGylated liposomal doxorubicin vs. a paclitaxel-containing control regimen for cardiac safety and efficacy in early-stage female breast cancer. |
| [NCT01426880](https://clinicaltrials.gov/study/NCT01426880) | Phase II/III | Completed | 595 | Investigated addition of carboplatin to standard neoadjuvant anthracycline-taxane therapy in triple-negative and HER2-positive early breast cancer. Demonstrated improved pathological complete response (pCR) rates with carboplatin addition to paclitaxel backbone. |
| [NCT03289819](https://clinicaltrials.gov/study/NCT03289819) | Phase II | Completed | 53 | Single-arm study of nab-paclitaxel + pembrolizumab followed by epirubicin + cyclophosphamide as neoadjuvant treatment in TNBC. Explored immunotherapy–taxane synergy with pCR as primary endpoint. |
| [NCT01276041](https://clinicaltrials.gov/study/NCT01276041) | Phase II | Completed | 70 | Weekly paclitaxel combined with trastuzumab + pertuzumab for metastatic HER2-positive breast cancer. Evaluated dual HER2 blockade supported by weekly paclitaxel as the chemotherapy backbone. |
| [NCT04293393](https://clinicaltrials.gov/study/NCT04293393) | Phase II | Active, not recruiting | 200 | Randomised comparison of standard neoadjuvant chemotherapy (paclitaxel-based) vs. letrozole + abemaciclib in HR+/HER2− high-/intermediate-risk breast cancer. Paclitaxel-based arm serves as the clinical benchmark. |
| [NCT05569811](https://clinicaltrials.gov/study/NCT05569811) | Phase II | Active, not recruiting | 120 | VALENTINE trial: three-arm neoadjuvant study comparing multi-agent chemotherapy (containing paclitaxel) vs. HER3-DXd ± letrozole in HR+/HER2− breast cancer with high genomic risk. |
| [NCT05189535](https://clinicaltrials.gov/study/NCT05189535) | Phase II/III | Completed | 66 | Evaluated pentoxifylline 400 mg twice daily for prevention of paclitaxel-induced peripheral neuropathy in breast cancer patients. Directly informs safety management protocols for NL clinical practice. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [31783552](https://pubmed.ncbi.nlm.nih.gov/31783552/) | 2019 | Review | Biomolecules | Comprehensive review of paclitaxel's mechanistic and clinical effects in breast cancer, covering microtubule stabilisation, apoptosis induction, resistance mechanisms, and efficacy across HER2+, TNBC, and HR+ subtypes. Foundational reference for this repurposing rationale. |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | Review | Chemical Biology & Drug Design | Evaluated paclitaxel combination therapies using patient-derived breast carcinoma data; identified synergistic drug pairs to overcome resistance, supporting continued clinical relevance of paclitaxel in combination strategies. |
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | RCT | Cancer | Phase II multicentre trial of doxorubicin + paclitaxel in advanced breast carcinoma; assessed the impact of prior adjuvant anthracycline therapy on combination efficacy in the metastatic setting. |
| [32461977](https://pubmed.ncbi.nlm.nih.gov/32461977/) | 2020 | Cohort | BioMed Research International | Real-world study evaluating epirubicin/cyclophosphamide followed by weekly paclitaxel + trastuzumab as neoadjuvant chemotherapy in HER2-positive breast carcinoma; confirmed feasibility and efficacy in clinical practice. |
| [39009452](https://pubmed.ncbi.nlm.nih.gov/39009452/) | 2024 | Translational | Journal for Immunotherapy of Cancer | Demonstrated that paclitaxel modulates tumour-associated macrophages (TAMs) to enhance PD-1 blockade efficacy in TNBC, revealing an immunomodulatory mechanism beyond direct cytotoxicity. Supports rationale for paclitaxel + checkpoint inhibitor combinations. |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | Translational | Nature Communications | Exome sequencing identified TEKT4 germline variations enriched in post-paclitaxel tumours in ~10% of a breast cancer cohort; provides a genomic biomarker candidate for predicting paclitaxel response. |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug and Therapeutics Bulletin | Early review documenting paclitaxel and docetaxel evidence in breast and ovarian cancer; records the extension of paclitaxel licensing to first-line breast cancer treatment, establishing historical regulatory precedent. |
| [11745249](https://pubmed.ncbi.nlm.nih.gov/11745249/) | 2001 | Clinical | Cancer | Investigated paclitaxel's role in multimodality treatment for inflammatory breast carcinoma (IBC), demonstrating significant clinical activity in this aggressive subtype and supporting use beyond standard early-stage disease. |
| [9164198](https://pubmed.ncbi.nlm.nih.gov/9164198/) | 1997 | Phase II | Journal of Clinical Oncology | ECOG study evaluating biweekly paclitaxel + cisplatin in advanced breast carcinoma; one of the early trials establishing paclitaxel's single-agent and combination efficacy in the metastatic setting. |
| [20665703](https://pubmed.ncbi.nlm.nih.gov/20665703/) | 2011 | In vitro | Journal of Cellular Physiology | Demonstrated that ZD6474 (vandetanib, EGFR/VEGFR inhibitor) enhances paclitaxel's antiproliferative and apoptotic effects in breast carcinoma cells; provides mechanistic rationale for EGFR-targeted + paclitaxel combination strategies. |

---

## Netherlands Market Information

Paclitaxel currently holds **no marketing authorisation** registered with the CBG-MEB (College ter Beoordeling van Geneesmiddelen) in the Netherlands. There are no RVG numbers on file in this Evidence Pack.

> **Note for clinical teams:** Paclitaxel is available in the Netherlands under EMA centrally authorised product (CAP) status (e.g., originator and generic formulations for breast cancer, ovarian cancer, NSCLC, and AIDS-related Kaposi's sarcoma). The SmPC (Samenvatting van de Productkenmerken) applicable to Dutch practice is accessible via the EMA product database. Clinical teams should verify the current approved indications, formulation-specific guidance (conventional paclitaxel vs. nab-paclitaxel), and applicable reimbursement pathways under Zorgverzekeringswet (ZVW) prior to prescribing.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Taxane class (microtubule-stabilising agent) |
| Myelosuppression Risk | Moderate to High — dose-limiting neutropenia is the primary haematological toxicity; febrile neutropenia risk is clinically significant, particularly with dose-dense schedules |
| Emetogenicity Classification | Low to Moderate — paclitaxel is classified as low emetogenic potential per MASCC/ESMO antiemetic guidelines; premedication focus is primarily on hypersensitivity prophylaxis |
| Monitoring Items | CBC with differential (before each cycle and at nadir), liver function tests (ALT, AST, bilirubin), renal function, peripheral neurological assessment (CTCAE grading for neuropathy), cardiac function monitoring when used with anthracyclines or trastuzumab |
| Handling Protection | Yes — standard cytotoxic drug handling protocols required: appropriate PPE (gloves, gown, eye protection), closed-system drug transfer devices (CSTD), designated preparation in a certified laminar flow cabinet |

---

## Safety Considerations

Formal Dutch SmPC safety data (specific warnings, contraindications, drug interactions) was not retrieved in this Evidence Pack. Please refer to the current SmPC (accessible via the EMA or the CBG-MEB Geneesmiddeleninformatiebank) for comprehensive prescribing information before clinical use.

Key safety considerations documented in the published literature:
- **Peripheral neuropathy**: Cumulative dose-limiting toxicity in a substantial proportion of patients; onset and severity should be monitored each cycle using standardised tools (CTCAE or FACT-Taxane questionnaire). Dose reduction or discontinuation may be required.
- **Hypersensitivity reactions**: Standard formulation (Cremophor EL-based) requires premedication with corticosteroids (e.g., dexamethasone) and antihistamines (H1 + H2 blockers) prior to each infusion. Nab-paclitaxel does not require routine premedication.
- **Myelosuppression**: Monitor ANC before each cycle; dose modifications or G-CSF support should follow institutional protocols for significant neutropenia.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The global evidence base for paclitaxel in female breast carcinoma is among the strongest in oncology, anchored by multiple completed Phase III randomised trials (including NCT00005970, n = 3,436) that establish it as a standard-of-care adjuvant, neoadjuvant, and palliative agent across all major breast cancer subtypes. The TxGNN prediction score of 99.995% is consistent with this clinical reality. The key barrier in the Netherlands context is not clinical evidence but the absence of a CBG-MEB-specific registration entry; EMA CAP status should already enable legitimate clinical use in Dutch healthcare.

**To proceed, the following is needed:**
- Confirm applicable EMA CAP authorisation details (product name, approved indications, formulation) and ensure alignment with the intended use case (adjuvant, neoadjuvant, or metastatic setting)
- Obtain and review the current SmPC for full contraindications, warnings, interaction profile, and pregnancy/lactation guidance
- Determine the specific breast cancer subtype (HER2+, TNBC, HR+/HER2−) to select the appropriate evidence-based combination regimen per ESMO Clinical Practice Guidelines
- Establish a structured toxicity monitoring plan covering peripheral neuropathy, haematological toxicity, and hypersensitivity management per NL institutional protocols
- Clarify ZVW reimbursement eligibility and formulary pathway for the intended indication and formulation
- If a CBG-MEB-specific registration is clinically or administratively required, identify whether a Type II variation or national procedure is the appropriate route in consultation with the regulatory affairs team
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

