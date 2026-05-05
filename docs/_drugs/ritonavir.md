---
layout: default
title: Ritonavir
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L5
indication_count: 3
---

# Ritonavir
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

Using `txgnn-pipeline` skill noted. The skill confirms standard TxGNN pipeline workflow. Now generating the Netherlands healthcare evaluation report from the Evidence Pack.

---

# Ritonavir: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Ritonavir is a protease inhibitor developed for HIV-1 treatment, also widely used as a pharmacokinetic booster in combination antiretroviral regimens.
The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome (FIV)**, with **0 directly relevant clinical trials** and **0 publications** currently supporting this specific direction.
The one retrieved clinical trial was misclassified by the data pipeline and does not constitute supporting evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV infection (NL regulatory record unavailable; based on established drug class context from repurposing rationale) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV) |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| NL Market Status | Not registered in the Netherlands |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this Evidence Pack. Based on the mechanistic context documented in the repurposing rationale, Ritonavir is an HIV-1 protease inhibitor that blocks viral polyprotein processing, thereby halting viral replication. It is also a potent CYP3A4 inhibitor, widely co-administered as a pharmacokinetic booster to enhance the plasma exposure of partner antiretrovirals.

FIV (Feline Immunodeficiency Virus) and HIV-1 are both members of the lentivirus subfamily, and their proteases share partial structural homology. This biological relationship provides the mechanistic basis for the TxGNN model's prediction: if Ritonavir can inhibit the HIV-1 protease, it may theoretically exert activity against the structurally related FIV protease. In vitro susceptibility data have demonstrated that HIV protease inhibitors can inhibit FIV protease to some degree.

However, clinical translation is substantially limited for two reasons. First, FIV protease has different substrate specificity from HIV-1 protease, and inhibitors optimised for HIV-1 are not expected to achieve equivalent in vivo efficacy against FIV. Second, and more fundamentally, **FIV is a veterinary indication** — the regulatory pathway for veterinary medicines in the Netherlands falls under NVWA/Vet-MEB, which is entirely separate from the human medicines authority (CBG-MEB). This prediction therefore lies outside the scope of the Dutch human healthcare system and cannot progress through the standard human drug repurposing review track.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | ⚠️ **Misclassified — not relevant to FIV.** This trial compares Ritonavir-boosted Darunavir + Lamivudine versus standard dual/triple regimens in ARV-naïve **human** HIV-1-infected adults. Ritonavir serves as a pharmacokinetic booster here, not a direct antiviral agent against feline lentivirus. The pipeline retrieved this trial by incorrectly matching the keyword "boosted (Ritonavir-boosted)" to the feline AIDS query. This trial contributes zero evidentiary weight for the FIV indication. |

---

## Literature Evidence

Currently no related literature directly supporting Ritonavir use in Feline Acquired Immunodeficiency Syndrome is available.

---

## Netherlands Market Information

Ritonavir is not currently registered in the Netherlands according to this Evidence Pack. No CBG-MEB marketing authorizations are on record.

> **Reviewer note:** Ritonavir (Norvir®) holds EMA centralised marketing authorisation and is commercially available across EU member states. There is a discrepancy between this dataset and expected market reality. Reviewers should confirm the current authorisation status directly via the [CBG-MEB public register](https://www.cbg-meb.nl) or the [EMA product database](https://www.ema.europa.eu) before drawing any regulatory conclusions.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information.

> Ritonavir is a potent CYP3A4 and CYP2D6 inhibitor with one of the broadest drug–drug interaction profiles among approved medicines. Formal DDI data and contraindications were not captured in this Evidence Pack. Clinical reviewers should consult the full EMA SmPC and a validated drug interaction database (e.g., Liverpool HIV Interactions, Lexicomp) before any prescribing or protocol decision, particularly in patients receiving statins, anticoagulants, antifungals, immunosuppressants, or QT-prolonging agents.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN-predicted indication for Ritonavir is a **veterinary condition** (FIV / Feline AIDS), which falls entirely outside the scope of the Netherlands human healthcare and medicines evaluation framework administered by CBG-MEB. The sole retrieved clinical trial was a pipeline misclassification and provides no valid evidence; no supporting literature exists for this specific indication.

**To proceed, the following is needed:**

- **Pipeline correction:** Implement a veterinary-indication filter in the TxGNN prediction pipeline to exclude animal-only diseases (FIV, etc.) from human drug repurposing reports for CBG-MEB review.
- **Prioritise next-ranked indications:** Consider re-initiating review against **Rank 2 — Simian Immunodeficiency Virus infection (L3, Research Question)**, which has 12 peer-reviewed publications supporting mechanistic and in vivo plausibility in non-human primate models.
- **MOA data retrieval:** Obtain Ritonavir's complete mechanism of action from DrugBank (DB00503) to support any future mechanistic-link analysis.
- **SmPC safety retrieval:** Download and parse the EMA SmPC for Ritonavir to populate warnings, contraindications, and DDI sections prior to any S1 safety screen.
- **Market status verification:** Reconcile the "not registered" dataset status against known EMA centralised authorisation to confirm current CBG-MEB availability.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

