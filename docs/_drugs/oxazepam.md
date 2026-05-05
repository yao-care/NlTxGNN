---
layout: default
title: Oxazepam
parent: 僅模型預測 (L5)
nav_order: 101
evidence_level: L5
indication_count: 1
---

# Oxazepam
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

Using the `txgnn-pipeline` skill to confirm context. Now generating the evaluation report based on the Evidence Pack.

---

# Oxazepam: From Anxiety Disorders to Insomnia

## One-Sentence Summary

Oxazepam is a medium-acting benzodiazepine (BZD) primarily established as an anxiolytic and sedative-hypnotic agent within its drug class.
The TxGNN model predicts it may be effective for **Insomnia**,
with **0 registered clinical trials** and **11 publications** currently supporting this direction.
Notably, 2 of those publications are randomized controlled trials directly evaluating Oxazepam in sleep-disturbed patients.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in the Netherlands; established pharmacologically as an anxiolytic/sedative (benzodiazepine class) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L2 |
| NL Market Status | Not marketed in the Netherlands |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Oxazepam is a benzodiazepine that acts by binding to the α subunit of the GABA-A receptor, positively modulating the inhibitory effects of GABA. This mechanism shortens sleep latency, increases total sleep time, and suppresses REM sleep — the same pharmacological effects underpinning all BZD-class hypnotics and directly relevant to insomnia treatment. As a medium-acting agent (t½ ≈ 8–12 hours) with **no active metabolites**, Oxazepam carries a theoretically lower risk of next-day residual sedation compared to long-acting BZDs such as flurazepam, which may offer a practical tolerability advantage in clinical use.

The mechanistic overlap between anxiolysis and hypnosis in this drug class is well-established: GABA-A receptor-mediated CNS depression simultaneously reduces anxiety and promotes sleep onset. Since anxiety and insomnia are highly comorbid and share common neurobiological substrates, the TxGNN model's prediction of efficacy in insomnia is entirely consistent with Oxazepam's known mechanism of action. The transition from anxiolytic use to a sleep indication represents a **within-class pharmacological extension**, not a mechanistic leap.

Clinical literature reinforces this plausibility. A 1984 polysomnographic RCT (PMID 6691478) directly compared Oxazepam and flurazepam in chronic insomnia patients, demonstrating improvement in nocturnal sleep measures with markedly less daytime sedation for Oxazepam. A 2018 comparative RCT in post-STEMI patients (PMID 29749262) further used Oxazepam as an active comparator for managing both anxiety and sleep quality, confirming its real-world application for sleep disturbance in medically ill populations.

---

## Clinical Trial Evidence

Currently no related clinical trials registered on ClinicalTrials.gov or ICTRP for Oxazepam in insomnia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [6691478](https://pubmed.ncbi.nlm.nih.gov/6691478/) | 1984 | RCT | Am J Psychiatry | Polysomnographic RCT (n=14) in chronic insomnia: both Oxazepam and flurazepam improved nocturnal sleep; Oxazepam produced significantly less daytime sleepiness, supporting a more favourable daytime safety profile |
| [29749262](https://pubmed.ncbi.nlm.nih.gov/29749262/) | 2018 | RCT | Ann Pharmacother | Comparative RCT in STEMI patients post-PCI: melatonin vs Oxazepam for anxiety and sleep quality; confirms Oxazepam's active role in managing sleep disorders in acutely ill cardiac patients |
| [17317444](https://pubmed.ncbi.nlm.nih.gov/17317444/) | 2007 | Review | Arch Gerontol Geriatr | Review of hypnotic safety and efficacy in elderly patients (>70 years) with comorbidities including dementia; evaluates BZDs including Oxazepam for insomnia management in high-risk populations |
| [29844949](https://pubmed.ncbi.nlm.nih.gov/29844949/) | 2018 | Observational | PeerJ | Retrospective observational study on long-term BZD/z-drug use in older adults; identifies patient-level factors (age, sex, depression, chronic disease) associated with prolonged BZD use including Oxazepam for insomnia |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opin Drug Metab Toxicol | Pharmacokinetic review of anxiolytic/hypnotic drugs; provides comparative PK profile of Oxazepam (no active metabolites, medium t½) relevant to its sleep application |
| [36340306](https://pubmed.ncbi.nlm.nih.gov/36340306/) | 2022 | Clinical Guideline | J Clin Exp Hepatol | Clinical guideline on alcohol withdrawal syndrome in liver disease; references BZDs including Oxazepam for managing insomnia as a withdrawal symptom, with hepatic safety considerations |
| [6139491](https://pubmed.ncbi.nlm.nih.gov/6139491/) | 1983 | Case Report | JAMA | Two-case report on withdrawal syndrome following substitution of Oxazepam (short-acting) for diazepam (long-acting); relevant to discontinuation risk management in insomnia treatment |
| [15633073](https://pubmed.ncbi.nlm.nih.gov/15633073/) | 2005 | Clinical Review | Psychiatr Praxis | Cross-sectional review of BPSD management in dementia patients in Germany/Austria/Switzerland; includes Oxazepam for sleep-related behavioural disturbances |
| [39544757](https://pubmed.ncbi.nlm.nih.gov/39544757/) | 2024 | Case Report | Am J Transl Res | Case report of agomelatine-induced adverse effect; Oxazepam recorded as concomitant medication for insomnia, providing a contemporary real-world usage reference |
| [23338224](https://pubmed.ncbi.nlm.nih.gov/23338224/) | 1997 | Drug Review | CNS Drugs | Review of paroxetine in panic disorder; Oxazepam cited as representative BZD comparator, contextualising its class pharmacology across anxiolytic and hypnotic indications |

---

## Netherlands Market Information

Oxazepam currently holds **no marketing authorizations** registered with CBG-MEB in the Netherlands. Any clinical use would require off-label prescription, magistral preparation, or import via Article 3(2) exemption under Dutch medicines law (Geneesmiddelenwet). There is no approved SmPC on file with CBG-MEB; the EMA-level product information (where available for the BZD class) should be consulted as the closest reference document.

---

## Safety Considerations

Formal SmPC-level warning and contraindication data is not available in this evidence pack for the Dutch market. Please refer to the Summary of Product Characteristics (SmPC / Samenvatting van de Productkenmerken) from a reference country authorization for full safety information.

Key class-level considerations known for benzodiazepines that clinicians should review prior to use:
- **Dependence and withdrawal risk**: BZDs carry a recognized risk of physical dependence with long-term use; abrupt discontinuation may precipitate withdrawal seizures (see PMID 6139491).
- **Elderly populations**: Particular caution is warranted in patients >70 years due to fall risk, cognitive effects, and accumulation in polypharmacy contexts (see PMID 17317444, 29844949).
- **Hepatic impairment**: Unlike many BZDs, Oxazepam undergoes direct glucuronidation without hepatic oxidation, which may be relevant in patients with liver disease (see PMID 36340306).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction score of 99.86% is supported by a coherent and well-understood mechanism of action (GABA-A receptor modulation), two randomized controlled trials directly evaluating Oxazepam in sleep-disturbed patients, and a broader body of BZD class literature on insomnia. The predicted indication is pharmacologically contiguous with the drug's established anxiolytic use, and Oxazepam's PK profile (no active metabolites, medium half-life) offers a theoretically differentiated position within the BZD class.

**To proceed, the following is needed:**

- **Regulatory pathway clarification**: Confirm whether CBG-MEB registration, EMA mutual recognition, or off-label use pathway applies; obtain reference SmPC (e.g., from UK, Germany, or France where Oxazepam holds authorizations).
- **Full safety data**: Retrieve approved SmPC warnings, contraindications, and drug interaction data via official regulatory sources before prescribing or protocol development.
- **Dependence and withdrawal risk management plan**: Any insomnia indication trial or off-label use protocol must include a structured BZD tapering and discontinuation strategy.
- **Elderly-specific assessment**: Given the prominence of insomnia in older adults and the known BZD risks in this population, a geriatric risk-benefit evaluation (e.g., Beers Criteria, STOPP/START) is recommended.
- **Comparison with approved hypnotics**: Position Oxazepam against currently authorized first-line insomnia treatments in the Netherlands (e.g., temazepam, z-drugs) to define the clinical niche and patient population where Oxazepam would offer incremental value.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

