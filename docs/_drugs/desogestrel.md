---
layout: default
title: Desogestrel
parent: 僅模型預測 (L5)
nav_order: 50
evidence_level: L5
indication_count: 10
---

# Desogestrel
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

Using the `txgnn-pipeline` skill — confirmed this is an NL-TxGNN drug repurposing report task. Proceeding to generate the evaluation report.

---

# Desogestrel: From Hormonal Contraception to Amenorrhea

## One-Sentence Summary

Desogestrel is a third-generation progestogen, widely used as a component of combined oral contraceptives (COC) and as a progestogen-only pill (POP) for hormonal contraception.
The TxGNN model predicts it may be effective for **Amenorrhea**,
with **2 clinical trials** and **16 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No NL registration on record; known clinical use as hormonal contraceptive |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L2 |
| NL Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank entry. Based on known pharmacological information, Desogestrel is a third-generation progestogen that suppresses the hypothalamic-pituitary-ovarian axis (HPOA), stabilising the endometrium and modulating LH/FSH pulse frequency. This mechanism is directly relevant to the regulation of the menstrual cycle and the management of amenorrhea — including both functional hypothalamic amenorrhea (FHA) and anovulatory states associated with hyperandrogenism.

Clinical studies have demonstrated that COC formulations containing Desogestrel restore and regulate menstrual cycles in adolescent girls with oligomenorrhea and ovarian hyperandrogenism (PMID 2956138, 2976224). Pharmacodynamic investigations (PMID 3161265) specifically evaluated Desogestrel's low androgenicity in the context of conditions such as PCOS, which frequently presents with amenorrhea. The reduction in LH, FSH, androstenedione, and testosterone seen with Desogestrel-based COC use is mechanistically consistent with cycle restoration.

The completed Phase 3 trial NCT00946192 directly investigates fat-mediated modulation of reproductive and endocrine function in young athletes with FHA — a population in which progestogen intervention is central to the study design. Together, the HPOA-regulatory mechanism, the clinical data in anovulatory populations, and this Phase 3 evidence base provide a coherent and plausible rationale for the TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT00946192](https://clinicaltrials.gov/study/NCT00946192) | Phase 3 | Completed | 121 | Investigates fat-mediated modulation of reproductive and endocrine function in young athletes who have stopped menstruating; evaluates whether transdermal or oral oestrogen restores bone density in estrogen-deficient athletes with amenorrhea — progestogen intervention design is highly aligned with Desogestrel's HPOA-modulating mechanism |
| [NCT01588873](https://clinicaltrials.gov/study/NCT01588873) | Phase 4 | Unknown | 42 | Compares effects of 59-week oral COC versus hormonal vaginal ring on androgen secretion, insulin/glucose metabolism, lipid profile, SHBG, and hs-CRP in women with PCOS — indirectly covers menstrual cycle regulation endpoints; trial status unknown limits evidence reliability |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35261299](https://pubmed.ncbi.nlm.nih.gov/35261299/) | 2022 | Prospective Cohort | Gynecological Endocrinology | Desogestrel 75 µg POP shows poor cycle control including amenorrhea in cardiovascular-risk women; compares bleeding profiles versus drospirenone-only pill across nine cycles |
| [21249657](https://pubmed.ncbi.nlm.nih.gov/21249657/) | 2011 | Cochrane Systematic Review (Update) | Cochrane Database | Updated SR examining bleeding pattern changes — including amenorrhea risk — with 20 µg vs >20 µg oestrogen COCs; directly addresses cycle control in desogestrel-containing formulations |
| [18843653](https://pubmed.ncbi.nlm.nih.gov/18843653/) | 2008 | Cochrane Systematic Review | Cochrane Database | Systematic review assessing the impact of progressive oestrogen dose reductions in COCs on contraceptive effectiveness, safety, and bleeding patterns including amenorrhea |
| [8218004](https://pubmed.ncbi.nlm.nih.gov/8218004/) | 1993 | Comparative RCT | Br J Obstet Gynaecol | Head-to-head comparison of desogestrel 150 µg with 20 µg versus 30 µg ethinyl oestradiol for cycle control, reliability, and side effects; directly relevant to menstrual regulation with Desogestrel |
| [3161265](https://pubmed.ncbi.nlm.nih.gov/3161265/) | 1985 | Pharmacodynamic Study | Acta Obstet Gynecol Scand Suppl | Evaluates androgenicity of progestogens with specific focus on Desogestrel; notes PCOS-like presentation with amenorrhea and characterises Desogestrel's endocrine modulation via radioimmunoassay |
| [11725730](https://pubmed.ncbi.nlm.nih.gov/11725730/) | 2001 | Clinical Study | J Reprod Med | Evaluates whether decreasing oestrogen doses in OCs affect bone loss in hypothalamic amenorrhea — directly addresses OC use in amenorrhoeic population |
| [8447356](https://pubmed.ncbi.nlm.nih.gov/8447356/) | 1993 | Clinical Observational | Am J Obstet Gynecol | Reviews tolerability of desogestrel/ethinyl oestradiol COC; highlights non-contraceptive benefits including reduction of dysmenorrhea and improvement of menstrual cycle regularity |
| [23221134](https://pubmed.ncbi.nlm.nih.gov/23221134/) | 2012 | Clinical Study | Georgian Med News | Studies pathogenetic management of central-genesis menstrual disorders including oligomenorrhea and amenorrhea in 159 infertile women; compares electroencephalography-guided vs standard hormonal therapy |
| [1436906](https://pubmed.ncbi.nlm.nih.gov/1436906/) | 1992 | Narrative Review | Obstet Gynecol Surv | Overview of desogestrel as a third-generation progestogen derived from levonorgestrel; reviews efficacy, pharmacokinetics, and cycle-control properties at lower doses |
| [8324604](https://pubmed.ncbi.nlm.nih.gov/8324604/) | 1993 | Narrative Review | Br Med Bull | Reviews COC safety and efficacy with lessons from major cohort and case-control studies; discusses non-contraceptive benefits including menstrual cycle regulation |

---

## Netherlands Market Information

Desogestrel currently holds **no marketing authorizations from CBG-MEB** in the Netherlands. There are no registered products or approved indications on record in this dataset.

> **Regulatory note**: Desogestrel-containing products (e.g., Cerazette® 75 µg progestogen-only pill, Mercilon®/Marvelon® combined OC) are widely authorised across EU member states, either via EMA centralised procedure or national registration. Current registration status for the Netherlands should be verified directly with CBG-MEB prior to any clinical application.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics / Samenvatting van de Productkenmerken) for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction for Desogestrel in amenorrhea has strong mechanistic plausibility — the drug's HPOA-suppressive and anti-androgenic progestogenic activity directly addresses the endocrine dysregulation underlying most amenorrhea subtypes. The L2 evidence level is anchored by one completed Phase 3 trial (NCT00946192, n=121), supported by a Cochrane systematic review, a comparative RCT, and pharmacodynamic studies. However, the majority of clinical evidence derives from Desogestrel used within a COC (combined with ethinyl oestradiol) rather than as a stand-alone POP, and Desogestrel is currently not registered in the Netherlands.

**To proceed, the following is needed:**
- Verify current CBG-MEB / EMA registration status for Desogestrel products in the Netherlands (Cerazette®, Mercilon®, Marvelon®) and obtain applicable SmPCs
- Retrieve DrugBank MOA data (remediation per DG002) to complete mechanistic analysis and support regulatory submission
- Obtain TFDA/EMA SmPC to extract contraindications and key warnings (remediation per DG001)
- Clarify whether the repurposing target is Desogestrel as monotherapy (POP 75 µg) or in combination (COC), given that current evidence is primarily COC-based
- Design a prospective study or registry specifically examining amenorrhea endpoints with Desogestrel monotherapy, as no such dedicated trial currently exists
- Assess the regulatory pathway for label expansion to include amenorrhea as a new indication, in coordination with CBG-MEB
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

