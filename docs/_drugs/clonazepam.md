---
layout: default
title: Clonazepam
parent: 僅模型預測 (L5)
nav_order: 45
evidence_level: L5
indication_count: 3
---

# Clonazepam
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

The txgnn-pipeline skill confirms this is within the NlTxGNN (Netherlands) deployment scope. The report generation instructions are fully specified in the system prompt. I'll now generate the report.

---

# Clonazepam: From Epilepsy & Panic Disorder to Restless Legs Syndrome

## One-Sentence Summary

Clonazepam is a long-acting benzodiazepine widely used clinically for epileptic seizure disorders and panic disorder, though no CBG-MEB marketing authorization is currently on file in the Netherlands.
The TxGNN model predicts it may be effective for **Restless Legs Syndrome (RLS)**,
with **0 registered clinical trials** and **20 publications** currently supporting this direction — including a Cochrane Systematic Review, a 2025 AASM Clinical Practice Guideline, and a dedicated historical overview of clonazepam's role in RLS.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No CBG-MEB authorization on file; clinically established for epilepsy and panic disorder |
| Predicted New Indication | Restless Legs Syndrome (RLS) |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L3 |
| NL Market Status | Not Registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, clonazepam belongs to the **benzodiazepine class** and acts as a positive allosteric modulator of GABA-A receptors. Its efficacy in seizure suppression and panic disorder has been established across decades of clinical practice, and mechanistically this GABAergic action may be applicable to Restless Legs Syndrome.

Restless Legs Syndrome is a sensorimotor disorder defined by an irresistible urge to move the legs — particularly at rest and at night — often accompanied by uncomfortable paresthesias and periodic limb movements during sleep (PLMS). While the primary pathophysiology of RLS is dopaminergic, nocturnal cortical hyperarousal and spinal motor neuron over-excitability are recognised contributing factors. Clonazepam's GABA-A–mediated neuronal hyperpolarization can dampen this cortical hyperarousal and suppress PLMS, providing symptomatic relief through an **adjunctive, non-dopaminergic mechanism** rather than addressing the core dopamine pathway.

Clinical evidence corroborates this mechanistic rationale. A 2024 historical review (PMID 38708125) identified 17 articles on clonazepam use specifically in RLS, and a survey of 16,694 RLS patients found approximately **25% were treated with benzodiazepines**. The 1984 randomised double-blind crossover trial (PMID 6380197) demonstrated significant improvement in subjective sleep quality and leg dysaesthesia versus placebo. The 2017 Cochrane Systematic Review and the 2025 AASM Clinical Practice Guideline both acknowledge clonazepam within the RLS treatment landscape — positioning it as an adjunct option rather than first-line therapy (which remains dopamine agonists and alpha-2-delta ligands).

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Clonazepam in Restless Legs Syndrome.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [28319266](https://pubmed.ncbi.nlm.nih.gov/28319266/) | 2017 | Cochrane Systematic Review | Cochrane Database Syst Rev | Systematic review of benzodiazepines (including clonazepam) for RLS; acknowledges widespread clinical use despite limited RCT evidence; highlights the evidence gap |
| [39324694](https://pubmed.ncbi.nlm.nih.gov/39324694/) | 2025 | Clinical Practice Guideline | J Clin Sleep Med | AASM clinical practice guideline for treatment of RLS and PLMD in adults and paediatric patients; provides authoritative therapeutic framework |
| [38708125](https://pubmed.ncbi.nlm.nih.gov/38708125/) | 2024 | Narrative Review | Tremor Other Hyperkinetic Mov | Historical overview of benzodiazepines — particularly clonazepam — in RLS/PLMS; identified 17 relevant articles; ~25% of 16,694 surveyed RLS patients received benzodiazepines |
| [36692194](https://pubmed.ncbi.nlm.nih.gov/36692194/) | 2023 | Systematic Review & Meta-analysis | J Clin Sleep Med | Pharmacological responsiveness of PLMS in RLS; meta-analysis quantifying efficacy of drug categories including benzodiazepines in suppressing periodic limb movements |
| [31942156](https://pubmed.ncbi.nlm.nih.gov/31942156/) | 2019 | RCT | J Mid-Life Health | Prospective open-label randomised study comparing clonazepam vs nortriptyline in women over 40 with RLS; directly evaluates clonazepam efficacy on RLS frequency and severity |
| [11313161](https://pubmed.ncbi.nlm.nih.gov/11313161/) | 2001 | Placebo-Controlled Study | Eur Neuropsychopharmacol | Placebo-controlled sleep laboratory study of 1 mg clonazepam measuring objective and subjective sleep quality in RLS/PLMD patients; demonstrates acute polysomnographic effects |
| [6380197](https://pubmed.ncbi.nlm.nih.gov/6380197/) | 1984 | RCT | Acta Neurol Scand | Randomised double-blind crossover trial vs placebo in 6 RLS patients; significant improvement in sleep quality and leg dysaesthesia; earliest controlled evidence for clonazepam in RLS |
| [18925578](https://pubmed.ncbi.nlm.nih.gov/18925578/) | 2008 | Evidence-Based Review | Movement Disorders | MDS task force evidence-based review of RLS treatments; classifies therapeutic efficacy by drug class including benzodiazepines |
| [24363103](https://pubmed.ncbi.nlm.nih.gov/24363103/) | 2014 | Review | Neurotherapeutics | Overview of evolving RLS treatment landscape; discusses role of benzodiazepines alongside first-line dopaminergic agents and anticonvulsants |
| [17876423](https://pubmed.ncbi.nlm.nih.gov/17876423/) | 2007 | Expert Consensus | Arq Neuropsiquiatr | Brazilian RLS Study Group consensus on diagnosis and management; discusses therapeutic evidence hierarchy including clonazepam as a secondary option |

---

## Netherlands Market Information

Clonazepam currently holds **no CBG-MEB marketing authorizations** in the Netherlands based on available data (0 RVG numbers on file). There are no registered products to list.

> If prescribers are considering off-label use, they should consult the applicable EMA-level SmPC (e.g., for Rivotril or equivalent centrally authorised products) and follow the relevant Dutch off-label prescribing framework under the Geneesmiddelenwet.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Clonazepam has a mechanistically plausible and historically documented role in RLS — supported by a Cochrane review, an AASM guideline, and a small placebo-controlled RCT — however the overall evidence base is characterised by small sample sizes, older study dates, and an absence of active clinical trials. The drug is furthermore not registered with CBG-MEB, and complete safety data (key warnings, contraindications, DDI profile) could not be retrieved, making a full risk-benefit assessment impossible at this stage.

**To proceed, the following is needed:**

- **Regulatory clarification**: Verify whether clonazepam (e.g., as Rivotril) holds any current CBG-MEB or EMA centrally authorised status; resolve the apparent data gap in the regulatory pipeline
- **Full SmPC review**: Retrieve and analyse the SmPC for clonazepam to complete S1 safety screening — specifically regarding dependence risk, CNS depression, use in elderly, and respiratory insufficiency (standard benzodiazepine class concerns)
- **DDI profile**: Obtain drug-drug interaction data to assess safety in the polypharmacy context typical of RLS patients (who may also be on dopamine agonists or iron supplements)
- **MOA documentation**: Retrieve full mechanism of action data from DrugBank (DB01068) to complete the mechanistic link analysis
- **Guideline alignment**: Assess whether current Dutch/EU RLS treatment guidelines (e.g., EAN, EFNS) formally include clonazepam and under what conditions
- **Prospective evidence**: Commission or identify a prospective controlled study in an EU/NL RLS patient cohort before any formal repurposing recommendation can be issued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

