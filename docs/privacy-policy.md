---
layout: default
title: Privacybeleid
nav_order: 95
permalink: /privacy-policy/
description: "Privacybeleid van NlTxGNN: statische site zonder accounts of formulieren; gebruikt analytische cookies van Google Analytics 4 voor gebruiksstatistieken."
---

# Privacybeleid

<div class="key-takeaway">
Dit is een statische site — geen registratie en geen formulieren. De site gebruikt analytische cookies van Google Analytics 4 om gebruiksstatistieken op te stellen.
</div>

---

## Wat wij verzamelen

<p class="key-answer" data-question="Verzamelt NlTxGNN persoonsgegevens?">
<strong>Alleen gebruiksstatistieken, via Google Analytics 4.</strong> Deze site wordt als volledig statische site gehost op GitHub
Pages. Er is geen accountsysteem en er zijn geen formulieren, en wij verzamelen geen namen, e-mailadressen of medische
dossiers. De site gebruikt analytische cookies van Google Analytics 4 om gebruiksstatistieken op te stellen (bekeken
pagina's, verwijzende site, scrolldiepte en tijd op de pagina). De cookies worden geplaatst wanneer een pagina laadt;
zoektermen, formulierinhoud en queryparameters in de URL worden niet verzonden.
</p>

---

## Diensten van derden

De site maakt gebruik van de volgende bronnen van derden, die volgens hun eigen beleid toegang kunnen
registreren:

| Dienst | Doel | Privacybeleid |
|---------|---------|----------------|
| GitHub Pages | Hosting van de site | [GitHub Privacy Statement](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement) |
| Google Analytics 4 (www.googletagmanager.com, google-analytics.com) | Bezoekstatistieken (bekeken pagina’s, verwijzende site); gebruikt analysecookies. Zoektermen, formulierinhoud en URL-parameters worden niet verstuurd. | [Privacybeleid van Google](https://policies.google.com/privacy) |
| cdn.jsdelivr.net | Scriptbibliotheken: d3-grafieken op elke pagina; Fuse.js voor naamvergelijking en de SMART on FHIR-client op de SMART-pagina’s en in de geneesmiddelzoeker op de startpagina | [Privacybeleid van jsDelivr](https://www.jsdelivr.com/terms/privacy-policy-jsdelivr-net) |
| clinicaltrials.gov | Zoeken naar klinische studies op de SMART-pagina’s: alleen als u erom vraagt, worden de naam van het geneesmiddel en de indicatie naar de API van ClinicalTrials.gov gestuurd | [Webbeleid van de NLM](https://www.nlm.nih.gov/web_policies.html) |
| rxnav.nlm.nih.gov | SMART-app: de RxNorm-codes van de geneesmiddelen die uit uw elektronisch patiëntendossier worden gelezen, worden naar de RxNav-API van de NLM gestuurd om de naam van de werkzame stof op te zoeken (geen patiëntgegevens die u identificeren) | [Webbeleid van de NLM](https://www.nlm.nih.gov/web_policies.html) |

Wanneer u de SMART on FHIR-app zelf start, vraagt deze medicatiegegevens op uit uw elektronisch
patiëntendossiersysteem. De identiteit van de patiënt en de dossiergegevens worden <strong>niet naar de servers van deze
site verzonden</strong> (het is een statische site zonder backend) en worden niet door deze site opgeslagen. Om
geneesmiddelnamen te koppelen, stuurt de app de RxNorm-codes van de geneesmiddelen naar de RxNav-dienst van de
Amerikaanse National Library of Medicine; deze codes bevatten geen gegevens waarmee de patiënt kan worden
geïdentificeerd. Wanneer u klinische studies opvraagt, worden de naam van het geneesmiddel en de indicatie naar
ClinicalTrials.gov verzonden.

---

<!-- privacy-law:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改；法規與連結見 .claude/privacy_text_20261119.py）-->
## Toepasselijk recht

Voor bezoekers in Nederland gelden de [Algemene verordening gegevensbescherming (AVG)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) en de [Uitvoeringswet AVG](https://wetten.overheid.nl/BWBR0040940); voor cookies geldt daarnaast artikel 11.7a van de Telecommunicatiewet. Toezichthouder is de [Autoriteit Persoonsgegevens](https://www.autoriteitpersoonsgegevens.nl/). De verwerkingsverantwoordelijke zit in Taiwan en heeft geen vestiging in de EU; het gaat om de gebruiksgegevens die Google Analytics 4 via cookies verzamelt.

## Uw rechten en hoe u ze uitoefent

- Recht op inzage (artikel 15) en rectificatie (artikel 16).
- Recht op gegevenswissing (artikel 17) en beperking (artikel 18).
- Recht van bezwaar (artikel 21), ook tegen webanalyse.
- Recht om een klacht in te dienen bij de Autoriteit Persoonsgegevens (artikel 77).

Verzoeken en vragen: service@yao.care. Omdat de site geen accounts heeft, kunnen we gegevens bij Google Analytics alleen behandelen als u genoeg details geeft (bijvoorbeeld datum en pagina's van uw bezoek); u kunt analytische cookies ook in uw browser blokkeren of verwijderen.

## Auteursrecht en gegevensbronnen

De teksten van de site zijn beschermd door de [Auteurswet](https://wetten.overheid.nl/BWBR0001886). De code van de site staat onder de MIT-licentie in de [GitHub-repository](https://github.com/yao-care/NlTxGNN); rapportteksten zijn © 藥提醒科技有限公司 (yao.care).

Gegevensbronnen van deze site en hun voorwaarden:

- **TxGNN**-voorspellingsgegevens (Harvard Dataverse): CC0 1.0 (publiek domein); citeer Huang et al., *Nature Medicine* 2024.
- **ClinicalTrials.gov** en **PubMed**: US National Library of Medicine; zie de [voorwaarden van ClinicalTrials.gov](https://clinicaltrials.gov/about-site/terms-conditions) en het [NCBI-beleid](https://www.ncbi.nlm.nih.gov/home/about/policies/) (sommige PubMed-samenvattingen vallen onder het auteursrecht van de uitgever).
- **DrugBank**-identificatoren en -gegevens: volgens de licentievoorwaarden van [DrugBank](https://go.drugbank.com/) (niet-commercieel gebruik).
- **Lokale dataset**: [CBG-MEB Geneesmiddeleninformatiebank](https://www.geneesmiddeleninformatiebank.nl/metadata.csv), gepubliceerd door College ter Beoordeling van Geneesmiddelen (CBG-MEB); hergebruik valt onder de voorwaarden van de uitgever, en deze site verleent geen aanvullende rechten.

<!-- privacy-law:end -->

---

## Wijzigingen in dit beleid

Eventuele wijzigingen worden rechtstreeks op deze pagina gepubliceerd.

---

## Over de ontwikkelaar

Dit platform is ontwikkeld en wordt beheerd door **藥提醒科技有限公司** (yao.care). Gegevens over het bedrijf,
de achtergrond van het TxGNN-model en alle sites van de productlijn staan op de pagina
<a href="{{ '/about/' | relative_url }}">Over ons</a>.

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
Dit rapport is uitsluitend bedoeld als naslagwerk voor wetenschappelijk onderzoek en <strong>vormt geen medisch advies</strong>. Volg altijd de aanwijzingen van uw arts op; pas nooit op eigen initiatief uw medicatie aan. Elke beslissing over geneesmiddelherpositionering vereist volledige klinische validatie en toetsing door de registratieautoriteit.
<br><br>
<small>Beoordeeld door: 藥提醒科技有限公司 (yao.care)</small>
</div>
