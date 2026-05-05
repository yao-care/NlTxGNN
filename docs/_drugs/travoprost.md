---
layout: default
title: Travoprost
parent: 僅模型預測 (L5)
nav_order: 120
evidence_level: L5
indication_count: 10
---

# Travoprost
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

Using **txgnn-pipeline** context noted. Now generating the evaluation report based on the Evidence Pack.

---

# Travoprost: From Open-Angle Glaucoma to Visceral Calciphylaxis

## One-Sentence Summary

Travoprost is a prostaglandin FP receptor agonist used clinically for reducing intraocular pressure in open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **Visceral Calciphylaxis**,
with **0 clinical trials** and **0 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma / Ocular hypertension (derived from clinical trial data; no CBG-MEB marketing authorisation on file) |
| Predicted New Indication | Visceral Calciphylaxis |
| TxGNN Prediction Score | 99.9998% |
| Evidence Level | L5 |
| NL Market Status | Not marketed in the Netherlands |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacological information, Travoprost is a selective prostaglandin FP receptor agonist. Its efficacy in reducing intraocular pressure in open-angle glaucoma and ocular hypertension has been well established across multiple Phase 3–4 clinical trials. The primary mechanism involves enhanced uveoscleral aqueous outflow via FP receptor stimulation, with a secondary vasodilatory effect responsible for the characteristic conjunctival hyperaemia observed clinically.

Visceral calciphylaxis (calcific uraemic arteriolopathy) is a distinct pathological entity characterised by medial calcification and thrombotic occlusion of small cutaneous and visceral vessels. It occurs most commonly in end-stage renal disease patients and involves dysregulated calcium-phosphate homeostasis, vascular smooth muscle transdifferentiation into osteoblast-like cells, and thrombotic microangiopathy. None of these mechanisms are known targets of the prostaglandin FP receptor pathway.

The exceptionally high TxGNN score (>99.99%) most likely reflects a knowledge graph topology artefact: Travoprost shares broad "vascular" and "prostaglandin" graph nodes with calciphylaxis through intermediate graph connections, rather than a direct mechanistic or clinical relationship. The Evidence Pack's own repurposing rationale notes this prediction "may arise from propagation bias at generalised vascular nodes." No published literature or registered clinical trial currently supports this repurposing direction.

---

## Clinical Trials

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Netherlands Market Information

Travoprost currently holds **no marketing authorisation** issued by the CBG-MEB (College ter Beoordeling van Geneesmiddelen) in the Netherlands. No RVG number has been assigned. The drug is therefore not commercially available through standard Dutch distribution channels.

For regulatory reference, travoprost-containing ophthalmic solutions (e.g., Travatan®, Travatan Z®) have received marketing authorisations in other EU member states via national procedures. The corresponding SmPC (Samenvatting van de Productkenmerken) from those authorisations — in particular the warnings, contraindications, and special populations sections — should be consulted as the primary safety reference.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information. No key warnings, contraindications, or drug interaction data are currently available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial evidence, no supporting literature, and no established mechanistic rationale linking Travoprost's FP receptor pathway to visceral calciphylaxis. The high TxGNN score is most plausibly attributable to knowledge graph propagation bias through shared vascular ontology nodes rather than a genuine biological signal.

**To proceed, the following would be needed:**

- **Mechanistic hypothesis generation**: Identify any plausible biological pathway connecting prostaglandin FP receptor activation to vascular calcification or thrombotic microangiopathy (e.g., via TGF-β, Wnt/β-catenin, or inflammation-mediated calcification pathways).
- **Preclinical evidence**: In vitro or animal model data demonstrating an effect of FP receptor agonism on vascular calcification or calciphylaxis lesion progression before any clinical consideration.
- **Safety profile retrieval**: Obtain the full SmPC from an EU member state authorisation to assess systemic exposure risk, contraindications, and relevant warnings — particularly given that calciphylaxis patients typically have severe renal impairment, which may substantially affect drug clearance and tolerability.
- **CBG-MEB marketing authorisation status**: Confirm whether an EU centralised or mutual recognition procedure has been filed; if not, a de novo authorisation pathway would be required before any Dutch clinical use.
- **Reassessment of TxGNN ranking**: Investigate whether the prediction score persists after correcting for vascular node degree bias; a robust score post-correction would warrant escalation to L4 preclinical exploration.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

