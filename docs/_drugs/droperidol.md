---
layout: default
title: Droperidol
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 10
---

# Droperidol
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

Using the `txgnn-pipeline` skill to confirm context. Now generating the Netherlands drug repurposing evaluation report.

---

# Droperidol: From Acute Agitation to Tourette Syndrome

## One-Sentence Summary

Droperidol is a butyrophenone antipsychotic historically used for managing acute agitation, psychomotor sedation, and perioperative premedication.
The TxGNN model predicts it may be effective for **Tourette Syndrome**, with **0 clinical trials** and **1 publication** currently supporting this specific direction.
The single available reference addresses haloperidol — a structurally related butyrophenone — rather than droperidol itself, making direct evidence for this repurposing candidate very limited.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in the Netherlands; internationally used for acute agitation and perioperative sedation |
| Predicted New Indication | Tourette Syndrome |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 |
| NL Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, droperidol belongs to the butyrophenone class and acts as a potent dopamine D2 receptor antagonist — the same pharmacological class as haloperidol. Its clinical utility in acute agitation and psychosis has been established, and mechanistically this may be applicable to Tourette syndrome.

Tourette syndrome is a neurodevelopmental disorder driven by dysregulation of the dopaminergic system, particularly hyperactivation of striatal D2 receptors, which produces the characteristic motor and vocal tic phenotype. Haloperidol — also a butyrophenone D2 antagonist — is one of the cornerstone pharmacological treatments for tic suppression, providing the pharmacological bridge underlying the TxGNN model's prediction for droperidol.

However, the extrapolation carries important caveats. Droperidol is almost exclusively available as an injectable formulation intended for acute, short-duration use, whereas Tourette syndrome requires long-term chronic oral therapy. The sole retrieved literature (PMID 791589) describes haloperidol in severe behaviour disorders — not droperidol in Tourette syndrome — making the evidence base indirect and mechanistic at best. The prediction score of 99.89% most likely reflects graph-level proximity in the TxGNN knowledge graph between butyrophenone compounds and dopamine-related movement disorders, rather than direct drug–disease evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for droperidol in Tourette syndrome.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [791589](https://pubmed.ncbi.nlm.nih.gov/791589/) | 1976 | Clinical Study | *Current Psychiatric Therapies* | Haloperidol in severe behaviour disorders — indirect evidence only; not droperidol-specific and not focused on tic suppression |

---

## Netherlands Market Information

Droperidol currently holds **no CBG-MEB marketing authorizations** in the Netherlands. There are no registered RVG numbers, no approved SmPC documents, and no product entries in the national medicines register. The drug is not commercially available through standard Dutch pharmacy channels.

Any future clinical application in the Netherlands would require either:
- A new marketing authorization application to the CBG-MEB or via the EMA centralized procedure, or
- Use under a named-patient / compassionate use or hospital exemption framework.

---

## Safety Considerations

Please refer to the SmPC (Samenvatting van de Productkenmerken) for safety information. No warning, contraindication, or drug interaction data was available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for droperidol in Tourette syndrome is at L4 level — the single retrieved publication concerns a related but distinct compound (haloperidol), no droperidol-specific clinical trials exist, and the drug carries no Dutch marketing authorization, blocking any near-term clinical pathway in the Netherlands.

**To proceed, the following is needed:**

- Droperidol-specific clinical or preclinical studies targeting tic suppression in Tourette syndrome
- Formal MOA documentation from DrugBank API or current SmPC sources
- Safety review, with particular attention to QT-interval prolongation risk, prior to any trial design
- Route-of-administration feasibility assessment: an oral or transdermal formulation would be required for a chronic-use Tourette indication
- Regulatory pre-submission consultation with CBG-MEB to explore authorization pathway options
- Comparative analysis against existing approved D2 antagonists for Tourette syndrome (haloperidol, pimozide, aripiprazole) to establish a differentiation rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

