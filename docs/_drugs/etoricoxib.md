---
layout: default
title: Etoricoxib
parent: 僅模型預測 (L5)
nav_order: 64
evidence_level: L5
indication_count: 10
---

# Etoricoxib
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

Using the `txgnn-pipeline` skill for context. Now generating the Netherlands drug repurposing evaluation report for Etoricoxib.

---

# Etoricoxib: From Musculoskeletal Inflammation to Migraine Disorder

## One-Sentence Summary

Etoricoxib is a selective COX-2 inhibitor used in many countries for musculoskeletal inflammatory conditions — including osteoarthritis, rheumatoid arthritis, and ankylosing spondylitis — though it currently holds no marketing authorization from the CBG-MEB in the Netherlands.
The TxGNN model predicts it may be effective for **migraine disorder** with a score of 99.90%, yet there are currently **no clinical trials** and **no publications** directly supporting this specific indication.
Closely related predicted indications — particularly **headache disorder** (rank 9) and **trigeminal autonomic cephalalgia** (rank 10) — show early case-level evidence that provides indirect mechanistic support and represents a more tractable near-term research target.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Musculoskeletal inflammatory conditions (osteoarthritis, ankylosing spondylitis, acute gouty arthritis); no CBG-MEB authorization in the Netherlands |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| NL Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Etoricoxib is a selective cyclooxygenase-2 (COX-2) inhibitor. Detailed mechanism of action data from DrugBank was not available in this evidence pack, however based on its pharmacological class, etoricoxib works by selectively blocking the COX-2 enzyme, reducing synthesis of prostaglandins — in particular prostaglandin E2 (PGE2) — in inflamed tissues. By sparing COX-1 activity (which protects the gastric mucosa), etoricoxib achieves anti-inflammatory and analgesic effects with a lower gastrointestinal risk profile than non-selective NSAIDs such as indomethacin or naproxen.

The mechanistic bridge from musculoskeletal inflammation to migraine is scientifically plausible. COX-2 is expressed in the central nervous system and participates in neurogenic inflammation within the trigeminovascular system. PGE2 produced via COX-2 can activate trigeminal nociceptors, promote central sensitization, and facilitate meningeal vasodilation — all recognized elements of the migraine cascade. This rationale is indirectly supported by the well-established efficacy of indomethacin (a non-selective COX inhibitor) in several primary headache subtypes, suggesting that COX pathway inhibition plays a genuine physiological role in headache pathophysiology.

The critical limitation is that the predicted indication is **migraine disorder** at a broad disease level. No direct clinical evidence currently exists demonstrating etoricoxib's efficacy specifically in migraine. The TxGNN model's high score reflects strong graph-level associative connectivity, not clinical validation. The more evidenced signals — case series and case reports of etoricoxib resolving primary stabbing headache, secondary cough headache, and indomethacin-responsive trigeminal autonomic cephalalgias — point to narrower, mechanistically coherent subtypes where a proof-of-concept investigation would be better targeted.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for etoricoxib in migraine disorder.

---

## Literature Evidence

Currently no related literature available for etoricoxib in migraine disorder.

---

## Netherlands Market Information

Etoricoxib currently holds **no marketing authorization** from the CBG-MEB (College ter Beoordeling van Geneesmiddelen — Medicines Evaluation Board). The drug is not marketed in the Netherlands as of the data cutoff (May 2026). Notably, etoricoxib has also never received approval from the US FDA, though it is authorized in more than 70 countries — including several EU member states via national procedures — and is listed in the EMA's assessment history.

Any future application for use in the Netherlands would require either a centralized EMA marketing authorization procedure or a national CBG-MEB submission supported by a full SmPC (Samenvatting van de Productkenmerken). The absence of a current Dutch SmPC means that safety and dosing guidance must be sourced from international SmPCs (e.g., the EMA's Arcoxia assessment report) for any research or compassionate-use context.

---

## Safety Considerations

**Important safety signals from related evidence (headache indication context):**

- **Reversible Cerebral Vasoconstriction Syndrome (RCVS)**: A case of RCVS possibly induced by etoricoxib has been reported ([PMID 25229174](https://pubmed.ncbi.nlm.nih.gov/25229174/)). Given the neurological nature of the predicted indication (migraine), this cerebrovascular adverse event profile warrants particular attention in any future clinical investigation.

- **Life-threatening hyperkalemia and acute kidney injury**: A case report ([PMID 21373319](https://pubmed.ncbi.nlm.nih.gov/21373319/)) describes severe hyperkalemia precipitated by etoricoxib in a patient concurrently taking telmisartan (an ARB) on a low-sodium diet. This highlights a clinically important drug–drug and drug–diet interaction relevant to any prescribing context.

- **Cardiovascular risk**: As a COX-2 selective inhibitor, etoricoxib carries a class-level cardiovascular risk signal (increased risk of myocardial infarction and stroke), which must be weighed against potential benefit in any new indication — particularly for long-term use in a migraine prophylaxis context.

For complete warnings, contraindications, and drug interaction data, please refer to the international SmPC (e.g., EMA Arcoxia SmPC) as no Dutch SmPC is currently available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for migraine disorder is mechanistically plausible via the COX-2/PGE2/trigeminovascular pathway, but rests entirely on graph-level model inference with no supporting clinical trials or publications — constituting L5 evidence only. Furthermore, etoricoxib has no CBG-MEB marketing authorization in the Netherlands, creating a dual barrier (clinical evidence and regulatory) that must be addressed before any healthcare system consideration.

**To proceed, the following is needed:**

- **Narrow the target**: Consider reframing the research question around the better-evidenced related indications — **headache disorder** (L4; 5 case-level publications including PMID [35277974](https://pubmed.ncbi.nlm.nih.gov/35277974/) and [18171381](https://pubmed.ncbi.nlm.nih.gov/18171381/)) and **trigeminal autonomic cephalalgia** (L4; 1 case series, PMID [35277974](https://pubmed.ncbi.nlm.nih.gov/35277974/)) — where COX-2 inhibition has shown real patient-level responses in indomethacin-responsive subtypes
- **Obtain full MOA documentation**: Query DrugBank API for etoricoxib (DB01628) and retrieve pharmacodynamics and pharmacokinetics data to complete the mechanistic assessment
- **Safety profile review**: Conduct a structured review of cardiovascular, renal, and neurological adverse events (including RCVS risk) before any neurological indication development
- **Pilot study design**: If proceeding, design a small proof-of-concept study in a well-defined indomethacin-responsive headache subtype (e.g., primary stabbing headache or hemicrania continua) before advancing to broader migraine populations
- **Regulatory pathway**: Consult with CBG-MEB or EMA regarding the regulatory pathway for an investigational use in the Netherlands, particularly in the context of no current Dutch market authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

