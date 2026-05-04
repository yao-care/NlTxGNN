---
layout: default
title: Acetaminophen
parent: 僅模型預測 (L5)
nav_order: 16
evidence_level: L5
indication_count: 1
---

# Acetaminophen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Acetaminophen: From Analgesic/Antipyretic to Migraine with Brainstem Aura

## One-Sentence Summary

Acetaminophen (paracetamol) is one of the most widely used analgesic and antipyretic agents worldwide, available over the counter for pain and fever management. The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura** (MBA), a rare migraine subtype formerly known as basilar-type migraine, with **0 clinical trials** specific to this subtype but **20 publications** supporting the broader use of acetaminophen in migraine treatment. Notably, clinical guidelines already position acetaminophen as a first-line option for MBA — not because of direct efficacy trials, but because triptans are traditionally contraindicated in this subtype.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pain and fever (analgesic/antipyretic) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L3 — Systematic reviews and RCTs exist for general migraine; no direct trials for MBA subtype |
| NL Market Status | Not found in evidence pack (Note: paracetamol is widely available OTC in the Netherlands) |
| Number of Authorizations | 0 (in current dataset) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Acetaminophen exerts its analgesic effect primarily through central COX inhibition and modulation of the endocannabinoid system, reducing pain signal processing in the central nervous system. Unlike NSAIDs, its mechanism is predominantly central rather than peripheral, which is particularly relevant for headache disorders where central sensitization plays a key role.

Migraine with brainstem aura (MBA) is a specific subtype of migraine characterized by aura symptoms originating from the brainstem — including dysarthria, vertigo, tinnitus, diplopia, and decreased consciousness — followed by a typical migraine headache. The underlying pathophysiology involves cortical spreading depolarization (CSD) extending to brainstem structures. While acetaminophen's efficacy in general migraine acute treatment is supported by Level 1 evidence (multiple RCTs), its application to MBA specifically is extrapolated rather than directly validated. The mechanistic rationale is that the headache pain phase of MBA shares the same trigeminovascular pathway as common migraine, which acetaminophen can modulate.

A critical practical consideration strengthens this prediction: triptans, the standard acute migraine therapy, are traditionally considered relatively contraindicated in MBA due to theoretical concerns about vasoconstriction in the vertebrobasilar territory. This makes acetaminophen one of the few recommended first-line acute treatments for MBA in clinical guidelines — positioned there by a process of safe elimination rather than positive efficacy evidence. This regulatory and clinical reality creates a genuine therapeutic niche where formal validation of acetaminophen's efficacy in MBA would be clinically valuable.

## Clinical Trial Evidence

Currently no clinical trials specifically investigating acetaminophen for migraine with brainstem aura are registered on ClinicalTrials.gov or the WHO ICTRP platform. This represents a significant evidence gap, as RCTs for general migraine have not stratified results by MBA subtype.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Systematic Review / Evidence-Based Guideline | Headache | AHS updated evidence assessment of acute migraine pharmacotherapies; establishes acetaminophen among evaluated treatments for acute migraine |
| [9482363](https://pubmed.ncbi.nlm.nih.gov/9482363/) | 1998 | RCT (×3) | Archives of Neurology | Three double-blind, randomized, placebo-controlled trials assessing the combination of acetaminophen, aspirin, and caffeine for migraine headache pain relief |
| [11112243](https://pubmed.ncbi.nlm.nih.gov/11112243/) | 2000 | RCT | Archives of Internal Medicine | Randomized, double-blind, placebo-controlled, population-based study demonstrating efficacy and safety of acetaminophen alone in acute migraine treatment |
| [10321417](https://pubmed.ncbi.nlm.nih.gov/10321417/) | 1999 | RCT (retrospective analysis) | Clinical Therapeutics | Acetaminophen/aspirin/caffeine combination effective for menstruation-associated migraine across three randomized placebo-controlled studies |
| [11318886](https://pubmed.ncbi.nlm.nih.gov/11318886/) | 2001 | Comparative Trial | Headache | Isometheptene mucate/dichloralphenazone/acetaminophen compared to sumatriptan for mild-to-moderate migraine; evaluates acetaminophen-containing regimen |
| [30470274](https://pubmed.ncbi.nlm.nih.gov/30470274/) | 2019 | Review | Neurologic Clinics | Identifies acetaminophen as first-line symptomatic treatment for headache in pregnancy, where MBA management is particularly challenging |
| [39493026](https://pubmed.ncbi.nlm.nih.gov/39493026/) | 2024 | Narrative Review | Cureus | Reviews abortive and prophylactic migraine therapies in pregnancy; positions acetaminophen as a primary safe option when triptans are avoided |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Narrative Review | Handbook of Clinical Neurology | Examines status migrainosus (debilitating migraine >72h); relevant to understanding severe migraine complications including brainstem aura variants |
| [33525313](https://pubmed.ncbi.nlm.nih.gov/33525313/) | 2021 | Review | Neurology International | Reviews migraine pharmacotherapy landscape; notes acetaminophen as standard treatment for mild-to-moderate migraine before escalation to triptans |
| [37123778](https://pubmed.ncbi.nlm.nih.gov/37123778/) | 2023 | Review | Cureus | Discusses migraine treatment approaches in pregnancy/breastfeeding with acetaminophen as preferred agent due to safety profile |

## Netherlands Market Information

No CBG-MEB marketing authorizations for acetaminophen (paracetamol) were identified in the current evidence pack dataset. However, paracetamol is one of the most widely available over-the-counter medicines in the Netherlands, sold under numerous brand names (e.g., Panadol, generic paracetamol) in pharmacies, drugstores, and supermarkets. The absence of records in this dataset likely reflects a data matching limitation rather than true market unavailability. For complete authorization information, consult the [CBG-MEB Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/).

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics / Samenvatting van de Productkenmerken) for comprehensive safety information.

Key general safety points for acetaminophen based on well-established clinical knowledge:
- **Hepatotoxicity**: Risk of severe liver injury at doses exceeding 4g/day or in patients with hepatic impairment, chronic alcohol use, or malnutrition
- **Dosing vigilance**: Many combination products contain acetaminophen, creating risk of inadvertent overdose
- **Renal considerations**: Caution with long-term use in patients with renal impairment

> ⚠️ **Data Gap**: Specific SmPC warnings and contraindications from the regulatory authority were not available in this evidence pack. These must be obtained before proceeding to formal safety evaluation (Stage S1).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Acetaminophen has strong RCT-level evidence (L1) for efficacy in general acute migraine treatment, and clinical guidelines already recommend it as a first-line option for migraine with brainstem aura due to triptan contraindications. However, the evidence is L3 for the MBA subtype specifically, as no trials have directly validated efficacy in this population. The TxGNN prediction score of 99.15% aligns with existing clinical practice patterns.

**To proceed, the following is needed:**
- **Mechanism of action data**: Obtain detailed MOA from DrugBank to strengthen the mechanistic rationale for MBA specifically (current data gap DG002)
- **SmPC safety data**: Retrieve full warnings, contraindications, and drug interactions from CBG-MEB/EMA SmPC (current data gap DG001 — blocking for S1 safety assessment)
- **MBA-specific clinical evidence**: Search for subgroup analyses within existing migraine RCTs that may have included MBA patients
- **Expert consultation**: Engage neurologists with MBA expertise to assess whether the central analgesic mechanism adequately addresses brainstem aura-phase pathophysiology
- **CBG-MEB registration confirmation**: Verify current Dutch marketing authorization status via the Geneesmiddeleninformatiebank

---

*This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. Report generated on 2026-04-03 based on evidence pack v4 (data cutoff: 2026-04-03).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

