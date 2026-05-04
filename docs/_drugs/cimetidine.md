---
layout: default
title: Cimetidine
parent: 僅模型預測 (L5)
nav_order: 43
evidence_level: L5
indication_count: 9
---

# Cimetidine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

The txgnn-pipeline skill confirms this is a Netherlands (NL) deployment context. Now I'll generate the full evaluation report for Cimetidine based on the Evidence Pack.

---

# Cimetidine: From Peptic Ulcer Disease to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Cimetidine is a first-generation histamine H2 receptor antagonist, historically the standard-of-care treatment for peptic ulcer disease and related acid hypersecretory conditions throughout the 1970s–1990s.
The TxGNN model predicts it may be effective for **Smouldering Systemic Mastocytosis (SMM)**,
with **no registered clinical trials** and **no published literature** directly supporting this specific indication at this time — placing this prediction in the mechanistic hypothesis category only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Peptic ulcer disease (histamine H2 receptor antagonist; well-established historical core indication) |
| Predicted New Indication | Smouldering Systemic Mastocytosis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 |
| NL Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available for this report. Based on well-established pharmacological knowledge, Cimetidine is a **histamine H2 receptor antagonist** — it competitively blocks H2 receptors on gastric parietal cells, markedly reducing both basal and stimulated gastric acid secretion. This mechanism underpinned its landmark role in peptic ulcer healing throughout the late 20th century and is one of the most thoroughly validated drug–receptor interactions in modern pharmacology.

The TxGNN prediction for Smouldering Systemic Mastocytosis (SMM) is mechanistically coherent. SMM is an indolent variant of systemic mastocytosis in which clonally expanded mast cells accumulate primarily in the bone marrow; progression to aggressive disease is slow. The dominant symptom burden — urticaria, gastrointestinal cramps, flushing, and episodic hypotension — is driven by excess **histamine release** from activated mast cells. Blocking H2 receptors therefore directly addresses the gastric acid hypersecretion and GI components of histamine-mediated injury. In clinical practice, combined H1 + H2 antihistamine therapy is already recommended as first-line symptomatic management in mastocytosis guidelines (e.g., European Competence Network on Mastocytosis).

That said, cimetidine's role in SMM is supportive and off-label. SMM is an indolent but systemic disease requiring specialist haematological follow-up, and no formal RCT has ever been conducted. The TxGNN model likely captures the strong histamine-pathway overlap between peptic ulcer disease (the original indication) and mastocytosis, but the mechanistic step from "H2 blockade reduces GI symptoms" to "modifies mast cell disease course" is not proven.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Cimetidine in Smouldering Systemic Mastocytosis.

---

## Literature Evidence

Currently no related literature available for Cimetidine in Smouldering Systemic Mastocytosis.

---

## Netherlands Market Information

Cimetidine is currently **not authorized for marketing in the Netherlands**. No RVG numbers are on record with the CBG-MEB (College ter Beoordeling van Geneesmiddelen). Any clinical use would require an individual patient named-patient or magistral preparation route.

| RVG Number | Product Name | Dosage Form | Approved Indication |
|------------|--------------|-------------|---------------------|
| — | — | — | No CBG-MEB authorization on record |

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model generates a high confidence score (99.80%) for cimetidine in SMM based on a mechanistically sound histamine H2 pathway overlap, but the complete absence of direct clinical trial or published literature evidence — combined with the drug's unauthorized status in the Netherlands — means this prediction cannot be translated into a repurposing programme without substantial additional evidence generation.

**To proceed, the following is needed:**

- Systematic search and review of off-label cimetidine use in mastocytosis case series, expert consensus statements, and mastocytosis society guidelines (e.g., ECNM) to establish whether any informal clinical evidence base already exists
- Retrieval of cimetidine's full mechanism of action and safety profile from DrugBank (DG002 remediation: DrugBank API query)
- Identification of available pharmaceutical formulations and appropriate dosing regimens suitable for SMM symptom management in Dutch clinical practice
- CBG-MEB consultation on the regulatory pathway for an unlicensed drug in a rare/ultra-rare disease setting (SMM qualifies as an orphan disease indication under EMA criteria)
- If supportive evidence is found, design of a prospective observational registry or pilot study in collaboration with a Dutch haematology centre (e.g., HOVON network) before considering a formal Phase 2 trial
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

