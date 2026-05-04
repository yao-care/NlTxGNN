---
layout: default
title: Bimatoprost
parent: 僅模型預測 (L5)
nav_order: 31
evidence_level: L5
indication_count: 10
---

# Bimatoprost
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

# Bimatoprost: From Glaucoma to Malformation Syndrome with Odontal and/or Periodontal Component

## One-Sentence Summary

Bimatoprost is a synthetic prostamide F2α analogue originally approved for ocular hypertension / open-angle glaucoma (Lumigan) and eyelash hypotrichosis (Latisse) in multiple jurisdictions.
The TxGNN model predicts it may be relevant for **malformation syndrome with odontal and/or periodontal component** — a rare congenital syndrome featuring structural dental and periodontal developmental abnormalities — with the highest TxGNN score among all predicted candidates (**99.997%**).
However, **0 clinical trials** and **0 publications directly evaluating Bimatoprost in this indication** currently exist; the 20 retrieved publications describe general periodontal biology and are not specific to this drug.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Glaucoma / Ocular hypertension (Lumigan); Eyelash hypotrichosis (Latisse) — based on known approvals in other jurisdictions (no NL authorisation on file) |
| Predicted New Indication | Malformation syndrome with odontal and/or periodontal component |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L5 |
| NL Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Bimatoprost activates FP (prostaglandin F) receptors and prostamide receptors. In ophthalmology, this lowers intraocular pressure by increasing aqueous humour outflow; in dermatology, the same receptor pathway extends the anagen (growth) phase of hair follicles — a serendipitous observation that led to its FDA approval for eyelash hypotrichosis (Latisse). The drug therefore has two mechanistically distinct but well-characterised approved uses.

The theoretical bridge to odontal/periodontal pathology rests on the known role of **prostaglandin E2 (PGE2)** in periodontal bone resorption and gingival inflammation. Because bimatoprost is a prostaglandin structural analogue, the TxGNN knowledge graph may have connected it to this pathway through shared receptor or signalling nodes. In principle, a prostamide analogue could modulate prostaglandin-related cascades involved in periodontal tissue homeostasis and alveolar bone metabolism.

In practice, however, the connection is highly indirect. The target entity — **malformation syndrome with odontal and/or periodontal component** — encompasses rare congenital syndromes (such as Papillon-Lefèvre syndrome or related ectodermal dysplasias) caused by germline mutations in structural or immune-regulatory genes. Prostamide/FP receptor agonism has no established role in correcting or modifying the underlying developmental defects. The TxGNN high score most plausibly reflects shared pathway proximity in the knowledge graph rather than a pharmacologically tractable indication. This prediction is assessed as mechanistically implausible for the specific orphan disease entity at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Bimatoprost in this indication.

---

## Literature Evidence

The following publications were retrieved in the evidence search. They describe the biology and treatment of periodontal disease as the putative target pathway — **none directly evaluate Bimatoprost for this specific indication**. They are included here as background on the target disease mechanism only.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35420698](https://pubmed.ncbi.nlm.nih.gov/35420698/) | 2022 | Systematic Review | Cochrane Database of Systematic Reviews | Periodontal treatment (SRP) produces modest but statistically significant improvement in glycaemic control in patients with diabetes and periodontitis |
| [22057194](https://pubmed.ncbi.nlm.nih.gov/22057194/) | 2012 | Review | Diabetologia | Bidirectional relationship between diabetes and periodontitis established; diabetes increases periodontitis susceptibility approximately threefold |
| [35688447](https://pubmed.ncbi.nlm.nih.gov/35688447/) | 2022 | Clinical Practice Guideline | Journal of Clinical Periodontology | EFP S3-level guideline for treatment of Stage IV periodontitis, addressing tooth loss sequelae and functional rehabilitation |
| [36883660](https://pubmed.ncbi.nlm.nih.gov/36883660/) | 2023 | Review | Journal of Dental Research | Gingival fibroblasts act as innate immune sentinels in periodontium; key roles in periodontal inflammation and tissue remodelling |
| [37452425](https://pubmed.ncbi.nlm.nih.gov/37452425/) | 2023 | Experimental | Advanced Science | M2 macrophage-derived exosomes engineered with melatonin shown to modulate immune microenvironment and reduce periodontal bone loss in animal models |
| [38362600](https://pubmed.ncbi.nlm.nih.gov/38362600/) | 2024 | Observational | Journal of Dental Research | Stage III/IV periodontitis patients show oral–gut microbial dysbiosis; subgingival instrumentation partially restores microbiota (n=47) |
| [38907216](https://pubmed.ncbi.nlm.nih.gov/38907216/) | 2024 | Review | Journal of Nanobiotechnology | Biomaterial-mediated macrophage immunotherapy as an emerging strategy for periodontal regeneration |
| [37435999](https://pubmed.ncbi.nlm.nih.gov/37435999/) | 2023 | Review | Periodontology 2000 | Complications of regenerative periodontal surgery reviewed, including membrane exposure and infection risk |
| [20599785](https://pubmed.ncbi.nlm.nih.gov/20599785/) | 2010 | Review | Biochemical Pharmacology | Complement system overactivation contributes to immunopathology in periodontitis; potential therapeutic target identified |
| [9495612](https://pubmed.ncbi.nlm.nih.gov/9495612/) | 1998 | Observational | Journal of Clinical Periodontology | Foundational characterisation of microbial complexes in subgingival plaque (n=185); "red complex" pathogens associated with severe disease |

---

## Netherlands Market Information

Bimatoprost currently holds **no marketing authorisations (RVG numbers)** registered with the CBG-MEB. It is not available through standard NL market channels.

> **Note for prescribers:** In other EU jurisdictions bimatoprost is available as Lumigan (glaucoma, EMA centrally authorised) and as Latisse (eyelash hypotrichosis, national authorisations in several countries). For compassionate use, named-patient supply, or off-label prescribing in the Netherlands, a formal CBG-MEB or hospital pharmacy assessment would be required.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics / Samenvatting van de Productkenmerken) of authorised bimatoprost products (e.g., Lumigan SmPC via EMA) for full safety information, including contraindications, special warnings, and drug interactions. No NL SmPC data were available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns the highest prediction score in this candidate set to bimatoprost for malformation syndrome with odontal/periodontal component, but no clinical or direct preclinical evidence supports this link. The proposed mechanism through prostaglandin signalling is highly speculative and does not address the congenital developmental aetiology of the target syndrome. This is a model-only signal (L5) with no translational basis identified.

**To proceed, the following is needed:**

- **Mechanistic validation:** Establish whether prostamide/FP receptor agonism has any measurable effect in in vitro models of periodontal ligament cells, dental follicle cells, or relevant gene-knockout models mimicking the target syndrome
- **Target clarification:** Determine whether the TxGNN prediction refers to the developmental malformation syndrome entity specifically, or conflates it with acquired periodontitis (for which the retrieved literature applies)
- **SmPC review:** Obtain and review the full EMA-authorised Lumigan SmPC for contraindications and warnings before any further evaluation
- **Alternative candidates:** Consider prioritising the Bimatoprost × **Alopecia** indication (rank 8 in this evidence pack; L2 evidence, 11 completed Phase 2 RCTs, n=244–307), which presents a far stronger evidence base and a direct mechanistic rationale — this may represent the more actionable repurposing opportunity from this prediction set
- **CBG-MEB registration status:** Clarify the regulatory pathway required to bring bimatoprost into the NL market for any indication, given zero current authorisations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

