---
layout: default
title: Didanosine
parent: 僅模型預測 (L5)
nav_order: 52
evidence_level: L5
indication_count: 3
---

# Didanosine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

The `txgnn-pipeline` skill is loaded. Now I'll analyze the Evidence Pack carefully and generate the report following the v5 prompt specifications.

Key observations before writing:
- **Drug**: Didanosine (NRTI antiretroviral; MOA is [Data Gap] but inferred from literature context in the pack)
- **Top prediction**: Feline AIDS — a **veterinary, non-human** disease; unusual scope for NL human healthcare
- **NL market**: No CBG-MEB authorizations (0 licenses, not marketed)
- **Safety data**: All [Data Gap] → omit, refer to SmPC
- **Not antineoplastic** → omit Cytotoxicity section
- **Evidence**: L4 (animal/in vitro studies only, 0 clinical trials)

---

# Didanosine: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Didanosine (ddI) is a nucleoside reverse transcriptase inhibitor (NRTI) established for the treatment of HIV infection in humans.
The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome** (caused by feline immunodeficiency virus, FIV),
with **0 clinical trials** and **3 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV infection (antiretroviral therapy; NRTI class) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.33% |
| Evidence Level | L4 |
| NL Market Status | Not marketed in the Netherlands |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, Didanosine is a dideoxynucleoside-class NRTI whose active metabolite — dideoxyadenosine triphosphate (ddATP) — competitively inhibits viral reverse transcriptase and terminates elongating proviral DNA. Its efficacy against HIV, a retroviral lentivirus, is well established after decades of clinical use.

Feline acquired immunodeficiency syndrome is caused by feline immunodeficiency virus (FIV), which belongs to the same lentivirus family as HIV. Both viruses depend on a reverse transcriptase enzyme for replication. This shared biological architecture is why the TxGNN model assigns a high similarity score: in principle, ddATP could inhibit FIV reverse transcriptase by the same chain-termination mechanism. PMID 17616550 explicitly uses a FIV-infected cat model to study didanosine's effects, confirming the drug does reach and act within this biological system.

However, two critical caveats must be stated clearly. First, FIV reverse transcriptase differs from HIV-1 RT in substrate-binding residues, so cross-activity is not guaranteed and requires dedicated experimental validation. Second — and more fundamentally — **feline acquired immunodeficiency syndrome is a veterinary disease affecting cats, not humans**. This places the top-ranked TxGNN prediction outside the standard scope of human drug repurposing for the Netherlands healthcare system. The evidence base is limited to animal and in vitro studies, with no registered clinical trials in any population.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [17616550](https://pubmed.ncbi.nlm.nih.gov/17616550/) | 2007 | Animal toxicity study | *Brain* | Didanosine induces sensory neuropathy in FIV-infected cats (ex vivo and in vivo ATN model); impaired mitochondrial and neurotrophic factor gene expression. Demonstrates ddI pharmacological activity in FIV-infected hosts, though in a toxic rather than therapeutic context. |
| [2540111](https://pubmed.ncbi.nlm.nih.gov/2540111/) | 1989 | Animal experiment | *Intervirology* | FeLV (feline leukaemia virus)-infected cats used as an antiretroviral chemotherapy model; ddI (2',3'-dideoxyinosine) tested in vitro against feline retroviral replication alongside AZT and other dideoxynucleosides — earliest evidence of ddI activity in feline retroviral systems. |
| [19380511](https://pubmed.ncbi.nlm.nih.gov/19380511/) | 2009 | Animal neuroscience study | *FASEB Journal* | CXCR3-mediated neuronal injury during lentiviral infection studied in FIV/HIV models; antiretroviral therapy (including ddI-class agents) shown to have neuroprotective effects, supporting mechanistic overlap between FIV and HIV treatment pathways. |

---

## Netherlands Market Information

Didanosine currently holds **no marketing authorizations** with CBG-MEB (College ter Beoordeling van Geneesmiddelen). It is not registered or marketed in the Netherlands. No RVG numbers are on record.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information. Full SmPC data for Didanosine can be accessed via the EMA product registry or the originating regulatory authority's database.

> **Note:** SmPC retrieval is flagged as a blocking data gap (DG001) for this Evidence Pack. The CBG-MEB/TFDA label, including warnings and contraindications, must be obtained and reviewed before any repurposing decision can progress past the initial screening stage.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The highest-ranked TxGNN prediction for Didanosine is a **veterinary disease** (feline acquired immunodeficiency syndrome in cats), which falls outside the scope of human drug repurposing for the Dutch healthcare system. All available supporting evidence consists of animal and in vitro studies (Evidence Level L4), no clinical trials are registered in any registry, and Didanosine holds zero CBG-MEB authorizations in the Netherlands.

**To proceed, the following is needed:**

- **Scope clarification**: Confirm whether veterinary indications are within the programme's remit; if not, re-rank to focus on the second-ranked human-relevant prediction (Simian Immunodeficiency Virus infection, L3, 12 publications)
- **SmPC retrieval (DG001 — Blocking)**: Obtain the full label from EMA or originating authority to complete the S1 safety screening; this is a prerequisite for any further evaluation
- **MOA data (DG002 — High)**: Query DrugBank API to formally confirm the NRTI mechanism and enable structured mechanistic analysis
- **FIV-specific pharmacology**: If veterinary application is explored, conduct dedicated in vitro susceptibility testing of FIV reverse transcriptase against ddATP to determine cross-species activity
- **Regulatory pathway assessment**: If redirected toward the SIV indication or another human indication, evaluate whether existing EMA/ICH guidelines cover a new repurposing application, and identify whether an off-label use framework or a new MAA is more appropriate for the Netherlands context
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

