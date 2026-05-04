---
layout: default
title: Celecoxib
parent: 僅模型預測 (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
---

# Celecoxib
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

# Celecoxib: From Arthritis and Pain to Inflammatory Spondylopathy

## One-Sentence Summary

Celecoxib is a selective COX-2 inhibitor widely used for the symptomatic treatment of osteoarthritis, rheumatoid arthritis, and musculoskeletal pain. The TxGNN model predicts it may be effective for **Inflammatory Spondylopathy** (ankylosing spondylitis / axial spondyloarthritis), with **19 clinical trials** and **20 publications** currently supporting this direction. Importantly, celecoxib already holds an EMA-wide marketing authorization for ankylosing spondylitis — meaning this prediction validates a well-established indication rather than proposing a genuinely novel repurposing, though its current absence from the Dutch RVG national register warrants regulatory clarification.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Symptomatic treatment of osteoarthritis and rheumatoid arthritis (COX-2 inhibitor / NSAID class) |
| Predicted New Indication | Inflammatory Spondylopathy (Ankylosing Spondylitis / Axial Spondyloarthritis) |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L1 |
| NL Market Status | Not currently registered in Dutch RVG national database |
| Number of Authorizations | 0 (RVG database; EMA central authorization may apply) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Celecoxib selectively inhibits the cyclooxygenase-2 (COX-2) enzyme, which is responsible for synthesizing prostaglandin E2 (PGE2) — a central mediator of inflammation, pain, and fever. Unlike non-selective NSAIDs, celecoxib largely spares COX-1, the isoform responsible for gastrointestinal mucosal protection. This selectivity gives celecoxib a more favorable upper GI safety profile while preserving its anti-inflammatory potency.

Inflammatory spondylopathy — encompassing ankylosing spondylitis (AS) and axial spondyloarthritis (axSpA) — is driven by chronic immune-mediated inflammation of the spine and sacroiliac joints. The COX-2/PGE2 axis is a primary contributor to the synovial inflammation, enthesitis, and bone marrow edema that characterize these conditions. NSAIDs, including COX-2 inhibitors, are the first-line pharmacological treatment per EULAR/ASAS guidelines, directly connecting celecoxib's mechanism to this disease.

A particularly compelling emerging finding (PMID 39757202, 2025) suggests that celecoxib may uniquely inhibit new bone formation (syndesmophyte progression) in spondyloarthritis through modulation of the Wnt signaling pathway — an effect not replicated with the non-selective NSAID diclofenac. This positions celecoxib not merely as a symptomatic reliever but as a potential disease-modifying agent in axSpA, lending additional mechanistic depth to the TxGNN model's high-confidence prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00648141](https://clinicaltrials.gov/study/NCT00648141) | Phase 3 | Completed | 458 | 12-week double-blind RCT comparing celecoxib 200 mg QD, 200 mg BID, and diclofenac 75 mg SR BID in AS — primary efficacy and safety evidence for the AS indication |
| [NCT00762463](https://clinicaltrials.gov/study/NCT00762463) | Phase 3 | Completed | 240 | 6-week double-blind RCT of celecoxib vs diclofenac SR in Chinese AS patients with 6-week extension phase; confirms efficacy across ethnicities |
| [NCT02758782](https://clinicaltrials.gov/study/NCT02758782) | Phase 4 | Completed | 156 | CONSUL trial: randomized controlled comparison of celecoxib + golimumab vs golimumab alone on radiographic spinal progression over 2 years in AS |
| [NCT02528201](https://clinicaltrials.gov/study/NCT02528201) | Phase 4 | Completed | 330 | 12-week double-blind RCT confirming celecoxib 200 mg and 400 mg QD vs diclofenac TID in AS — replication of earlier Phase 3 findings |
| [NCT01934933](https://clinicaltrials.gov/study/NCT01934933) | Phase 4 | Completed | 150 | Multi-center open-label RCT of etanercept alone, celecoxib alone, and combination therapy in active AS; MRI SPARCC score as primary endpoint |
| [NCT02355236](https://clinicaltrials.gov/study/NCT02355236) | Phase 4 | Unknown | 106 | Double-blind double-dummy RCT comparing Naxozol (naproxen + esomeprazole) vs celecoxib for gastro-protective and pain-relief effects in OA/RA/AS |
| [NCT05164198](https://clinicaltrials.gov/study/NCT05164198) | Phase 4 | Unknown | 448 | Multicenter prospective RCT on TNFi dose reduction in stable AS; celecoxib used as background medication — real-world usage data |
| [NCT04115098](https://clinicaltrials.gov/study/NCT04115098) | Phase 2 | Terminated | 42 | N-of-1 trials comparing selective COX-2 vs non-selective COX inhibitors in individual axSpA patients; includes proteomic biomarker assessment |
| [NCT03190603](https://clinicaltrials.gov/study/NCT03190603) | Phase 4 | Completed | 12 | MRI-based evaluation of NSAID effect on inflammatory lesions in axial SpA — imaging endpoint data |
| [NCT03473665](https://clinicaltrials.gov/study/NCT03473665) | Phase 4 | Terminated | 9 | Pilot 6-week RCT comparing 4 different NSAIDs in axial spondyloarthritis on pain score change from baseline |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39757202](https://pubmed.ncbi.nlm.nih.gov/39757202/) | 2025 | RCT/Meta-analysis | BMB Reports | Celecoxib uniquely inhibits radiographic bone progression in SpA via a COX-2-independent Wnt pathway mechanism — not replicated with diclofenac |
| [38228361](https://pubmed.ncbi.nlm.nih.gov/38228361/) | 2024 | RCT | Annals of the Rheumatic Diseases | CONSUL trial: celecoxib + golimumab did not significantly reduce spinal radiographic progression vs golimumab alone at 2 years in r-axSpA |
| [38832489](https://pubmed.ncbi.nlm.nih.gov/38832489/) | 2024 | RCT | Scandinavian Journal of Rheumatology | Iguratimod + celecoxib combination demonstrated improved efficacy vs celecoxib alone in active axSpA (randomized double-blind placebo-controlled) |
| [36800138](https://pubmed.ncbi.nlm.nih.gov/36800138/) | 2023 | RCT | Clinical Rheumatology | Imrecoxib and celecoxib both modulated bone metabolism markers and angiogenesis in sacroiliac joint inflammation in axSpA |
| [40028763](https://pubmed.ncbi.nlm.nih.gov/40028763/) | 2025 | Comparative Cohort | Scandinavian Journal of Rheumatology | Nationwide retrospective cohort: cardiovascular disease and GI bleeding risk comparable between celecoxib and non-selective NSAIDs in AS patients |
| [39315555](https://pubmed.ncbi.nlm.nih.gov/39315555/) | 2024 | Observational | Reumatismo | Long-term NSAID use in AS associated with changes in liver (AST/ALT) and kidney (creatinine) function — supports monitoring recommendations |
| [28626213](https://pubmed.ncbi.nlm.nih.gov/28626213/) | 2017 | RCT | Medical Science Monitor | Celecoxib 200 mg BID in axSpA improved BASDAI and MRI scores; serum DKK-1 levels correlated with imaging outcomes |
| [22141388](https://pubmed.ncbi.nlm.nih.gov/22141388/) | 2011 | Review | Drugs | Comprehensive review confirming EU approval of celecoxib for OA, RA, and AS in adults; demonstrates favorable GI profile vs non-selective NSAIDs |
| [17983259](https://pubmed.ncbi.nlm.nih.gov/17983259/) | 2007 | Review | Drugs | Celecoxib's clinical profile across arthritis indications; approved in multiple countries for AS; 10-year post-introduction assessment |
| [16960941](https://pubmed.ncbi.nlm.nih.gov/16960941/) | 2006 | Clinical Trial | Journal of Rheumatology | Celecoxib is efficacious and well tolerated in treating signs and symptoms of ankylosing spondylitis |

---

## Netherlands Market Information

Celecoxib is **not currently listed in the Dutch RVG (Register van Geneesmiddelen) national database** and has no Dutch-specific RVG authorization number on file in this evidence pack.

However, this requires important context: Celebrex (celecoxib) holds a **centrally authorized EMA marketing authorization** that is valid across all EU/EEA member states, including the Netherlands. Central EMA authorizations do not always generate a separate RVG national entry. The CBG-MEB (College ter Beoordeling van Geneesmiddelen) recognizes EMA central authorizations, and the product's availability in the Dutch market should be verified directly through the CBG-MEB register or the EMA product database.

The EMA-approved indication for celecoxib explicitly includes the **symptomatic treatment of ankylosing spondylitis in adults** — the very indication predicted by TxGNN. There are therefore no additional regulatory barriers specific to this indication within the EU framework.

| Action Required | Details |
|----------------|---------|
| Verify NL market availability | Check CBG-MEB database and EMA authorization status for Celebrex |
| Confirm GVS reimbursement | Verify whether celecoxib is included in the Dutch pharmaceutical reimbursement list (Geneesmiddelenvergoedingssysteem) for the AS indication |
| Review current SmPC | Obtain the Dutch-language SmPC (Samenvatting van de Productkenmerken) from the CBG-MEB for prescribing details |

---

## Safety Considerations

No detailed safety data (warnings, contraindications, or drug interactions) was available from the NL regulatory source in this evidence pack. The following considerations are drawn from the clinical literature included in the evidence review:

- **Cardiovascular risk**: As a selective COX-2 inhibitor, celecoxib carries a class-related cardiovascular risk (myocardial infarction, stroke). A nationwide retrospective cohort in AS patients (PMID 40028763, 2025) found that CV and GI bleeding risk was comparable between celecoxib and non-selective NSAIDs, providing disease-specific reassurance. Individual cardiovascular risk assessment is nonetheless warranted before initiating therapy.
- **Gastrointestinal tolerability**: Celecoxib's COX-1–sparing mechanism provides a favorable upper GI profile. A pooled analysis of 21 RCTs confirmed superior GI tolerability vs non-selective NSAIDs in elderly arthritis patients (PMID 21561397).
- **Renal and hepatic monitoring**: Long-term continuous NSAID therapy in AS patients has been associated with changes in serum creatinine, AST, and ALT (PMID 39315555). Periodic monitoring of liver and kidney function is advisable, particularly with prolonged use.

For complete prescribing information including contraindications and drug interactions, please refer to the current **SmPC (Samenvatting van de Productkenmerken)** via the CBG-MEB or EMA product database.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Celecoxib has robust L1 clinical evidence for inflammatory spondylopathy (ankylosing spondylitis/axial spondyloarthritis), underpinned by at least two completed Phase 3 RCTs (NCT00648141, N=458; NCT00762463, N=240) and a broad body of Phase 4 and observational data. The TxGNN prediction score of 99.80% is strongly supported by the mechanistic rationale (COX-2/PGE2 axis in SpA) and emerging evidence of a potential disease-modifying effect on bone progression unique to celecoxib among NSAIDs. Critically, this indication is already covered by the EMA central marketing authorization for Celebrex, so no novel regulatory pathway is required.

**To proceed, the following is needed:**
- Confirm whether Celebrex (celecoxib) is actively marketed and reimbursed in the Netherlands under the EMA central authorization — contact CBG-MEB for current status
- Clarify GVS (Geneesmiddelenvergoedingssysteem) reimbursement coverage for the AS indication in Dutch clinical practice
- Obtain the current Dutch SmPC to assess full contraindication and drug interaction profiles before initiating therapy
- Conduct individual cardiovascular risk assessment for each patient prior to prescribing, in line with Dutch prescribing guidelines for NSAIDs
- Consider whether celecoxib's potential disease-modifying effect on syndesmophyte progression (PMID 39757202) merits inclusion in a Dutch axSpA patient registry or observational study to generate local real-world evidence

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Please include appropriate YMYL disclaimers in any patient-facing materials derived from this report.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

