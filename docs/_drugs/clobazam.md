---
layout: default
title: Clobazam
parent: 僅模型預測 (L5)
nav_order: 44
evidence_level: L5
indication_count: 10
---

# Clobazam
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

The `txgnn-pipeline` skill confirms this is the NL (Netherlands) deployment context. The system prompt's Report Prompt v5 provides complete formatting instructions. Generating the report now.

---

# Clobazam: From Epilepsy to Febrile Infection-Related Epilepsy Syndrome

## One-Sentence Summary

Clobazam is a 1,5-benzodiazepine with established global use as an antiepileptic and anxiolytic agent, including FDA-approved adjunctive treatment for Lennox-Gastaut syndrome (2011).
The TxGNN model predicts it may be effective for **febrile infection-related epilepsy syndrome (FIRES)**,
with **0 clinical trials** and **2 publications** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Epilepsy (adjunctive therapy incl. Lennox-Gastaut syndrome) and anxiety — not registered in the Netherlands |
| Predicted New Indication | Febrile infection-related epilepsy syndrome (FIRES) |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| NL Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on information embedded in the evidence literature, Clobazam is a 1,5-benzodiazepine that enhances GABA-A receptor function with a known preference for the α2 subtype. This mechanism reduces cortical and subcortical hyperexcitability, forming the pharmacological basis for its broad use across epilepsy syndromes — from focal seizures to severe developmental epileptic encephalopathies such as Lennox-Gastaut syndrome and Dravet syndrome.

FIRES is a catastrophic form of new-onset refractory status epilepticus (NORSE) that primarily affects previously healthy children and adolescents. During the acute phase, intravenous benzodiazepines — in particular midazolam — are a cornerstone of seizure suppression. The TxGNN prediction rests on a plausible class-level inference: oral clobazam, as a 1,5-BZD, could theoretically serve as a transitional weaning agent when patients are being stepped down from IV anaesthetic management toward oral maintenance therapy. This pathway has biological coherence given shared GABA-A receptor targets.

However, the available literature does not study clobazam directly in FIRES. The two identified publications focus on enteral **lorazepam** (PMID 35770765) and **perampanel** (PMID 39958143) as weaning strategies — clobazam is not the primary subject in either. This prediction therefore represents a **BZD class-effect extrapolation**, not drug-specific evidence, which appropriately constrains the evidence level to L4.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35770765](https://pubmed.ncbi.nlm.nih.gov/35770765/) | 2022 | Case series | Epileptic Disorders | Enteral lorazepam used as effective weaning substitute for midazolam in FIRES patients; supports the BZD class weaning concept but does not study clobazam directly |
| [39958143](https://pubmed.ncbi.nlm.nih.gov/39958143/) | 2025 | Case report | Cureus | Perampanel reduced barbiturate dependency in a 13-year-old with FIRES; highlights need for non-anaesthetic alternatives — clobazam not evaluated |

---

## Netherlands Market Information

Clobazam currently holds **no CBG-MEB marketing authorization** in the Netherlands. There are 0 registered products containing clobazam in the Dutch medicines registry. Any clinical use in the Netherlands would require a patient-level special authorization (Article 3.17 Geneesmiddelenwet) or a named-patient importation route under applicable regulatory provisions. The absence of a Dutch SmPC means safety and dosing guidance must be sourced from the EMA product information or the FDA-approved SmPC (Onfi®).

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for full safety information. Given the absence of a Dutch CBG-MEB authorization, the EMA SmPC for clobazam (where available) or the FDA SmPC for Onfi® is the recommended reference document.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.82%), the supporting evidence for clobazam specifically in FIRES consists of only 2 publications — neither of which directly investigates clobazam — and 0 registered clinical trials. The mechanistic rationale is biologically plausible as a benzodiazepine class effect, but drug-specific clinical validation is absent.

**To proceed, the following is needed:**
- Direct clinical data on clobazam in FIRES: a prospective case series or observational study specifically evaluating clobazam as a weaning or maintenance agent
- Safety and pharmacokinetic profiling in the FIRES population (critically ill, predominantly pediatric, often on concurrent anaesthetics)
- Regulatory pathway assessment: clobazam is not authorized in the Netherlands; a Named Patient / hospital exemption pathway via CBG-MEB must be established before any trial use
- Mechanism of action documentation: DrugBank API query to resolve the current data gap (DG002) and support mechanistic plausibility analysis
- Safety review to resolve DG001: Dutch or EMA SmPC warnings and contraindications must be obtained before entering formal safety evaluation (currently blocking S1 stage)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

