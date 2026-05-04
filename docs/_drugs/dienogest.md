---
layout: default
title: Dienogest
parent: 僅模型預測 (L5)
nav_order: 53
evidence_level: L5
indication_count: 10
---

# Dienogest
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

The txgnn-pipeline skill is focused on pipeline management and deployment — the report format and clinical interpretation guidance are already fully specified in the system prompt. I'll proceed directly with generating the evaluation report.

---

# Dienogest: From Endometriosis to Amenorrhea

## One-Sentence Summary

Dienogest is a fourth-generation selective progestin widely used for the treatment of endometriosis, acting by suppressing the hypothalamic-pituitary-ovarian (HPO) axis to reduce estrogen-driven ectopic endometrial growth.
The TxGNN model predicts it may be effective for **Amenorrhea**, with **4 clinical trials** and **6 publications** currently retrieved — however, mechanistic analysis reveals this is almost certainly a **contra-directional prediction**: Dienogest *induces* amenorrhea as a deliberate therapeutic effect in endometriosis management, rather than treating primary amenorrhea as a condition.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Endometriosis (known standard clinical use; no CBG-MEB marketing authorization on record for the Netherlands) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L3 |
| NL Market Status | Not marketed in the Netherlands |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the provided evidence pack. Based on established pharmacological knowledge, Dienogest is a fourth-generation synthetic progestin with highly selective progesterone receptor agonist activity and minimal androgenic, estrogenic, or glucocorticoid effects. It treats endometriosis by suppressing the HPO axis: inhibiting ovulation and follicular maturation, lowering endogenous estradiol concentrations, and inducing endometrial decidualization and atrophy — with amenorrhea being a direct and intended therapeutic outcome.

This is precisely where the mechanistic paradox lies. Amenorrhea is not a condition that Dienogest is designed to *treat* — it is a condition that Dienogest *causes*, intentionally, as a cornerstone of its efficacy against ectopic endometrial tissue. Prescribing Dienogest to treat primary or secondary amenorrhea in a patient who already lacks menstruation would be pharmacologically contradictory and could worsen underlying hormonal suppression.

The TxGNN model has likely captured the statistical co-occurrence of Dienogest, endometriosis, and amenorrhea in the knowledge graph without distinguishing the causal direction of the relationship. This is a recognized limitation of graph-based repurposing models: they can identify strongly associated node pairs without inferring whether the drug causes, treats, or simply correlates with the disease. **This prediction should be classified as a contra-directional artifact, not a genuine repurposing opportunity, and may be worth flagging as a pipeline quality signal.**

## Clinical Trial Evidence

> **Important context**: All retrieved clinical trials pertain to Dienogest's established endometriosis indication, not to treating amenorrhea. Amenorrhea in these trials appears as an outcome measure or adverse event — not as the therapeutic target. No trials treating amenorrhea with Dienogest were identified.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07164183](https://clinicaltrials.gov/study/NCT07164183) | Phase 3 | Recruiting | 290 | Non-inferiority RCT comparing Indinol Forto® 200 mg vs Visanne® (Dienogest 2 mg) for endometriosis; amenorrhea rate likely a secondary outcome |
| [NCT02425462](https://clinicaltrials.gov/study/NCT02425462) | N/A | Completed | 895 | Large prospective observational cohort assessing Visanne® effectiveness and long-term safety for quality of life in Asian women with endometriosis across routine clinical settings |
| [NCT04495855](https://clinicaltrials.gov/study/NCT04495855) | N/A | Completed | 968 | Real-world observational study of Dienogest in endometriosis; evaluates symptom control, recurrence after treatment cessation, and tolerability profile |
| [NCT07204093](https://clinicaltrials.gov/study/NCT07204093) | N/A | Active, not recruiting | 138 | Comparison of Dienogest vs drospirenone combined with transdermal estradiol in endometriosis; evaluates patient satisfaction and tolerability |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [39090694](https://pubmed.ncbi.nlm.nih.gov/39090694/) | 2024 | Systematic Review | BMC Pharmacology & Toxicology | Bayesian analysis of Dienogest adverse effects across multiple studies; identifies irregular bleeding and amenorrhea as frequent outcomes — confirming amenorrhea as an effect *of* the drug, not a treated condition |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Narrative Review | Reviews in Endocrine & Metabolic Disorders | Overview of hormonal endometriosis treatments; describes estrogen-dependency and progesterone-resistance as key pathogenic events; covers Dienogest's HPO axis suppression mechanism |
| [41329046](https://pubmed.ncbi.nlm.nih.gov/41329046/) | 2026 | Pharmacological Study | European Journal of Contraception & Reproductive Health Care | Quantitative pharmacological analysis of Dienogest 2 mg inhibition ratio; amenorrhea induction explicitly described as a mechanism of therapeutic action in endometriosis |
| [29161960](https://pubmed.ncbi.nlm.nih.gov/29161960/) | 2018 | Prospective Cohort | Reproductive Sciences | Retrospective cohort of 514 women with ovarian endometrioma across 7 hospitals; evaluates long-term efficacy and safety of Dienogest beyond 12 months including recurrence rates |
| [34918698](https://pubmed.ncbi.nlm.nih.gov/34918698/) | 2021 | Case Report | Medicine | Ovarian granulosa cell tumor in a PCOS patient; minimal direct relevance to Dienogest or amenorrhea as a treatment target |
| [40543564](https://pubmed.ncbi.nlm.nih.gov/40543564/) | 2025 | Review/Imaging | Journal of Pediatric and Adolescent Gynecology | Advanced 3D visualization techniques for obstructive Müllerian anomalies; minimal direct relevance to Dienogest repurposing |

## Netherlands Market Information

Dienogest currently holds **no marketing authorization** from the CBG-MEB (College ter Beoordeling van Geneesmiddelen) in the Netherlands. No RVG numbers are on record.

> Dienogest is marketed as Visanne® 2 mg in multiple EU member states (approved via national procedures and EMA scientific opinion), as well as in Japan, South Korea, and Australia. Any use in the Netherlands would require either a new CBG-MEB marketing authorization application, an EMA centralized procedure submission, or a compassionate use (named patient) pathway under Dutch medicines law.

## Safety Considerations

Please refer to the SmPC (Samenvatting van de Productkenmerken) for complete safety information. No warnings, contraindications, or drug interaction data were available in the current evidence pack.

> For orientation: based on EMA public assessment reports for Visanne® in other EU member states, the known safety profile of Dienogest includes irregular uterine bleeding, headache, depressed mood, decreased libido, acne, weight gain, and potential impact on bone mineral density with prolonged use. Use during pregnancy and in patients with undiagnosed abnormal vaginal bleeding is contraindicated per the originator SmPC.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for amenorrhea is assessed as a **contra-directional model artifact** — Dienogest pharmacologically induces amenorrhea as part of its endometriosis mechanism, and no clinical evidence exists for its use as a treatment for primary or secondary amenorrhea. Proceeding with this indication as a repurposing candidate would be pharmacologically unjustified based on current evidence.

**To proceed, the following is needed:**

- **Mandatory**: Clinical pharmacologist review to formally confirm the contra-directional classification and close this candidate in the pipeline
- **Pipeline quality action**: Flag this prediction pair (Dienogest ↔ Amenorrhea) as a known model artifact for the NlTxGNN contra-directional prediction audit
- **For completeness**: Extract the full MOA profile from DrugBank (DB09123) and EMA SmPC to document for future similar progestin candidates
- **If any amenorrhea subtype warrants further review** (e.g., progestin challenge testing in evaluation of amenorrhea etiology), a separate, narrowly scoped clinical question should be formulated with a gynecologist before re-evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

