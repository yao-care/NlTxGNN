---
layout: default
title: Diazepam
parent: 僅模型預測 (L5)
nav_order: 51
evidence_level: L5
indication_count: 10
---

# Diazepam
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

Using `txgnn-pipeline` to guide this report generation for the NlTxGNN project. Now generating the report based on the Evidence Pack.

---

# Diazepam: From Anxiety and Seizure Management to Insomnia Treatment

## One-Sentence Summary

Diazepam is a long-established benzodiazepine, classically used for anxiety disorders, acute seizures, and muscle relaxation.
The TxGNN model predicts it may be effective for **Insomnia (disease)** with a prediction score of **99.9997%**,
with **24 clinical trials** and **18 publications** currently indexed in support of this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No CBG-MEB authorization found; clinically established as an anxiolytic and anticonvulsant |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.9997% |
| Evidence Level | L2 |
| NL Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on well-established pharmacological knowledge, Diazepam belongs to the benzodiazepine (BZD) class and acts as a **positive allosteric modulator of GABA-A receptors**. By binding at the benzodiazepine site (located between the α and γ subunits of the receptor), it potentiates the effect of endogenous GABA, increasing the frequency of Cl⁻ channel opening. This enhances inhibitory neurotransmission throughout the central nervous system, producing its characteristic anxiolytic, sedative-hypnotic, anticonvulsant, and myorelaxant effects.

The mechanistic link between diazepam and insomnia is direct. Enhanced GABAergic tone in the reticular activating system and limbic arousal circuits reduces sleep-onset latency and extends total sleep time — precisely the same pathway exploited by all benzodiazepine hypnotics, including temazepam and nitrazepam. The TxGNN prediction therefore reflects a **confirmed pharmacological relationship** rather than a speculative repurposing discovery. Notably, PMID 6113175 provides a direct head-to-head RCT confirming diazepam's hypnotic efficacy against lormetazepam in 100 insomnia patients, and diazepam appears as an active positive control in numerous subsequent insomnia model studies.

An important clinical caveat must be acknowledged: diazepam suppresses REM sleep and slow-wave sleep architecture, and chronic use results in tolerance, physical dependence, and rebound insomnia on discontinuation. Contemporary Dutch NHG and European EMA guidelines recommend limiting benzodiazepines for insomnia to short-term use (≤4 weeks) and prioritise cognitive behavioural therapy for insomnia (CBTI) as first-line treatment. The clinical utility of this TxGNN prediction is therefore best framed within a **short-term or bridging treatment context**, with careful patient selection and a defined exit strategy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02530580](https://clinicaltrials.gov/study/NCT02530580) | Phase 1 | Completed | 12 | Double-blind crossover study of selective GABA-A modulator AZD7325 using diazepam as active pharmacological reference; confirms diazepam's established role as benchmark GABA-A hypnotic |
| [NCT04050176](https://clinicaltrials.gov/study/NCT04050176) | Phase 3 | Active, not recruiting | 260 | Blinded vs open-label hypnotic tapering combined with CBTI for insomnia; directly evaluates benzodiazepine discontinuation strategies in insomnia patients |
| [NCT04751851](https://clinicaltrials.gov/study/NCT04751851) | N/A | Completed | 128 | RCT comparing Acceptance and Commitment Therapy (ACT) vs standard psychological support for BZD withdrawal in hypnotic-dependent insomnia patients |
| [NCT03687086](https://clinicaltrials.gov/study/NCT03687086) | N/A | Completed | 188 | Novel mechanism-targeted hypnotic discontinuation programme for older adults; aims to achieve and sustain high rates of non-use beyond tapering alone |
| [NCT02281175](https://clinicaltrials.gov/study/NCT02281175) | N/A | Completed | 114 | PASSE-65+ psychosocial intervention for gradual BZD tapering in elderly users; addresses the insomnia-BZD dependency cycle in the older population |
| [NCT03461042](https://clinicaltrials.gov/study/NCT03461042) | Phase 4 | Completed | 17 | Ramelteon as adjunct during BZD/non-BZD dose reduction in chronic insomnia; evaluates melatonin receptor agonist as a transition strategy |
| [NCT03405493](https://clinicaltrials.gov/study/NCT03405493) | N/A | Completed | 60 | Sleep and light therapy for depression in a UK community setting; provides validated sleep outcome measures relevant to insomnia assessment |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Unknown | 1,400 | Prospective Taiwanese cohort on hypnotic prescribing patterns in the elderly; includes BZD class pharmacokinetic, pharmacogenetic, and efficacy data |
| [NCT05935553](https://clinicaltrials.gov/study/NCT05935553) | Phase 2/3 | Recruiting | 93 | Baclofen (GABA-B agonist) for improving BZD dose titration in BZD-dependent patients; explores complementary GABAergic pharmacology |
| [NCT00287794](https://clinicaltrials.gov/study/NCT00287794) | N/A | Unknown | 1,000 | Prospective characterisation of sleep quality in rheumatoid arthritis patients; evaluates sleep structure and disturbance as comorbid outcomes |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6113175](https://pubmed.ncbi.nlm.nih.gov/6113175/) | 1981 | RCT | J Int Med Research | 7-day double-blind RCT of diazepam 5 mg vs lormetazepam 1 mg in 100 insomnia patients; diazepam demonstrated measurable hypnotic efficacy with reduced sleep latency and extended sleep duration |
| [39581171](https://pubmed.ncbi.nlm.nih.gov/39581171/) | 2024 | Review | Bioorganic Chemistry | Comprehensive review of GABA-A receptor modulators in clinical use; confirms diazepam as the prototypical positive allosteric modulator for epilepsy, anxiety, and insomnia |
| [35228700](https://pubmed.ncbi.nlm.nih.gov/35228700/) | 2022 | Basic Science | Nature Neuroscience | Long-term diazepam causes microglial spine engulfment via TSPO, impairing dendritic structural plasticity and cognitive performance in mice; critical safety signal for chronic hypnotic use |
| [6114852](https://pubmed.ncbi.nlm.nih.gov/6114852/) | 1981 | Review | Drugs | Clinical review of BZD hypnotics for acute and chronic insomnia; positions shorter-acting agents against longer-acting diazepam with respect to sleep architecture and next-day residual effects |
| [29479317](https://pubmed.ncbi.nlm.nih.gov/29479317/) | 2018 | Review | Front Pharmacology | Systematic review of Suanzaoren formulae for insomnia against high-quality RCTs; uses diazepam as active comparator, confirming its reference standard status in insomnia trials |
| [40583063](https://pubmed.ncbi.nlm.nih.gov/40583063/) | 2025 | Clinical Study | Cell Mol Biol Letters | Long-term BZD (diazepam) and Z-drug use associated with exacerbated breast cancer risk via GABA-A signalling; important long-term safety consideration for insomnia treatment |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analysis | Acta Pharmaceutica | Meta-analysis of tranquilizer use in elderly patients with chronic non-communicable diseases; evaluates BZD dose, clinical outcomes, and adverse effect profiles for sleep disorders |
| [37776625](https://pubmed.ncbi.nlm.nih.gov/37776625/) | 2023 | Animal Study | Food & Function | Goat vs cow milk for insomnia in mouse model; diazepam used as positive hypnotic control, demonstrating consistent benchmarking role across preclinical studies |
| [40347763](https://pubmed.ncbi.nlm.nih.gov/40347763/) | 2025 | Animal Study | J Pharm Biomed Analysis | Yiyin Anshen Granule for sleep-deprived insomnia mice; diazepam as positive control evaluating GABAergic neurotransmitter modulation and sleep extension |
| [34983880](https://pubmed.ncbi.nlm.nih.gov/34983880/) | 2021 | Animal Study | Exp Neurobiology | Validation of thyroxine-induced insomnia model via sympathetic stimulation; diazepam as predictive positive control confirming model face and construct validity |

---

## Netherlands Market Information

No CBG-MEB marketing authorizations for Diazepam were identified in the current dataset.

| RVG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | No registrations found | — | — |

> **Note for reviewers**: The absence of registered products likely reflects a data retrieval gap rather than actual market absence. Diazepam is a well-established generic medicine available across the EU under multiple product names. Manual verification via the [CBG-MEB product database](https://www.cbg-meb.nl/) or the EMA medicines database is strongly recommended before drawing any regulatory conclusions.

---

## Safety Considerations

Complete safety data (SmPC warnings and contraindications) is not available for this Evidence Pack entry. No drug-drug interaction data was retrieved.

Please refer to the SmPC (Samenvatting van de Productkenmerken) for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Diazepam's hypnotic mechanism is directly and robustly established — this TxGNN prediction reflects confirmed pharmacology rather than a novel repurposing discovery. A direct head-to-head RCT (PMID 6113175) and multiple review articles confirm hypnotic efficacy in insomnia patients, supporting an L2 evidence level. The primary clinical challenge is not whether diazepam works for insomnia, but rather its unfavourable long-term risk-benefit profile: dependence liability, cognitive impairment (including risk of dementia with chronic use), fall risk in elderly patients, and rebound insomnia on discontinuation are all well-documented and have led to increasing prescribing restrictions across Europe.

**To proceed, the following is needed:**
- Manual verification of CBG-MEB registration status and available SmPC documents for diazepam products in the Netherlands
- MOA data retrieval from DrugBank API to formally resolve data gap DG002
- Complete SmPC warnings, contraindications, and indication text via EMA/CBG-MEB document review (data gap DG001)
- Alignment assessment with current NHG (Nederlands Huisartsen Genootschap) prescribing guidelines for insomnia and anxiolytics
- Scope definition: confirm whether this evaluation targets short-term (≤4 weeks) or a novel long-term formulation/delivery strategy
- Risk management plan addressing maximum treatment duration, supervised tapering protocols, monitoring for dependence, and contraindicated populations (elderly, respiratory disease, pregnancy)
- Pharmacovigilance strategy covering cognitive effects, fall risk, and potential cancer signal with prolonged use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

