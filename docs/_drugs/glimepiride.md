---
layout: default
title: Glimepiride
parent: 僅模型預測 (L5)
nav_order: 74
evidence_level: L5
indication_count: 9
---

# Glimepiride
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

Using the `txgnn-pipeline` skill to guide report generation for the NL deployment context. Now producing the evaluation report based on the Evidence Pack.

---

# Glimepiride: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

Glimepiride is a third-generation sulfonylurea antidiabetic agent, established for the treatment of type 2 diabetes mellitus in adults.
The TxGNN model predicts it may be effective for **Focal Stiff Limb Syndrome** (prediction score: 99.75%), yet **no clinical trials** and **no supporting publications** for this indication currently exist.
The prediction remains model-driven only (Evidence Level L5), and independent preclinical and clinical verification is required before any further consideration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus (no CBG-MEB marketing authorisation on record for the Netherlands) |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| NL Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on established pharmacological knowledge, Glimepiride belongs to the third-generation sulfonylurea class. Its glucose-lowering efficacy is achieved by binding to the SUR1 subunit of ATP-sensitive potassium (K_ATP) channels on pancreatic β-cells, causing channel closure, membrane depolarisation, and subsequent insulin secretion. It also carries a weak partial agonist activity at PPAR-γ, which contributes modestly to insulin sensitisation.

Focal Stiff Limb Syndrome is a rare autoimmune neurological disorder in which anti-GAD65 antibodies selectively impair GABAergic inhibitory interneurons in the spinal cord, producing focal involuntary muscle rigidity. The mechanistic bridge to Glimepiride is indirect: SUR1 (ABCC8) — the sulfonylurea receptor — is expressed not only in pancreatic β-cells but also in central neurons, including GABAergic interneurons. In theory, modulating neuronal K_ATP channel activity could influence membrane excitability and downstream GABA-mediated inhibition, potentially counteracting the hyperexcitability seen in stiff limb syndrome.

However, this connection is highly speculative. No in vitro or in vivo data support sulfonylurea use in GABAergic or autoimmune neurological conditions. The TxGNN high score most likely reflects a structural knowledge-graph artefact: GAD65 is expressed in both pancreatic islets (where it participates in GABA synthesis for paracrine signalling) and spinal inhibitory neurons, creating a shared graph node that inflates co-association scores. This is a recognised false-positive risk pattern in graph neural network drug repurposing, and should be interpreted with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Netherlands Market Information

Glimepiride currently holds **no marketing authorisation** with the CBG-MEB (College ter Beoordeling van Geneesmiddelen) in the Netherlands. No RVG numbers are on record. Any clinical use in the Netherlands would require an off-label or named-patient basis, subject to applicable Dutch and EMA regulatory procedures.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics / Samenvatting van de Productkenmerken) for complete safety information, including key warnings, contraindications, and drug–drug interaction data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.75%), this score is most likely driven by knowledge-graph topology — specifically the dual expression of GAD65 in pancreatic and neuronal tissue — rather than genuine biological plausibility. With zero supporting clinical trials, zero relevant publications, and a purely speculative mechanistic link, there is insufficient basis to advance this candidate for the Netherlands healthcare context at this stage.

**To proceed, the following is needed:**
- Preclinical in vitro and/or in vivo data demonstrating that sulfonylurea-class K_ATP channel modulation produces measurable effects on spinal GABAergic interneuron excitability
- Expert review by a neuropharmacologist and a neurologist specialised in autoimmune movement disorders to assess genuine biological plausibility
- Formal investigation of whether the TxGNN prediction reflects a GAD65 knowledge-graph structural artefact (false-positive triage)
- Full SmPC retrieval and review for Glimepiride to establish the safety profile, including key warnings, contraindications, and major drug interactions relevant to any future trial design
- Regulatory pathway consultation with CBG-MEB regarding the absence of NL marketing authorisation and any named-patient or compassionate-use options should preclinical evidence emerge
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

