---
layout: default
title: Tropicamide
parent: 僅模型預測 (L5)
nav_order: 122
evidence_level: L5
indication_count: 3
---

# Tropicamide
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

Using the `txgnn-pipeline` skill to confirm context — the NlTxGNN project targets the Netherlands CBG-MEB framework. The skill confirms standard workflow applies. Proceeding to generate the report from the Evidence Pack.

---

# Tropicamide: From Ophthalmology (Mydriasis) to Cauda Equina Syndrome

## One-Sentence Summary

Tropicamide is a well-established antimuscarinic (anticholinergic) agent, primarily used in ophthalmology to induce pupil dilation (mydriasis) and temporary paralysis of accommodation (cycloplegia) during eye examinations.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**,
with **0 clinical trials** and **0 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No CBG-MEB authorization on record; classically used for ophthalmic mydriasis/cycloplegia |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| NL Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on established pharmacological knowledge, Tropicamide is a competitive antagonist at muscarinic acetylcholine receptors — particularly M3 and M4 subtypes. When applied topically to the eye, this antimuscarinic action relaxes the iris sphincter and ciliary muscle, producing mydriasis and cycloplegia. Beyond ophthalmology, antimuscarinic agents are pharmacologically active across the autonomic nervous system, influencing smooth muscle tone in the bladder, bowel, and other visceral organs.

Cauda equina syndrome (CES) is a serious neurological emergency caused by compression of the lumbosacral nerve root bundle. A hallmark feature of CES is disruption of the autonomic pathways governing micturition (urination), defecation, and sexual function — areas precisely where muscarinic receptor modulation is pharmacologically relevant. Anticholinergic drugs are already established in managing neurogenic bladder dysfunction, a frequent sequela of CES. TxGNN may therefore be detecting a mechanistic overlap between Tropicamide's receptor profile and the autonomic dysfunction component of CES, rather than a direct effect on nerve root compression itself.

That said, CES is primarily a structural/surgical condition: nerve root decompression remains the cornerstone of treatment. Tropicamide's utility would, at most, address symptomatic autonomic complications rather than the underlying pathology. The high TxGNN score likely reflects a graph-neighbourhood association through shared autonomic pathway nodes. Without clinical evidence, this prediction should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Netherlands Market Information

Tropicamide currently holds no marketing authorizations issued by the CBG-MEB (College ter Beoordeling van Geneesmiddelen) and is not commercially available on the Dutch market according to this Evidence Pack. No RVG numbers are on record.

> **Note for reviewers:** Tropicamide ophthalmic solutions are widely authorized across EU member states under various brand names. A dedicated CBG-MEB registry search is recommended to verify whether any mutual recognition or decentralized procedure authorizations exist that may not yet be captured in this dataset.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information. Key warnings, contraindications, and drug interaction data are not available in the current Evidence Pack and must be retrieved from the CBG-MEB/EMA product dossier or TFDA SmPC PDF before this candidate can advance to a formal safety screening stage.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base sits at Level L5 — the lowest tier, consisting solely of a TxGNN model prediction with no supporting clinical trials or published literature. Combined with zero Dutch market authorizations and unresolved data gaps in both mechanism of action and safety data, there is insufficient information to support any further recommendation at this stage.

**To proceed, the following is needed:**

- **MOA verification:** Retrieve full DrugBank entry (DB00809) to confirm receptor targets, pharmacodynamics, and known off-target effects
- **SmPC review:** Download and parse the relevant SmPC (EMA or national CBG-MEB) for key warnings, contraindications, and special population precautions
- **DDI assessment:** Re-query drug interaction databases once SmPC data is available
- **Indication disambiguation:** Clarify whether the TxGNN prediction targets CES itself, or its autonomic sequelae (e.g., neurogenic bladder); the latter has much stronger pharmacological plausibility
- **Targeted literature search:** Broaden PubMed query beyond exact disease match — search for "tropicamide autonomic neuropathy", "anticholinergic neurogenic bladder cauda equina", and related terms
- **NL market status verification:** Confirm via CBG-MEB public register whether any ophthalmic Tropicamide products hold an RVG number under mutual recognition procedures
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

