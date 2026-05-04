---
layout: default
title: Amitriptyline Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 25
evidence_level: L5
indication_count: 0
---

# Amitriptyline Hydrochloride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Amitriptyline Hydrochloride: Insufficient Data for Drug Repurposing Evaluation

## One-Sentence Summary

Amitriptyline hydrochloride is a well-established tricyclic antidepressant (TCA) widely used for the treatment of depression, neuropathic pain, and other conditions globally. However, the TxGNN model has **not generated any predicted new indications** for this drug in the current analysis cycle, and **no clinical trial or literature evidence** has been collected. This report documents the current data gaps and outlines what is needed before a repurposing evaluation can proceed.

## Quick Overview

| Item | Content |
|------|------|
| Drug Name (INN) | Amitriptyline Hydrochloride |
| Original Indication | Not available in current dataset |
| Predicted New Indication | None — no TxGNN predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (No predictions or supporting studies available) |
| Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

There are currently **no TxGNN predictions** available for Amitriptyline Hydrochloride, so a mechanistic plausibility assessment cannot be performed at this time.

For context, Amitriptyline is a tricyclic antidepressant that primarily works by inhibiting the reuptake of serotonin and norepinephrine in the central nervous system. It also has anticholinergic, antihistaminic, and sodium channel-blocking properties. These diverse pharmacological actions have historically made it a candidate for off-label uses including neuropathic pain, migraine prophylaxis, fibromyalgia, and irritable bowel syndrome.

Currently, detailed mechanism of action data is not available in the evidence pack (listed as a data gap). The DrugBank ID has not been mapped, and no original indications are recorded in the regulatory data provided. A complete DrugBank lookup and regulatory data integration are required before any repurposing analysis can proceed.

## Clinical Trial Evidence

Currently no related clinical trials registered in the evidence pack.

> **Note:** This does not mean no clinical trials exist globally for Amitriptyline — it means the evidence collection pipeline has not yet been executed for this drug. Amitriptyline has extensive clinical trial history across multiple indications.

## Literature Evidence

Currently no related literature available in the evidence pack.

> **Note:** Amitriptyline has thousands of publications in PubMed. The absence of literature here reflects that no TxGNN-predicted indication was generated, so the evidence collection pipeline was not triggered.

## Market Information

No marketing authorizations were found in the current regulatory dataset. The drug is recorded as **not marketed** (未上市) with **0 licenses** on file.

> **Note:** Amitriptyline is widely marketed in many countries (including the Netherlands, where it is available as various generics). The absence of authorization records here may reflect a gap in the local regulatory data source rather than true unavailability.

## Safety Considerations

> Please refer to the SmPC (Summary of Product Characteristics) for complete safety information. Key safety data (warnings, contraindications, and drug–drug interactions) could not be retrieved in the current data collection cycle.
>
> **Known general safety considerations for Amitriptyline** (from established clinical knowledge):
> - **Black box warning** (in many jurisdictions): Increased risk of suicidal thinking and behaviour in children, adolescents, and young adults
> - **Cardiac risk**: QT prolongation, arrhythmias — ECG monitoring recommended
> - **Anticholinergic effects**: Dry mouth, urinary retention, constipation, blurred vision
> - **CNS depression**: Sedation, impaired psychomotor performance
> - **Contraindicated** with MAO inhibitors (risk of serotonin syndrome) and in recent myocardial infarction
>
> *These points are provided from general pharmacological knowledge and should be verified against the current SmPC.*

## Data Gaps Identified

The following critical data gaps were flagged during evidence pack assembly:

| Gap ID | Category | Item | Severity | Impact | Remediation |
|--------|----------|------|----------|--------|-------------|
| DG001 | Drug Level | Regulatory warnings/contraindications | **Blocking** | Cannot enter Stage 1 safety screening | Download and parse product label PDF from regulatory authority |
| DG002 | Drug Level | Mechanism of Action (MOA) | High | Affects mechanistic relevance analysis | Query DrugBank API |

**Additional gaps observed:**
- DrugBank ID not mapped (despite a successful DrugBank query logged on 2026-03-26)
- No original indications recorded
- No TxGNN predictions generated — root cause should be investigated (possible mapping failure)
- Drug–drug interaction query returned no results, which is unexpected for a widely-used TCA

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN predictions have been generated for Amitriptyline Hydrochloride, and multiple blocking data gaps prevent any meaningful repurposing evaluation. The absence of a DrugBank ID mapping is likely the root cause preventing the prediction pipeline from running, as the knowledge graph requires a valid DrugBank identifier to generate candidates.

**To proceed, the following is needed:**

1. **Resolve DrugBank mapping** — Amitriptyline's DrugBank ID is [DB00321](https://go.drugbank.com/drugs/DB00321). This should be populated in the evidence pack to enable KG-based prediction
2. **Re-run TxGNN prediction pipeline** once the DrugBank ID is correctly mapped
3. **Retrieve SmPC/label data** — Download and parse the product label to fill safety data gaps (DG001)
4. **Populate MOA data** from DrugBank (DG002) — Amitriptyline's targets include SLC6A4 (SERT), SLC6A2 (NET), and multiple receptor subtypes
5. **Verify market status** — Amitriptyline is widely available internationally; confirm whether the "not marketed" status reflects the local dataset scope or an actual gap
6. **Re-run evidence collection** (ClinicalTrials.gov, PubMed) once a predicted indication is available

---

*⚠️ Disclaimer: This report is for research purposes only and does not constitute medical advice. Any drug repurposing candidates require clinical validation before application. Data cutoff: 2026-04-03.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

