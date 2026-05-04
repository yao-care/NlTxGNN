---
layout: default
title: Etonogestrel
parent: 僅模型預測 (L5)
nav_order: 62
evidence_level: L5
indication_count: 5
---

# Etonogestrel
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

Using **txgnn-pipeline** to guide report structure, then generating the NL-framework evaluation report per the v5 prompt specification.

---

# Etonogestrel: From Contraception to Amenorrhea

## One-Sentence Summary

Etonogestrel is a third-generation progestin delivered via a subdermal implant, widely used internationally as a long-acting reversible contraceptive (brand name Implanon/Nexplanon), though it holds no CBG-MEB marketing authorisation in the Netherlands.
The TxGNN model predicts it may be applicable to **Amenorrhea**, with **1 clinical trial** and **1 relevant publication** currently supporting this direction.
Importantly, amenorrhea in this context is a well-documented pharmacological consequence of etonogestrel use rather than a primary therapeutic target, which requires careful interpretation when assessing this prediction's repurposing value.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Contraception — long-acting reversible contraceptive implant (based on clinical trial context; no CBG-MEB authorisation on record) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L3 |
| NL Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on known information, Etonogestrel is the active metabolite of desogestrel and is the sole active component of the Implanon/Nexplanon subdermal implant system. It belongs to the third-generation progestin class and exerts its primary effects by suppressing the hypothalamic-pituitary-ovarian (HPO) axis — specifically by inhibiting the LH surge — resulting in consistent anovulation. Secondary effects include thickening of cervical mucus and atrophic changes to the endometrium.

The link between etonogestrel and amenorrhea is therefore pharmacologically direct: amenorrhea is one of the most frequently reported outcomes of implant use, occurring in approximately 20–30% of users within the first year and increasing over time. The TxGNN knowledge graph likely captures this strong mechanistic and epidemiological association, which explains the high prediction score.

However, this prediction describes a **known side effect / pharmacological consequence** rather than a conventional therapeutic repurposing scenario. If the clinical intent is to leverage etonogestrel's amenorrhoea-inducing properties as a treatment — for instance in endometriosis-associated bleeding, heavy menstrual bleeding, or functional uterine bleeding — there is indirect mechanistic support. However, no RCTs with amenorrhea as a primary therapeutic endpoint are currently available, and the repurposing value requires prospective framing before it can be assessed meaningfully.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04626596](https://clinicaltrials.gov/study/NCT04626596) | Phase 3 | Completed | 498 | Extended-use study (years 4–5) of the ENG contraceptive implant in women aged ≤35. Primary endpoint is contraceptive efficacy; amenorrhea is recorded as a secondary safety/tolerability measure. Confirms the implant remains highly effective beyond the approved 3-year duration and provides high-quality data on amenorrhea incidence during extended use — though not as a therapeutic target. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10549446](https://pubmed.ncbi.nlm.nih.gov/10549446/) | 1999 | RCT | Contraception | Randomised multicentre comparison of single-rod Implanon (etonogestrel) vs. six-capsule Norplant over up to 4 years (n=200, China). No pregnancies in either arm. Systematically documents bleeding patterns — including amenorrhea rates — over successive 90-day reference periods, providing the earliest RCT-level evidence of etonogestrel's amenorrhoea profile. |
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | RCT | Trials | Study protocol for BIO101 in COVID-19 pneumonia prevention of respiratory deterioration. **Not related to etonogestrel or amenorrhea** — this appears to be a spurious search result and should not be considered supporting evidence for this repurposing candidate. |

---

## Netherlands Market Information

Etonogestrel currently holds **no marketing authorisations** from the CBG-MEB (College ter Beoordeling van Geneesmiddelen). The drug is not registered on the Dutch market in any dosage form. Note that in neighbouring EU member states, the etonogestrel subdermal implant (Implanon NXT) holds EMA-coordinated centralised or mutual recognition authorisations; a national or centralised EMA submission pathway would need to be evaluated if clinical development in the Netherlands is pursued.

---

## Safety Considerations

Please refer to the SmPC (Samenvatting van de Productkenmerken) for complete safety information. No key warnings, contraindications, or drug interaction data were available in the current evidence pack — retrieval of the full SmPC is listed as a blocking data gap (DG001) that must be resolved before any safety assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction captures a pharmacologically valid and well-established association — etonogestrel reliably induces amenorrhea — but this represents a documented side effect rather than a validated therapeutic indication, and there are no RCTs targeting amenorrhea as a primary endpoint. Additionally, the absence of any CBG-MEB marketing authorisation and the missing SmPC data mean that basic regulatory and safety prerequisites for a Stage 1 evaluation cannot yet be met.

**To proceed, the following is needed:**

- **Define the clinical question precisely**: Is the goal to treat pathological amenorrhea, or to leverage etonogestrel's amenorrhoea-inducing properties for a specific condition (e.g., endometriosis, heavy menstrual bleeding, adenomyosis)?
- **Resolve DG001 (Blocking)**: Obtain the full SmPC for the etonogestrel implant (e.g., from EMA public assessment reports for Implanon NXT) to enable safety screening
- **Resolve DG002 (High)**: Retrieve formal MOA data from DrugBank (DB00294) to support mechanistic link analysis
- **Conduct a targeted literature search**: Focus on etonogestrel in amenorrhea-induction as a therapeutic strategy, including gynaecological indications where amenorrhea is a desired endpoint
- **Evaluate the EMA centralised authorisation pathway**: Given the drug is authorised in other EU member states, assess whether a label extension or off-label use framework is applicable within the Netherlands
- **Clean the evidence pipeline**: Remove irrelevant search hits (e.g., PMID 33430924) that inflate the apparent evidence base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

