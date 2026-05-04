---
layout: default
title: Entacapone
parent: 僅模型預測 (L5)
nav_order: 59
evidence_level: L5
indication_count: 10
---

# Entacapone
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

Using the `txgnn-pipeline` skill to confirm report generation context. The skill confirms this is the Netherlands (Nl) deployment. Now generating the report per the Drug Repurposing Evaluation Report Prompt v5.

---

# Entacapone: From Parkinson's Disease to PLA2G6-Associated Neurodegeneration

## One-Sentence Summary

Entacapone is a catechol-O-methyltransferase (COMT) inhibitor used as an adjunct therapy to levodopa/carbidopa for Parkinson's disease.
The TxGNN model predicts it may be effective for **PLA2G6-Associated Neurodegeneration (PLAN)**, a rare progressive neurodegenerative disorder caused by *PLA2G6* gene mutations.
Currently, **no clinical trials** and **no supporting publications** have been identified for this specific indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's disease (adjunct to levodopa/carbidopa therapy) |
| Predicted New Indication | PLA2G6-Associated Neurodegeneration |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| NL Market Status | Not registered in the Netherlands (CBG-MEB) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, Entacapone is a COMT (catechol-O-methyltransferase) inhibitor — its primary role is to prevent the peripheral breakdown of levodopa, thereby extending levodopa bioavailability and duration of dopaminergic effect in Parkinson's disease patients. Its efficacy as an adjunct in Parkinson's disease has been well established, and mechanistically it may be applicable to conditions with progressive dopaminergic neuronal loss.

PLA2G6-Associated Neurodegeneration (PLAN) is a spectrum disorder caused by biallelic mutations in the *PLA2G6* gene, which encodes a calcium-independent phospholipase A2 involved in mitochondrial membrane maintenance. PLAN encompasses phenotypes ranging from infantile neuroaxonal dystrophy (INAD) to adult-onset dystonia-parkinsonism. In the adult-onset form, progressive degeneration of dopaminergic neurons in the substantia nigra leads to parkinsonian features, and some patients demonstrate a partial initial response to levodopa therapy.

This partial dopaminergic overlap is the most plausible mechanistic bridge: if PLAN patients can derive benefit from levodopa, then COMT inhibition — by prolonging levodopa's therapeutic window — could in principle extend that benefit. However, this reasoning is indirect and speculative at this stage. PLAN's primary pathology is lipid metabolism disruption and mitochondrial membrane instability, not a COMT-mediated process. The high TxGNN score most likely reflects shared network topology between PLAN and other neurodegenerative diseases in the knowledge graph, rather than a direct mechanistic relationship. Preclinical validation is required before this hypothesis can be taken further.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for complete safety information. No drug interaction data was identified in the current Evidence Pack query.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.76%), the evidence for Entacapone in PLA2G6-Associated Neurodegeneration is at Level L5 — model prediction only, with no clinical trials, no observational data, and no supporting publications identified. The mechanistic link is indirect and speculative, relying on the partial dopaminergic overlap in adult-onset PLAN rather than a direct target relationship. Additionally, Entacapone is not currently found in the CBG-MEB registry for the Netherlands, which further limits near-term clinical applicability.

**To proceed, the following is needed:**
- Preclinical studies (animal models or patient-derived iPSC models) examining COMT inhibition effects in PLA2G6-deficient contexts
- Systematic literature review of dopaminergic treatment outcomes in adult-onset PLAN patients to quantify levodopa responsiveness
- Clarification of CBG-MEB registration status for Entacapone in the Netherlands (Comtan/Stalevo are registered in several EU countries; the zero-license result may reflect a data pipeline gap)
- Retrieval of full MOA data from DrugBank (DB00494) to enable formal mechanistic link scoring
- Safety profile review via the current SmPC before any clinical consideration is advanced
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

