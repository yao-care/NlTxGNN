---
layout: default
title: Nitrazepam
parent: 僅模型預測 (L5)
nav_order: 98
evidence_level: L5
indication_count: 3
---

# Nitrazepam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Using the `txgnn-pipeline` skill to guide this NL-country drug repurposing report, and now producing the evaluation report from the Evidence Pack.

---

# Nitrazepam: From Sedative-Hypnotic to Sleep Disorder (Initiating and Maintaining Sleep)

## One-Sentence Summary

Nitrazepam is a benzodiazepine compound known internationally as a sedative-hypnotic; it carries no current marketing authorization in the Netherlands.
The TxGNN model predicts it may be effective for **sleep disorder, initiating and maintaining sleep**, with a prediction score of **99.89%**.
This direction is supported by **0 registered clinical trials** and **20 publications**, and notably aligns with the drug's established pharmacological use in countries where it is authorized — making this a regulatory access question as much as a scientific one.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No NL (CBG-MEB) authorization on record; internationally known as a sedative-hypnotic |
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 (clinical comparison studies and reviews; no registered Phase 2/3 trials) |
| NL Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Nitrazepam belongs to the benzodiazepine class. Benzodiazepines act as positive allosteric modulators of the GABA-A receptor, enhancing the inhibitory effect of gamma-aminobutyric acid in the central nervous system. This produces sedative, hypnotic, anxiolytic, and anticonvulsant effects — mechanisms that are directly relevant to the initiation and maintenance of sleep.

The predicted indication is not a novel repurposing in the classical sense. Nitrazepam's hypnotic use has been established for decades in countries including the United Kingdom, Japan, and Canada, where it is marketed under brand names such as Mogadon. The TxGNN model's high prediction score (99.89%) reflects this strong mechanistic and clinical alignment. Multiple comparative studies in the literature confirm nitrazepam's efficacy as a hypnotic, showing performance comparable to triazolam, flunitrazepam, brotizolam, and zolpidem in head-to-head clinical studies.

The key question for the Netherlands context is therefore not whether nitrazepam works for insomnia, but whether its benefit-risk profile — particularly risks of dependence (documented as early as 1975), next-day residual sedation, and cognitive impairment in elderly populations — justifies pursuing market access in an environment where CBG-MEB/EMA has authorized several alternative agents and where Dutch clinical guidelines (NHG-standaard) increasingly favour non-pharmacological first-line approaches such as cognitive behavioural therapy for insomnia (CBT-I).

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for Nitrazepam in the indication of sleep disorder (initiating and maintaining sleep).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [4892037](https://pubmed.ncbi.nlm.nih.gov/4892037/) | 1969 | Clinical trial (double-blind) | British Medical Journal | 27 overdose patients and a double-blind ward trial: nitrazepam was as effective as butobarbitone as a hypnotic with no untoward effects even at high doses. Concluded safe and effective. |
| [6135296](https://pubmed.ncbi.nlm.nih.gov/6135296/) | 1983 | RCT (double-blind cross-over) | Acta Psychiatrica Scandinavica | 26 geriatric inpatients: triazolam 0.25 mg vs nitrazepam 5 mg. Sleep quantity, quality, and psychomotor performance were similar for both drugs. |
| [7037262](https://pubmed.ncbi.nlm.nih.gov/7037262/) | 1981 | Review | Clinical Pharmacokinetics | Comprehensive pharmacokinetics review of nitrazepam, covering half-life, distribution, and dosing implications — foundational for clinical use planning. |
| [3281819](https://pubmed.ncbi.nlm.nih.gov/3281819/) | 1988 | Review | Drugs | Brotizolam pharmacology review with direct clinical comparison to nitrazepam 2.5–5 mg: efficacy for insomnia was equivalent across controlled trials. |
| [10804040](https://pubmed.ncbi.nlm.nih.gov/10804040/) | 2000 | Review | Drugs | Zolpidem update: hypnotic efficacy comparable to nitrazepam, flurazepam, flunitrazepam, and temazepam in elderly insomniacs; positions nitrazepam within the benzodiazepine comparator landscape. |
| [15089115](https://pubmed.ncbi.nlm.nih.gov/15089115/) | 2004 | Review | CNS Drugs | Reviews epidemiological evidence linking hypnotics including nitrazepam to next-day psychomotor impairment, increased accident risk, and clinical management implications. |
| [19450355](https://pubmed.ncbi.nlm.nih.gov/19450355/) | 2007 | Review | BMJ Clinical Evidence | Up to 40% of adults experience insomnia; prevalence increases with age. Reviews risk factors, diagnosis, and evidence-based treatment options relevant to positioning any hypnotic. |
| [14960254](https://pubmed.ncbi.nlm.nih.gov/14960254/) | 2004 | HTA / RCT | Health Technology Assessment | CBT-I evaluated in long-term hypnotic users (including nitrazepam users) in UK general practice; demonstrates that psychological treatment can reduce dependence on drugs like nitrazepam. |
| [1125532](https://pubmed.ncbi.nlm.nih.gov/1125532/) | 1975 | Case report | British Journal of Psychiatry | Early documentation of nitrazepam (Mogadon) dependence — a key safety signal directly relevant to long-term insomnia management risk assessment. |
| [39231170](https://pubmed.ncbi.nlm.nih.gov/39231170/) | 2024 | Observational | PLoS One | Benzodiazepine prescribing pattern analysis in primary care: long-term use associated with dependence, tolerance, and cognitive decline, especially in older adults. Reinforces the need for careful prescribing and deprescribing strategies. |

---

## Netherlands Market Information

Nitrazepam currently holds **no CBG-MEB marketing authorization** in the Netherlands and is not listed in the NL medicines registry. No approved indications, dosage forms, or RVG numbers are on record.

Clinicians wishing to use nitrazepam in the Netherlands would need to pursue one of the following pathways:

- **Magistrale bereiding** (extemporaneous compounding) — subject to Dutch pharmacy regulations under the Geneesmiddelenwet
- **Named-patient import** — requires CBG-MEB notification and justification under Article 40(3) of the Dutch Medicines Act
- **Full marketing authorization application** — via the EMA centralized procedure or CBG-MEB national procedure

Currently authorized alternatives in the Netherlands for insomnia include temazepam, lormetazepam, and zolpidem, all of which would serve as the relevant clinical comparators in any regulatory submission.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for full safety information, as no drug-specific warnings or contraindication data were available in this evidence pack.

Based on the benzodiazepine drug class and literature evidence retrieved, the following class-level considerations are clinically relevant:

- **Dependence and withdrawal**: Documented nitrazepam dependence exists (PMID 1125532); consistent with general benzodiazepine class risk
- **Residual sedation**: Next-day psychomotor impairment and increased accident risk reported (PMID 15089115); particularly relevant for elderly and driving populations
- **Elderly populations**: Increased sensitivity to sedative effects and cognitive impairment; dosing adjustment typically required
- **Long-term use**: Associated with tolerance, dependence, and cognitive decline in primary care settings (PMID 39231170)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the literature clearly supports nitrazepam's efficacy as a hypnotic for insomnia, the drug has no NL marketing authorization, no registered clinical trials for this indication, and known risks of dependence and residual sedation that require active risk management. Additionally, the predicted indication aligns with the drug's established pharmacological use — not a novel repurposing — making the regulatory and clinical positioning strategy the primary barrier rather than lack of efficacy evidence.

**To proceed, the following is needed:**

- Confirm full mechanism of action documentation via DrugBank API or EMA assessment reports (currently a data gap)
- Obtain the SmPC from a country where nitrazepam is authorized (e.g., UK, Japan) to extract formal warnings and contraindications
- Conduct a regulatory feasibility analysis: assess the named-patient import or full marketing authorization pathway with CBG-MEB
- Review Dutch clinical guidelines (NHG-standaard Slaapproblemen en Slaapmiddelen) to determine whether nitrazepam could be positioned relative to authorized alternatives
- Develop a risk management framework covering dependence monitoring, appropriate patient selection (excluding elderly as first-line), maximum treatment duration, and deprescribing protocols
- Conduct a formal benefit-risk comparison against currently authorized NL hypnotics (temazepam, lormetazepam, zolpidem) to justify the regulatory submission rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

