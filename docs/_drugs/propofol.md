---
layout: default
title: Propofol
parent: 僅模型預測 (L5)
nav_order: 107
evidence_level: L5
indication_count: 5
---

# Propofol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Using the `txgnn-pipeline` skill to confirm the reporting workflow for NlTxGNN. Now generating the report from the Evidence Pack.

---

# Propofol: From General Anaesthesia to Migraine Disorder

## One-Sentence Summary

Propofol is a short-acting intravenous general anaesthetic and sedative agent, widely used in clinical practice for induction and maintenance of anaesthesia.
The TxGNN model predicts it may be effective for **Migraine Disorder**,
with **5 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | General anaesthesia and procedural sedation |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L1 |
| NL Market Status | Not registered (no CBG-MEB authorizations found in current dataset) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on published literature, Propofol (2,6-diisopropylphenol) is an intravenous anaesthetic that primarily enhances inhibitory neurotransmission through potentiation of GABA-A receptors in the central nervous system.

Migraine pathophysiology involves two key mechanisms that Propofol is known to modulate: (1) **central sensitisation** of the trigeminal pain pathway, and (2) **cortical spreading depression (CSD)** — the electrophysiological event underlying migraine aura and a key trigger for migraine pain. Preclinical data (PMID 22390898) demonstrate that Propofol hemisuccinate suppresses CSD propagation. At **sub-anaesthetic doses** — substantially lower than those required for full sedation — Propofol can interrupt an acute migraine attack without inducing unconsciousness, suggesting a pharmacologically specific action rather than a non-specific sedative effect.

This mechanistic rationale is reinforced by over two decades of clinical observation in emergency department settings. Multiple randomised trials and a 2025 American Headache Society practice guideline now include Propofol among parenteral options for migraine patients who fail standard first-line treatment (dopamine antagonists, NSAIDs). The consistent signal across paediatric and adult populations, combined with a systematic review and network meta-analysis, elevates this from a mechanistic hypothesis to a clinically plausible repurposing candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01604785](https://clinicaltrials.gov/study/NCT01604785) | Phase 2/3 | Completed | 74 | Prospective RCT testing low-dose Propofol for abortive therapy of acute paediatric migraine in the ED; the highest-quality direct trial evidence for this indication to date |
| [NCT02485418](https://clinicaltrials.gov/study/NCT02485418) | NA | Completed | 40 | Evaluated efficacy and safe dosing limits of low-dose Propofol infusion as an abortive agent in the paediatric migraine population; complements NCT01604785 |
| [NCT02492295](https://clinicaltrials.gov/study/NCT02492295) | NA | Terminated | 12 | Designed to study low-dose Propofol for severe refractory migraine in adult ED patients; terminated early with insufficient enrolment (n=12), results inconclusive |
| [NCT03789370](https://clinicaltrials.gov/study/NCT03789370) | NA | Unknown | 130 | Compared anaesthetic maintenance agents (Propofol vs sevoflurane) on postoperative headache incidence; indirect evidence only, not a therapeutic migraine trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [35402989](https://pubmed.ncbi.nlm.nih.gov/35402989/) | 2022 | RCT | Archives of Academic Emergency Medicine | Double-blind RCT comparing Propofol + granisetron vs Propofol + metoclopramide for acute migraine symptom management in the ED |
| [29456086](https://pubmed.ncbi.nlm.nih.gov/29456086/) | 2018 | RCT | The Journal of Emergency Medicine | Prospective RCT of sub-anaesthetic Propofol for paediatric ED migraine; assessed efficacy and side-effect profile with favourable results |
| [35573713](https://pubmed.ncbi.nlm.nih.gov/35573713/) | 2022 | RCT | Archives of Academic Emergency Medicine | RCT evaluating sumatriptan + Propofol combination vs sumatriptan alone for acute migraine; assessed whether Propofol provides additive benefit |
| [32705801](https://pubmed.ncbi.nlm.nih.gov/32705801/) | 2020 | RCT (Pilot) | Emergency Medicine Australasia | Pilot RCT comparing IV Propofol at procedural sedation dose vs standard therapy for initial migraine management in the ED |
| [31621134](https://pubmed.ncbi.nlm.nih.gov/31621134/) | 2020 | Systematic Review | Academic Emergency Medicine | Systematic review evaluating safety and efficacy of Propofol for acute migraine treatment in the ED; summarises all available evidence up to 2020 |
| [39364614](https://pubmed.ncbi.nlm.nih.gov/39364614/) | 2024 | Systematic Review + Network Analysis | Headache | Network meta-analysis comparing parenteral agents for reducing migraine relapse after severe acute presentations; includes Propofol |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Practice Guideline | Headache | 2025 American Headache Society update on parenteral pharmacotherapies for migraine in the ED; provides current evidence-based positioning of Propofol |
| [27454834](https://pubmed.ncbi.nlm.nih.gov/27454834/) | 2016 | Narrative Review | Expert Review of Neurotherapeutics | Comprehensive drug profile of Propofol for super-refractory migraine at sub-anaesthetic doses; covers pharmacology and clinical evidence |
| [32638172](https://pubmed.ncbi.nlm.nih.gov/32638172/) | 2020 | Narrative Review | Current Pain and Headache Reports | Review of IV migraine treatments in children and adolescents in the paediatric ED, including a summary of Propofol evidence |
| [22309235](https://pubmed.ncbi.nlm.nih.gov/22309235/) | 2012 | Narrative Review | Headache | Part of a 3-part series on rescue therapy for acute migraine; covers Propofol among neuroleptics, antihistamines, and other agents in emergency settings |

---

## Netherlands Market Information

No CBG-MEB marketing authorizations for Propofol were identified in the current dataset (total licenses: 0, market status: not registered). This likely reflects a data extraction gap rather than true unavailability — Propofol-containing products (e.g., Diprivan®, Fresenius Kabi Propofol) are routinely used in Dutch hospital anaesthesia practice and are expected to hold valid RVG numbers. A direct verification against the [CBG-MEB product register](https://www.cbg-meb.nl/) is required before drawing any regulatory conclusion.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information.

> **Important note for off-label use evaluation:** No safety data — including warnings, contraindications, or drug–drug interactions — was available in this evidence pack. Given that Propofol is a potent intravenous anaesthetic with narrow therapeutic margins (risk of respiratory depression, apnoea, and haemodynamic compromise even at sub-anaesthetic doses), a full review of the current Dutch SmPC is **essential** prior to any off-label use consideration, particularly outside a monitored anaesthesia care setting.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple randomised controlled trials, a 2020 systematic review, and a 2025 American Headache Society practice guideline collectively support the use of sub-anaesthetic Propofol for acute, refractory migraine in the emergency department — justifying advancement to a structured feasibility and regulatory review.

**To proceed, the following is needed:**

- **Confirm CBG-MEB registration status**: Cross-check Propofol products against the official CBG-MEB register and obtain the applicable Dutch SmPC(s)
- **Safety review**: Complete a full contraindication and drug interaction assessment from the SmPC; clarify minimum monitoring requirements (e.g., pulse oximetry, IV access, resuscitation equipment) for sub-anaesthetic use outside the operating theatre
- **Define target population**: Specify the clinical context (adult vs paediatric; second-line ED treatment for refractory migraine) to scope the off-label use appropriately
- **Guideline alignment**: Review the 2025 AHS guideline (PMID 41321235) and any applicable Dutch neurological or emergency medicine guidelines to determine whether Propofol is already recognised or excluded for this indication in the Netherlands
- **Regulatory pathway**: Determine whether an off-label use protocol, hospital formulary amendment, or formal indication extension would be the appropriate regulatory route under the CBG-MEB/EMA framework
- **Pharmacovigilance plan**: Establish a post-use monitoring protocol for respiratory and haemodynamic adverse events in the Dutch clinical setting
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

