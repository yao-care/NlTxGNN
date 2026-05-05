---
layout: default
title: Temazepam
parent: 僅模型預測 (L5)
nav_order: 117
evidence_level: L5
indication_count: 1
---

# Temazepam
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

Using `txgnn-pipeline` skill to guide report generation for the NlTxGNN project. Now generating the evaluation report from the provided Evidence Pack.

---

# Temazepam: From Established Global Hypnotic to Sleep Disorder, Initiating and Maintaining Sleep

## One-Sentence Summary

Temazepam is a benzodiazepine hypnotic with decades of established global use for insomnia, but is not currently registered in the Netherlands under a CBG-MEB marketing authorisation.
The TxGNN model predicts — and strongly confirms — its efficacy for **sleep disorder, initiating and maintaining sleep**,
with **no registered clinical trials** but **20 publications** (including at least one Phase III RCT) supporting this direction.
Notably, TxGNN is here *validating* a well-known indication rather than identifying a novel one, making this effectively a market-entry evaluation for the Dutch healthcare system.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in the Netherlands; globally established for insomnia / sleep initiation and maintenance |
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L1 (multiple completed RCTs including ≥1 Phase III) |
| NL Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data was not retrieved from DrugBank (a data gap flagged in this Evidence Pack). Based on well-established pharmacological knowledge, Temazepam is a short-to-intermediate half-life **benzodiazepine** belonging to the GABA-A receptor positive allosteric modulator class. By enhancing GABAergic inhibitory neurotransmission in the CNS — particularly in sleep-regulating circuits of the hypothalamus and limbic system — it reduces sleep latency and nocturnal awakenings. Its half-life of approximately 8–20 hours makes it particularly suited for sleep *maintenance* insomnia compared to ultra-short agents such as triazolam.

The predicted indication, "sleep disorder, initiating and maintaining sleep," is the canonical indication for which Temazepam holds regulatory approval in the United States (FDA), the United Kingdom, Australia, and numerous other jurisdictions. The TxGNN model's high confidence score (99.82%, rank 501 of all drug–disease pairs) is therefore unsurprising: the knowledge graph correctly captures decades of clinical evidence linking this compound to insomnia pharmacotherapy.

The clinical relevance for the Netherlands is precisely the absence of a CBG-MEB authorisation. Whether this reflects a deliberate formulary policy, historical market withdrawal, or an unmet regulatory filing is outside the scope of this Evidence Pack and warrants investigation. Regardless, the evidence base is mature: from 1978 sleep-laboratory dose-finding studies through a 2024 multicenter Phase III RCT, Temazepam has been consistently evaluated for this indication.

---

## Clinical Trial Evidence

No clinical trials were retrieved from ClinicalTrials.gov or ICTRP for the Temazepam × sleep disorder query.

> Currently no related clinical trials registered in ClinicalTrials.gov or ICTRP against this specific query. Note: historical trials predating online registration systems (pre-2000) would not appear in these registries; substantive RCT evidence is captured in the literature table below.

---

## Literature Evidence

Prioritised by study design (RCT > systematic review/meta-analysis > review/guideline > clinical study). Showing top 10 of 20 retrieved publications.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39304187](https://pubmed.ncbi.nlm.nih.gov/39304187/) | 2024 | Phase III RCT | *Journal of Palliative Medicine* | Three-arm double-blind multicenter RCT: Temazepam vs melatonin PR vs placebo for insomnia in advanced cancer (prevalence 30–78%); directly evaluates temazepam efficacy and safety as a pharmacologic hypnotic |
| [39374004](https://pubmed.ncbi.nlm.nih.gov/39374004/) | 2024 | RCT | *JAMA Internal Medicine* | Masked taper + CBTI vs standard taper for benzodiazepine receptor agonist (BZRA) discontinuation; informs safe de-prescribing protocols for temazepam in older adults |
| [2859305](https://pubmed.ncbi.nlm.nih.gov/2859305/) | 1985 | RCT | *Journal of Clinical Psychopharmacology* | Multicenter double-blind crossover study: Temazepam 30 mg vs midazolam 15 mg vs placebo for sleep maintenance insomnia; demonstrates hypnotic efficacy with acceptable next-day residual effects |
| [6149491](https://pubmed.ncbi.nlm.nih.gov/6149491/) | 1984 | RCT | *Neuropsychobiology* | Comparative RCT of temazepam 40 mg vs flurazepam 30 mg: both produced significant improvements in sleep quality and duration; temazepam showed less next-morning performance impairment |
| [342551](https://pubmed.ncbi.nlm.nih.gov/342551/) | 1978 | Clinical Study | *Journal of Clinical Pharmacology* | Sleep-laboratory evaluation of temazepam 30 mg under short-, intermediate-, and long-term administration; foundational dose-finding study establishing the 30 mg standard dose |
| [33249496](https://pubmed.ncbi.nlm.nih.gov/33249496/) | 2021 | Systematic Review / NMA | *Sleep* | Network meta-analysis comparing hypnotics for insomnia in older adults; positions temazepam relative to newer agents (z-drugs, orexin antagonists) in terms of efficacy and safety profile |
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Clinical Practice Guideline | *Journal of Clinical Sleep Medicine* | AASM guideline on pharmacologic treatment of chronic insomnia in adults; evaluates temazepam as an individual agent with drug-specific evidence review |
| [30058034](https://pubmed.ncbi.nlm.nih.gov/30058034/) | 2018 | Review | *Drugs & Aging* | Pharmacological management of insomnia in the elderly (57% prevalence); discusses benzodiazepines including temazepam with risk–benefit analysis for geriatric populations |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Review | *Clinical Therapeutics* | Safety and efficacy review of sleep medicines in older adults, including pharmacokinetic changes with ageing relevant to temazepam dosing |
| [1319429](https://pubmed.ncbi.nlm.nih.gov/1319429/) | 1992 | Review | *Journal of Clinical Psychiatry* | Historical pharmacology review of benzodiazepine hypnotics; charts temazepam's emergence as the preferred short half-life agent replacing flurazepam in the 1980s |

---

## Netherlands Market Information

Temazepam currently holds **no CBG-MEB marketing authorisation** in the Netherlands. There are no registered RVG numbers, no approved indications on file, and no active product licences in the dataset.

| RVG Number | Product Name | Dosage Form | Approved Indication |
|-----------|-------------|------------|-------------------|
| — | — | — | No authorisations on record |

> **Note for reviewers:** The absence of a Dutch registration does not reflect a lack of global evidence. Temazepam is authorised in the US (DEA Schedule IV), UK, Australia, and other jurisdictions under brand names such as Restoril, Normison, and Euhypnos. A CBG-MEB application or a request for inclusion in the Dutch national formulary (Farmacotherapeutisch Kompas) would require a formal marketing authorisation dossier.

---

## Safety Considerations

Formal safety data (SmPC warnings, contraindications, DDI data) was not retrieved for this Evidence Pack. The following applies:

> No SmPC, PIL, or DDI data was available from the sources queried. Please refer to the EMA/MHRA product information for authorised temazepam products, or the DrugBank entry for DB00231, for a full safety profile.

As a benzodiazepine class alert, prescribers and pharmacists in the Netherlands should be aware that temazepam carries class-level risks including **dependence and tolerance** (critical for chronic insomnia management), **CNS depression**, risk of falls and fractures in older adults, and potential for rebound insomnia on discontinuation — all of which are relevant to the predicted indication and should be addressed in any market authorisation or formulary review.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction is confirmed by a robust and mature evidence base (Phase III RCT, multiple earlier RCTs, systematic reviews, and clinical guidelines), and the indication is Temazepam's globally established primary use — this is not a speculative repurposing scenario but rather a market-entry question for the Netherlands. However, the complete absence of a CBG-MEB authorisation, combined with well-known benzodiazepine class safety concerns (dependence, elderly fall risk), warrants a structured regulatory and clinical safety review before any formulary recommendation.

**To proceed, the following is needed:**

- **Regulatory clarification**: Determine why Temazepam lacks a Dutch/EMA centralised authorisation — historical withdrawal, patent expiry, or never-filed; assess whether a CBG-MEB MRP/DCP application is feasible
- **SmPC retrieval**: Obtain and parse the UK MHRA or Australian TGA SmPC for warnings, contraindications, and DDI data (remediation for DG001)
- **DrugBank MOA data**: Retrieve formal mechanism-of-action, pharmacokinetics, and toxicity data via DrugBank API (remediation for DG002)
- **Dutch clinical context**: Review Farmacotherapeutisch Kompas and NHG-standaard Slaapproblemen en slaapmiddelen to understand current NL prescribing landscape and whether alternative agents have displaced temazepam
- **Elderly population safety plan**: Given that most literature highlights geriatric concerns, a risk management plan addressing Beers Criteria alignment and deprescribing protocols is required
- **Controlled substance classification**: Confirm Opiumwet (Dutch Opium Act) scheduling for temazepam and its implications for dispensing and monitoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

