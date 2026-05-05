---
layout: default
title: Famciclovir
parent: 僅模型預測 (L5)
nav_order: 66
evidence_level: L5
indication_count: 9
---

# Famciclovir
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

# Famciclovir: From Herpes Zoster to Post-Infectious Neuralgia

## One-Sentence Summary

Famciclovir (Famvir®) is an oral antiviral prodrug approved in multiple jurisdictions (US, EU, Japan) for herpes zoster (shingles) and herpes simplex virus infections, though it currently holds no CBG-MEB marketing authorization in the Netherlands.
The TxGNN model predicts it may be effective for **post-infectious neuralgia** (top-ranked prediction, score 99.75%),
with **2 clinical trials** identified — neither directly investigating famciclovir for this indication — and **no supporting literature**, placing current evidence at Level L4.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No NL authorization on record; globally approved for Herpes Zoster / Herpes Simplex Virus infections |
| Predicted New Indication | Post-Infectious Neuralgia |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L4 |
| NL Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known clinical information, Famciclovir is the oral prodrug of penciclovir — a nucleoside analogue that inhibits viral DNA polymerase, specifically targeting varicella-zoster virus (VZV) and herpes simplex virus (HSV). After oral administration, it undergoes rapid first-pass conversion to penciclovir, which is phosphorylated by viral thymidine kinase to its active triphosphate form, thereby blocking VZV/HSV DNA replication.

Post-infectious neuralgia — in particular postherpetic neuralgia (PHN) — is the most prevalent and debilitating complication of herpes zoster, arising from persistent VZV-induced nerve damage long after the acute rash resolves. The mechanistic link is indirect but biologically coherent: early antiviral treatment during the acute herpes zoster episode is well established to reduce the incidence and severity of PHN by curtailing viral replication and limiting neuronal inflammation. This positions Famciclovir as a **preventive** agent against post-infectious neuralgia rather than a treatment for already-established PHN.

This distinction carries clinical weight: once PHN is established, antiviral drugs have limited therapeutic value, and pain management shifts to agents such as gabapentin, pregabalin, and tricyclic antidepressants. The TxGNN model likely captures the strong biological co-occurrence of VZV infection and neuropathic sequelae within the knowledge graph, but the clinical evidence for famciclovir specifically treating existing post-infectious neuralgia remains absent. Dedicated clinical investigation is needed to establish whether this prediction translates to a meaningful new indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | NA | Unknown | 140 | Evaluates early oxycodone (opioid analgesic) during acute herpes zoster for PHN prevention; not famciclovir-specific, but confirms PHN prevention is an active unmet need in the field |
| [NCT06798662](https://clinicaltrials.gov/study/NCT06798662) | NA | Not Yet Recruiting | 120 | Compares liposomal bupivacaine vs ropivacaine nerve block combined with pulse radiofrequency for acute herpes zoster pain; interventional pain management approach, no antiviral component |

> **Important note:** Neither trial directly investigates famciclovir for post-infectious neuralgia. Both trials address pain management strategies (opioid analgesia and nerve block), not antiviral repurposing. This limits their relevance to a Grade C level for the present evaluation.

---

## Literature Evidence

Currently no related literature available for famciclovir specifically in post-infectious neuralgia.

---

## Netherlands Market Information

Famciclovir currently holds **no CBG-MEB marketing authorization** in the Netherlands. No registered products, dosage forms, or approved indications are on record for this jurisdiction.

> **Regulatory context:** Famciclovir (Famvir®) is authorized in multiple other jurisdictions — including by the FDA (US), EMA/EU, and PMDA (Japan) — for herpes zoster and herpes simplex indications. The absence of a Dutch CBG-MEB license reflects current market availability rather than a lack of global regulatory support. Any repurposing pathway in the Netherlands would first require establishing a primary marketing authorization, or leveraging a centralized EMA procedure if applicable.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for complete safety information. No warnings, contraindications, or drug interaction data were available in this Evidence Pack.

> For reference, the EMA SmPC for Famvir® (famciclovir) is the authoritative source for the Netherlands context. Key known considerations from global SmPCs include renal dose adjustment (reduced doses required for creatinine clearance < 60 mL/min), caution in severe hepatic impairment, and common adverse effects such as headache and nausea. These should be verified against the current SmPC before clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although a plausible mechanistic connection exists between VZV-driven nerve damage and post-infectious neuralgia, no clinical trials or published literature directly evaluate famciclovir for treating established post-infectious neuralgia, placing this prediction at L4 (mechanistic inference only). Proceeding without targeted evidence would not meet CBG-MEB evidentiary standards.

**To proceed, the following is needed:**

- **Clarify the clinical question:** Is the intended use (a) *prevention* of PHN via early acute-phase famciclovir treatment, or (b) *treatment* of established post-infectious neuralgia? These require fundamentally different trial designs and have different evidentiary bases.
- **Mine existing herpes zoster RCT data:** Several completed famciclovir Phase 3 trials (e.g., NCT01327144 for herpes zoster) likely report PHN incidence as a secondary endpoint — these should be systematically reviewed before initiating new studies.
- **Complete MOA documentation:** Query DrugBank API (DB00426) to obtain full mechanism of action, pharmacokinetic profile, and toxicity data.
- **Retrieve NL SmPC and safety data:** Extract warnings and contraindications from the EMA Famvir® SmPC; assess DDI profile via the relevant Dutch pharmacovigilance database.
- **Assess regulatory pathway:** Determine whether a CBG-MEB national application, EMA mutual recognition, or centralized procedure is the appropriate route given the drug's existing EU authorization history.
- **Benchmark against authorized alternatives:** Valaciclovir and aciclovir are currently the standard of care for herpes zoster in the Netherlands; a famciclovir dossier would need to demonstrate added value over these authorized competitors.

> **Additional note — stronger evidence exists for a related indication:** Among all TxGNN predictions in this pack, **chickenpox (VZV infection, rank 7)** carries the highest evidence level (L1), supported by two completed Phase 3 RCTs directly involving famciclovir (NCT01327144; NCT00098046). If the objective is to establish famciclovir on the Dutch market, pursuing a primary authorization for VZV infection/herpes zoster — leveraging this robust clinical evidence base — would be a more defensible first step, with post-infectious neuralgia as a secondary indication hypothesis to investigate thereafter.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

