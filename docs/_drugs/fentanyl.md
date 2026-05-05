---
layout: default
title: Fentanyl
parent: 僅模型預測 (L5)
nav_order: 68
evidence_level: L5
indication_count: 2
---

# Fentanyl
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

Using **txgnn-pipeline** to guide report generation.

---

# Fentanyl: From Severe Pain Management to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fentanyl is a potent μ-opioid receptor agonist widely used in clinical practice for the management of moderate-to-severe acute and chronic pain.
The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, with **0 clinical trials** and **0 publications** currently supporting this direction.
Critically, pharmacological analysis suggests this prediction is a probable false positive: the opioid–ADH pathway captured by the knowledge graph is directionally opposed to the therapeutic goal in NSIAD.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Severe pain management (opioid analgesic; no NL authorisation on record) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| NL Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Fentanyl is a high-potency μ-opioid receptor (MOR) agonist with rapid onset and high lipophilicity. Opioid drugs are well-established in the literature as stimulants of hypothalamic antidiuretic hormone (ADH/vasopressin) release, creating a direct pharmacological link to the body's water-regulation axis. This mechanistic pathway — **opioid receptor → ADH secretion → renal water retention** — is the topological connection captured by the TxGNN knowledge graph, explaining its high confidence score (0.9946).

NSIAD is a rare disease caused by gain-of-function mutations in the *AVPR2* gene (V2 vasopressin receptor), resulting in constitutive receptor activation, unregulated renal water reabsorption, and persistent hyponatraemia — all occurring **independently of circulating ADH levels**. The therapeutic strategy in NSIAD is to reduce water retention and correct hyponatraemia, not to further activate the ADH axis.

This creates a fundamental pharmacological mismatch: administering fentanyl to an NSIAD patient would likely **amplify ADH-mediated effects and worsen hyponatraemia**, which is the opposite of the therapeutic goal. This is a recognised limitation of knowledge-graph-based drug repurposing models — biological connectivity between nodes does not imply therapeutic benefit, and directionality matters. The high TxGNN score here almost certainly reflects a false positive arising from the graph's proximity between the opioid system and water-metabolism disease nodes.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Netherlands Market Information

No marketing authorisations for fentanyl-containing products are recorded in the CBG-MEB dataset included in this evidence pack. It should be noted that fentanyl products may exist under centralised EMA authorisation (e.g., transdermal patches, buccal films for breakthrough cancer pain) or national RVG registrations not captured in the current data extract. Practitioners should consult the CBG-MEB public register directly for up-to-date authorisation status.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for complete safety information on fentanyl. Given fentanyl's classification as a Schedule II high-potency opioid with a narrow therapeutic index, particular attention should be paid to respiratory depression risk, dependence and abuse potential, and interactions with CNS depressants and CYP3A4 inhibitors.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5 prediction with zero supporting clinical trials or published literature, and mechanistic analysis identifies a probable false positive: fentanyl's stimulation of ADH release could plausibly worsen hyponatraemia in NSIAD rather than treat it, meaning the biological pathway identified by TxGNN is directionally counterproductive.

**To proceed, the following is needed:**
- Systematic literature review to determine whether any opioid compounds have ever been investigated in NSIAD or SIADH in a therapeutic (rather than causative) role
- Expert nephrology consultation to evaluate whether any clinical scenario exists in which MOR agonism could benefit NSIAD patients
- Mechanistic modelling of fentanyl's net effect on V2R-independent water retention in the context of gain-of-function AVPR2 mutations
- Reassessment of the TxGNN graph edges linking the opioid system to NSIAD to determine whether edge directionality metadata can be incorporated to reduce false-positive predictions of this type

> **Note:** The second-ranked TxGNN prediction — **Tourette Syndrome** (score 99.05%) — similarly carries an L5 evidence level and a Hold recommendation. While an indirect mechanistic link exists via opioid modulation of striatal dopaminergic circuits (CSTC loop), fentanyl's high addiction liability and extremely narrow therapeutic window make it entirely unsuitable for the long-term management of a chronic neurodevelopmental disorder. That prediction also appears to be a topological false positive and is not recommended for further development.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

