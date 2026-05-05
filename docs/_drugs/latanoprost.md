---
layout: default
title: Latanoprost
parent: 僅模型預測 (L5)
nav_order: 83
evidence_level: L5
indication_count: 10
---

# Latanoprost
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

Using `txgnn-pipeline` to confirm NL deployment context, then generating the report now.

---

# Latanoprost: From Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Latanoprost is a prostaglandin F2α (PGF2α) analogue, internationally established as a first-line treatment for open-angle glaucoma and ocular hypertension by lowering intraocular pressure (IOP) via the FP receptor pathway.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**, with **1 completed clinical trial** and **no published literature** currently supporting this direction.
This represents an indication extension into a paediatric/genetic glaucoma subtype rather than a classical drug repurposing, given the highly overlapping underlying mechanism.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Glaucoma / Ocular Hypertension (not registered in the Netherlands; based on international drug profile) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| NL Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Latanoprost acts as a selective agonist at the prostaglandin F2α (FP) receptor located in the ciliary body. By activating this receptor, it increases uveoscleral outflow of aqueous humour, thereby reducing IOP. This mechanism is well-established and forms the pharmacological basis for its use as a first-line agent in open-angle glaucoma and ocular hypertension across most international guidelines.

Primary hereditary glaucoma — encompassing primary congenital glaucoma (PCG) and juvenile open-angle glaucoma (JOAG) — involves structurally impaired aqueous humour outflow, most commonly due to developmental abnormalities of the trabecular meshwork. The core pathophysiology (elevated IOP from outflow obstruction) is mechanistically identical to the adult-onset forms for which Latanoprost is already used. This makes the pharmacological rationale for IOP-lowering therapy in hereditary glaucoma highly credible.

This prediction is therefore better characterised as an **indication extension** (into a genetic/paediatric subtype) rather than a conventional repurposing scenario. An important caveat is that specific mutations associated with primary hereditary glaucoma — particularly in the *MYOC* and *CYP1B1* genes — may modulate trabecular meshwork biology and potentially influence the magnitude of the prostaglandin analogue response. Genotype-stratified efficacy data are still limited.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | Completed | 37 | Assessed the IOP-lowering effect and safety of a prostaglandin analogue (latanoprost class) versus dorzolamide (a carbonic anhydrase inhibitor) in paediatric glaucoma patients who were refractory to surgical procedures. The protocol was later amended to target 68 eyes from 34–68 patients. Trial ran from July 2009 to November 2016. |

---

## Literature Evidence

Currently no related literature available.

---

## Netherlands Market Information

Latanoprost holds **no marketing authorisation** issued by CBG-MEB and is not commercially available in the Netherlands. No Dutch SmPC or PIL is on record.

> **Note for practitioners:** Latanoprost is available in other EU member states under brand names such as **Xalatan®** (Pfizer), which holds a centralised EMA authorisation. For use in the Netherlands, access would require one of the following pathways:
> - Off-label prescribing with documented informed consent
> - Named-patient / compassionate use programme via CBG-MEB
> - Import under Article 3(1) of Directive 2001/83/EC

---

## Safety Considerations

No safety data (key warnings, contraindications, or drug interactions) was captured in this Evidence Pack for Latanoprost.

Please refer to the **SmPC (Summary of Product Characteristics)** for safety information. In the absence of a Dutch SmPC, consult the EMA-approved Xalatan® SmPC or the originator country product information. Particular attention is warranted for paediatric use, including iris pigmentation changes, local ocular tolerability, and systemic absorption in small children.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is strong — primary hereditary glaucoma shares the same IOP-driven pathophysiology as adult-onset glaucoma, and at least one completed Phase 2 trial provides direct clinical evidence for prostaglandin analogues in this paediatric/genetic subtype. However, the drug is not registered in the Netherlands, and paediatric-specific safety and genotype-stratified efficacy data remain incomplete.

**To proceed, the following is needed:**

- Retrieve and review the full results of **NCT01527682** (Phase 2, completed 2016) — efficacy endpoints, IOP reduction magnitude, and adverse event profile in paediatric patients
- Conduct a broader literature search for Latanoprost and topical prostaglandin analogues specifically in primary congenital glaucoma and JOAG (search terms beyond the current query scope)
- Obtain SmPC from EMA or originator source (Xalatan®) to complete the safety assessment — key warnings, contraindications, and drug interactions
- Clarify whether *MYOC* or *CYP1B1* genotype influences response to prostaglandin analogue therapy
- Determine the applicable regulatory pathway for use in the Netherlands (CBG-MEB off-label use, named-patient import, or magistral preparation)
- Develop a paediatric-specific safety monitoring plan covering: IOP surveillance, iris and periorbital pigmentation changes, systemic β-adrenergic-like effects, and long-term structural outcomes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

