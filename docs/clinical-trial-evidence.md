---
layout: default
title: "Geneesmiddelen met studiebewijs voor een nieuwe indicatie"
nav_order: 25
permalink: /clinical-trial-evidence/
description: "Geneesmiddelen van het CBG-MEB waarvan de door TxGNN voorspelde nieuwe indicatie bewijs uit klinische studies heeft (L1-L2): indicatie, niveau, studies."
last_modified_at: 2026-11-03
---
{%- comment -%}
2026-11-03：回答 AI 搜尋常問的「本國藥物中，哪些新適應症有臨床試驗證據」。全表由 Liquid 從藥物頁產生，不寫死藥名或數字。
收錄＝公開藥物頁（排除 id_redirect 與 noindex）中 evidence_level 為 L1 或 L2（本站 evidence-high 標準：L1 多個 Phase 3 RCT／系統性回顧，
L2 單一 RCT 或多個 Phase 2 試驗）。預測新適應症與等級註記取自各藥物頁快速總覽表；下列欄名是本站藥物頁實際用到的寫法（建頁時逐頁核對），
新寫法抓不到時顯示「zie rapport」、等級仍取 front matter。試驗數＝該藥物頁引用的不重複 NCT 編號數。
{%- endcomment -%}
{%- assign ind_labels = "Voorspelde nieuwe indicatie" | split: "|" -%}
{%- assign lev_labels = "Bewijsniveau|Evidentieniveau|Evidenceniveau" | split: "|" -%}
{%- assign listed = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" -%}
{%- assign l1 = listed | where: "evidence_level", "L1" | sort: "title" -%}
{%- assign l2 = listed | where: "evidence_level", "L2" | sort: "title" -%}
{%- assign trial_drugs = l1 | concat: l2 -%}
{%- assign latest = trial_drugs | sort: "last_modified_at" | last -%}
{%- assign latest_date = latest.last_modified_at | date: "%Y-%m-%d" -%}

# Geneesmiddelen in Nederland met bewijs uit klinische studies voor een nieuwe indicatie

<p class="key-answer" data-question="Welke geneesmiddelen in Nederland hebben bewijs uit klinische studies voor een nieuwe indicatie?">
<strong>{{ trial_drugs.size }}</strong> van de {{ listed.size }} geneesmiddelen met een NlTxGNN-rapport hebben een door TxGNN voorspelde nieuwe indicatie met bewijsniveau <strong>L1 of L2</strong> ({{ l1.size }} op L1, {{ l2.size }} op L2): daarvoor is dus bewijs uit klinische studies gevonden (gerandomiseerde studies, fase 2–3-studies of systematische reviews).
</p>

De geneesmiddelen komen uit de Geneesmiddeleninformatiebank van het [CBG-MEB](https://www.cbg-meb.nl/) (in Nederland geregistreerde geneesmiddelen); de lijst geeft de geneesmiddelrapporten weer zoals laatst bijgewerkt op {{ latest_date }}.

<div class="key-takeaway">
Bewijs uit studies voor een voorspelde indicatie is geen bewijs van werkzaamheid. Elke kandidaat hieronder <strong>vereist nog klinische validatie</strong> en beoordeling door de regelgever vóór enig klinisch gebruik.
</div>

---

## Geneesmiddelen met bewijs uit studies (L1–L2)

<div class="table-wrapper"><table>
<thead>
<tr><th>Geneesmiddel</th><th>Voorspelde nieuwe indicatie</th><th>Bewijsniveau</th><th>Geciteerde geregistreerde studies (NCT)</th></tr>
</thead>
<tbody>
{%- for drug in trial_drugs -%}
{%- assign indication = "" -%}
{%- for lab in ind_labels -%}{%- if indication == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign qo = drug.content | split: needle -%}{%- if qo.size > 1 -%}{%- assign indication = qo[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign level_cell = "" -%}
{%- for lab in lev_labels -%}{%- if level_cell == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign lv = drug.content | split: needle -%}{%- if lv.size > 1 -%}{%- assign level_cell = lv[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign parts = drug.content | split: "NCT" -%}
{%- capture nct_ids -%}{%- for p in parts offset: 1 -%}{%- assign id = p | slice: 0, 8 -%}{%- assign rest = id | remove: "0" | remove: "1" | remove: "2" | remove: "3" | remove: "4" | remove: "5" | remove: "6" | remove: "7" | remove: "8" | remove: "9" -%}{%- if id.size == 8 and rest == "" -%}{{ id }},{%- endif -%}{%- endfor -%}{%- endcapture -%}
{%- assign nct_count = nct_ids | split: "," | uniq | size %}
<tr><td><a href="{{ drug.url | relative_url }}">{{ drug.title }}</a></td><td>{% if indication != "" %}{{ indication }}{% else %}zie rapport{% endif %}</td><td>{{ drug.evidence_level }}{% if level_cell != "" and level_cell != drug.evidence_level %} <a href="{{ drug.url | relative_url }}" title="{{ level_cell | strip_html | escape }}">(met voorbehoud)</a>{% endif %}</td><td>{{ nct_count }}</td></tr>
{%- endfor %}
</tbody>
</table></div>

## Zo leest u deze lijst

- **Bewijsniveau** volgt de [criteria]({{ '/evidence-high/' | relative_url }}) van de site: L1 = Meerdere fase 3-RCT's / systematische reviews; L2 = Eén RCT of meerdere fase 2-studies. ‘(met voorbehoud)’ betekent dat het rapport een voorbehoud maakt bij het niveau; lees de toelichting in het rapport voordat u erop vertrouwt.
- **Voorspelde nieuwe indicatie** is de hoofdvoorspelling van elk rapport. Indicaties en contra-indicaties die al in de TxGNN-kennisgraaf staan, zijn uitgesloten, maar sommige voorspellingen kunnen toch overlappen met een bestaand gebruik; het rapport licht dat toe waar het van toepassing is.
- **Geciteerde geregistreerde studies** telt de ClinicalTrials.gov-nummers (NCT) die in het rapport worden geciteerd. De rapporten citeren een selectie van de gevonden studies; 0 betekent dat het rapport geen geregistreerde studie citeert, en de sectie over literatuurbewijs toont de basis voor het niveau.
- Voor alle niveaus en de volledige methode, zie [Sterk bewijs (L1-L2)]({{ '/evidence-high/' | relative_url }}), [Alle geneesmiddelen]({{ '/drugs/' | relative_url }}) en de [methodologie]({{ '/methodology/' | relative_url }}).

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
Dit rapport is uitsluitend bedoeld als naslagwerk voor wetenschappelijk onderzoek en <strong>vormt geen medisch advies</strong>. Volg altijd de aanwijzingen van uw arts op; pas nooit op eigen initiatief uw medicatie aan. Elke beslissing over geneesmiddelherpositionering vereist volledige klinische validatie en toetsing door de registratieautoriteit.
<br><br>
<small>Beoordeeld door: 藥提醒科技有限公司 (yao.care)</small>
</div>
