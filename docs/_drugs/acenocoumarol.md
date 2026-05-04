---
layout: default
title: Acenocoumarol
parent: 僅模型預測 (L5)
nav_order: 15
evidence_level: L5
indication_count: 3
---

# Acenocoumarol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Acenocoumarol: From Anticoagulation Therapy to Hereditary Thrombophilia

## One-Sentence Summary

Acenocoumarol is a vitamin K antagonist (VKA) anticoagulant, widely used in Europe for the prevention and treatment of thromboembolic disorders. The TxGNN model predicts it may be effective for three rare hereditary thrombophilias: **Heparin Cofactor 2 Deficiency**, **Factor V Excess with Spontaneous Thrombosis**, and **Antithrombin Deficiency Type 2**, though currently **no clinical trials** and **no publications** directly support these specific repurposing indications.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anticoagulation therapy (thromboembolic disorders) — no local licenses on file |
| Predicted New Indication (Rank 1) | Heparin Cofactor 2 Deficiency |
| Predicted New Indication (Rank 2) | Factor V Excess with Spontaneous Thrombosis |
| Predicted New Indication (Rank 3) | Antithrombin Deficiency Type 2 |
| TxGNN Prediction Score (Rank 1) | 99.84% |
| Evidence Level | L5 — Model prediction only, no direct clinical studies |
| Market Status | Not marketed (未上市) in the queried jurisdiction |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Acenocoumarol is a coumarin-derivative vitamin K antagonist (VKA) that inhibits vitamin K epoxide reductase (VKORC1), thereby reducing the hepatic synthesis of vitamin K–dependent clotting factors (Factors II, VII, IX, and X) as well as the anticoagulant proteins C and S. It is pharmacologically closely related to warfarin and phenprocoumon and has been a standard oral anticoagulant in the Netherlands and other European countries for decades.

All three predicted indications are rare hereditary thrombophilias — conditions in which a genetic defect in the natural anticoagulant pathway leads to a hypercoagulable state and increased risk of venous thromboembolism (VTE). **Heparin Cofactor II (HCII/SERPIND1) deficiency** reduces thrombin inhibition; **Factor V excess** leads to overactivation of the coagulation cascade; and **Antithrombin III (SERPINC1) type 2 deficiency** impairs the inhibition of thrombin and Factor Xa. In each case, the fundamental problem is an imbalance favouring clot formation, and a VKA like acenocoumarol can counteract this by reducing the supply of functional procoagulant factors from upstream.

The mechanistic logic is strongest for antithrombin deficiency type 2, where international guidelines already recommend long-term oral anticoagulation (including VKAs) for patients with confirmed thrombotic events. For heparin cofactor II deficiency and factor V excess, the evidence base is far thinner — HCII deficiency's status as an independent thrombotic risk factor remains debated, and factor V excess (distinct from Factor V Leiden) is exceedingly rare. Nevertheless, the shared pathophysiology of defective natural anticoagulation ↔ VKA-mediated reduction of procoagulant factor synthesis provides a coherent mechanistic rationale for all three predictions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the three predicted indications in combination with acenocoumarol, based on searches of ClinicalTrials.gov and the WHO ICTRP (searched 2026-03-10).

---

## Literature Evidence

Currently no related literature available linking acenocoumarol specifically to heparin cofactor 2 deficiency, factor V excess with spontaneous thrombosis, or antithrombin deficiency type 2, based on PubMed searches (searched 2026-03-10).

---

## Market Information

No marketing authorizations were found in the queried jurisdiction. Acenocoumarol has **0 registered licenses** on file.

> **Note:** Acenocoumarol is widely authorized and prescribed in the Netherlands (e.g., Sintrom®) and across continental Europe. The absence of licenses in this evidence pack reflects the queried data source (Taiwan/TFDA), where acenocoumarol is not marketed. For Dutch regulatory status, the CBG-MEB Geneesmiddeleninformatiebank should be consulted.

---

## Safety Considerations

> Please refer to the SmPC (Summary of Product Characteristics) for comprehensive safety information. The evidence pack did not contain resolved safety data for acenocoumarol.

**General VKA class safety profile (for context):**
- **Narrow therapeutic index** — requires regular INR monitoring (target typically 2.0–3.5 depending on indication)
- **Bleeding risk** — major and minor haemorrhage is the primary adverse effect
- **Teratogenicity** — coumarins are contraindicated in pregnancy (coumarin embryopathy)
- **Extensive drug–drug interactions** — CYP2C9 substrate; interactions with NSAIDs, antibiotics, antifungals, and many other drug classes
- **Dietary interactions** — vitamin K intake affects anticoagulant effect
- **Skin necrosis** — rare but serious, particularly in protein C/S deficiency (relevant for this patient population)

> ⚠️ **Special consideration for hereditary thrombophilias:** In patients with protein C or protein S deficiency (which may coexist with the predicted indications), initiation of VKA therapy without heparin bridging can precipitate warfarin-induced skin necrosis. This risk must be evaluated before prescribing acenocoumarol in thrombophilia patients.

---

## Detailed Predicted Indications

### Rank 1: Heparin Cofactor 2 Deficiency

| Item | Content |
|------|------|
| TxGNN Score | 99.84% (rank 473) |
| Evidence Level | L5 |
| Decision Stage | S0 |
| Recommendation | Hold |

**Mechanistic rationale:** Heparin Cofactor II (HCII/SERPIND1) is a serine protease inhibitor. When deficient, thrombin inhibition is insufficient, predisposing to thrombosis. Acenocoumarol reduces clotting factor synthesis upstream, thereby decreasing thrombin generation — a logical but indirect compensatory mechanism. Whether HCII deficiency constitutes an independent thrombotic risk factor remains debated, with some studies suggesting very low penetrance.

---

### Rank 2: Factor V Excess with Spontaneous Thrombosis

| Item | Content |
|------|------|
| TxGNN Score | 99.78% (rank 583) |
| Evidence Level | L5 |
| Decision Stage | S0 |
| Recommendation | Hold |

**Mechanistic rationale:** Excess Factor V leads to overactivation of the coagulation cascade and spontaneous thrombosis. Acenocoumarol does not directly inhibit Factor V (which is not vitamin K–dependent), but can indirectly attenuate the coagulation cascade by reducing prothrombin (Factor II) synthesis. This condition is distinct from Factor V Leiden (a gain-of-function mutation conferring activated protein C resistance) and is exceedingly rare.

---

### Rank 3: Antithrombin Deficiency Type 2

| Item | Content |
|------|------|
| TxGNN Score | 99.77% (rank 607) |
| Evidence Level | L5 |
| Decision Stage | S1 |
| Recommendation | Hold |

**Mechanistic rationale:** Antithrombin III (SERPINC1) type 2 deficiency is a qualitative defect (dysfunctional protein) leading to insufficient inhibition of thrombin and Factor Xa. This is a well-established high-risk thrombophilia. VKAs provide long-term anticoagulant protection by reducing clotting factor synthesis. **This indication has the strongest mechanistic link** of the three, as long-term oral anticoagulation (including VKAs) is already recommended in international guidelines for antithrombin-deficient patients with thrombotic events.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the mechanistic rationale connecting a VKA to hereditary thrombophilias is sound — particularly for antithrombin deficiency type 2, where VKA use is already part of established clinical practice — there are **no disease-specific clinical trials or publications** to support formal repurposing. All three predictions are at evidence level L5 (model prediction only). Additionally, the drug has no marketing authorization in the queried jurisdiction, and critical safety data (SmPC warnings, contraindications, DDI profile) were not available in this evidence pack.

**To proceed, the following is needed:**
- **Regulatory data:** Obtain Dutch CBG-MEB marketing authorization details for acenocoumarol (Sintrom® and generics) from the Geneesmiddeleninformatiebank
- **Safety profile:** Extract SmPC warnings, contraindications, and drug interaction data from the Dutch-authorized SmPC
- **Mechanism of action:** Confirm detailed MOA via DrugBank API (data gap DG002)
- **Literature search expansion:** Broaden PubMed search to include VKA class (not just acenocoumarol) in combination with each thrombophilia, and include warfarin-based evidence that may be applicable
- **Clinical guideline review:** Cross-reference with ISTH, ASH, and Dutch (NIV/NHG) guidelines on management of hereditary thrombophilias to determine whether VKA use is already standard of care (which would change this from "repurposing" to "established off-label/guideline-supported use")
- **Prioritization note:** Antithrombin deficiency type 2 (rank 3) may warrant fast-tracking to S1 evaluation given existing guideline support for VKA use in this population

---

*This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. Report generated 2026-04-03.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

