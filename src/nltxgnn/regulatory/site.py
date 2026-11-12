"""本站查核機制的在地設定（NlTxGNN，荷蘭文；2026-11-12 建）。

程式（page_format、licenses、withdrawn、scripts/apply_drug_reviews.py、build_license_snapshot.py、reviews_from_edits.py、
check_original_indications.py）的核心流程比照 TwTxGNN／UsTxGNN，本站的字樣、規則細節、提交清單集中在這裡。
本站的許可證資料是 CBG-MEB 的 Geneesmiddeleninformatiebank（metadata.csv），事實層只涵蓋對得上的部分（checker X_SCOPE）。
"""
import re

SITE = "NlTxGNN"
CODE = "nl"

# ---- 頁首等級（page_format）----
OVERVIEW_LEVEL_LABELS = ["Bewijsniveau", "Evidentieniveau", "Evidenceniveau"]
HEADER_LABEL = "Bewijsniveau"
# 2026-11-12 實測：321 頁有總覽等級，頁首全部＝總覽格第一個等級（主預測），0 頁例外 → first（不照 Tw 整格取最高）
HEADER_RULE = "first"
HEADER_KEEP_NA = True
HEADER_EXCEPTIONS: dict = {}
WITHDRAWN_RE = re.compile(r"^\s*(\*\*)?(Ingetrokken|Teruggetrokken)\b", re.I)
DESC_LEVEL_WORD = r"bewijsniveau|evidentieniveau|evidenceniveau"
DESC_LEVEL_DEFAULT = "bewijsniveau"
NA_DESC = "alleen bekend gebruik"

# ---- 許可證（licenses）----
MARKET_SECTIONS = ["Informatie over de Nederlandse markt", "Marktinformatie Nederland"]

# ---- 查核框與查核紀錄表（apply_drug_reviews）----
DISCLAIMER_RE = re.compile(r"^## Disclaimer\b", re.M)
LOG_HEAD = "## Controlelogboek"
LOG_COLS = "| Controledatum | Onderdeel | Actie | Bron |"
LABEL = {"correct": "Controlecorrectie", "annotate": "Controleopmerking", "rereview": "Wacht op herbeoordeling",
         "rereview_result": "Resultaat herbeoordeling"}
ACTION = {"correct": "Gecorrigeerd", "annotate": "Opmerking toegevoegd", "rereview": "Gemarkeerd voor herbeoordeling",
          "section": "Sectie met bronnen toegevoegd", "rereview_result": "Herbeoordeling afgerond",
          "header_level": "Bewijsniveau in de paginakop opnieuw berekend uit het snelle overzicht",
          "description_level": "Bewijsniveau in de paginabeschrijving volgt de paginakop"}
VERDICT = {"maintain": "Ongewijzigd", "downgrade": "Verlaagd", "upgrade": "Verhoogd", "withdraw": "Ingetrokken"}
BOX_HEAD = "> **{label} ({date})**: "
ORIG_STATED = "Oorspronkelijk stond er: “{claim}”"
SPACE, FULL_STOP, SENT_END = " ", ".", ".!?)”"
PAREN = " ({})"
JOIN, LIST_SEP, ITEM_SEP = " / ", "; ", ", "
SOURCE_WORD = "Bron: "
DECISION = "Aanbevolen besluit: "
TABLE_UPDATED = "{labels} op deze pagina zijn bijgewerkt volgens de herbeoordeling; de oorspronkelijke waarden staan in het controlelogboek hieronder."
LEVEL_SAME = "bewijsniveau {o} ongewijzigd"
LEVEL_CHANGE = "bewijsniveau {o} → {n}"
ACT_REREVIEWED = "Gemarkeerd voor herbeoordeling → herbeoordeeld (zie het resultaat van de herbeoordeling)"
ACT_HEADER = "Bewijsniveau in de paginakop opnieuw berekend uit het snelle overzicht ({o} → {n})"
ACT_HEADER_WD = "Hoofdvoorspelling ingetrokken bij herbeoordeling; bewijsniveau in de paginakop opnieuw berekend ({o} → {n})"
ACT_NA_LIST = ", nu vermeld onder “{title}”"
ACT_RESULT = "Herbeoordeling: {verdict}, {change}"
ACT_TABLE = "; {label}: “{a}” → “{b}”"
ACT_DESC = "Paginabeschrijving: “bewijsniveau {o}” gewijzigd in “{n}” (volgt de paginakop; overige tekst ongewijzigd, origineel bewaard in het record)"
ACT_REVISED = " (herzien op {d}; eerdere versie bewaard in het record)"
ST_SUPERSEDED = "Vervangen door de door het programma gegenereerde vergunningstabel (eerder: {act})"
ST_REGEN = "Niet meer aanwezig nadat het rapport opnieuw is gegenereerd ({d}: {note}; eerder: {act})"
ST_PROGRAM = "Niet meer aanwezig na een programmacorrectie ({d}: {note}; eerder: {act})"
ST_WITHDRAWN = "Controle ingetrokken ({d}: {note}; eerder: {act})"
INTRO = ("Hieronder staat het controlelogboek van deze pagina: gegevens gecontroleerd aan de hand van de registratiegegevens van het CBG "
         "(College ter Beoordeling van Geneesmiddelen). Correcties betreffen alleen feitelijke basisgegevens; modelvoorspellingen, "
         "bewijsniveaus en conclusies zijn niet herschreven.")
INTRO_HEADER = ("Hieronder staat het controlelogboek van deze pagina; het bewijsniveau in de paginakop volgt het snelle overzicht. "
                "Modelvoorspellingen, de overzichtstabel en de conclusies zijn niet herschreven.")
INTRO_RERE = ("Hieronder staat het controlelogboek van deze pagina: gegevens gecontroleerd aan de hand van de registratiegegevens van het CBG. "
              "Correcties betreffen alleen feitelijke basisgegevens en de tekst van de modelvoorspellingen is niet herschreven; bewijsniveaus en "
              "besluiten zijn alleen gewijzigd door een resultaat van herbeoordeling (verlaging, verhoging of intrekking), met de oorspronkelijke waarden hieronder.")

# ---- 刪改轉紀錄（reviews_from_edits）----
# 2026-10-31～11-06 的許可證刪改：b6bb5b517 刪「只剩註銷許可」、e246792bc 第二批掃描刪矛盾子句。
COMMITS = ["b6bb5b517", "e246792bc"]
REGEN_COMMITS = ["7aba8dccd", "3de843ac2", "b26e8790f", "78ff97867", "dc41cd3d4", "2c4557c3d", "b8d96724f", "63ac0fe27", "48e706d3f"]
SOURCES = [{"title": "CBG-MEB – Geneesmiddeleninformatiebank (metadata)", "url": "https://www.geneesmiddeleninformatiebank.nl/metadata.csv"},
           {"title": "Geneesmiddeleninformatiebank", "url": "https://www.geneesmiddeleninformatiebank.nl/"}]
SENT = re.compile(r'(?<=[.!?])\s+(?=[A-Z0-9(*"“\[])|\n')
CLASS_EXTRA: dict = {}
NOTES = {
    "tw": "Verwijderd: achtergebleven sjabloontekst over de Taiwanese geneesmiddelenautoriteit (TFDA), die niet van toepassing is op deze Nederlandse pagina.",
    "cancel": "Verwijderd: de vermelding dat de vergunningen zijn doorgehaald of dat er geen geldige vergunning is, kwam niet overeen met de registratiegegevens van het CBG ({date}).",
    "count": "Verwijderd: het aantal of de status van de vergunningen kwam niet overeen met de registratiegegevens van het CBG ({date}).",
    "generic": "Verwijderd: de vermelding kwam niet overeen met de registratiegegevens van het CBG ({date}).",
}
FIGURES = " Aantal vergunningen in de gegevens: {total}, waarvan geldig: {valid}; actuele aantallen staan in het snelle overzicht en bij de marktinformatie."
SUMMARY = "Verwijderd: “{text}”"
STRIP_CHARS = " ,;.\n-"
REGEN_NOTE = "het rapport is in november 2026 opnieuw gegenereerd en bevat de vermelding niet meer"

# ---- 原適應症交叉驗證（check_original_indications）----
ORIGINAL_LABELS = ["Oorspronkelijke indicatie"]
ORIGINAL_NONE_RE = re.compile(r"^\s*(niet vermeld|niet bekend|geen|ontbreekt|onbekend|n/a)", re.I)
PHRASE_SPLIT = re.compile(r"[;,/()]+|\ben\b|\bof\b", re.I)
PHRASE_MIN = 4
