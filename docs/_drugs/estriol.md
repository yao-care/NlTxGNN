---
layout: default
title: Estriol
parent: 僅模型預測 (L5)
nav_order: 61
evidence_level: L5
indication_count: 1
---

# Estriol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

Using **txgnn-pipeline** to confirm context. Now generating the Netherlands CBG-MEB evaluation report from the Evidence Pack.

---

# Estriol: From Menopausal Urogenital Symptoms to Amenorrhea

## One-Sentence Summary

Estriol is a naturally occurring weak estrogen (ERα/ERβ agonist) with established clinical use for menopausal urogenital symptoms such as vaginal atrophy and hypoestrogenism.
The TxGNN model predicts it may be effective for **Amenorrhea** — specifically functional hypothalamic amenorrhea (FHA) — with **3 clinical trials** and **13 publications** currently identified, including one direct prospective clinical study in FHA patients.
Overall evidence is rated **L3**, as the clinical trials involve a related but distinct compound (estetrol) and do not directly target amenorrhea.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No CBG-MEB authorisation on record; internationally used for menopausal urogenital symptoms and vaginal atrophy |
| Predicted New Indication | Amenorrhea (Functional Hypothalamic Amenorrhea) |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L3 — Observational studies, reviews, and one prospective clinical study |
| NL Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank is currently unavailable. Based on known pharmacology, Estriol (DB04573) is a naturally occurring endogenous estrogen with relatively weak ERα/ERβ agonist activity compared to estradiol. This weaker receptor-binding affinity is clinically significant: it provides a broader therapeutic safety window and makes low-dose neuroendocrine modulation a particularly attractive approach for conditions driven by hormonal deficit rather than hormonal excess.

Functional hypothalamic amenorrhea (FHA) is characterised by impaired pulsatile GnRH secretion from the hypothalamus — typically triggered by psychosocial stress, excessive exercise, or malnutrition — leading to deficient LH/FSH release and downstream ovarian suppression with amenorrhea. In this pathophysiology, low-dose estriol may restore the hypothalamic–pituitary positive feedback loop, correcting LH secretion rhythm and reversing anovulatory amenorrhea. A 2012 prospective clinical study (PMID 22137494, *Fertility and Sterility*) specifically evaluated estriol administration on hypothalamus–pituitary function and gonadotropin secretion in FHA patients, directly supporting this mechanism.

The predicted repurposing direction is mechanistically coherent because both the original use and the new indication share the same underlying driver: systemic hypoestrogenism. Whether caused by menopause (ovarian senescence) or FHA (central GnRH suppression), the deficit in estrogenic signalling is the target being corrected. A 2023 review (PMID 37371858, *Biomedicines*) further contextualises low-dose estrogens as neuroendocrine modulators in FHA, reinforcing the biological plausibility of the TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04209543](https://clinicaltrials.gov/study/NCT04209543) | Phase 3 | Completed | 1,570 | Largest of the three trials; evaluates Estetrol (E4) 15/20 mg vs placebo for vasomotor symptoms (Efficacy Part) and endometrial safety (Safety Part) in postmenopausal women; indirect relevance via shared hypoestrogenism model |
| [NCT04090957](https://clinicaltrials.gov/study/NCT04090957) | Phase 3 | Completed | 1,015 | Estetrol (E4) 15 mg or 20 mg vs placebo for severity and frequency of vasomotor symptoms in postmenopausal women; indirect evidence for estrogen-deficiency reversal, not directly amenorrhea |
| [NCT04487392](https://clinicaltrials.gov/study/NCT04487392) | Phase 2 | Withdrawn | 0 | Photobiomodulation for vulvovaginal atrophy in postmenopausal women; trial withdrawn before any enrolment — no usable clinical data |

> **Important note:** All three registered trials involve **estetrol** (a distinct synthetic estrogen) or a non-pharmacological intervention, and target postmenopausal vasomotor symptoms rather than amenorrhea. No ClinicalTrials.gov registration directly evaluating **estriol** for amenorrhea was identified. The two completed Phase 3 studies (NCT04090957, NCT04209543) are graded B relevance (indirect) by the evidence pipeline.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [22137494](https://pubmed.ncbi.nlm.nih.gov/22137494/) | 2012 | Prospective Clinical Study | *Fertility and Sterility* | **Direct evidence:** Estriol administration modulates LH secretion in women with FHA; evaluates hypothalamus–pituitary function and gonadotropin dynamics — strongest mechanistic anchor in this evidence pack |
| [37371858](https://pubmed.ncbi.nlm.nih.gov/37371858/) | 2023 | Review | *Biomedicines* | Low-dose estrogens as neuroendocrine modulators in FHA; details positive feedback mechanism triggering by estrogen in GnRH-deficient states; supports Estriol's role at the hypothalamic level |
| [16526238](https://pubmed.ncbi.nlm.nih.gov/16526238/) | 2005 | Cohort/Observational | *Medicinski pregled* | Estro-progestagen effects on lipid and hormonal profiles in women with premature primary ovarian failure (hypergonadotropic amenorrhea); demonstrates measurable hormonal benefits in amenorrheic patients |
| [14194444](https://pubmed.ncbi.nlm.nih.gov/14194444/) | 1964 | Clinical Trial | *J Obstet Gynaecol Br Commonw* | Pituitary and urinary FSH with hCG in idiopathic secondary amenorrhoea; early controlled data on gonadotrophin-driven menstrual restoration |
| [4102186](https://pubmed.ncbi.nlm.nih.gov/4102186/) | 1971 | Case Report | *Lancet* | Endocrinological findings in two patients with premature ovarian failure; early documentation of amenorrhea-associated hormonal abnormalities |
| [4254759](https://pubmed.ncbi.nlm.nih.gov/4254759/) | 1971 | Clinical Report | *British Journal of Psychiatry* | Anorexia nervosa and associated amenorrhea; contextualises hypothalamic suppression as the driver of FHA in metabolically stressed patients |
| [2949864](https://pubmed.ncbi.nlm.nih.gov/2949864/) | 1986 | Observational | *Zhong Xi Yi Jie He Za Zhi* | Relationship between gonadal function changes and amenorrhea/oligomenorrhea; background observational data |
| [13931724](https://pubmed.ncbi.nlm.nih.gov/13931724/) | 1963 | Mechanistic | *J Clin Endocrinol Metab* | Mechanism of action of anti-ovulatory compounds; historical mechanistic study on estrogen–gonadotropin axis regulation |
| [7026111](https://pubmed.ncbi.nlm.nih.gov/7026111/) | 1981 | Review | *Clin Obstet Gynecol* | Neoplasia and hormonal contraception; peripheral relevance as hormonal safety context for estrogen-class drugs |
| [979592](https://pubmed.ncbi.nlm.nih.gov/979592/) | 1976 | Methodological | *Die Medizinische Welt* | Radioimmunoassay methodology for LH, FSH, progesterone, and estriol; methodological context for hormonal measurement in amenorrhea workup |

---

## Netherlands Market Information

Estriol (DB04573) currently has **no marketing authorisation** registered with the CBG-MEB (College ter Beoordeling van Geneesmiddelen) in the Netherlands. There are no RVG numbers on record.

Should a repurposing pathway be pursued, a new marketing authorisation or a formal off-label use protocol would need to be established — either through the CBG-MEB national procedure or via an EMA centralised procedure, depending on the target indication and patient population.

---

## Safety Considerations

No SmPC (Samenvatting van de Productkenmerken) or PIL (Bijsluiter) data are available for a Dutch-authorised estriol product, as no CBG-MEB marketing authorisation exists. No drug–drug interaction data were identified across queried sources.

Please refer to the SmPC of comparable estriol products authorised in other EU member states (available via the EMA product database) and consult current prescribing information before any clinical application.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.18%) and mechanistically plausible evidence — including one direct prospective clinical study of estriol in FHA (PMID 22137494) — Estriol is currently not marketed in the Netherlands (0 CBG-MEB authorisations), and critical safety data including SmPC warnings and contraindications remain entirely unavailable. The registered clinical trials involve estetrol (a distinct compound) targeting postmenopausal vasomotor symptoms rather than amenorrhea, placing overall evidence at L3 and making a Go recommendation premature at this stage.

**To proceed, the following is needed:**

- **Safety data retrieval:** Obtain and review the SmPC/PIL for estriol products authorised in other EU member states via EMA or national databases, to resolve the blocking safety data gap
- **MOA confirmation:** Query DrugBank API for full mechanism of action, receptor binding profile, and pharmacokinetic data
- **Direct clinical evidence:** Commission or identify a Phase 2/3 RCT directly evaluating estriol (not estetrol) in functional hypothalamic amenorrhea; the 2012 prospective study (PMID 22137494) provides a strong basis for protocol design
- **Regulatory pathway:** Consult CBG-MEB on requirements for either a new marketing authorisation or a recognised off-label use framework for this indication
- **Monitoring plan:** Define prospective monitoring parameters for any clinical study, including LH/FSH levels, endometrial safety, bone mineral density, and cardiovascular risk markers
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

