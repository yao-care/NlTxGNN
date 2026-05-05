---
layout: default
title: Sulpiride
parent: 僅模型預測 (L5)
nav_order: 114
evidence_level: L5
indication_count: 9
---

# Sulpiride
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

Generating the evaluation report now based on the provided Evidence Pack.

---

# Sulpiride: From Psychotic Disorder to Retinal Dystrophy with Extraocular Anomalies

## One-Sentence Summary

Sulpiride is a selective dopamine D2/D3 receptor antagonist internationally used for psychotic disorders and as an antiemetic, though it currently holds no CBG-MEB marketing authorization in the Netherlands.
The TxGNN model predicts it may be effective for **Retinal Dystrophy with or without Extraocular Anomalies**,
with **0 clinical trials** and **16 publications** retrieved — none of which directly study this drug-disease combination.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in the Netherlands; no CBG-MEB approved indication on record |
| Predicted New Indication | Retinal Dystrophy with or without Extraocular Anomalies |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| NL Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the provided data sources. Based on known pharmacological information, Sulpiride is a benzamide-class selective antagonist at dopamine D2 and D3 receptors. It is internationally established as an atypical antipsychotic and antiemetic, though it has not been granted marketing authorization by the CBG-MEB in the Netherlands.

The theoretical mechanistic link rests on the presence of dopaminergic amacrine cells in the retina, which express D2 and D4 receptors. In some photoreceptor dystrophies, retinal dopamine signaling is known to be reduced. This provides a superficially plausible rationale for a dopaminergic intervention.

However, this link is assessed as **very weak and directionally inconsistent**. Sulpiride is a D2/D3 *antagonist*, meaning it would further suppress — not restore — retinal dopaminergic transmission. More critically, retinal dystrophies are primarily driven by photoreceptor-level genetic mutations (e.g., RPGR, CRB1), which Sulpiride has no known mechanism to correct. The TxGNN model's high confidence score likely reflects shared graph topology rather than a biologically actionable connection.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 16 publications retrieved address orbital anatomy, extraocular muscle disorders, and congenital ocular anomalies in general. **None directly investigate Sulpiride for retinal dystrophy.** They were retrieved based on the disease category (conditions with extraocular anomalies) rather than the specific drug-disease pair, and should be interpreted accordingly.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | *Pediatric Radiology* | Differential diagnosis and imaging features of pediatric ocular pathologies including congenital/developmental lesions, retinopathy of prematurity, and Coats disease |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | *Taiwan Journal of Ophthalmology* | Congenital anomalies of lens shape and their association with anterior segment dysgenesis and extraocular features |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Original article | *Int J Molecular Sciences* | Optic nerve head and retinal abnormalities in congenital fibrosis of extraocular muscles (CFEOM) arising from KIF21A/TUBB3 mutations |
| [33447730](https://pubmed.ncbi.nlm.nih.gov/33447730/) | 2020 | Review | *Therapeutic Advances in Ophthalmology* | Eye involvement in inherited metabolic disorders, covering retinal, corneal, lens, and extraocular muscle abnormalities |
| [30747268](https://pubmed.ncbi.nlm.nih.gov/30747268/) | 2019 | Review | *Neuroradiology* | Neuroradiological and clinical evaluation of ophthalmoplegia for differential diagnosis and treatment planning |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | *J Binocular Vision and Ocular Motility* | Congenital cranial dysinnervation disorders (CCDDs) and patterns of ophthalmoplegia; diagnostic confirmation challenges |
| [27930425](https://pubmed.ncbi.nlm.nih.gov/27930425/) | 2017 | Case series | *Ophthalmic Plastic & Reconstructive Surgery* | The gracillimus orbitis — an anomalous accessory extraocular muscle found in 5–14% of cadaver orbits |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Case series | *American Journal of Ophthalmology* | Pathogenesis and treatment rationale for maculopathy associated with cavitary optic disc anomalies |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case report | *J Neuro-Ophthalmology* | Isolated trochlear-oculomotor synkinesis in a 6-year-old; subset of congenital cranial dysinnervation disorders |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | *Klinische Monatsblätter für Augenheilkunde* | Congenital ptosis: levator muscle fatty dystrophy/fibrosis and association with refractive errors and binocular disturbances |

---

## Netherlands Market Information

Sulpiride currently holds **no marketing authorization** from the CBG-MEB (College ter Beoordeling van Geneesmiddelen) in the Netherlands. No RVG numbers, registered product names, or approved SmPC documents are on file. Any future use in the Netherlands would require either a full centralized EMA authorization or a national procedure through CBG-MEB.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score of 99.95%, this candidate is unsupported by any clinical trial evidence, and the retrieved literature does not study Sulpiride in the context of retinal dystrophy. Most critically, Sulpiride's mechanism as a D2/D3 *antagonist* is directionally opposite to what the retinal dopamine hypothesis would require, and the underlying genetic etiology of retinal dystrophies is not addressable through dopaminergic pharmacology. The complete absence of a CBG-MEB marketing authorization creates an additional regulatory barrier.

**To proceed, the following is needed:**

- **Mechanistic validation**: Preclinical studies in animal models of retinal dystrophy (e.g., rd10, RPGR-knockout mice) to determine whether D2 antagonism has any measurable neuroprotective effect on photoreceptors
- **MOA data gap resolution**: Full mechanism of action data retrieval from DrugBank (currently unavailable — Data Gap DG002)
- **Genetic target analysis**: Review of the specific gene mutations underlying the target disease to assess whether any pharmacological approach targeting dopamine receptors is biologically plausible
- **Safety data gap resolution**: Download and parse the original SmPC/product information from source regulatory agencies to fill Data Gap DG001
- **Regulatory pathway scoping**: If preclinical results are unexpectedly positive, initiate a CBG-MEB/EMA scoping discussion for a possible off-label use or compassionate use framework
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

