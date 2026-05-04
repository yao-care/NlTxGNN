---
layout: default
title: Abacavir
parent: 僅模型預測 (L5)
nav_order: 11
evidence_level: L5
indication_count: 3
---

# Abacavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Abacavir: From HIV Treatment to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Abacavir is a nucleoside reverse transcriptase inhibitor (NRTI) widely used as part of combination antiretroviral therapy for HIV-1 infection. The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**, with **0 clinical trials** and **1 publication** currently available. However, all three top-ranked predictions involve either non-human animal diseases or rare genetic conditions with no mechanistic basis, rendering them **not clinically translatable** to human medicine.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (antiretroviral combination therapy) |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L4 — Preclinical / in vitro study only |
| NL Market Status | Not registered (no CBG-MEB licenses in dataset) |
| Number of Authorizations | 0 (Note: Abacavir is EMA-authorized as Ziagen®; absence likely reflects dataset scope) |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Abacavir is a nucleoside analogue reverse transcriptase inhibitor (NRTI) that, once intracellularly phosphorylated to its active metabolite carbovir triphosphate, competitively inhibits HIV-1 reverse transcriptase and terminates proviral DNA chain elongation. It is a cornerstone of modern HIV-1 combination antiretroviral therapy, typically co-formulated with lamivudine (as Kivexa®/Epzicom®) or with lamivudine and dolutegravir (as Triumeq®). Detailed mechanism of action data was not available in this evidence pack, but the NRTI class mechanism is well-established in the literature.

The TxGNN prediction linking Abacavir to SIV infection has a clear mechanistic rationale: SIV belongs to the same Lentivirus genus as HIV and shares the reverse transcriptase enzyme targeted by NRTIs. An in vitro study (PMID 15040537) has demonstrated that SIV strains exhibit susceptibility to multiple anti-HIV-1 compounds, including abacavir. From a purely molecular standpoint, the prediction is pharmacologically sound.

**Critical limitation:** SIV exclusively infects non-human primates and does not cause disease in humans. Therefore, despite the high TxGNN score and valid mechanistic basis, this prediction has **no direct clinical translation value** for human drug repurposing. The same applies to the second-ranked prediction (feline immunodeficiency syndrome, an exclusively feline disease) and the third-ranked prediction (a rare monogenic neurodevelopmental disorder with no known mechanistic link to NRTI activity). This case highlights a known limitation of knowledge graph-based models: high-scoring predictions may reflect genuine biological relationships that nonetheless lack human therapeutic relevance.

## Clinical Trial Evidence — Indication 1: SIV Infection

Currently no related clinical trials registered.

## Literature Evidence — Indication 1: SIV Infection

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro susceptibility study | Antiviral Therapy | Evaluated 16 approved antiretrovirals (including abacavir) against HIV-2, SIV (mac251, B670), and SHIV strains. Demonstrated that SIV strains are susceptible to multiple anti-HIV-1 NRTIs, providing preclinical rationale for post-exposure prophylaxis considerations in laboratory settings. |

## Clinical Trial Evidence — Indication 2: Feline Acquired Immunodeficiency Syndrome

> **Note:** All four clinical trials retrieved are human HIV-1 studies that were returned due to keyword matching on "Abacavir." None are relevant to feline immunodeficiency virus (FIV). They are listed below for completeness with relevance grades.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Dose-selection study for dolutegravir + ABC/3TC in ART-naïve HIV-1 patients. **Not relevant to FIV** (Grade C). |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | SINGLE trial: DTG + ABC/3TC vs Atripla in ART-naïve HIV-1 adults over 96 weeks. **Not relevant to FIV** (Grade C). |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | SPRING-2 trial: DTG vs raltegravir with dual NRTI backbone in ART-naïve HIV-1 adults. **Not relevant to FIV** (Grade C). |
| [NCT01499199](https://clinicaltrials.gov/study/NCT01499199) | Phase 3 | Completed | 13 | CNS and plasma pharmacokinetics of DTG + ABC/3TC in ART-naïve HIV-1 subjects. **Not relevant to FIV** (Grade C). |

## Literature Evidence — Indication 2: Feline Acquired Immunodeficiency Syndrome

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | Animal study (in vitro, feline model) | Antiviral Research | Investigated combined ZDV + 3TC + abacavir triple therapy against FIV replication in vitro. Demonstrated that NRTIs effective against HIV also inhibit FIV, supporting the domestic cat as an animal model for HIV drug research. Not applicable to human repurposing. |

## Clinical Trial & Literature Evidence — Indication 3: Neurodevelopmental Disorder with Ataxic Gait, Absent Speech, and Decreased Cortical White Matter

Currently no related clinical trials registered.

Currently no related literature available.

## Netherlands Market Information

No CBG-MEB marketing authorizations were found in the dataset for abacavir.

> **Note:** Abacavir is well-known to be authorized in the EU via centralized EMA procedure as **Ziagen®** (ViiV Healthcare) and is available in the Netherlands in multiple fixed-dose combinations (Kivexa®, Triumeq®). The absence in this dataset likely reflects the scope of the data source (Taiwan TFDA) rather than actual unavailability in the Netherlands. Prescribers should consult the [CBG-MEB Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/) for current Dutch authorization status.

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for comprehensive safety information.

> **Key known safety concern (not from evidence pack):** Abacavir carries a well-established risk of **hypersensitivity reaction (HSR)** associated with HLA-B*5701 allele. HLA-B*5701 screening is mandatory before initiating abacavir therapy per EMA and Dutch guidelines. This HSR can be fatal upon re-challenge and is a black box warning in most jurisdictions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three TxGNN-predicted indications for abacavir are unsuitable for human drug repurposing. The top two predictions (SIV infection and feline AIDS) involve pathogens that exclusively infect non-human species — while the mechanistic link is real (shared lentivirus reverse transcriptase targets), there is no clinical translation pathway to human medicine. The third prediction (a rare monogenic neurodevelopmental disorder) has no mechanistic basis, no supporting evidence, and represents a model artifact. This candidate should not proceed further in the repurposing pipeline.

**To proceed, the following would be needed:**
- Re-evaluation of TxGNN model output with a **human-disease-only filter** to exclude veterinary and non-human primate diseases from candidate ranking
- If abacavir is to be considered for repurposing, focus on emerging hypotheses with human relevance (e.g., NRTI effects on LINE-1 retrotransposon activity in age-related diseases, or NLRP3 inflammasome modulation), which were not captured in the current TxGNN predictions
- Completion of NL regulatory data by querying the CBG-MEB Geneesmiddeleninformatiebank
- Resolution of data gaps: MOA details from DrugBank API, and SmPC safety data (warnings, contraindications, interactions)

---

*This report was generated on 2026-04-03. Results are for research purposes only and do not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Please consult the SmPC (Samenvatting van de Productkenmerken) via the [CBG-MEB](https://www.cbg-meb.nl/) for authoritative prescribing information.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

