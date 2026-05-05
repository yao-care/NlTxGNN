---
layout: default
title: Piroxicam
parent: 僅模型預測 (L5)
nav_order: 106
evidence_level: L5
indication_count: 10
---

# Piroxicam
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

# Piroxicam: From Adult Inflammatory Arthritis to Juvenile Idiopathic Arthritis

## One-Sentence Summary

Piroxicam is a well-established NSAID (non-steroidal anti-inflammatory drug) of the oxicam class, globally used for rheumatoid arthritis, osteoarthritis, and related inflammatory conditions, though it currently holds no marketing authorization from the CBG-MEB in the Netherlands.
The TxGNN model predicts it may be effective for **Juvenile Idiopathic Arthritis (JIA)**, with **0 registered clinical trials** but **13 publications** — including 2 controlled trials and 2 systematic reviews/network meta-analyses — providing substantive literature support for this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, and inflammatory conditions (globally established NSAID; no CBG-MEB authorization in the Netherlands) |
| Predicted New Indication | Juvenile Idiopathic Arthritis (JIA) |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L2 |
| NL Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on prediction selection:** The TxGNN model's top-ranked predictions (ranks 1–8) pointed to rare congenital skeletal dysplasias (e.g., colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachydactyly-syndactyly syndrome) with TxGNN scores near 99.99%. These were assessed as **L5 / Hold** — no clinical trials, no literature, and no credible pharmacological mechanism. The high scores likely reflect topological similarity of skeletal disease nodes in the knowledge graph rather than genuine drug-disease relevance. JIA (rank 10, score 99.93%) was selected for this report as the highest-evidence, most clinically actionable prediction.

---

## Why is This Prediction Reasonable?

Piroxicam is a non-selective cyclooxygenase inhibitor (COX-1 and COX-2) of the oxicam chemical class. By blocking COX enzymes, it prevents the conversion of arachidonic acid to prostaglandins — particularly PGE₂ — thereby reducing inflammation, pain sensitization, and fever. Although this analysis cycle's DrugBank query did not return a formal MOA entry, Piroxicam's pharmacology is extensively described in the medical literature and is confirmed by the clinical evidence retrieved for JIA in this Evidence Pack.

Juvenile Idiopathic Arthritis is a heterogeneous group of chronic autoimmune inflammatory arthritides affecting children under 16 years of age, and is the most common rheumatic disease in childhood. PGE₂ plays a central role in driving synovial inflammation, joint swelling, and pain sensitization in JIA. Because Piroxicam directly suppresses this prostaglandin pathway through COX inhibition, NSAIDs — including Piroxicam — are recommended as first-line symptomatic treatment in JIA per ACR and EULAR guidelines. The mechanistic rationale is direct and well-grounded.

Piroxicam has been directly studied in paediatric inflammatory arthritis. A 1986 multicentre double-blind crossover RCT (PMID 3510686) compared Piroxicam to Naproxen in 47 children with seronegative juvenile chronic arthritis over 8 weeks, and a 1987 randomised clinical trial (PMID 2957205) enrolled 26 patients aged 3–25 years and reported significant reductions in painful and swollen joint counts. Two more recent systematic reviews and network meta-analyses (2021 and 2024) have comprehensively compared NSAIDs in JIA, situating Piroxicam within the broader treatment landscape. Paediatric pharmacokinetic data for Piroxicam in children with rheumatic disease are also available (PMID 1782984), supporting evidence-based dose guidance.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3510686](https://pubmed.ncbi.nlm.nih.gov/3510686/) | 1986 | Multicentre RCT | British Journal of Rheumatology | Double-blind crossover RCT of piroxicam vs naproxen in 47 children (aged 5–16) with seronegative JCA; no significant difference between treatments over 8 weeks; discusses key challenges of NSAID trials in childhood arthritis |
| [2957205](https://pubmed.ncbi.nlm.nih.gov/2957205/) | 1987 | Clinical Trial (RCT) | European Journal of Rheumatology and Inflammation | Piroxicam vs naproxen in 26 JRA patients aged 3–25 years; significant reductions in painful and swollen joint counts (p<0.05); supports safety and efficacy in paediatric patients |
| [38680254](https://pubmed.ncbi.nlm.nih.gov/38680254/) | 2024 | Systematic Review / NMA | World Journal of Clinical Cases | Network meta-analysis comparing multiple NSAIDs for JIA; aims to identify the optimal NSAID in a condition lacking consensus treatment |
| [33632948](https://pubmed.ncbi.nlm.nih.gov/33632948/) | 2021 | Systematic Review / NMA | Indian Pediatrics | Comparative efficacy and safety of 9 NSAIDs in JIA via network meta-analysis; provides class-level ranking of NSAID options in paediatric arthritis |
| [9890680](https://pubmed.ncbi.nlm.nih.gov/9890680/) | 1998 | Safety Analysis | Clinical Rheumatology | Long-term toxicity of antirheumatic drugs in 117 children (155 NSAID exposures, mean 8.6-year follow-up); key safety reference for paediatric NSAID use |
| [1782984](https://pubmed.ncbi.nlm.nih.gov/1782984/) | 1991 | PK Study | European Journal of Clinical Pharmacology | Steady-state pharmacokinetics of piroxicam in 10 children with RA (aged 7–16 years, 0.4 mg/kg/day); mean half-life 32.6 h; informs paediatric dosing |
| [7797387](https://pubmed.ncbi.nlm.nih.gov/7797387/) | 1994 | Cohort Study | International Ophthalmology | Frequency (56%) and outcomes of chronic iridocyclitis in ANA-positive pauciarticular JCA; highlights need for ophthalmological monitoring during JIA management |
| [2185374](https://pubmed.ncbi.nlm.nih.gov/2185374/) | 1990 | Review | Kinderarztliche Praxis | Review of drug therapy for juvenile chronic arthritis; explicitly introduces piroxicam as a new therapeutic agent in this population |
| [21175420](https://pubmed.ncbi.nlm.nih.gov/21175420/) | 2010 | Review | Critical Reviews in Therapeutic Drug Carrier Systems | Reviews NSAID delivery systems for arthritis types including JIA; discusses piroxicam among agents under development for improved drug delivery |
| [6753142](https://pubmed.ncbi.nlm.nih.gov/6753142/) | 1982 | Review | Schweizerische Medizinische Wochenschrift | Rational NSAID prescribing policy for inflammatory arthritis; safety-first approach positioning propionic acid derivatives and newer agents (including piroxicam) as initial therapy |

---

## Netherlands Market Information

Piroxicam currently holds **no marketing authorization** from the CBG-MEB (College ter Beoordeling van Geneesmiddelen) in the Netherlands. There are no registered RVG numbers. Any use in the Netherlands would require one of the following pathways:

- **Off-label prescription** with documented clinical rationale and informed consent
- **Named patient import** on a case-by-case basis
- **New marketing authorization application** to the CBG-MEB or via the EMA centralized procedure

---

## Safety Considerations

Formal safety data (key warnings, contraindications, drug-drug interactions) were not available for Piroxicam in this analysis cycle. Please refer to the SmPC (Summary of Product Characteristics / Samenvatting van de Productkenmerken) of an authorized Piroxicam product — or the relevant EMA public assessment report — for complete safety guidance.

Based on evidence retrieved in the literature for paediatric use in JIA, the following safety considerations are particularly relevant:

- **Gastrointestinal risk**: Long-term NSAID use carries gastrointestinal adverse effects; co-administration of a proton pump inhibitor (PPI) is recommended
- **Renal monitoring**: Renal function should be monitored during chronic use, especially in children
- **Cardiovascular risk**: Prolonged NSAID therapy carries cardiovascular risk; treatment duration should be minimized where possible
- **Ocular monitoring**: JIA patients — particularly ANA-positive, pauciarticular subtype — require regular ophthalmological screening for chronic iridocyclitis regardless of NSAID choice (PMID 7797387)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Piroxicam has direct controlled clinical trial evidence in Juvenile Idiopathic Arthritis from two paediatric trials (including a 1986 multicentre double-blind RCT), supported by paediatric pharmacokinetic data and two recent systematic reviews/NMAs comparing NSAIDs in JIA. The mechanistic basis — COX-1/COX-2 inhibition reducing PGE₂-driven synovial inflammation — is well-established and directly applicable to JIA pathophysiology. The primary barriers are the absence of a current CBG-MEB marketing authorization in the Netherlands and the age of the pivotal clinical evidence (1980s), which predates modern paediatric regulatory standards.

**To proceed, the following is needed:**

- Retrieve the complete SmPC / EMA product documentation for Piroxicam to fill the current safety data gap (warnings, contraindications, known interactions — DG001)
- Retrieve formal MOA documentation from DrugBank to complete mechanistic analysis (DG002)
- Determine the regulatory pathway in the Netherlands: off-label use protocol versus marketing authorization application to CBG-MEB
- Develop a paediatric safety monitoring plan covering CBC, renal function, gastrointestinal symptoms, and hepatic function, with mandatory gastric protection (PPI co-prescription)
- Consult with a Dutch paediatric rheumatologist to confirm clinical appropriateness within local JIA treatment protocols and Dutch healthcare guidelines
- Evaluate whether more COX-2 selective NSAIDs with better-established paediatric safety profiles (e.g., naproxen, meloxicam) should be preferred first-line options before pursuing Piroxicam for this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

