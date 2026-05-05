---
layout: default
title: Levetiracetam
parent: 僅模型預測 (L5)
nav_order: 85
evidence_level: L5
indication_count: 10
---

# Levetiracetam
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

The txgnn-pipeline skill confirms this is the NlTxGNN Netherlands deployment. Now I'll generate the full evaluation report from the Evidence Pack.

---

# Levetiracetam: From Partial-Onset Seizures to Visual Epilepsy

## One-Sentence Summary

Levetiracetam (Keppra®) is an established second-generation antiepileptic drug (AED), widely used for adjunctive and monotherapy treatment of partial-onset seizures in adults and children with epilepsy.
The TxGNN model predicts it may be effective for **Visual Epilepsy**,
with **9 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Partial-onset seizures / epilepsy (based on published literature context; no formal NL registration data available in current dataset) |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| NL Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Levetiracetam is an established second-generation antiepileptic drug (Keppra®), its efficacy in partial-onset seizures and various generalized epilepsy subtypes has been clinically proven across multiple Phase 3 RCTs and meta-analyses, and mechanistically may be applicable to visual epilepsy.

Visual epilepsy — encompassing photosensitive epilepsy, visually-induced reflex epilepsy, and related photoparoxysmal conditions — involves abnormal cortical hyperexcitability and synchronization of the visual cortex in response to flickering light sources or visual patterns. Levetiracetam is known from published literature to bind selectively to synaptic vesicle protein 2A (SV2A), modulating presynaptic neurotransmitter release and broadly suppressing neuronal over-synchronization. A 2005 review in *Epilepsia* (PMID 16302877) documents photosensitivity as a prominent feature within idiopathic generalized epilepsies (IGE), and a 2023 network meta-analysis (PMID 37378757) demonstrates Levetiracetam's quantified efficacy across multiple IGE subtypes — many of which carry photosensitive phenotypes. This provides indirect mechanistic plausibility for the TxGNN prediction.

However, no dedicated clinical trial specifically targeting visual or photosensitive epilepsy as the primary endpoint has been identified for Levetiracetam in humans. The available evidence represents extrapolation from broader epilepsy populations rather than direct proof-of-concept in visual epilepsy. A dedicated research question and prospective data collection are needed before any formal repurposing claim can be advanced.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Completed | 111 | Liceo Study: Prospective observational study assessing new AEDs (including levetiracetam) as first-line bitherapy in focal epilepsy under real-world daily clinical conditions; provides broad-spectrum real-world LEV efficacy data across epilepsy subtypes |
| [NCT00105040](https://clinicaltrials.gov/study/NCT00105040) | Phase 2 | Completed | 87 | 19-week randomised double-blind safety study evaluating cognitive and neuropsychological effects of LEV (20–60 mg/kg/day) as adjunctive treatment in children aged 4–16 years with refractory partial-onset seizures; relevant safety reference |
| [NCT04573803](https://clinicaltrials.gov/study/NCT04573803) | Phase 3 | Not Yet Recruiting | 1,649 | MAST trial: Randomised double-blind placebo-controlled study comparing shorter vs longer AED course, and phenytoin vs levetiracetam for seizure prevention post-traumatic brain injury; provides large-scale Phase 3 safety and prophylactic efficacy framework for LEV |
| [NCT00203216](https://clinicaltrials.gov/study/NCT00203216) | N/A | Completed | 31 | Open-label trial examining LEV efficacy and safety for prophylactic treatment of migraine with or without aura, including visual disturbance phenotypes; provides indirect data supporting LEV use in visually-triggered neurological conditions |
| [NCT07336992](https://clinicaltrials.gov/study/NCT07336992) | Phase 3 | Not Yet Recruiting | 580 | Randomised double-blind placebo-controlled Phase 3 trial of prophylactic LEV for improving functional outcome in acute intracerebral haemorrhage; additional large-scale prophylactic safety/efficacy framework |
| [NCT04559529](https://clinicaltrials.gov/study/NCT04559529) | Phase 2 | Completed | 62 | LEV modulation of hippocampal hyperactivity in psychotic disorders assessed via BOLD-fMRI visual scene processing task; demonstrates LEV's measurable effects on visually-engaged neural circuits, though primary target is psychosis rather than epilepsy |
| [NCT03107507](https://clinicaltrials.gov/study/NCT03107507) | Phase 4 | Unknown | 40 | LEV efficacy in neonatal seizure control; general AED comparison study with phenobarbital; patient population not specific to visual epilepsy but contributes to overall LEV safety profile |
| [NCT04833907](https://clinicaltrials.gov/study/NCT04833907) | Phase 1/2 | Enrolling by Invitation | 24 | AVASPA intracranial gene therapy for Canavan Disease; LEV used as background antiepileptic medication rather than primary investigational drug |
| [NCT04277936](https://clinicaltrials.gov/study/NCT04277936) | Phase 2 | Terminated | 1 | Pharmacologic modulation of hippocampal activity in psychosis using LEV and visual scene processing task; terminated very early (N=1), no conclusions can be drawn |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | Pediatrics | First RCT directly comparing LEV vs phenobarbital for neonatal seizures; demonstrates LEV's efficacy and excellent safety profile in a vulnerable population, supporting broad AED applicability |
| [38678766](https://pubmed.ncbi.nlm.nih.gov/38678766/) | 2024 | RCT | Seizure | Open-label RCT comparing phenytoin vs LEV for acute symptomatic seizures in children with acute encephalitis syndrome; establishes LEV's broad-spectrum efficacy against acute symptomatic seizures |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Systematic Review / Network MA | Journal of Neurology | Network meta-analysis comparing antiseizure medications (including LEV) as monotherapy and adjunctive therapy for idiopathic generalized epilepsies and related subtypes; quantified efficacy/safety comparison directly relevant to IGE-spectrum visual epilepsy |
| [40450767](https://pubmed.ncbi.nlm.nih.gov/40450767/) | 2025 | Systematic Review / MA | Epilepsy & Behavior | Meta-analysis comparing LEV vs other ASMs specifically for myoclonic seizures in IGE, with focus on juvenile myoclonic epilepsy (JME); relevant to generalized reflex seizure subtypes overlapping with visual epilepsy |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | Systematic Review / MA | Neurocritical Care | Systematic review and meta-analysis evaluating LEV for seizure prophylaxis across neurocritical settings (ICH, TBI, neurosurgery, SAH); clarifies efficacy, optimal dosing, and adverse event profile |
| [36209676](https://pubmed.ncbi.nlm.nih.gov/36209676/) | 2022 | Systematic Review / Network MA | Seizure | Network meta-analysis of interventions for benzodiazepine-resistant status epilepticus in children and adults; provides comparative ranking of LEV against alternative second-line agents |
| [35963261](https://pubmed.ncbi.nlm.nih.gov/35963261/) | 2022 | RCT | The Lancet Neurology | PEACH trial: Phase 3 randomised double-blind placebo-controlled trial of prophylactic LEV to reduce acute seizure risk in intracerebral haemorrhage; high-quality safety and efficacy data in an acute neurological setting |
| [16302877](https://pubmed.ncbi.nlm.nih.gov/16302877/) | 2005 | Review | Epilepsia | Key review of photosensitivity in idiopathic generalized epilepsies; characterises the EEG and clinical phenotype of photosensitive epilepsy within IGE — directly underpins the mechanistic basis for the TxGNN prediction of LEV in visual epilepsy |
| [34260837](https://pubmed.ncbi.nlm.nih.gov/34260837/) | 2021 | Review | New England Journal of Medicine | Authoritative review of initial seizure management in adults; covers LEV's established role and practical considerations in first-line and adjunctive epilepsy treatment |
| [21936590](https://pubmed.ncbi.nlm.nih.gov/21936590/) | 2011 | Review | CNS Drugs | Comprehensive spotlight review of Levetiracetam in epilepsy; summarises global approved indications (partial-onset seizures, JME, primary generalised tonic-clonic seizures) and the evidence base behind each |

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Levetiracetam has a robust, well-documented efficacy profile across multiple epilepsy types, and the TxGNN prediction score (99.98%) reflects strong knowledge-graph similarity between visual epilepsy and established indications. However, no dedicated clinical trial specifically targeting visual or photosensitive epilepsy as the primary endpoint has been identified, the drug's formal mechanism of action data and Dutch market authorization data are not available in the current dataset, and the supporting evidence is indirect at best (Evidence Level L3).

**To proceed, the following is needed:**

- **MOA verification**: Retrieve formal mechanism of action data from DrugBank (DB01202) to confirm SV2A-mediated mechanistic plausibility specifically for visual cortex hyperexcitability circuits
- **SmPC review**: Obtain and parse the full SmPC (via CBG-MEB or EMA) to document contraindications, key warnings, and drug interactions before any S1 safety gate can be cleared
- **NL market authorization verification**: Confirm CBG-MEB and/or EMA central authorization status for Levetiracetam in the Netherlands (Keppra® is a known EMA-authorized product; the absence of registration data in the current dataset likely reflects a pipeline data gap rather than true non-authorization)
- **Dedicated clinical evidence**: Design a prospective case series or observational study specifically enrolling patients with visual/photosensitive epilepsy treated with Levetiracetam, or identify any existing registry data targeting this subtype
- **Neurologist consultation**: Engage a Dutch neurologist or epileptologist specialising in reflex epilepsy to assess clinical feasibility and patient-selection criteria before advancing to a formal repurposing research protocol
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

