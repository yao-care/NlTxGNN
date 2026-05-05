---
layout: default
title: Modafinil
parent: 僅模型預測 (L5)
nav_order: 96
evidence_level: L5
indication_count: 1
---

# Modafinil
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

The txgnn-pipeline skill confirms this is NL deployment context. Now I'll generate the full evaluation report based on the Evidence Pack.

---

# Modafinil: From Narcolepsy to Insomnia

## One-Sentence Summary

Modafinil is a wake-promoting agent used internationally for narcolepsy, shift work sleep disorder, and obstructive sleep apnoea, though it holds no CBG-MEB marketing authorisation in the Netherlands.
The TxGNN model predicts it may be effective for **Insomnia**, with **29 clinical trials** and **19 publications** retrieved — however, the vast majority address excessive daytime sleepiness rather than insomnia directly.
Critically, modafinil's pro-wakefulness mechanism is pharmacologically opposite to the sedating action required for primary insomnia treatment, making this prediction plausible only in narrowly defined secondary-insomnia subgroups.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Narcolepsy / Excessive Daytime Sleepiness (globally approved; no NL registration) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L3 |
| NL Market Status | Not registered (no CBG-MEB authorisation) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Modafinil is a wake-promoting agent whose mechanism centres on inhibiting the dopamine transporter (DAT), enhancing histaminergic H1 signalling, and activating the hypothalamic orexin (hypocretin) pathway — together sustaining wakefulness and reducing excessive daytime sleepiness. It is approved in multiple jurisdictions (FDA, EMA) for narcolepsy, residual sleepiness in obstructive sleep apnoea, and shift work sleep disorder. Detailed MOA data was not included in this Evidence Pack; the above is drawn from published evidence-based reviews (PMID 18729534). Currently, detailed mechanism of action data is not available in the regulatory record for the Netherlands. Based on known pharmacological information, modafinil is a wake-promoting stimulant whose efficacy for excessive daytime sleepiness has been firmly established across multiple approved indications.

There is a fundamental **mechanistic paradox** in this prediction. Primary insomnia — characterised by difficulty initiating or maintaining sleep — requires a sedating or sleep-promoting intervention, which is the pharmacological opposite of modafinil's action. The high TxGNN score (99.85%) most likely reflects the model's recognition of broad graph-level adjacency between modafinil and the generic "sleep disorder" disease node, rather than an insomnia-specific therapeutic signal. This distinction is clinically important.

However, a **limited mechanistic rationale does exist for secondary insomnia**: in patients where excessive daytime sleepiness leads to compensatory napping and disrupts the homeostatic sleep drive, modafinil could theoretically normalise daytime wakefulness, consolidate the circadian sleep–wake rhythm, and thereby indirectly improve nocturnal sleep quality. Clinical evidence supports this hypothesis in narrow populations — cancer survivors with chemotherapy-related fatigue and co-occurring insomnia, and patients with neurodegenerative disease whose fragmented sleep is driven by circadian dysregulation. This is a context-specific repurposing hypothesis and does not support broad application of modafinil for primary insomnia.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00124384](https://clinicaltrials.gov/study/NCT00124384) | Phase 4 | Completed | 40 | The only registered trial targeting **primary insomnia** directly with modafinil; examines modafinil alone or in combination with CBT-I to improve daytime functioning and reduce insomnia severity |
| [NCT01019187](https://clinicaltrials.gov/study/NCT01019187) | Phase 2 | Completed | 226 | Randomised trial of CBT-I ± armodafinil (R-enantiomer of modafinil) for **cancer survivor insomnia and fatigue** post-chemotherapy; armodafinil serves as a pharmacological proxy for modafinil |
| [NCT01091974](https://clinicaltrials.gov/study/NCT01091974) | Phase 2 | Completed | 138 | Four-arm RCT of CBT-I and armodafinil in female breast cancer patients with **post-chemotherapy sleep disturbances**; provides the most rigorous direct armodafinil-insomnia dataset |
| [NCT01011218](https://clinicaltrials.gov/study/NCT01011218) | Phase 2 | Completed | 70 | Pilot RCT in breast cancer patients; armodafinil 150 mg/day combined with brief or standard CBT-I to manage **cancer-related insomnia** |
| [NCT02552303](https://clinicaltrials.gov/study/NCT02552303) | N/A | Completed | 39 | Armodafinil, CBT-I, or combination for **insomnia comorbid with obstructive sleep apnoea**; measures sleep continuity and CPAP adherence |
| [NCT06404086](https://clinicaltrials.gov/study/NCT06404086) | Phase 2 | Completed | 830 | RECOVER-SLEEP platform trial: evaluates multiple interventions for **sleep disturbances in long COVID** (PASC); flexible platform design allowing comparative analysis across intervention arms |
| [NCT06404099](https://clinicaltrials.gov/study/NCT06404099) | Phase 2 | Active (not recruiting) | 361 | Second RECOVER-SLEEP platform arm: ongoing evaluation of sleep interventions in post-acute COVID sequelae |
| [NCT01965925](https://clinicaltrials.gov/study/NCT01965925) | Phase 4 | Completed | 18 | 8-week, randomised, placebo-controlled trial of modafinil in **stable bipolar disorder**, targeting both sleep-wake cycle disruption and residual cognitive impairment |
| [NCT07295834](https://clinicaltrials.gov/study/NCT07295834) | Phase 2 | Not yet recruiting | 70 | Double-blind RCT of modafinil vs. placebo (12 weeks) for **severe fatigue in inflammatory bowel disease**; the only forthcoming direct modafinil trial; not yet started |
| [NCT00626210](https://clinicaltrials.gov/study/NCT00626210) | Phase 4 | Terminated | 2 | Modafinil for **sleep/wake disturbances in older adults**; terminated after only 2 participants enrolled — no meaningful conclusions can be drawn |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [18219235](https://pubmed.ncbi.nlm.nih.gov/18219235/) | 2008 | Randomised Trial | J Head Trauma Rehabil | Modafinil reduced fatigue and excessive daytime sleepiness in chronic traumatic brain injury; illustrates that wakefulness normalisation may indirectly benefit fragmented sleep architecture |
| [18729534](https://pubmed.ncbi.nlm.nih.gov/18729534/) | 2008 | Evidence-Based Review | Drugs | Comprehensive review of modafinil's approved and investigational uses across double-blind RCTs; confirms wake-promoting MOA and approved evidence base; no direct insomnia indication found |
| [24312590](https://pubmed.ncbi.nlm.nih.gov/24312590/) | 2013 | Meta-Analysis | PLoS One | Meta-analysis of modafinil for fatigue and EDS in neurological disorders; results inconsistent across conditions; no demonstrated direct improvement of nocturnal sleep |
| [22021174](https://pubmed.ncbi.nlm.nih.gov/22021174/) | 2011 | Systematic Review / EBM | Movement Disorders | MDS evidence-based review of Parkinson's non-motor symptom treatments including sleep; modafinil recommended for EDS but evidence base for insomnia in PD remains insufficient |
| [27010071](https://pubmed.ncbi.nlm.nih.gov/27010071/) | 2016 | Systematic Review | Parkinsonism Relat Disord | Systematic review of pharmacological interventions for daytime sleepiness in Parkinson's; highlights that few high-quality trials address insomnia specifically |
| [39535843](https://pubmed.ncbi.nlm.nih.gov/39535843/) | 2024 | Narrative Review | Expert Opin Pharmacother | Most current review of sleep dysfunction in Parkinson's; notes modafinil role in managing EDS but underlines that nocturnal insomnia management in PD remains an unmet need |
| [20082966](https://pubmed.ncbi.nlm.nih.gov/20082966/) | 2009 | Review | Parkinsonism Relat Disord | Describes narcolepsy-like napping in Parkinson's disease; modafinil addresses daytime symptoms but has not been shown to improve nighttime sleep in this population |
| [18805301](https://pubmed.ncbi.nlm.nih.gov/18805301/) | 2008 | Review | Rev Neurol | Review of narcolepsy with cataplexy; notes sleep maintenance insomnia as a co-occurring feature of narcolepsy and discusses modafinil's primary role in daytime symptom control |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Review | Drug Des Dev Ther | Profiles pitolisant as a newer narcolepsy treatment; provides comparative context for modafinil's mechanism and its limitations in addressing nocturnal sleep disruption |
| [17060310](https://pubmed.ncbi.nlm.nih.gov/17060310/) | 2006 | Case Series | Am J Hosp Palliat Care | Modafinil reduced fatigue in Charcot-Marie-Tooth disease type 1A; illustrates off-label use pattern in fatigue-predominant conditions with secondary sleep disruption |

---

## Netherlands Market Information

Modafinil currently holds **no CBG-MEB marketing authorisation** in the Netherlands and does not appear in the Dutch national medicines register. Any prescribing in the Netherlands would require an individual import authorisation, a named-patient supply arrangement, or an off-label use pathway, each requiring explicit clinical justification and pharmacovigilance planning.

| RVG Number | Product Name | Dosage Form | Approved Indication |
|-----------|-------------|-------------|---------------------|
| — | No registered products | — | — |

---

## Safety Considerations

Please refer to the **SmPC (Summary of Product Characteristics / Samenvatting van de Productkenmerken)** for safety information.

Given the absence of a CBG-MEB authorisation and the lack of safety data in this Evidence Pack, the EMA SmPC for the EU-registered modafinil product (where applicable) and published pharmacovigilance literature should be reviewed before any clinical decision. Key areas to examine include hypersensitivity reactions, CYP enzyme interactions, cardiovascular precautions, and potential for dependence or misuse.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score of 99.85% for modafinil in insomnia most likely reflects broad graph-level adjacency to the "sleep disorder" disease cluster rather than a genuine insomnia-specific therapeutic signal. Modafinil's pro-wakefulness mechanism is pharmacologically opposed to primary insomnia treatment; the only evidence of mechanistic plausibility is in secondary insomnia driven by circadian disruption (e.g., cancer-related fatigue, neurodegenerative disease). Direct clinical evidence is limited to one small completed Phase 4 trial (NCT00124384, n=40) plus several armodafinil studies in oncology populations. Modafinil is unregistered in the Netherlands, and critical safety and MOA data gaps remain unresolved.

**To proceed, the following is needed:**

- **Indication scoping**: Determine whether the clinical target is primary insomnia or a specific secondary-insomnia subgroup (e.g., post-chemotherapy, neurodegeneration-related); these require different evidence packages and regulatory strategies
- **Safety documentation**: Obtain the current EMA/nationally authorised SmPC for modafinil to complete the S1 safety assessment — in particular contraindications, warnings, and DDI profile (CYP3A4 interactions are clinically significant)
- **MOA confirmation**: Retrieve DrugBank DB00745 MOA data to formally document mechanism and support or refute the mechanistic hypothesis for the target indication
- **Regulatory landscape check**: Confirm whether EMA or any EU national competent authority has previously reviewed modafinil for an insomnia indication; check for any EPAR entry or prior scientific advice
- **Subgroup literature review**: If pursuing secondary insomnia, commission a focused systematic review in the cancer-survivor and circadian-disruption populations, where the circadian-restoration hypothesis is most mechanistically grounded
- **CBG-MEB pre-submission consultation**: Given zero NL authorisations, early dialogue with CBG-MEB is advisable before initiating any formal development programme in the Netherlands
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

