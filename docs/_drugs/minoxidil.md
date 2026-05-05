---
layout: default
title: Minoxidil
parent: 僅模型預測 (L5)
nav_order: 94
evidence_level: L5
indication_count: 10
---

# Minoxidil
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

Using `txgnn-pipeline` to confirm this is a Netherlands (Nl) deployment report — proceeding with the Evidence Pack analysis for Minoxidil.

---

# Minoxidil: From Androgenetic Alopecia to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Minoxidil is a potassium channel opener established as a topical treatment for androgenetic alopecia (pattern hair loss) in both men and women, with a long-standing systemic use history for severe hypertension.
The TxGNN model predicts it may also be effective for **Hypotrichosis Simplex of the Scalp** (HSS), a rare hereditary hair growth disorder,
with **no registered clinical trials** and **3 case-level publications** currently available to support this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Androgenetic alopecia (pattern hair loss) — no Dutch (CBG-MEB) marketing authorisation on record |
| Predicted New Indication | Hypotrichosis Simplex of the Scalp |
| TxGNN Prediction Score | 99.9999% |
| Evidence Level | L3 |
| NL Market Status | Not Registered |
| Number of Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this Evidence Pack. Based on established pharmacological knowledge, Minoxidil functions as a potassium (K⁺) ATP channel opener. Applied topically, it promotes perifollicular vasodilation — increasing blood flow and oxygen delivery to hair follicles — and extends the anagen (active growth) phase of the hair cycle. It may also facilitate the conversion of fine vellus hairs into thicker terminal hairs. These properties underlie its well-established efficacy in androgenetic alopecia and explain why it appears frequently as an adjunct treatment across multiple hair loss conditions.

Hypotrichosis Simplex of the Scalp is a rare autosomal dominant monogenic disorder caused by loss-of-function variants in the *CDSN* gene, which encodes the desmosome protein corneodesmosin. Unlike scarring alopecias — where follicles are permanently replaced by fibrous tissue — HSS involves structurally underdeveloped follicles that retain a degree of residual function. This distinction is mechanistically important: Minoxidil's vasodilation-based approach can, in principle, stimulate these remaining follicles to produce more and longer hair, which is the primary biological reason the TxGNN model assigns a near-perfect prediction score.

The mechanistic overlap between HSS and androgenetic alopecia is real but partial. Both conditions involve impaired hair growth from living follicles; however, HSS arises from a fixed genetic structural defect rather than androgen-mediated follicular miniaturisation. All three currently available publications document positive clinical responses to Minoxidil at the case level, consistent with biological plausibility. However, the evidence base is far too limited to support routine clinical use, and the ultra-rare nature of HSS makes large-scale trial recruitment exceptionally challenging.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Minoxidil in Hypotrichosis Simplex of the Scalp.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [35761391](https://pubmed.ncbi.nlm.nih.gov/35761391/) | 2022 | Case Series | Dermatologic Therapy | Oral minoxidil combined with growth factors led to improvement in hereditary HSS; supports feasibility of minoxidil-based treatment in this rare genetic condition |
| [39902296](https://pubmed.ncbi.nlm.nih.gov/39902296/) | 2024 | Case Series | Frontiers in Genetics | An 8-year-old male with genetically confirmed HSS (CDSN mutation) was treated with botanical extracts plus minoxidil; clinical response documented in a diagnosed familial case |
| [36651821](https://pubmed.ncbi.nlm.nih.gov/36651821/) | 2023 | Case Report | Journal of Dermatological Treatment | A 14-year-old with hereditary hypotrichosis simplex treated with platelet-rich plasma injection combined with topical minoxidil 2%; improvement in hair length and density reported |

---

## Netherlands Market Information

No products containing Minoxidil hold a marketing authorisation issued by CBG-MEB at the time of this assessment. No RVG numbers are on record.

> **Note:** Topical Minoxidil preparations (e.g., Regaine/Rogaine) are widely authorised across other EU Member States for androgenetic alopecia. This result warrants direct verification against the current CBG-MEB and EMA product registers, as a data collection gap cannot be excluded.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics / *Samenvatting van de Productkenmerken*) for complete safety information, including key warnings, contraindications, and drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a near-perfect prediction score and the mechanistic rationale for Minoxidil in HSS is biologically plausible — residual functional follicles in this genetic condition may respond to perifollicular vasodilation. However, all current supporting evidence is limited to three case-level publications (two case series, one case report), no prospective trials exist for this indication, formal safety data in this Evidence Pack is incomplete, and Minoxidil carries no confirmed CBG-MEB marketing authorisation in the Netherlands. This combination of evidence and regulatory gaps warrants a Hold until foundational data can be collected.

**To proceed, the following is needed:**

- Verification of current NL/EU marketing authorisation status through the CBG-MEB register and EMA product database (EPAR)
- Retrieval of SmPC safety data: key warnings, contraindications, and drug-drug interactions
- Mechanism of action documentation via DrugBank API (DB00350)
- At least one prospective pilot study or well-documented consecutive case series (n ≥ 10) in genetically confirmed HSS patients
- EMA Orphan Designation assessment, given the ultra-rare classification of HSS
- Pre-consultation with CBG-MEB on off-label prescribing pathways if an unregistered product is to be used in the Netherlands
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

