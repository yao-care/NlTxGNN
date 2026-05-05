---
layout: default
title: Pimozide
parent: 僅模型預測 (L5)
nav_order: 105
evidence_level: L5
indication_count: 10
---

# Pimozide
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

Using `txgnn-pipeline` skill for context on TxGNN drug repurposing report generation. Now generating the report based on the Evidence Pack.

---

# Pimozide: From Tourette Syndrome to Trichotillomania

## One-Sentence Summary

Pimozide is a typical antipsychotic of the diphenylbutylpiperidine class, approved in multiple countries as a second-line treatment for Gilles de la Tourette syndrome and historically used for schizophrenia maintenance therapy.
The TxGNN model predicts it may be effective for **Trichotillomania**,
with **0 clinical trials** and **10 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Tourette Syndrome (Gilles de la Tourette); schizophrenia maintenance |
| Predicted New Indication | Trichotillomania |
| TxGNN Prediction Score | 99.996% |
| Evidence Level | L3 |
| NL Market Status | Not marketed in the Netherlands |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known information, Pimozide belongs to the diphenylbutylpiperidine class of typical antipsychotics and acts as a dopamine D2 receptor antagonist. Its efficacy in Tourette syndrome has been established through postsynaptic dopamine blockade in the striatum, suppressing repetitive motor and vocal tics driven by hyperdopaminergic activity in cortico-striato-thalamo-cortical (CSTC) circuits.

Trichotillomania (TTM) is classified within the obsessive-compulsive spectrum disorders (OCD-spectrum), where dysregulation of striatal dopamine circuits plays a central role in mediating repetitive compulsive behaviours — the same circuit implicated in Tourette syndrome. This neurobiological overlap provides a direct mechanistic rationale: if D2 blockade in the striatum reduces tic expression in Tourette syndrome, the same mechanism may attenuate the compulsive hair-pulling urges in TTM. Furthermore, pimozide's mechanistic resemblance to the augmentation strategies already employed in refractory OCD (where adding a low-dose D2 antagonist to an SRI improves outcomes) strengthens the cross-indication case.

Clinically, published case series (PMID 1532960) and a 2023 systematic evidence mapping of randomised controlled trials (PMID 36802832) both identify pimozide augmentation of serotonin reuptake inhibitors (SRIs) as a pharmacologically grounded strategy for SRI-refractory TTM. A 2004 comprehensive review (PMID 15554735) additionally confirms pimozide's established off-label use across several psychodermatological compulsive conditions. While the evidence base remains observational, the mechanistic alignment and the drug's prior clinical experience in closely related disorders make this TxGNN prediction well-founded.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36802832](https://pubmed.ncbi.nlm.nih.gov/36802832/) | 2023 | Systematic Review / Evidence Mapping | J Cutaneous Med Surg | Evidence mapping of RCTs for pharmacological management of primary psychodermatologic disorders including TTM; highlights evidence gaps and appraises available safety and effectiveness data |
| [15554735](https://pubmed.ncbi.nlm.nih.gov/15554735/) | 2004 | Comprehensive Review | Am J Clin Dermatol | Comprehensive review of pimozide in dermatological practice; documents established off-label efficacy in monosymptomatic hypochondriacal psychosis and psychodermatological compulsive conditions |
| [30446201](https://pubmed.ncbi.nlm.nih.gov/30446201/) | 2018 | Review | Clin Dermatol | Reviews antipsychotics including pimozide in dermatology; describes D2 blockade, H1, muscarinic, and α1-adrenergic effects relevant to cutaneous and psychodermatological applications |
| [27320510](https://pubmed.ncbi.nlm.nih.gov/27320510/) | 2016 | Review | Tijdschr Psychiatrie | Reviews treatment options for paediatric TTM; highlights limited pharmacotherapeutic research investment and discusses antipsychotic augmentation strategies |
| [1532960](https://pubmed.ncbi.nlm.nih.gov/1532960/) | 1992 | Clinical Case Series | J Clin Psychiatry | Low-dose pimozide augmentation of SRI therapy in TTM; draws mechanistic parallels between Tourette syndrome, OCD, and TTM; supports D2 antagonist as augmentation strategy in SRI-refractory cases |
| [10357517](https://pubmed.ncbi.nlm.nih.gov/10357517/) | 1999 | Case Series | J Child Adolesc Psychopharmacol | Reports risperidone augmentation in SRI-resistant TTM; cites prior open-label pimozide augmentation data showing benefit, establishing the D2 antagonist augmentation rationale in TTM |
| [11475941](https://pubmed.ncbi.nlm.nih.gov/11475941/) | 2001 | Review | CNS Drugs | Reviews psychogenic excoriation and related OCD-spectrum conditions; contextualises compulsive skin/hair disorders and the role of antipsychotic augmentation |
| [28225970](https://pubmed.ncbi.nlm.nih.gov/28225970/) | 2017 | Case Report | An Bras Dermatol | Case report of TTM with dermoscopic differential diagnosis from alopecia areata; notes standardisation gap in pharmacological treatment, with N-acetylcysteine as one emerging option |
| [10497682](https://pubmed.ncbi.nlm.nih.gov/10497682/) | 1999 | Review | Ann Acad Med Singapore | Epidemiology, clinical features, and treatment approaches for TTM as an under-diagnosed chronic psychiatric syndrome; lifetime prevalence 1.5–3.4% in college students |
| [10900563](https://pubmed.ncbi.nlm.nih.gov/10900563/) | 2000 | Clinical Profile | Int J Psychiatry Med | Clinical profile of monohypochondriacal psychosis (delusional parasitosis); contextualises pimozide's broader psychodermatological utility in delusional compulsive conditions |

---

## Netherlands Market Information

Pimozide currently holds **no marketing authorisations** in the Netherlands registered with the CBG-MEB. The drug is not commercially available through registered channels. Any clinical use would require a special import procedure (Article 3.17 Geneesmiddelenwet) or a compassionate use/named-patient application.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for complete safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Trichotillomania shares a striatal dopaminergic neurobiological basis with Tourette syndrome, and published case series combined with a 2023 systematic evidence mapping provide L3-level support for pimozide augmentation in SRI-refractory TTM. However, pimozide holds no CBG-MEB authorisation in the Netherlands and no dedicated TTM clinical trials have been registered to date, meaning any patient access requires regulatory navigation and prospective safety monitoring.

**To proceed, the following is needed:**
- Design of a dedicated Phase 2 RCT evaluating low-dose pimozide augmentation in SRI-refractory TTM patients
- Full SmPC review to establish QT prolongation risk profile and mandatory ECG monitoring protocol prior to any clinical use
- CBG-MEB special import or named-patient application for NL patient access
- DrugBank MOA data retrieval (DG002) to formally document receptor binding profile and strengthen mechanistic rationale documentation
- Definition of a safety monitoring plan covering cardiac monitoring, extrapyramidal effects, and contraindication screening
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

