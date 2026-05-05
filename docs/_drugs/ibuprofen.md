---
layout: default
title: Ibuprofen
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 7
---

# Ibuprofen
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

Using the `txgnn-pipeline` skill to guide this report generation. Now producing the evaluation report based on the Evidence Pack.

---

# Ibuprofen: From Analgesic/Anti-inflammatory to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ibuprofen is a well-established non-steroidal anti-inflammatory drug (NSAID), widely used for pain relief, fever reduction, and inflammatory conditions such as arthritis. The TxGNN model predicts it may be effective for **Acromesomelic Dysplasia, Hunter-Thompson Type** — a rare autosomal recessive skeletal dysplasia caused by GDF5/CDMP1 loss-of-function mutations — with **0 clinical trials** and **0 publications** currently supporting this direction. This prediction rests entirely on graph network topology and carries no supporting clinical or preclinical evidence at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from CBG-MEB registry (no NL authorizations found in dataset) |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| NL Market Status | Not registered (no CBG-MEB RVG authorizations found) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this evidence pack. Based on established pharmacological knowledge, Ibuprofen is a prototypical NSAID that inhibits both COX-1 and COX-2 cyclooxygenase enzymes, thereby suppressing prostaglandin synthesis. This results in analgesic, antipyretic, and anti-inflammatory effects. Its well-known clinical applications include musculoskeletal pain, dysmenorrhoea, fever, and inflammatory arthropathies.

Acromesomelic dysplasia, Hunter-Thompson type is an extremely rare congenital skeletal dysplasia caused by loss-of-function mutations in the GDF5 gene (also known as CDMP1). GDF5 is a bone morphogenetic protein (BMP) family member that plays a critical role in chondrocyte differentiation and long bone development. The theoretical mechanistic link is that PGE2 — a downstream COX-2 product — modulates BMP signalling in chondrocytes. In principle, COX-2 inhibition by Ibuprofen could alter PGE2-mediated BMP pathway activity in cartilage.

However, the mechanistic link is assessed as extremely weak and directionally uncertain. Suppressing COX-2/PGE2 could simultaneously reduce local inflammation and interfere with residual GDF5-dependent bone development signalling — opposing effects that make the net clinical outcome unpredictable. This is a congenital structural disorder caused by a genetic defect; it is not an acquired inflammatory condition. The high TxGNN score most likely reflects graph-topological proximity to other musculoskeletal diseases in which Ibuprofen has established activity, rather than a true mechanism-based repurposing opportunity. All 7 TxGNN-predicted indications for Ibuprofen in this dataset share this same pattern: rare skeletal or developmental dysplasias with L5 evidence and Hold recommendations.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Netherlands Market Information

No CBG-MEB RVG authorizations were found for Ibuprofen in the current dataset.

> **Important note**: This likely reflects a data collection gap in the regulatory pipeline rather than actual NL market absence. Ibuprofen is a widely authorised OTC and prescription medicine throughout the EU. Please verify current authorization and RVG status directly via the [CBG-MEB public register](https://www.cbg-meb.nl/) or the [EMA product database](https://www.ema.europa.eu/) before drawing any conclusions about NL market availability.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.74%), acromesomelic dysplasia, Hunter-Thompson type is a congenital skeletal dysplasia caused by a specific genetic defect in the GDF5/BMP pathway. The mechanistic connection to Ibuprofen's COX-2 inhibition mechanism is speculative, directionally ambiguous, and entirely unsupported by any clinical trial, observational data, or published literature (L5 — model prediction only). Proceeding without foundational evidence would not meet CBG-MEB or EMA repurposing standards.

**To proceed, the following is needed:**

- **Regulatory data verification**: Retrieve actual CBG-MEB RVG authorization records and SmPC for Ibuprofen to establish the NL regulatory baseline
- **MOA data from DrugBank**: Query DrugBank API (DB01050) to obtain the full mechanism of action and target interaction profile to formally assess the COX-2 / GDF5-BMP pathway hypothesis
- **Safety data**: Obtain complete SmPC warnings, contraindications, and drug-drug interaction data before any further evaluation stage
- **Preclinical evidence**: Commission or identify cell-based or animal studies examining COX-2 inhibition in GDF5-deficient skeletal models; without this, biological plausibility cannot be established
- **Expert consultation**: Engage skeletal dysplasia specialists and a clinical pharmacologist to assess whether anti-inflammatory intervention could have any disease-modifying role in this congenital condition
- **Reassessment of all 7 predictions**: All TxGNN-predicted indications for this drug are rare skeletal/developmental dysplasias at L5 with no supporting evidence — a systematic review of the full prediction set is recommended to identify whether any higher-priority repurposing signal exists across Ibuprofen's broader disease network
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

