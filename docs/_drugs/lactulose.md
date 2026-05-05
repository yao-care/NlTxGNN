---
layout: default
title: Lactulose
parent: 僅模型預測 (L5)
nav_order: 81
evidence_level: L5
indication_count: 8
---

# Lactulose
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

The txgnn-pipeline skill covers infrastructure management and does not override the report generation instructions already specified in the system prompt. I will now generate the report directly from the Evidence Pack.

---

# Lactulose: From Hepatic Encephalopathy to Acute Urate Nephropathy

## One-Sentence Summary

Lactulose is a non-absorbable synthetic disaccharide with a decades-long clinical track record in treating hepatic encephalopathy and constipation, acting through gut osmotic effects and microbiome modulation.
The TxGNN model predicts it may be effective for **Acute Urate Nephropathy**,
however **no clinical trials** and **no publications** currently support this specific indication — placing the evidence at level **L5 (model prediction only)**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hepatic encephalopathy / Constipation (established clinical use; no NL registration data found in this evidence pack) |
| Predicted New Indication | Acute Urate Nephropathy |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| NL Market Status | Not Registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established clinical knowledge, Lactulose is a non-absorbable disaccharide whose primary actions include: **(1)** an osmotic laxative effect that accelerates intestinal transit, **(2)** acidification of colonic contents that suppresses ammonia-producing gram-negative bacteria, and **(3)** reduction of systemic endotoxin load by limiting bacterial translocation. Its efficacy in hepatic encephalopathy has been proven and is confirmed by multiple independent publications in this evidence pack (e.g., PMID 9145459, PMID 28875419).

Acute urate nephropathy is a distinct condition caused by the sudden crystallisation of uric acid within renal tubules — typically triggered by tumour lysis syndrome or severe hyperuricaemia — leading to tubular obstruction and acute kidney injury. This mechanism has no direct pharmacological overlap with Lactulose's known actions.

The theoretical bridge proposed by TxGNN — **gut microbiota modulation → altered purine metabolism → reduced uric acid production** — is an extremely indirect pathway that currently has no supporting preclinical or clinical evidence. The model's high score of 99.89% most plausibly reflects knowledge graph over-generalisation between renal disease nodes rather than a genuine therapeutic signal. This prediction is consistent with a model artefact and should not be prioritised for clinical development at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Netherlands Market Information

No CBG-MEB (College ter Beoordeling van Geneesmiddelen) marketing authorisations for Lactulose were identified in this evidence pack.

> **Important note:** Lactulose is a long-established generic medicine with widespread use across Europe. The absence of RVG records in this dataset is likely a data collection gap and does **not** necessarily reflect the actual market situation in the Netherlands. Before drawing any regulatory conclusions, direct verification via the **CBG-MEB online register** (geneesmiddeleninformatiebank.nl) and the **EMA product database** is strongly recommended. The relevant regulatory document to consult is the **SmPC (Samenvatting van de Productkenmerken)** for the authorised product.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for acute urate nephropathy sits at evidence level L5 — with zero supporting publications, zero clinical trials, and no mechanistically plausible pathway connecting Lactulose's gut-targeted pharmacology to uric acid crystal nephropathy. Advancing this indication would require building an entirely new evidence base from scratch with no strong scientific rationale to justify the investment.

**To proceed, the following is needed:**
- Preclinical studies (animal or in vitro) demonstrating any effect of Lactulose on uric acid metabolism, xanthine oxidase activity, or renal tubular protection under hyperuricaemic conditions
- Mechanistic data explicitly linking gut microbiome modulation to purine catabolism and uric acid production
- MOA data retrieval from DrugBank (DB00581) to establish a full pharmacological profile and assess biological plausibility
- Verification of actual NL market authorisation status via the CBG-MEB register
- Review of the authorised SmPC for contraindications, warnings, and drug interactions before any study design is considered

---

> **Context note on other TxGNN predictions:** While this report focuses on the top-ranked TxGNN prediction, it is important to flag that other predicted indications for Lactulose carry substantially stronger evidence and are better-positioned for near-term evaluation in the Dutch healthcare context:
>
> | Rank | Indication | Evidence Level | Recommendation | Trials | Publications |
> |------|-----------|---------------|----------------|--------|--------------|
> | 3 | Obstructive Jaundice | L3 | Proceed with Guardrails | 1 | 20 |
> | 4 | Bile Duct Disease | L3 | Research Question | 0 | 20 |
> | 5 | Biliary Tract Disease | L3 | Research Question | 0 | 20 |
>
> The **obstructive jaundice** indication (rank 3) is particularly notable: a direct clinical trial (NCT01090193) and a 1991 multicentre randomised controlled trial (PMID 2032107) exist, and the mechanistic basis — Lactulose reducing perioperative endotoxaemia and postoperative renal dysfunction in jaundiced surgical patients — is well described. A separate, focused report for that indication is recommended as the next step.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

