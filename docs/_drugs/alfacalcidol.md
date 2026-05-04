---
layout: default
title: Alfacalcidol
parent: 僅模型預測 (L5)
nav_order: 20
evidence_level: L5
indication_count: 5
---

# Alfacalcidol
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

# Alfacalcidol: From Vitamin D-Related Disorders to Familial Isolated Hypoparathyroidism

## One-Sentence Summary

Alfacalcidol is a synthetic vitamin D analog (1α-hydroxycholecalciferol) widely used for calcium and bone metabolism disorders such as renal osteodystrophy and osteomalacia. The TxGNN model predicts it may be effective for **Familial Isolated Hypoparathyroidism Due to Impaired PTH Secretion**, with strong mechanistic rationale supporting this direction, though **no dedicated clinical trials or publications** specific to this rare indication have been identified. A secondary prediction for **Renal Tubular Acidosis** (rank 5) is supported by **8 publications** including case reports demonstrating alfacalcidol use in this setting.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No authorized indications on record (not marketed in the Netherlands) |
| Predicted New Indication | Familial isolated hypoparathyroidism due to impaired PTH secretion |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L4 — Established mechanistic rationale, no dedicated clinical trials |
| NL Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Alfacalcidol (1α-hydroxycholecalciferol) is a prodrug that requires only hepatic 25-hydroxylation to be converted into calcitriol (1,25-dihydroxyvitamin D₃), the biologically active form of vitamin D. Unlike native vitamin D, it bypasses the renal 1α-hydroxylation step — a critical distinction because this enzyme is normally stimulated by parathyroid hormone (PTH).

In familial isolated hypoparathyroidism due to impaired PTH secretion, the core defect is insufficient PTH production. This leads to reduced renal 1α-hydroxylase activity, diminished calcitriol synthesis, and consequently hypocalcaemia. Because alfacalcidol does not depend on PTH-driven renal activation, it directly compensates for this metabolic block. This is a well-established pharmacological principle: alfacalcidol is already recognized as standard-of-care for general hypoparathyroidism in many countries, and its application to this familial subtype follows the same mechanistic logic.

The TxGNN prediction score of 99.61% is consistent with this strong mechanistic link. While the specific familial subtype is rare and lacks dedicated clinical trial data, the broader use of alfacalcidol in hypoparathyroidism is well-documented in clinical practice, making this a high-confidence repurposing candidate from a pharmacological standpoint.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for alfacalcidol specifically targeting familial isolated hypoparathyroidism due to impaired PTH secretion.

---

## Literature Evidence

No publications were identified that specifically address alfacalcidol in the context of familial isolated hypoparathyroidism due to impaired PTH secretion. However, the established use of alfacalcidol in general hypoparathyroidism is well-documented in endocrinology textbooks and guidelines.

---

## Netherlands Market Information

Alfacalcidol currently holds no marketing authorization (RVG) in the Netherlands. No CBG-MEB licensed products were identified.

> **Note:** Alfacalcidol is marketed in other European countries and may be accessible via cross-border pharmacy supply or the EMA named patient/compassionate use framework. A CBG-MEB application or Article 126a procedure may be required.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) from the country of origin for safety information. No safety data (warnings, contraindications, or drug-drug interactions) was available in the current evidence pack.

> **Data Gap:** TFDA label warnings and contraindications have not yet been extracted. This is classified as a **blocking** gap for Stage 1 safety assessment. Remediation: download and parse the SmPC/PIL from the relevant regulatory authority.

---

## Additional Predicted Indications

The TxGNN model identified four additional indications. Two are noteworthy:

### Renal Tubular Acidosis (Rank 5) — Proceed with Guardrails

| Item | Content |
|------|------|
| TxGNN Score | 99.27% |
| Evidence Level | L4 |
| Mechanistic Link | **Strong** — RTA (especially Type 2/proximal and Fanconi syndrome) causes phosphate wasting, chronic metabolic acidosis suppressing renal 1α-hydroxylase, and secondary osteomalacia. Alfacalcidol bypasses impaired renal vitamin D activation. |

#### Literature Evidence (Renal Tubular Acidosis)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11518137](https://pubmed.ncbi.nlm.nih.gov/11518137/) | 2001 | Case Report | Intern Med (Tokyo) | Rapid improvement of osteomalacia with alfacalcidol in Sjögren's + RTA-1 |
| [22740247](https://pubmed.ncbi.nlm.nih.gov/22740247/) | 2013 | Case Report | Mod Rheumatol | Successful treatment of osteomalacia caused by RTA + Sjögren's; alfacalcidol used as part of regimen, bone density normalized by 24 months |
| [6893175](https://pubmed.ncbi.nlm.nih.gov/6893175/) | 1980 | Clinical Study | Contrib Nephrol | 1α-OH-VD₃ in 6 patients with different types of Fanconi syndrome; 200–250× potency vs vitamin D₂; calcium malabsorption from failed 1α-hydroxylation confirmed |
| [33398781](https://pubmed.ncbi.nlm.nih.gov/33398781/) | 2021 | Case Report | CEN Case Rep | Osteomalacia from atypical RTA with vitamin D deficiency; treated with active vitamin D |
| [28509074](https://pubmed.ncbi.nlm.nih.gov/28509074/) | 2012 | Case Report + Review | CEN Case Rep | Osteomalacia secondary to distal RTA due to Sjögren's; alfacalcidol in management |
| [36412607](https://pubmed.ncbi.nlm.nih.gov/36412607/) | 2023 | Case Report | Kidney Blood Press Res | Severe hypophosphatemia as initial presentation of renal Fanconi's syndrome and distal RTA |
| [6709109](https://pubmed.ncbi.nlm.nih.gov/6709109/) | 1984 | Case Report | Neth J Med | 25-hydroxylation of 1α-OH vitamin D in primary biliary cirrhosis complicated by RTA |
| [9134837](https://pubmed.ncbi.nlm.nih.gov/9134837/) | 1997 | Longitudinal Follow-up | Nihon Jinzo Gakkai Shi | Long-term bone mineral density follow-up in adult idiopathic Fanconi syndrome |

### Indications with Weak Mechanistic Links (Hold)

| Rank | Disease | TxGNN Score | Recommendation | Rationale |
|------|---------|-------------|----------------|-----------|
| 2 | Dahlberg-Borer-Newcomer syndrome | 99.60% | Hold | Ultra-rare genetic disorder with no known link to calcium/phosphate metabolism; high TxGNN score likely an artifact of rare disease node connectivity patterns |
| 3 | Craniofacial conodysplasia | 99.55% | Hold | Genetic craniofacial bone malformation driven by developmental signaling pathways (SHH, BMP, FGF), not calcium/phosphate imbalance |
| 4 | Acromesomelic dysplasia, Campailla Martinelli type | 99.53% | Hold | Genetic short-limb dwarfism involving growth plate chondrocyte mutations (GDF5/BMPR1B/NPR2); VDR-mediated calcium regulation cannot correct this |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Alfacalcidol has a strong, well-established pharmacological mechanism for treating hypoparathyroidism — it bypasses PTH-dependent renal 1α-hydroxylation to restore active vitamin D levels and correct hypocalcaemia. While the specific familial isolated subtype lacks dedicated trials, the drug's mechanism directly addresses the core pathophysiology. The secondary prediction for renal tubular acidosis is further supported by multiple case reports demonstrating clinical benefit.

**To proceed, the following is needed:**
- **Regulatory pathway clarification**: Determine how to access alfacalcidol in the Netherlands (cross-border supply, Article 126a, or new CBG-MEB application)
- **SmPC/safety data extraction**: Obtain the Summary of Product Characteristics from an EU-authorized source to complete the safety assessment (currently a blocking data gap)
- **Mechanism of action documentation**: Retrieve full MOA data from DrugBank to formalize the pharmacological rationale
- **Clinical evidence for familial subtype**: Conduct a targeted literature search for alfacalcidol or calcitriol use specifically in familial isolated hypoparathyroidism registries
- **Expert consultation**: Engage a clinical endocrinologist to assess the applicability of standard hypoparathyroidism management protocols to this rare genetic subtype

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. Report version: v4 | Data cutoff: 2026-04-03 | Candidate ID: TW-DB01436-multi*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

