---
layout: default
title: Ciclesonide
parent: 僅模型預測 (L5)
nav_order: 42
evidence_level: L5
indication_count: 6
---

# Ciclesonide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Using the `txgnn-pipeline` skill to inform report structure, then proceeding to generate the NL evaluation report for Ciclesonide.

---

# Ciclesonide: From Asthma to Atopic Eczema

## One-Sentence Summary

Ciclesonide is an inhaled/intranasal corticosteroid (ICS) established for the treatment of asthma and allergic rhinitis; no Dutch marketing authorizations were found in the CBG-MEB registry.
The TxGNN model predicts it may be effective for **Atopic Eczema** with a prediction score of **99.96%**, yet this is currently supported by **0 clinical trials** and **0 publications** — a pure model prediction.
The mechanistic rationale is questionable: ciclesonide's inhaled/nasal route of administration is fundamentally incompatible with the topical requirements of treating a skin condition, suggesting this may be a false-positive driven by the model's generalisation of the glucocorticoid drug class.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Asthma and allergic rhinitis (inhaled/intranasal corticosteroid; no approved indication text available from NL registry) |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| NL Market Status | Not registered (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Ciclesonide is a prodrug inhaled/intranasal corticosteroid that is converted locally in the airways to its active metabolite des-ciclesonide. It exerts its effect by binding to the glucocorticoid receptor and suppressing airway inflammation — reducing eosinophil activity, mast cell degranulation, and pro-inflammatory cytokines including IL-4, IL-5, and IL-13.

The TxGNN model's prediction likely stems from a shared biological pathway: atopic eczema (atopic dermatitis, ICD-10: L20) is an inflammatory skin disease in which corticosteroids are the cornerstone of treatment. At a class level, the logic is superficially coherent — glucocorticoids suppress inflammation, and atopic eczema is an inflammatory condition driven by Th2 cytokine dysregulation, the very same pathway ciclesonide targets in the airways.

However, this is almost certainly a model artefact rather than a genuine repurposing signal. Ciclesonide is engineered specifically for minimal systemic bioavailability and has no topical skin formulation. Its route of administration (inhaled or intranasal) cannot reach cutaneous disease targets. Furthermore, well-established topical corticosteroids (betamethasone, triamcinolone, mometasone) already fulfil this therapeutic role with robust evidence. The combination of zero clinical evidence, route incompatibility, and no unmet medical need makes this prediction a clear **Hold**.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Netherlands Market Information

No marketing authorizations for Ciclesonide were found in the Dutch CBG-MEB registry for this data cut (2026-05-01).

> **Note for reviewers:** Ciclesonide (brand name Alvesco®) holds a centralized EMA marketing authorization valid across the EU/EEA. Its current availability and SmPC status in the Netherlands should be verified directly via the [CBG-MEB product database](https://www.cbg-meb.nl/) or the [EMA product page](https://www.ema.europa.eu/en/medicines/human/EPAR/alvesco). The absence of an RVG number in this dataset may reflect a data-sourcing gap rather than a true absence of authorization.

---

## Safety Considerations

No safety data (key warnings, contraindications, or drug interactions) was available in this Evidence Pack.

Please refer to the SmPC (Samenvatting van de Productkenmerken) for complete safety information, including corticosteroid-class effects such as HPA-axis suppression, growth retardation in children, and risk of systemic absorption at high doses.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.96%), there is no clinical or preclinical evidence supporting ciclesonide for atopic eczema, and — more critically — ciclesonide's inhaled/intranasal route of administration is mechanistically incompatible with treating a cutaneous condition. This prediction is best interpreted as a model false-positive arising from the broad association between the glucocorticoid drug class and inflammatory diseases.

**To proceed, the following would be needed:**

- **Route feasibility assessment**: Could a topical dermatological formulation of ciclesonide be developed, and would it offer any advantage over established topical corticosteroids?
- **MOA gap resolution**: Obtain full DrugBank data (currently DG002 — High severity) to formally document the receptor binding profile and confirm class-level reasoning.
- **NL/EMA registration verification**: Confirm current Dutch market availability of Alvesco® via CBG-MEB direct query, as the zero-license finding may reflect a data gap.
- **Differentiation analysis**: If formulation feasibility is confirmed, a comparative efficacy/safety assessment against existing topical corticosteroids is required before any further investment.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

