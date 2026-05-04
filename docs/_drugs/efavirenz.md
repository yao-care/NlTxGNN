---
layout: default
title: Efavirenz
parent: 僅模型預測 (L5)
nav_order: 57
evidence_level: L5
indication_count: 3
---

# Efavirenz
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

基於 Evidence Pack 資料，我將依照格式規範產生完整報告。

---

# Efavirenz: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Efavirenz is a non-nucleoside reverse transcriptase inhibitor (NNRTI), clinically established as a first-line antiretroviral agent for HIV-1 infection in humans.
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection** with a prediction score of **99.80%**,
however there are currently **0 clinical trials** and **0 publications** specifically supporting this direction — the prediction rests entirely on mechanistic and graph-based inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (globally established; no Netherlands marketing authorization on file) |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 — model prediction only, no actual studies |
| NL Market Status | Not registered (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Efavirenz is a selective NNRTI that binds directly to and inhibits HIV-1 reverse transcriptase — an enzyme the virus requires to convert its RNA genome into DNA for integration into the host cell. This mechanism is entirely virus-specific: Efavirenz does not inhibit human DNA polymerases.

The biological link to SIV infection is structurally compelling. Simian Immunodeficiency Virus is a lentivirus that shares significant genomic and enzymatic homology with HIV-1; both viruses depend on reverse transcriptase for replication, and the active sites of their respective polymerases are structurally conserved. The TxGNN knowledge graph likely captures this phylogenetic and enzymatic relationship when generating a high-confidence prediction score.

That said, species-specific differences in reverse transcriptase conformation mean that NNRTIs optimised against HIV-1 RT do not automatically retain potency against SIV RT. Non-human primate SIV models are widely used in HIV vaccine and antiviral research, so any potential utility would be in preclinical/translational science rather than direct clinical application to patients.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Efavirenz in simian immunodeficiency virus infection.

---

## Literature Evidence

Currently no related literature available for Efavirenz in simian immunodeficiency virus infection.

---

## Netherlands Market Information

Efavirenz currently holds **no marketing authorisation** in the Netherlands. There are no CBG-MEB (College ter Beoordeling van Geneesmiddelen) registered products on file. Physicians seeking to use Efavirenz in the Netherlands would need to access it via a named-patient or compassionate-use pathway, or as part of an EMA-authorised combination product (e.g., Atripla, which contains efavirenz/emtricitabine/tenofovir disoproxil fumarate and holds EMA centralised authorisation, but is not within the scope of this repurposing review).

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information. No key warnings, contraindications, or drug interaction data were available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a near-maximum confidence score to this repurposing candidate based on the mechanistic overlap between HIV-1 and SIV reverse transcriptases; however, there is currently **no supporting clinical trial or published literature evidence** for Efavirenz in SIV infection, placing this firmly at evidence level L5. Furthermore, SIV infection is a non-human primate disease — any translational application would be in preclinical research settings, not direct patient care within the Dutch healthcare system. The absence of a Netherlands (or EMA) marketing authorisation for Efavirenz as a standalone product further complicates a regulatory pathway.

**To proceed, the following is needed:**

- **MOA data gap resolution**: Retrieve full Efavirenz SmPC / DrugBank entry to document NNRTI mechanism and known RT inhibition spectrum, including comparative activity against SIV RT
- **Preclinical evidence search**: Conduct a systematic search of in vitro / primate model literature for Efavirenz activity against SIV strains (this Evidence Pack returned zero results, but targeted biochemical literature may exist)
- **Regulatory clarification**: Determine whether the intended use context is (a) a veterinary/primate model research tool or (b) a human clinical application — the regulatory pathway differs substantially
- **Safety documentation**: Obtain full SmPC warnings and contraindications to complete the S1 safety screening step (currently blocked by Data Gap DG001)
- **Re-evaluate rank 2 indication**: The Evidence Pack's second-ranked prediction (feline acquired immunodeficiency syndrome, same score of 99.80%) has one supporting biochemical study (PMID [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/)) comparing NNRTI activity against FIV and HIV-1 reverse transcriptases — this may represent a more actionable evidence thread for further review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

