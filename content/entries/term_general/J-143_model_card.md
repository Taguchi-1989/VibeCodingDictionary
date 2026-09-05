---
id: J-143
title: モデルカード
title_reading:
category: term_general
subtype: ai_governance
experience_level: partial
reader_level: 3
importance: C
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-09-05
related_terms: [説明可能性, EU AI Act, Hugging Face, Evals, Llama]
status: needs_review
---

# モデルカード

## tagline

AI モデルの説明書です。用途・学習データ・限界を短くまとめます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

モデルの意図された用途、学習データ、評価結果、限界、倫理的な考慮点を構造化した文書にまとめます。2019 年の論文が出発点で、Hugging Face などのモデル配布ページに添えられています。

## どこで出会うか

Hugging Face や各社のモデル配布ページで見かけます。EU AI Act のもとでは、高リスク用途のモデルで技術文書が任意ではなくなりつつあります。

## メイン図

### 図の狙い

9 項目のうち非エンジニアが読むべき要点だけを取り出し、「使ってよい範囲」が見える化されていることを掴んでもらいます。

## 会話での使い方例

「モデルカードの限界の欄、先に読んでおきましょう。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

用途・データ・限界を 1 枚にまとめる説明書です。

### 2. うれしさ

想定外の使い方や偏りに気づきやすくなります。

### 3. 注意点

書いてある内容の詳しさはモデルごとに差があります。

### 4. どこで役立つか

業務でモデルを選ぶときの下調べに使えます。

### 5. はじめに

意図された用途と限界の欄から読みます。

### 6. 深掘り先

Datasheets for Datasets、EU AI Act 技術文書

## 開発フローでの位置（必須）

1. モデル候補を探す — Hugging Face 等で複数を並べます
2. モデルカードを読む — 用途・限界・評価データを確認します
3. 禁止事項を確認する — させてはいけない使い方を先に把握します
4. 選定・導入する — 用途に合うか判断してから使い始めます

## 関連用語

- 説明可能性
- EU AI Act
- Hugging Face
- Evals
- Llama

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 
- 
- 
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 
- 👍 良い点: 
- 👎 ダメな点: 
- 👥 誰向けか: 
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: モデルカードという 1 枚の書類のイラスト。9 項目のうち「意図された用途」「限界」「評価データ」「倫理的考慮」の 4 マスだけ強調枠で囲む
- 登場人物（いれば）: モデルを選ぼうとしている非エンジニアの読者
- 吹き出し・心の声: 読者の心の声「できることより、できないことが知りたい」
- 中央に置くキーワード/ラベル: 「使ってよい範囲」

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 虫眼鏡でモデル一覧を見る
- Step 2 のアイコン/絵柄: 書類（モデルカード）を読む人
- Step 3 のアイコン/絵柄: 禁止マークの欄を確認する人
- Step 4 のアイコン/絵柄: モデルを選んで導入する人

## コミュニティ補完メモ

- J-139 説明可能性との住み分け：モデルカードはモデル全体の説明書（用途・データ・限界）、説明可能性は個々の出力がなぜそうなったかを扱う語。層が違うため両方引ける導線を残す
- J-58 EU AI Act との住み分け：モデルカードは技術文書そのもの、EU AI Act はそれを義務化する規制の側。制度の詳細は J-58 に譲る
- D 章の個別モデルエントリ（D-40 Llama 等）への入口として機能させる

## 出典メモ

- arXiv "Model Cards for Model Reporting" (Mitchell et al., 2019) https://arxiv.org/pdf/1810.03993 — checked 2026-09-05
- Future AGI Glossary "Model Cards" https://futureagi.com/glossary/model-cards/ — checked 2026-09-05
- TechAhead "AI Model Cards & Data Provenance" https://www.techaheadcorp.com/blog/ai-model-cards-data-provenance/ — checked 2026-09-05

## 備考

EU AI Act のもとでの高リスク AI 技術文書の義務は段階施行中であり、適用時期は断定していません（evaluation_date: 2026-09-05 時点の整理）。実装形式としては Hugging Face のモデルカード metadata 仕様が広く使われているとされています。
