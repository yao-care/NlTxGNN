---
layout: default
title: Atenolol
parent: 僅模型預測 (L5)
nav_order: 27
evidence_level: L5
indication_count: 9
---

# Atenolol
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

# Atenolol: From Hypertension/Angina to Posteroinferior Myocardial Infarction

## One-Sentence Summary

Atenolol is a cardioselective β1-adrenergic blocker widely used for the treatment of hypertension, angina pectoris, and cardiac arrhythmias. The TxGNN model predicts it may be effective for **posteroinferior myocardial infarction**, with **0 clinical trials** and **1 publication** currently supporting this specific anatomical subtype, though β-blockers are well established in the broader myocardial infarction setting. Across all 9 predicted indications, the strongest evidence base exists for **chronic pulmonary heart disease** (1 clinical trial, 15 publications), though that indication carries significant mechanistic concerns.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, angina pectoris, cardiac arrhythmias (well-established β-blocker) |
| Predicted New Indication | Posteroinferior myocardial infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 (Preclinical / mechanism-level studies) |
| NL Market Status | Not found in evidence pack (Note: Atenolol is widely available in NL under multiple CBG-MEB authorizations — see section below) |
| Number of Authorizations | 0 in current dataset (regulatory data gap) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Atenolol is a selective β1-adrenergic receptor antagonist. It works by competitively blocking β1-receptors predominantly located in the heart, thereby reducing heart rate, myocardial contractility, and myocardial oxygen demand. These properties are the basis of its longstanding use in hypertension, stable angina, and post-myocardial infarction (MI) secondary prevention. Atenolol does not possess intrinsic sympathomimetic activity (ISA), making it suitable for reducing sympathetic overdrive in acute coronary events.

Posteroinferior myocardial infarction is an anatomical subtype of MI affecting the posterior and inferior walls of the left ventricle, typically caused by occlusion of the right coronary artery or the left circumflex artery. β-blockers, including atenolol, are already part of standard MI secondary prevention protocols per ESC and AHA/ACC guidelines. The TxGNN model's prediction essentially identifies that the existing pharmacological mechanism is fully applicable to this anatomical subtype — a logical extension given that β-blocker cardioprotection (reduction of infarct size, prevention of reinfarction, and reduction of sudden cardiac death) is not dependent on infarct location.

However, it is important to note that posteroinferior MI often involves the right ventricle and the cardiac conduction system (particularly the AV node), which means that β-blocker use requires additional caution. Bradycardia, AV block, and right ventricular dysfunction are specific risks in this patient population, and clinical monitoring should be more intensive than in anterior MI.

---

## Clinical Trial Evidence

Currently no clinical trials specifically studying atenolol for posteroinferior myocardial infarction are registered.

**Note:** While no trials target this specific anatomical subtype, atenolol has been extensively studied in the broader MI context. The landmark ISIS-1 trial (1986) demonstrated a 15% reduction in vascular mortality with early IV atenolol in acute MI. The following trial from a related predicted indication (chronic pulmonary heart disease) provides indirect context:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03278509](https://clinicaltrials.gov/study/NCT03278509) | Phase 4 | Active, not recruiting | 5,000 | REDUCE-SWEDEHEART: Evaluates whether long-term β-blocker therapy after MI with preserved LVEF reduces all-cause death or new MI. Results may inform the role of β-blockers across MI subtypes. |

---

## Literature Evidence

### Primary Indication: Posteroinferior Myocardial Infarction

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3901170](https://pubmed.ncbi.nlm.nih.gov/3901170/) | 1985 | Crossover RCT | Rev Med Interne | Compared anti-ischaemic effects of atenolol (200 mg) vs diltiazem (240 mg) in 23 patients with residual ischaemia 4 weeks after posteroinferior or anterior MI. Used computerized exercise testing. |

### Related Indication: Septal Myocardial Infarction (Rank 7)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7257500](https://pubmed.ncbi.nlm.nih.gov/7257500/) | 1981 | Diagnostic study | Z Kardiol | Studied changes in regional myocardial perfusion with 201-Tl stress imaging in 14 patients before and after IV atenolol (5 mg). Evaluated perfusion in 6 LV segments including septal region. |

### Related Indication: Chronic Pulmonary Heart Disease (Rank 9, most literature)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31524](https://pubmed.ncbi.nlm.nih.gov/31524/) | 1978 | Clinical study | Lille Med | Studied atenolol's effects in chronic pulmonary patients with airway obstruction. |
| [6673339](https://pubmed.ncbi.nlm.nih.gov/6673339/) | 1983 | Clinical study | Vutreshni Bolesti | Compared β-blockers in COPD patients with concomitant ischaemic heart disease over 14 days. |
| [14520850](https://pubmed.ncbi.nlm.nih.gov/14520850/) | 2003 | Comparative study | Ter Arkh | Compared efficacy and safety of atenolol, metoprolol, and bisoprolol in isolated systolic hypertension with concomitant diabetes and/or COPD. |
| [15881093](https://pubmed.ncbi.nlm.nih.gov/15881093/) | 2005 | Clinical study | Ter Arkh | Investigated respiratory disorders in IHD patients with COPD taking long-term atenolol. |
| [28982831](https://pubmed.ncbi.nlm.nih.gov/28982831/) | 2017 | Observational | BMJ Open | Population-based retrospective cohort study on asthma-COPD overlap syndrome and cardiovascular disease associations. |

---

## Netherlands Market Information

The current evidence pack does not contain CBG-MEB regulatory data. However, atenolol is a well-established medicine widely available in the Netherlands under multiple marketing authorizations. It is registered in oral formulations (tablets 25 mg, 50 mg, 100 mg) and has been marketed in the EU for decades.

> **Data Gap:** CBG-MEB license details were not included in this evidence pack. To complete this section, CBG-MEB authorization data should be retrieved from the Geneesmiddeleninformatiebank (GIB) at [https://www.geneesmiddeleninformatiebank.nl](https://www.geneesmiddeleninformatiebank.nl).

---

## Safety Considerations

> Please refer to the SmPC (Summary of Product Characteristics) for complete safety information.

**Key Clinical Considerations for Posteroinferior MI:**

- **AV Conduction:** Posteroinferior MI frequently involves the AV node (supplied by the posterior descending artery). Atenolol may worsen AV block in these patients. ECG monitoring is essential before and during treatment.
- **Right Ventricular Involvement:** Inferior MI may extend to the right ventricle. β-blockers can reduce preload-dependent cardiac output in RV infarction, potentially causing haemodynamic deterioration.
- **Bradycardia:** Patients with inferior MI are prone to vagal-mediated bradycardia. Atenolol's negative chronotropic effect may compound this risk.
- **Bronchospasm:** Although β1-selective, atenolol's selectivity diminishes at higher doses. Patients with concomitant reactive airway disease should be monitored.

---

## All Predicted Indications Overview

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Key Concern |
|------|---------------------|-------------|---------------|----------------|-------------|
| 1 | Posteroinferior myocardial infarction | 99.87% | L4 | Proceed with Guardrails | AV block risk; strong mechanistic rationale |
| 2 | Posterolateral myocardial infarction | 99.87% | L5 | Proceed with Guardrails | No direct evidence; mechanism applies |
| 3 | Malignant renovascular hypertension | 99.85% | L4 | Hold | β-blocker not first-line; doesn't address root cause (RAS) |
| 4 | Malignant hypertensive renal disease | 99.85% | L5 | Hold | Insufficient potency for hypertensive emergency |
| 5 | Pulmonary hypertension (lung disease/hypoxia) | 99.84% | L5 | Hold | ⛔ **Contraindicated** — may cause haemodynamic collapse |
| 6 | Pulmonary hypertension (multifactorial) | 99.84% | L5 | Hold | ⛔ **Contraindicated** — β-blockers harmful in PH |
| 7 | Septal myocardial infarction | 99.84% | L4 | Proceed with Guardrails | Conduction bundle damage risk; mechanism applies |
| 8 | Braddock syndrome | 99.80% | L5 | Hold | No mechanistic link; rare genetic disorder |
| 9 | Chronic pulmonary heart disease | 99.04% | L3 | Research Question | Controversial; evidence inconsistent |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction for posteroinferior myocardial infarction is mechanistically sound — atenolol's β1-selective blockade reduces myocardial oxygen demand and prevents reinfarction, and this mechanism is not dependent on infarct location. β-blockers are already standard-of-care for MI secondary prevention per ESC guidelines. However, the specific anatomical subtype (posteroinferior) carries additional risks (AV block, right ventricular involvement) that require heightened monitoring, and no dedicated clinical trials exist for this specific subtype.

**Important safety flags across all predictions:**
- Predictions #5 and #6 (pulmonary hypertension) should be **rejected** — β-blockers are generally contraindicated in pulmonary hypertension and may cause life-threatening haemodynamic deterioration.
- Prediction #8 (Braddock syndrome) has **no mechanistic basis** and should be disregarded.

**To proceed, the following is needed:**
- Retrieve CBG-MEB authorization details and SmPC for atenolol products available in the Netherlands
- Obtain detailed mechanism of action data from DrugBank (currently a data gap)
- Conduct a focused literature review of β-blocker use stratified by MI anatomical subtype (inferior vs anterior vs lateral)
- Monitor results of the REDUCE-SWEDEHEART trial (NCT03278509) for updated evidence on post-MI β-blocker benefit
- Develop a safety monitoring protocol specifically addressing AV conduction and right ventricular function in posteroinferior MI patients
- Consult SmPC warnings and contraindications (currently a data gap in this evidence pack)

---

*Disclaimer: This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. Refer to the SmPC (Samenvatting van de Productkenmerken) for authoritative prescribing information.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

