---
layout: default
title: Leflunomide
parent: 僅模型預測 (L5)
nav_order: 84
evidence_level: L5
indication_count: 2
---

# Leflunomide
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

# Leflunomide: From Rheumatoid Arthritis to Brachydactyly-Syndactyly Syndrome

---

## One-Sentence Summary

Leflunomide is a disease-modifying antirheumatic drug (DMARD) established internationally for the treatment of rheumatoid arthritis and psoriatic arthritis.
The TxGNN model predicts it may be effective for **Brachydactyly-Syndactyly Syndrome**, an ultra-rare congenital limb malformation disorder.
However, **no clinical trials or published literature** support this direction, and the mechanistic rationale identified by the knowledge graph contains a critical directional flaw that renders this a likely false positive.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid arthritis / psoriatic arthritis (established internationally; no NL authorization recorded in this dataset) |
| Predicted New Indication | Brachydactyly-Syndactyly Syndrome |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| NL Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, Leflunomide is an inhibitor of **dihydroorotate dehydrogenase (DHODH)**, the rate-limiting enzyme in de novo pyrimidine biosynthesis. By depleting intracellular pyrimidine pools, it suppresses proliferation of activated T and B lymphocytes, producing its anti-inflammatory effect in rheumatoid arthritis.

The knowledge graph (KG) likely traced the following path to generate this prediction: loss-of-function (LOF) mutations in the *DHODH* gene are known to cause **Miller syndrome**, a rare disorder characterised by acrofacial dysostosis including limb abnormalities. The KG may have established an indirect association between the DHODH gene node and brachydactyly/syndactyly phenotype nodes, giving rise to a high-confidence score.

**However, this connection represents a mechanistic direction inversion false positive.** The congenital phenotype arises from *insufficient* DHODH activity (LOF), while Leflunomide further *inhibits* DHODH — meaning the drug acts in the same direction as the underlying pathological mechanism rather than opposing it. Applying a DHODH inhibitor to treat a disorder caused by DHODH deficiency is pharmacologically counterproductive. This prediction does not carry therapeutic plausibility and should be treated as a model artefact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Netherlands Market Information

No CBG-MEB national authorization (RVG number) for Leflunomide is recorded in this dataset.

> **Note:** Leflunomide (brand name Arava) is authorized in the European Union via centralized EMA procedure. EU-wide authorizations (EU/x/xx/xxx format) may not be captured in national RVG datasets. Clinicians and pharmacists should verify current authorization and market availability directly via the **CBG-MEB product database** or the **EMA medicines portal** before drawing conclusions about NL accessibility.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information. Safety data — including key warnings, contraindications, and drug interactions — was not available in this evidence pack.

> Given that Leflunomide holds a well-established EMA authorization for rheumatoid arthritis, a current SmPC is available via the EMA website and should be consulted for any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for brachydactyly-syndactyly syndrome is a **mechanistic direction inversion false positive**: the disorder is caused by DHODH loss-of-function, while Leflunomide inhibits DHODH — the drug would exacerbate rather than correct the underlying pathophysiology. Combined with an evidence level of L5 (zero clinical trials, zero publications), there is no basis to advance this indication.

**To proceed constructively, the following is needed:**

- **Flag this prediction** as a false positive in the TxGNN pipeline; consider implementing a mechanistic directionality filter for enzyme LOF/inhibitor pairs
- **Do not initiate** any clinical or translational study for this indication without independent mechanistic re-evaluation
- **Verify NL market status** via CBG-MEB / EMA databases — Leflunomide likely holds an EU centralized authorization not captured in this national dataset
- **Retrieve SmPC** safety data (warnings, contraindications, hepatotoxicity monitoring requirements) before any clinical consideration of the drug in the Netherlands
- **If exploring Leflunomide for novel indications**, prioritize inflammatory or immune-mediated disease phenotypes where DHODH inhibition is mechanistically coherent (e.g., lupus nephritis, inflammatory bowel disease — indications with existing investigational literature)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

