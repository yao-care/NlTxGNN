---
layout: default
title: Abciximab
parent: 僅模型預測 (L5)
nav_order: 12
evidence_level: L5
indication_count: 0
---

# Abciximab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# ABCIXIMAB: Drug Repurposing Evaluation — No Candidate Indications Identified

## One-Sentence Summary

Abciximab (DrugBank: DB00054) is a glycoprotein IIb/IIIa receptor inhibitor historically used as an antiplatelet agent during percutaneous coronary interventions. The TxGNN model did **not generate any predicted new indications** for this drug, and the evidence pack contains **no clinical trials** or **publications** to support a repurposing direction at this time.

## Quick Overview

| Item | Content |
|------|------|
| Drug (INN) | Abciximab |
| DrugBank ID | [DB00054](https://go.drugbank.com/drugs/DB00054) |
| Original Indication | Not recorded in evidence pack (see note below) |
| Predicted New Indication | **None** — no TxGNN predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | **L5** (No model predictions, no supporting studies) |
| NL Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

> **Note on original indication:** The evidence pack does not contain approved indication text. From established pharmacological references, abciximab (brand name ReoPro) is a chimeric monoclonal antibody Fab fragment that inhibits glycoprotein IIb/IIIa on platelets, and has been used as adjunct antiplatelet therapy during percutaneous coronary intervention (PCI) and unstable angina management. However, the product has been discontinued in many markets globally.

## Why is This Prediction Reasonable?

No TxGNN predictions were generated for abciximab. This may be due to one or more of the following reasons:

1. **Limited knowledge graph connectivity:** Abciximab is a biologic (monoclonal antibody fragment) rather than a small molecule. The TxGNN knowledge graph may have insufficient relational data for biologics, resulting in no high-confidence repurposing candidates.

2. **Market withdrawal:** Abciximab (ReoPro) has been discontinued or withdrawn from many global markets, including the Netherlands. Its absence from active regulatory databases may reduce its connectivity within the prediction model's drug–disease network.

3. **Narrow mechanism of action:** As a highly specific GPIIb/IIIa inhibitor acting on platelet aggregation, the pharmacological mechanism may not readily extrapolate to non-cardiovascular disease domains within the model's scoring threshold.

Currently, detailed mechanism of action data was not provided in the evidence pack. Based on established pharmacological knowledge, abciximab is a chimeric human-murine monoclonal antibody Fab fragment that binds to the glycoprotein IIb/IIIa receptor on activated platelets, preventing fibrinogen binding and thereby inhibiting platelet aggregation. This mechanism is well-characterized but highly specific to the coagulation/thrombosis pathway.

## Clinical Trial Evidence

Currently no related clinical trials registered for repurposing candidates (no predicted indications available).

## Literature Evidence

Currently no related literature available for repurposing candidates (no predicted indications available).

## Netherlands Market Information

Abciximab has **no current marketing authorizations** registered in the evidence pack. The drug is listed as **not marketed** (未上市).

> **Regulatory context:** No CBG-MEB (College ter Beoordeling van Geneesmiddelen) registrations or EMA centrally authorized product records were identified for this drug. Historically, abciximab was marketed as ReoPro but has been discontinued in many jurisdictions. Any future repurposing consideration would require a new marketing authorization application.

## Safety Considerations

> Please refer to the SmPC (Summary of Product Characteristics) for safety information. The evidence pack does not contain warnings, contraindications, or drug interaction data for abciximab. For historical reference, the ReoPro SmPC documented key risks including bleeding, thrombocytopenia, and hypersensitivity reactions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model did not identify any repurposing candidates for abciximab. Combined with the drug's lack of current market authorization in the Netherlands and significant data gaps (no MOA data, no safety data, no regulatory filings in the evidence pack), there is insufficient basis to advance this drug into any repurposing evaluation pathway.

**To proceed, the following would be needed:**
- TxGNN model re-evaluation with updated knowledge graph data to determine if any predictions emerge
- Retrieval of mechanism of action data from DrugBank API (identified as data gap DG002)
- Clarification of global regulatory status and commercial availability
- Assessment of whether a biologic-specific repurposing model would yield different results
- If a candidate indication is eventually identified: retrieval of SmPC safety data (identified as blocking data gap DG001)

---

*This report was generated on 2026-04-03 based on Evidence Pack v4. Results are for research purposes only and do not constitute medical advice. Any drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

