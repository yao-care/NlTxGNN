---
layout: default
title: Capecitabine
parent: 僅模型預測 (L5)
nav_order: 38
evidence_level: L5
indication_count: 10
---

# Capecitabine
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

# Capecitabine: From Colorectal Cancer to Gastric Tubular Adenocarcinoma

## One-Sentence Summary

Capecitabine is an oral fluoropyrimidine prodrug that serves as a tumour-selective precursor to 5-fluorouracil (5-FU), globally approved as standard-of-care treatment for colorectal cancer and breast cancer.
The TxGNN model predicts it may be effective for **Gastric Tubular Adenocarcinoma** — the most prevalent histological subtype of gastric cancer (Lauren intestinal type) — with a prediction confidence of **99.94%**.
This prediction is supported by **20 publications** including at least **8 completed Phase 3 RCTs** in which capecitabine, as the CAPOX regimen, served as either the experimental arm or the standard chemotherapy backbone, collectively constituting Level 1 (L1) evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Colorectal cancer; breast cancer (oral fluoropyrimidine prodrug of 5-FU, globally approved) |
| Predicted New Indication | Gastric Tubular Adenocarcinoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| NL Market Status | No CBG-MEB national registration identified; likely centrally authorised via EMA (Xeloda, Roche) |
| Number of Authorizations | 0 (CBG-MEB national) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Capecitabine is an orally bioavailable prodrug that undergoes a three-step enzymatic cascade: intestinal absorption, hepatic conversion to 5′-deoxy-5-fluorouridine (5′-DFUR), and final tumour-localised conversion to 5-fluorouracil (5-FU) by thymidine phosphorylase (TP). Because TP is markedly overexpressed in many solid tumours relative to surrounding healthy tissue, this final step preferentially delivers cytotoxic 5-FU within the tumour microenvironment, sparing normal cells. Once activated, 5-FU inhibits thymidylate synthase (TS), blocking de novo pyrimidine synthesis and halting DNA replication in rapidly dividing cancer cells.

Gastric tubular adenocarcinoma — classified under the Lauren intestinal type — is the most prevalent subtype of gastric cancer and is characterised by high TP expression, creating the precise biological substrate for Capecitabine's tumour-selective activation pathway. The mechanistic overlap between Capecitabine's established activity in colorectal cancer (another gastrointestinal epithelial malignancy with high TP expression) and gastric tubular adenocarcinoma is compelling: both share similar TP-dependent fluoropyrimidine metabolism, TS-mediated cytotoxicity, and fluoropyrimidine sensitivity profiles. Molecular studies have further demonstrated that the MALAT1-miRNA regulatory network modulates TYMS expression, influencing 5-FU-class drug efficacy in a tumour-subtype-specific manner, reinforcing the scientific basis for fluoropyrimidine use in TP-high gastric subtypes.

The TxGNN model's prediction is therefore not only consistent with established pharmacology but is directly validated by robust clinical evidence. The landmark CLASSIC Phase 3 RCT (PMID 22226517) demonstrated that CAPOX (capecitabine + oxaliplatin) as adjuvant therapy after D2 gastrectomy significantly improved disease-free survival versus surgery alone (HR = 0.68) in Stage II–IIIB gastric cancer. Subsequently, CAPOX was adopted as the standard chemotherapy backbone in numerous Phase 3 combination trials — CheckMate 649, KEYNOTE-859, ORIENT-16, RATIONALE-305, and GLOW — cementing its central role in the gastric cancer treatment landscape.

---

## Clinical Trial Evidence

No clinical trials were identified through direct registry search using "gastric tubular adenocarcinoma" as the query term. However, the literature evidence below includes multiple completed Phase 3 RCTs in which capecitabine, as part of the CAPOX regimen, was evaluated in gastric and gastroesophageal junction adenocarcinoma populations that encompass the tubular adenocarcinoma subtype. Notably, the CLASSIC trial (Phase 3, n = 1,035) directly established CAPOX efficacy in the post-D2 gastrectomy gastric cancer setting.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [22226517](https://pubmed.ncbi.nlm.nih.gov/22226517/) | 2012 | Phase 3 RCT | *Lancet* | **CLASSIC trial**: CAPOX adjuvant therapy after D2 gastrectomy significantly improved DFS vs surgery alone (HR = 0.68) in Stage II–IIIB gastric cancer — the core L1 anchor for capecitabine in gastric cancer |
| [34252374](https://pubmed.ncbi.nlm.nih.gov/34252374/) | 2021 | Phase 3 RCT | *Lancet Oncology* | **RESOLVE** (initial report): perioperative SOX vs postoperative CAPOX in locally advanced gastric/GEJ cancer after D2 gastrectomy; CAPOX confirmed as standard adjuvant reference regimen |
| [39952264](https://pubmed.ncbi.nlm.nih.gov/39952264/) | 2025 | Phase 3 RCT | *Lancet Oncology* | **RESOLVE** (final report): updated overall survival data confirming long-term efficacy of CAPOX as a standard adjuvant regimen in resectable gastric cancer |
| [37524953](https://pubmed.ncbi.nlm.nih.gov/37524953/) | 2023 | Phase 3 RCT | *Nature Medicine* | **GLOW trial**: zolbetuximab + CAPOX vs placebo + CAPOX in CLDN18.2-positive, HER2-negative metastatic gastric/GEJ adenocarcinoma; CAPOX served as the active control backbone |
| [34102137](https://pubmed.ncbi.nlm.nih.gov/34102137/) | 2021 | Phase 3 RCT | *Lancet* | **CheckMate 649**: nivolumab + chemotherapy (CAPOX backbone) vs chemotherapy alone; demonstrated OS benefit in HER2-negative advanced gastric/GEJ adenocarcinoma |
| [38806195](https://pubmed.ncbi.nlm.nih.gov/38806195/) | 2024 | Phase 3 RCT | *BMJ* | **RATIONALE-305**: tislelizumab + chemotherapy (CAPOX backbone) vs placebo + chemotherapy as first-line treatment in advanced gastric/GEJ adenocarcinoma |
| [37875143](https://pubmed.ncbi.nlm.nih.gov/37875143/) | 2023 | Phase 3 RCT | *Lancet Oncology* | **KEYNOTE-859**: pembrolizumab + capecitabine/FP + platinum vs placebo in HER2-negative advanced gastric/GEJ adenocarcinoma; capecitabine was one of the guideline-recommended backbone options |
| [38051328](https://pubmed.ncbi.nlm.nih.gov/38051328/) | 2023 | Phase 3 RCT | *JAMA* | **ORIENT-16**: sintilimab + CAPOX vs placebo + CAPOX first-line in unresectable gastric/GEJ cancer; capecitabine as core chemotherapy backbone |
| [20728210](https://pubmed.ncbi.nlm.nih.gov/20728210/) | 2010 | Phase 3 RCT | *Lancet* | **ToGA**: trastuzumab + capecitabine/5-FU + cisplatin in HER2-positive advanced gastric/GEJ cancer; established the fluoropyrimidine + targeted therapy combination paradigm |
| [30982686](https://pubmed.ncbi.nlm.nih.gov/30982686/) | 2019 | Phase 3 RCT | *Lancet* | **FLOT4**: FLOT vs ECF/ECX (capecitabine-containing) perioperative therapy in locally advanced resectable gastric/GEJ adenocarcinoma; ECX arm contained capecitabine as the fluoropyrimidine component |

---

## Netherlands Market Information

No CBG-MEB (College ter Beoordeling van Geneesmiddelen) national marketing authorisations for Capecitabine were identified in the regulatory database (0 authorisations; market status: not nationally registered).

> **Note for Dutch prescribers and pharmacists:** Capecitabine is marketed as **Xeloda** (Roche) under a centrally granted EMA authorisation that is directly valid throughout the European Economic Area, including the Netherlands, without requiring a separate CBG-MEB national approval. The absence of a CBG-MEB national registration does not indicate unavailability in the Netherlands. The applicable SmPC (Samenvatting van de Productkenmerken) is published on the EMA product database and constitutes the authoritative prescribing reference. Prescribers should verify current dispensing pathways and reimbursement status through the Dutch Medicines Reimbursement System (GVS).

---

## Cytotoxicity

Capecitabine meets the criteria for antineoplastic classification: it is a fluoropyrimidine-class cytotoxic chemotherapy drug with proven efficacy in gastrointestinal and breast malignancies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Fluoropyrimidine class (oral prodrug of 5-FU) |
| Myelosuppression Risk | Low to moderate; less myelosuppressive than intravenous 5-FU infusion regimens; neutropenia and thrombocytopenia occur, risk increases significantly in combination regimens (e.g., CAPOX with oxaliplatin) |
| Emetogenicity Classification | Low to moderate (oral fluoropyrimidines carry lower intrinsic emetogenic potential than cisplatin; emetogenicity increases when combined with oxaliplatin) |
| Monitoring Items | CBC with differential before each cycle; liver function tests (ALT, AST, bilirubin); renal function — creatinine clearance must be assessed before initiation and monitored during treatment (dose reduction required for CrCl 30–50 mL/min; contraindicated if CrCl < 30 mL/min); palmar-plantar erythrodysesthesia (hand-foot syndrome) assessment at each clinical visit |
| Handling Protection | Yes — classified as cytotoxic; institutional cytotoxic drug handling protocols apply (appropriate PPE, dedicated preparation area, closed-system drug transfer devices where applicable per Dutch pharmacy standards) |

---

## Safety Considerations

Detailed SmPC warnings and contraindications were not available in this Evidence Pack. Please refer to the EMA-approved SmPC (Samenvatting van de Productkenmerken) for Xeloda (Capecitabine) for complete safety information.

Priority areas to review in the SmPC before use in the gastric cancer setting:

- **Anticoagulant interaction**: Capecitabine significantly potentiates the effect of coumarin-type anticoagulants (warfarin, acenocoumarol), with reported cases of severe and fatal haemorrhage. INR monitoring is mandatory and dose adjustment of the anticoagulant is typically required.
- **DPD deficiency**: Patients with complete dihydropyrimidine dehydrogenase (DPD) deficiency must not receive capecitabine; partial DPD deficiency carriers require dose reduction. DPD genotyping (DPYD) prior to initiation is recommended under current European pharmacovigilance guidance.
- **Renal impairment**: Dose adjustment is required for CrCl 30–50 mL/min; capecitabine is contraindicated below CrCl 30 mL/min.
- **Cardiac toxicity**: Cardiotoxicity (angina, myocardial infarction, arrhythmia) has been reported with fluoropyrimidines; caution in patients with pre-existing coronary artery disease.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction aligns with — and is directly validated by — an extensive body of L1 clinical evidence. CAPOX (capecitabine + oxaliplatin) is already an internationally recognised standard-of-care chemotherapy backbone for gastric and gastroesophageal adenocarcinoma, including the tubular subtype, supported by the CLASSIC Phase 3 RCT and at least seven subsequent major Phase 3 trials. In this context, the repurposing opportunity for the Netherlands healthcare system relates primarily to access, reimbursement, and off-label subtype use, rather than establishing clinical efficacy from scratch.

**To proceed, the following is needed:**

- **Regulatory clarification**: Confirm EMA central authorisation status for Xeloda in the Netherlands and identify applicable CBG-MEB dispensing and reimbursement pathways (GVS listing status for gastric cancer indication)
- **SmPC safety review**: Retrieve complete Dutch SmPC; document contraindications (DPD deficiency, renal thresholds), key drug interactions (warfarin/acenocoumarol, leucovorin, phenytoin, antacids), and pregnancy/lactation restrictions for the institutional formulary
- **DPYD genotyping protocol**: Establish pre-treatment DPYD screening pathway in line with current EMA pharmacovigilance requirements
- **Subtype-specific caution**: For predicted indications with Hold status (GAPPS, microinvasive gastric cancer, EBV-associated gastric carcinoma, malignant gastric granular cell tumour), no clinical evidence supports capecitabine use — these should not proceed to clinical application without dedicated prospective investigation
- **Institutional protocol**: Confirm CAPOX cycle scheduling, antiemetic prophylaxis, and hand-foot syndrome management guidelines in the context of Dutch oncology formulary standards
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

