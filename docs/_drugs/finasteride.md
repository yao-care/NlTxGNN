---
layout: default
title: Finasteride
parent: 僅模型預測 (L5)
nav_order: 69
evidence_level: L5
indication_count: 6
---

# Finasteride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Using the `txgnn-pipeline` skill to guide report generation for the NL (Netherlands) deployment. Now generating the evaluation report based on the provided Evidence Pack.

---

# Finasteride: From Androgenetic Alopecia / BPH to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Finasteride is a 5-alpha reductase inhibitor with established clinical use in benign prostatic hyperplasia (BPH) and male pattern hair loss (androgenetic alopecia), working by reducing dihydrotestosterone (DHT) levels.
The TxGNN model predicts it may be effective for **Ambras Type Hypertrichosis Universalis Congenita**, a rare congenital hair overgrowth disorder linked to TRPS1 gene rearrangements,
with **0 clinical trials** and **0 publications** currently supporting this specific direction — evidence level L5.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia (BPH); male pattern hair loss (androgenetic alopecia) |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| NL Market Status | Not registered (CBG-MEB data: 0 authorisations found) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on well-established pharmacological knowledge, Finasteride is a competitive inhibitor of 5-alpha reductase (isoforms type 1 and 2), the enzyme that converts testosterone into the more potent androgen dihydrotestosterone (DHT). By lowering tissue DHT concentrations, finasteride suppresses androgen-driven hair follicle miniaturisation in androgenetic alopecia and reduces prostate cell proliferation in BPH. Its efficacy in androgen-dependent conditions is pharmacologically well-characterised.

Ambras Type Hypertrichosis Universalis Congenita, however, is a distinct biological entity. It is caused by chromosomal rearrangements at 8q22–24 that dysregulate the TRPS1 transcription factor, leading to generalised, dense hypertrichosis present from birth. This condition is **not androgen-dependent**: the pathomechanism involves transcription factor imbalance rather than excessive DHT signalling. Finasteride's primary mechanism — DHT suppression — therefore lacks a clear pharmacological rationale for reversing or modulating this congenital phenotype.

The TxGNN model's very high score (0.9999) almost certainly reflects the topological proximity of finasteride's established hair-follicle disease nodes to hypertrichosis disease nodes within the knowledge graph, rather than a genuine mechanistic link. This is a well-recognised limitation of graph-based repurposing models: rare congenital conditions that share broad phenotypic labels (e.g., "hair disease") with well-studied drug targets can generate high scores without meaningful biological overlap. In the absence of any preclinical or clinical evidence, this prediction should be considered a computational hypothesis only and is **not ready for clinical translation**.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Netherlands Market Information

No CBG-MEB marketing authorisation records were found for Finasteride in this dataset. This may indicate a data retrieval gap rather than true absence from the Dutch market — Finasteride products (e.g., Propecia 1 mg for androgenetic alopecia and Proscar 5 mg for BPH) are EMA-authorised and are expected to have national registration or mutual recognition procedure status in the Netherlands.

**Action required:** Verify current NL authorisation status directly via the [CBG-MEB Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/) or the [EMA product database](https://www.ema.europa.eu/en/medicines).

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics / Samenvatting van de Productkenmerken) for complete safety information. No safety data — including warnings, contraindications, or drug interactions — was available in this Evidence Pack.

> For EU-authorised products, the SmPC is accessible via the [EMA medicines portal](https://www.ema.europa.eu/en/medicines). For nationally authorised products, the SmPC can be obtained from the CBG-MEB.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Ambras Type Hypertrichosis Universalis Congenita is a TRPS1-mediated congenital disorder with no established connection to DHT signalling or androgen pathways. The TxGNN prediction (L5) is entirely unsupported by any clinical trial, preclinical study, or published literature, and the high model score most likely represents a knowledge graph topology artefact rather than a pharmacologically valid signal.

**To proceed, the following is needed:**

- **Mechanistic validation:** Peer-reviewed evidence demonstrating that DHT or 5-alpha reductase activity plays a role in TRPS1-related hair follicle dysregulation
- **Preclinical studies:** In vitro or in vivo data showing finasteride activity in relevant congenital hypertrichosis models
- **CBG-MEB / EMA authorisation check:** Confirm current NL market status and retrieve the full SmPC for safety profiling
- **MOA data gap closure:** Retrieve complete DrugBank entry (DB01216) to populate mechanism-of-action and safety fields for a proper S1-level safety evaluation
- **Regulatory assessment:** If mechanistic evidence emerges, consult CBG-MEB guidance on off-label use or orphan designation pathways, given the ultra-rare nature of this condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

