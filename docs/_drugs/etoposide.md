---
layout: default
title: Etoposide
parent: 僅模型預測 (L5)
nav_order: 63
evidence_level: L5
indication_count: 10
---

# Etoposide
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

Using the `txgnn-pipeline` skill to guide report generation for the Netherlands deployment context.

---

# Etoposide: From Germ Cell Tumours and Small Cell Lung Cancer to Well-Differentiated Fetal Adenocarcinoma of the Lung

## One-Sentence Summary

Etoposide (VP-16) is a classic topoisomerase II inhibitor, established globally as a cornerstone chemotherapy agent for germ cell tumours, small cell lung cancer, and lymphomas — although it holds no current CBG-MEB marketing authorisation in the Netherlands.
The TxGNN model predicts it may be effective for **well-differentiated fetal adenocarcinoma of the lung (WDFA)**,
with **no registered clinical trials** and **1 publication** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Germ cell tumours, small cell lung cancer, lymphomas (globally recognised; not registered in the Netherlands) |
| Predicted New Indication | Well-differentiated fetal adenocarcinoma of the lung |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| NL Market Status | Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Etoposide is a semisynthetic derivative of podophyllotoxin that inhibits topoisomerase II alpha (TOP2A), an enzyme essential for DNA replication and transcription in rapidly proliferating cells. By stabilising the TOP2A–DNA cleavage complex, etoposide induces irreversible DNA double-strand breaks and triggers apoptosis. This mechanism is particularly effective in tumours with high proliferation indices and elevated TOP2A expression.

Well-differentiated fetal adenocarcinoma of the lung (WDFA) is the monophasic, low-grade variant of pulmonary blastoma, characterised by glandular structures that closely resemble the pseudoglandular stage of fetal lung development (approximately 10–16 weeks). The tumour cells are glycogen-rich and typically harbour activating β-catenin mutations. As a rare subtype of pulmonary blastoma — a highly proliferative, poorly understood malignancy — WDFA would be expected to express TOP2A at levels sufficient to confer sensitivity to etoposide-based regimens.

The mechanistic extrapolation is supported indirectly by case reports of the closely related classic biphasic pulmonary blastoma (CBPB) responding to cisplatin/etoposide and ICE (ifosfamide, carboplatin, etoposide) chemotherapy. WDFA constitutes the adenocarcinomatous component of CBPB, and its shared embryonic lung histology makes the biochemical rationale for TOP2A inhibition plausible. However, no direct clinical trial or prospective observational study has evaluated etoposide specifically in WDFA, and the TxGNN prediction is primarily driven by knowledge-graph connectivity between etoposide's TOP2A inhibitor node and the pulmonary blastoma disease cluster.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33107372](https://pubmed.ncbi.nlm.nih.gov/33107372/) | 2020 | Case Report | The Journal of International Medical Research | Classic biphasic pulmonary blastoma (which contains a WDFA component): patient underwent resection followed by nedaplatin + paclitaxel adjuvant chemotherapy; upon recurrence, published literature supporting etoposide-containing regimens was reviewed. No standard treatment guidelines exist due to tumour rarity. |

---

## Netherlands Market Information

Etoposide holds no CBG-MEB marketing authorisations in the Netherlands. No RVG numbers are currently registered.

> Etoposide is widely available internationally — EMA-centralised authorisations exist for combination products containing etoposide, and standalone etoposide formulations are registered in multiple EU member states. For any clinical application in the Netherlands, a compassionate use pathway, hospital preparation exemption, or Article 3(1) national licensing route under CBG-MEB would need to be explored prior to use.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic (Epipodophyllotoxin class / Topoisomerase II inhibitor) |
| Myelosuppression Risk | High — leucopenia is the primary dose-limiting toxicity; nadir typically at days 10–14; thrombocytopenia also common |
| Emetogenicity Classification | Low to moderate (IV route: low; oral route: moderate) |
| Monitoring Items | Full blood count (CBC) at baseline and before each cycle; liver function tests (LFTs); renal function (dose reduction required for impaired clearance); temperature monitoring for febrile neutropenia |
| Handling Protection | Special cytotoxic handling required: PPE (gloves, gown, eye protection), closed-system drug transfer devices (CSTDs), disposal per hazardous waste regulations |

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics / Samenvatting van de Productkenmerken) for full safety information, as no Dutch SmPC data is currently available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a very high prediction score (99.94%), the clinical evidence base for etoposide in well-differentiated fetal adenocarcinoma of the lung is at L4 — limited to mechanistic inference and a single tangentially related case report involving the parent tumour type (biphasic pulmonary blastoma). WDFA is an exceptionally rare tumour with no established chemotherapy guidelines, no dedicated clinical trials, and no CBG-MEB registration for etoposide in the Netherlands.

**To proceed, the following is needed:**

- **Evidence review:** Systematic identification of all published WDFA case reports and series to determine whether any patient received an etoposide-containing regimen and what outcomes were observed
- **MOA documentation:** Retrieval of formal mechanism of action data from DrugBank (DB00773) to complete the pharmacological rationale section
- **Safety data:** Download and parse the relevant SmPC/PIL to establish contraindications, warnings, and clinically significant drug interactions for the Dutch prescribing context
- **Regulatory pathway assessment:** Evaluation of CBG-MEB routes for hospital use or compassionate access (Article 3(1) national licensing, hospital formula, or named-patient import)
- **Expert consultation:** Referral to a rare lung tumour multidisciplinary team (pulmonary oncology, pathology) before any clinical application is considered

> ⚠️ This report is for research reference only and does not constitute medical advice. All repurposing candidates require prospective clinical validation before therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

