---
layout: default
title: Mesalazine
parent: 僅模型預測 (L5)
nav_order: 93
evidence_level: L5
indication_count: 7
---

# Mesalazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

Using `txgnn-pipeline` skill — this is an NlTxGNN drug repurposing evaluation report. Now generating the full report based on the Evidence Pack.

---

# Mesalazine: From Inflammatory Bowel Disease to Congenital Hypotrichosis with Juvenile Macular Dystrophy

## One-Sentence Summary

Mesalazine (5-aminosalicylic acid, 5-ASA) is a well-established anti-inflammatory drug used for decades in the treatment of inflammatory bowel disease, particularly ulcerative colitis. The TxGNN model's top-ranked prediction is **congenital hypotrichosis with juvenile macular dystrophy** with a score of 99.65%, yet this direction is currently supported by **no clinical trials** and **no published literature**. The high model score is likely a knowledge graph topology artefact rather than a true pharmacological signal, and a Hold decision is warranted for this specific indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Inflammatory bowel disease (ulcerative colitis) |
| Predicted New Indication | Congenital hypotrichosis with juvenile macular dystrophy |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| NL Market Status | No CBG-MEB authorizations found in current data |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, Mesalazine (5-ASA) is the active anti-inflammatory moiety of sulfasalazine. It exerts its effects primarily through inhibition of the NF-κB signalling pathway, suppression of prostaglandin and leukotriene synthesis, and reactive oxygen species scavenging — predominantly at mucosal surfaces in the gastrointestinal tract. Its efficacy in inflammatory bowel disease has been validated in numerous clinical trials over several decades.

Congenital hypotrichosis with juvenile macular dystrophy (CHIJMD) is a rare autosomal recessive disorder caused by mutations in the *LIPA* gene (lysosomal acid lipase A). The disease manifests as progressive hair loss and early-onset macular degeneration. Critically, the underlying pathology is **structural and genetic** in nature — driven by lysosomal enzyme deficiency and lipid accumulation — and is **not primarily inflammation-mediated**. There is no established biological pathway linking Mesalazine's anti-inflammatory mechanism to the *LIPA* gene axis or to retinal/hair follicle structural integrity.

The TxGNN model's high prediction score (99.65%) for this indication most likely reflects shared graph-level node connections in the knowledge graph — such as "skin" or "ophthalmology" disease nodes — rather than a genuine pharmacological basis. This prediction should be treated as a computational signal requiring biological validation before any further investment. No mechanistic justification supports proceeding at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Netherlands Market Information

No CBG-MEB marketing authorizations are recorded in the current evidence pack for Mesalazine in the Netherlands. The evidence pack carries candidate ID `TW-DB00244-multi`, indicating that the regulatory data field was populated with Taiwan (TFDA) data rather than Dutch CBG-MEB registry data.

> ⚠️ **Important:** Mesalazine is a widely used drug that is expected to carry CBG-MEB authorizations in the Netherlands (e.g., under brand names such as Pentasa, Asacol, or Salofalk). A direct query to the CBG-MEB registry is required to confirm the actual Dutch market status before making any regulatory conclusions.

---

## Safety Considerations

Please refer to the SmPC (Samenvatting van de Productkenmerken) for safety information. No key warnings, contraindications, or drug interaction data were available in the current evidence pack.

> ⚠️ Retrieval of the Dutch SmPC is classified as a **Blocking** data gap (DG001) — safety evaluation cannot proceed until this document is obtained from the CBG-MEB or via the EMA's product information portal.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction for Mesalazine — congenital hypotrichosis with juvenile macular dystrophy — carries no supporting clinical trials, no published literature, and no plausible mechanistic link. The *LIPA* gene-driven structural disease pathology is fundamentally incompatible with Mesalazine's anti-inflammatory mechanism of action, making this an L5 computational signal that does not meet the threshold for further evaluation at this time.

**To proceed, the following is needed:**

- **CBG-MEB registry query**: Confirm actual Dutch marketing authorization status for all Mesalazine formulations (resolves the regulatory data gap)
- **SmPC retrieval**: Obtain the current Dutch SmPC to complete key warnings, contraindications, and drug interaction assessment (resolves DG001 — Blocking gap)
- **Mechanistic pre-screening**: If any new evidence emerges linking Mesalazine to lysosomal lipase biology or retinal/follicular structural pathways, re-evaluate prediction viability
- **Consider alternative indications**: The evidence pack contains two other predictions with stronger biological support — **osteoarthritis** (rank 2, L4, 1 × 2024 Nature Communications pre-clinical study via OSCAR-PPARγ axis) and **rheumatoid arthritis** (rank 3, L3, historical Sulfasalazine DMARD evidence) — which may be more suitable candidates for dedicated repurposing evaluation reports
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

