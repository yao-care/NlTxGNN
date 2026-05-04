---
layout: default
title: Cytarabine
parent: 僅模型預測 (L5)
nav_order: 48
evidence_level: L5
indication_count: 9
---

# Cytarabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

Using the `txgnn-pipeline` skill (NL deployment) to generate the Netherlands drug repurposing evaluation report for Cytarabine.

---

# Cytarabine: From Acute Myeloid Leukaemia to Small Cell Lung Carcinoma

## One-Sentence Summary

Cytarabine (cytosine arabinoside, Ara-C) is a well-established pyrimidine antimetabolite with long-standing clinical use in haematological malignancies, particularly acute myeloid leukaemia (AML).
The TxGNN model predicts it may be effective for **Small Cell Lung Carcinoma (SCLC)**,
with **3 clinical trials** and **20 publications** currently identified — though the majority of this evidence is indirect or from historical studies predating modern SCLC treatment protocols.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute myeloid leukaemia (well-established clinical use; no CBG-MEB marketing authorisation data found for NL) |
| Predicted New Indication | Small Cell Lung Carcinoma |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L3 |
| NL Market Status | Not Authorized |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on established pharmacology, Cytarabine is a pyrimidine antimetabolite that is phosphorylated intracellularly to its active triphosphate form (ara-CTP), which inhibits DNA polymerase alpha and incorporates into nascent DNA strands, thereby blocking DNA synthesis. This mechanism is cell-cycle specific — active exclusively in the S-phase — making it most effective against rapidly dividing tumour cells.

Small cell lung carcinoma (SCLC) is defined by an extremely high proliferative index (Ki-67 typically >80%) and aggressive neuroendocrine biology, which in principle renders it sensitive to S-phase-specific agents such as Cytarabine. Historically, this rationale was acted upon: in the 1970s–1980s, Cytarabine was incorporated into multi-agent SCLC regimens — including cyclophosphamide/Adriamycin/cytosine arabinoside combinations and VP-16/Ara-C salvage protocols — with modest clinical responses observed. Laboratory data further demonstrate that multidrug-resistant SCLC cell lines paradoxically show collateral sensitivity to Cytarabine, providing a potential niche in refractory disease.

However, the modern SCLC treatment landscape has moved decisively toward etoposide–platinum (EP) regimens, and more recently to EP combined with atezolizumab as first-line chemoimmunotherapy. Cytarabine is absent from current ESMO and NCCN SCLC guidelines. The TxGNN prediction reflects a biologically coherent historical signal, but its clinical relevance in contemporary practice is limited and the evidence base is predominantly retrospective or preclinical.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03101579](https://clinicaltrials.gov/study/NCT03101579) | Phase 1 | Completed | 13 | Intrathecal pemetrexed for recurrent leptomeningeal metastasis from NSCLC; Cytarabine cited as existing standard of intrathecal chemotherapy — indirect evidence of Ara-C role in lung cancer CNS disease |
| [NCT03507244](https://clinicaltrials.gov/study/NCT03507244) | Phase 1/2 | Completed | 34 | Intrathecal pemetrexed combined with involved-field radiotherapy for leptomeningeal metastasis from solid tumours; conceptually supports intrathecal Ara-C framework in lung cancer meningeal involvement |
| [NCT00863512](https://clinicaltrials.gov/study/NCT00863512) | Phase 3 | Terminated | 34 | Adjuvant chemotherapy (vinorelbine, cisplatin, docetaxel, gemcitabine, pemetrexed) in early-stage NSCLC; terminated early due to low accrual and does not include Cytarabine — minimal relevance |

> ⚠️ **Important caveat:** All three identified trials are indirect — none directly evaluate Cytarabine in SCLC. Trials primarily concern NSCLC or alternative agents. No contemporary Phase 2 or Phase 3 trial evidence exists for Cytarabine in SCLC within the current search scope.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [2841844](https://pubmed.ncbi.nlm.nih.gov/2841844/) | 1988 | Phase II-type clinical study | Am J Clin Oncol | VP-16 + continuous-infusion Ara-C (45 mg/m²/day × 72 h) in 17 refractory SCLC patients; direct evidence of Cytarabine in SCLC salvage setting — most clinically relevant study in this dataset |
| [6095640](https://pubmed.ncbi.nlm.nih.gov/6095640/) | 1984 | Clinical series | Am J Clin Oncol | Ara-C 100 mg/m²/day by continuous infusion in SCLC: no responses in 10 heavily pre-treated patients; Ara-C added to CAV in 25 extensive-stage SCLC patients with severe toxicity |
| [232239](https://pubmed.ncbi.nlm.nih.gov/232239/) | 1979 | Retrospective case series | Med Pediatr Oncol | Cyclophosphamide + Adriamycin + cytosine arabinoside + radiotherapy in 20 untreated SCLC patients; earliest documented use of Cytarabine in SCLC combination regimens |
| [9363869](https://pubmed.ncbi.nlm.nih.gov/9363869/) | 1997 | Randomized Trial | J Clin Oncol | CALGB randomized study of chemoradiotherapy ± warfarin in limited-stage SCLC; provides context for historical Cytarabine-era combination protocols in SCLC |
| [6264785](https://pubmed.ncbi.nlm.nih.gov/6264785/) | 1981 | Case series | Am J Med | Meningeal carcinomatosis in SCLC (60 patients); highlights CNS complications in SCLC as a specific clinical niche where intrathecal Cytarabine remains a treatment option |
| [28223673](https://pubmed.ncbi.nlm.nih.gov/28223673/) | 2017 | Case report | Gan to Kagaku Ryoho | SCLC (Stage IV) with meningeal carcinomatosis effectively managed with multidisciplinary approach including intrathecal chemotherapy; real-world precedent for IT-Ara-C in SCLC CNS disease |
| [11331076](https://pubmed.ncbi.nlm.nih.gov/11331076/) | 2001 | Basic research | Biochem Pharmacol | Daunorubicin- and VM-26-resistant SCLC cell lines show collateral sensitivity to gemcitabine and Cytarabine; mechanistic rationale for Ara-C in MDR SCLC |
| [1360876](https://pubmed.ncbi.nlm.nih.gov/1360876/) | 1992 | Basic research | Cancer Chemother Pharmacol | Comparative drug sensitivity patterns across SCLC cell lines; evaluates cross-resistance profiles relevant to Cytarabine positioning |
| [2992752](https://pubmed.ncbi.nlm.nih.gov/2992752/) | 1985 | In vitro | Cancer | Five human SCLC cell lines grown as 3D spheroid models; drug efficacy panel including multiple chemotherapeutic agents — provides preclinical screening context |
| [348088](https://pubmed.ncbi.nlm.nih.gov/348088/) | 1978 | Review | Antibiotics Chemother | Comprehensive review of Ara-C and its analogues; discusses rapid deactivation by cytidine deaminase and strategies (e.g., enzyme inhibitors, structural derivatives) to enhance clinical activity |

---

## Netherlands Market Information

No active CBG-MEB marketing authorisations were found for Cytarabine under this INN in the Netherlands. This may reflect that available formulations are centrally authorised at EU level through the EMA, or that the data extraction did not capture all authorisations.

Clinicians in the Netherlands requiring authorised product information should consult:
- [CBG-MEB product database](https://www.cbg-meb.nl/) for nationally authorised products
- [EMA medicines database](https://www.ema.europa.eu/en/medicines) for centrally authorised products
- The relevant SmPC (Samenvatting van de Productkenmerken) for approved indications and safety information

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Pyrimidine antimetabolite (nucleoside analogue class) |
| Myelosuppression Risk | High — dose-dependent; Grade IV myelosuppression reported in 32% of patients at high-dose regimens (3 g/m² IV, PMID 2156598); Grade III in an additional 14% |
| Emetogenicity Classification | Low to moderate at standard doses; high-dose regimens (≥1 g/m²) associated with significant nausea, vomiting, and additional toxicities including conjunctivitis and cerebellar syndrome |
| Monitoring Items | Complete blood count (CBC) with differential, liver function tests (LFTs), renal function (creatinine, eGFR), neurological assessment — especially with high-dose or intrathecal administration |
| Handling Protection | Must be handled in accordance with cytotoxic drug handling regulations; appropriate PPE (gloves, gown, eye protection) required; preparation in a laminar flow hood recommended |

---

## Safety Considerations

Please refer to the SmPC (Samenvatting van de Productkenmerken) for complete safety information. No Dutch or EU-specific warnings, contraindications, or drug interaction data were available in the current Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the TxGNN model assigns a high prediction score (99.78%) and there is historical clinical precedent from the 1979–1988 era for Cytarabine use in SCLC, modern SCLC treatment has evolved substantially — current first-line standards (EP ± atezolizumab) do not include Cytarabine, and all identified contemporary clinical trials are indirect. The evidence base is predominantly retrospective case series and in vitro data, warranting a "Research Question" designation rather than an actionable repurposing signal.

**To proceed, the following is needed:**
- Retrieve complete mechanism of action data from DrugBank (currently a Data Gap) to formally document the S-phase specificity rationale
- Obtain the relevant SmPC from CBG-MEB or EMA for current NL-approved safety and contraindication profile
- Review current ESMO/NCCN SCLC guidelines to identify specific niches where Cytarabine-containing regimens may still apply (e.g., intrathecal therapy for leptomeningeal metastasis, salvage after EP failure in MDR disease)
- Assess feasibility of a prospective Phase 2 trial in relapsed/refractory SCLC, potentially combining Cytarabine with modern backbone regimens or exploiting the collateral sensitivity phenotype in MDR tumours
- Evaluate whether a systematic review or meta-analysis of historical SCLC + Cytarabine data (1979–1997) could provide a more robust quantitative estimate of activity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

