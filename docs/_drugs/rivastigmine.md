---
layout: default
title: Rivastigmine
parent: 僅模型預測 (L5)
nav_order: 111
evidence_level: L5
indication_count: 1
---

# Rivastigmine
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

Using the `txgnn-pipeline` skill for context, and now generating the evaluation report from the Evidence Pack.

---

# Rivastigmine: From Alzheimer's Disease to Glaucoma

## One-Sentence Summary

Rivastigmine is a dual acetylcholinesterase (AChE) and butyrylcholinesterase (BuChE) inhibitor, globally indicated for Alzheimer's disease and Parkinson's disease dementia.
The TxGNN model predicts it may be effective for **Glaucoma** by reducing intraocular pressure (IOP) through the same cholinergic pathway used by first-line glaucoma drugs.
This prediction is currently supported by **0 clinical trials** and **3 preclinical/mechanistic publications**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Alzheimer's disease / Parkinson's disease dementia (no NL authorization on record) |
| Predicted New Indication | Glaucoma |
| TxGNN Prediction Score | 99.27% |
| Evidence Level | L4 |
| NL Market Status | Not Registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Rivastigmine is a carbamate-type inhibitor that simultaneously blocks AChE and BuChE. In its approved indication — Alzheimer's disease — it raises acetylcholine levels in the brain synaptic cleft to slow cognitive decline. Crucially, AChE is also expressed in the anterior segment of the eye, specifically in the ciliary body and the trabecular meshwork. Inhibiting AChE at these sites causes local acetylcholine to accumulate in the same way it does in the brain.

This surplus acetylcholine activates M3 muscarinic receptors in the ciliary muscle and trabecular meshwork, stimulating ciliary muscle contraction and widening of the trabecular meshwork channels. The net result is increased aqueous humor outflow and a measurable reduction in intraocular pressure (IOP). This is mechanistically the same drug class as Pilocarpine, an EMA/FDA-approved first-line therapy for glaucoma — making the TxGNN prediction highly plausible from a pharmacological standpoint.

The central translational hurdle is the route of administration. All currently approved Rivastigmine products worldwide are systemic formulations (transdermal patch and oral capsule). Ophthalmic use would require developing a dedicated topical eye drop, which sidesteps blood–brain barrier concerns but necessitates new local bioavailability and safety data. A 2000 rabbit study (PMID 10673128) already demonstrated that topically applied rivastigmine lowers IOP in normotensive animals, providing direct proof-of-concept for this approach.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | Animal Study (Rabbit) | J Ocular Pharmacol Ther | Topical rivastigmine lowered IOP in normotensive conscious rabbits over an 8-hour period — direct proof-of-concept for ophthalmic application of a selective AChE inhibitor |
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | Systems Genetics / Molecular Modeling | Frontiers in Molecular Biosciences | Multi-method analysis confirms M3 muscarinic receptor activation in the anterior eye segment regulates IOP via the trabecular meshwork; identifies mechanistic basis supporting AChE inhibitors as IOP-lowering candidates |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | Patent Literature Review | Expert Opinion on Therapeutic Patents | Comprehensive review of AChE inhibitor patents (2012–2015) confirms glaucoma as an established therapeutic application alongside Alzheimer's disease; mild AChE inhibition is distinguished from toxic strong inhibition |

---

## Netherlands Market Information

No CBG-MEB marketing authorizations for Rivastigmine are recorded in the current dataset (total licenses: 0, market status: not registered).

> **Verification recommended:** Rivastigmine (Exelon®) holds EMA central authorization and is commercially available across EU member states including the Netherlands. The absence of NL-specific records likely reflects a data pipeline gap rather than a true lack of market access. The CBG-MEB register should be consulted directly to confirm the current authorization status before any regulatory assessment proceeds.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for complete safety information.

> No contraindication, key warning, or drug interaction data was available in the current Evidence Pack. Before any clinical application, the Exelon® SmPC (available via the EMA product database) must be reviewed — with particular attention to cholinergic class effects such as nausea, vomiting, bradycardia, and bronchospasm, all of which carry heightened relevance in an ophthalmic context where systemic absorption via the nasolacrimal duct remains possible even with topical formulations.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between Rivastigmine and IOP reduction is scientifically sound and sits within the same drug class as an approved glaucoma therapy, but all current evidence remains at the preclinical/mechanistic level (L4) — one animal model study and two mechanistic/review publications — with no human clinical trial data whatsoever. In addition, the NL market authorization data gap prevents a complete regulatory assessment under the CBG-MEB framework.

**To proceed, the following is needed:**

- **Clinical evidence:** At minimum one Phase 1/2 human study evaluating topical rivastigmine for IOP reduction — this is the single most critical evidence gap
- **Formulation development:** A dedicated topical ophthalmic formulation (eye drop) must be developed and characterized for local bioavailability, stability, and tolerability, since existing approved products are systemic
- **Safety dossier:** Full SmPC review (contraindications, warnings, drug interactions) including assessment of systemic cholinergic risk from ocular absorption
- **NL regulatory status:** Verify current CBG-MEB authorization status directly; if Exelon® is centrally authorized via EMA, the existing SmPC may already satisfy part of the safety review requirement
- **MOA documentation:** Formal mechanism of action data from DrugBank to complete the evidence package for regulatory submission
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

