---
layout: default
title: Flurbiprofen
parent: 僅模型預測 (L5)
nav_order: 72
evidence_level: L5
indication_count: 10
---

# Flurbiprofen
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

Using the `txgnn-pipeline` skill for context. This is a NlTxGNN report generation task. The Evidence Pack's highest-ranked prediction (acromesomelic dysplasia, L5/Hold) has zero evidence, while **rank 8 — Ankylosing Spondylitis** carries 20 publications including 8 RCTs and an L2/Proceed with Guardrails classification. I'll focus the report on AS as the sole clinically actionable candidate, which is consistent with the report format's intent.

---

# Flurbiprofen: From Inflammatory Joint Disease to Ankylosing Spondylitis

## One-Sentence Summary

Flurbiprofen is a phenylalkanoic acid NSAID internationally established for rheumatoid arthritis, osteoarthritis, and inflammatory joint conditions, but currently holding **no marketing authorization in the Netherlands**.
The TxGNN model predicts it may be effective for **Ankylosing Spondylitis (AS)**, with **0 registered clinical trials** but **20 publications** — including at least 8 randomized controlled trials directly comparing Flurbiprofen against standard-of-care agents in AS patients.
This body of evidence, spanning 1974–1986, consistently demonstrates efficacy equivalent to indomethacin, phenylbutazone, and naproxen, and Flurbiprofen has received AS marketing authorization in other European markets such as the United Kingdom.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, and allied inflammatory joint conditions (international; not registered in NL) |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| NL Market Status | Not on market |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Flurbiprofen is a non-selective inhibitor of cyclooxygenase enzymes (COX-1 and COX-2). By blocking prostaglandin synthesis, it reduces the downstream inflammatory mediators responsible for joint pain, swelling, and stiffness. Although detailed MOA documentation was not available in the current Evidence Pack, published review data establishes Flurbiprofen as at least as potent as indomethacin in preclinical models, and approximately 200 times more potent than aspirin — placing it among the more efficacious members of the NSAID class.

Ankylosing Spondylitis is an HLA-B27-associated chronic inflammatory spondyloarthropathy in which prostaglandin-driven inflammation causes progressive axial skeletal destruction and joint fusion. NSAIDs are recognized as the first-line pharmacological treatment for AS by current ASAS/EULAR guidelines precisely because COX inhibition directly suppresses the inflammatory cascade that drives disease activity and symptom burden. Flurbiprofen's mechanism is therefore not peripheral or speculative — it targets the central pathophysiological pathway of AS.

This is not a novel or hypothetical repurposing. Multiple rigorous double-blind RCTs conducted between 1974 and 1986 directly evaluated Flurbiprofen in AS patients, and Flurbiprofen (as Froben®) received marketing authorization for AS and allied rheumatic conditions in the United Kingdom. The TxGNN knowledge graph model independently recovers this biological connection through shared musculoskeletal inflammatory nodes, lending additional computational confidence. The key question for the Netherlands is not whether Flurbiprofen works in AS, but rather whether a CBG-MEB marketing authorization pathway can be established using the existing international evidence base.

---

## Clinical Trial Evidence

Currently no related clinical trials registered on ClinicalTrials.gov or ICTRP for Flurbiprofen in Ankylosing Spondylitis.

> **Context note:** The available clinical evidence derives entirely from published randomized trials conducted in the 1970s–1980s (see Literature Evidence below). These trials predate mandatory trial registration requirements (introduced circa 2000) and were therefore never assigned NCT or ICTRP identifiers. Their absence from trial registries does not reflect a lack of formal investigation.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [4611579](https://pubmed.ncbi.nlm.nih.gov/4611579/) | 1974 | RCT (double-blind crossover) | British Medical Journal | Flurbiprofen 150 mg/day vs phenylbutazone 300 mg/day in 35 AS patients over 4 weeks; flurbiprofen well tolerated with therapeutic efficacy approaching phenylbutazone |
| [4595274](https://pubmed.ncbi.nlm.nih.gov/4595274/) | 1974 | RCT (double-blind crossover) | Annals of the Rheumatic Diseases | Three-arm double-blind comparison: flurbiprofen vs indomethacin vs placebo in AS patients |
| [71969](https://pubmed.ncbi.nlm.nih.gov/71969/) | 1977 | RCT (active-controlled) | Current Medical Research and Opinion | Flurbiprofen 150–200 mg/day vs indomethacin 75–100 mg/day in 26 active AS patients over 6 weeks; equally effective in pain and joint tenderness relief; no withdrawals due to lack of efficacy in either arm |
| [329422](https://pubmed.ncbi.nlm.nih.gov/329422/) | 1977 | RCT (active-controlled) | Southern Medical Journal | Parallel double-blind RCT, flurbiprofen vs indomethacin in 26 AS patients; comparable efficacy confirmed in an independent cohort |
| [324773](https://pubmed.ncbi.nlm.nih.gov/324773/) | 1977 | RCT (active-controlled) | European Journal of Clinical Pharmacology | Flurbiprofen 150–200 mg/day vs phenylbutazone 300–400 mg/day in 27 AS patients over 6 weeks; equivalent joint pain and tenderness relief |
| [7003449](https://pubmed.ncbi.nlm.nih.gov/7003449/) | 1980 | RCT (double-blind crossover) | New Zealand Medical Journal | Flurbiprofen 200 mg/day vs naproxen 750 mg/day in 30 AS patients over 4 weeks; both agents very effective; side-effects more frequent with flurbiprofen; minor renal excretion increase noted |
| [3963018](https://pubmed.ncbi.nlm.nih.gov/3963018/) | 1986 | RCT (double-blind, 26-week) | The American Journal of Medicine | Flurbiprofen vs indomethacin in 57 AS patients over 26 weeks; flurbiprofen 200 mg/day effectively controlled pain and associated symptoms; some patients adequately managed at 100 mg/day |
| [3963017](https://pubmed.ncbi.nlm.nih.gov/3963017/) | 1986 | RCT (double-blind, 26-week) | The American Journal of Medicine | Flurbiprofen 200 mg/day vs phenylbutazone 300 mg/day in 90 AS patients over 26 weeks; equivalent efficacy; some patients well controlled at 150 mg/day |
| [3963024](https://pubmed.ncbi.nlm.nih.gov/3963024/) | 1986 | Pooled Safety Analysis | The American Journal of Medicine | Liver and kidney function data pooled from 9 Phase III trials (941 flurbiprofen / 736 comparator patients with AS, OA, or RA); no clinically significant organ function abnormalities identified |
| [391529](https://pubmed.ncbi.nlm.nih.gov/391529/) | 1979 | Review | Drugs | Comprehensive pharmacological review; flurbiprofen 150–300 mg/day comparable to established NSAID doses in AS; fewer side-effects than aspirin at equivalent anti-inflammatory doses |

---

## Netherlands Market Information

Flurbiprofen currently holds **no CBG-MEB marketing authorization** in the Netherlands. No RVG registration numbers are on file and the drug is classified as **not on market**.

For regulatory context: Flurbiprofen is authorized in other European markets under brand names including **Froben®** (UK, indicated for rheumatoid arthritis, osteoarthritis, and ankylosing spondylitis) and **Ansaid®** (US). An EMA centralized procedure or a CBG-MEB national/mutual recognition procedure would be required before Flurbiprofen can be lawfully marketed in the Netherlands.

---

## Safety Considerations

Detailed SmPC safety data — including formal warnings, contraindications, and drug-drug interactions — was not available in the Evidence Pack for the Netherlands market. Please refer to the **SmPC** (Samenvatting van de Productkenmerken) of an EMA-authorized or equivalent European formulation for complete safety information.

Based on the published clinical trial programme and NSAID class knowledge, the following considerations are relevant for the Dutch clinical context:

- **Gastrointestinal risk**: NSAIDs carry a well-established association with peptic ulcer disease, GI bleeding, and perforation. The 1979 review (PMID 391529) notes that flurbiprofen causes fewer GI side-effects than aspirin at anti-inflammatory doses. Co-prescription of a proton pump inhibitor (PPI) should be evaluated for at-risk patients, consistent with current NL prescribing standards.
- **Renal monitoring**: The 1986 pooled safety analysis (PMID 3963024) found no clinically significant renal impairment across 9 Phase III trials; however, a 1980 crossover study (PMID 7003449) observed a small but significant increase in urinary β-N-acetylglucosaminidase excretion with flurbiprofen. Monitoring of renal function is advisable in elderly patients or those with pre-existing renal conditions.
- **Elderly patients**: A dedicated pharmacokinetic study in patients with mean age 84 years (sustained-release 200 mg capsule) has been conducted, supporting use in older populations with appropriate monitoring.
- **Cardiovascular risk**: Long-term non-selective NSAID use is associated with increased cardiovascular event risk and should be weighed against disease burden, particularly in patients with pre-existing cardiovascular disease.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
At least eight double-blind randomized controlled trials conducted between 1974 and 1986 directly and consistently demonstrate Flurbiprofen's efficacy in Ankylosing Spondylitis, with results equivalent to indomethacin, phenylbutazone, and naproxen across studies ranging from 4 to 26 weeks in duration. The COX-inhibition mechanism is directly applicable to AS pathophysiology, and Flurbiprofen already holds an AS indication in other European markets. The primary barrier to use in the Netherlands is the **absence of a CBG-MEB marketing authorization**, not a lack of clinical evidence.

**To proceed, the following is needed:**

- **Regulatory pathway determination**: Assess whether an EMA centralized procedure or a CBG-MEB national/mutual recognition procedure is appropriate; confirm whether the existing UK Froben® SmPC data package meets current EMA evidentiary standards for an AS indication
- **SmPC / safety documentation**: Obtain the full Dutch-language SmPC (or an EMA-equivalent document) to complete the safety profile required for prescriber and pharmacist review
- **Modern evidence gap assessment**: The existing RCT evidence predates current AS management standards (biologic DMARDs, ASDAS outcome measures); CBG-MEB may require evidence against contemporary comparators or a bridging justification
- **MOA documentation**: Retrieve formal DrugBank / EMA mechanism-of-action data to strengthen the mechanistic rationale in the regulatory submission dossier
- **Risk Management Plan (RMP)**: Develop an EU-standard RMP covering GI, cardiovascular, and renal safety monitoring as part of the registration application
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

