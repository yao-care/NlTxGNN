---
layout: default
title: Meloxicam
parent: 僅模型預測 (L5)
nav_order: 92
evidence_level: L5
indication_count: 10
---

# Meloxicam
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

The `txgnn-pipeline` skill confirms this is standard NlTxGNN pipeline output requiring report generation — proceeding with the structured evaluation report per the system prompt format.

---

# Meloxicam: From Osteoarthritis to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Meloxicam is a selective COX-2 inhibitor (NSAID) widely used for pain and inflammation management in musculoskeletal conditions such as osteoarthritis and rheumatoid arthritis.
The TxGNN model predicts it may be relevant for **Acromesomelic Dysplasia, Hunter-Thompson Type**,
however, this prediction is currently supported by **0 clinical trials and 0 publications**, placing it at the lowest evidence tier (L5) with a **Hold** recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Netherlands (CBG-MEB) authorization data available |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| NL Market Status | Not Registered (0 authorizations found) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on well-established pharmacological knowledge, Meloxicam is a preferential COX-2 inhibitor of the oxicam class. It suppresses prostaglandin synthesis — particularly PGE₂ — by selectively inhibiting cyclooxygenase-2 (COX-2), thereby reducing inflammation, pain, and fever. Its clinical role is well established in inflammatory musculoskeletal conditions including osteoarthritis, rheumatoid arthritis, and ankylosing spondylitis. In the Netherlands, NSAIDs of this class are regulated under CBG-MEB oversight and prescribed according to the SmPC.

Acromesomelic Dysplasia, Hunter-Thompson Type (ACMSD) is a rare autosomal recessive skeletal dysplasia caused by loss-of-function mutations in the *GDF5* gene (encoding Cartilage-Derived Morphogenetic Protein-1, CDMP1). The disorder is characterised by severe shortening of the middle and distal limb segments, resulting from disrupted bone morphogenetic protein signalling during skeletal development. Crucially, **this is a structural genetic disorder with no established inflammatory or COX-pathway-driven pathomechanism**. There is no biological rationale for COX-2 inhibition to modify disease course.

The TxGNN model's high prediction score (99.92%) most likely reflects **network proximity** between Meloxicam and skeletal disease nodes within the knowledge graph — a recognised limitation of graph-based prediction models — rather than a genuine therapeutic relationship. This prediction should be treated as a computational artefact rather than a clinically actionable signal. For context, more mechanistically plausible repurposing candidates in this Evidence Pack include **spondyloarthropathy (rank 6)**, where NSAIDs are a first-line treatment, and **RF-positive polyarticular juvenile idiopathic arthritis (rank 8)**, where indirect NSAID safety literature exists (PMID: 25057265).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Netherlands Market Information

No CBG-MEB marketing authorizations were retrieved in the current dataset (0 records). Meloxicam is a widely marketed NSAID in Europe, and this result is likely a **data collection gap** rather than a true reflection of Dutch market availability. Independent verification via the CBG-MEB public register is strongly recommended before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for complete safety information, including warnings, contraindications, and drug interactions. Note that as an NSAID, Meloxicam carries class-level considerations (e.g., gastrointestinal, cardiovascular, and renal risks) that are relevant regardless of the indication being evaluated.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction — acromesomelic dysplasia, Hunter-Thompson type — is a genetic structural disorder with no known inflammatory or COX-2 pathway involvement. With zero clinical trials, zero supporting publications (L5 evidence), and a mechanistic mismatch, there is no basis to proceed further for this specific indication.

**To proceed, the following is needed:**

- **Verify NL market status** via the CBG-MEB public register (https://www.cbg-meb.nl/) — current data likely reflects a collection gap
- **Obtain the Meloxicam SmPC** to retrieve complete warnings, contraindications, and drug interaction data (currently all listed as data gaps)
- **Retrieve MOA data** from DrugBank (DB00814) to formally document the COX-2 selectivity profile for mechanistic analysis
- **Re-prioritise repurposing evaluation** towards higher-value candidates in this same Evidence Pack:
  - **Rank 6 — Spondyloarthropathy**: NSAIDs are first-line therapy; mechanistically sound; requires confirmatory search in broader literature databases
  - **Rank 8 — RF+ Polyarticular Juvenile Idiopathic Arthritis**: Indirect NSAID safety evidence exists ([PMID: 25057265](https://pubmed.ncbi.nlm.nih.gov/25057265/)); Meloxicam is approved for JIA in some markets (e.g., USA); NL approval status should be verified
- **Conduct targeted literature searches** for Meloxicam in SpA and JIA populations to establish whether sufficient evidence exists for an L3 or higher evidence designation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

