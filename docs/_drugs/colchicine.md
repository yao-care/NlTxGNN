---
layout: default
title: Colchicine
parent: 僅模型預測 (L5)
nav_order: 47
evidence_level: L5
indication_count: 3
---

# Colchicine
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

以下是根據 Evidence Pack 生成的完整評估報告：

---

# Colchicine: From Gout to Plasmodium Falciparum Malaria

## One-Sentence Summary

Colchicine is a plant-derived alkaloid with a long history of use in gout and autoinflammatory conditions — though no Netherlands marketing authorization is currently registered.
The TxGNN model predicts it may be effective against **Plasmodium Falciparum Malaria**,
with **0 clinical trials** and **6 mechanistic publications** currently supporting this direction — all based on analogous compounds rather than Colchicine itself.

> **Note:** The second-ranked TxGNN prediction — **Familial Mediterranean Fever (FMF)** — carries substantially stronger evidence (L1, 1 clinical trial, 20 publications) and a recommendation of *Proceed with Guardrails*. Clinicians and formulary reviewers may wish to prioritise that indication for further evaluation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not specified in NL regulatory data (established historical use: Gout, Familial Mediterranean Fever) |
| Predicted New Indication | Plasmodium Falciparum Malaria |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L4 |
| NL Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Colchicine binds to β-tubulin dimers and inhibits microtubule polymerisation. This disrupts mitotic spindle formation (blocking cell division) and impairs neutrophil chemotaxis and degranulation. These properties underpin its efficacy in gout flares and autoinflammatory conditions such as FMF and pericarditis.

*Plasmodium falciparum* possesses its own β-tubulin (pfβ-tubulin), which is an essential structural component throughout the parasite's intraerythrocytic life cycle. Several tubulin-binding compounds — including tubulozoles and curcumin — have demonstrated activity against *P. falciparum* in vitro, providing the biological rationale for TxGNN's prediction. Colchicine, as a prototypical tubulin-binding agent, is algorithmically grouped with this mechanistic class.

However, the mechanistic parallel has important limitations. Plasmodial β-tubulin differs from mammalian tubulin at functionally important residues, raising questions about selectivity and therapeutic window. Critically, **none of the identified literature studies Colchicine directly** — all six publications concern structurally distinct compounds. Colchicine's extremely narrow therapeutic index (therapeutic and toxic doses overlap significantly) further complicates any infectious disease application. The current prediction is therefore best characterised as a **mechanistic analogy hypothesis** rather than evidence-based repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [2670249](https://pubmed.ncbi.nlm.nih.gov/2670249/) | 1989 | In vitro screening | Cell Biology International Reports | Nine tubulin-binding compounds tested against *P. falciparum* in vitro; plasmodial tubulin differs from mammalian protein at molecular level; tubulozole-T showed promise |
| [2221861](https://pubmed.ncbi.nlm.nih.gov/2221861/) | 1990 | In vitro mechanistic | Antimicrobial Agents and Chemotherapy | Tubulozoles inhibit protein biosynthesis in *P. falciparum*; Colcemid (a tubulin-binding agent related to Colchicine) showed a similar inhibitory profile |
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In vitro mechanistic | PLoS ONE | Curcumin binds tubulin and disrupts *P. falciparum* microtubule structure; supports the concept that tubulin-targeted agents can affect the malaria parasite |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | In vitro mechanistic | Molecular and Cellular Biology | *pfmdr1*-encoded protein Pgh1 expressed in CHO cells increases chloroquine susceptibility; mechanistic context for *P. falciparum* drug resistance |
| [6362934](https://pubmed.ncbi.nlm.nih.gov/6362934/) | 1984 | Clinical observation | Clinical and Experimental Immunology | 82% of acute malaria patients showed antibodies to intermediate filaments; suggests cytoskeletal involvement in host–parasite interaction |

> **Caution on relevance:** No publication directly investigates Colchicine against *P. falciparum*. All studies concern compounds with overlapping but distinct mechanisms.

---

## Netherlands Market Information

Colchicine holds no marketing authorization (RVG number) issued by the CBG-MEB (College ter Beoordeling van Geneesmiddelen). There are no registered products to list.

> For prescribers in the Netherlands: Colchicine may be available via hospital pharmacy compounding or importation procedures under Article 3(1) of Directive 2001/83/EC. Clinicians should consult the relevant SmPC from an EMA-approved source (e.g., for the EU-authorized product *Colchicine Rottapharm*, if applicable) or contact CBG-MEB for current regulatory status.

---

## Safety Considerations

Safety data (key warnings, contraindications, and drug–drug interaction records) is not available in the current Evidence Pack.

> Please refer to the SmPC (Summary of Product Characteristics — *Samenvatting van de Productkenmerken*) for complete safety information.

**Known clinical safety signals of note** (based on established pharmacological knowledge, to be verified against the SmPC):

- **Narrow therapeutic index**: The gap between therapeutic and toxic doses is small; overdose can be fatal.
- **Renal and hepatic impairment**: Colchicine is renally excreted and hepatically metabolised (CYP3A4, P-glycoprotein); dose reduction is required in organ impairment.
- **Drug interactions**: Strong CYP3A4 inhibitors (e.g., clarithromycin, cyclosporine) can markedly increase Colchicine plasma levels and toxicity risk.
- **Haematological toxicity**: Bone marrow suppression, leucopenia, and agranulocytosis reported with prolonged use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model identifies a mechanistically plausible tubulin-disruption pathway applicable to *P. falciparum*, but all supporting evidence derives from structurally distinct compounds — not Colchicine itself. With zero clinical trials, no direct in vitro *P. falciparum* data, a narrow therapeutic index, and no Netherlands regulatory foothold, there is insufficient evidence to advance this indication.

**To proceed, the following is needed:**

- **Direct preclinical validation**: In vitro susceptibility testing of Colchicine against *P. falciparum* strains (e.g., 3D7, Dd2), including IC₅₀ determination
- **Selectivity assessment**: Comparative binding affinity of Colchicine to pfβ-tubulin vs. human β-tubulin to assess selective toxicity
- **Pharmacokinetic modelling**: Determine whether therapeutic concentrations in erythrocytes can be achieved without systemic toxicity
- **Complete MOA data**: Obtain full mechanism of action data via DrugBank API (currently listed as a data gap — DG002)
- **Safety profile from SmPC**: Download and parse the applicable SmPC to complete the safety tier (DG001)
- **Consideration of FMF indication**: The rank-2 prediction (Familial Mediterranean Fever, autosomal dominant) has L1 evidence and a *Proceed with Guardrails* recommendation — this represents a more actionable near-term priority for the Netherlands clinical context

---
*Report generated: 2026-05-01 | Data cut-off: 2026-05-01 | Evidence Pack v4 | Candidate ID: TW-DB01394-multi*
*This report is intended for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

