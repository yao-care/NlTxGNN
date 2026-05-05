---
layout: default
title: Hyaluronidase
parent: 僅模型預測 (L5)
nav_order: 76
evidence_level: L5
indication_count: 10
---

# Hyaluronidase
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

---

# Hyaluronidase: From Spreading Adjuvant to Diabetic Retinopathy

## One-Sentence Summary

Hyaluronidase is an enzyme that degrades hyaluronic acid in the extracellular matrix, clinically used as a spreading adjuvant for local anaesthetics and as a reversal agent for hyaluronic acid-based dermal fillers.
The TxGNN model identifies **diabetic retinopathy** as the highest-evidence repurposing candidate, backed by **4 clinical trials** — including 2 completed Phase 3 RCTs enrolling a combined 1,260 patients — and **20 publications** supporting its use for vitreous haemorrhage clearance via pharmacological vitreolysis.
An ophthalmic formulation (Vitrase, ovine hyaluronidase) has already completed pivotal trials in the United States, though the drug remains **unregistered in the Netherlands**.

> **Note on primary indication selection**: The highest TxGNN score belongs to esotropia (99.89%, rank #331 among all disease nodes), but expert review identifies this as a likely false positive — the sole supporting publication (PMID 16934027) describes hyaluronidase as an anaesthetic adjuvant implicated in post-operative strabismus as a complication, not as a treatment. Diabetic retinopathy (TxGNN score 99.71%, rank #708) is selected as the primary focus of this report on the basis of its **L1 evidence profile** and highest actionability.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Adjuvant to increase absorption and dispersion of injected drugs or subcutaneous fluids (spreading agent) |
| Predicted New Indication | Diabetic Retinopathy — vitreous haemorrhage clearance via intravitreal pharmacological vitreolysis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L1 |
| NL Market Status | Not registered (geen RVG-registratie) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Hyaluronidase is an enzyme that cleaves the glycosidic bonds of hyaluronic acid (HA) — a high-molecular-weight glycosaminoglycan that forms the structural backbone of the vitreous gel. When injected intravitreally, hyaluronidase promotes **pharmacological vitreolysis**: enzymatic liquefaction of the vitreous, followed by complete posterior vitreous detachment (PVD) — separation of the vitreous cortex from the inner surface of the retina. This is the core mechanism underlying the Vitrase programme.

In diabetic retinopathy (DR), the vitreo-retinal interface is a central site of pathology. Proliferative DR drives formation of fragile neovascular membranes at the vitreo-retinal junction; rupture of these vessels produces vitreous haemorrhage (VH), causing sudden and often severe visual loss. A 2026 mechanistic study (PMID 41789111) confirmed that the HA pathway is directly dysregulated in the proliferative DR microenvironment — with altered expression of HA synthase-2, Hyal-1, Hyal-2, CD44, and RHAMM driving local inflammation and pathological angiogenesis. This provides molecular-level evidence that hyaluronidase is not merely an empirical choice, but targets a documented pathological substrate.

The current standard of care for VH is pars plana vitrectomy — an invasive surgical procedure associated with risks of endophthalmitis, cataract formation, and retinal detachment. Intravitreal ovine hyaluronidase (Vitrase; ISTA Pharmaceuticals) was developed as a pharmacological alternative, completing two large Phase 3 RCTs in the United States with a combined enrolment of 1,260 patients. It is important to define the indication precisely: the Phase 3 trials targeted **vitreous haemorrhage secondary to diabetic retinopathy**, not direct reversal of retinopathy progression itself. Any CBG-MEB dossier should reflect this distinction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00198510](https://clinicaltrials.gov/study/NCT00198510) | Phase 3 | Completed | 750 | Pivotal RCT — intravitreal Vitrase (ovine hyaluronidase) for clearance of severe vitreous haemorrhage; registration-quality evidence for the DR–VH indication |
| [NCT00198497](https://clinicaltrials.gov/study/NCT00198497) | Phase 3 | Completed | 510 | Confirmatory Phase 3 RCT — same indication; completed June 2003; together with NCT00198510 forms the L1 evidence core |
| [NCT00198471](https://clinicaltrials.gov/study/NCT00198471) | Phase 2 | Completed | 10 | Open-label pilot — intravitreous Vitrase for inducing PVD in moderate-to-severe non-proliferative DR; small sample limits conclusions but establishes feasibility |
| [NCT04311606](https://clinicaltrials.gov/study/NCT04311606) | Phase 2 | Completed | 11 | Sub-tenon aflibercept ± hyaluronidase in acute Thyroid Eye Disease (AcTED Study) — retrieved due to ophthalmology indexing overlap; **not counted as DR-specific evidence** |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41789111](https://pubmed.ncbi.nlm.nih.gov/41789111/) | 2026 | Basic Science | Frontiers in Immunology | HA pathway enzymes (Hyal-1, Hyal-2) and receptors (CD44, RHAMM) are directly dysregulated in the vitreous of proliferative DR patients — molecular confirmation of HA as a therapeutic target |
| [20939804](https://pubmed.ncbi.nlm.nih.gov/20939804/) | 2011 | Review | Curr Pharmaceutical Biotechnology | Pharmacological vitreolysis review: intravitreal ovine hyaluronidase shown effective for VH clearance; PVD induction summarised as emerging DR management strategy |
| [23847321](https://pubmed.ncbi.nlm.nih.gov/23847321/) | 2013 | Basic Science | Invest Ophthalmol Vis Sci | Enzyme-induced complete PVD alleviates DR progression via HIF-1α pathway suppression — mechanistic basis for neuroprotective effect of vitreolysis |
| [19199900](https://pubmed.ncbi.nlm.nih.gov/19199900/) | 2009 | Review | Current Diabetes Reviews | Enzymatic vitreolysis review: vitreo-retinal interface role in proliferative DR and macular oedema; hyaluronidase pharmacology detailed alongside other vitreolytic agents |
| [19050667](https://pubmed.ncbi.nlm.nih.gov/19050667/) | 2009 | Animal Study | Retina | Plasmin + hyaluronidase combination induces PVD in diabetic rats — in vivo preclinical confirmation of vitreolytic efficacy |
| [17245084](https://pubmed.ncbi.nlm.nih.gov/17245084/) | 2007 | Review | Developments in Ophthalmology | Pharmacological vitreolysis overview — incomplete PVD and attached vitreous cortex directly linked to DR and maculopathy progression; rationale for PVD induction articulated |
| [19644368](https://pubmed.ncbi.nlm.nih.gov/19644368/) | 2009 | Review | Current Opinion in Ophthalmology | Changing paradigms in DR treatment: pharmacological vitreolysis positioned within evolving treatment landscape including anti-VEGF and surgical options |
| [12757408](https://pubmed.ncbi.nlm.nih.gov/12757408/) | 2003 | Drug Profile | Drugs in R&D | Vitrase (ovine hyaluronidase) product profile — mechanism, clinical development history, and positioning for vitreous haemorrhage and diabetic retinopathy |
| [30445048](https://pubmed.ncbi.nlm.nih.gov/30445048/) | 2019 | Animal Study | Experimental Eye Research | Diabetes and exogenous hyaluronidase jointly alter retinal endothelial glycocalyx thickness in Akita mice — translational mechanistic evidence for retinal HA dynamics |
| [17713597](https://pubmed.ncbi.nlm.nih.gov/17713597/) | 2007 | Review | Experimental Diabetes Research | DR pharmacotherapy landscape: intravitreal agents including hyaluronidase discussed in context of completed and ongoing trials; clinical context established |

---

## Netherlands Market Information

Hyaluronidase currently holds **no marketing authorisations** with the CBG-MEB. There are no RVG numbers on record and no registered products in the Netherlands.

Clinicians or sponsors seeking to use hyaluronidase in the Dutch healthcare system would need to explore one of the following regulatory pathways:

- **Named-patient basis** (Article 3.17, Geneesmiddelenwet): for individual patients under specialist supervision, with documented medical need
- **Compassionate use programme**: via formal application to CBG-MEB, supported by clinical evidence
- **Full marketing authorisation**: via the centralised EMA procedure (recommended given the pan-European DR patient population) or the national CBG-MEB procedure

> Vitrase (ovine hyaluronidase) received FDA approval in the United States for ophthalmic use. Its European regulatory status should be independently verified with the EMA and CBG-MEB before any clinical use in the Netherlands.

---

## Safety Considerations

All safety fields in the Evidence Pack are marked as unavailable (no NL SmPC on record). The following information is supplemented from the clinical trial and literature evidence retrieved:

**Allergic reactions**: Hyaluronidase allergy has been documented since 1984 and is frequently misdiagnosed (PMID 37145319, 2024 safety review in *Aesthetic Plastic Surgery*). Risk factors include prior exposure and bee/wasp venom sensitivity. Skin sensitivity testing prior to intravitreal or intradermal administration is advisable, particularly for ovine-derived preparations (Vitrase).

**Immunogenicity of ovine formulation**: Ovine (sheep-derived) hyaluronidase may carry higher allergenic potential than recombinant human hyaluronidase (rHuPH20; Hylenex). Product selection should account for this when preparing a Dutch-market risk management plan.

**Intravitreal injection risks**: Standard risks of intraocular administration apply — endophthalmitis, rhegmatogenous retinal detachment, acute intraocular pressure elevation, and traumatic lens injury. These must be addressed in any Dutch-specific risk minimisation programme.

**Spreading effect on co-administered agents**: When used as an adjuvant, hyaluronidase enhances tissue absorption of co-administered drugs. Dose adjustments for local anaesthetics may be required. No formal drug interaction data was identified in the queried database.

Please refer to the Vitrase US label and any available rHuPH20 SmPC for comprehensive safety information. An EU-compliant SmPC (Samenvatting van de Productkenmerken) and PIL (Bijsluiter) will be required prior to any CBG-MEB registration application.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 RCTs (combined n=1,260) provide robust L1 evidence for intravitreal hyaluronidase in clearing vitreous haemorrhage secondary to diabetic retinopathy, supported by a well-established pharmacological mechanism (HA degradation → vitreous liquefaction → PVD induction) and a 2026 molecular study directly implicating the HA pathway in DR pathogenesis. The drug is not currently registered in the Netherlands, and EU regulatory groundwork has not been laid — these are the primary barriers, not the clinical evidence.

**To proceed, the following is needed:**

- **Regulatory pathway analysis**: Determine whether a centralised EMA procedure or national CBG-MEB procedure is appropriate; check EMA EPAR database for any existing or lapsed EU applications for Vitrase or rHuPH20
- **Clinical study report review**: Obtain full CSRs for NCT00198510 and NCT00198497 to evaluate primary endpoint data (VH clearance rates, best-corrected visual acuity at 3 and 6 months) and complete safety profiles
- **Indication scoping**: Define the NL label indication precisely as *"vitreous haemorrhage secondary to diabetic retinopathy"*, not broad DR — this aligns with Phase 3 evidence and mitigates off-label extension risk
- **Formulation decision**: Evaluate ovine (Vitrase) versus recombinant human (rHuPH20) hyaluronidase based on immunogenicity, manufacturing availability, and regulatory preference in the EU context
- **SmPC and PIL preparation**: Commission EU-compliant SmPC and Dutch-language Bijsluiter for CBG-MEB submission
- **Pharmacovigilance plan**: Develop a Risk Management Plan (RMP) per EMA/GVP Module V, addressing allergic reactions, intravitreal injection risks, and immunogenicity monitoring
- **Reimbursement assessment**: Engage Zorginstituut Nederland (ZIN) early on cost-effectiveness versus current standard of care (pars plana vitrectomy), given the minimally invasive nature of intravitreal injection as a potential advantage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

