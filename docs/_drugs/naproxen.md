---
layout: default
title: Naproxen
parent: 僅模型預測 (L5)
nav_order: 97
evidence_level: L5
indication_count: 4
---

# Naproxen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Using the `txgnn-pipeline` skill for context — this is an NlTxGNN drug repurposing evaluation report. Now generating the report from the Evidence Pack.

---

# Naproxen: From Pain and Inflammation to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Naproxen is a widely used non-steroidal anti-inflammatory drug (NSAID), proven effective for pain relief, fever, and a range of inflammatory conditions including arthritis and dysmenorrhoea.
The TxGNN model predicts it may show activity in **Brachydactyly-Syndactyly Syndrome**, a rare inherited limb malformation affecting digit length and fusion.
Currently, **no clinical trials** and **no published literature** specifically support this indication, placing the prediction at the lowest evidence tier (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pain, fever, and inflammatory conditions — arthritis, dysmenorrhoea, ankylosing spondylitis (NSAID class) |
| Predicted New Indication | Brachydactyly-Syndactyly Syndrome |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| NL Market Status | Not Registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, Naproxen is a non-selective COX-1/COX-2 inhibitor from the propionic acid class of NSAIDs. It suppresses prostaglandin synthesis — particularly PGE2 — producing anti-inflammatory, analgesic, and antipyretic effects. COX-2 is expressed in osteoblasts, and prostaglandins, especially PGE2, are known participants in skeletal development, growth plate regulation, and bone remodelling. This shared biology forms the theoretical basis of the TxGNN model's prediction.

However, brachydactyly-syndactyly syndrome is a congenital structural malformation driven by germline mutations in developmental genes such as those within the HOXD cluster and FGF signalling pathway. These genetic alterations determine limb patterning during embryogenesis — a process occurring before birth that is not mediated by inflammatory pathways. Naproxen's COX inhibition mechanism has no established role in correcting pre-formed structural digit abnormalities arising from such developmental gene defects.

The mechanistic link is therefore highly indirect and speculative. The model prediction likely reflects a pattern-matching signal within shared skeletal biology pathways rather than a clinically actionable therapeutic mechanism. Without supporting preclinical or clinical evidence, this prediction cannot be considered pharmacologically justified at its current stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests solely on a TxGNN model signal (L5 evidence) with no supporting clinical trials, published literature, or established mechanistic rationale. Brachydactyly-syndactyly syndrome is a rare congenital genetic disorder; NSAID-based pharmacotherapy has no known role in its pathophysiology or management.

**To proceed, the following is needed:**

- **Preclinical evidence**: In vitro or animal model studies demonstrating a COX inhibitor effect on digit malformation pathways
- **Mechanistic validation**: A confirmed biological link between prostaglandin signalling dysregulation and brachydactyly-syndactyly syndrome aetiology
- **Safety review**: Full SmPC retrieval from CBG-MEB to assess contraindications, key warnings, and drug interactions before any further evaluation
- **NL regulatory clarification**: Verification of Naproxen's CBG-MEB registration status — the current dataset shows 0 authorizations, which warrants confirmation against the official CBG-MEB register
- **Clinical genetics consultation**: Assessment by a clinical geneticist on whether any prostaglandin-mediated mechanism could plausibly modulate the relevant genetic pathways (HOXD, FGF)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

