---
layout: default
title: Iloprost
parent: 僅模型預測 (L5)
nav_order: 78
evidence_level: L5
indication_count: 9
---

# Iloprost
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

以下是根據 Evidence Pack 生成的 Iloprost 藥師評估報告：

---

# Iloprost: From Pulmonary Arterial Hypertension to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Iloprost is a synthetic prostacyclin analogue internationally established for the treatment of pulmonary arterial hypertension and peripheral arterial disease, though it currently holds no registered marketing authorization with the CBG-MEB in the Netherlands.
The TxGNN model predicts it may be effective for **Hypotrichosis Simplex of the Scalp**,
with **0 clinical trials** and **0 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pulmonary arterial hypertension / peripheral arterial disease (no CBG-MEB authorization on record) |
| Predicted New Indication | Hypotrichosis Simplex of the Scalp |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| NL Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Iloprost is a synthetic analogue of prostacyclin (PGI₂) acting as an IP (prostacyclin) receptor agonist. It activates adenylate cyclase, elevating intracellular cAMP, which drives pulmonary and peripheral vascular smooth muscle relaxation, inhibits platelet aggregation, and suppresses vascular smooth muscle cell proliferation. These properties form the basis of its internationally recognized use in pulmonary arterial hypertension (PAH) and peripheral vascular disease.

Hypotrichosis simplex of the scalp is a hereditary hair follicle disorder caused by mutations in *APCDD1*, *LPAR6*, or *LIPH* genes, resulting in progressive follicular miniaturization. Its pathophysiology is fundamentally genetic and structural in nature, driven by disruption of Wnt/β-catenin, FGF, and BMP developmental signaling pathways — none of which have established crosstalk with the prostacyclin receptor pathway.

No pharmacologically plausible mechanistic link has been described between the prostacyclin IP-receptor axis and hair follicle biology. The high TxGNN score (0.9945) is most likely a **topological artifact** within the knowledge graph — where hair follicle disease nodes may share indirect connectivity with skin vascularization nodes — rather than a genuine pharmacological association. The complete absence of supporting clinical trial and literature evidence confirms that this prediction should not serve as a basis for research initiation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Netherlands Market Information

No marketing authorizations for Iloprost are registered with the CBG-MEB in the Netherlands. Iloprost-containing products holding EMA centralized authorization (e.g., Ventavis® for inhaled use in PAH; Ilomedin® for intravenous use in peripheral arterial disease) should be cross-referenced directly with the EMA product register, as centrally authorized products operate under EMA's jurisdiction rather than CBG-MEB's national procedure. The current dataset reports NL market status as **not marketed**.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a numerically high TxGNN prediction score (99.45%), the model prediction for this indication carries no mechanistic plausibility and is unsupported by any clinical trial or published literature; the signal is consistent with a knowledge graph topological pseudo-association rather than a true pharmacological link between the prostacyclin pathway and hereditary scalp hypotrichosis.

**To proceed, the following is needed:**
- Preclinical evidence (in vitro or in vivo) demonstrating any prostacyclin pathway involvement in hair follicle cycling or maintenance
- Knowledge graph path analysis to identify which nodes are driving TxGNN's topological link between Iloprost and this indication
- Full SmPC review (Ventavis and Ilomedin) to establish the complete safety and contraindication profile before any clinical consideration
- Regulatory clarification with CBG-MEB on Iloprost's current availability in the Netherlands under EMA centralized authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

