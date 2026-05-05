---
layout: default
title: Tetrabenazine
parent: 僅模型預測 (L5)
nav_order: 119
evidence_level: L5
indication_count: 10
---

# Tetrabenazine
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

Using the `txgnn-pipeline` skill for context. Now generating the report based on the Evidence Pack.

---

# Tetrabenazine: From Chorea (Huntington's Disease) to Polycystic Kidney Disease 3 with Polycystic Liver Disease

## One-Sentence Summary

Tetrabenazine is a vesicular monoamine transporter 2 (VMAT2) inhibitor used internationally (e.g., FDA-approved Xenazine) for chorea associated with Huntington's disease and other hyperkinetic movement disorders; it is currently not registered in the Netherlands.
The TxGNN model predicts it may be effective for **polycystic kidney disease 3 with or without polycystic liver disease (PKD3/ADPKD-GANAB)**, with **0 clinical trials** and **20 background publications** identified — though none of these publications directly investigates Tetrabenazine as a treatment for this condition.
Overall, this represents a low-confidence, model-driven prediction without biological plausibility support.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in the Netherlands regulatory database (drug not registered in NL; known internationally for Huntington's disease chorea) |
| Predicted New Indication | Polycystic kidney disease 3 with or without polycystic liver disease |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| NL Market Status | Not Registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available from the Dutch regulatory source for this review. Based on internationally available pharmacological information, Tetrabenazine inhibits VMAT2, the transporter responsible for packaging monoamine neurotransmitters (dopamine, serotonin, norepinephrine) into presynaptic vesicles. By depleting these stores, the drug reduces excessive dopaminergic transmission, which underlies the involuntary hyperkinetic movements seen in Huntington's disease and related conditions. Its efficacy in this neurological context is well established internationally, though no Dutch market authorizations exist.

Polycystic kidney disease type 3 (PKD3) is caused by mutations in the *GANAB* gene, which encodes a glucosidase involved in glycoprotein processing. This is a ciliopathy: defective glycoprotein maturation impairs primary cilia function, leading to dysregulated mTOR signalling and progressive cyst formation in the kidneys and liver. This disease mechanism is entirely distinct from monoamine neurotransmitter biology.

There is currently no known biological intersection between VMAT2 inhibition or monoamine depletion and the mTOR/cystogenesis pathway central to PKD3 pathogenesis. The TxGNN model's high score (99.90%) most likely reflects network proximity effects in the knowledge graph — Tetrabenazine nodes sitting near rare nephropathy disease nodes — rather than any direct mechanistic rationale. Independent expert review of the mechanistic link confirms the absence of plausibility for this repurposing candidate at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Tetrabenazine in polycystic kidney disease 3 with or without polycystic liver disease.

---

## Literature Evidence

The 20 publications identified address the general diagnosis, genetics, pathophysiology, and management of polycystic kidney and liver disease. **None specifically investigates Tetrabenazine as a treatment for this condition.** These papers are presented as disease background only and do not constitute evidence for this repurposing direction.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38958301](https://pubmed.ncbi.nlm.nih.gov/38958301/) | 2024 | Clinical Guideline | Am J Gastroenterology | ACG guideline on focal liver lesions; covers diagnosis and management of polycystic liver disease including cystic lesion surveillance |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Clinical Guideline | J Hepatology | EASL Clinical Practice Guidelines on cystic liver diseases; addresses polycystic liver disease, Caroli disease, and biliary hamartomas |
| [30819518](https://pubmed.ncbi.nlm.nih.gov/30819518/) | 2019 | Review | Lancet | Comprehensive ADPKD review; covers genetics, systemic manifestations (cysts, hypertension, intracranial aneurysms), and emerging therapies including tolvaptan |
| [29038287](https://pubmed.ncbi.nlm.nih.gov/29038287/) | 2018 | Review | JASN | Genetic complexity of ADPKD/ADPLD; describes 8 causative genes including *GANAB* (relevant to PKD3) and their phenotypic overlap |
| [38097330](https://pubmed.ncbi.nlm.nih.gov/38097330/) | 2023 | Review | Advances in Kidney Disease and Health | Detailed genetic spectrum of PKD/PLD; *PKD1* accounts for ~80% of patients; minor loci including *GANAB* discussed |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clinics in Liver Disease | ADPKD with polycystic liver disease; tolvaptan slows renal deterioration; management of symptomatic PLD |
| [40081770](https://pubmed.ncbi.nlm.nih.gov/40081770/) | 2025 | Review | Biochemical Pharmacology | Extracellular matrix dynamics and MMP activity in ADPKD/ARPKD as novel therapeutic targets; fibrosis-cyst interaction |
| [37208103](https://pubmed.ncbi.nlm.nih.gov/37208103/) | 2023 | Review | J Hepatology | Combined liver-kidney transplantation in polycystic disease; outcomes and immunological considerations |
| [34724412](https://pubmed.ncbi.nlm.nih.gov/34724412/) | 2022 | Review | Annual Review of Pathology | Mechanism of polycystic liver disease; primary, secondary, and tertiary interconnected pathways driving cholangiocyte cystogenesis |
| [36047551](https://pubmed.ncbi.nlm.nih.gov/36047551/) | 2022 | Review | Revue Médicale Suisse | Adult polycystic liver disease overview; distinguishes ADPLD, ADPKD-associated PLD, and biliary hamartomas; hormonal influence on cyst growth |

---

## Netherlands Market Information

Tetrabenazine currently holds **no marketing authorizations** registered with the CBG-MEB (College ter Beoordeling van Geneesmiddelen) in the Netherlands. There are no RVG numbers to list.

If Tetrabenazine is clinically indicated for a Dutch patient, access may be possible through:
- **Named-patient import** (artikel 3 lid 8 Geneesmiddelenwet) via a hospital pharmacist, referencing the EMA or FDA-approved label
- **Hospital pharmacy compounding**, subject to applicable regulations

Prescribers should consult the EMA product information or the FDA Xenazine prescribing information (SmPC equivalent) for the full approved indication, dosing, and safety profile.

---

## Safety Considerations

Detailed safety data specific to the Netherlands market was not available in this evaluation (no Dutch SmPC exists). Based on internationally available product information, the following safety concerns are well documented for Tetrabenazine and are particularly relevant when considering any off-label use:

- **Depression and suicidality**: Tetrabenazine carries a black-box warning (FDA) for the risk of depression and suicidal ideation; contraindicated in patients with untreated depression
- **Sedation and cognitive impairment**: Central nervous system depression is a common dose-limiting effect
- **QTc prolongation**: Risk of cardiac arrhythmia; ECG monitoring recommended
- **Neuroleptic malignant syndrome**: Rare but serious; requires immediate discontinuation
- **Renal and hepatic impairment**: Pharmacokinetic data in patients with impaired kidney or liver function (directly relevant to the PKD3 patient population) is limited

Please refer to the EMA or FDA SmPC for complete safety information before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite the TxGNN prediction score of 99.90%, there is no credible biological mechanism connecting VMAT2 inhibition with the mTOR/cystogenesis pathway that drives PKD3, and no clinical or preclinical studies support this repurposing direction. The high model score reflects knowledge graph network proximity, not pharmacological plausibility. Additionally, Tetrabenazine is not registered in the Netherlands, and the PKD3 patient population (with progressive renal impairment) presents meaningful pharmacokinetic safety concerns.

**To proceed beyond Hold, the following would be needed:**

- **Mechanistic evidence**: Identification of a credible biological pathway linking VMAT2/monoamine neurotransmitter systems to PKD3 cyst formation or mTOR signalling (currently absent)
- **Preclinical data**: In vitro or animal model studies (e.g., *Ganab*-mutant kidney organoids or mouse models) assessing any effect of Tetrabenazine or VMAT2 inhibition on cystogenesis
- **Pharmacokinetic review**: Assessment of drug exposure in patients with reduced GFR (relevant to PKD3 disease progression); full DrugBank MOA data retrieval (Data Gap DG002)
- **Safety gap remediation**: Retrieval of full SmPC warnings and contraindications (Data Gap DG001) to complete a formal safety screening (S1 gate)
- **Regulatory pathway assessment**: Consultation with CBG-MEB on named-patient access or RVG application if preclinical evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

