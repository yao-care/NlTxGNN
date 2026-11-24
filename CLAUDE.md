# TxGNN 國際化 SOP - 從初始化包建立地區藥品老藥新用預測系統

## 目標

將此初始化包轉換為您國家的藥品老藥新用預測系統。

**使用方式**：
1. 解壓縮 TxGNN_init.zip
2. 閱讀本文件，按照階段化流程執行
3. 將 `.template` 檔案改名並填入當地資訊
4. 執行預測流程

---

## 一、元件分類總覽

### 1.1 通用元件（直接使用，約 60-70%）

| 類別 | 檔案 | 說明 |
|------|------|------|
| **TxGNN 知識圖譜** | `data/node.csv`, `data/kg.csv` | 知識圖譜基礎資料（需下載） |
| **詞彙表提取** | `scripts/prepare_external_data.py` | 從 TxGNN 提取 DrugBank/疾病詞彙 |
| **藥名正規化** | `src/txgnn/mapping/normalizer.py` | 通用藥名標準化 |
| **DrugBank 映射** | `src/txgnn/mapping/drugbank_mapper.py` | 成分 → DrugBank ID |
| **KG 預測** | `src/txgnn/predict/repurposing.py` | 知識圖譜方法 |
| **DL 預測** | `src/txgnn/predict/txgnn_model.py` | 深度學習方法 |
| **通用收集器** | `collectors/clinicaltrials.py`, `pubmed.py`, `drugbank.py`, `ictrp.py` | 全球資料來源 |
| **收集器基類** | `src/txgnn/collectors/base.py` | 收集器介面 |

### 1.2 需在地化元件（約 30-40%）

| 類別 | 模板檔案 | 需修改內容 |
|------|----------|------------|
| **專案設定** | `pyproject.toml.template` | 專案名稱 |
| **欄位映射** | `config/fields.yaml.template` | 藥監局資料欄位對應 |
| **資料載入** | `src/txgnn/data/loader.py.template` | 載入邏輯 |
| **疾病映射** | `src/txgnn/mapping/disease_mapper.py.template` | DISEASE_DICT（當地語言→英文） |
| **資料處理** | `scripts/process_fda_data.py.template` | ZIP/JSON 解析 |
| **預測腳本** | `scripts/run_kg_prediction.py.template` | 微調欄位名稱 |
| **FHIR 生成** | `scripts/generate_fhir_resources.py.template` | URL 和管轄區域 |
| **新聞同義詞** | `data/news/synonyms.json.template` | 疾病/藥物同義詞 |
| **網站設定** | `docs/_config.yml.template` | 標題、URL |
| **SMART App** | `docs/smart/launch.html.template` | Client ID |
| **CI/CD** | `.github/workflows/pages.yml.template` | 部署設定 |

---

## 二、階段化實施流程

### Phase 0：專案初始化

**目標**：設定專案基礎

#### 步驟：

1. **重新命名專案**
   ```bash
   # 建議命名：{Country}TxGNN
   # 例：JpTxGNN, KrTxGNN, ThTxGNN
   mv TxGNN_init {Country}TxGNN
   cd {Country}TxGNN
   ```

2. **設定 pyproject.toml**
   ```bash
   mv pyproject.toml.template pyproject.toml
   # 編輯 pyproject.toml，修改 name 和 description
   ```

3. **下載 TxGNN 資料**
   ```bash
   mkdir -p data
   curl -L -o data/node.csv "https://dataverse.harvard.edu/api/access/datafile/7144482"
   curl -L -o data/kg.csv "https://dataverse.harvard.edu/api/access/datafile/7144484"
   ```

4. **安裝依賴**
   ```bash
   uv sync
   ```

**品質檢查點**：
- [ ] 專案已重新命名
- [ ] `pyproject.toml` 已修改
- [ ] `uv sync` 執行成功
- [ ] TxGNN 資料下載完成（node.csv ~15MB, kg.csv ~500MB）

---

### Phase 1：FDA 資料整合

**目標**：整合當地藥監局資料

#### 1.1 調查資料來源

常見藥監局資料來源：

| 國家 | 藥監局 | 資料來源 |
|------|--------|----------|
| 日本 | PMDA | https://www.pmda.go.jp/ |
| 韓國 | MFDS | https://nedrug.mfds.go.kr/ |
| 泰國 | Thai FDA | https://www.fda.moph.go.th/ |

**產出**：記錄資料來源 URL、格式、欄位說明

#### 1.2 建立欄位映射設定

```bash
mv config/fields.yaml.template config/fields.yaml
# 編輯 fields.yaml，填入欄位對應
```

**fields.yaml 範例（日本 PMDA）**：
```yaml
country_code: JP
language: ja
regulatory_agency: PMDA

field_mapping:
  license_id: "承認番号"
  brand_name_local: "販売名"
  brand_name_en: "一般名"
  ingredients: "有効成分"
  indication: "効能・効果"
  dosage_form: "剤形"
  status: "承認状況"

withdrawn_statuses:
  - "取消"
  - "回収"
```

#### 1.3 實作資料載入器

```bash
mv src/txgnn/data/loader.py.template src/txgnn/data/loader.py
# 編輯 loader.py，實作載入邏輯
```

#### 1.4 實作資料處理腳本

```bash
mv scripts/process_fda_data.py.template scripts/process_fda_data.py
# 編輯並執行
uv run python scripts/process_fda_data.py
```

**品質檢查點**：
- [ ] `config/fields.yaml` 建立完成
- [ ] `loader.py` 能正確載入資料
- [ ] `process_fda_data.py` 執行成功
- [ ] `data/raw/{country}_fda_drugs.json` 產生

---

### Phase 2：疾病映射

**目標**：建立當地語言 → 英文疾病對照

#### 2.1 建立 DISEASE_DICT

```bash
mv src/txgnn/mapping/disease_mapper.py.template src/txgnn/mapping/disease_mapper.py
# 編輯 disease_mapper.py，填入 DISEASE_DICT
```

**目標數量**：150-200 個疾病詞條

**分類建議**：

| 分類 | 建議數量 |
|------|----------|
| 心血管系統 | 15-20 |
| 呼吸系統 | 10-15 |
| 消化系統 | 15-20 |
| 神經系統 | 10-15 |
| 精神疾病 | 8-12 |
| 內分泌系統 | 10-15 |
| 肌肉骨骼 | 10-15 |
| 皮膚疾病 | 10-15 |
| 泌尿系統 | 8-12 |
| 眼科 | 5-8 |
| 耳鼻喉 | 5-8 |
| 感染症 | 10-15 |
| 過敏 | 5-8 |
| 婦科 | 8-12 |
| 腫瘤/癌症 | 10-15 |
| 一般症狀 | 15-20 |

#### 2.2 建立新聞同義詞

```bash
mv data/news/synonyms.json.template data/news/synonyms.json
# 編輯 synonyms.json，填入當地語言同義詞
```

**品質檢查點**：
- [ ] DISEASE_DICT 有 150+ 詞條
- [ ] 涵蓋所有主要疾病分類
- [ ] `synonyms.json` 建立完成

---

### Phase 3：KG 預測流程

**目標**：執行知識圖譜預測

#### 執行步驟：

```bash
# 1. 準備詞彙表
uv run python scripts/prepare_external_data.py

# 2. 設定預測腳本
mv scripts/run_kg_prediction.py.template scripts/run_kg_prediction.py
# 編輯並執行

# 3. 執行預測
uv run python scripts/run_kg_prediction.py
```

#### 預期產出：

| 檔案 | 預期內容 |
|------|----------|
| `data/external/drugbank_vocab.csv` | ~7,958 個藥物 |
| `data/external/disease_vocab.csv` | ~17,081 個疾病 |
| `data/external/drug_disease_relations.csv` | ~80,127 個關係 |
| `data/processed/repurposing_candidates.csv` | 視藥品數量而定 |

**品質檢查點**：
- [ ] 詞彙表正確產生
- [ ] `repurposing_candidates.csv` 產生
- [ ] DrugBank 映射率 > 30%
- [ ] 疾病映射率 > 20%

---

### Phase 4：網站與 FHIR

**目標**：部署文件網站與 FHIR API

#### 4.1 Jekyll 設定

```bash
mv docs/_config.yml.template docs/_config.yml
# 編輯 _config.yml，修改標題、URL、語言
```

#### 4.2 FHIR 資源設定

```bash
mv scripts/generate_fhir_resources.py.template scripts/generate_fhir_resources.py
# 編輯 BASE_URL 和 JURISDICTION
uv run python scripts/generate_fhir_resources.py
```

#### 4.3 SMART App 設定

```bash
mv docs/smart/launch.html.template docs/smart/launch.html
# 編輯 CLIENT_ID
```

#### 4.4 本地測試

```bash
cd docs
bundle install
bundle exec jekyll serve
# 訪問 http://localhost:4000
```

**品質檢查點**：
- [ ] Jekyll 本地建置成功
- [ ] `/fhir/metadata` 可存取
- [ ] FHIR 資源正確產生

---

### Phase 5：證據收集

**目標**：設定證據收集器

#### 5.1 建立當地 FDA 收集器

建立 `src/txgnn/collectors/{country}fda.py`：

```python
from .base import BaseCollector, CollectorResult

class {Country}FDACollector(BaseCollector):
    source_name = "{country}fda"

    def search(self, drug: str, disease: str | None = None) -> CollectorResult:
        # 實作搜尋邏輯
        pass
```

#### 5.2 區域臨床試驗註冊

ICTRP 涵蓋的區域註冊：
- 日本：JPRN (UMIN-CTR, JapicCTI)
- 韓國：CRIS
- 泰國：TCTR

**品質檢查點**：
- [ ] 當地 FDA 收集器建立
- [ ] ClinicalTrials.gov 收集器正常
- [ ] PubMed 收集器正常

---

### Phase 6：新聞監測

**目標**：設定健康新聞監測

#### 6.1 設定關鍵字模式

建立 `scripts/generate_news_keywords.py`，參考 TwTxGNN 版本。

#### 6.2 新增當地新聞來源

建立 `scripts/fetchers/{country}_news.py`

**品質檢查點**：
- [ ] `keywords.json` 產生
- [ ] 新聞爬蟲正常運作

---

### Phase 7：驗證與部署

**目標**：端對端驗證並部署

#### 7.1 設定 GitHub Actions

```bash
mv .github/workflows/pages.yml.template .github/workflows/pages.yml
# 編輯部署設定
```

#### 7.2 完整流程測試

```bash
uv run python scripts/process_fda_data.py
uv run python scripts/prepare_external_data.py
uv run python scripts/run_kg_prediction.py
uv run python scripts/generate_fhir_resources.py
```

#### 7.3 品質指標

| 指標 | 台灣參考值 | 目標 |
|------|-----------|------|
| FDA 藥品總數 | 71,552 | 記錄 |
| 有效藥品比例 | 33% | > 20% |
| DrugBank 映射率 | 73.87% | > 50% |
| 疾病映射率 | 44.85% | > 30% |
| 預測候選數 | 142,328 | 記錄 |

**品質檢查點**：
- [ ] 端對端流程通過
- [ ] GitHub Pages 部署成功
- [ ] SMART App 可從 SMART Launcher 啟動

---

## 三、關鍵檔案詳解

### 3.1 `config/fields.yaml`

欄位映射設定檔，定義藥監局資料欄位與標準欄位的對應關係。

### 3.2 `src/txgnn/data/loader.py`

資料載入器，根據 `fields.yaml` 載入並過濾藥品資料。

### 3.3 `src/txgnn/mapping/disease_mapper.py`

疾病映射模組，包含 `DISEASE_DICT`（當地語言→英文對照表）。

### 3.4 `scripts/process_fda_data.py`

資料處理腳本，將原始資料轉換為標準 JSON 格式。

---

## 四、GitHub Actions 設定

### 需設定的 Workflow：

| Workflow | 功能 | 需修改 |
|----------|------|--------|
| `pages.yml` | Jekyll 部署 | URL |
| `link-check.yml` | 連結檢查 | 無 |
| `check-new-evidence.yml` | 證據檢查 | 無 |

### 需設定的 Secrets：

| Secret | 用途 |
|--------|------|
| `GITHUB_TOKEN` | 自動提供 |
| `NCBI_API_KEY` | PubMed API（可選，提高速率限制） |

---

## 五、驗證清單

### 總體完成檢查

- [ ] Phase 0：專案初始化完成
- [ ] Phase 1：FDA 資料整合完成
- [ ] Phase 2：疾病映射完成
- [ ] Phase 3：KG 預測完成
- [ ] Phase 4：網站與 FHIR 完成
- [ ] Phase 5：證據收集完成
- [ ] Phase 6：新聞監測完成
- [ ] Phase 7：驗證與部署完成

### YMYL 檢查（醫療內容必檢）

- [ ] 免責聲明：「僅供研究參考，不構成醫療建議」
- [ ] 預測結果標註：「需經臨床驗證」
- [ ] 資料來源標註完整

---

## 六、附錄：區域特殊考量

### 日本 (PMDA)
- 資料格式：可能有 Shift-JIS 編碼
- 藥名：漢字/平假名/片假名混用
- 臨床試驗：JPRN (UMIN-CTR, JapicCTI, JMACCT)

### 韓國 (MFDS)
- 資料格式：UTF-8
- 藥名：韓文 + 英文音譯
- 臨床試驗：CRIS

### 泰國 (Thai FDA)
- 資料格式：UTF-8
- 藥名：泰文 + 英文
- 臨床試驗：TCTR

### 常見挑戰

1. **成分名稱變異**：同一藥物可能有不同鹽類形式
2. **品牌名映射**：當地品牌名需對應到國際名稱
3. **適應症文字解析**：不同語言的標點符號慣例不同
4. **日期格式**：各地區日期格式不同
5. **狀態碼**：有效/註銷的術語不同

---

## 常用命令

```bash
# 安裝依賴
uv sync

# 處理 FDA 資料
uv run python scripts/process_fda_data.py

# 準備詞彙表資料
uv run python scripts/prepare_external_data.py

# 執行知識圖譜預測
uv run python scripts/run_kg_prediction.py

# 生成 FHIR 資源
uv run python scripts/generate_fhir_resources.py

# 本地測試網站
cd docs && bundle exec jekyll serve

# 執行測試
uv run pytest tests/ -v
```

---

## 注意事項

- 本專案結果僅供研究參考，不構成醫療建議
- 老藥新用候選需經過臨床驗證才能應用
- 所有網站頁面需包含 YMYL 免責聲明

---

## 藥物頁查核機制（2026-11-12 起）

用戶 2026-11-12 決定：30 站各有自己的查核機制，核心流程比照 TwTxGNN（Tw 的 CLAUDE.md「藥物頁人工查核紀錄」「藥物頁許可證表與張數」兩節）；
UsTxGNN 是第一個試做站（做法見 UsTxGNN/CLAUDE.md 同名一節）。本站的規則與程式都在本 repo，頁面文字用荷蘭文，依據是CBG-MEB（Geneesmiddeleninformatiebank）的登記資料。
本站的在地字樣、頁首規則細節、歷史刪改的提交清單集中在 `src/nltxgnn/regulatory/site.py`。

| 環節 | 本站檔案 | 說明 |
|------|----------|------|
| 查核紀錄 | `docs/_data/drug_reviews.json` | 單一真實來源，欄位同 Tw（correct／annotate／rereview／rereview_result／header_level／description_level、history、status） |
| 套用 | `scripts/apply_drug_reviews.py` | 套到 `docs/_drugs/*.md`：查核框 `<!-- review:begin id -->`、每頁在免責聲明前的查核紀錄表；可重複執行；`--check` 只檢查、`--touch` 連 last_modified_at 一起改 |
| 頁首等級 | `src/nltxgnn/regulatory/page_format.py` | 頁首＝快速總覽「Bewijsniveau」格的**第一個**等級（主預測）。2026-11-12 實測 321 頁有總覽等級，頁首全部符合（0 頁例外），所以照實寫成程式、不改現有等級；Tw 是整格取最高，本站不同。頁首已是 N/A 的頁不依總覽格重算 |
| 撤回預測 | `src/nltxgnn/regulatory/withdrawn.py` | verdict=withdraw 的預測不進證據監測（`scripts/extract_drug_list.py`）、搜尋索引與 FHIR（母目錄 `.claude/rebuild_search_index.py`、`.claude/sync_fhir_levels.py` 會讀本站這支） |
| 許可證 | `snapshots/nl_licenses.json.gz`、`scripts/build_license_snapshot.py`、`src/nltxgnn/regulatory/licenses.py` | 快照存本藥許可證號與事實層；gate 依快照驗市場段落表格的許可證號屬於本藥、狀態列與張數列＝事實層寫法、表格列狀態不跟事實相反（本站沒有程式產生的許可證表，不驗表格列內容） |
| 刪改轉紀錄 | `scripts/reviews_from_edits.py` | 依 git 前後版本（或改寫前後目錄）把正文刪改轉成 correct 紀錄 |
| 待查清單 | `docs/_data/drug_reviews_uncertain.json`、`scripts/check_original_indications.py` | 原適應症交叉驗證與待重審項目；證據包沒有許可證適應症文字時照實回報可比對 0 頁 |
| gate | `scripts/check_seo_docs.py` 最後 4 項 | 紀錄都已套用、許可證＝快照、頁首＝快速總覽等級、撤回預測沒有對外發布 |

原則（同 Tw）：基本事實照主管機關資料更正；模型預測原文不刪不改寫，只加註；證據等級與決策只經重審（rereview → rereview_result）變更。

改頁之後要跑：

```bash
python3 scripts/apply_drug_reviews.py          # 重套查核紀錄（sync_notes_to_docs.py、每週排程結尾都會自動跑）
python3 scripts/build_license_snapshot.py --ws <工作目錄>   # 證據包或事實層變了才要（每週排程會自動跑）
python3 scripts/check_seo_docs.py              # 必須 exit 0
```

2026-10-31～11-06 依新事實直接刪掉的矛盾子句，2026-11-12 已用 `scripts/reviews_from_edits.py --git` 轉成 96 筆紀錄（69 頁；其中 1 筆因報告在 11 月經 AI 重產、原句已不在頁面，標 resolved_by_regeneration）。
`scripts/sync_notes_to_docs.py` 依 notes 重寫整頁後會重套紀錄，notes 裡的舊錯句會被紀錄再更正一次。

2026-11-12 事實層改依 CBG 現行登記重建（用戶決定）：原本的證據包來自第三方鏡像（openstate，已停），每個藥大多只收到 1 張登記、全標 active
（例：atorvastatin 現行 CBG 有 212 張，證據包只有 1 張，而且那張已不在現行登記；518 個登記號只有 215 個在現行清單）。
- `scripts/rebuild_licenses_by_ingredient.py`：下載 CBG 官方 metadata.csv（https://www.geneesmiddeleninformatiebank.nl/metadata.csv），依成分（WERKZAMESTOFFEN，去鹽類／酯類／水合物寫法、排除順勢療法 RVH）補收全部現行登記；
  證據包原有、但不在現行清單的登記號保留並標「Niet geregistreerd」（license_status＝cancelled、cbg_not_listed＝日期）。CBG 網站對這類號碼寫「Niet geregistreerd geneesmiddel — … komt niet voor in de Geneesmiddeleninformatiebank」，照原文用，不寫撤銷。
  只加不刪、可重複執行；`.github/workflows/license-refresh.yml` 每週在 license_refresh 前先跑，重建有變動就發新 Release。原本沒有紀錄的證據包不動（不知道荷蘭文成分名）。
- 2026-11-12 第一次重建：383 個藥新收 9,446 張現行登記、331 張標不在現行登記；333 頁的概覽狀態列與張數列、37 格表格狀態格由程式同步。
  正文跟新事實矛盾的 164 句以 `nl-lic-20261112-*` 刪除（多是「唯一的荷蘭許可已註銷」，現行其實有多張）；93 列 LLM 表格把不在現行登記的號碼寫成 geldig，以紀錄改成 niet geregistreerd。
  `scripts/license_sentence_fixes.json` 原本標 keep 的 96 句：88 句因本藥有現行登記改為刪除，其中 8 句是指表上那張（「Deze vergunning is doorgehaald」等）、那張確實不在現行登記，維持 keep；另 8 句的藥（ambroxol、lubiprostone、ranitidine、tiapride）現行 0 張，維持 keep。
  amylmetacresol、ethinylestradiol 兩筆 11-06 紀錄的錨點／留下的半句受影響，改錨或同 id 重發，前版存 history。
- 現行 0 張的 10 頁，概覽狀態列原由共用模板寫成「Niet in de handel (ingetrokken vergunningen: …)」，2026-11-12 母目錄 check_drug_page.py 的 nl 模板已改成「Niet in de handel (niet geregistreerd: n van n)」（照 CBG 原文）。
- 2026-11-15 正文許可證狀態再掃：本站事實層的 cancelled 全是 CBG 現行清單沒有的登記號（原文「Niet geregistreerd」），正文 28 處寫成 doorgehaald／ingetrokken，以 28 筆 `nl-lic-20261115-*` 更正：0 張的 4 頁（ambroxol、lubiprostone、ranitidine、tiapride，11-12 原標 keep 的 8 句）與指單張登記的句子照 CBG 原文改寫；有有效登記的藥說整體已撤回的句子（efavirenz、fexofenadine、arginine、tamsulosin、tretinoin、topotecan）刪除或改寫；8 列表格「(doorgehaald／ingetrokken)」改成「(niet geregistreerd)」。臨床試驗、撤稿論文的「ingetrokken」不動。

## 新資料查不到的許可證（2026-11-17）

2026-11-16 每週排程：證據包 8,514 張許可證有 309 張（331 筆紀錄）不在 CBG metadata.csv，涵蓋 96.4%，摘要列「查不到」。
2026-11-17 用戶要求確認實際狀態：這 309 張（全是 RVG 號）就是 2026-11-12 依成分重建時已標 Niet geregistreerd（cbg_not_listed）的那批，
2026-03 的 CBG 清單（data/raw/geneesmiddeleninformatiebank.csv）全部有、11 月 metadata.csv 全部沒有；CBG 產品頁
（https://www.geneesmiddeleninformatiebank.nl/nl/rvg<號>）逐號查 309 張都寫「Niet geregistreerd geneesmiddel … komt niet voor in de Geneesmiddeleninformatiebank」
（含 2 張「X=Y」重複登記寫法的號，用 X 查）。CBG 沒有另一份現行登記清單（metadata.csv 已含 RVG、EU 集中許可、RVH、平行輸入），所以沒有「其實仍有效」的號；號碼寫法也沒有對不上的。
- `scripts/license_adapter.py` 加 CURRENT／MIN_CURRENT（15,000）與 `confirmed_absent()`：metadata.csv 成功下載時，不在現行登記的 RVG／EU 號列為
  「主管機關現行清單確認已不列」，不算「查不到」、不開 issue（母目錄 license_refresh 的掛鉤）。標註仍由排程先跑的 rebuild_licenses_by_ingredient.py 做，寫法不變（Niet geregistreerd，不寫撤銷）。
- 頁面在 11-12、11-15 已照這批事實改過：排程重跑 0 筆狀態變動、0 頁要改；現行 0 張的 10 頁（abciximab、acarbose、ambroxol、chlordiazepoxide、cyclizine、didanosine、
  lubiprostone、piroxicam、ranitidine、tiapride）依成分對 metadata.csv 確認沒有其他現行產品（cyclizine 只命中 Primatour＝chloorcyclizine，是別的藥）。

## 作用機轉段的資料來源與查核機制（2026-11-19）

用戶 2026-11-19 決定把 NZTxGNN 同日的作法推到各站（seo-ops 轉交：搜「<藥名> mechanism of action」落在藥物頁排名 30–99，因為頁面寫「作用機轉資料不可得」）。
2026-11-19 量測：本站公開藥物頁（排除 noindex、轉址頁）有 264 頁在正文章節寫這種句子（證據包 drugbank.source＝vocab_only、沒有作用機轉文字，AI 照實寫「沒有資料」；本站最常見的寫法：「Gegevens over het werkingsmechanisme zijn voor dit rapport niet beschikbaar.」）。
作用機轉是藥物本身的基本藥理事實、不是模型預測，所以照查核機制補：每段都節錄官方仿單或資料庫原文、附可點的出處與取用日期，不自己寫。

- 來源（理由同 NZTxGNN/CLAUDE.md 同名一節）：美國 FDA 核准仿單（openFDA drug label，連結到 NLM DailyMed 同一份 SPL setid；FDA 仿單是美國政府公開資料），美國沒有仿單時用 ChEMBL drug mechanism 表（CC BY-SA 3.0）；證據包的 DrugBank 欄位只有 vocab，DrugBank 文字授權也不允許轉載，不用。
  2026-11-19 這次用 openFDA 的 drug label 全量下載檔（download.open.fda.gov，同一批資料，只留 human prescription 仿單；`--fda-bulk <目錄>`），不吃 API 每日 1,000 次配額；之後少量重跑可直接用 API（不給 `--fda-bulk`）。快取目錄各站共用。
- `scripts/build_mechanism_reviews.py --cache <目錄> [--fda-bulk <目錄>]`：掃公開頁正文章節（排除結論／下一步的待辦、安全性、摘要、總覽表、查核紀錄、免責聲明等）裡同時有「作用機轉」「資料」「沒有」字樣的短句（本站語言的字樣在檔內 L 的 KW／DATA／NEG／EXCL）→ 依 front matter monitor_inn（INN 另對 USAN，表在 US_NAME）查 openFDA，選仿單規則同 NZ：只用單一成分、主成分名（去鹽類；酯類要相同）跟本頁相同的處方藥仿單；排序全身給藥→節錄夠長→有 12.1→有品牌名→版本新；美國只有複方仿單的只節錄 12.1 裡講本藥成分的句子並寫明是複方；節錄照原文 2～4 句、不改寫。
  紀錄寫進 `docs/_data/drug_reviews.json`（action＝mechanism，id `nl-moa-<日期>-<藥>-1`，sources 附 url、accessed、excerpt、label_version、section、set_id 或 chembl_id）；仿單與 ChEMBL 都沒有的，列進 `docs/_data/drug_reviews_uncertain.json`（source＝mechanism of action，附原因）。已有紀錄或已列待查的頁不重抓。`--list` 只列仍寫「不可得」的頁。
- 替換句格式：本站語言（Nederlands）的出處句＋節錄的忠實翻譯（標明「非官方翻譯」）＋英文原文（照引、為準）＋DailyMed 連結、仿單版本、取用日期（用戶 2026-11-19 決定「當地語言摘要＋英文原文」）。只換「不可得」那一句（英文站句首子句後接 so／but 的後半句是 AI 推論，保留），不加框；查核紀錄表列原句與出處。模型預測與其他正文不動。
- 翻譯：節錄的翻譯是 AI 輔助的忠實翻譯（不增不減，藥名、基因與受體符號、數字、「[…]」照原文），2026-11-19 批次產生，存在紀錄 sources 的 translation（translation_lang、translation_note 註明非官方、英文原文為準）；頁面上同時列英文原文。`--translations <檔>` 讀翻譯、`--need <檔>` 列出還沒翻的節錄（這些頁那次不寫紀錄，gate 會擋，翻好再跑）。
- 2026-11-19 結果：232 頁寫入紀錄（美國仿單 215、ChEMBL 17），32 頁列待查（美國沒有單一成分處方藥仿單、仿單段落不是作用機轉，且 ChEMBL 沒有已核准分子的機轉紀錄；多是胺基酸、維生素、礦物質、賦形劑、生物製劑或只在別國上市的藥）。
- `scripts/apply_drug_reviews.py` 支援 mechanism；gate 第 21 項（`scripts/check_seo_docs.py`，函式在 build_mechanism_reviews.gate_errors）：公開頁仍寫「不可得」、既沒有 mechanism 紀錄也沒列待查的，擋下；有紀錄沒套上的由查核紀錄那一項擋。
- 注意：節錄的是美國仿單，劑型與適應症可能跟本站市場的產品不同（例如取到外用仿單）；文字上已寫明是美國 FDA 核准仿單。`sync_notes_to_docs.py` 整頁重寫後會重套紀錄（claim 是頁面原句）；報告重產、原句改寫後要再跑 build_mechanism_reviews.py。
- 2026-11-20 補做：程式更新：同頁不只一句「不可得」時每句各一筆紀錄（-1、-2…）；同頁別筆紀錄的更正文字、錨點與已套上的節錄不再當成「不可得」句；gate 改成公開頁仍寫「不可得」、又沒列待查就擋（不再只看該頁有沒有紀錄）；ChEMBL 譯文（詞組清單）後補句號 17 筆；同 id 重發，前版 replacement 存 history。
- 2026-11-20 試跑母目錄「交付前驗證」規則時補做：偵測改成原條件不動、另加新增寫法（L2，比中的再用 NOT 排除以缺資料為前提的模型推論），字樣用獨立、更寬的偵測全量掃出的候選句逐句標註校準（A 沒有漏、B 沒有誤中）；偵測漏抓的「不可得」句補 3 筆紀錄；節錄後面接著 AI 說明「上面描述依據」的句子（會讀成美國仿單的出處）5 筆改成那句在節錄前（原文不改，只換順序）；以上同 id 重發，前版存 history。程式另加 reorder_src_tail、同頁已引用同一段節錄時改指向上方（產生器 txgnn/.claude/moa_rollout_20261119/fix_20261120/）。

## 說明頁與證據等級頁的在地資料（2026-11-19）

用戶 2026-11-19 決定的第一批改版（母目錄 `.claude/gen_local_pages_20261119.py` 產生，不逐站手改）：說明頁（about／guide／sources／downloads／methodology，自有結構站只有證據等級頁與隱私頁）加本站資料區塊（`<!-- local-facts -->`）、證據等級頁的事實段與藥名表（`<!-- tier-facts -->`、`<!-- tier-table -->`）、隱私頁的適用法律／權利／著作權與資料來源段（`<!-- privacy-law -->`）；en／es／de 樣板站的共用長段落縮成一段（`<!-- local-condensed -->`）。
資料檔 `docs/_data/local_facts.json`、`docs/_data/evidence_tier_facts.json` 由 `scripts/local_facts.py`（＝母目錄 `.claude/local_facts_lib.py`）依藥物頁、許可證快照、查核紀錄、FHIR 算；`apply_drug_reviews.py`、許可證快照程式結尾會自動 `--write`，`check_seo_docs.py` 跑 `--check` 擋過期。跨站欄位（cross：本站獨有預測、30 站中位數）與頁面區塊只由母目錄產生器更新；藥物頁改等級、noindex 或預測後要在母目錄重跑。

## 藥物頁 description 句尾在地化（2026-11-19）

用戶 2026-11-19 決定（「藥物頁簡述在地化」，SEO 工具判定 30 站藥物頁近似重複，原因之一是 description 句尾都是同一句「原適應症：本地資料未記載」）：公開藥物頁（排除 noindex、轉址頁）front matter description 句尾的「Oorspronkelijke indicatie: Niet vermeld in de lokale gegevens」換成本站許可證快照事實層（`snapshots/*_licenses.json.gz`，經 `src/*/regulatory/licenses.py` 的 snapshot()）的品項數句子，資料名稱照本站口徑：CBG 登記。藥名、預測新適應症、等級字樣不動（母目錄 sync_description_levels.py 照舊對得到）；已有原適應症原文的頁不動。
例：abacavir「Oorspronkelijke indicatie: Niet vermeld in de lokale gegevens」→「In Nederland, CBG-vergunningen: 17 (geldig: 16)」；2026-11-19 改了 201 頁。
由母目錄 `.claude/drug_meta_description.py --apply --site NlTxGNN` 產生（站上複本 `tools/txgnn/.claude/drug_meta_description.py --apply --root .`），改動記在 `docs/_data/description_local_log.json`（pages＝目前句尾與原字樣、entries＝每次改動前後整行，可還原）。快照數字變了重跑會換新數字；`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾會自動 --apply，`check_seo_docs.py` 跑 --check 擋「還是未記載句尾」或「數字跟快照不符」。只改 front matter，lastmod_fix 不算正文改動、last_modified_at 不動。
同日修：`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾重算 local_facts 的 atexit 掛鉤在結束時取不到 `__file__`（NameError，之前其實沒跑成），改成先算好路徑。

## 許可證表與正文張數由程式產生（2026-11-24）

用戶 2026-11-24 決定（各站同日，本站「做表＋B」）：每週許可證排程只改得到概覽表狀態列／張數列，AI 寫在市場段落的自由格式許可證表（依 10-31 前舊證據包只列 1～5 張）與正文張數句會跟 CBG 現行登記矛盾；而 11-12 依成分重建後很多藥有上百張登記（acetaminophen 279、atorvastatin 213），舊表的 1～5 張不能代表本藥。改成程式產生、每週自動同步。
- A. 程式許可證表：`scripts/sync_license_tables.py`。市場段落（site.MARKET_SECTIONS，## 或 ###）的第一張表（表頭有 RVG／Registratie）換成程式依證據包（thaifda.records）產生的
  「| Registratienummer | Productnaam | Werkzame stof(fen) | Farmaceutische vorm | Status |」，文字照 CBG metadata.csv 原文（荷蘭文）；狀態：現行登記「Geldig」、不在現行清單（cbg_not_listed）「Niet geregistreerd」（照 CBG 網站原文，不寫 ingetrokken／doorgehaald；字樣同 `.claude/license_labels/NlTxGNN.json`）。
  排序：有效在前、單方（kind=single）在前、再依登記號數字；最多 20 列，超過時表下一句「Getoond worden N van de M registraties in de gegevens (…)」；表後一句來源；沒有紀錄時 NONE_LINE。前後 `<!-- licenses:begin -->`／`<!-- licenses:end -->`。
  Registratiehouder 欄 2026-11-24 第二輪加回（母目錄 checker 295dd578 已豁免「GmbH … KG」公司名；見下節）。
  快照 `snapshots/nl_licenses.json.gz` 另存 rows（前 20 列）／total（build_license_snapshot.py 用 rows_of）；gate 第 18 項（licenses.py）擋「程式區塊≠快照重算」「市場段落沒有程式表」。
  接上：`apply_drug_reviews.py`（非 --check）結尾、`build_license_snapshot.py` 結尾（`--no-rewrite` 不跑）、`scripts/license_adapter.py` 的 `sync_tables`（每週排程依證據包重排）與 `PAGE_NOTE`（3b 自我檢查放行程式句）。
  `--migrate`（2026-11-24 一次性）另拿掉市場段落裡只講舊表筆數／完整性的說明句（「Hieronder staan de eerste 5 vergunningen.」「De lijst is volledig.」等 13 句）；查核紀錄更正文字所在的句子不動。
- B. 正文張數程式改寫：`scripts/rewrite_license_counts.py`＋`src/nltxgnn/regulatory/count_prose.py`（照 Kr／My／DE 移植，荷蘭文句型：「Van de M registraties … zijn er N geldig」「N van de M vergunningen zijn geldig」「N geldige vergunningen」「N vergunningen」）。
  有保留、講證據包或查詢、相對數、劑型／單方複方／平行輸入／廠商子集、講表格或清單、待辦（vaststellen、nagaan、beoordel…）、partial 頁不動；同一行有判斷不了的句子整行不動；
  1 跟非 1 之間（荷蘭文單複數、指示詞、動詞要跟著改）、「beide」、0 張、「alle／beide／de enige … geldig」而事實不符的不改、列待查。apply（非 --check）與 build_license_snapshot 結尾自動跑；gate 第 22 項擋「再跑一次會變」。
- 2026-11-24 套用（資料 data-20261123-162625）：公開藥物頁 334 頁全部換成程式表（326 頁取代 AI 表、8 頁段落沒有表補在段落開頭；117 頁超過 20 張有「Getoond worden」句）；noindex 3 頁沒有市場段落、不加。
  錨在被取代表格列上的 103 筆查核紀錄標 `status: superseded`＋`superseded_by`。正文改寫 1 句（arginine「Van de 2 registraties … zijn er 2 geldig」→ 54／53）。
  查核紀錄同 id 重發（前版存 history，reason「程式許可證表／正文張數改由程式維護」）：note 裡寫死的「Aantal vergunningen in de gegevens: N, waarvan geldig: M」258 筆改成不寫數字（site.FIGURES 同步改，之後 reviews_from_edits 產生的紀錄也不寫數字）；
  更正文字講舊表單張（「Deze vergunning is geldig」「De enige bekende vergunning …」「Dit registratienummer …」「Beide registratienummers …」「(1 van 1)」）或只講舊表完整的 19 筆改成指名登記號或不寫張數的寫法（其中 dalteparin、finasteride、dutasteride、lamotrigine、nortriptyline 原文說舊表那張「geldig」，其實那張是 Niet geregistreerd、本藥另有有效登記，改成「Bij het CBG-MEB zijn geldige vergunningen geregistreerd (…)」；bumetanide「De lijst is volledig.」整句刪）。
  單方／複方：articaine「Beide vergunningen zijn enkelvoudige producten」（證據包 13 張全部是 articaïne＋adrenaline）以 `nl-lic-20261124-articaine-1` 更正。
  待查清單加 54 句（20 句 count_prose 判斷不了：多是「Er is 1 vergunning, en die is geldig」這類單數句、實際有 4～56 張；33 句另寫的寬偵測找到的單數／狀態敘述（「de enige Nederlandse vergunning is geschrapt」「het ontbreken van een geldige registratie」等，跟事實層不符；其中 articaine 1 句已寫紀錄、標 resolved）；lidocaine 單方張數 1 句：證據包 kind 欄把只多賦形劑的也算複方，只驗不改）。
  checker 全量前後都是 0、row-status 0；gate exit 0；寬偵測（正文張數／單數／全部有效敘述跟事實層不符）改前 77 句、改後 70 句（articaine 已更正），扣掉誤中 18 句，剩 52 句都已列待查（open）。last_modified_at：改到的 334 頁改 2026-11-24（表格與查核框內容都變了）。

## 第二輪：待查舊錯句逐句更正、程式表加 Registratiehouder（2026-11-24）

用戶 2026-11-24 第二輪決定（各站同日）：第一輪列進待查的舊錯句逐句寫查核紀錄更正，劑型說法、「表由程式補上」句一併處理。
- 程式表加回 Registratiehouder 欄：`| Registratienummer | Productnaam | Werkzame stof(fen) | Farmaceutische vorm | Registratiehouder | Status |`（證據包 license_holder，CBG 原文；沒有的寫「–」）；來源句同步。334 頁重排、快照 rows 重算。母目錄 checker 已豁免「GmbH … KG」公司名，全量 checker 加欄前後都是 0、row-status 0。
- 待查清單 53 句（第一輪 count_prose 判斷不了 20 句、寬偵測 33 句）逐句對照證據包（Release data-20261123-162625）與快照事實層：全部跟現行 CBG 登記不符（「Er is 1 vergunning, en die is geldig」實際 4～56 張；
  ganirelix、palonosetron、zuclopenthixol、mianserin、topiramate 等「de enige Nederlandse vergunning is geschrapt／geannuleerd」其實有效登記多張；ammonia「enige vergunning」實為 2 張別的藥；mannitol「RVG 108589 未列入表」程式表已列出；lidocaine「4 張單方」等），
  以 51 筆 `nl-lic-20261124b-*` 更正、2 筆同 id 重發（lorazepam、rocuronium 前版更正文字留下的單數／不可得說法；前版存 history），53 項標 resolved（附 record_ids）。
- 另寫的寬偵測（正文單數「deze vergunning」、全稱、註銷字樣、劑型全稱、「表由程式補上」）全量掃公開頁，再找到 22 句以 `nl-lic-20261124b-*` 更正（selenium「is geregistreerd geweest」、thymol「voorkwam」、esomeprazole「status niet eenduidig」、
  phenylephrine「alleen injectie-oplossingen」、benzydamine「geregistreerd als zuigtablet」（有效的是 crème）、ganirelix 待辦「de geschrapte vergunning (RVG 111978)」（Fyremadel 其實有效）、labetalol／epinephrine／zuclopenthixol 以「已註銷／沒有有效登記」為前提的理由與待辦、
  dexketoprofen「De vergunningentabel wordt door het programma toegevoegd」、tramadol「geen toedieningsvorm」、piroxicam「geannuleerd」改照 CBG 原文 niet geregistreerd 等），tamsulosin 11-12 紀錄同 id 重發（「doseringsvorm en fabrikant niet beschikbaar」程式表已有）。
- 寫法：更正文字不寫死張數，指向「het snelle overzicht en de vergunningstabel bij de marktinformatie」；待辦與決策理由只拿掉錯的前提（建議內容、決策不動）；模型預測文字不動。
- 驗證：寬偵測改後剩下的命中都跟事實層一致（總數 1 的頁、程式改寫的 arginine、正確的全稱）；apply --check、rewrite_license_counts --check、gate 都過；checker 全量 0、row-status 0。缺程式表的公開頁 0；site.FIGURES 第一輪已改成不寫數字。
- 待查清單剩下 open 32 項，都是作用機轉（2026-11-19，美國仿單與 ChEMBL 都沒有），不在這輪範圍。

