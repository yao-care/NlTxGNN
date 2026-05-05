---
layout: default
title: Lynestrenol
parent: 僅模型預測 (L5)
nav_order: 90
evidence_level: L5
indication_count: 5
---

# Lynestrenol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Using the `txgnn-pipeline` skill — this is a NL-country drug repurposing report. No additional overrides from the skill. Proceeding to generate the report per the system prompt (v5).

---

# Lynestrenol: From Gynecological Conditions to Migraine with or without Aura

## One-Sentence Summary

Lynestrenol (marketed as Orgametril) is a synthetic progestogen historically used for gynecological conditions including endometriosis, dysfunctional uterine bleeding, and premenstrual disorders.
The TxGNN model predicts it may have utility in **Migraine with or without Aura (susceptibility)**, with **0 clinical trials** and **20 publications** available — though most literature addresses epilepsy-migraine genetic comorbidity mechanisms rather than Lynestrenol's direct therapeutic role, and the drug currently holds no marketing authorisation in the Netherlands.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gynecological conditions (progestogen class; no NL marketing authorisation on record) |
| Predicted New Indication | Migraine with or without Aura, susceptibility to |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L4 |
| NL Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on established pharmacology, Lynestrenol is a synthetic progestogen structurally related to 19-nortestosterone. It is converted in vivo to norethisterone and subsequently to neuroactive metabolites — most notably allopregnanolone-like steroids — which act as positive allosteric modulators of GABA-A receptors. This raises the neuronal excitability threshold, a mechanism directly relevant to both migraine and epilepsy pathophysiology. In fact, this class of neuroactive steroids forms the basis for brexanolone, a clinically approved GABA-A modulator used in postpartum depression.

Oestrogen withdrawal is a well-established migraine trigger, particularly in the menstrual window. By maintaining stable progestogenic tone, Lynestrenol may attenuate hormonal fluctuation and thereby reduce migraine frequency — especially in women with menstrually-associated migraine. A 1963 clinical observation by Lundberg (PMID 14091721) reported direct use of Lynestrenol (Orgametril) for migraine prophylaxis, providing the earliest direct clinical signal for this hypothesis. A 2026 comparative review (PMID 41723577) further contextualises progestogens within combined oral contraceptive use for migraine management, noting the nuanced benefit-risk balance by migraine subtype.

The TxGNN rank-1 prediction specifically targets the genetically-defined subtype "migraine with or without aura, susceptibility to," which shares genetic pathways with epilepsy (SCN1A, MTHFR variants, GABA-A receptor dysregulation). While the GABA-A modulatory mechanism of Lynestrenol's metabolites is plausible in this genetic context, the available literature for this specific subtype predominantly characterises epilepsy genetics rather than Lynestrenol's pharmacological activity. A direct mechanistic bridge to this genetic susceptibility variant remains to be demonstrated experimentally.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Lynestrenol in migraine with or without aura.

---

## Literature Evidence

The following publications are drawn from the rank-1 indication evidence set. Papers are ranked by relevance to the migraine-Lynestrenol mechanistic connection; note that several address epilepsy-migraine comorbidity at the genetic level rather than Lynestrenol directly.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33856647](https://pubmed.ncbi.nlm.nih.gov/33856647/) | 2021 | Review | Molecular Neurobiology | Epilepsy and migraine share genetic susceptibility (SCN1A, MTHFR), neuroinflammatory pathways, and ion channel dysfunction; therapeutic strategies applicable to both conditions discussed |
| [23294289](https://pubmed.ncbi.nlm.nih.gov/23294289/) | 2013 | Genetic Cohort Study | Epilepsia | Shared genetic susceptibility between migraine and epilepsy demonstrated in the Epilepsy Phenome/Genome Project (EPGP) cohort |
| [17460155](https://pubmed.ncbi.nlm.nih.gov/17460155/) | 2007 | Genetic Linkage Study | Neurology | Large Belgian family with familial occipitotemporal lobe epilepsy co-segregating with migraine with visual aura; disease locus mapped to chromosome 9q |
| [30267335](https://pubmed.ncbi.nlm.nih.gov/30267335/) | 2018 | Meta-analysis | Neurological Sciences | MTHFR C677T polymorphism significantly associated with epilepsy susceptibility; supports the migraine-epilepsy genetic overlap model |
| [34575901](https://pubmed.ncbi.nlm.nih.gov/34575901/) | 2021 | Review | Int J Molecular Sciences | GABA-A receptor modulation identified as a key molecular target for antiepileptogenesis; directly relevant to the proposed mechanism of Lynestrenol's neuroactive metabolites |
| [16201993](https://pubmed.ncbi.nlm.nih.gov/16201993/) | 2005 | Review | Epilepsia | Developmental changes in GABAergic and glutamatergic receptor composition drive heightened neural excitability; GABA-A subunit rearrangements described |
| [34209535](https://pubmed.ncbi.nlm.nih.gov/34209535/) | 2021 | Review | Int J Molecular Sciences | Bidirectional relationship between neuroinflammation and epilepsy; shared inflammatory pathways with migraine aura pathophysiology |
| [24076350](https://pubmed.ncbi.nlm.nih.gov/24076350/) | 2014 | Meta-analysis | Gene | SCN1A IVS5N+5G>A polymorphism associated with susceptibility to epilepsy with febrile seizures; SCN1A also implicated in migraine with aura |
| [22938964](https://pubmed.ncbi.nlm.nih.gov/22938964/) | 2012 | Review | Handbook of Clinical Neurology | Overview of in vitro and in vivo animal models used to study epilepsy pathophysiology and drug mechanisms |
| [28086980](https://pubmed.ncbi.nlm.nih.gov/28086980/) | 2017 | Review | Journal of Neuroinflammation | Post-traumatic epileptogenesis driven by neuroinflammation; inflammatory pathways overlap with cortical spreading depression in migraine aura |

> **Directly relevant evidence from rank-2 (Migraine Disorder) — highest clinical specificity for Lynestrenol:**

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [14091721](https://pubmed.ncbi.nlm.nih.gov/14091721/) | 1963 | Historical Case Series | Svenska Läkartidningen | **Earliest direct clinical report**: prophylactic use of Lynestrenol (Orgametril) for migraine treatment by Lundberg P.O. |
| [41723577](https://pubmed.ncbi.nlm.nih.gov/41723577/) | 2026 | Comparative Review | Medical Science Monitor | Review of progestogen-containing COC components across acne, hirsutism, migraine, and dysmenorrhoea; notes that menstrual migraine may benefit from extended-cycle regimens, while migraine with aura remains a COC contraindication |

---

## Netherlands Market Information

Lynestrenol currently holds **no marketing authorisation** with the CBG-MEB (College ter Beoordeling van Geneesmiddelen). No RVG number is on record. The product is not available as a registered medicinal product in the Netherlands.

> Historically, Lynestrenol was developed by Organon (a Dutch pharmaceutical company) and marketed as Orgametril in several European markets. Its regulatory status in neighbouring countries (Belgium, Germany, UK) may be relevant for a future cross-border authorisation or label-extension strategy.

---

## Safety Considerations

Please refer to the SmPC (Samenvatting van de Productkenmerken) for complete safety information, as no structured warning or contraindication data was available in the current Evidence Pack.

**Class-level safety note relevant to the predicted indication:**
Combined hormonal contraceptives (oestrogen + progestogen) are **contraindicated** in migraine with aura due to significantly increased thromboembolic and ischaemic stroke risk. As a progestogen-only agent, Lynestrenol theoretically carries lower thrombogenic risk, but this has not been formally evaluated for migraine with aura. For migraine with brainstem aura (rank-3 indication), the risk-benefit ratio is particularly unfavourable given the posterior circulation involvement. Any clinical investigation must prospectively characterise haemostatic effects and stroke risk.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is currently at L4, consisting of mechanism-level hypotheses and a single historical case series (1963) with no control group. Lynestrenol holds no NL marketing authorisation, making any near-term regulatory pathway for a new indication filing particularly complex. The most compelling pharmacological signal — GABA-A modulation via neuroactive progestogen metabolites — is mechanistically plausible but unvalidated in the migraine-with-aura genetic subtype targeted by the rank-1 TxGNN prediction.

**To proceed, the following is needed:**

- **Mechanism confirmation**: Formal characterisation of Lynestrenol's neuroactive metabolite profile (allopregnanolone-type activity, GABA-A receptor binding data)
- **Clinical evidence**: A prospective controlled trial evaluating Lynestrenol or its active metabolite norethisterone in menstrually-associated migraine; the 1963 Lundberg observation should be replicated with modern methodology
- **Safety evaluation**: Dedicated assessment of coagulation parameters and stroke risk for the progestogen-only route in patients with migraine with aura
- **SmPC review**: Obtain and review the SmPC from a jurisdiction where Lynestrenol is currently authorised (e.g., Belgium) to assess existing warnings and contraindications applicable to the Dutch healthcare context
- **Regulatory pathway assessment**: Consultation with CBG-MEB on whether a new indication could be pursued under Article 29 (referral) or whether a fresh marketing authorisation application would be required, given the absence of any current NL registration
- **Subtype stratification**: Distinguish between menstrual migraine without aura (potentially lower risk, plausible benefit) and migraine with aura (higher thrombotic risk, stricter safety standards required) before any clinical programme is designed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

