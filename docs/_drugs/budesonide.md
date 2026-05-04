---
layout: default
title: Budesonide
parent: 僅模型預測 (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
---

# Budesonide
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

# Budesonide: From Asthma and Inflammatory Airway Disease to Atopic Eczema

## One-Sentence Summary

Budesonide is a synthetic corticosteroid with well-established global use in asthma, COPD, and inflammatory gastrointestinal diseases (including Crohn's disease and eosinophilic esophagitis), working through glucocorticoid receptor (GR)-mediated suppression of mucosal inflammation; it is currently **not registered in the Netherlands**.
The TxGNN model predicts it may be effective for **Atopic Eczema**, with **2 clinical trials** and **20 publications** identified as potentially relevant to this direction.
Evidence is currently at **L3** (observational and preclinical level), and a critical safety signal — budesonide's dual role as both a therapeutic agent and a recognized contact allergen in atopic patients — requires careful evaluation before any progression.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in the Netherlands; globally established for asthma and inflammatory airway/gastrointestinal diseases |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| NL Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source dataset. Based on known information, budesonide is a synthetic glucocorticoid belonging to the corticosteroid class. Its efficacy in asthma and inflammatory bowel disease has been clinically proven, and mechanistically it may be applicable to atopic eczema through its potent local anti-inflammatory properties at epithelial and mucosal surfaces.

Atopic eczema and asthma share a common immunological architecture — both are driven by Th2-skewed inflammatory pathways dominated by IL-4, IL-13, and IL-31 signalling, with eosinophil infiltration, mast cell activation, and disruption of epithelial barrier integrity. Budesonide, acting via the glucocorticoid receptor, suppresses these mediators locally at the target tissue level, which provides a coherent mechanistic rationale for therapeutic activity in eczematous skin. This connection is further reinforced by the well-documented clinical concept of the "atopic march," in which asthma and atopic dermatitis co-occur as manifestations of the same underlying Th2 dysregulation.

A 2024 preclinical study (PMID 38275852) specifically investigated budesonide-loaded polymeric nanoparticles formulated into hydrogels for the local therapy of pediatric atopic dermatitis, demonstrating that pH-sensitive delivery systems can improve targeted release at the lesion site while reducing systemic absorption. This confirms active pharmaceutical interest in budesonide as a topical anti-inflammatory agent for atopic skin disease. However, a critical complication must be acknowledged: multiple independent studies consistently identify budesonide as a recognized contact allergen in atopic dermatitis patients, with budesonide included in the European Baseline Series since 2000 precisely as a marker for corticosteroid hypersensitivity. Any therapeutic application in this population must therefore account for the risk of aggravating the condition it is intended to treat.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04680117](https://clinicaltrials.gov/study/NCT04680117) | N/A | Unknown | 150 | Characterises severe paediatric asthma endotypes (ages 0–12) using immune, metabolomic, and microbiota profiling; atopic conditions including eczema define the study population as co-morbidities, not the primary treatment endpoint — budesonide is not the study drug |
| [NCT01028560](https://clinicaltrials.gov/study/NCT01028560) | Phase 1/2 | Completed | 58 | Allergy immunotherapy in atopic wheezing children (18 months–3 years) at high risk for asthma; eczema is used as an eligibility criterion defining atopic risk status, not a treatment outcome — the primary intervention is subcutaneous immunotherapy, not budesonide |

> **Note:** Neither trial is a direct intervention study for budesonide in atopic eczema. Both received a **Grade C** relevance rating. No directly relevant clinical trials were identified.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38275852](https://pubmed.ncbi.nlm.nih.gov/38275852/) | 2024 | Preclinical/Formulation | Gels (Basel) | Eudragit L100 nanoparticles loaded with budesonide in hydrogels demonstrated pH-sensitive drug release at atopic lesion sites, improving topical delivery for paediatric atopic dermatitis while reducing systemic absorption risk |
| [9496795](https://pubmed.ncbi.nlm.nih.gov/9496795/) | 1998 | Clinical Study | Pediatric Dermatology | Open longitudinal knemometry study in 14 children (5–12 years) with atopic dermatitis directly treated with topical budesonide; confirms direct clinical application in AD and identifies short-term growth suppression as a monitoring requirement |
| [8864369](https://pubmed.ncbi.nlm.nih.gov/8864369/) | 1996 | Cohort | Dermatology (Basel) | Evaluated IGF axis, bone and collagen turnover in children with atopic dermatitis treated with topical glucocorticosteroids including budesonide; percutaneous absorption confirmed as clinically significant — systemic monitoring recommended |
| [21062310](https://pubmed.ncbi.nlm.nih.gov/21062310/) | 2010 | RCT (Veterinary) | J Vet Pharmacol Ther | Randomised, blinded, placebo-controlled crossover trial of 0.025% budesonide leave-on conditioner (Barazone) in 29 dogs with atopic dermatitis; significant reductions in skin lesion scores and pruritus; provides proof-of-concept for topical budesonide in AD (non-human) |
| [19875223](https://pubmed.ncbi.nlm.nih.gov/19875223/) | 2010 | RCT Sub-analysis | Allergologia et Immunopathologia | Evaluated differential budesonide response in atopic versus non-atopic infants/preschoolers with recurrent wheezing; relevant to understanding immunological context of budesonide response in atopic populations |
| [35133669](https://pubmed.ncbi.nlm.nih.gov/35133669/) | 2022 | Cross-sectional | Contact Dermatitis | Asian dermatology centre study on contact sensitization patterns in AD patients; highlights budesonide as a relevant patch-test allergen in this population — a key safety signal for topical use |
| [24603519](https://pubmed.ncbi.nlm.nih.gov/24603519/) | 2014 | Cross-sectional | Dermatitis | Corticosteroid series patch testing in adolescents and adults with atopic dermatitis; contact hypersensitivity to budesonide confirmed in the target patient population |
| [33931866](https://pubmed.ncbi.nlm.nih.gov/33931866/) | 2021 | Observational | Contact Dermatitis | Italian SIDAPA baseline series data (2018–2019): budesonide has been the standard European marker for corticosteroid hypersensitivity since 2000; a decreasing trend in sensitization rates was noted over two decades |
| [40020933](https://pubmed.ncbi.nlm.nih.gov/40020933/) | 2025 | Translational | J Allergy Clin Immunol | Shared epithelial barrier dysfunction between eosinophilic esophagitis and atopic dermatitis; dysregulation of cutaneous ceramide synthesis identified as a common pathway — provides mechanistic context for corticosteroid intervention across epithelial barrier diseases |
| [30053491](https://pubmed.ncbi.nlm.nih.gov/30053491/) | 2018 | Cross-sectional | J Am Acad Dermatol | Allergic contact dermatitis to topical medications in adults with atopic dermatitis; skin barrier disruption and immune dysregulation in AD increase sensitization risk to topical corticosteroids including budesonide |

---

## Netherlands Market Information

Budesonide is **not currently registered** in the Netherlands. No RVG (Registratienummer voor Geneesmiddelen) authorizations have been issued by the CBG-MEB (College ter Beoordeling van Geneesmiddelen) for any budesonide-containing product.

> In other EU member states and centrally via EMA, budesonide is available in multiple authorised formulations for asthma (inhaled suspension/powder), Crohn's disease and microscopic colitis (oral enteric-coated capsules), and allergic rhinitis (nasal spray). Prescribers in the Netherlands may refer to EMA-authorised SmPCs for reference products such as **Pulmicort**, **Entocort**, and **Rhinocort** for mechanism, dosing, and safety information relevant to potential off-label consideration.

---

## Safety Considerations

> No structured safety data (key warnings, contraindications, or drug interactions) was available in the source dataset. Please refer to the SmPC (Summary of Product Characteristics / Samenvatting van de Productkenmerken) of the relevant authorised formulation for complete safety information.

**Clinically Important Signal Identified from Literature:**

Multiple independent publications in the evidence base consistently identify budesonide as a **recognized contact allergen** in patients with atopic dermatitis. Budesonide has been included in the **European Baseline Patch Test Series since 2000** as the primary marker for corticosteroid hypersensitivity (PMID 33931866). Rates of positive patch-test reactions to budesonide are elevated in the atopic dermatitis population due to compromised skin barrier function and repeated topical medication exposure (PMIDs 35133669, 24603519, 30053491). Any clinical use of topical budesonide in atopic patients should include baseline patch testing to exclude corticosteroid hypersensitivity before initiating treatment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While budesonide has a mechanistically plausible basis for activity in atopic eczema — particularly through GR-mediated suppression of Th2-driven skin inflammation — the current evidence is limited to preclinical formulation work, veterinary RCTs, and observational studies in humans (L3), with no directly relevant completed Phase 2/3 clinical trials in human atopic eczema patients identified. Compounding this, budesonide is not registered in the Netherlands for any indication, and its established role as a contact sensitizer in the very patient population it would be intended to treat represents a safety concern requiring formal characterisation before progression.

**To proceed, the following is needed:**

- **Clinical evidence gap**: Commission or identify Phase 2 human trials specifically evaluating topical budesonide (including novel nanoparticle/hydrogel formulations) in atopic eczema with validated endpoints (EASI, SCORAD, IGA)
- **Safety characterisation**: Conduct a systematic review of budesonide contact sensitization rates in atopic dermatitis patients; develop a patch-test screening protocol as a prerequisite for therapeutic use in this population
- **Mechanism of action documentation**: Retrieve complete DrugBank MOA data and confirm GR-mediated activity at cutaneous Th2 inflammatory targets (IL-4, IL-13, IL-31, TSLP)
- **Regulatory pathway assessment**: As budesonide has no NL registration, a new marketing authorisation application or Article 3(2) exemption assessment via CBG-MEB would be required; EMA-level scientific advice may be warranted given the cross-EU regulatory context
- **Paediatric safety plan**: Given that the most biologically plausible patient population includes children (paediatric atopic dermatitis), a dedicated paediatric safety monitoring plan addressing HPA axis suppression and growth effects from topical absorption is required in accordance with the EU Paediatric Regulation (PIP requirements)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

