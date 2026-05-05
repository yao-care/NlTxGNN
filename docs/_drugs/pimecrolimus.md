---
layout: default
title: Pimecrolimus
parent: 僅模型預測 (L5)
nav_order: 104
evidence_level: L5
indication_count: 4
---

# Pimecrolimus
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Using the `txgnn-pipeline` skill to guide report generation for NL deployment context.

---

# Pimecrolimus: From Atopic Dermatitis to Seborrheic Dermatitis

## One-Sentence Summary

Pimecrolimus (brand name: Elidel) is a topical calcineurin inhibitor originally developed for the treatment of atopic dermatitis (eczema), suppressing local skin inflammation by blocking T-cell activation without the skin-thinning side effects of corticosteroids.
The TxGNN model predicts it may be effective for **Seborrheic Dermatitis**,
with **1 clinical trial** and **18 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Atopic dermatitis (mild to moderate; contextual – no CBG-MEB registration found) |
| Predicted New Indication | Seborrheic Dermatitis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 (1 completed Phase 2 RCT) |
| NL Market Status | Not marketed (no CBG-MEB national authorizations on file) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on market status:** Pimecrolimus (Elidel) holds a centrally authorized EMA marketing authorization (valid across all EU/EEA member states including the Netherlands) for atopic dermatitis. The CBG-MEB dataset shows 0 national authorizations, which likely reflects the absence of a *national* procedure — this should be cross-checked against the EMA product database before any regulatory submission.

---

## Why is This Prediction Reasonable?

Pimecrolimus is a member of the calcineurin inhibitor (TCI) drug class. It acts by binding to macrophilin-12 (FKBP-12) and inhibiting calcineurin, thereby preventing the dephosphorylation of NFAT (Nuclear Factor of Activated T-cells). This blocks the transcription of pro-inflammatory cytokines — including IL-2, IL-4, IFN-γ, and TNF-α — selectively in T cells and mast cells. Critically, it does not cause dermal atrophy, which makes it particularly suitable for long-term use on sensitive facial skin areas.

Seborrheic dermatitis involves a Th1/Th17 immune imbalance triggered by skin commensal yeasts of the *Malassezia* genus, leading to disruption of the epidermal barrier and local inflammatory cytokine release. This immune-driven inflammatory component is mechanistically aligned with pimecrolimus's mode of action: by suppressing the local cytokine cascade, pimecrolimus can reduce the erythema, scaling, and pruritus that characterise the condition. The steroid-free profile is an additional clinical advantage, since seborrheic dermatitis frequently affects the face and scalp — areas where corticosteroid-related adverse effects (telangiectasia, rosacea-like eruptions, skin atrophy) are a genuine concern.

Both atopic dermatitis and seborrheic dermatitis are chronic, relapsing inflammatory skin conditions in which immune-mediated skin barrier dysfunction plays a central role. While *Malassezia* colonisation adds a fungal dimension to seborrheic dermatitis that does not exist in atopic dermatitis, the inflammatory pathway targeted by pimecrolimus is shared. Multiple independent systematic reviews have concluded that pimecrolimus 1% cream provides comparable efficacy to antifungals and mild corticosteroids in seborrheic dermatitis, with a favourable tolerability profile for repeated use — lending strong biological and clinical plausibility to this TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT00403559](https://clinicaltrials.gov/study/NCT00403559) | Phase 2 | Completed | 113 | 4-week randomised, double-blind, active-comparator controlled exploratory study comparing Elidel (pimecrolimus 1% cream) against an active comparator for seborrheic dermatitis. This is the only completed Phase 2 RCT directly evaluating pimecrolimus in this indication. Results informed subsequent evidence synthesis. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|---|---|---|---|---|
| [36072203](https://pubmed.ncbi.nlm.nih.gov/36072203/) | 2022 | Systematic Review | Cureus | Critical review of RCTs evaluating pimecrolimus efficacy and safety in *facial* seborrheic dermatitis; concludes pimecrolimus is a viable topical alternative to corticosteroids and antifungals in this indication. |
| [22142161](https://pubmed.ncbi.nlm.nih.gov/22142161/) | 2012 | Systematic Review of RCTs | Expert Review of Clinical Pharmacology | Pimecrolimus 1% cream shows comparable efficacy to corticosteroids and antimycotics in seborrheic dermatitis with good tolerability; positioned as a well-tolerated alternative for long-term management. |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic Review | American Journal of Clinical Dermatology | Comprehensive review of topical treatments for facial seborrheic dermatitis; pimecrolimus included in the evidence base alongside antifungals and corticosteroids. |
| [34910320](https://pubmed.ncbi.nlm.nih.gov/34910320/) | 2022 | RCT | Clinical and Experimental Dermatology | Randomised blinded trial comparing pimecrolimus 1% cream vs. sertaconazole 2% cream in facial seborrheic dermatitis; evaluates long-term treatment in a chronic relapsing condition. |
| [23715821](https://pubmed.ncbi.nlm.nih.gov/23715821/) | 2013 | RCT | Irish Journal of Medical Science | Head-to-head comparison of sertaconazole 2% vs. pimecrolimus 1% cream in seborrheic dermatitis; contributes comparative efficacy data. |
| [18677657](https://pubmed.ncbi.nlm.nih.gov/18677657/) | 2009 | Randomised Open-label Study | Journal of Dermatological Treatment | Open randomised prospective comparison of pimecrolimus 1% cream vs. ketoconazole 2% cream in seborrheic dermatitis. |
| [20000875](https://pubmed.ncbi.nlm.nih.gov/20000875/) | 2010 | Open-label Study | American Journal of Clinical Dermatology | Open-label study of pimecrolimus 1% cream in corticosteroid-resistant facial seborrheic dermatitis; confirms efficacy and good tolerability in a difficult-to-treat subgroup. |
| [23441238](https://pubmed.ncbi.nlm.nih.gov/23441238/) | 2013 | Clinical Study | Journal of Clinical and Aesthetic Dermatology | Reviews clinical evidence supporting topical pimecrolimus as a safe, steroid-free alternative for seborrheic dermatitis, particularly for long-term facial use. |
| [16033622](https://pubmed.ncbi.nlm.nih.gov/16033622/) | 2005 | Narrative Review | International Journal of Clinical Practice | Seminal mechanistic review describing pimecrolimus's selective inhibition of T-cell and mast cell cytokine release (IL-2, IL-4, IFN-γ, TNF-α); discusses applications beyond atopic dermatitis, including seborrheic dermatitis. |
| [15700745](https://pubmed.ncbi.nlm.nih.gov/15700745/) | 2004 | Clinical Study | Drugs Under Experimental and Clinical Research | Early prospective assessment of pimecrolimus 1% cream in seborrheic dermatitis of the face and upper trunk; reports efficacy, tolerability and safety across a clinic-based patient cohort. |

---

## Netherlands Market Information

Pimecrolimus currently holds **no national marketing authorization** through CBG-MEB. However, Elidel (pimecrolimus 1% cream) is a **centrally authorized EMA product** (approved for mild to moderate atopic dermatitis) and is therefore legally marketable in the Netherlands without a separate CBG-MEB national procedure. Verification against the EMA product database is recommended before proceeding with any off-label use assessment.

| RVG Number | Product Name | Dosage Form | Approved Indication |
|---|---|---|---|
| — | No CBG-MEB national authorization registered | — | — |

> Clinicians and pharmacists should consult the **EMA-approved SmPC for Elidel** (available via the EMA website) as the reference document for authorized indications, contraindications, and special warnings applicable in the Netherlands.

---

## Safety Considerations

Detailed safety data (warnings, contraindications, drug interactions) are not available in this Evidence Pack for the Netherlands context.

> Please refer to the **SmPC (Samenvatting van de Productkenmerken)** for Elidel, available via the EMA and/or CBG-MEB databases, for complete safety information prior to any clinical use or off-label application.

A specific safety note from the literature is worth flagging: there is an unresolved long-term question regarding **malignancy risk** with topical calcineurin inhibitors. A 2023 systematic review and meta-analysis (PMID 36370744, *The Lancet Child & Adolescent Health*) assessed cancer risk in atopic dermatitis patients treated with pimecrolimus and tacrolimus. Regulatory authorities in the EU have maintained a warning regarding this theoretical risk, particularly in paediatric patients. This should be explicitly addressed in any off-label use protocol for seborrheic dermatitis.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN model prediction is strongly supported by mechanistic plausibility (calcineurin inhibition directly targets the T-cell-driven inflammatory cascade relevant to seborrheic dermatitis), and by a meaningful body of clinical evidence — including one completed Phase 2 RCT, two head-to-head RCTs against sertaconazole, at least two systematic reviews, and multiple prospective open-label studies — all demonstrating that pimecrolimus 1% cream is effective and well-tolerated in seborrheic dermatitis. The absence of a large Phase 3 confirmatory trial prevents escalation to L1, and the lack of CBG-MEB registration requires regulatory clarification before formalising use in the Netherlands.

**To proceed, the following is needed:**

1. **Regulatory verification**: Confirm EMA central authorization status for Elidel and its applicability in the Netherlands for off-label use in seborrheic dermatitis; determine whether a label extension or formal off-label prescribing protocol (magistrale bereiding/off-label policy) is required by the CBG-MEB.
2. **SmPC review**: Retrieve the current Elidel SmPC to complete the safety assessment — specifically key warnings, contraindications, and any age-related restrictions relevant to seborrheic dermatitis patient populations.
3. **Malignancy risk protocol**: Establish a monitoring framework addressing the long-term theoretical malignancy risk identified by EMA, particularly for paediatric or long-term use scenarios.
4. **MOA documentation**: Retrieve full pharmacological profile from DrugBank (DB00337) to formally document the mechanism of action for the clinical dossier.
5. **Phase 3 gap assessment**: Evaluate whether the existing Phase 2 and comparative RCT evidence is sufficient for the intended use context, or whether a Phase 3 confirmatory trial would be required by Dutch/EMA standards for any formal indication extension.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

