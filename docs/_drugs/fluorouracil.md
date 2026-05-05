---
layout: default
title: Fluorouracil
parent: 僅模型預測 (L5)
nav_order: 71
evidence_level: L5
indication_count: 10
---

# Fluorouracil
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

Using `txgnn-pipeline` for context — this is a NlTxGNN report generation task. Now generating the evaluation report based on the Evidence Pack.

---

# Fluorouracil (5-FU): From Colorectal Cancer to Botryoid-Type Embryonal Rhabdomyosarcoma of the Vagina

## One-Sentence Summary

Fluorouracil (5-FU) is a fluoropyrimidine antimetabolite widely used as the backbone agent in combination chemotherapy regimens (FOLFOX, FOLFIRI, FOLFIRINOX) for gastrointestinal cancers, including colorectal and gastric cancer.
The TxGNN model predicts it may be effective for **Botryoid-Type Embryonal Rhabdomyosarcoma of the Vagina**, an extremely rare paediatric soft tissue sarcoma.
Currently, **0 clinical trials** and **0 publications** specifically support this direction, placing this prediction at the lowest evidence level — **L5 (model prediction only)**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No CBG-MEB marketing authorisation on record for the Netherlands |
| Predicted New Indication | Botryoid-Type Embryonal Rhabdomyosarcoma of the Vagina |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| NL Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on well-established pharmacology, Fluorouracil (5-FU) is a fluoropyrimidine antimetabolite that inhibits thymidylate synthase (TS), thereby blocking DNA synthesis and selectively killing rapidly dividing cells. This mechanism underlies its efficacy as the backbone of major oncology regimens — including FOLFOX, FOLFIRI, and FOLFIRINOX — widely used for colorectal, gastric, pancreatic, and biliary cancers worldwide.

The predicted target — botryoid-type embryonal rhabdomyosarcoma of the vagina — is a distinctly rare paediatric soft tissue sarcoma. The standard of care for rhabdomyosarcoma (RMS) is the VAC regimen (vincristine, actinomycin D, cyclophosphamide), as established by international cooperative groups including ARST0531 and EpSSG RMS 2005. Fluorouracil does not appear in any current RMS treatment guidelines, and this specific botryoid vaginal subtype has its own distinct clinical behaviour from the broader RMS family.

The TxGNN score of 99.75% most likely reflects the knowledge graph generalising from the broader RMS parent node to this extremely rare subtype, rather than any direct biological signal. While 5-FU's cytotoxic mechanism is theoretically applicable to any rapidly proliferating malignancy, there is no clinical, translational, or preclinical evidence specific to this vaginal RMS subtype to support this prediction. It should be treated as a model-generated hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Netherlands Market Information

Fluorouracil (DB00544) has no CBG-MEB marketing authorisation on record in this Evidence Pack (0 RVG numbers). This likely represents a data gap in the current dataset, as 5-FU is a well-established antineoplastic agent available in multiple European markets. Clinicians and assessors should verify the current registration status directly via the [CBG-MEB public register](https://www.cbg-meb.nl/) or the [EMA product database](https://www.ema.europa.eu/en/medicines).

| RVG Number | Product Name | Dosage Form | Approved Indication |
|------------|--------------|-------------|---------------------|
| — | No authorisation data available in this Evidence Pack | — | — |

---

## Cytotoxicity

Fluorouracil is a conventional cytotoxic agent (fluoropyrimidine antimetabolite). The following applies to systemic administration.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Fluoropyrimidine class (antimetabolite) |
| Myelosuppression Risk | Moderate to High — dose-limiting leucopenia, thrombocytopenia, and anaemia are well-documented |
| Emetogenicity Classification | Low to Moderate |
| Monitoring Items | Full blood count (CBC), liver function tests, renal function; DPD (dihydropyrimidine dehydrogenase) enzyme deficiency screening is strongly recommended prior to treatment initiation |
| Handling Protection | Yes — cytotoxic handling precautions required per NIOSH guidelines and ISOPP standards for preparation, administration, and waste disposal |

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for complete safety information. No Dutch SmPC or TFDA package insert data was available in this Evidence Pack for formal safety extraction.

> **Note for clinical reviewers:** Given that all key warning and contraindication fields are absent from this dataset, a full SmPC review is mandatory before any clinical or regulatory decision is made. Special attention should be paid to DPD deficiency, cardiotoxicity (particularly with continuous infusion), and neurotoxicity.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is currently zero clinical, translational, or preclinical evidence specifically linking Fluorouracil to botryoid-type embryonal rhabdomyosarcoma of the vagina. The TxGNN prediction score (99.75%) is high in absolute terms but is almost certainly driven by knowledge graph node generalisation from the broader RMS parent class — not by disease-specific biological evidence. This subtype is also an ultra-rare paediatric tumour with an established standard of care (VAC chemotherapy) that does not include 5-FU.

**To proceed, the following is needed:**

- **Mechanistic evidence:** TS expression and 5-FU sensitivity data in RMS cell lines (particularly botryoid subtype), ideally via in vitro cytotoxicity assays
- **Preclinical data:** In vivo RMS models incorporating Fluorouracil to establish proof-of-concept antitumour activity
- **Clinical expert review:** Consultation with paediatric oncology specialists (e.g., via SIOPE/EpSSG network) to assess scientific plausibility before any further investment
- **NL regulatory status clarification:** Confirm CBG-MEB registration status and available SmPC for Fluorouracil in the Netherlands — the current data gap must be resolved
- **Safety package:** Obtain full SmPC and contraindication data, with special attention to use in paediatric and ultra-rare disease populations
- **Knowledge graph audit:** Evaluate whether the high TxGNN scores for all five RMS subtypes in this Evidence Pack reflect genuine biological signal or a systematic structural false positive from RMS node generalisation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

