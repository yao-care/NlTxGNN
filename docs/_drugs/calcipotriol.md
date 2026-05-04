---
layout: default
title: Calcipotriol
parent: 僅模型預測 (L5)
nav_order: 36
evidence_level: L5
indication_count: 10
---

# Calcipotriol
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

# Calcipotriol: From Psoriasis to Seborrheic Keratosis

## One-Sentence Summary

Calcipotriol is a synthetic vitamin D3 analogue established globally for the topical treatment of plaque psoriasis through its vitamin D receptor (VDR) agonist activity, though it currently holds no CBG-MEB marketing authorisation in the Netherlands.
The TxGNN model predicts it may be effective for **Seborrheic Keratosis**,
with **0 clinical trials** and **6 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Plaque psoriasis (established global use; no NL authorisation on record) |
| Predicted New Indication | Seborrheic Keratosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| NL Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Calcipotriol is a synthetic vitamin D3 analogue that acts as a potent agonist at the vitamin D receptor (VDR). In plaque psoriasis, VDR activation suppresses abnormal keratinocyte proliferation and modulates immune responses — reducing IL-2 and IFN-γ production and dampening T-cell-driven inflammation. This well-characterised action in hyperproliferative keratinocyte disorders provides the core biological rationale for exploring its application in seborrheic keratosis.

Seborrheic keratosis (SK) is the most common benign epidermal tumour, driven by somatic mutations in FGFR3 and PIK3CA that cause uncontrolled keratinocyte proliferation. VDR activation is mechanistically relevant to this process: it downregulates PCNA (a key proliferation marker), upregulates terminal differentiation markers (involucrin, loricrin), and shifts the Bcl-2/Bax ratio in favour of apoptosis. VDR agonism can also counter-regulate the MAPK signalling pathway, which is overactivated by the FGFR3/PIK3CA mutations that characterise SK — a mechanistic link that aligns closely with the lesion regression observed in published case series.

While psoriasis and seborrheic keratosis differ in aetiology (immune-mediated inflammation vs. mutation-driven benign proliferation), both converge on pathological keratinocyte hyperproliferation regulated by VDR-dependent pathways. The convergence on a shared effector mechanism, together with published observational evidence of complete lesion regression following topical calcipotriol treatment, makes this a scientifically plausible repurposing candidate warranting further prospective evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [36752725](https://pubmed.ncbi.nlm.nih.gov/36752725/) | 2023 | Prospective case series | Australasian Journal of Dermatology | 12 patients with facial SK treated with 0.005% calcipotriol ointment for 3–8 months; complete regression achieved in all cases with remission lasting 6–10 years |
| [16043912](https://pubmed.ncbi.nlm.nih.gov/16043912/) | 2005 | Clinical observation + mechanistic study | Journal of Dermatology | Topical vitamin D3 analogues (including calcipotriol) applied to 116 SK cases; 30.2% achieved complete or near-complete regression; apoptosis induction proposed as mechanism |
| [15090020](https://pubmed.ncbi.nlm.nih.gov/15090020/) | 2004 | Comparative non-randomised study | International Journal of Dermatology | Head-to-head comparison of cryosurgery vs. topical calcipotriene, tazarotene, and imiquimod for SK; evaluates relative efficacy of non-surgical topical options |
| [15577148](https://pubmed.ncbi.nlm.nih.gov/15577148/) | 2004 | Case series / clinical review | Clinical Calcium | Topical VDR analogues (tacalcitol, calcipotriol, maxacalcitol) applied once or twice daily to senile warts (SK); summarises clinical response across multiple formulations |
| [10721662](https://pubmed.ncbi.nlm.nih.gov/10721662/) | 2000 | Case report | Journal of Dermatology | Keratosis lichenoides chronica with prominent seborrheic keratosis-like features showed marked response to calcipotriol ointment; supports broader anti-keratinisation activity |
| [21534378](https://pubmed.ncbi.nlm.nih.gov/21534378/) | 2011 | Clinical vignette | JAAPA | Case teaching vignette featuring seborrheic keratosis on the shins; contextual reference for clinical presentation |

---

## Netherlands Market Information

Calcipotriol is **not currently registered** with the CBG-MEB (College ter Beoordeling van Geneesmiddelen) in the Netherlands. No RVG numbers are available, and no SmPC has been issued by the Dutch Medicines Evaluation Board for this drug.

> **Regulatory note**: Calcipotriol is authorised in other EU Member States and available via EMA-centralised or national procedures under brand names such as Daivonex® and Dovonex® for plaque psoriasis. Any Netherlands-based application would require either a national marketing authorisation application to CBG-MEB, a mutual recognition/decentralised procedure, or evaluation of off-label use pathways under Article 68 of the Geneesmiddelenwet.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information. As no CBG-MEB SmPC is currently available for this drug in the Netherlands, the reference SmPC for Daivonex®/Dovonex® from the EMA or the reference Member State should be consulted for warnings, contraindications, and drug interactions.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple observational studies and case series (6 publications, Evidence Level L3) demonstrate that topical calcipotriol can induce complete regression of seborrheic keratosis lesions with a biologically plausible VDR-mediated mechanism; however, no registered clinical trials exist, and the drug currently holds no CBG-MEB authorisation in the Netherlands.

**To proceed, the following is needed:**

- Retrieve the full SmPC for Daivonex®/Dovonex® from the EMA or a reference EU Member State to complete the safety, contraindication, and drug-drug interaction assessment
- Obtain formal mechanism of action documentation from DrugBank or primary pharmacology literature to strengthen mechanistic justification
- Assess CBG-MEB regulatory pathways: new marketing authorisation application, mutual recognition procedure, or Article 68 off-label use framework
- Design a prospective randomised controlled trial (RCT) to upgrade the evidence base from L3 to L2/L1, with complete regression as the primary endpoint and standardised calcipotriol 0.005% ointment as the investigational arm
- Evaluate local tolerability on facial skin (the most common SK treatment site) and mucosal areas, given the known irritation potential of topical calcipotriol on sensitive skin regions
- Confirm optimal treatment duration and long-term remission data beyond the 6–10 year follow-up observed in the 2023 case series
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

