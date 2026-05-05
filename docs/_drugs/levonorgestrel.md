---
layout: default
title: Levonorgestrel
parent: 僅模型預測 (L5)
nav_order: 87
evidence_level: L5
indication_count: 6
---

# Levonorgestrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Using `txgnn-pipeline` for context — this is a Netherlands (NL) TxGNN report generation task. The skill confirms the NL deployment is one of the supported multi-country instances. Proceeding to generate the report from the Evidence Pack.

---

# Levonorgestrel: From Hormonal Contraception to Acne

## One-Sentence Summary

Levonorgestrel is a synthetic progestin widely used in hormonal contraception — including combined oral contraceptives (COCs), intrauterine systems (IUS), and emergency contraception.
The TxGNN model predicts it may be effective for **Acne**, with a prediction score of **99.88%**.
This is supported by **5 clinical trials** and **20 publications**, of which at least one randomized placebo-controlled trial directly tested a levonorgestrel-containing COC for acne treatment.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hormonal contraception (combined oral contraceptive, IUS, emergency contraception) |
| Predicted New Indication | Acne |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| NL Market Status | Not registered (no CBG-MEB authorizations found in dataset) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, levonorgestrel is a synthetic progestin derived from the 19-nortestosterone (androstane) series. Crucially, it carries **intrinsic androgenic activity** — it binds to both progesterone and androgen receptors, which distinguishes it from newer, less androgenic progestins such as drospirenone or chlormadinone acetate (PMID 7825629).

Acne vulgaris is driven largely by excess androgen stimulation of the pilosebaceous unit, which increases sebum production and promotes comedone formation. Combined oral contraceptives containing levonorgestrel + ethinyl estradiol (EE) can produce a **net anti-androgenic effect** via two mechanisms: EE suppresses LH/FSH, reducing ovarian androgen synthesis, and substantially elevates sex hormone-binding globulin (SHBG), thereby lowering free bioavailable testosterone. A randomized placebo-controlled trial (PMID 12196750) directly demonstrated that a 20 µg EE / 100 µg LNG formulation improved androgenicity biomarkers and showed measurable benefit in moderate acne.

However, the evidence carries an important caveat: the acne benefit of EE/LNG combinations is attributed **primarily to EE**, not to LNG itself. Comparative trials show that OCs with lower-androgenicity progestins (e.g., EE/chlormadinone acetate) outperform EE/LNG on acne endpoints (PMID 15025547). Levonorgestrel monotherapy — as in the IUS or progestin-only pill — lacks EE's SHBG-raising effect and could theoretically worsen acne in androgenically sensitive individuals. This mechanistic nuance is critical when interpreting the TxGNN prediction: it most plausibly applies to **LNG as part of a COC formulation**, not as a standalone agent.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01650168](https://clinicaltrials.gov/study/NCT01650168) | N/A | Completed | 101,498 | Large prospective cohort comparing NOMAC-E2 vs LNG-containing COCs across >100,000 real-world users; captures dermatological side effects including acne changes, providing a large indirect comparative safety base |
| [NCT00480532](https://clinicaltrials.gov/study/NCT00480532) | N/A | Completed | 131 | Study of continuous COC use with doxycycline; doxycycline was included specifically for its acne-treatment properties, directly placing LNG-containing COC in an acne clinical context |
| [NCT05570786](https://clinicaltrials.gov/study/NCT05570786) | Phase 2 | Completed | 100 | Phase 2 RCT of subdermal gestrinone (androgenic synthetic progestin) pellet for endometriosis pelvic pain; contextually relevant to androgenic progestin effects on the pilosebaceous unit |
| [NCT05492487](https://clinicaltrials.gov/study/NCT05492487) | Phase 2 | Unknown | 60 | Pilot study of LNG IUS (Mirena) for atypical endometrial hyperplasia in Singapore; provides systemic LNG exposure data relevant to whole-body hormonal side-effect assessment |
| [NCT00161226](https://clinicaltrials.gov/study/NCT00161226) | N/A | Terminated | 44 | LNG IUS for endometrial cancer prevention; protocol explicitly notes acne as a known systemic side effect of oral progestins, reinforcing LNG's androgenic profile |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [12196750](https://pubmed.ncbi.nlm.nih.gov/12196750/) | 2002 | Clinical Trial (RCT) | J Am Acad Dermatol | Randomized, placebo-controlled trial: 20 µg EE + 100 µg LNG demonstrated improvement in biochemical androgenicity markers and measurable benefit in moderate acne — **most directly relevant study** |
| [6084924](https://pubmed.ncbi.nlm.nih.gov/6084924/) | 1984 | Clinical Study | Acta Derm Venereol | Head-to-head OC comparison (150 µg LNG vs. desogestrel) in 54 female acne patients; measured total/unbound testosterone and SHBG before and after 6 months' treatment |
| [15025547](https://pubmed.ncbi.nlm.nih.gov/15025547/) | 2004 | Review | Drugs | EE/chlormadinone acetate significantly more effective than EE/levonorgestrel for papulopustular acne; establishes that progestin androgenicity determines acne outcomes |
| [21895044](https://pubmed.ncbi.nlm.nih.gov/21895044/) | 2011 | Review/Clinical | Am J Clin Dermatol | Dermatological benefits of low-androgen OCs in hyperandrogenemia; acne, seborrhoea, hirsutism, and FPHL linked to PSU androgen excess; OC class context for LNG |
| [7825629](https://pubmed.ncbi.nlm.nih.gov/7825629/) | 1995 | Review | Am J Medicine | Foundational review of progestin androgenicity: LNG (19-nortestosterone series) has higher androgen receptor binding affinity than pregnane-derived progestins |
| [16796485](https://pubmed.ncbi.nlm.nih.gov/16796485/) | 2006 | Review | J Women's Health | Drospirenone vs LNG comparison: antiandrogenic progestins reduce acne, hirsutism, and water retention; positions LNG as comparator with higher androgenic risk |
| [32909630](https://pubmed.ncbi.nlm.nih.gov/32909630/) | 2020 | Cochrane Review | Cochrane Database Syst Rev | Comprehensive systematic review of LNG-IUS for endometrial hyperplasia; includes structured safety data reporting, androgenic side effects (acne, hirsutism) documented |
| [11727177](https://pubmed.ncbi.nlm.nih.gov/11727177/) | 2001 | Review | Semin Reprod Med | LNG-releasing IUS pharmacology, local vs. systemic LNG exposure, and endometrial effects; baseline pharmacokinetic reference for dermatological risk stratification by route |
| [14688179](https://pubmed.ncbi.nlm.nih.gov/14688179/) | 2004 | Clinical Study | Hum Reprod | LNG-IUS treatment of endometriosis; characterises systemic progestogenic exposure, relevant to androgenic side effects across the body including skin |
| [11091988](https://pubmed.ncbi.nlm.nih.gov/11091988/) | 2000 | Review | Obstet Gynecol Clin N Am | LNG implant contraception review; acne reported among known androgenic side effects across implant formulations at varying release rates |

---

## Netherlands Market Information

No CBG-MEB marketing authorizations were found for Levonorgestrel in this Evidence Pack dataset (total licenses: 0, market status: not registered).

> **Important caveat**: This is likely a **data pipeline gap** rather than a true regulatory absence. Levonorgestrel is an established, long-approved medicine available throughout the European Union under multiple formulations — including the Mirena IUS (Bayer), Jaydess/Kyleena IUS, Norlevo emergency contraception, and various combined OC products. CBG-MEB or EMA centralized registration should be verified directly via the [CBG-MEB public register](https://www.cbg-meb.nl/) before drawing any regulatory conclusions from this report.

---

## Safety Considerations

No safety data were returned by the Evidence Pack for this drug (key warnings, contraindications, and drug-drug interactions were all unavailable).

> Please refer to the **SmPC** (Summary of Product Characteristics / *Samenvatting van de Productkenmerken*) for the relevant levonorgestrel formulation for complete safety information, including cardiovascular risks, thromboembolic risk, contraindications in hormone-sensitive conditions, and androgenic side effects.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A published randomized placebo-controlled trial (PMID 12196750) directly tested an EE/LNG formulation for moderate acne and demonstrated benefit, and the TxGNN prediction score of 99.88% is among the strongest observed. However, the evidence attributes the acne benefit largely to the EE component; LNG's intrinsic androgenic activity means that monotherapy applications are mechanistically unfounded and could be counterproductive. Any repurposing pathway must clearly define the intended formulation and population.

**To proceed, the following is needed:**

- **Formulation clarity**: Define whether the repurposing claim is for an EE/LNG COC combination or LNG alone — these are mechanistically different claims
- **SmPC review**: Obtain and review the full SmPC for all NL-authorized LNG formulations to complete the safety assessment (currently blocked by data gap)
- **CBG-MEB register check**: Verify actual registration status and approved indications via the official Dutch register
- **Comparative positioning**: Assess how EE/LNG performs against already EMA/CBG-approved anti-acne OCs (e.g., EE/cyproterone acetate — *Diane-35*, EE/drospirenone — *Yasmin*) that have stronger anti-androgenic profiles
- **Dedicated monotherapy data**: If LNG monotherapy is the proposed route, a dedicated clinical trial is required — no current evidence supports this route for acne
- **Dermatology specialist input**: Engage a Dutch dermatologist to evaluate positioning within existing acne treatment guidelines (*Nederlandse Vereniging voor Dermatologie en Venereologie*, NVDV)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

