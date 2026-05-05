---
layout: default
title: Oxcarbazepine
parent: 僅模型預測 (L5)
nav_order: 102
evidence_level: L5
indication_count: 10
---

# Oxcarbazepine
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

# Oxcarbazepine: From Focal Epilepsy to Visual Epilepsy

## One-Sentence Summary

Oxcarbazepine (OXC) is a second-generation antiepileptic drug — a keto-analogue of carbamazepine — established internationally as a first-line treatment for focal (partial-onset) seizures in adults and children, though not currently registered in the Netherlands.
The TxGNN model predicts it may be effective for **Visual Epilepsy** — a reflex focal epilepsy subtype triggered by visual stimuli — with a prediction score of **99.95%**.
This prediction is supported by **1 clinical trial** and **19 publications**, principally derived from OXC's well-documented efficacy in focal epilepsy more broadly.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Focal epilepsy / partial-onset seizures (established global use; no NL authorisation on record) |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L3 |
| NL Market Status | Not registered in the Netherlands (CBG-MEB) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on published pharmacological information, Oxcarbazepine acts primarily through its active metabolite, 10-monohydroxycarbazepine (MHD), which blocks voltage-gated sodium channels (Nav1.x). By stabilising neuronal membranes and limiting high-frequency repetitive firing, OXC suppresses the initiation and propagation of seizure activity. This mechanism is directly described in primary pharmacological studies included in the evidence base (PMID 8156978, McLean et al., 1994).

Visual epilepsy — also called reflex visual epilepsy or occipital reflex focal epilepsy — is a subtype of focal epilepsy in which seizures are triggered by flickering lights, geometric patterns, or specific visual stimuli arising from abnormal electrical discharges in the occipital cortex. Because OXC's core approved indication is precisely focal/partial-onset seizures, the mechanistic overlap is strong: Nav1.x blockade directly suppresses the abnormal occipital discharge circuits that underlie visual epilepsy, with no fundamental distinction from the mechanism applicable to other focal epilepsy subtypes.

Critically, visual epilepsy is not a distinct disease entity from a pharmacological perspective — it is a pathophysiologically contiguous subtype of the broader focal epilepsy category for which OXC is already first-line therapy. This explains the TxGNN model's high confidence (99.95%). The main caveat is that dedicated prospective trials targeting visual epilepsy specifically have not been conducted; available evidence is derived from broader focal epilepsy studies. Additionally, OXC is **contraindicated in idiopathic generalised epilepsy** (including photosensitive generalised epilepsy), requiring careful differential diagnosis before use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Completed | 111 | LICEO Study: Prospective observational study assessing real-world effectiveness of new AEDs — including OXC, lamotrigine, levetiracetam, pregabalin, and others — as first-line combination therapy in patients with focal epilepsy. Provides indirect evidence for OXC efficacy in focal epilepsy subtypes including visual epilepsy. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [35429132](https://pubmed.ncbi.nlm.nih.gov/35429132/) | 2022 | RCT | CNS Neuroscience & Therapeutics | Multicentre open-label RCT (China) comparing OXC vs levetiracetam monotherapy in newly diagnosed focal epilepsy; OXC demonstrated comparable seizure-free rates and quality-of-life outcomes. |
| [35380580](https://pubmed.ncbi.nlm.nih.gov/35380580/) | 2022 | Review | JAMA | Comprehensive review of antiseizure medications for adults with epilepsy; covers OXC efficacy, adverse effect profile, and its role in focal seizure management. |
| [39899099](https://pubmed.ncbi.nlm.nih.gov/39899099/) | 2025 | Review | Continuum | 2025 update on antiseizure medications; addresses OXC pharmacokinetics, current indications, and modes of use across focal epilepsy subtypes. |
| [33334546](https://pubmed.ncbi.nlm.nih.gov/33334546/) | 2020 | Review | Seizure | Detailed review of the contemporary role of CBZ and OXC in epilepsy; discusses OXC's improved tolerability over CBZ and its place as first-line therapy for focal seizures. |
| [37092337](https://pubmed.ncbi.nlm.nih.gov/37092337/) | 2023 | Review | Pharmacogenomics | OXC pharmacogenomics review; characterises metabolic enzyme and transporter variants affecting OXC efficacy and safety — important for personalised prescribing. |
| [26844734](https://pubmed.ncbi.nlm.nih.gov/26844734/) | 2016 | Review | Continuum | Comprehensive AED review focusing on pharmacokinetics, monotherapy indications, and clinical use; OXC highlighted for focal epilepsy. |
| [11772334](https://pubmed.ncbi.nlm.nih.gov/11772334/) | 2002 | Drug Review | Expert Opinion on Pharmacotherapy | Expert overview of OXC demonstrating efficacy as adjunctive and monotherapy for partial-onset seizures; also notes early evidence in neuropathic pain and bipolar disorder. |
| [10530693](https://pubmed.ncbi.nlm.nih.gov/10530693/) | 1999 | Drug Monograph | Epilepsia | Foundational OXC monograph; describes mechanism of action, efficacy for partial and secondarily generalised seizures, and improved safety profile vs carbamazepine. |
| [1379159](https://pubmed.ncbi.nlm.nih.gov/1379159/) | 1992 | Review | Drugs | Early comprehensive pharmacological review establishing OXC's distinct kinetic profile via MHD active metabolite and efficacy in epilepsy and trigeminal neuralgia. |
| [28237319](https://pubmed.ncbi.nlm.nih.gov/28237319/) | 2017 | Expert Consensus | Epilepsy & Behavior | Expert opinion on AED treatment for adults and adolescents in the US; OXC recommended among first-line options for focal seizures, filling practical clinical decision gaps. |

---

## Netherlands Market Information

Oxcarbazepine currently holds **no marketing authorisation** with the CBG-MEB (College ter Beoordeling van Geneesmiddelen) in the Netherlands. There are no RVG numbers registered, and the drug does not appear in the Dutch medicines register.

> **Note for prescribers and hospital pharmacists:** Oxcarbazepine is approved in multiple other EU member states (marketed as Trileptal® and generic equivalents) with EMA-recognised data supporting its use in focal epilepsy. Use in the Netherlands would require either a named-patient import procedure, a hospital preparation authorisation, or an off-label use pathway. Prescribers should consult the applicable EMA SmPC and current CBG-MEB guidance prior to any clinical use.

---

## Safety Considerations

Formal safety data (key warnings, contraindications, drug interactions) was not retrieved for this Evidence Pack. However, the clinical evidence base highlights two critical safety signals that must be addressed before clinical use:

- **Risk of aggravating generalised epilepsy**: OXC can precipitate or worsen myoclonic seizures and myoclonic status epilepticus in patients with Juvenile Myoclonic Epilepsy (JME) and other idiopathic generalised epilepsy syndromes (PMID 23774821). Rigorous diagnostic workup — including EEG confirmation of focal rather than generalised epilepsy origin — is mandatory before prescribing OXC for visual epilepsy.
- **Hyponatremia**: OXC is associated with a clinically meaningful risk of symptomatic hyponatremia, particularly in older patients, females, those on higher doses, and those on prolonged treatment. Baseline sodium measurement and periodic monitoring are recommended (documented across multiple studies in the evidence base).

Please refer to the SmPC (Summary of Product Characteristics — in Dutch: Samenvatting van de Productkenmerken) for complete safety information including full contraindications and drug interaction data.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Visual epilepsy is mechanistically indistinguishable from the broader focal epilepsy category for which OXC is already an established first-line treatment; the Nav1.x blockade mechanism directly addresses the occipital focal discharge pathophysiology. However, OXC is not registered in the Netherlands, dedicated RCTs for visual epilepsy are absent, and the critical risk of worsening generalised epilepsy requires strict patient selection — justifying a structured, cautious approach rather than immediate broad use.

**To proceed, the following is needed:**

- EEG and specialist neurology review to confirm focal (occipital) origin and exclude idiopathic generalised epilepsy before initiating OXC in any patient with visual epilepsy
- Formal application to CBG-MEB for marketing authorisation, or initiation of a named-patient import or hospital exemption procedure for individual cases
- Retrieval and review of the complete SmPC (warnings, contraindications, full drug interaction profile) prior to any clinical use
- Baseline serum sodium measurement and a structured monitoring plan for hyponatremia during treatment
- Establishment of a prospective patient registry or observational cohort specifically documenting OXC use in visual epilepsy patients in the Netherlands, to generate dedicated local evidence and support a future formal authorisation application
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

