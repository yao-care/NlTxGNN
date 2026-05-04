---
layout: default
title: Baclofen
parent: 僅模型預測 (L5)
nav_order: 29
evidence_level: L5
indication_count: 2
---

# Baclofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Baclofen: From Spasticity to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Baclofen is a GABA-B receptor agonist classically used in the treatment of spasticity associated with neurological conditions such as multiple sclerosis and spinal cord injury.
The TxGNN model predicts it may be effective for **Attention Deficit-Hyperactivity Disorder (ADHD)**, with a prediction score of **99.3%**.
However, current evidence supporting this indication is limited to **10 publications** — predominantly animal studies and indirect reviews — with **no registered clinical trials** specifically in ADHD, placing this at an early exploratory stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Spasticity (multiple sclerosis, spinal cord disease) — *Note: no NL authorizations retrieved; based on general pharmacological knowledge* |
| Predicted New Indication | Attention Deficit-Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.3% |
| Evidence Level | L4 (preclinical studies and mechanism studies only) |
| NL Market Status | No authorizations on record in this dataset — *please verify directly with CBG-MEB* |
| Number of Authorizations | 0 (as retrieved) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrievable for this Evidence Pack. Based on established pharmacological knowledge, Baclofen acts as a selective agonist at GABA-B receptors in the central nervous system. By activating these inhibitory receptors — particularly on dopaminergic neurons in the ventral tegmental area (VTA) — Baclofen can reduce dopamine release into downstream regions including the nucleus accumbens and prefrontal cortex. This dopaminergic modulation provides a theoretical basis for its predicted relevance in ADHD.

ADHD is characterised by dysregulation of dopaminergic and noradrenergic signalling in the prefrontal cortex, circuits responsible for executive function, attention, and impulse control. Since GABA-B activation can dampen excess dopamine activity, Baclofen could in principle attenuate hyperactive dopaminergic tone. Some support comes from studies using spontaneously hypertensive rats (a validated ADHD animal model), in which GABA-ergic agents including Baclofen produced measurable cortical EEG changes. Additionally, Tourette syndrome — which co-occurs with ADHD in a high proportion of cases — features Baclofen as an established off-label treatment for tic suppression, and several of the retrieved publications originate from this overlap.

Despite this mechanistic plausibility, the translational path from these observations to clinical ADHD benefit remains highly speculative. None of the retrieved literature directly evaluates Baclofen in patients with a primary ADHD diagnosis; references are indirect, routed through Tourette syndrome or rodent impulsivity models. The evidence base does not yet support advancing this candidate beyond early hypothesis generation.

---

## Clinical Trial Evidence

Currently no clinical trials related to Baclofen in ADHD are registered in ClinicalTrials.gov or ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [10342599](https://pubmed.ncbi.nlm.nih.gov/10342599/) | 1999 | Review | Journal of Child Neurology | Baclofen used in 450 Tourette patients to reduce tic severity via Yale Global Tic Severity Scale; primary outcome is tics, not ADHD, but ADHD comorbidity is prevalent in this population |
| [11393328](https://pubmed.ncbi.nlm.nih.gov/11393328/) | 2001 | Review | Paediatric Drugs | Overview of Tourette syndrome pharmacotherapy; Baclofen referenced as treatment for tics in the presence of ADHD comorbidity |
| [21300040](https://pubmed.ncbi.nlm.nih.gov/21300040/) | 2011 | Animal Study (EEG) | Brain Research | Neurotransmitter agonists including GABA-ergic agents tested in spontaneously hypertensive rats (ADHD model); EEG changes observed, providing indirect mechanistic signal |
| [24062084](https://pubmed.ncbi.nlm.nih.gov/24062084/) | 2014 | Animal Study | Psychopharmacology | α2A-adrenergic modulation in ventral hippocampus reduces impulsive decision-making — Baclofen not tested directly, but establishes relevance of GABAergic/monoaminergic interaction to impulsivity |
| [24103016](https://pubmed.ncbi.nlm.nih.gov/24103016/) | 2013 | Animal Study | European Journal of Neuroscience | Habenula integrity necessary for social play in rats; monoaminergic regulation discussed — highly indirect relevance to ADHD social-cognitive deficits |
| [24295630](https://pubmed.ncbi.nlm.nih.gov/24295630/) | 2013 | Review | International Review of Neurobiology | Emerging Tourette syndrome treatments reviewed; Baclofen discussed in context of tic-ADHD overlap and as an option where first-line agents fail |
| [24496320](https://pubmed.ncbi.nlm.nih.gov/24496320/) | 2014 | Animal Study | Neuropsychopharmacology | Anterior cingulate cortex and basolateral amygdala roles in cognitive effort-based choice — relevant to ADHD decision-making deficits, but Baclofen not among tested compounds |
| [26366961](https://pubmed.ncbi.nlm.nih.gov/26366961/) | 2015 | Review | Clinical Neuropharmacology | Mood stabilisers in children and adolescents with ASD; ADHD comorbidity addressed, Baclofen not primary focus |
| [30122296](https://pubmed.ncbi.nlm.nih.gov/30122296/) | 2019 | Observational/Off-label Review | L'Encéphale | Off-label methylphenidate prescribing in adult ADHD reviewed; Baclofen mentioned only peripherally in the context of psychiatric off-label practice |
| [35345730](https://pubmed.ncbi.nlm.nih.gov/35345730/) | 2022 | Systematic Review | Cureus | Systematic review of behavioural interventions, antipsychotics, and alpha agonists for Tourette tics; ADHD comorbidity discussed throughout, Baclofen not independently evaluated |

---

## Netherlands Market Information

No CBG-MEB marketing authorizations for Baclofen were retrieved in this dataset. This likely reflects a data retrieval gap rather than the true regulatory status, since Baclofen-containing products (e.g., Lioresal) are known to be used clinically in the Netherlands. **Please verify the current authorization status directly via the CBG-MEB public register (geneesmiddeleninformatiebank.nl) and obtain the Dutch SmPC before any clinical assessment.**

---

## Additional Predicted Indication: Nicotine Dependence (Rank 2)

> **Note:** The Evidence Pack includes a second predicted indication with substantially stronger clinical evidence. A brief summary is provided here; a full dedicated report is recommended.

The TxGNN model ranks **nicotine dependence** second (score: 99.2%), with **3 registered clinical trials** and **20 publications** retrieved. Evidence level is **L3** (observational studies and mechanistic human data), and the scoring system places this at decision stage S2 ("Research Question").

**Mechanistic rationale:** Baclofen, as a GABA-B agonist, suppresses dopamine release in the nucleus accumbens triggered by nicotine, thereby attenuating the rewarding properties of smoking. Multiple rodent studies confirm reduction of nicotine-conditioned place preference, self-administration reinstatement, and withdrawal manifestations. One completed Phase 2 fMRI study (NCT01821560, n=44) provides initial human proof-of-concept data on brain cue-reactivity in smokers.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT01821560](https://clinicaltrials.gov/study/NCT01821560) | Phase 2 | Completed | 44 | fMRI and behavioural assessment of Baclofen's effect on smoking cue-reactivity; only completed human trial for this indication |
| [NCT00257894](https://clinicaltrials.gov/study/NCT00257894) | Phase 2 | Terminated | 41 | Assessed Baclofen's effect on smoking urge and withdrawal; terminated before completion — reason unknown, partial data may exist |
| [NCT01228994](https://clinicaltrials.gov/study/NCT01228994) | Phase 2 | Terminated | 6 | Testing the GABAergic hypothesis of nicotine dependence; terminated very early (n=6), likely due to recruitment difficulties |

**Recommendation for nicotine dependence:** *Proceed with Guardrails* — mechanistic basis is sound and human POC data exists, but sample sizes are small and two trials did not complete. A well-powered Phase 2b RCT is needed before this indication can be assessed definitively.

---

## Safety Considerations

Safety data including key warnings, contraindications, and drug–drug interactions were not available in this Evidence Pack.

> Please refer to the SmPC (Summary of Product Characteristics / Samenvatting van de Productkenmerken) for full safety information. Particular attention should be paid to CNS depressant effects, abrupt withdrawal risks (which can precipitate seizures), and dose-dependent sedation — all known class effects of GABA-B agonists.

---

## Conclusion and Next Steps

**Decision: Hold** *(for ADHD indication)*

**Rationale:**
Despite a high TxGNN prediction score, all supporting literature for the ADHD indication is indirect — derived from Tourette syndrome comorbidity reviews and rodent models — and no clinical trials have been conducted in ADHD patients. The mechanistic link is plausible but unvalidated in humans, placing evidence firmly at L4.

**To proceed, the following is needed:**

- **Regulatory data:** Retrieve the current CBG-MEB authorisation status and Dutch SmPC for Baclofen via geneesmiddeleninformatiebank.nl; resolve the apparent data retrieval gap showing 0 authorisations
- **Safety review:** Obtain full warnings, contraindications, and DDI data from the EMA SmPC or DrugBank API to complete the S1 safety assessment
- **Mechanism clarification:** Query DrugBank for detailed GABA-B receptor pharmacology and its established CNS effects, including prefrontal dopamine modulation
- **Evidence scoping:** Commission a targeted systematic review of Baclofen in ADHD and closely related neurodevelopmental conditions (Tourette, ASD with ADHD features) to determine whether any unpublished trial data exists
- **Prioritise nicotine dependence:** Consider redirecting near-term investigational resources to the nicotine dependence indication (Rank 2), which has an established mechanistic rationale, human POC data, and a clear path to a Phase 2b RCT

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. This report complies with YMYL (Your Money or Your Life) standards: findings are exploratory and should not inform prescribing decisions without further clinical evidence.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

