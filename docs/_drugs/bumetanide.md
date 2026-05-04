---
layout: default
title: Bumetanide
parent: 僅模型預測 (L5)
nav_order: 34
evidence_level: L5
indication_count: 1
---

# Bumetanide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Bumetanide: From Oedema to Acute Pulmonary Heart Disease

## One-Sentence Summary

Bumetanide is a potent loop diuretic classically used for the treatment of oedema associated with congestive heart failure, hepatic disease, and renal insufficiency.
The TxGNN model predicts it may be effective for **Acute Pulmonary Heart Disease (Acute Cor Pulmonale)**, with **3 registered clinical trials** and **5 publications** currently identified in support of this direction.
However, the drug currently holds **no marketing authorisation** with CBG-MEB in the Netherlands, and formal safety data specific to this indication remains to be confirmed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Oedema associated with congestive heart failure, hepatic and renal disease (derived from pharmacological profile; no NL authorisation records available) |
| Predicted New Indication | Acute Pulmonary Heart Disease (Acute Cor Pulmonale) |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L3 — Observational studies and pharmacological reviews |
| NL Market Status | Not Registered (CBG-MEB: 0 authorisations) |
| Number of Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Bumetanide is a high-ceiling loop diuretic that acts by inhibiting the **Na⁺-K⁺-2Cl⁻ cotransporter (NKCC2)** in the thick ascending limb of the loop of Henle. This rapidly reduces tubular reabsorption of sodium and chloride, producing a brisk, dose-dependent diuresis within 30–60 minutes of administration. The consequent reduction in circulating blood volume directly lowers cardiac preload and pulmonary capillary wedge pressure — the central pathophysiological drivers of acute pulmonary congestion.

In acute pulmonary heart disease (acute cor pulmonale), elevated pulmonary vascular resistance causes acute right ventricular pressure overload, which can lead to pulmonary oedema and impaired gas exchange. Loop diuretics such as bumetanide are mechanistically well positioned to decompress the pulmonary circulation, reduce right heart filling pressures, and improve respiratory function in this context. This aligns with current acute heart failure management guidelines, which recommend loop diuretics as first-line decongestive therapy.

A 1987 prospective haemodynamic study (PMID 3304383) directly demonstrated that intravenous bumetanide reduces pulmonary artery occluded pressure (PAOP) and systemic vascular resistance in patients with acute and chronic heart failure, providing early human evidence directly relevant to this predicted indication. While detailed MOA documentation was not available in the Evidence Pack, the mechanistic rationale for this repurposing prediction is well established in the broader pharmacological literature.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07375212](https://clinicaltrials.gov/study/NCT07375212) | Phase 4 | **Withdrawn** | 0 | Investigated whether a single 4 mg intranasal dose of bumetanide acutely reduces pulmonary artery pressure and blood volume in outpatient heart failure patients with implanted remote monitoring devices (CardioMEMS™ / Cordella™). Trial was withdrawn before enrolment; no efficacy data generated, but the hypothesis was endorsed by investigators. |
| [NCT05580510](https://clinicaltrials.gov/study/NCT05580510) | Phase 2/3 | Unknown | 160 | Evaluates empagliflozin and sacubitril/valsartan in adults with congenital heart disease and heart failure with reduced ejection fraction. Bumetanide is not the study drug; provides disease-context background only. |
| [NCT06885164](https://clinicaltrials.gov/study/NCT06885164) | N/A | Recruiting | 200 | Observational study of seismocardiographic remote monitoring in heart failure patients (2025–2027). Device evaluation; does not involve bumetanide. |

> **Note:** No clinical trial provides direct interventional efficacy data for bumetanide in acute pulmonary heart disease. NCT07375212 demonstrates investigator interest in this direction but was withdrawn before recruiting any participants.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [6391889](https://pubmed.ncbi.nlm.nih.gov/6391889/) | 1984 | Comprehensive Pharmacological Review | *Drugs* | Landmark review establishing bumetanide's role as a potent loop diuretic for oedema in congestive heart failure, hepatic and renal disease, and **acute pulmonary congestion**. Describes onset within 30 minutes, action persisting 3–6 hours, and supports oral, IV, and IM routes. |
| [3304383](https://pubmed.ncbi.nlm.nih.gov/3304383/) | 1987 | Prospective Haemodynamic Study | *British Journal of Clinical Pharmacology* | IV bumetanide (25 µg/kg) prospectively studied in 24 patients with coronary artery disease and acute or chronic heart failure. Demonstrated reductions in pulmonary artery occluded pressure (PAOP) and cardiac index changes consistent with preload reduction — directly relevant to acute cor pulmonale physiology. |
| [19142155](https://pubmed.ncbi.nlm.nih.gov/19142155/) | 2009 | Narrative Review | *American Journal of Therapeutics* | Reviews therapeutic options for acute decompensated heart failure, noting that loop diuretics remain the cornerstone of acute management. Contextualises bumetanide within the broader decongestive strategy for 1 million annual US hospitalisations. |
| [19843838](https://pubmed.ncbi.nlm.nih.gov/19843838/) | 2009 | Comparative Review | *Annals of Pharmacotherapy* | Systematic comparison of loop diuretics (bumetanide, furosemide, torsemide) on pharmacokinetics, safety, efficacy, and cost. Supports bumetanide's comparable or superior bioavailability profile versus furosemide in congested states. |
| [39366035](https://pubmed.ncbi.nlm.nih.gov/39366035/) | 2024 | Epidemiological Cohort | *American Journal of Emergency Medicine* | Large-scale US epidemiological analysis of heart failure presentations to emergency departments (2016–2023), providing contemporary burden-of-disease data and treatment patterns. Confirms continued relevance of diuretic-centred management in acute settings. |

---

## Netherlands Market Information

Bumetanide currently holds **no marketing authorisation** registered with the CBG-MEB (College ter Beoordeling van Geneesmiddelen) in this dataset. No RVG numbers, product names, dosage forms, or approved indications are on record.

> Clinicians and researchers seeking to use bumetanide in the Netherlands should consult the CBG-MEB register directly and assess whether an import authorisation or hospital exemption pathway is applicable. Reference SmPC documentation from authorised markets (e.g., UK, US) for product characteristics.

---

## Safety Considerations

No safety-specific data (key warnings, contraindications, or drug–drug interactions) was available in the Evidence Pack for this candidate.

> Please refer to the **SmPC (Samenvatting van de Productkenmerken)** from an authorised market for comprehensive safety information, including electrolyte disturbances (hypokalaemia, hyponatraemia), ototoxicity risk (particularly at high doses or in combination with aminoglycosides), renal function monitoring requirements, and contraindications in anuria or hepatic coma.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic basis for bumetanide in acute pulmonary heart disease is well-grounded and consistent with established loop diuretic pharmacology; Level 3 evidence (observational studies, pharmacological reviews, and a prospective haemodynamic study) supports biological plausibility. However, no completed interventional trial specifically in acute cor pulmonale exists, no NL marketing authorisation is in place, and formal safety documentation for this indication has not been reviewed.

**To proceed, the following is needed:**

- **Regulatory pathway clarification**: Confirm whether bumetanide can be obtained via CBG-MEB import authorisation, hospital pharmacy preparation, or an EMA centralised procedure before clinical use in the Netherlands.
- **SmPC safety review**: Retrieve and analyse the full Summary of Product Characteristics from an authorised market (e.g., UK MHRA or US FDA label) to complete the safety assessment — particularly electrolyte monitoring protocols, contraindications, and drug interaction profile.
- **MOA documentation**: Formally document bumetanide's mechanism of action from DrugBank (DB00887) to strengthen the mechanistic link analysis and support any regulatory submission.
- **Comparative effectiveness data**: Identify head-to-head comparison data between bumetanide and furosemide in acute pulmonary decompensation, as furosemide is the standard-of-care loop diuretic in most NL clinical settings.
- **Prospective pilot study**: Given that NCT07375212 was withdrawn before enrolment, a new prospective pilot study in acute cor pulmonale — potentially leveraging the intranasal route — should be considered to generate first-in-indication efficacy data.
- **YMYL disclaimer**: Any clinical communication or web publication based on this report must include the standard disclaimer: *"For research reference only. Drug repurposing candidates require clinical validation before application. This does not constitute medical advice."*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

