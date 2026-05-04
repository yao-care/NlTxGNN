---
layout: default
title: Azathioprine
parent: 僅模型預測 (L5)
nav_order: 28
evidence_level: L5
indication_count: 10
---

# Azathioprine
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

# Azathioprine: From Immunosuppression to Inflammatory Bowel Disease

## One-Sentence Summary

Azathioprine is a well-established purine antimetabolite immunosuppressant, historically used for organ transplant rejection prevention and autoimmune diseases. The TxGNN model predicts it may be effective for **Inflammatory Bowel Disease (IBD)**, with **50 clinical trials** and **20 publications** currently supporting this direction — notably, this prediction aligns with azathioprine's already-approved use for IBD in the Netherlands and internationally, serving as a strong validation of the model.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Immunosuppression (autoimmune diseases, organ transplant rejection) |
| Predicted New Indication | Inflammatory Bowel Disease |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L1 (multiple completed Phase 3 RCTs) |
| NL Market Status | Marketed (Azathioprine is registered in the Netherlands; note: the evidence pack contains Taiwan regulatory data showing "Not marketed" in Taiwan) |
| Number of Authorizations | Not available for NL in this dataset |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Azathioprine is a prodrug of 6-mercaptopurine, which inhibits purine synthesis, reduces lymphocyte proliferation, and suppresses pro-inflammatory cytokines (TNF-α, IL-6). By dampening the adaptive immune response, azathioprine effectively controls the dysregulated immune activation that drives chronic intestinal inflammation in IBD.

Inflammatory bowel disease — encompassing both Crohn's disease and ulcerative colitis — is fundamentally an immune-mediated condition where the gut's adaptive and innate immune systems mount an inappropriate response against intestinal flora and mucosal antigens. Azathioprine's mechanism of suppressing lymphocyte-driven inflammation directly addresses this core pathology, making the TxGNN prediction mechanistically well-grounded.

Remarkably, this prediction is already clinically validated: azathioprine was approved for long-term therapy of Crohn's disease in the Netherlands and is recognized worldwide as a first-line immunomodulatory maintenance therapy for both Crohn's disease and ulcerative colitis. Multiple Cochrane systematic reviews and landmark trials (e.g., SONIC trial, NCT00094458) have confirmed its efficacy. The TxGNN model's correct identification of this established drug-disease relationship serves as a powerful positive control for the model's predictive accuracy.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00094458](https://clinicaltrials.gov/study/NCT00094458) | Phase 3 | Completed | 508 | SONIC trial: IFX + AZA combination vs. AZA or IFX monotherapy in CD naïve to immunomodulators and biologics; demonstrated superiority of combination therapy |
| [NCT05040464](https://clinicaltrials.gov/study/NCT05040464) | Phase 3 | Recruiting | 166 | Head-to-head RCT comparing AZA vs. MTX as combination partner with adalimumab in Crohn's disease |
| [NCT03185611](https://clinicaltrials.gov/study/NCT03185611) | Phase 3 | Unknown | 120 | Rifaximin + thiopurine vs. thiopurine alone for preventing postoperative endoscopic recurrence in CD |
| [NCT00976690](https://clinicaltrials.gov/study/NCT00976690) | Phase 3 | Completed | 83 | AZA vs. mesalazine for prevention of postoperative CD recurrence; assessed AZA superiority |
| [NCT07424040](https://clinicaltrials.gov/study/NCT07424040) | N/A | Not Yet Recruiting | 154 | Infliximab monotherapy vs. IFX + AZA combination in pediatric Crohn's disease |
| [NCT02852694](https://clinicaltrials.gov/study/NCT02852694) | Phase 4 | Completed | 192 | Risk-stratified trial: MTX vs. AZA for maintaining remission in low-risk pediatric CD |
| [NCT00554710](https://clinicaltrials.gov/study/NCT00554710) | Phase 4 | Completed | 129 | Top-down (early immunomodulators/biologics) vs. step-up strategy in newly diagnosed CD (Benelux study) |
| [NCT00546546](https://clinicaltrials.gov/study/NCT00546546) | Phase 4 | Completed | 120 | Early immunosuppressant prescription vs. conventional strategy on 3-year CD course |
| [NCT05584228](https://clinicaltrials.gov/study/NCT05584228) | N/A | Not Yet Recruiting | 150 | SMART trial: AZA + subcutaneous IFX vs. ileocecal resection in symptomatic stricturing small bowel CD |
| [NCT03464136](https://clinicaltrials.gov/study/NCT03464136) | Phase 3b | Completed | 386 | Ustekinumab vs. adalimumab in biologic-naïve CD patients who failed conventional therapy including AZA |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29293971](https://pubmed.ncbi.nlm.nih.gov/29293971/) | 2018 | Review | J Crohn's Colitis | State-of-the-art overview of thiopurine (AZA/MP/TG) treatment in IBD: indications, efficacy, and safety by expert panel |
| [19072367](https://pubmed.ncbi.nlm.nih.gov/19072367/) | 2008 | Mechanistic Review | Expert Rev Gastroenterol Hepatol | 45 years of clinical experience with thiopurines in IBD; strong data from RCTs and meta-analyses documenting efficacy |
| [30889246](https://pubmed.ncbi.nlm.nih.gov/30889246/) | 2019 | Translational Research | Inflamm Bowel Dis | AZA induces autophagy via mTORC1 and PERK pathways — a novel molecular mechanism relevant to CD treatment |
| [37586320](https://pubmed.ncbi.nlm.nih.gov/37586320/) | 2023 | Translational Research | Cell Rep Med | Commensal bacteria (B. wexlerae) promote AZA therapy failure in IBD by decreasing 6-MP bioavailability |
| [22072847](https://pubmed.ncbi.nlm.nih.gov/22072847/) | 2011 | Clinical Review | World J Gastroenterol | Optimizing 6-MP and AZA therapy: 6-TGN levels correlate with efficacy, 6-MMP with toxicity |
| [16048561](https://pubmed.ncbi.nlm.nih.gov/16048561/) | 2005 | Pharmacogenomics Review | J Gastroenterol Hepatol | AZA/6-MP pharmacogenetics and metabolite monitoring; TPMT polymorphisms and dosing implications |
| [36462311](https://pubmed.ncbi.nlm.nih.gov/36462311/) | 2023 | Pharmacogenomics | Biomed Pharmacother | DNA methylation of TPMT affects AZA pharmacokinetics in VEO-IBD children |
| [10499471](https://pubmed.ncbi.nlm.nih.gov/10499471/) | 1999 | Comprehensive Review | Scand J Gastroenterol Suppl | AZA clinical efficacy and safety update — documents approval for Crohn's disease in the Netherlands |
| [15177535](https://pubmed.ncbi.nlm.nih.gov/15177535/) | 2004 | Clinical Review | Gastroenterol Clin North Am | Critical review of 6-MP and AZA efficacy and toxicities in IBD |
| [30954317](https://pubmed.ncbi.nlm.nih.gov/30954317/) | 2019 | Review | Gastroenterol Hepatol | Evidence on optimal duration and withdrawal of thiopurine therapy in IBD |

## Ulcerative Colitis — Secondary Prediction (Rank 9)

The TxGNN model also independently predicts azathioprine for **ulcerative colitis** (score: 99.33%, Evidence Level: L1), which is a subtype of IBD. This prediction is supported by equally robust evidence:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03101800](https://clinicaltrials.gov/study/NCT03101800) | Phase 3 | Unknown | 84 | Low-dose AZA + allopurinol vs. AZA monotherapy in UC — directly evaluates AZA dosing strategies |
| [NCT02425852](https://clinicaltrials.gov/study/NCT02425852) | Phase 4 | Completed | 65 | Early AZA + IFX vs. corticosteroids + AZA for acute severe UC |
| [NCT00537316](https://clinicaltrials.gov/study/NCT00537316) | Phase 3 | Terminated | 242 | IFX monotherapy vs. IFX + AZA vs. AZA monotherapy in moderate-to-severe active UC |
| [NCT07235904](https://clinicaltrials.gov/study/NCT07235904) | Phase 4 | Recruiting | 300 | MIRACLE trial: Mirikizumab vs. AZA as standard of care in newly diagnosed moderate-to-severe UC |
| [NCT07271069](https://clinicaltrials.gov/study/NCT07271069) | N/A | Not Yet Recruiting | 150 | Real-world: Ozanimod vs. AZA for UC in Japan |

**Key UC Literature:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40013523](https://pubmed.ncbi.nlm.nih.gov/40013523/) | 2025 | Cochrane Systematic Review | Cochrane Database Syst Rev | Updated Cochrane review: AZA and 6-MP for maintenance of remission in UC |
| [39586616](https://pubmed.ncbi.nlm.nih.gov/39586616/) | 2025 | RCT | Gut | ACTIVE trial: Top-down IFX + AZA vs. AZA alone in acute severe UC responding to IV steroids |
| [19392869](https://pubmed.ncbi.nlm.nih.gov/19392869/) | 2009 | Meta-analysis | Aliment Pharmacol Ther | Meta-analysis confirming AZA/6-MP efficacy in UC |
| [27192092](https://pubmed.ncbi.nlm.nih.gov/27192092/) | 2016 | Cochrane Systematic Review | Cochrane Database Syst Rev | AZA and 6-MP for UC remission maintenance |
| [9412914](https://pubmed.ncbi.nlm.nih.gov/9412914/) | 1997 | Clinical Study | J Clin Gastroenterol | AZA in steroid-resistant and steroid-dependent UC: clinical outcomes |

## Netherlands Market Information

The evidence pack contains Taiwan regulatory data (showing azathioprine as "Not marketed" in Taiwan with 0 licenses). However, **azathioprine is well-established in the Netherlands**:

| Item | Content |
|------|------|
| Market Status (NL) | Marketed — azathioprine has been registered and widely prescribed in the Netherlands for decades |
| CBG-MEB Authorization | Available as Imuran® and generic formulations |
| Known NL Approvals | Crohn's disease (documented since 1999, PMID 10499471), organ transplant rejection, autoimmune hepatitis, severe rheumatoid arthritis, SLE, dermatomyositis |
| Dosage Forms | Oral tablets (25 mg, 50 mg); injectable formulations |
| SmPC Reference | Consult the CBG-MEB Geneesmiddeleninformatiebank for current Dutch SmPC |

> **Note:** Detailed CBG-MEB license numbers (RVG numbers) were not included in this evidence pack. Please consult the [CBG-MEB database](https://www.geneesmiddeleninformatiebank.nl/) for complete authorization details.

## Other TxGNN Predictions

The TxGNN model generated 10 predictions for azathioprine. Beyond IBD and UC (discussed above), the remaining 8 predictions are all classified as **Hold** due to lack of mechanistic rationale or absence of clinical evidence:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Rationale |
|------|---------|-------------|----------------|----------------|-----------|
| 1 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.99% | L5 | Hold | Congenital developmental anomaly; no immune-mediated pathology; no clinical evidence |
| 2 | Brachydactyly-syndactyly syndrome | 99.99% | L5 | Hold | Genetic skeletal defect (GDF5/BMPR1B); not inflammatory; no clinical evidence |
| 3 | Osteoarthritis susceptibility | 99.70% | L5 | Hold | Genetic susceptibility phenotype; AZA cannot modify genetic predisposition |
| 4 | WHIM syndrome | 99.68% | L5 | Hold | Primary immunodeficiency (CXCR4 mutation); immunosuppression is **contraindicated** |
| 6 | Chronic granulomatous disease (AR type 5) | 99.41% | L5 | Hold | NADPH oxidase deficiency; further immunosuppression would worsen infection risk |
| 7 | Osteoarthritis | 99.40% | L4 | Hold | Degenerative/mechanical pathology; systemic immunosuppression risk outweighs benefit |
| 8 | Granulomatous disease with neutrophil chemotaxis defect | 99.37% | L5 | Hold | Innate immune deficiency; AZA would worsen immune function |
| 10 | Acromesomelic dysplasia, Hunter-Thompson type | 99.27% | L5 | Hold | GDF5 homozygous mutation; gene-driven developmental defect; no treatment logic |

> **Important safety note:** Predictions for WHIM syndrome (Rank 4), chronic granulomatous disease (Rank 6), and granulomatous disease with neutrophil chemotaxis defect (Rank 8) represent immunodeficiency conditions where azathioprine use would be **mechanistically contraindicated**, as further immunosuppression could cause life-threatening infections.

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics; Dutch: Samenvatting van de Productkenmerken) for comprehensive safety information. The SmPC is available via the [CBG-MEB Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/).

Key safety considerations known from established clinical use include:
- **Myelosuppression:** Dose-dependent bone marrow suppression (leukopenia, thrombocytopenia, anaemia); TPMT and NUDT15 genotyping recommended before initiation
- **Hepatotoxicity:** Elevated 6-MMP metabolite levels associated with liver injury
- **Infection risk:** Increased susceptibility to opportunistic infections due to immunosuppression
- **Malignancy risk:** Long-term use associated with increased risk of lymphoproliferative disorders (particularly hepatosplenic T-cell lymphoma when combined with anti-TNF agents in young males)
- **Pharmacogenomics:** TPMT and NUDT15 polymorphisms significantly affect drug metabolism; pre-treatment genotyping is recommended by EMA guidelines
- **Drug interactions:** Allopurinol markedly increases 6-TGN levels (dose reduction to 25-33% required); 5-aminosalicylates may increase thiopurine toxicity

> **Note:** Detailed DDI, warnings, and contraindications data were not available in this evidence pack. The items listed above are derived from the clinical trial and literature evidence reviewed.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Azathioprine for inflammatory bowel disease represents a validated prediction — the drug is already an approved and guideline-recommended therapy for both Crohn's disease and ulcerative colitis in the Netherlands and globally. Multiple completed Phase 3 RCTs, Cochrane systematic reviews, and meta-analyses provide L1-level evidence confirming its efficacy in maintaining steroid-free remission. The TxGNN model's correct identification of this established drug-disease relationship serves as a strong positive control for the model's overall predictive validity.

**To proceed, the following is needed:**
- **Obtain NL-specific regulatory data:** Retrieve current CBG-MEB authorization details (RVG numbers, approved indications, current SmPC) from the Geneesmiddeleninformatiebank
- **Complete safety profile:** Download and parse the current Dutch SmPC for detailed warnings, contraindications, and drug interactions
- **Mechanism of action data:** Query DrugBank API for structured MOA data (known: purine antimetabolite → 6-MP → 6-TGN → lymphocyte apoptosis via Rac1 inhibition)
- **Pharmacogenomic screening protocol:** Ensure TPMT and NUDT15 genotyping is integrated into any prescribing pathway, per current EMA and DPWG (Dutch Pharmacogenetics Working Group) guidelines
- **Therapeutic drug monitoring:** Establish 6-TGN and 6-MMP metabolite monitoring protocols for dose optimization
- **Evaluate model performance:** Use this validated prediction as a benchmark to assess TxGNN model reliability for other, less-established drug-disease predictions

---

*This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All treatment decisions should be made by qualified healthcare professionals in accordance with current clinical guidelines and the applicable SmPC.*

*Data cutoff: 2026-04-03 | Evidence Pack version: v4 | Candidate ID: TW-DB00993-multi*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

