---
layout: default
title: "Voorspellingen voor Geneesmiddelherpositionering \u2014 Nederland"
nav_order: 1
description: "AI-gestuurde voorspellingen voor herbestemming van geneesmiddelen voor 334 door het CBG-MEB goedgekeurde geneesmiddelen. Het TxGNN-model vindt mogelijke nieuwe therapeutische toepassingen met evidence-based validatie."
last_modified_at: 2026-11-04
permalink: /
---

# Herbestemming van geneesmiddelen: van AI naar bewijs

**NlTxGNN** gebruikt het TxGNN-model van Harvard om kandidaten voor geneesmiddelherpositionering te voorspellen voor **{{ site.data.drug_stats.total_drugs }}** door het CBG-MEB goedgekeurde geneesmiddelen en zo mogelijke nieuwe therapeutische toepassingen te vinden.

[Bekijk geneesmiddelrapporten](/drugs/){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Lees over de methodologie](/methodology/){: .btn .fs-5 .mb-4 .mb-md-0 }

---

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## Nederland: wat deze site omvat

Deze site publiceert rapporten over **{{ site.data.drug_stats.total_drugs }}** geneesmiddelen uit de registratiegegevens van [CBG-MEB](https://www.cbg-meb.nl/) (Nederland).

Dataset: [CBG-MEB Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/metadata.csv); wordt elke week (op maandag) automatisch gedownload en vergeleken. Details: [Gegevensbronnen]({{ '/sources/' | relative_url }}).

Rapporten per bewijsniveau:

| Bewijsniveau | Rapporten | Aandeel |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

### Geneesmiddelen met het hoogste bewijsniveau op deze site

| Geneesmiddel | Bewijsniveau |
|---|---|
| [Bendamustine](/drugs/bendamustine/) | L1 |
| [Bupropion](/drugs/bupropion/) | L1 |
| [Ribavirin](/drugs/ribavirin/) | L1 |
| [Acetylcysteine](/drugs/acetylcysteine/) | L2 |
| [Diazepam](/drugs/diazepam/) | L2 |
| [Fludarabine](/drugs/fludarabine/) | L2 |
| [Clozapine](/drugs/clozapine/) | L2 |
| [Hydrocortisone](/drugs/hydrocortisone/) | L2 |
| [Prednisolone](/drugs/prednisolone/) | L2 |
| [Doxorubicin](/drugs/doxorubicin/) | L2 |

<!-- local-home:end -->

## Geneesmiddel zoeken

Voer een **geneesmiddelnaam** of **ziektenaam** in om voorspellingen voor herpositionering te vinden. Generieke namen, merknamen en ziektetrefwoorden worden ondersteund.

<style>
.drug-lookup-container { margin: 1.5rem 0; }
.lookup-search-box { display: flex; gap: 0.5rem; margin-bottom: 1rem; }
.lookup-input-wrapper { flex: 1; position: relative; }
#lookup-input { width: 100%; padding: 0.75rem 2.5rem 0.75rem 1rem; border: 2px solid #ddd; border-radius: 8px; font-size: 1rem; }
#lookup-input:focus { outline: none; border-color: #1976D2; }
.lookup-clear-btn { position: absolute; right: 0.75rem; top: 50%; transform: translateY(-50%); background: none; border: none; cursor: pointer; color: #999; font-size: 1.2rem; }
.lookup-search-btn { padding: 0.75rem 1.5rem; background: #1976D2; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: 600; }
.lookup-search-btn:hover { background: #1565C0; }
.lookup-filters { display: flex; gap: 1rem; align-items: center; flex-wrap: wrap; margin-bottom: 1rem; }
.filter-label { font-weight: 600; color: #666; }
.lookup-filters label { display: flex; align-items: center; gap: 0.25rem; cursor: pointer; }
.lookup-results { margin-top: 1rem; }
</style>

<div class="drug-lookup-container">
  <div class="lookup-search-box">
    <div class="lookup-input-wrapper">
      <input type="text" id="lookup-input" placeholder="Voer een geneesmiddel- of ziektenaam in..." autocomplete="off">
      <button id="lookup-clear" class="lookup-clear-btn" style="display: none;">✕</button>
    </div>
    <button id="lookup-search" class="lookup-search-btn">Zoeken</button>
  </div>
  <div class="lookup-filters">
    <span class="filter-label">Bewijsniveau:</span>
    <label><input type="checkbox" class="level-filter" value="L1" checked> L1</label>
    <label><input type="checkbox" class="level-filter" value="L2" checked> L2</label>
    <label><input type="checkbox" class="level-filter" value="L3" checked> L3</label>
    <label><input type="checkbox" class="level-filter" value="L4" checked> L4</label>
    <label><input type="checkbox" class="level-filter" value="L5" checked> L5</label>
  </div>
  <div id="lookup-results" class="lookup-results"></div>
</div>

<script src="https://cdn.jsdelivr.net/npm/fuse.js@7.0.0/dist/fuse.min.js" integrity="sha384-PCSoOZTpbkikBEtd/+uV3WNdc676i9KUf01KOA8CnJotvlx8rRrETbDuwdjqTYvt" crossorigin="anonymous"></script>
<script>
  window.NLTXGNN_CONFIG = {
    searchIndexUrl: '{{ "/data/search-index.json" | relative_url }}',
    drugsBaseUrl: '{{ "/drugs/" | relative_url }}'
  };
</script>
<script src="{{ '/assets/js/drug-lookup.js' | relative_url }}"></script>

---

## Belangrijkste kenmerken

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin: 1.5rem 0;">
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #2E7D32;">
    <strong style="font-size: 1.1rem;">Van voorspelling naar bewijs</strong><br>
    <span style="color: #666;">Elk rapport bundelt ID's van klinische studies (NCT), literatuurverwijzingen (PMID) en registratiegegevens van het CBG-MEB, volledig herleidbaar.</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #1976D2;">
    <strong style="font-size: 1.1rem;">Bewijsclassificatie in vijf niveaus</strong><br>
    <span style="color: #666;">De classificatie van L1 (meerdere fase 3-RCT's) tot L5 (alleen AI-voorspelling) helpt kandidaten voor validatie te prioriteren.</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #FB8C00;">
    <strong style="font-size: 1.1rem;">Dekking van Nederlandse geneesmiddelen</strong><br>
    <span style="color: #666;">Gericht op {{ site.data.drug_stats.total_drugs }} door het CBG-MEB goedgekeurde geneesmiddelen met voorspellingen voor herpositionering, klaar voor onderzoek.</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #9B59B6;">
    <strong style="font-size: 1.1rem;">FHIR-integratie</strong><br>
    <span style="color: #666;">FHIR R4-conforme API en SMART on FHIR-app voor integratie met elektronische patiëntendossiers.</span>
  </div>
</div>

---

## Snelle navigatie

| Categorie | Beschrijving | Link |
|----------|-------------|------|
| **Sterk bewijs** | L1-L2, prioriteit voor klinische beoordeling | [Bekijk geneesmiddelen](/evidence-high/) |
| **Matig bewijs** | L3-L4, aanvullende validatie nodig | [Bekijk geneesmiddelen](/evidence-medium/) |
| **AI-voorspellingen** | L5, referentie voor onderzoeksrichting | [Bekijk geneesmiddelen](/evidence-low/) |
| **Alle geneesmiddelen** | Alle {{ site.data.drug_stats.total_drugs }} geneesmiddelen (doorzoekbaar) | [Geneesmiddelenlijst](/drugs/) |
| **Gezondheidsnieuws** | Automatische monitoring van gezondheidsnieuws | [Bekijk nieuws](/news/) |
| **FHIR API** | Integratie-eindpunten | [FHIR-metadata](/fhir/metadata) |

---

## Over dit project

NlTxGNN gebruikt het deep-learningmodel **TxGNN**, gepubliceerd door het Zitnik Lab van Harvard in *Nature Medicine*, om mogelijke nieuwe therapeutische toepassingen van door het CBG-MEB goedgekeurde geneesmiddelen te voorspellen.

> "TxGNN is het eerste foundationmodel dat is ontworpen voor geneesmiddelherpositionering vanuit het perspectief van de clinicus; het combineert kennisgrafen met deep learning om de werkzaamheid van geneesmiddelen bij zeldzame ziekten te voorspellen."
> <cite>— Huang et al., Nature Medicine (2024)</cite>

### Statistieken

| Onderdeel | Aantal |
|------|-------|
| Geneesmiddelrapporten | {{ site.data.drug_stats.total_drugs }} |
| Registratieautoriteit | College ter Beoordeling van Geneesmiddelen (CBG-MEB) |

[Meer informatie](/about/) | [Methodologie](/methodology/) | [Gegevensbronnen](/sources/)

---

## Gegevensbronnen

<style>
.data-source-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 1rem; margin: 2rem 0; padding: 1.5rem; background: #f8f9fa; border-radius: 12px; }
.data-source-card { display: flex; flex-direction: column; align-items: center; padding: 1.25rem 1rem; background: white; border-radius: 10px; text-decoration: none; color: #333; box-shadow: 0 2px 8px rgba(0,0,0,0.08); transition: transform 0.2s, box-shadow 0.2s; }
.data-source-card:hover { transform: translateY(-4px); box-shadow: 0 6px 20px rgba(0,0,0,0.12); }
.data-source-icon { width: 48px; height: 48px; margin-bottom: 0.75rem; display: flex; align-items: center; justify-content: center; border-radius: 12px; font-size: 24px; }
.data-source-card strong { font-size: 0.95rem; margin-bottom: 0.25rem; }
.data-source-card small { font-size: 0.75rem; color: #666; text-align: center; }
</style>

<div class="data-source-grid">
  <a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/" target="_blank" rel="noopener" class="data-source-card">
    <div class="data-source-icon" style="background: #FDE8E8;">🧬</div>
    <strong style="color: #A51C30;">TxGNN</strong>
    <small>Harvard Zitnik Lab</small>
  </a>
  <a href="https://clinicaltrials.gov/" target="_blank" rel="noopener" class="data-source-card">
    <div class="data-source-icon" style="background: #E8F0F8;">🏥</div>
    <strong style="color: #205493;">ClinicalTrials.gov</strong>
    <small>Klinische studies van het NIH</small>
  </a>
  <a href="https://pubmed.ncbi.nlm.nih.gov/" target="_blank" rel="noopener" class="data-source-card">
    <div class="data-source-icon" style="background: #E8F0F5;">📚</div>
    <strong style="color: #326599;">PubMed</strong>
    <small>Biomedische literatuur</small>
  </a>
  <a href="https://go.drugbank.com/" target="_blank" rel="noopener" class="data-source-card">
    <div class="data-source-icon" style="background: #FDEDEC;">💊</div>
    <strong style="color: #E74C3C;">DrugBank</strong>
    <small>Geneesmiddelendatabank</small>
  </a>
  <a href="https://www.cbg-meb.nl/" target="_blank" rel="noopener" class="data-source-card">
    <div class="data-source-icon" style="background: #E8F8EE;">🇳🇱</div>
    <strong style="color: #FF6600;">CBG-MEB</strong>
    <small>College ter Beoordeling van Geneesmiddelen</small>
  </a>
</div>

---

<div style="background: #fff3cd; padding: 1rem; border-left: 4px solid #ffc107; border-radius: 4px; margin: 1rem 0;">
<strong>Disclaimer</strong><br>
Dit rapport is <strong>uitsluitend bedoeld voor onderzoek</strong> en vormt geen medisch advies. Volg bij geneesmiddelgebruik de aanwijzingen van uw arts. Elke beslissing over geneesmiddelherpositionering vereist volledige klinische validatie en toetsing door de registratieautoriteit.
<br><br>
<small>Laatst bijgewerkt: {{ page.last_modified_at | date: "%Y-%m-%d" }} | Beheerder: 藥提醒科技有限公司 (yao.care)</small>
</div>

---

## Over de ontwikkelaar

Dit platform is ontwikkeld en wordt beheerd door **藥提醒科技有限公司** (yao.care). Gegevens over het bedrijf,
de achtergrond van het TxGNN-model en alle sites van de productlijn staan op de pagina
<a href="{{ '/about/' | relative_url }}">Over ons</a>.
