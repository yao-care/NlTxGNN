---
layout: default
title: Sorbitol
parent: 僅模型預測 (L5)
nav_order: 112
evidence_level: L5
indication_count: 1
---

# Sorbitol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

Using the `txgnn-pipeline` skill context (NlTxGNN, Netherlands deployment), I'll now generate the evaluation report from the Evidence Pack.

---

# Sorbitol: From Osmotic Agent to Exercise-Induced Malignant Hyperthermia

## One-Sentence Summary

Sorbitol is a sugar alcohol widely used as an osmotic laxative, humectant, and pharmaceutical excipient; no formal approved indication is recorded in the Dutch regulatory database.
The TxGNN model predicts it may be effective for **Exercise-Induced Malignant Hyperthermia**,
however with **0 clinical trials** and **0 publications** currently supporting this direction, the evidence base consists entirely of a computational model prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication on record |
| Predicted New Indication | Exercise-induced malignant hyperthermia |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| NL Market Status | Not Registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Sorbitol in this evidence pack. Based on established pharmacology, Sorbitol is an osmotic sugar alcohol that exerts its primary therapeutic effect through osmotic pressure regulation in the gastrointestinal tract. Its metabolic pathway — Sorbitol → Fructose → glycolysis — is well characterised in intermediary metabolism but carries no known direct pharmacological relevance to skeletal muscle pathophysiology.

Exercise-induced malignant hyperthermia is a rare, potentially life-threatening disorder caused predominantly by gain-of-function mutations in the *RYR1* gene, which encodes the ryanodine receptor governing calcium release from the sarcoplasmic reticulum of skeletal muscle. During an acute episode, uncontrolled intracellular calcium efflux leads to sustained muscular contraction, severe hyperthermia, and metabolic acidosis. The established first-line treatment is dantrolene, which directly suppresses RYR1-mediated calcium release — a completely different mechanism from osmotic modulation.

There is no recognised mechanistic bridge between Sorbitol's osmotic properties and RYR1-mediated calcium dysregulation. The high TxGNN score (0.994) most plausibly reflects indirect node proximity in the knowledge graph through shared skeletal muscle metabolism pathways, rather than a true drug–disease pharmacological connection. This prediction is assessed as a likely computational false positive with no current clinical translational basis, and should not be advanced without preclinical mechanistic evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Netherlands Market Information

Sorbitol currently holds no marketing authorisation registered with the **CBG-MEB** (College ter Beoordeling van Geneesmiddelen) in the Netherlands. There are no RVG-numbered products on record. Should future evidence warrant regulatory consideration, a new marketing authorisation application or extension of indication procedure would be required from the outset.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information. As no products are currently registered in the Netherlands, the relevant reference documents would be those from comparable jurisdictions (e.g., EMA-authorised products containing Sorbitol as an active substance).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This repurposing candidate is classified as **L5** (model prediction only) — there are no registered clinical trials, no published literature, and no established mechanistic link between Sorbitol's osmotic pharmacology and the RYR1-driven calcium dysregulation underlying exercise-induced malignant hyperthermia. The prediction is assessed as a likely knowledge-graph false positive.

**To proceed, the following is needed:**
- Retrieve formal MOA documentation for Sorbitol via DrugBank API to rule out any overlooked secondary pharmacology
- Establish a plausible mechanistic hypothesis connecting Sorbitol to RYR1-mediated calcium handling (e.g., osmotic effects on intracellular calcium dynamics, or fructose-pathway interactions with muscle energetics)
- Generate at minimum Level L4 evidence: in vitro or animal model data demonstrating any meaningful effect on malignant hyperthermia pathways
- If preclinical evidence emerges, initiate CBG-MEB pre-submission consultation — noting that no NL market presence currently exists and a full authorisation pathway would be required
- Conduct a competitive landscape review against dantrolene and other RYR1-targeted agents to assess clinical differentiation potential
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

