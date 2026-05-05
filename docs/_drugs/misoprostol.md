---
layout: default
title: Misoprostol
parent: 僅模型預測 (L5)
nav_order: 95
evidence_level: L5
indication_count: 2
---

# Misoprostol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Misoprostol: From Medical Abortion / Postpartum Hemorrhage to Amenorrhea

## One-Sentence Summary

Misoprostol is a synthetic prostaglandin E1 (PGE1) analogue, established globally for medical abortion (in combination with mifepristone) and postpartum hemorrhage prevention, though it is not currently registered in the Netherlands.
The TxGNN model predicts it may be effective for **Amenorrhea**, with **0 clinical trials** and **7 publications** providing contextual support for this direction.
However, the retrieved literature predominantly uses "amenorrhea" as a patient enrolment criterion for early-pregnancy abortion studies — not as a therapeutic target — meaning the direct evidentiary link to treating amenorrhea as a pathological condition remains limited.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in the Netherlands; established global use for medical abortion and postpartum hemorrhage prevention |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L4 |
| NL Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Misoprostol is a synthetic PGE1 analogue that activates EP1 and EP3 prostaglandin receptors on uterine smooth muscle, triggering myometrial contractions and inducing endometrial shedding. This mechanism underlies its clinically established applications in medical abortion and postpartum hemorrhage management. The TxGNN knowledge graph likely inferred this predicted indication through the well-documented co-occurrence of misoprostol with uterine bleeding induction in the biomedical literature.

The connection between misoprostol and amenorrhea is mechanistically plausible. If amenorrhea results from failure of the endometrium to shed despite adequate proliferation — for example in anovulatory cycles or cases of endometrial accumulation without spontaneous bleeding — a uterotonic prostaglandin analogue could theoretically trigger withdrawal-like bleeding. This is mechanistically very similar to its established use in medical abortion, where it expels early pregnancy tissue through the same EP1/EP3-mediated pathway. In this sense, "menstrual induction" sits on a mechanistic continuum with "pregnancy termination."

That said, an important distinction limits the strength of this prediction: the repurposing rationale itself acknowledges that **amenorrhea is not the primary therapeutic endpoint in any of the identified studies**. The 7 retrieved publications largely enrol women with "amenorrhea ≤35 days" as a way to define ultra-early pregnancy timing, not to study misoprostol as a treatment for amenorrhea as a clinical diagnosis. Dedicated prospective evidence targeting amenorrhea specifically — with appropriate diagnostic sub-grouping (e.g., hypothalamic, anovulatory, endometrial) — is absent.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for Misoprostol specifically targeting amenorrhea as a primary indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | RCT | Reproductive Sciences | Low-dose mifepristone + self-administered misoprostol for ultra-early medical abortion in 744 women with amenorrhea ≤35 days; "amenorrhea" used as pregnancy-timing inclusion criterion, not as a condition being treated |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | RCT | Reproductive Sciences | Dose-ranging RCT (n=2,500) of mifepristone + misoprostol for ultra-early pregnancy termination; amenorrhea ≤35 days defines eligibility; primary endpoint is complete abortion rate |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | RCT | J Obstet Gynaecol Res | Safety and efficacy of low-dose mifepristone + self-administered misoprostol for early pregnancy termination; confirms uterotonic mechanism but amenorrhea is an enrolment parameter |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Cohort | Human Reproduction | Explores pre-menstrual administration of mifepristone + misoprostol to prevent unintended pregnancy; provides context for pre-ovulatory/post-ovulatory prostaglandin intervention on the uterus |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Review | J Obstet Gynaecol Can | Systematic review of endometrial ablation for abnormal uterine bleeding; contextually relevant to uterine pathology and menstrual dysregulation, not specific to misoprostol |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Clinical Series | BMJ | Early clinical evidence for misoprostol in medical management of missed abortion and anembryonic pregnancy; establishes foundational uterotonic use |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Case Report | Cureus | Acute fatty liver of pregnancy presenting with amenorrhea and HELLP syndrome; misoprostol is not the focus — tangential relevance only |

---

## Netherlands Market Information

Misoprostol is currently **not registered** in the Netherlands. No marketing authorizations (RVG numbers) are on record with the CBG-MEB (College ter Beoordeling van Geneesmiddelen). As a result, no Dutch SmPC (Samenvatting van de Productkenmerken) is available through standard channels.

Clinicians and researchers considering investigational use in the Netherlands should consult the CBG-MEB for applicable compassionate use or clinical trial frameworks. Reference SmPCs from EMA-registered products in comparable jurisdictions may be consulted for safety guidance in the interim.

---

## Safety Considerations

Safety data (key warnings and contraindications) for Misoprostol were not available in this Evidence Pack, and no NL-specific SmPC exists given the drug's unregistered status in the Netherlands.

Please refer to internationally available SmPCs and authoritative pharmacological references for safety information. Based on established clinical use of misoprostol in reproductive medicine, practitioners should be aware that uterotonic agents carry risks including excessive uterine contractions, uterine rupture (particularly in women with prior uterine surgery), and significant haemorrhage — considerations that would apply directly to any proposed use in amenorrhea management.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN prediction score is high (99.64%) and a mechanistic pathway via EP1/EP3 receptor-mediated endometrial shedding is biologically plausible, no clinical trial addresses amenorrhea as a primary indication for misoprostol, the retrieved literature treats amenorrhea as a pregnancy-timing entry criterion rather than a therapeutic target, and the drug carries no regulatory standing in the Netherlands — leaving both efficacy and safety undocumented for this specific use case.

**To proceed, the following is needed:**

- Prospective clinical studies or well-characterized case series evaluating misoprostol specifically for amenorrhea as a pathological condition, with diagnostic sub-grouping (anovulatory, hypothalamic, endometrial/structural)
- Formal MOA documentation from DrugBank or an equivalent pharmacological authority, to substantiate the mechanistic claim at regulatory level
- Comprehensive safety review including contraindications and key warnings (e.g., prior uterine surgery, hypersensitivity to prostaglandins, cardiovascular risk)
- Regulatory pathway consultation with CBG-MEB for any investigational or compassionate use in the Netherlands
- Comparative positioning against existing prostaglandin-based or hormonal therapies for amenorrhea, to clarify where misoprostol would offer a clinically meaningful advantage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

