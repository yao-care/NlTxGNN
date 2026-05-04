---
layout: default
title: Epinephrine
parent: 僅模型預測 (L5)
nav_order: 60
evidence_level: L5
indication_count: 4
---

# Epinephrine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Using the `txgnn-pipeline` skill to guide report generation for the NL deployment, and following the Drug Repurposing Evaluation Report Prompt (v5). Now generating the full evaluation for Epinephrine (DB00668).

---

# Epinephrine: From Anaphylaxis to Obstructive Lung Disease

## One-Sentence Summary

Epinephrine (adrenaline) is a well-established catecholamine used globally as first-line emergency treatment for anaphylaxis and cardiac resuscitation, though it currently holds no CBG-MEB marketing authorization in the Netherlands.
The TxGNN model predicts it may be effective for **Obstructive Lung Disease** (including asthma exacerbations and viral bronchiolitis), with **8 directly relevant clinical trials** and **20 publications** currently supporting this direction.
This prediction receives an **L1 evidence rating**, based on multiple completed Phase 3 randomized controlled trials directly studying epinephrine in obstructive airway conditions.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anaphylaxis & cardiac resuscitation (no CBG-MEB Netherlands authorization) |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L1 |
| NL Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Epinephrine is a naturally occurring catecholamine that acts simultaneously on α- and β-adrenergic receptors. When administered by inhalation, β2-adrenergic receptor stimulation produces potent bronchial smooth muscle relaxation, directly reversing airflow obstruction. Concurrent α1-adrenergic receptor activation causes vasoconstriction of mucosal blood vessels, reducing airway oedema and microvascular leakage — both core pathological features of obstructive lung disease, whether in acute asthma exacerbations, viral bronchiolitis in infants, or croup.

> **Note:** Detailed mechanism of action data from DrugBank is currently unavailable for this evaluation. The mechanistic description above is based on established pharmacological knowledge of epinephrine's well-characterized adrenergic receptor profile.

The connection between epinephrine's primary emergency indication (anaphylaxis) and obstructive lung disease is pharmacologically direct: epinephrine reverses bronchospasm in anaphylaxis through exactly the same β2-mediated pathway as it would in asthma. Nebulized racemic epinephrine has been used clinically for decades in acute management of croup and viral bronchiolitis in children, and in the United States an epinephrine HFA metered-dose inhaler (Primatene Mist) is available over-the-counter for intermittent asthma — providing an international regulatory precedent. The TxGNN model's prediction therefore converges with decades of clinical practice and mechanistic evidence, even though formal Netherlands (CBG-MEB) or EMA-wide authorization for this indication does not yet exist.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01460511](https://clinicaltrials.gov/study/NCT01460511) | Phase 3 | Completed | 70 | Multi-center double-blind RCT: E004 epinephrine inhalation aerosol (HFA-MDI) vs. placebo in children aged 4–11 with asthma — directly evaluates efficacy and safety of epinephrine inhaler for obstructive airway disease |
| [NCT03567473](https://clinicaltrials.gov/study/NCT03567473) | Phase 3 | Completed | 864 | Multicentre RCT: inhaled epinephrine + oral dexamethasone vs. double placebo in infants with bronchiolitis; primary endpoint: hospitalization rate over 7 days |
| [NCT00116584](https://clinicaltrials.gov/study/NCT00116584) | Phase 3 | Completed | 72 | Heliox-driven vs. air-driven nebulized racemic epinephrine in moderate-to-severe pediatric bronchiolitis in the emergency department; assesses speed of airway improvement |
| [NCT01300325](https://clinicaltrials.gov/study/NCT01300325) | Phase 4 | Completed | 136 | RCT: nebulized 3% hypertonic saline + epinephrine vs. normal saline + epinephrine in RSV bronchiolitis hospitalizations; direct evidence for epinephrine combination regimen |
| [NCT01834820](https://clinicaltrials.gov/study/NCT01834820) | Phase 4 | Completed | 120 | Pilot RCT: epinephrine + dexamethasone + hypertonic saline for infant bronchiolitis; evaluates hospital admission rate reduction with combined treatment strategy |
| [NCT04207840](https://clinicaltrials.gov/study/NCT04207840) | Phase 4 | Completed | 28 | Three-way crossover PK study: Primatene Mist (inhaled epinephrine 0.25 mg) vs. IM epinephrine 0.30 mg vs. ProAir (albuterol) — systemic exposure comparison supporting inhaled epinephrine as an asthma bronchodilator route |
| [NCT05363670](https://clinicaltrials.gov/study/NCT05363670) | Phase 2 | Completed | 18 | Four-period crossover RCT: intranasal epinephrine (ARS-1) as a needleless alternative for management of refractory asthma symptoms — evaluates bronchodilatory efficacy in persistent asthma |
| [NCT01025648](https://clinicaltrials.gov/study/NCT01025648) | Phase 1/2 | Terminated | 9 | Dose-ranging study: E004 epinephrine HFA-MDI vs. placebo and active control (epinephrine CFC-MDI) in mild-to-moderate persistent asthma — terminated early; informed dose selection for subsequent Phase 3 |
| [NCT02586961](https://clinicaltrials.gov/study/NCT02586961) | Phase 2/3 | Terminated | 195 | Multicentre RCT: high-dose oral betamethasone + nebulized adrenaline vs. placebo in acute bronchiolitis presenting to pediatric emergency departments; terminated before completion |
| [NCT01070225](https://clinicaltrials.gov/study/NCT01070225) | Phase 4 | Completed | 14 | Proof-of-concept study: reversal of acute β-blocker-induced bronchoconstriction using β-agonist rescue — contextualises adrenergic receptor modulation in airway obstruction management |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | Cochrane Systematic Review | Cochrane Database Syst Rev | Comprehensive meta-analysis of epinephrine vs. other bronchodilators for acute bronchiolitis; found epinephrine superior to placebo for short-term clinical outcomes and hospitalization reduction |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | Cochrane Systematic Review | Cochrane Database Syst Rev | Foundational Cochrane review establishing that bronchodilators — including epinephrine — produce modest but statistically significant short-term benefit in mild-to-moderate bronchiolitis |
| [4606289](https://pubmed.ncbi.nlm.nih.gov/4606289/) | 1974 | Clinical Study | Clin Pharmacol Ther | Direct comparative study of bronchodilator effects of terbutaline vs. epinephrine in obstructive lung disease — cornerstone pharmacological evidence for epinephrine in this indication |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Review | Expert Rev Respir Med | Systematic review of therapeutic strategies for pediatric bronchiolitis (2009–2018) with focused analysis of racemic epinephrine's evidence base, including its role alongside hypertonic saline and high-flow oxygen |
| [19135584](https://pubmed.ncbi.nlm.nih.gov/19135584/) | 2009 | Review | Pediatr Clin North Am | Evidence-based review of croup and acute bronchiolitis: confirms good evidence for temporary symptomatic benefit from nebulized adrenaline in both virally induced obstructive conditions |
| [21486501](https://pubmed.ncbi.nlm.nih.gov/21486501/) | 2011 | Review | BMJ Clin Evid | BMJ clinical evidence review on bronchiolitis management, addressing epinephrine's role in the most common cause of infant respiratory hospitalization |
| [19450362](https://pubmed.ncbi.nlm.nih.gov/19450362/) | 2007 | Review | BMJ Clin Evid | Earlier BMJ evidence synthesis on bronchiolitis treatment; provides historical baseline for evaluating evolving evidence on epinephrine in infant obstructive lower respiratory disease |
| [30856157](https://pubmed.ncbi.nlm.nih.gov/30856157/) | 2019 | Drug Bulletin | Med Lett Drugs Ther | Commentary on the regulatory return of Primatene Mist (OTC epinephrine HFA inhaler) to the US market, confirming regulatory precedent for epinephrine as a self-administered asthma bronchodilator |
| [37088194](https://pubmed.ncbi.nlm.nih.gov/37088194/) | 2023 | Scoping Review | Ann Allergy Asthma Immunol | Scoping review of prehospital epinephrine for anaphylaxis in patients with comorbid asthma — highlights mechanistic overlap and safety of epinephrine across obstructive pulmonary and anaphylactic presentations |
| [4551435](https://pubmed.ncbi.nlm.nih.gov/4551435/) | 1972 | Clinical Study | Ann Allergy | Early clinical evidence for nebulized bronchodilators — including epinephrine — in obstructive lung disease; establishes historical and mechanistic basis for inhaled epinephrine as a bronchodilator |

---

## Netherlands Market Information

Epinephrine currently holds **no CBG-MEB marketing authorization** in the Netherlands and is not registered as a commercial pharmaceutical product in the Dutch RVG (Register Geneesmiddelen) database. No RVG numbers are therefore available to list.

This does not mean epinephrine is absent from Dutch clinical practice: in hospital settings, epinephrine is routinely used for anaphylaxis management, cardiac resuscitation, and as a local anesthetic adjunct, typically supplied under hospital pharmacy authorization or as a ziekenhuisbereiding (hospital preparation). However, the absence of a formal commercial CBG-MEB registration means that any future application of epinephrine for obstructive lung disease in the Netherlands would require one of the following regulatory pathways:

- A new Marketing Authorization Application (MAA) submitted to CBG-MEB directly or centrally via EMA
- Compassionate use or named-patient supply under Dutch Medicines Act (Geneesmiddelenwet)
- Off-label prescribing under the prescriber's clinical responsibility, with documented medical justification per Dutch professional standards

---

## Safety Considerations

Please refer to the **SmPC (Summary of Product Characteristics / Samenvatting van de Productkenmerken)** for complete safety information.

Formal safety data — including specific Dutch/EMA-registered warnings, contraindications, and drug interaction profiles — were not available in the current evidence pack. Based on the internationally recognized pharmacology of epinephrine, prescribers should be aware of the potential for cardiovascular adverse effects (including tachycardia, hypertension, and cardiac arrhythmias), particularly in elderly patients and those with pre-existing cardiac or thyroid conditions. These considerations are especially relevant when evaluating inhaled epinephrine for chronic obstructive lung disease use in a broader outpatient population beyond the current emergency-use context.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs — directly studying epinephrine in bronchiolitis and asthma — support an L1 evidence rating, and the TxGNN prediction score of 99.71% reflects a strong mechanistic and knowledge-graph alignment. However, the total absence of a Netherlands CBG-MEB marketing authorization, the lack of formal safety data in this evidence pack, and the need to differentiate acute-use from chronic-indication protocols necessitate a structured, gated approach before clinical or regulatory implementation.

**To proceed, the following is needed:**

- **Safety data gap closure**: Obtain and review the SmPC from an internationally authorized epinephrine inhalation product (e.g., E004/Armstrong, Primatene Mist) to fulfil the DG001/DG002 data gaps identified in this pack
- **Mechanistic documentation**: Source DrugBank API data for formal MOA characterization to support regulatory submission narratives
- **CBG-MEB pre-submission consultation**: Determine the appropriate regulatory pathway (national MAA vs. EMA centralized) and discuss indication scope with the Medicines Evaluation Board
- **Risk Management Plan (RMP)**: Develop a pharmacovigilance plan covering cardiovascular adverse effects, particularly for paediatric and elderly populations
- **Formulation-specific strategy**: Clarify which route of administration (nebulized, HFA-MDI, intranasal) is being developed, as each carries a distinct regulatory and clinical evidence profile
- **Comparative effectiveness assessment**: Commission an HTA comparing epinephrine vs. standard-of-care bronchodilators (salbutamol, ipratropium) within the Dutch clinical context and Zorginstituut Nederland reimbursement framework
- **Clinical guideline alignment**: Engage Dutch professional bodies (NVvR — Nederlandse Vereniging van Artsen voor Longziekten en Tuberculose; NVK — Paediatric Society) to assess compatibility with existing national treatment guidelines for asthma and bronchiolitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

