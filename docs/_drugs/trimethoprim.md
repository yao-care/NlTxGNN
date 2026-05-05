---
layout: default
title: Trimethoprim
parent: 僅模型預測 (L5)
nav_order: 121
evidence_level: L5
indication_count: 2
---

# Trimethoprim
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

Using the `txgnn-pipeline` skill to confirm Netherlands deployment context. Now generating the report following the Drug Repurposing Evaluation Report Prompt (v5).

---

# Trimethoprim: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Trimethoprim is a dihydrofolate reductase (DHFR) inhibitor classically used to treat bacterial infections, including urinary tract and respiratory infections.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis (PEK)**, with a prediction score of 99.57%.
However, **no clinical trials and no published literature** currently support this specific application — the prediction rests entirely on model inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available per NL records (generally: bacterial infections incl. UTI) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| NL Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, Trimethoprim is a selective inhibitor of bacterial dihydrofolate reductase (DHFR), blocking the folate synthesis pathway essential for bacterial DNA replication. It is active against gram-positive organisms (particularly *Staphylococcus aureus* and *Streptococcus pneumoniae*) and selected gram-negative species such as *Haemophilus influenzae* — all of which are common causative agents of ocular surface infections. When combined with Polymyxin B (as in the marketed ophthalmic product Polytrim, approved in the USA), the formulation covers the principal pathogens of bacterial conjunctivitis.

Punctate epithelial keratoconjunctivitis (PEK) is a distinct clinical entity, predominantly of viral (adenoviral) aetiology, presenting as diffuse punctate lesions on the corneal epithelium and conjunctiva. The high TxGNN score (99.57%, rank 933) most plausibly reflects **disease-graph proximity** between PEK and bacterial conjunctivitis rather than a direct pharmacological link: within the knowledge graph, both conditions share the ocular surface as a disease locus, and bacterial conjunctivitis has well-documented clinical evidence for trimethoprim-containing ophthalmic preparations.

Critically, however, there is no established mechanism by which Trimethoprim would address the primary adenoviral driver of PEK, nor any preclinical data suggesting anti-inflammatory or antiviral activity relevant to this condition. The prediction should be treated as hypothesis-generating until mechanistic or empirical evidence emerges.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for punctate epithelial keratoconjunctivitis.

---

## Literature Evidence

Currently no related literature available for punctate epithelial keratoconjunctivitis.

---

## Netherlands Market Information

No marketing authorizations (RVG numbers) for Trimethoprim are recorded in this dataset for the Netherlands.

> **Note for reviewers:** Trimethoprim and co-trimoxazole (trimethoprim/sulfamethoxazole) formulations are in clinical use across Europe, including ophthalmic preparations (e.g., Polytrim eye drops). The absence of records here likely reflects a data gap in the current Evidence Pack rather than an actual absence of Dutch registrations. CBG-MEB records should be consulted directly to confirm current authorization status before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics / Samenvatting van de Productkenmerken) for complete safety information, including warnings, contraindications, and drug interactions. No safety data is available in the current Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score, the evidence base for Trimethoprim in punctate epithelial keratoconjunctivitis is entirely absent (Evidence Level L5 — model prediction only). PEK's predominantly viral aetiology does not align with Trimethoprim's antibacterial mechanism of action, and the high score is best interpreted as an artifact of disease-graph proximity to bacterial conjunctivitis rather than a clinically actionable signal.

**To proceed, the following is needed:**

- **Mechanistic validation**: Clarify whether Trimethoprim (or host DHFR inhibition) has any relevance to adenoviral PEK pathophysiology, or whether the prediction could instead support use in PEK with confirmed bacterial superinfection
- **Preclinical data**: In vitro or animal model studies specifically addressing trimethoprim activity in PEK
- **Disease stratification**: Assess whether a subgroup of PEK with documented bacterial secondary infection might represent a more tractable indication for trimethoprim-based ophthalmic therapy
- **NL regulatory verification**: Confirm current CBG-MEB authorization status for Trimethoprim and related ophthalmic formulations via direct registry query
- **SmPC review**: Obtain the full SmPC to complete the safety profile, particularly regarding ophthalmic use and known contraindications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

