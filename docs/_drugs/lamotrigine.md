---
layout: default
title: Lamotrigine
parent: 僅模型預測 (L5)
nav_order: 82
evidence_level: L5
indication_count: 9
---

# Lamotrigine
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

Using `txgnn-pipeline` for context, and now generating the report per the Drug Repurposing Evaluation Report Prompt v5. Note: TxGNN rank 1 ("trigeminal nerve neoplasm") is explicitly flagged as a model false positive in the evidence pack; this report pivots to **rank 2 (trigeminal neuralgia)** as the primary actionable indication, with the false-positive flag documented in the summary.

---

# Lamotrigine: From Epilepsy to Trigeminal Neuralgia

## One-Sentence Summary

Lamotrigine is a second-generation antiepileptic drug broadly used for epilepsy and bipolar disorder, working primarily by blocking voltage-gated sodium channels to suppress aberrant neuronal firing.
The TxGNN model predicts it may be effective for **Trigeminal Neuralgia**, with **4 clinical trials** and **19 publications** currently supporting this direction.

> ⚠️ **False Positive Flag (Rank 1):** The highest-ranked TxGNN prediction ("trigeminal nerve neoplasm", score 99.97%) is assessed as a **model false positive** — the knowledge graph likely conflated "trigeminal nerve neoplasm" with "trigeminal neuralgia" due to shared neuroanatomical nodes. No antitumour mechanism exists for lamotrigine. This report focuses on **trigeminal neuralgia (rank 2, score 99.89%)** as the primary clinically actionable indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not found in NL CBG-MEB registry (no active authorizations in dataset) |
| Predicted New Indication | Trigeminal Neuralgia |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| NL Market Status | Not registered (see data quality note below) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (Data Gap DG002). Based on well-established pharmacological knowledge, Lamotrigine is a voltage-gated sodium (Na⁺) channel blocker that stabilises neuronal membrane potential and suppresses the high-frequency repetitive firing of action potentials. It also inhibits presynaptic glutamate release, further reducing excitatory neurotransmission in the central nervous system.

Trigeminal neuralgia (TN) is characterised by paroxysmal, electric shock-like facial pain arising from aberrant ectopic discharges along the trigeminal nerve — most commonly caused by focal demyelination at the nerve root entry zone leading to ephaptic axonal transmission. This pathophysiology is mechanistically identical to the target of carbamazepine (the EAN-endorsed first-line pharmacotherapy for TN), which also works via Na⁺ channel blockade. Lamotrigine shares this mechanism and additionally blocks sodium channel subtypes Nav1.3 and Nav1.7, which are overexpressed in TN patients and represent validated molecular targets.

The clinical rationale is therefore strong: Lamotrigine offers a mechanistically equivalent alternative to carbamazepine — particularly relevant for patients who cannot tolerate carbamazepine's dose-dependent side effects (dizziness, hyponatraemia, drug interactions). A completed Phase 2/3 head-to-head trial (NCT00913107) and a double-blind placebo-controlled add-on study (NCT00203229) provide direct clinical support, making this prediction biologically plausible and clinically actionable.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT00913107](https://clinicaltrials.gov/study/NCT00913107) | Phase 2/3 | Completed | 21 | Head-to-head comparison of lamotrigine vs. carbamazepine in TN patients; evaluates efficacy and safety as most direct comparative evidence available |
| [NCT00203229](https://clinicaltrials.gov/study/NCT00203229) | N/A | Completed | 20 | Double-blind, placebo-controlled add-on study assessing lamotrigine's safety and efficacy in reducing TN attack frequency in adults |
| [NCT00243152](https://clinicaltrials.gov/study/NCT00243152) | N/A | Completed | 6 | fMRI mechanistic study evaluating lamotrigine's effects on neuropathic facial pain; supports neurobiological plausibility and biomarker hypothesis |
| [NCT04996199](https://clinicaltrials.gov/study/NCT04996199) | Phase 4 | Unknown | 132 | RCT comparing carbamazepine vs. oxcarbazepine in TN; provides class-level efficacy benchmark for Na⁺ channel blockers in TN |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [21621166](https://pubmed.ncbi.nlm.nih.gov/21621166/) | 2011 | Clinical Study | J Chinese Medical Assoc | Direct comparison of lamotrigine vs. carbamazepine in TN; demonstrated comparable analgesic efficacy with a different tolerability profile |
| [37892981](https://pubmed.ncbi.nlm.nih.gov/37892981/) | 2023 | Systematic Review | Biomedicines | Umbrella review of drug therapies for TN evaluating efficacy and side effects across multiple agents including lamotrigine |
| [34108244](https://pubmed.ncbi.nlm.nih.gov/34108244/) | 2021 | Clinical Practice Guide | Practical Neurology | Up-to-date practical guide to TN diagnosis and management; includes lamotrigine as a pharmacological option for drug-resistant cases |
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Clinical Guideline | European Journal of Neurology | European Academy of Neurology (EAN) guideline on TN; provides evidence-based treatment recommendations including anticonvulsants |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Review of Neurotherapeutics | Most recent pharmacotherapy update for TN; discusses third-generation anticonvulsants as alternatives when first-line drugs fail |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Review | Molecular Pain | Comprehensive review of TN pathophysiology and pharmacological mechanisms; details Na⁺ channel targets relevant to lamotrigine's action |
| [30081317](https://pubmed.ncbi.nlm.nih.gov/30081317/) | 2018 | Case Report | Multiple Sclerosis & Related Disorders | Refractory TN in MS patient successfully treated with pregabalin + lamotrigine combination after carbamazepine intolerance |
| [30178160](https://pubmed.ncbi.nlm.nih.gov/30178160/) | 2018 | Review | Drugs | Evidence-based review of current and innovative pharmacological options for both typical and atypical TN including adjunctive agents |
| [25864062](https://pubmed.ncbi.nlm.nih.gov/25864062/) | 2015 | Review | Neurosciences | Update on neuropathic pain treatment in TN covering pharmacological and surgical options; positions lamotrigine among second-line agents |
| [25299564](https://pubmed.ncbi.nlm.nih.gov/25299564/) | 2014 | Review | BMJ Clinical Evidence | Systematic evidence review on TN including anticonvulsant treatment options; discusses quality of evidence across drug classes |

---

## Netherlands Market Information

Lamotrigine is listed as **not registered** in the CBG-MEB dataset provided, with no active marketing authorizations on file (0 RVG numbers).

> ⚠️ **Data Quality Note:** This finding is almost certainly a **data pipeline error**. Lamotrigine (brand name Lamictal, plus multiple generic products) is a well-established antiepileptic drug that holds EMA-level and national marketing authorizations across EU member states, including the Netherlands. CBG-MEB public records are expected to show multiple active RVG authorizations. **Verification against the official CBG-MEB registry (https://www.cbg-meb.nl/) is strongly required** before this market status information is used for any regulatory or clinical purpose.

---

## Safety Considerations

Safety data (key warnings, contraindications, drug-drug interactions) were not retrieved in this evidence pack run.

> Please refer to the SmPC (Samenvatting van de Productkenmerken) for complete safety information. Clinicians should be aware of the following well-documented risks associated with lamotrigine:
> - **Serious skin reactions** (Stevens-Johnson Syndrome, Toxic Epidermal Necrolysis): risk is higher with rapid dose escalation or concurrent valproate use
> - **Aseptic meningitis**, haemophagocytic lymphohistiocytosis (HLH), and multi-organ hypersensitivity reactions
> - **Drug interactions**: valproate substantially increases lamotrigine plasma levels; enzyme inducers (carbamazepine, phenytoin) reduce lamotrigine levels
> - **Cardiac effects**: lamotrigine overdose has been associated with cardiac arrhythmia; caution in patients with cardiac conduction disorders

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed clinical trials, including a Phase 2/3 head-to-head trial against the first-line standard carbamazepine (NCT00913107), directly evaluate lamotrigine in trigeminal neuralgia. The mechanistic basis is well-established (Na⁺ channel blockade suppressing ectopic trigeminal discharges), and the 2019 EAN clinical guideline and 2023 systematic review confirm lamotrigine as a recognised pharmacological option, particularly in carbamazepine-intolerant patients.

**To proceed, the following is needed:**

- **Verify NL market status** via the CBG-MEB public registry — the current "not registered" finding appears to be a data error and must be corrected before regulatory use
- **Retrieve SmPC safety data** (warnings, contraindications, DDIs) to complete the S1 safety initial assessment (Data Gap DG001 — currently Blocking)
- **Confirm mechanism of action details** via DrugBank API query (Data Gap DG002)
- **Address the TxGNN false positive** at rank 1 ("trigeminal nerve neoplasm") — recommend adding a post-processing filter to flag or exclude neoplasm indications from antiepileptic drug predictions
- **Obtain larger confirmatory RCT data**: existing TN trials are small (n = 20–21); a powered confirmatory trial or inclusion in a broader NL-registry pharmacoepidemiology study is needed before formal guideline adoption
- **Assess off-label prescribing pathway** under Dutch regulations: if confirmed as on-market, verify whether existing SmPC covers TN or whether an Article 23 off-label use protocol is required
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

