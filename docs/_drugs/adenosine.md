---
layout: default
title: Adenosine
parent: 僅模型預測 (L5)
nav_order: 18
evidence_level: L5
indication_count: 2
---

# Adenosine
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

# Adenosine: From Supraventricular Tachycardia to Catecholaminergic Polymorphic Ventricular Tachycardia

## One-Sentence Summary

Adenosine is a naturally occurring nucleoside widely used in clinical practice for the acute termination of supraventricular tachycardia (SVT) and as a pharmacological stress agent in cardiac imaging. The TxGNN model predicts it may be effective for **Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT)**, with **1 clinical trial** and **13 publications** currently supporting this direction. A second prediction for bundle branch block was assessed as mechanistically contradictory and is not recommended for further pursuit.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Supraventricular tachycardia (SVT) termination; cardiac stress testing (no local marketing authorization on record) |
| Predicted New Indication | Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT) |
| TxGNN Prediction Score | 99.42% (rank 1,158) |
| Evidence Level | L4 — Preclinical and mechanistic studies |
| Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold — Research Question |

> **Note on Rank 1 Prediction:** The TxGNN model's highest-ranked prediction for adenosine was "obsolete bundle branch block" (score 99.94%). However, expert assessment determined a **mechanistic directionality conflict** — adenosine slows AV nodal conduction and could worsen conduction system disorders. This prediction had zero supporting evidence (no trials, no literature) and is classified **L5 / Hold**. The remainder of this report focuses on the rank 2 prediction (CPVT), which has a plausible mechanistic basis and supporting literature.

---

## Why is This Prediction Reasonable?

Adenosine exerts its cardiac effects primarily through the A₁ adenosine receptor, activating the Gi protein signalling cascade. This inhibits adenylyl cyclase, lowers intracellular cyclic AMP (cAMP), and directly opposes the catecholamine-driven sympathetic stimulation that triggers CPVT episodes. Since CPVT arrhythmias are precipitated by adrenergic stress that raises cAMP and promotes aberrant calcium release from the sarcoplasmic reticulum (SR) via the ryanodine receptor (RyR2), adenosine's ability to reduce cAMP represents a mechanistically rational counter-strategy.

A second, complementary mechanism is supported by basic science evidence. Blayney et al. (PMID: 23747301) demonstrated that ATP — which is rapidly converted to adenosine in vivo — directly interacts with the CPVT mutation-associated central domain of the cardiac ryanodine receptor (RyR2). This suggests that adenosine (or its nucleotide precursor) may directly stabilize the abnormal calcium release channel that underlies CPVT pathophysiology. Furthermore, a clinical case report by Sumitomo et al. (PMID: 18313614) documented successful termination of bidirectional ventricular tachycardia in a CPVT patient using ATP, providing direct clinical precedent.

The original clinical use of adenosine (SVT termination) and the predicted new indication (CPVT) are both cardiac arrhythmias rooted in abnormal electrophysiology, sharing overlapping ion channel and second-messenger pathways. However, the mechanisms diverge significantly: SVT involves re-entrant circuits through the AV node, while CPVT involves catecholamine-triggered calcium-handling defects. This distinction means the therapeutic rationale for CPVT rests on adenosine's anti-adrenergic and RyR2-modulating properties rather than its AV-nodal blocking effects.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07263139](https://clinicaltrials.gov/study/NCT07263139) | Phase 2a | Recruiting | 10 | Safety, tolerability and exploratory efficacy of AGP100 in CPVT patients. Tests the adenosine/purinergic signalling pathway in CPVT but uses AGP100 (not adenosine directly). Serves as indirect pathway validation. No results yet (est. completion June 2027). |

> **Interpretation:** Only one registered trial was identified, and it evaluates AGP100 — potentially an adenosine analogue or prodrug — rather than adenosine itself. The trial's existence validates scientific interest in targeting this pathway for CPVT, but direct clinical evidence for adenosine in CPVT remains absent. The small sample size (N=10) and early phase further limit the evidentiary weight.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [18313614](https://pubmed.ncbi.nlm.nih.gov/18313614/) | 2008 | Case Report | Heart Rhythm | **Most directly relevant.** ATP successfully terminated bidirectional ventricular tachycardia in a patient with CPVT — clinical proof-of-concept for the adenosine/purinergic pathway in CPVT. |
| [23747301](https://pubmed.ncbi.nlm.nih.gov/23747301/) | 2013 | Basic Research (in vitro) | Biochim Biophys Acta | ATP interacts with the CPVT mutation-associated central domain of the cardiac ryanodine receptor (RyR2), suggesting a direct molecular mechanism for adenosine/ATP in modulating the CPVT-defective channel. |
| [41691612](https://pubmed.ncbi.nlm.nih.gov/41691612/) | 2026 | Basic Research (in vitro) | J Physiol | Human cardiac-neural microtissues reveal CPVT is also a disease of the sympathetic neuron, supporting the rationale that anti-adrenergic agents (like adenosine) could target the upstream trigger. |
| [38776406](https://pubmed.ncbi.nlm.nih.gov/38776406/) | 2024 | Basic Research (in vivo) | Cardiovasc Res | Gene therapy with PDE2A/PDE4B (which modulate cAMP compartmentation) prevents heart failure and arrhythmias in mice — validates the cAMP pathway as a therapeutic target for arrhythmias. |
| [30209242](https://pubmed.ncbi.nlm.nih.gov/30209242/) | 2018 | Basic Research (in vivo) | Sci Transl Med | SR calcium leak via RyR2 contributes to arrhythmia; RyR2 stabilizer rycal S36 normalizes SR Ca²⁺ leak and improves survival — supports RyR2 stabilization as a valid therapeutic strategy. |
| [23858002](https://pubmed.ncbi.nlm.nih.gov/23858002/) | 2013 | Basic Research (in vitro) | J Gen Physiol | Calsequestrin regulation of RyR2 in normal and CPVT conditions — elucidates the luminal Ca²⁺ regulation defects underlying CPVT arrhythmogenesis. |
| [40165484](https://pubmed.ncbi.nlm.nih.gov/40165484/) | 2025 | Clinical Review | Europace | Multi-society consensus on pharmacological provocation testing in cardiac EP, including adenosine use in arrhythmia diagnostics — confirms adenosine's established role in cardiac electrophysiology. |
| [21699856](https://pubmed.ncbi.nlm.nih.gov/21699856/) | 2011 | Case Report | Heart Rhythm | Postpacing abnormal repolarization in CPVT with RyR2 mutation — demonstrates EPS findings and arrhythmic substrate characterization in CPVT. |
| [35577932](https://pubmed.ncbi.nlm.nih.gov/35577932/) | 2022 | Basic Research (in vitro) | Commun Biol | TECRL deficiency causes aberrant mitochondrial function in cardiomyocytes, linked to CPVT — expands the molecular understanding of CPVT subtypes. |
| [39148245](https://pubmed.ncbi.nlm.nih.gov/39148245/) | 2024 | Clinical Review | Paediatr Anaesth | Review of pediatric arrhythmias including CPVT management; notes adenosine use in differentiating arrhythmia types — contextualizes adenosine's role in pediatric arrhythmia care. |

---

## Market Information

| Item | Detail |
|------|--------|
| Market Status | Not marketed (未上市) — no marketing authorizations on record |
| Total Licenses | 0 |
| Dosage Forms | None registered locally |

> **Note:** Adenosine is widely available internationally (e.g., Adenocard® in the US/EU) as an IV formulation for SVT termination. The absence of local marketing authorization does not preclude access through special import pathways or hospital exemptions, but represents a practical barrier to routine clinical use. For the Netherlands specifically, adenosine products may be available through centralized EU marketing authorizations (EMA) — this should be verified with CBG-MEB records.

---

## Safety Considerations

> Detailed safety data (SmPC warnings, contraindications, drug-drug interactions) was not available in the evidence pack. Please refer to the **SmPC (Summary of Product Characteristics)** for comprehensive safety information.
>
> **Known safety considerations for adenosine (based on established clinical use):**
> - **Transient side effects:** Chest tightness, dyspnoea, facial flushing, and brief periods of asystole are common but self-limiting due to adenosine's ultra-short half-life (<10 seconds)
> - **Contraindications (general):** Second- or third-degree AV block, sick sinus syndrome (without pacemaker), severe asthma/COPD (risk of bronchospasm)
> - **Critical consideration for CPVT:** Adenosine's conduction-slowing properties must be weighed carefully in patients who may have coexisting conduction system abnormalities
> - **Route:** IV administration only; requires cardiac monitoring and resuscitation equipment available
>
> ⚠️ *These are general considerations. A formal safety assessment based on the SmPC is required before any clinical use.*

---

## Conclusion and Next Steps

**Decision: Hold — Research Question**

**Rationale:**
Adenosine has a mechanistically plausible dual rationale for CPVT (anti-adrenergic cAMP reduction and potential direct RyR2 modulation), supported by one compelling case report (ATP terminating CPVT-related VT) and relevant basic science. However, the evidence remains at Level L4 — there are no completed clinical trials of adenosine in CPVT, the single registered trial tests a different compound (AGP100), and the literature is predominantly preclinical. The drug is also not locally marketed, adding a practical barrier. The TxGNN prediction is scientifically interesting but insufficient for clinical action.

**To proceed, the following is needed:**
- **Mechanism of Action clarification:** Confirm adenosine's MOA via DrugBank API query (identified data gap DG002) and assess whether the A₁ receptor pathway provides sufficient anti-arrhythmic effect in CPVT models
- **AGP100 relationship:** Determine whether AGP100 (NCT07263139) is an adenosine analogue, prodrug, or pathway-related compound — positive Phase 2a results would strengthen the case for adenosine
- **SmPC safety data:** Obtain detailed warnings and contraindications (identified data gap DG001, blocking severity) — essential for evaluating risk-benefit in CPVT patients who may have conduction abnormalities
- **Preclinical validation:** Commission or identify in vivo studies testing adenosine (not just ATP) in CPVT animal models (e.g., RyR2 mutant mice)
- **Regulatory pathway:** Assess availability of adenosine IV formulations through CBG-MEB/EMA marketing authorizations or hospital import mechanisms
- **Clinical feasibility assessment:** Adenosine's ultra-short half-life (~10 seconds) may limit its utility for chronic CPVT management — evaluate whether continuous infusion or longer-acting analogues would be required

---

*This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. Data cutoff: 2026-04-03.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

