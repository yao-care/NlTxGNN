---
layout: default
title: Emtricitabine
parent: 僅模型預測 (L5)
nav_order: 58
evidence_level: L5
indication_count: 3
---

# Emtricitabine
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

The txgnn-pipeline skill is focused on pipeline operations; the detailed report format is governed by the system prompt (v5). Proceeding to generate the report from the Evidence Pack.

---

# Emtricitabine: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Emtricitabine (FTC) is a nucleoside reverse transcriptase inhibitor (NRTI) established for the treatment of HIV-1 and HIV-2 infection in humans.
The TxGNN model predicts it may also be effective against **Feline Acquired Immunodeficiency Syndrome** (caused by Feline Immunodeficiency Virus, FIV),
with **no directly relevant clinical trials** registered and **1 feline animal study** (2023) currently available to support this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV infection (established antiretroviral use; no CBG-MEB registration data captured in current database) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 (single feline animal study; no FIV-specific clinical trials) |
| NL Market Status | Not registered (per CBG-MEB database) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the regulatory database for this Evidence Pack. Based on established pharmacological knowledge, Emtricitabine is a fluorinated cytidine analogue. After intracellular phosphorylation to its active triphosphate form (FTC-TP), it competitively inhibits the RNA-dependent DNA polymerase (reverse transcriptase) of retroviruses and terminates nascent viral DNA chain elongation. This mechanism is the basis for its potent activity against HIV-1 and HIV-2 in humans.

Feline Immunodeficiency Virus (FIV) and HIV belong to the same family of lentiviruses (*Retroviridae*) and share a conserved, reverse transcriptase-dependent replication cycle. The mechanistic link is therefore structurally plausible: FTC-TP can compete with natural cytidine triphosphate for incorporation by FIV reverse transcriptase, causing chain termination through the same mechanism validated against HIV. Supporting this, the M184V resistance mutation — the hallmark of Emtricitabine resistance in HIV — has been shown to emerge under drug pressure in FIV-infected cats as well (PMID 37112803), confirming that the same molecular target is engaged in both species.

The key uncertainty is quantitative, not mechanistic. FIV reverse transcriptase differs from HIV-1 RT in amino acid sequence, which may reduce FTC-TP binding affinity and therefore require higher doses than those used in humans. The single available feline study used Emtricitabine at 40 mg/kg — substantially higher than the standard human dose of approximately 6 mg/kg — highlighting that species-specific pharmacokinetic and pharmacodynamic calibration will be essential before any clinical application.

---

## Clinical Trial Evidence

> **Important note:** No clinical trials specifically studying Emtricitabine for feline acquired immunodeficiency syndrome (FIV) are registered on ClinicalTrials.gov. The four trials listed below were retrieved through an Emtricitabine keyword search; all concern human HIV treatment (relevance grade C) and have no direct applicability to the FIV indication. They are included here for transparency.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Ritonavir-boosted Darunavir + Lamivudine vs Darunavir + Emtricitabine/Tenofovir in ART-naïve HIV-1 patients — human HIV trial; Emtricitabine is the background NRTI only, not the investigational drug; no FIV relevance |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Dolutegravir dose selection with Abacavir/Lamivudine or Tenofovir/Emtricitabine as background NRTI in ART-naïve HIV-1 adults — human HIV trial; no FIV relevance |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Dolutegravir + Abacavir/Lamivudine vs Efavirenz/Emtricitabine/Tenofovir over 96 weeks in ART-naïve HIV-1 adults — large non-inferiority trial; Emtricitabine is a comparator component only; no FIV relevance |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Dolutegravir vs Raltegravir, both with dual NRTI backbone (ABC/3TC or TDF/FTC), over 96 weeks in ART-naïve HIV-1 adults — head-to-head integrase inhibitor trial; no FIV relevance |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Animal Study (Feline) | *Viruses* | Evaluated pharmacokinetics and immunophenotypic outcomes of combination ART — Dolutegravir (2.5 mg/kg) + Tenofovir (20 mg/kg) + **Emtricitabine (40 mg/kg)** — in FIV-infected domestic cats. Provides the first direct proof-of-concept for Emtricitabine-containing cART in a feline lentiviral model; M184V resistance emergence was documented, confirming the same RT target engagement as in HIV |

---

## Netherlands Market Information

No products containing Emtricitabine are registered with the CBG-MEB (College ter Beoordeling van Geneesmiddelen) in the Netherlands according to the current database. This likely reflects a data capture gap rather than true absence from the Dutch market: Emtricitabine-containing products such as Emtriva (monotherapy), Truvada, Descovy, Biktarvy, and Symtuza hold EMA central marketing authorisations and are commercially available across EU member states including the Netherlands. Clinicians and pharmacists should verify the current authorisation status and applicable SmPC directly via the CBG-MEB product database at [https://www.cbg-meb.nl](https://www.cbg-meb.nl) or the EMA medicines portal.

---

## Safety Considerations

Please refer to the SmPC (Samenvatting van de Productkenmerken) for full safety information. No safety data — including key warnings, contraindications, or drug-drug interactions — was captured in the current Evidence Pack. Given that the predicted indication is a **veterinary application** (feline FIV), the human SmPC provides only a partial safety reference; species-specific toxicology data in cats would be required before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic plausibility of Emtricitabine against FIV is well-founded given the conserved lentiviral reverse transcriptase target, but the evidence base consists of a single 2023 feline pharmacokinetic study with no controlled efficacy endpoints, and all retrieved clinical trials concern human HIV with no applicability to feline AIDS. The TxGNN score of 99.92% reflects graph-topological proximity, not clinical validation.

**To proceed, the following is needed:**

- A randomised, placebo-controlled efficacy study in FIV-infected cats evaluating Emtricitabine alone or as part of combination ART (cART)
- Species-specific pharmacokinetic/pharmacodynamic (PK/PD) modelling to determine the optimal dose in cats (the 40 mg/kg used in the 2023 study is ~7× the human weight-adjusted dose and requires safety and tolerability confirmation)
- Feline-specific safety and tolerability data, including haematological and renal monitoring (NRTI-class renal and mitochondrial toxicity signals are relevant)
- Regulatory consultation on the authorisation pathway for veterinary use — likely via EMA's Committee for Medicinal Products for Veterinary Use (CVMP) or the Dutch medicines authority (Bureau Diergeneesmiddelen, BD)
- Retrieval of the full SmPC for Emtricitabine human products to perform cross-species safety extrapolation
- Clarification of CBG-MEB registration status, as Emtricitabine-based products are expected to be commercially available in the Netherlands via EMA central authorisation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

