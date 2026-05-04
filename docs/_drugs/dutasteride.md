---
layout: default
title: Dutasteride
parent: 僅模型預測 (L5)
nav_order: 55
evidence_level: L5
indication_count: 10
---

# Dutasteride
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

The txgnn-pipeline skill confirms this is an NlTxGNN (Netherlands) deployment report. Now generating the evaluation report from the Evidence Pack.

---

# Dutasteride: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Dutasteride is a dual 5α-reductase inhibitor (5-ARI) internationally approved for the treatment of benign prostatic hyperplasia (BPH), though it currently holds no marketing authorisation in the Netherlands.
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita** — a rare congenital disorder causing generalised excessive hair growth — with **0 clinical trials** and **0 publications** currently supporting this specific direction.
The entire evidence base rests solely on the computational model prediction; no empirical support exists.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in the Netherlands; internationally approved for benign prostatic hyperplasia (BPH) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| NL Market Status | Not registered (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this Evidence Pack. Based on established pharmacology, Dutasteride is a potent dual inhibitor of 5α-reductase isoenzymes type 1 and type 2 — the enzymes responsible for converting testosterone into dihydrotestosterone (DHT). By reducing DHT levels in both systemic circulation and target tissues, Dutasteride suppresses androgen-dependent processes, most notably prostate tissue proliferation (BPH) and the miniaturisation of scalp hair follicles seen in androgenetic alopecia. This androgen-pathway action forms the theoretical starting point for its inclusion in hair-related predictions.

Ambras type hypertrichosis universalis congenita is an exceptionally rare congenital syndrome characterised by dense, fine hair covering the entire body surface except the palms and soles. Critically, the condition is caused by structural rearrangements or mutations affecting the **TRPS1 gene** on chromosome 8q23-q24, which encodes a transcription factor involved in hair follicle morphogenesis. The pathological mechanism is entirely gene-developmental in nature and has **no established dependence on androgen signalling or DHT levels**.

The mechanistic connection between Dutasteride's DHT-lowering action and an androgen-independent genetic hair disorder is therefore extremely weak. The high TxGNN score most likely reflects shared ontological proximity in the knowledge graph (both Dutasteride and this disease are linked to hair-related nodes) rather than any true pharmacological relationship. This prediction should be treated as a knowledge-graph artefact, not a clinically actionable signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for complete safety information. No drug interaction data, key warnings, or contraindication data were available in this Evidence Pack for automated review.

> **Note for CBG-MEB reviewers:** As Dutasteride holds no RVG authorisation in the Netherlands, the relevant SmPC reference would be a centrally authorised EMA product document or the SmPC of an authorised equivalent in an EU member state.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Dutasteride's mechanism of action — DHT reduction through dual 5α-reductase inhibition — has no established pharmacological relevance to Ambras type hypertrichosis universalis congenita, which is driven by a TRPS1 developmental gene mutation entirely outside the androgen signalling pathway. The high TxGNN score reflects a knowledge-graph proximity artefact, not a clinical opportunity. Furthermore, Dutasteride is not currently authorised in the Netherlands (no CBG-MEB RVG number), so any clinical application would require full regulatory authorisation before use.

A broader observation: across all **10 top TxGNN-predicted indications** for Dutasteride in this pack, every prediction is rated **L5** with a **Hold** recommendation. The recurring pattern of rare genetic hair and developmental disorders with no androgen-pathway link suggests the model is over-fitting to hair-biology nodes in the knowledge graph without mechanistic validation.

**To proceed, the following would be needed:**
- Preclinical evidence (in vitro or animal model) demonstrating that 5α-reductase inhibition meaningfully affects TRPS1 pathway activity or follicular development in congenital hypertrichosis
- A mechanistic review clarifying whether any sub-classification of Ambras syndrome carries an androgen-sensitive component
- Acquisition of Dutasteride's full SmPC from EMA or a member-state authority to complete S1 safety screening
- MOA documentation from DrugBank (data gap DG002) to enable automated mechanistic linkage scoring
- Assessment of whether a more clinically relevant off-label indication (e.g., androgenetic alopecia in women, where DHT pathway evidence does exist) should be prioritised over the current rank-1 prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

