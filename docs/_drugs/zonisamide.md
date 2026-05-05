---
layout: default
title: Zonisamide
parent: 僅模型預測 (L5)
nav_order: 126
evidence_level: L5
indication_count: 10
---

# Zonisamide
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

The txgnn-pipeline skill confirms this is a report generation task for the NL deployment. The system prompt provides the complete format specification. Proceeding directly with the report.

---

# Zonisamide: From Partial Seizures to Tourette Syndrome

## One-Sentence Summary

Zonisamide is a third-generation antiepileptic drug internationally approved as adjunctive therapy for partial seizures in adults (marketed as Zonegran under EMA central authorisation).
The TxGNN model predicts it may be effective for **Tourette Syndrome**,
with **0 clinical trials** and **0 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in the Netherlands; internationally approved for adjunctive treatment of partial seizures in adults |
| Predicted New Indication | Tourette Syndrome |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| NL Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Zonisamide is a benzisoxazole sulfonamide antiepileptic drug. Its efficacy in partial and generalised seizures has been established across multiple international clinical programmes, and mechanistically it may be applicable to Tourette Syndrome through its dopaminergic and serotonergic modulatory properties — the same neurotransmitter systems targeted by first-line tic pharmacotherapy (e.g., aripiprazole, haloperidol).

Tourette Syndrome involves dysregulation of the basal ganglia–cortical dopaminergic circuit and insufficient GABAergic inhibition. Zonisamide's weak dopamine-modulating activity provides a theoretical foothold for the TxGNN prediction. However, it is important to note that this mechanistic link is indirect and speculative; no dedicated preclinical or clinical data exist to confirm tic-suppressing activity.

A significant safety concern actively undermines this prediction: a 2022 pragmatic review (PMID 36005856, *Expert Review of Neurotherapeutics*) specifically identified antiseizure medications as potential triggers or aggravators of tic disorders — the very symptoms that define Tourette Syndrome. This bidirectional risk, combined with the complete absence of supporting evidence, means the harm–benefit balance cannot currently be assessed in favour of investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Netherlands Market Information

Zonisamide currently holds **no marketing authorisations** with CBG-MEB and is not commercially available through the standard Dutch regulatory pathway.

> Clinicians requiring access to zonisamide in the Netherlands should consult the CBG-MEB regarding compassionate use or hospital exemption procedures, or verify whether the EMA-centralised authorisation for Zonegran (partial seizures indication) confers current Dutch market access.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level L5 — no clinical trials and no publications support Zonisamide for Tourette Syndrome, and a published safety signal (PMID 36005856) indicates antiseizure medications may exacerbate tic disorders, directly conflicting with the therapeutic intent.

**To proceed, the following is needed:**
- Preclinical studies in validated tic-disorder animal models to establish basic proof-of-concept
- Full MOA characterisation (via DrugBank API, flagged as Data Gap DG002) to confirm whether dopaminergic activity is sufficient and relevant for tic suppression
- Formal pharmacovigilance assessment of the antiseizure-medication–tic-exacerbation risk (PMID 36005856) for Zonisamide specifically
- CBG-MEB regulatory pathway consultation, since the drug is not registered in the Netherlands and any clinical programme would require a formal authorisation strategy
- Download and parse the SmPC/PIL (flagged as Data Gap DG001) to resolve blocking safety gaps before any S1 safety pre-assessment can be initiated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

