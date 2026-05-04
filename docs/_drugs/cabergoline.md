---
layout: default
title: Cabergoline
parent: 僅模型預測 (L5)
nav_order: 35
evidence_level: L5
indication_count: 5
---

# Cabergoline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Cabergoline: From Hyperprolactinemia to Pituitary Cancer

## One-Sentence Summary

Cabergoline is a dopamine D2/D3 receptor agonist, established internationally as the first-line medical treatment for hyperprolactinemia and prolactinoma. The TxGNN model predicts it may be effective across the broader spectrum of **Pituitary Cancer** — including non-functioning and secreting adenomas — with **19 clinical trials** and **20 publications** currently supporting this direction. Notably, the TxGNN top-ranked prediction is the specific subtype **pituitary adenocarcinoma** (score 99.06%), though evidence for that malignant form remains limited to case reports (L4); the clinically actionable evidence is concentrated in the broader pituitary cancer category (score 99.04%, L1).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hyperprolactinemia / Prolactinoma (established international use; no NL authorization on record) |
| Predicted New Indication | Pituitary Cancer (incl. non-functioning adenoma, corticotroph adenoma, prolactinoma) |
| TxGNN Prediction Score | 99.04% (pituitary cancer, rank 3); 99.06% (pituitary adenocarcinoma, rank 1) |
| Evidence Level | L1 (pituitary cancer); L4 (pituitary adenocarcinoma) |
| NL Market Status | Not marketed (geen RVG-registratie) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Cabergoline binds selectively to dopamine D2 and D3 receptors. Pituitary lactotroph cells (prolactin-secreting) express among the highest D2 receptor densities in the body, which explains why Cabergoline so effectively suppresses prolactin production and induces prolactinoma shrinkage. Crucially, D2 receptors are not restricted to lactotrophs: corticotroph cells (ACTH-secreting), somatotroph cells (GH-secreting in acromegaly), and a subset of non-functioning pituitary adenomas (NFPAs) also express D2R at varying levels. Upon receptor activation, the Gi protein-mediated inhibition of the cAMP/PKA pathway reduces hormone secretion, attenuates tumor cell proliferation, and promotes apoptosis — directly addressing the neoplastic process.

This mechanistic rationale has been validated in multiple clinical settings. Completed Phase 3 trials have established Cabergoline efficacy in corticotroph adenomas causing Cushing's disease (NCT00889525) and in residual NFPAs following transsphenoidal surgery (NCT03271918). A 2022 systematic review and meta-analysis (PMID 35902444) confirmed Cabergoline's tumor-stabilising effects in NFPAs. A 2020 review (PMID 31597135) specifically examined novel anti-tumor mechanisms beyond prolactinoma, including autophagy induction and cell-cycle arrest. Most recently, translational research (PMID 38989697, *Neuro-Oncology* 2024) demonstrated that co-targeting the HTR2B/Gαq/STAT3 pathway sensitises NFPAs to Cabergoline, pointing toward precision-medicine strategies.

The extension to the TxGNN top prediction — **pituitary adenocarcinoma** — requires more caution. Pituitary adenocarcinoma is an extremely rare malignant variant defined by cerebrospinal or systemic metastases, with an incidence of roughly 0.1–0.2% of all pituitary tumors. While D2R expression has been documented in some cases and isolated clinical reports describe ACTH-secreting carcinoma management with Cabergoline (PMID 20497940), no controlled trial data exist for this specific entity. The TxGNN high score likely reflects graph-topology proximity to the well-evidenced pituitary adenoma node rather than direct clinical evidence for the carcinoma subtype.

---

## Clinical Trial Evidence

*Based on the 19 trials identified for pituitary cancer; top 10 most relevant listed below.*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT00889525](https://clinicaltrials.gov/study/NCT00889525) | Phase 3 | Completed | N/A | Efficacy of Cabergoline for Cushing's disease (corticotroph adenoma); directly evaluates D2 agonism in a secreting pituitary tumor — highest-grade direct evidence |
| [NCT03271918](https://clinicaltrials.gov/study/NCT03271918) | Phase 3 | Completed | 140 | RCT evaluating Cabergoline in residual non-functioning pituitary adenoma after transsphenoidal surgery; large sample, directly relevant to post-surgical management |
| [NCT07034859](https://clinicaltrials.gov/study/NCT07034859) | Phase 4 | Enrolling by Invitation | 30 | 1:1 randomised trial of Cabergoline as primary (non-surgical) therapy for NFPA; 48-week follow-up through 2028 — prospective evidence accumulating |
| [NCT00376064](https://clinicaltrials.gov/study/NCT00376064) | Phase 4 | Completed | 20 | Proof-of-concept study: octreotide + Cabergoline combination therapy in acromegaly partially responsive to somatostatin analog monotherapy |
| [NCT03714763](https://clinicaltrials.gov/study/NCT03714763) | N/A | Unknown | 50 | PET-MR imaging of in vivo D2R expression in NFPA to predict Cabergoline treatment response; supports a precision-selection strategy |
| [NCT01915303](https://clinicaltrials.gov/study/NCT01915303) | Phase 2 | Terminated | 68 | Pasireotide alone vs. combined with Cabergoline in Cushing's disease; terminated early — provides partial efficacy and safety data for combination approach |
| [NCT02288962](https://clinicaltrials.gov/study/NCT02288962) | Phase 3 | Active, Not Recruiting | 60 | RCT of dopamine agonist treatment for NFPAs; ongoing follow-up through December 2028 |
| [NCT04107480](https://clinicaltrials.gov/study/NCT04107480) | Phase 4 | Recruiting | 880 | PRolaCT: three multicenter RCTs comparing surgery vs. dopamine agonist strategies for prolactinoma across multiple outcome dimensions |
| [NCT03400865](https://clinicaltrials.gov/study/NCT03400865) | N/A | Unknown | 30 | Cabergoline combined with hydroxychloroquine/chloroquine for cabergoline-resistant prolactinomas; mechanistic basis established in PMID 28973192 |
| [NCT01620138](https://clinicaltrials.gov/study/NCT01620138) | Phase 2/3 | Completed | 21 | Somatostatin and dopamine receptor expression in NFPAs and resistant prolactinomas; correlates receptor quantification with in vitro/in vivo responsiveness |

---

## Literature Evidence

*Top 10 most relevant publications from the 20 identified for pituitary cancer.*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35902444](https://pubmed.ncbi.nlm.nih.gov/35902444/) | 2022 | Systematic Review / Meta-Analysis | *Pituitary* | Meta-analysis confirming Cabergoline's tumor-stabilising and volume-reducing effects in non-functioning pituitary adenomas |
| [37097352](https://pubmed.ncbi.nlm.nih.gov/37097352/) | 2023 | Review | *JAMA* | Comprehensive review of pituitary adenoma diagnosis and management; Cabergoline positioned as standard of care for prolactinoma and documented for broader pituitary neoplasms |
| [38989697](https://pubmed.ncbi.nlm.nih.gov/38989697/) | 2024 | Translational Research | *Neuro-Oncology* | HTR2B targeting suppresses NFPA growth and sensitises tumors to Cabergoline via Gαq/PLC/PKCγ/STAT3 pathway; supports combination or biomarker-directed approach |
| [31597135](https://pubmed.ncbi.nlm.nih.gov/31597135/) | 2020 | Review | *Neuroendocrinology* | Reviews novel anti-tumor mechanisms of Cabergoline (autophagy, cell-cycle arrest, apoptosis) and their potential broader applications beyond prolactinoma |
| [37171003](https://pubmed.ncbi.nlm.nih.gov/37171003/) | 2023 | Clinical Guidelines | *Endocr Metab Immune Disord Drug Targets* | Italian national guidelines for prolactinoma management; Cabergoline recommended as first-line dopamine agonist with detailed dosing and monitoring guidance |
| [36974474](https://pubmed.ncbi.nlm.nih.gov/36974474/) | 2023 | Review | *J Clin Endocrinol Metab* | Practical approach to prolactinoma; Cabergoline superior to bromocriptine for normalisation of prolactin and tumor shrinkage across micro- and macroprolactinomas |
| [36013562](https://pubmed.ncbi.nlm.nih.gov/36013562/) | 2022 | Review | *Medicina* | Historical and modern prolactinoma treatment review, including multimodality therapy for aggressive prolactinomas and evidence for surgery vs. dopamine agonist sequencing |
| [28973192](https://pubmed.ncbi.nlm.nih.gov/28973192/) | 2017 | Preclinical / Translational | *J Clin Endocrinol Metab* | Cabergoline + chloroquine combination induces autophagy-mediated pituitary tumor suppression; mechanistic rationale for NCT03400865 |
| [25732645](https://pubmed.ncbi.nlm.nih.gov/25732645/) | 2015 | Review | *Endocrinol Metab Clin North Am* | Review of Cabergoline use for pituitary tumors and cardiac valvular safety; most studies show no clinically significant valvulopathy at pituitary doses |
| [40170221](https://pubmed.ncbi.nlm.nih.gov/40170221/) | 2025 | Research Article | *Eur J Endocrinol* | Circulating miR-20a-5p identified as a biomarker to predict Cabergoline responsiveness in patients with hyperprolactinemia and pituitary adenomas |

---

## Netherlands Market Information

Cabergoline is currently **not registered** with CBG-MEB (College ter Beoordeling van Geneesmiddelen) and holds no RVG number in the Netherlands.

| RVG Number | Product Name | Dosage Form | Approved Indication |
|-----------|-------------|-------------|-------------------|
| — | No authorization on record | — | — |

Cabergoline is authorized in other EU member states under the brand name **Dostinex®** (0.5 mg tablets, Pfizer/Viatris), with EMA oversight. Dutch prescribers wishing to use Cabergoline must currently pursue one of the following routes via CBG-MEB:
- **Named-patient importation** (Article 5(1) Directive 2001/83/EC) for individual patients with a documented clinical need
- **Compassionate use program** if formal marketing authorization is being pursued
- **Off-label use** with documented informed consent if obtained via importation

The applicable SmPC for safety reference is the **Dostinex® EU SmPC** (available via the EMA product database).

---

## Safety Considerations

Formal Dutch-market safety data (SmPC warnings, contraindications) are not available as no CBG-MEB authorization exists. Please refer to the **Dostinex® EU SmPC** as the primary safety reference. Based on evidence identified in this pack, the following signals warrant attention when considering use in pituitary cancer:

- **Cardiac valvulopathy**: At the high cumulative doses used in Parkinson's disease, ergot-derived dopamine agonists carry a recognized risk of restrictive valvular regurgitation. At the lower doses used for pituitary conditions, most studies (including PMID 25732645 and the observational study NCT00460616) report no significant increase in clinically relevant valvulopathy. Baseline and periodic echocardiographic monitoring is nonetheless recommended for long-term therapy.
- **Impulse control disorders (ICDs)**: De novo ICDs (pathological gambling, hypersexuality, compulsive spending/eating) are an increasingly recognized adverse effect of dopamine agonists, with prevalence up to ~60% in some series (PMID 41619686). Systematic screening with validated tools (e.g., QUIP-RS) before and during treatment is advisable.
- **Angle-closure glaucoma**: A case report (PMID 21347189) documents bilateral acute angle-closure glaucoma following oral Cabergoline; the proposed mechanism involves pupillary dilation and ciliary body congestion. Patients with a history of narrow-angle glaucoma should be evaluated before initiation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs — directly evaluating Cabergoline in corticotroph adenomas (Cushing's disease) and in non-functioning pituitary adenomas — combined with a 2022 systematic meta-analysis, establish L1-grade evidence for Cabergoline's efficacy across the spectrum of pituitary neoplasms. The D2 receptor agonist mechanism is well-characterised and biologically plausible for this indication class. The absence of a Dutch marketing authorization (RVG) is the primary regulatory barrier, not the clinical evidence base.

**To proceed, the following is needed:**

- **Regulatory pathway**: Determine the most appropriate access route through CBG-MEB — named-patient import for individual cases, or feasibility assessment for a formal marketing authorization application (MAA) based on the EMA-approved SmPC
- **Subtype stratification**: Clearly define the target pituitary tumor subtype(s), as evidence strength differs substantially: prolactinoma (strongest, decades of data) > corticotroph adenoma/Cushing's disease (Phase 3 completed) > NFPA (Phase 3 completed, meta-analysis) > pituitary adenocarcinoma (case reports only, L4)
- **D2R biomarker selection**: Consider D2 receptor expression testing (PET-MR imaging or immunohistochemistry on surgical specimens) to pre-select patients most likely to respond, supported by NCT03714763 and PMID 40170221
- **Safety monitoring protocol**: Establish baseline echocardiography and impulse control disorder (ICD) screening before treatment initiation; document monitoring schedule for long-term follow-up
- **Pituitary adenocarcinoma pathway**: For the TxGNN top-predicted entity (pituitary adenocarcinoma, L4), a dedicated literature review and case-registry analysis are needed before any clinical evaluation — the current evidence does not support routine use in this ultra-rare malignant subtype
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

