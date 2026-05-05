---
layout: default
title: Iohexol
parent: 僅模型預測 (L5)
nav_order: 79
evidence_level: L5
indication_count: 2
---

# Iohexol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

Using the `txgnn-pipeline` skill for context. Now I'll generate the evaluation report based on the Evidence Pack. This case involves Iohexol (a radiological contrast agent) with TxGNN predictions for insomnia and anxiety — both flagged as L5/Hold with false-positive evidence matches. I'll apply the report format accordingly.

---

# Iohexol: From Radiological Contrast Agent to Insomnia

## One-Sentence Summary

Iohexol is a non-ionic iodinated contrast medium used in radiological imaging procedures (CT, myelography, angiography), functioning purely through physical X-ray absorption rather than pharmacodynamic activity.
The TxGNN model predicts it may be effective for **Insomnia**, with **0 clinical trials** and **0 publications** directly supporting this direction.
A secondary prediction for **Anxiety** (rank 2, score 99.25%) was also retrieved, but all associated evidence represents confirmed false-positive matches where Iohexol served as a GFR measurement tool or guiding contrast agent — not as a therapeutic agent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Radiological contrast agent (X-ray, CT, myelography, angiography) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| NL Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, Iohexol is a non-ionic, water-soluble iodinated contrast medium. Its sole pharmacological mechanism is **physical**: the high iodine content absorbs X-rays, enhancing radiological image contrast in target tissues. It has no established receptor-binding activity, no central nervous system pharmacodynamics, and no known interaction with any pathway implicated in sleep regulation.

Insomnia involves dysregulation of GABA-A receptors, adenosine signalling, melatonin pathways, and the hypothalamic–pituitary–adrenal (HPA) axis. Iohexol has no known activity at any of these targets. The TxGNN analysis itself acknowledges this explicitly: the high prediction score most likely reflects **knowledge graph noise** — for example, spurious associations between iodinated compound nodes and protein nodes unrelated to sleep biology — rather than a genuine biological signal.

There is no mechanistic bridge between contrast agent use and insomnia pathophysiology. Unlike cases where a drug's known mechanism plausibly extends to a new indication (e.g., a kinase inhibitor repurposed across tumour types), Iohexol's mechanism is entirely physical and indication-agnostic. This prediction requires a biologically plausible hypothesis before any further evaluation is warranted.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Iohexol in insomnia.

> **Note on secondary indication — Anxiety (Rank 2):** Six clinical trials were retrieved but all are confirmed false positives (relevance grade C). In each case, Iohexol appeared in the study context either as a **GFR measurement tool** (iohexol plasma clearance technique) or as an **imaging contrast agent** for procedural guidance — not as the investigational therapeutic. Anxiety appeared only as a comorbidity measure or adverse event category, not as a primary endpoint being treated. Representative examples:
>
> | Trial | Role of Iohexol | Why It Is a False Positive |
> |-------|----------------|---------------------------|
> | [NCT01053130](https://clinicaltrials.gov/study/NCT01053130) | GFR measurement tool | Bariatric surgery/CKD study; anxiety not a treatment target |
> | [NCT01629537](https://clinicaltrials.gov/study/NCT01629537) | Guiding contrast for stellate ganglion block | Treatment is nerve block, not Iohexol; PTSD/anxiety as endpoint |
> | [NCT03736005](https://clinicaltrials.gov/study/NCT03736005) | GFR measurement tool | Critical illness/muscle wasting study; anxiety not an endpoint |

---

## Literature Evidence

Currently no related literature available for Iohexol in insomnia.

> **Note on secondary indication — Anxiety (Rank 2):** Six publications were retrieved but all represent false-positive associations. Anxiety or mental symptoms appear incidentally — as side effects of myelography (PMID [2352635](https://pubmed.ncbi.nlm.nih.gov/2352635/)), as procedural discomfort descriptors (PMID [8883531](https://pubmed.ncbi.nlm.nih.gov/8883531/)), or as patient-reported outcomes in imaging studies — not as a therapeutic target of Iohexol.

---

## Netherlands Market Information

Iohexol currently holds **no marketing authorization** registered with the CBG-MEB in the Netherlands. No RVG number, SmPC, or PIL is available through the Dutch regulatory database.

> For reference: Iohexol-containing products (e.g., Omnipaque®) hold authorizations in other EU member states. A decentralized procedure (DCP) or mutual recognition procedure (MRP) pathway would need to be separately verified for any Netherlands-specific authorization.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information. No warnings, contraindications, or drug interaction data were available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a pure model prediction (L5 evidence) with zero supporting clinical trials or literature for insomnia, and all retrieved evidence for the secondary indication (anxiety) consists of confirmed false-positive matches. Iohexol has no pharmacodynamic mechanism relevant to any neurological or psychiatric indication; the high TxGNN score is best explained by knowledge graph artifacts rather than a genuine repurposing signal.

**To proceed, the following is needed:**

- A biologically plausible hypothesis linking iohexol or iodinated contrast media to sleep or anxiety regulation — none currently exists in the published literature
- A knowledge graph quality audit to investigate why Iohexol scores highly for CNS indications (potential node mis-association in the TxGNN graph)
- Any preclinical (in vitro / in vivo) evidence of CNS-modulating effects before clinical consideration
- Confirmation of Dutch market authorization status via CBG-MEB or EMA centralized procedure review if future development is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

