---
layout: default
title: Brinzolamide
parent: 僅模型預測 (L5)
nav_order: 32
evidence_level: L5
indication_count: 1
---

# Brinzolamide
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

# Brinzolamide: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Brinzolamide is a topical carbonic anhydrase II (CA-II) inhibitor primarily indicated for reducing elevated intraocular pressure (IOP) in open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma** (including congenital and juvenile-onset open-angle glaucoma),
with **no registered clinical trials** and **no indexed publications** specifically supporting this combination — placing current evidence at **Level L4**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma / Ocular hypertension (known therapeutic class use; no NL license on file) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L4 (Mechanistic / model prediction only) |
| NL Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Brinzolamide is a selective carbonic anhydrase II (CA-II) inhibitor that acts on ciliary body epithelial cells to suppress aqueous humor production, thereby lowering intraocular pressure (IOP). Detailed MOA data from DrugBank was not retrieved in this evidence pack, but the mechanism is well established in the literature: inhibition of CA-II reduces bicarbonate secretion into the posterior chamber, decreasing fluid inflow and IOP.

Primary Hereditary Glaucoma (PHG) — encompassing Primary Congenital Glaucoma (PCG, CYP1B1 mutation) and Juvenile Open-Angle Glaucoma (JOAG, MYOC mutation) — shares the same core pathophysiology as other glaucoma subtypes: impaired aqueous humor outflow due to anterior chamber angle maldevelopment, leading to chronically elevated IOP and progressive optic nerve damage. Because elevated IOP is the central pathological driver across all glaucoma phenotypes, a CA-II inhibitor that reduces aqueous humor inflow targets this common final pathway directly, making the TxGNN prediction mechanistically coherent.

However, an important clinical nuance limits the translational value here. In PCG specifically, surgical intervention (goniotomy or trabeculotomy) remains first-line treatment; pharmacological IOP reduction — including topical CA-II inhibitors — is generally used only as a bridge prior to surgery or as adjunctive therapy post-operatively. Additionally, the paediatric pharmacokinetic profile of brinzolamide differs from adults, and systemic CA-II inhibition (which can occur with ophthalmic formulations in neonates and infants) carries risks of metabolic acidosis, a safety consideration that requires specific paediatric evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for Brinzolamide in primary hereditary glaucoma (search conducted 2026-03-10 via ClinicalTrials.gov and ICTRP).

---

## Literature Evidence

Currently no related literature available specifically for Brinzolamide in primary hereditary glaucoma (PubMed search conducted 2026-03-10).

---

## Netherlands Market Information

Brinzolamide currently holds **no marketing authorisation** through CBG-MEB or EMA in the Netherlands. No RVG numbers are on file for this active substance.

> Note: Brinzolamide-containing products (e.g., Azopt® 10 mg/mL eye drops) are authorised in several EU member states via national or mutual recognition procedures. If an EU-wide SmPC exists, it would be accessible via the EMA product database for reference purposes.

---

## Safety Considerations

Detailed warning and contraindication data for this candidate was not retrieved in this evidence pack. No drug-drug interaction records were returned from the DDI database query.

> Please refer to the SmPC (Summary of Product Characteristics) for complete safety information, including warnings regarding sulfonamide hypersensitivity, corneal endothelial effects, and systemic CA-II inhibition in paediatric and renally impaired patients.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis for using brinzolamide in primary hereditary glaucoma is sound — IOP reduction is the common therapeutic target across all glaucoma subtypes — but no clinical trial or published clinical evidence specifically evaluating this indication was found. With an evidence level of L4 and no NL marketing authorisation, this candidate requires foundational evidence generation before a regulatory or formulary pathway can be considered.

**To proceed, the following is needed:**

- **Confirm EMA/CBG-MEB status**: Verify whether any centralised or mutual-recognition authorisation exists for brinzolamide in the EU; retrieve the current SmPC for safety and posology reference.
- **Paediatric literature review**: Conduct a broader PubMed search covering brinzolamide use in congenital and juvenile glaucoma (not limited to the exact MeSH term "primary hereditary glaucoma") to capture relevant observational data.
- **Safety data gap closure**: Retrieve full contraindication, warning, and paediatric safety data from DrugBank and available SmPCs; specifically assess systemic CA-II inhibition risk in infants and neonates.
- **Clinical practice mapping**: Determine current NL/EU clinical guidelines (e.g., EGS Guidelines on Congenital Glaucoma) to understand whether pharmacological IOP lowering has any recognised role alongside surgery.
- **Feasibility of investigator-initiated study**: If existing evidence supports a role for adjunctive brinzolamide in PHG, assess feasibility of a prospective observational study or small RCT in a paediatric ophthalmology centre.

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. Data cutoff: 2026-04-03.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

