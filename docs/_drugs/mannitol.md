---
layout: default
title: Mannitol
parent: 僅模型預測 (L5)
nav_order: 91
evidence_level: L5
indication_count: 10
---

# Mannitol
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

Using the `txgnn-pipeline` skill to confirm context, then generating the report now based on the Evidence Pack.

---

# Mannitol: From Osmotic Diuretic to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Mannitol is a well-established osmotic diuretic used clinically for reducing intracranial pressure and promoting renal solute excretion, with no current CBG-MEB marketing authorization in the Netherlands.
The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**,
with **0 clinical trials** and **1 publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Netherlands (CBG-MEB) authorization on record; established clinical use: osmotic diuresis, intracranial pressure reduction |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| NL Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Mannitol (DB00742) is a sugar alcohol that acts as an osmotic diuretic. When administered intravenously, it increases plasma osmolality and draws free water out of cells, promoting its renal excretion through an ADH-independent mechanism. This pharmacological property is the basis for its established use in reducing cellular edema and intracranial pressure in acute clinical settings.

NSIAD is a rare X-linked disorder caused by gain-of-function mutations in the *AVPR2* gene, which encodes the vasopressin V2 receptor. Unlike nephrogenic diabetes insipidus — which results from loss-of-function of the same receptor — NSIAD involves constitutive, ligand-independent receptor activation. This leads to persistent antidiuresis and dilutional hyponatremia. Because Mannitol promotes free water excretion via an osmotic, non-ADH-dependent pathway, it could theoretically counteract this dilutional hyponatremia by transiently increasing free water output.

However, the mechanistic link is compensatory rather than targeted. Mannitol does not suppress the constitutively active AVPR2 receptor, nor does it correct the underlying gain-of-function mutation. In clinical practice, NSIAD is managed primarily with fluid restriction and oral urea, which address the pathophysiology more directly. The TxGNN prediction most likely reflects osmotic pathway overlap within the disease-drug knowledge graph, rather than a specific or novel therapeutic hypothesis for NSIAD.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Mannitol in nephrogenic syndrome of inappropriate antidiuresis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European Journal of Internal Medicine | Describes 10 common pitfalls in evaluating hyponatremic patients, including NSIAD as a diagnostic consideration. Relevant to understanding NSIAD in the differential of hyponatremia, but does not directly investigate Mannitol as a therapeutic agent for NSIAD. |

---

## Netherlands Market Information

Mannitol currently holds no CBG-MEB marketing authorization in the Netherlands. No registered products, dosage forms, or approved indications are on record. As a widely available generic compound, Mannitol may be used in hospital settings under individual clinical judgement, but formal regulatory authorization in the Netherlands is absent.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information. As Mannitol is not currently authorized in the Netherlands, consult available product information from the EMA or from equivalent national authorities in countries where Mannitol is formally registered (e.g., the United Kingdom, Germany, or the United States FDA label).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.97%), the evidence base for Mannitol in NSIAD is extremely limited — no clinical trials have been conducted, and the only available publication is a tangential review on hyponatremia evaluation. The proposed mechanistic link is indirect (transient osmotic compensation rather than targeted receptor therapy), and current NSIAD standard-of-care — fluid restriction and oral urea — is already well-established and better suited to the underlying pathophysiology.

**To proceed, the following is needed:**

- Formal mechanism of action data for Mannitol (DrugBank API query not yet completed; flagged as a High-severity data gap)
- Full safety profile including contraindications and drug-drug interactions (flagged as a Blocking data gap)
- At minimum, a case report or preclinical study specifically examining Mannitol in NSIAD or closely related AVPR2 gain-of-function models
- A clinical rationale document distinguishing the proposed use of Mannitol from established NSIAD treatments (fluid restriction, oral urea, tolvaptan)
- Regulatory consultation with CBG-MEB on whether off-label or investigational use in the Netherlands is feasible given the absence of any current NL marketing authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

