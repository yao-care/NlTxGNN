---
layout: default
title: Sulfasalazine
parent: 僅模型預測 (L5)
nav_order: 113
evidence_level: L5
indication_count: 10
---

# Sulfasalazine
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

以下是根據 Evidence Pack 產生的完整評估報告：

---

# Sulfasalazine: From Inflammatory Arthritis / IBD to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Sulfasalazine is a well-established anti-inflammatory agent and disease-modifying antirheumatic drug (DMARD), globally used for inflammatory bowel disease, rheumatoid arthritis, and ankylosing spondylitis; it is not currently registered in the Netherlands market.
The TxGNN model assigns it a **99.94% prediction score** for **Brachydactyly-Syndactyly Syndrome** as a potential new indication.
However, **no clinical trials and no published literature** support this direction, and the mechanistic rationale is considered implausible — this prediction is likely a knowledge-graph artefact.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in the Netherlands; globally used for inflammatory bowel disease, rheumatoid arthritis, and ankylosing spondylitis |
| Predicted New Indication | Brachydactyly-Syndactyly Syndrome |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| NL Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Sulfasalazine is a combined anti-inflammatory and DMARD whose therapeutic effects involve NF-κB inhibition, blockade of prostaglandin and leukotriene synthesis, and suppression of pro-inflammatory cytokine production. Its clinical efficacy in inflammatory bowel disease, rheumatoid arthritis, and spondyloarthritis is well established globally.

Brachydactyly-syndactyly syndrome is a congenital skeletal developmental disorder caused by genetic mutations (most commonly involving ROR2 or related developmental genes). The structural abnormalities arise during embryogenesis and cannot be corrected by post-natal anti-inflammatory therapy. There is no biological pathway through which Sulfasalazine's anti-inflammatory mechanisms could plausibly influence the molecular defects underlying this syndrome.

The high TxGNN score (99.94%) most likely results from topological proximity between orthopaedic disease nodes in the knowledge graph (KG), rather than from any true pharmacological relationship. This is a recognised limitation of graph-based prediction algorithms: high scores can reflect shared network neighbourhood rather than genuine drug-disease biology. **This prediction is considered a probable false positive and does not warrant further clinical investigation at this stage.**

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Netherlands Market Information

Sulfasalazine currently holds **no marketing authorizations** registered with the CBG-MEB (College ter Beoordeling van Geneesmiddelen). No SmPC (Samenvatting van de Productkenmerken) or PIL (Bijsluiter) data is available from the Dutch regulatory database for this product.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Brachydactyly-syndactyly syndrome is a congenital, genetically-determined skeletal disorder with no plausible pharmacological entry point for an anti-inflammatory DMARD such as Sulfasalazine. The very high TxGNN prediction score (99.94%) is most likely driven by knowledge-graph topological similarity rather than any genuine drug-disease signal; no clinical trial, observational study, or mechanistic publication exists to support this hypothesis.

**To proceed, the following is needed:**
- A credible biological hypothesis demonstrating how Sulfasalazine's known molecular pathways could influence the ROR2 (or equivalent) developmental signalling cascade underlying this syndrome — currently considered implausible
- Should any such mechanistic hypothesis emerge in future basic-science research, a targeted literature review and expert genetics consultation would be the mandatory first steps before any clinical consideration
- Separately, the NL regulatory data gap (0 CBG-MEB authorizations, missing SmPC) should be resolved to enable a proper safety baseline assessment of Sulfasalazine itself, independent of this repurposing question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

