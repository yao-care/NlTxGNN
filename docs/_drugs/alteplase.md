---
layout: default
title: Alteplase
parent: 僅模型預測 (L5)
nav_order: 24
evidence_level: L5
indication_count: 9
---

# Alteplase
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

# Alteplase: From Acute Thrombolysis to Posterolateral Myocardial Infarction

## One-Sentence Summary

Alteplase is a recombinant tissue plasminogen activator (tPA), a well-established thrombolytic agent used globally for acute myocardial infarction, ischemic stroke, and pulmonary embolism. The TxGNN model predicts it may be effective for **Posterolateral Myocardial Infarction** — an anatomical subtype of acute MI — with a prediction score of **99.79%**, supported by **3 publications** but currently no dedicated clinical trials for this specific subtype. Notably, TxGNN also identifies 8 additional thrombosis-related indications, forming a coherent mechanistic cluster.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute myocardial infarction, acute ischemic stroke, pulmonary embolism (established globally; no local license data in this pack) |
| Predicted New Indication | Posterolateral Myocardial Infarction |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L4 (Case reports and mechanistic studies) |
| NL Market Status | Not available in current dataset — verify with CBG-MEB/EMA (Actilyse is EMA-authorized) |
| Number of Authorizations | 0 (in current regulatory dataset) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Alteplase is a recombinant form of human tissue plasminogen activator (tPA). It works by binding to fibrin in a thrombus and converting the entrapped plasminogen to plasmin, which then degrades the fibrin matrix of the clot. This targeted fibrinolytic mechanism is the cornerstone of reperfusion therapy in acute thrombotic occlusion of coronary arteries, cerebral arteries, and pulmonary vasculature. Major landmark trials — GUSTO, GISSI, and TAMI — have firmly established alteplase as a standard of care for acute myocardial infarction.

Posterolateral myocardial infarction is an anatomical subtype of AMI, typically caused by occlusion of the left circumflex artery (LCx) or distal branches of the right coronary artery (RCA). The thrombolytic mechanism of alteplase is fully applicable: dissolving the culprit thrombus restores myocardial perfusion regardless of the specific coronary territory involved. In fact, large-scale RCTs like GUSTO and GISSI enrolled patients with all MI subtypes, including posterolateral infarctions, but did not report results stratified by specific anatomical location.

The TxGNN prediction is therefore mechanistically sound — it identifies a gap in formal indication labelling rather than a genuinely novel therapeutic hypothesis. The prediction score of 99.79% reflects the strong biological plausibility. The same reasoning applies to other top-ranked predictions in this evidence pack, including posteroinferior MI (rank 2, 99.79%), septal MI (rank 3, 99.77%), and coronary stenosis (rank 9, 99.14%), all of which share the common pathophysiology of coronary thrombosis.

---

## Clinical Trial Evidence

No clinical trials specifically targeting alteplase for posterolateral myocardial infarction were identified. However, closely related trials from other predicted indications in this pack provide relevant evidence:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00251771](https://clinicaltrials.gov/study/NCT00251771) | N/A | Completed | 209 | RCT of catheter-directed venous thrombolysis for acute iliofemoral vein thrombosis — directly supports tPA use in thrombotic events (thrombophilia indication) |
| [NCT05540834](https://clinicaltrials.gov/study/NCT05540834) | Phase 2 | Recruiting | 70 | VET-guided tPA treatment in critically ill patients with pro-thrombotic acute respiratory failure — personalised tPA dosing in hypercoagulable states |
| [NCT00604695](https://clinicaltrials.gov/study/NCT00604695) | Phase 2 | Completed | 40 | Low-dose intracoronary tenecteplase (alteplase analogue) as adjunct during primary PCI for STEMI — supports intracoronary fibrinolytic use |
| [NCT00868855](https://clinicaltrials.gov/study/NCT00868855) | Phase 1 | Terminated | 16 | Intracoronary tPA release as predictor of MACE in non-critical coronary artery disease — directly links tPA to coronary stenosis outcomes |
| [NCT02315898](https://clinicaltrials.gov/study/NCT02315898) | Phase 2 | Completed | 40 | Inhaled tPA for pediatric plastic bronchitis — confirms tPA safety in paediatric populations |
| [NCT04366778](https://clinicaltrials.gov/study/NCT04366778) | N/A | Completed | 341 | TEM-tPA to detect COVID-19 patients at high thrombosis risk — validates tPA-based diagnostics in hypercoagulable states |
| [NCT03377465](https://clinicaltrials.gov/study/NCT03377465) | N/A | Completed | 100 | Biomarkers and predictors of ischemic stroke — observational study with limited direct relevance |

> **Note:** While no trials target posterolateral MI specifically, the landmark GUSTO trial (41,000+ patients) and GISSI trials included all MI subtypes. The absence of subtype-specific trials reflects clinical practice rather than lack of evidence.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2521226](https://pubmed.ncbi.nlm.nih.gov/2521226/) | 1989 | RCT (Subgroup) | J Am Coll Cardiol | **TAMI-1 trial**: Analysed influence of infarct location on patency after 150 mg IV rt-PA; 90-min patency rates for LAD 77%, LCx 68%, RCA 68% — directly relevant to posterolateral territory |
| [3136953](https://pubmed.ncbi.nlm.nih.gov/3136953/) | 1988 | Clinical Study | Circulation | Maintenance rt-PA infusion prevented coronary reocclusion and reduced late stenosis after thrombolysis in 68 AMI patients |
| [8721695](https://pubmed.ncbi.nlm.nih.gov/8721695/) | 1996 | Clinical Study | Catheter Cardiovasc Diagn | Lesion-directed alteplase with intracoronary heparin in 45 unstable angina patients with coronary thrombus — multicenter prospective trial |
| [8763515](https://pubmed.ncbi.nlm.nih.gov/8763515/) | 1996 | Prospective Cohort | Rev Port Cardiol | Late thrombolysis with alteplase: clarified effects on left ventricular function parameters post-MI |
| [3121335](https://pubmed.ncbi.nlm.nih.gov/3121335/) | 1987 | Clinical Study | Eur Heart J | Residual coronary stenosis after rt-PA vs streptokinase: patent artery in 82% with rt-PA vs 59% with SK at 75–90 min |
| [8480981](https://pubmed.ncbi.nlm.nih.gov/8480981/) | 1993 | Case Report | Ann Cardiol Angeiol | Cerebral embolism during late tPA fibrinolysis in posterolateral MI — highlights risk-benefit in this specific subtype |
| [9502627](https://pubmed.ncbi.nlm.nih.gov/9502627/) | 1998 | Observational | J Am Coll Cardiol | ST elevation in posterior leads (V7–V9) identifies concomitant posterior infarction during inferior MI; these patients may benefit more from thrombolysis |
| [31870492](https://pubmed.ncbi.nlm.nih.gov/31870492/) | 2020 | Clinical Study | Am J Cardiol | ICE-T-TIMI-49: Low-dose IC tenecteplase (4 mg) during PPCI — no TIMI major bleeding; supports adjunctive coronary fibrinolysis |
| [9014973](https://pubmed.ncbi.nlm.nih.gov/9014973/) | 1997 | Retrospective Cohort | J Am Coll Cardiol | GUSTO sub-study: Impact of coronary revascularization surgery on survival after thrombolysis in MI |
| [21351226](https://pubmed.ncbi.nlm.nih.gov/21351226/) | 2011 | Case Report | Catheter Cardiovasc Interv | Primary PCI of unprotected left main facilitated by intracoronary reteplase in posterolateral acute MI |

---

## Netherlands Market Information

No CBG-MEB marketing authorizations were identified in the current regulatory dataset for Alteplase.

> **Important note:** Alteplase is marketed in the EU under the brand name **Actilyse** (Boehringer Ingelheim), authorized via the EMA decentralized procedure. It is widely available in Dutch hospitals for acute MI, ischemic stroke, and pulmonary embolism. The absence of data in this report reflects a limitation of the source dataset (Taiwan TFDA), not actual unavailability in the Netherlands. Prescribers should consult the Dutch SmPC (Samenvatting van de Productkenmerken) via the CBG-MEB Geneesmiddeleninformatiebank.

---

## Safety Considerations

> Please refer to the SmPC (Summary of Product Characteristics) for comprehensive safety information.
>
> **Known class-level considerations for tPA agents (from clinical practice):**
> - **Bleeding risk**: Major haemorrhage, including intracranial haemorrhage, is the principal safety concern
> - **Contraindications typically include**: Active internal bleeding, recent (within 3 months) intracranial or intraspinal surgery/trauma, intracranial neoplasm, known bleeding diathesis, severe uncontrolled hypertension
> - **Drug interactions**: No specific DDI data was retrieved for this evidence pack. Concomitant anticoagulants (heparin, warfarin) and antiplatelet agents increase bleeding risk
>
> *The above is provided for context based on the known pharmacological profile of alteplase. Formal safety assessment requires SmPC review and should be verified through the CBG-MEB database.*

---

## All Predicted Indications Overview

The TxGNN model identified 9 indications for alteplase, forming two coherent clusters:

### Cluster 1: Myocardial Infarction Subtypes (Strong Mechanistic Link)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|---------------------|-------------|---------------|----------------|
| 1 | Posterolateral myocardial infarction | 99.79% | L4 | Proceed with Guardrails |
| 2 | Posteroinferior myocardial infarction | 99.79% | L4 | Proceed with Guardrails |
| 3 | Septal myocardial infarction | 99.77% | L3 | Proceed with Guardrails |
| 9 | Coronary stenosis | 99.14% | L3 | Research Question |

### Cluster 2: Thrombophilic/Coagulation Disorders (Moderate Mechanistic Link)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|---------------------|-------------|---------------|----------------|
| 4 | Heparin cofactor 2 deficiency | 99.72% | L5 | Hold |
| 5 | Congenital coronary artery anomaly | 99.64% | L4 | Research Question |
| 6 | Factor V excess with spontaneous thrombosis | 99.56% | L5 | Hold |
| 7 | Antithrombin deficiency type 2 | 99.56% | L5 | Hold |
| 8 | Thrombophilia | 99.43% | L3 | Research Question |

> **Interpretation:** Cluster 1 predictions represent anatomical subtypes of AMI for which alteplase is already an established treatment globally. These are "labelling gaps" rather than novel repurposing opportunities. Cluster 2 predictions involve rare coagulation disorders where alteplase addresses thrombotic complications but not the underlying deficiency — these represent genuinely novel but weaker repurposing candidates.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Alteplase's efficacy in acute myocardial infarction is established through landmark RCTs (GUSTO, GISSI, TAMI) that included all MI subtypes. The posterolateral MI prediction reflects a labelling specificity gap rather than a novel therapeutic hypothesis. The mechanistic link is strong: fibrinolysis of the culprit thrombus in the left circumflex or distal RCA territory is fully consistent with alteplase's proven mechanism. For the thrombophilia-related predictions (ranks 4–8), the evidence is weaker and the mechanistic rationale is limited to treating complications rather than root causes.

**To proceed, the following is needed:**
- Verify Actilyse (alteplase) marketing authorization status via CBG-MEB Geneesmiddeleninformatiebank and obtain the Dutch SmPC
- Obtain detailed mechanism of action data from DrugBank to complete the pharmacological profile
- Conduct a subgroup analysis of existing large-scale AMI trials (GUSTO, GISSI) for posterolateral MI outcomes, if not already published
- For thrombophilia indications: monitor NCT05540834 (Phase 2, VET-guided tPA in pro-thrombotic respiratory failure) for results expected 2026–2027
- Establish a safety monitoring framework with emphasis on bleeding risk assessment in the specific patient populations

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All web pages should include YMYL (Your Money or Your Life) disclaimers.*

*Data cutoff: 2026-04-03 | Evidence Pack version: v4 | Candidate ID: TW-DB00009-multi*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

