---
layout: default
title: Allopurinol
parent: 僅模型預測 (L5)
nav_order: 21
evidence_level: L5
indication_count: 10
---

# Allopurinol
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

# Allopurinol: From Gout/Hyperuricemia to Hepatic Porphyria

## One-Sentence Summary

Allopurinol is a xanthine oxidase (XO) inhibitor, widely used for the treatment of gout and hyperuricemia.
The TxGNN model predicts it may be effective for **Hepatic Porphyria**,
but with only **0 clinical trials** and **2 publications** (hypothesis-level and animal study), this prediction currently rests on minimal evidence and warrants significant caution — particularly as allopurinol has been reported to potentially *exacerbate* porphyria.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout, hyperuricemia (well-established globally; no local licenses in current dataset) |
| Predicted New Indication | Hepatic Porphyria |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 — Preclinical/mechanism studies only |
| Market Status | Not marketed (未上市) in current regulatory dataset |
| Number of Authorizations | 0 (in current dataset) |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Allopurinol is a purine analogue whose active metabolite, oxipurinol, inhibits xanthine oxidase (XO), the enzyme responsible for converting hypoxanthine to xanthine and xanthine to uric acid. This mechanism has been clinically validated for decades in the management of gout and hyperuricemia. XO inhibition also reduces the generation of reactive oxygen species (ROS) as a by-product of purine metabolism.

Hepatic porphyrias are a group of metabolic disorders caused by enzyme deficiencies in the heme biosynthesis pathway, leading to accumulation of toxic porphyrin precursors (such as ALA and PBG) in the liver. The rate-limiting enzyme, 5-aminolevulinate synthase (ALAS1), is under negative feedback control by a small regulatory heme pool. In theory, XO inhibition could indirectly alter substrate availability for ALAS1 or influence the redox environment of hepatocytes. However, this mechanistic link is entirely hypothetical and has no direct experimental validation.

Critically, the repurposing rationale from the evidence pack itself flags a major safety concern: **allopurinol has been reported to potentially exacerbate porphyric attacks**. This runs counter to the therapeutic hypothesis and underscores the need for extreme caution. The TxGNN prediction score (99.95%) is high, but the model may be capturing structural proximity in the knowledge graph between purine metabolism and heme biosynthesis pathways rather than a genuine therapeutic relationship. Five of the top six predicted indications are liver-related conditions with nearly identical scores, suggesting a possible neighbourhood effect in the knowledge graph.

## Clinical Trial Evidence

Currently no related clinical trials registered for allopurinol in hepatic porphyria.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothesis/Commentary | Medical Hypotheses | Proposes metabolic targeting of liver ALAS by inhibition of heme utilisation by tryptophan 2,3-dioxygenase (TDO) as a therapy for acute hepatic porphyrias. Discusses regulatory heme pool dynamics — does not directly study allopurinol but provides mechanistic context for heme pathway modulation. |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Animal Study | Biochemical Pharmacology | Examined carbamazepine's effects on heme metabolism in rat liver, specifically how it exacerbates hepatic porphyrias. Provides a screening model for drug-induced porphyria exacerbation — relevant as a framework for evaluating allopurinol's porphyria risk. |

**Note:** Neither publication directly investigates allopurinol as a treatment for hepatic porphyria. The first is a hypothesis paper about heme pathway modulation; the second studies a different drug (carbamazepine) as a porphyria exacerbator.

## Netherlands Market Information

No CBG-MEB marketing authorizations were found in the current dataset for allopurinol. However, allopurinol is a well-established WHO Essential Medicine and is widely available throughout Europe, including the Netherlands, under multiple brand names (e.g., Zyloric). The absence of licenses in this dataset likely reflects a data coverage limitation rather than true market absence.

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for comprehensive safety information.

**Important safety signal for this specific repurposing candidate:**
- The mechanistic rationale itself notes that allopurinol has been reported to potentially **induce or exacerbate porphyric attacks**, which would directly contraindicate its use for the predicted indication (hepatic porphyria). This must be thoroughly investigated before any further evaluation.
- Allopurinol is known to cause severe hypersensitivity reactions (including Stevens-Johnson syndrome and DRESS syndrome), particularly in patients carrying the HLA-B*5801 allele.

## Additional Predicted Indications (Ranked 2–10)

The TxGNN model also predicted the following indications. All are rated **L5 (model prediction only)** with a **Hold** recommendation, as none have clinical trial or literature support:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|---------------------|-------------|----------------|----------------|
| 2 | Hepatopulmonary syndrome | 99.94% | L5 | Hold |
| 3 | Primitive portal vein thrombosis | 99.94% | L5 | Hold |
| 4 | Idiopathic copper-associated cirrhosis | 99.94% | L5 | Hold |
| 5 | Early-onset familial noncirrhotic portal hypertension | 99.94% | L5 | Hold |
| 6 | Hepatoportal sclerosis | 99.94% | L5 | Hold |
| 7 | Disorder of phenylalanine metabolism | 99.89% | L4 | Hold |
| 8 | Immune-mediated necrotizing myopathy | 99.86% | L5 | Hold |
| 9 | Antisynthetase syndrome | 99.85% | L5 | Hold |
| 10 | Idiopathic eosinophilic myositis | 99.85% | L5 | Hold |

**Pattern observation:** Ranks 2–6 share nearly identical TxGNN scores (99.94%) and are all hepatic/portal vein conditions. This clustering strongly suggests the predictions arise from a **knowledge graph neighbourhood effect** — the model recognises allopurinol's metabolic link to liver function and predicts broadly across liver-related disease nodes, rather than identifying specific therapeutic mechanisms.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.95%), the evidence for allopurinol in hepatic porphyria is critically weak: zero clinical trials, only two tangentially related publications (neither directly studying allopurinol for porphyria), and a significant safety concern that allopurinol may actually *worsen* porphyric attacks. The clustering of five liver-related predictions at near-identical scores suggests a knowledge graph artefact rather than a genuine therapeutic signal.

**To proceed, the following would be needed:**
- Preclinical investigation of allopurinol's direct effects on the heme biosynthesis pathway (ALAS1, PBG deaminase)
- A definitive assessment of whether allopurinol induces or exacerbates porphyria in validated animal models
- Detailed mechanism of action (MOA) characterisation relevant to porphyrin metabolism
- Retrieval of SmPC safety data (key warnings, contraindications, drug interactions) from CBG-MEB or EMA sources
- Pharmacogenomic assessment (HLA-B*5801 prevalence in target population)

---

*This report was generated on 2026-04-03 based on evidence pack v4 (data cutoff: 2026-04-03). Results are for research purposes only and do not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

