---
layout: default
title: Acarbose
parent: 僅模型預測 (L5)
nav_order: 13
evidence_level: L5
indication_count: 9
---

# Acarbose
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

# Acarbose: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

Acarbose is an α-glucosidase inhibitor widely used for the treatment of Type 2 Diabetes Mellitus by slowing carbohydrate digestion and reducing postprandial blood glucose spikes. The TxGNN model predicts it may be effective for **Focal Stiff Limb Syndrome**, but with **0 clinical trials** and **0 publications** supporting this specific direction, the prediction lacks any corroborating evidence. Among all 9 predicted indications, none had clinical trial support, and only **Pancreatic Agenesis** (rank 9) had marginally related literature (11 publications, mostly about diabetes management in general).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (postprandial hyperglycaemia) |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 — Model prediction only, no actual studies |
| NL Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

**Short answer: it is not.** The expert mechanistic assessment concludes there is no reasonable mechanistic link between Acarbose and focal stiff limb syndrome.

Acarbose is an α-glucosidase inhibitor that acts locally in the small intestine. It competitively and reversibly inhibits pancreatic α-amylase and membrane-bound intestinal α-glucoside hydrolases, delaying the digestion of complex carbohydrates and disaccharides into absorbable monosaccharides. This reduces the rate of glucose absorption and lowers postprandial blood glucose and insulin peaks. Its pharmacological activity is confined to the gastrointestinal tract, with minimal systemic absorption (<2%).

Focal stiff limb syndrome is a variant of Stiff Person Spectrum Disorder (SPSD), an autoimmune neurological condition mediated by anti-GAD65 (glutamic acid decarboxylase) antibodies. The pathophysiology involves disrupted GABAergic neurotransmission in the central nervous system, leading to continuous motor unit activity, rigidity, and painful spasms — typically confined to one limb. Standard treatment involves GABAergic agents (diazepam, baclofen) or immunomodulatory therapy (IVIg, rituximab, plasmapheresis).

The only theoretical link is that GAD (glutamic acid decarboxylase) is expressed in both pancreatic β-cells and the central nervous system. However, inhibiting intestinal α-glucosidase does not affect GAD function, GABA synthesis, or autoimmune pathways. The TxGNN model likely assigned a high score based on structural proximity within the knowledge graph rather than genuine pharmacological reasoning. This interpretation is further supported by the observation that ranks 1 and 2 (focal stiff limb syndrome and classic stiff person syndrome) received identical scores (0.9965), suggesting ontological adjacency rather than independent pharmacological evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered for Acarbose in focal stiff limb syndrome.

*Searches were conducted on ClinicalTrials.gov and the WHO ICTRP on 2026-03-10, yielding 0 results.*

## Literature Evidence

Currently no related literature available for Acarbose in focal stiff limb syndrome.

*A PubMed search was conducted on 2026-03-10, yielding 0 results.*

## Netherlands Market Information

Acarbose currently holds **no marketing authorizations** in this jurisdiction. Market status is recorded as "Not marketed."

*Note: Acarbose is marketed in many other countries (e.g., Glucobay/Precose by Bayer) for Type 2 Diabetes Mellitus. The absence of a local authorization represents a significant barrier to any repurposing effort in this market.*

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information.

*Note: Safety data (key warnings, contraindications, and drug-drug interactions) could not be retrieved for this evaluation. The data gaps are classified as "Blocking" severity — safety assessment cannot proceed without SmPC/label warnings. As a well-established global medicine, Acarbose's known class effects include flatulence, diarrhoea, abdominal pain, and rare hepatotoxicity. It is contraindicated in inflammatory bowel disease, intestinal obstruction, and severe renal impairment (known from international labels).*

## Additional Predicted Indications Overview

Since the primary prediction lacks all supporting evidence, the full set of 9 predicted indications is summarized below for completeness:

| Rank | Predicted Disease | TxGNN Score | Evidence Level | Mechanistic Link | Recommendation |
|------|------------------|-------------|----------------|-----------------|----------------|
| 1 | Focal stiff limb syndrome | 99.65% | L5 | None | Hold |
| 2 | Classic stiff person syndrome | 99.65% | L5 | None | Hold |
| 3 | Thiamine-responsive dysfunction syndrome | 99.62% | L5 | None | Hold |
| 4 | Opsismodysplasia | 99.62% | L5 | None | Hold |
| 5 | Drug-induced localized lipodystrophy | 99.24% | L5 | Very weak indirect | Hold |
| 6 | Centrifugal lipodystrophy | 99.22% | L5 | None | Hold |
| 7 | Pressure-induced localized lipoatrophy | 99.20% | L5 | None | Hold |
| 8 | Idiopathic localized lipodystrophy | 99.17% | L5 | None | Hold |
| 9 | Pancreatic agenesis | 99.16% | L4 | Weak indirect | Research Question |

**Pattern analysis:** The four lipodystrophy-related predictions (ranks 5–8) have highly similar scores (0.9917–0.9924), and the two stiff person spectrum disorders (ranks 1–2) share identical scores. This strongly suggests the TxGNN model is propagating predictions based on disease ontology clustering rather than independent pharmacological reasoning — a known bias pattern in knowledge-graph-based predictions.

### Pancreatic Agenesis — The Only Indication with Literature

Pancreatic agenesis (rank 9) is the only predicted indication with any literature. However, the 11 retrieved publications are largely about general diabetes management and do not specifically study Acarbose for pancreatic agenesis. Key publications:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10094112](https://pubmed.ncbi.nlm.nih.gov/10094112/) | 1999 | Preclinical | Metabolism | Acarbose prevented/reversed metabolic abnormalities in OLETF diabetic rats, preserving β-cell function |
| [21697254](https://pubmed.ncbi.nlm.nih.gov/21697254/) | 2011 | Review | J Clin Endocrinol Metab | Acarbose discussed as one of several agents for β-cell preservation in prediabetes |
| [9506190](https://pubmed.ncbi.nlm.nih.gov/9506190/) | 1998 | Review | Adv Intern Med | General overview of Type 2 DM pathophysiology and treatment including α-glucosidase inhibitors |
| [12877088](https://pubmed.ncbi.nlm.nih.gov/12877088/) | 2003 | Review | Nihon Rinsho | α-glucosidase inhibitors benefit postprandial hyperglycaemia in metabolic syndrome |
| [30572448](https://pubmed.ncbi.nlm.nih.gov/30572448/) | 2018 | Case Report | Medicine | Insulin autoimmune syndrome cases — acarbose mentioned as potential trigger |

*The mechanistic link is weak and indirect: Acarbose could theoretically assist with blood glucose management in pancreatic agenesis patients, but it cannot treat the underlying congenital defect, and these patients require exogenous insulin as primary therapy.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 9 predicted indications for Acarbose lack clinical trial evidence. The top prediction (focal stiff limb syndrome) has no mechanistic plausibility — an intestinal α-glucosidase inhibitor has no known pathway to affect autoimmune GABAergic neurological disorders. The prediction pattern (identical scores for ontologically related diseases, clustering of lipodystrophy subtypes) indicates knowledge-graph structural bias rather than genuine pharmacological signal. Furthermore, Acarbose holds no marketing authorization in this jurisdiction, adding a regulatory barrier.

**To proceed, the following would be needed:**
- Identification of a biologically plausible mechanism linking α-glucosidase inhibition to any of the predicted conditions
- At minimum one preclinical study or case report demonstrating a therapeutic effect
- Retrieval of complete SmPC safety data (currently classified as a Blocking data gap)
- Marketing authorization or access pathway in this jurisdiction
- For pancreatic agenesis (the only indication with any literature): a clinical case series or pilot study specifically evaluating Acarbose as adjunctive therapy in congenital pancreatic insufficiency

---

*This report was generated on 2026-04-03 based on evidence collected up to 2026-04-03. Results are for research purposes only and do not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

