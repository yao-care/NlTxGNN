---
layout: default
title: Alprazolam
parent: 僅模型預測 (L5)
nav_order: 22
evidence_level: L5
indication_count: 3
---

# Alprazolam
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

# Alprazolam: From Anxiety Disorders to Insomnia

## One-Sentence Summary

Alprazolam is a benzodiazepine widely approved globally for anxiety and panic disorder. The TxGNN model predicts it may be effective for **Insomnia**, with **7 clinical trials** and **18 publications** supporting this direction. A second prediction for **Agoraphobia** carries even stronger evidence (L1), with **2 clinical trials** and **19 publications** including multiple large-scale RCTs.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anxiety disorders, panic disorder (globally approved; no local license data in current dataset) |
| Predicted New Indication (Rank 1) | Insomnia (disease) |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L3 — Observational studies and comparative literature |
| Market Status | Not marketed (current dataset shows 0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

### Additional Predictions at a Glance

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|----------------------|-------------|----------------|----------------|
| 2 | Benign Paroxysmal Torticollis of Infancy | 99.61% | L5 — Model prediction only | Hold |
| 3 | Agoraphobia | 99.56% | L1 — Multiple completed RCTs | Proceed with Guardrails |

---

## Prediction 1: Insomnia

### Why is This Prediction Reasonable?

Alprazolam is a triazolobenzodiazepine that acts as a positive allosteric modulator (PAM) at GABA-A receptors. By enhancing inhibitory GABAergic neurotransmission in the central nervous system, it produces anxiolytic, sedative-hypnotic, and muscle-relaxant effects. The sedative properties of alprazolam are well documented and represent a pharmacologically expected extension of its primary mechanism of action.

The relationship between anxiety disorders (the original indication) and insomnia is well established: insomnia is one of the most common comorbid symptoms in anxiety, and the two conditions share overlapping neurobiological pathways involving GABAergic dysregulation. Alprazolam's ability to enhance GABA-mediated inhibition directly addresses the hyperarousal state implicated in both anxiety and insomnia.

However, an important caveat applies: despite the clear mechanistic rationale, modern clinical guidelines (including those from the European Sleep Research Society and the American Academy of Sleep Medicine) no longer recommend benzodiazepines as first-line treatment for insomnia. This is due to well-documented risks of tolerance, physical dependence, rebound insomnia, and cognitive impairment — particularly in elderly populations. Any repurposing consideration must weigh the mechanistic plausibility against these established safety concerns.

### Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|--------------|-------|--------|------------|--------------|
| [NCT00266409](https://clinicaltrials.gov/study/NCT00266409) | Phase 4 | Completed | 418 | Multicenter RCT comparing Niravam™ (alprazolam ODT) + SSRI/SNRI vs SSRI/SNRI alone for anxiety symptoms response time. Large completed trial provides indirect evidence on alprazolam's sedative-anxiolytic utility. |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Unknown | 1,400 | Prospective cohort study in Taiwan evaluating risk–benefit of hypnotics for sleep disorders in the elderly. Directly relevant to alprazolam use for insomnia; large sample size but observational design. |
| [NCT01584440](https://clinicaltrials.gov/study/NCT01584440) | Phase 2 | Completed | 220 | Double-blind, placebo-controlled RCT assessing AVP-923 for agitation in Alzheimer's; may contain comparative sleep/sedation data as secondary endpoints. |
| [NCT03327506](https://clinicaltrials.gov/study/NCT03327506) | Phase 4 | Unknown | 128 | Compared hypnosis vs alprazolam premedication for perioperative anxiety in gynecological surgery. Alprazolam used as active comparator; peripheral to chronic insomnia. |
| [NCT01893632](https://clinicaltrials.gov/study/NCT01893632) | Phase 2 | Terminated | 2 | Gabapentin treatment for benzodiazepine dependence. Terminated after enrolling only 2 patients. Highlights dependence risks but no efficacy data for insomnia. |
| [NCT04572750](https://clinicaltrials.gov/study/NCT04572750) | N/A | Completed | 170 | Patient self-management intervention promoting benzodiazepine cessation in Veterans. Underscores safety concerns (dependence, falls) rather than supporting insomnia efficacy. |
| [NCT01146600](https://clinicaltrials.gov/study/NCT01146600) | Phase 2 | Completed | 26 | Clarithromycin for hypersomnia — not relevant to alprazolam or insomnia treatment. |

**Summary**: No completed RCT directly tests alprazolam as a primary treatment for insomnia. The most relevant trial (NCT02648776, n=1,400) is observational. Several trials use alprazolam as a comparator or study benzodiazepine cessation, reflecting the clinical community's ambivalence about benzodiazepine use for sleep.

### Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [33403184](https://pubmed.ncbi.nlm.nih.gov/33403184/) | 2020 | Comparative Study | Cureus | Direct head-to-head comparison of alprazolam vs melatonin for sleep disturbances in hemodialysis patients. Directly relevant to insomnia treatment with alprazolam. |
| [39183410](https://pubmed.ncbi.nlm.nih.gov/39183410/) | 2024 | Clinical Study | Medicine | Integrative therapy (moxibustion + ear acupuncture + alprazolam) for coronary heart disease patients with insomnia. Alprazolam used as control arm; n=116. |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analysis | Acta Pharmaceutica | Meta-analysis of tranquilizer therapy in elderly patients with chronic non-communicable diseases. Evaluates dose, efficacy, safety, and adverse effects. |
| [37801512](https://pubmed.ncbi.nlm.nih.gov/37801512/) | 2023 | Preclinical | Aging | Proteomic analysis showing repeated alprazolam administration causes mitochondrial dysfunction and hippocampal memory impairment in mice. Safety signal. |
| [25532388](https://pubmed.ncbi.nlm.nih.gov/25532388/) | 2014 | Cross-sectional | China J Chinese Materia Medica | Real-world analysis of concurrent diseases and medicine use among insomnia patients (n=1,067). Documents alprazolam prescribing patterns. |
| [38363887](https://pubmed.ncbi.nlm.nih.gov/38363887/) | 2024 | Cross-sectional | Medicine | Insomnia among COVID-19 survivors; documents prevalence and influencing factors. Contextual relevance. |
| [35041261](https://pubmed.ncbi.nlm.nih.gov/35041261/) | 2022 | RCT | Brain and Behavior | Eszopiclone for sleep quality in elderly AD patients — alprazolam may serve as comparator class reference. |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opin Drug Metab Toxicol | Pharmacokinetics of anxiolytic drugs including alprazolam. Relevant for dosing and PK considerations. |
| [35493764](https://pubmed.ncbi.nlm.nih.gov/35493764/) | 2022 | Cohort | JHEP Reports | Deprescribing zolpidem reduces falls/fractures in cirrhosis patients — highlights safety risks of sedative-hypnotics in vulnerable populations. |
| [37984023](https://pubmed.ncbi.nlm.nih.gov/37984023/) | 2024 | Epidemiological | Value in Health Regional Issues | 10-year predictive model of benzodiazepine use trends and economic burden in Croatia. Documents long-term use risks. |

**Summary**: The literature provides moderate support for alprazolam's use in insomnia — primarily through comparative studies and real-world data rather than dedicated efficacy RCTs. Notably, several publications highlight safety concerns (dependence, memory impairment, falls), reflecting the broader clinical consensus against first-line benzodiazepine use for insomnia.

---

## Prediction 2: Benign Paroxysmal Torticollis of Infancy (BPTI)

### Why is This Prediction NOT Reasonable?

The mechanistic link is extremely weak. BPTI is considered a migraine variant or channelopathy involving vestibular dysfunction, potentially linked to CACNA1A gene mutations. While alprazolam's GABA-A modulation could theoretically provide muscle relaxation, the critical issues are:

1. **BPTI is a self-limiting infantile condition** that typically resolves spontaneously
2. **Benzodiazepines carry serious safety risks in infants**, including respiratory depression and developmental effects
3. **No clinical trials or literature** support this use whatsoever

**Evidence Level**: L5 — Model prediction only, zero supporting evidence.

**Decision: Hold** — This prediction should not be pursued. The risk–benefit profile is clearly unfavorable.

---

## Prediction 3: Agoraphobia

### Why is This Prediction Reasonable?

Agoraphobia — the fear and avoidance of situations where escape might be difficult — is closely related to panic disorder, for which alprazolam is already a globally approved treatment. The mechanistic rationale is strong: alprazolam's GABA-A PAM activity enhances inhibitory neurotransmission, reducing amygdala hyperactivation and attenuating the fear response and avoidance behavior characteristic of agoraphobia.

This is not a novel hypothesis. The landmark Cross-National Collaborative Panic Study, published in *Archives of General Psychiatry* (1988), demonstrated alprazolam's efficacy in panic disorder with agoraphobia in a large multicenter RCT (n=526). Multiple subsequent controlled trials have confirmed these findings. In many jurisdictions, alprazolam is already indicated for panic disorder with or without agoraphobia, making this less a "repurposing" and more a recognition of existing evidence.

### Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|--------------|-------|--------|------------|--------------|
| [NCT00634790](https://clinicaltrials.gov/study/NCT00634790) | Phase 4 | Terminated | 49 | Open-label study of Xanax XR (alprazolam extended-release) in adolescents with panic disorder ± agoraphobia. Directly tests alprazolam for the target indication. Terminated due to enrollment difficulties, not safety concerns. |
| [NCT01330472](https://clinicaltrials.gov/study/NCT01330472) | Phase 1 | Completed | 16 | Bioequivalence study of Xanax XR 3 mg tablets from two manufacturing sites. PK data only; no efficacy data. |

### Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [3282478](https://pubmed.ncbi.nlm.nih.gov/3282478/) | 1988 | Multicenter RCT | Arch Gen Psychiatry | Landmark Cross-National Collaborative Panic Study (n=526). Alprazolam significantly superior to placebo in agoraphobia with panic attacks and panic disorder. |
| [3282479](https://pubmed.ncbi.nlm.nih.gov/3282479/) | 1988 | Multicenter RCT | Arch Gen Psychiatry | Discontinuation effects in 126 patients: 97% of alprazolam patients worsened during taper. Documents dependence risk. |
| [2651490](https://pubmed.ncbi.nlm.nih.gov/2651490/) | 1989 | 3-arm RCT | J Clin Psychopharmacol | Alprazolam vs propranolol vs placebo (n=55). Results support efficacy of alprazolam but not propranolol for panic disorder with agoraphobia. |
| [8101126](https://pubmed.ncbi.nlm.nih.gov/8101126/) | 1993 | Controlled Study | Br J Psychiatry | Cross-national RCT (n=154): alprazolam 5 mg/day ± exposure for chronic panic disorder with agoraphobia. Alprazolam effective short-term, but gains lost at 6-month treatment-free follow-up. |
| [7802851](https://pubmed.ncbi.nlm.nih.gov/7802851/) | 1994 | Controlled Study | Br J Psychiatry | Safety and side-effect profile of alprazolam vs placebo in agoraphobia with panic disorder. Documents adverse effect profile. |
| [38014714](https://pubmed.ncbi.nlm.nih.gov/38014714/) | 2023 | Network Meta-analysis | Cochrane Database Syst Rev | Cochrane network meta-analysis of pharmacological treatments for panic disorder in adults. Highest-tier evidence synthesis. |
| [21869686](https://pubmed.ncbi.nlm.nih.gov/21869686/) | 2011 | Meta-analysis | J Clin Psychopharmacol | Meta-analysis of alprazolam vs other benzodiazepines for panic disorder (8 studies, n≥631). No significant differences in efficacy between alprazolam and other benzodiazepines. |
| [9259039](https://pubmed.ncbi.nlm.nih.gov/9259039/) | 1997 | Long-term Follow-up | Psychother Psychosom | 3.5-year follow-up after alprazolam/exposure treatment for agoraphobia/panic. Assesses durability of treatment gains. |
| [2859580](https://pubmed.ncbi.nlm.nih.gov/2859580/) | 1985 | Comparative Study | Psychiatr Clin North Am | Review of MAOIs and alprazolam efficacy in panic disorder and agoraphobia with clinical guidelines. |
| [7921716](https://pubmed.ncbi.nlm.nih.gov/7921716/) | 1994 | Controlled Study | Br J Psychiatry | Attribution of improvement to medication predicts relapse; patients attributing gains to alprazolam had worse outcomes after discontinuation. |

**Summary**: Agoraphobia has the strongest evidence base of all three predictions. Multiple large-scale, multicenter RCTs — including the seminal Ballenger et al. 1988 study (n=526) — and a 2023 Cochrane network meta-analysis confirm alprazolam's efficacy. This is effectively an already-validated indication in many regulatory jurisdictions.

---

## Market Information

The current evidence pack contains no marketing authorization data. The dataset reports **0 licenses** and a market status of "Not marketed" in the queried regulatory database. 

For reference, alprazolam (brand name Xanax) is widely authorized in the EU through national procedures. Practitioners should consult the CBG-MEB (College ter Beoordeling van Geneesmiddelen) database or the EMA for current Dutch marketing authorization status and approved SmPC.

---

## Safety Considerations

Detailed safety data (key warnings, contraindications, and drug–drug interactions) was not available in the current evidence pack. However, based on the well-established safety profile of benzodiazepines, the following risks are clinically significant for any repurposing consideration:

- **Dependence and withdrawal**: Alprazolam has high dependence potential, with documented withdrawal symptoms (rebound anxiety, seizures) even after short-term use
- **Cognitive impairment**: Repeated administration is associated with memory impairment and mitochondrial dysfunction (PMID [37801512](https://pubmed.ncbi.nlm.nih.gov/37801512/))
- **Falls and fractures**: Particularly in elderly populations, benzodiazepines are associated with increased fall and fracture risk
- **Respiratory depression**: Risk increases with concomitant opioid use or in patients with respiratory compromise
- **Rebound insomnia**: Paradoxically, benzodiazepine discontinuation can worsen insomnia

> For complete safety information, please refer to the SmPC (Summary of Product Characteristics / Samenvatting van de Productkenmerken).

---

## Conclusion and Next Steps

### Prediction 1: Insomnia

**Decision: Hold**

**Rationale:**
While the mechanistic rationale for alprazolam in insomnia is pharmacologically sound (GABA-A PAM → sedation), modern clinical guidelines explicitly recommend against benzodiazepines as first-line insomnia treatment due to dependence, tolerance, and rebound risks. No completed RCT directly validates this specific indication. The available evidence (L3) consists of observational studies and comparative real-world data. Given the availability of safer alternatives (e.g., CBT-I, melatonin receptor agonists, dual orexin receptor antagonists), pursuing this repurposing direction offers limited clinical value.

**To proceed, the following would be needed:**
- Head-to-head RCT comparing alprazolam to current first-line insomnia treatments
- Detailed safety monitoring plan addressing dependence and withdrawal
- Subpopulation analysis identifying patients who may benefit despite risks (e.g., insomnia refractory to first-line agents)
- Complete mechanism of action and drug–drug interaction data

---

### Prediction 2: Benign Paroxysmal Torticollis of Infancy

**Decision: Hold**

**Rationale:**
No evidence of any kind supports this indication. The target population (infants) represents an unacceptable safety risk for benzodiazepine exposure. This prediction should not be pursued.

---

### Prediction 3: Agoraphobia

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 2/3 RCTs (including the Cross-National Collaborative Panic Study, n=526) and a 2023 Cochrane network meta-analysis provide L1-level evidence supporting alprazolam's efficacy in panic disorder with agoraphobia. This indication is already approved in many jurisdictions, making it a strong repurposing candidate. However, dependence risk and relapse upon discontinuation remain significant concerns.

**To proceed, the following is needed:**
- Confirmation of current CBG-MEB marketing authorization status for alprazolam in the Netherlands
- Review of the approved SmPC to determine if agoraphobia is already covered under the panic disorder indication
- Safety monitoring plan with defined treatment duration limits and tapering protocols
- Cost-effectiveness analysis comparing alprazolam to SSRIs/SNRIs (current first-line treatments for agoraphobia)

---

*This report was generated on 2026-04-03 based on evidence collected through 2026-04-03. Results are for research purposes only and do not constitute medical advice. All drug repurposing candidates require clinical validation before application. Please consult the SmPC (Samenvatting van de Productkenmerken) and current CBG-MEB/EMA guidance for prescribing decisions.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

