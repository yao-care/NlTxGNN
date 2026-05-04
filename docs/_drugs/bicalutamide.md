---
layout: default
title: Bicalutamide
parent: 僅模型預測 (L5)
nav_order: 30
evidence_level: L5
indication_count: 10
---

# Bicalutamide
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

# Bicalutamide: From Prostate Cancer to Hypertrichosis

## One-Sentence Summary

Bicalutamide is a well-established non-steroidal antiandrogen that competitively blocks the androgen receptor (AR), approved in numerous countries for the treatment of prostate cancer — though not currently registered in the Netherlands.
The TxGNN model predicts it may be effective for **Hypertrichosis** — specifically, the management of minoxidil-induced excessive hair growth — with **1 publication** (an expert commentary letter) currently supporting this direction.
The evidence base is limited to expert opinion, placing this candidate at the early research investigation stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prostate cancer (globally approved; not registered in the Netherlands) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L4 |
| NL Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not formally captured in this Evidence Pack. Based on known pharmacological information and contextual signals within the evidence pack, Bicalutamide is a non-steroidal antiandrogen that competitively antagonizes the androgen receptor (AR). Androgens signaling through AR are a primary driver of hair follicle biology: in androgen-sensitive follicles, AR activation promotes follicle miniaturization in scalp hair while stimulating growth in body hair. By blocking AR, bicalutamide can attenuate follicular response to endogenous androgens.

In the context of minoxidil-induced hypertrichosis — a recognized side effect of systemic or topical minoxidil use — the excessive hair growth may be partially mediated through androgen-responsive follicular pathways. AR antagonism could theoretically reduce this unwanted growth by dampening follicular sensitivity to endogenous androgens. This provides a mechanistically coherent, if narrow, rationale for the TxGNN prediction.

It is important to note that this application is highly specific: the sole published commentary concerns managing a drug-induced side effect, not a primary disease indication. Furthermore, not all forms of hypertrichosis are androgen-driven — for example, the congenital Ambras type (also predicted by TxGNN at rank 3) is caused by chromosomal rearrangements affecting TRPS1/HR gene regulation, where AR antagonism has no pharmacological basis. The therapeutic scope of bicalutamide in hypertrichosis is therefore very narrow and requires prospective study.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35304167](https://pubmed.ncbi.nlm.nih.gov/35304167/) | 2022 | Letter / Comment | Journal of the American Academy of Dermatology | Expert commentary responding to a retrospective review of 35 patients, reporting that bicalutamide can improve minoxidil-induced hypertrichosis in female pattern hair loss; no new primary data presented |

---

## Netherlands Market Information

Bicalutamide is currently **not registered** with the CBG-MEB (College ter Beoordeling van Geneesmiddelen). No RVG marketing authorization numbers are on record, and there are no active licenses in the Netherlands. Any clinical use would require access via a special import procedure or a named-patient / compassionate use basis, subject to CBG-MEB authorization.

> Note: Bicalutamide (brand name Casodex) holds regulatory approval in many other countries for prostate cancer treatment. For prescribing information applicable to Dutch clinical practice, clinicians should consult the EMA SmPC or the authorized SmPC from another EU member state.

---

## Cytotoxicity

Bicalutamide is used in the treatment of prostate cancer and qualifies for this section as an antineoplastic agent.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Non-steroidal antiandrogen (hormone therapy); **not** a conventional cytotoxic agent |
| Myelosuppression Risk | Low — bicalutamide does not cause myelosuppression |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (LFTs) at baseline and periodically due to hepatotoxicity risk; PSA monitoring in prostate cancer settings; standard CBC |
| Handling Protection | Standard pharmaceutical handling procedures apply; specialized cytotoxic handling measures are not required |

---

## Safety Considerations

No formal SmPC safety data is available from the CBG-MEB registry as bicalutamide is not registered in the Netherlands. Please refer to the EMA SmPC or international SmPC (e.g., Casodex) for complete safety information. Key areas of clinical relevance from the international prescribing information include:

- **Known class effects**: Hepatotoxicity (including rare fatal cases), gynaecomastia and breast pain, hot flushes, decreased libido
- **Drug–drug interactions**: Bicalutamide is a CYP3A4 substrate and inhibitor; a clinically significant interaction with warfarin has been documented (potentiation of anticoagulant effect requiring INR monitoring)
- **Special populations**: Contraindicated in women of childbearing potential due to teratogenic risk; not indicated for use in children

No DDI records, specific Dutch-market warnings, or CBG-MEB contraindication data were retrieved for this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only available supporting evidence is a single expert commentary letter discussing bicalutamide for a drug side-effect management scenario — a highly narrow application with L4 evidence only. This is insufficient to support a formal drug repurposing recommendation within the Dutch healthcare system at this time.

**To proceed, the following is needed:**

- Prospective clinical studies or well-designed retrospective case series specifically evaluating bicalutamide for hypertrichosis (particularly minoxidil-induced cases)
- Formal MOA data retrieval from the DrugBank API (DrugBank ID: DB01128) to complete the mechanistic gap analysis (currently flagged as a High-severity data gap)
- Full safety profile review from EMA SmPC or equivalent to assess risk–benefit appropriateness for Dutch patients
- Clarification of the CBG-MEB regulatory pathway for off-label or compassionate use, should a pilot clinical investigation be proposed
- Consideration of whether the narrow scope of this indication — management of a minoxidil side effect — justifies a standalone repurposing program, or whether resources should be directed toward bicalutamide candidates with substantially stronger evidence, notably **female breast carcinoma (AR-positive/TNBC)**, which carries L2 evidence including an active Phase 2 clinical trial (NCT03650894) and 20 supporting publications

---

> ⚠️ **Disclaimer**: This report is intended for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. This analysis reflects data available as of 2026-04-03.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

