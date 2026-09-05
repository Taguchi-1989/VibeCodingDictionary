---
id: G-15
title: RAG
title_reading: アールエージー
category: term_llm
subtype: technique
experience_level: partial
reader_level: 3-4
importance: C
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - Embedding
  - ベクトル DB
  - Fine-tuning
  - Prompt Engineering
status: ready
---

# RAG

## tagline

Retrieval-Augmented Generation の略。回答前に外部文書を検索して文脈に添える手法です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

質問をベクトル化してベクトル DB（G-17）から類似文書を取り出し、プロンプトに添えます。社内規定など学習データ外の知識を根拠にした回答を作りやすくなります。

## どこで出会うか

社内 FAQ ボットや製品マニュアル Q&A を組む場面で登場します。「Fine-tuning より手早く試せて根拠文書も示せる」と紹介され、ドキュメントやスライドで名前を見かけます。


## メイン図

### 図の狙い

質問がどう変換され、どの順番で外部文書が合流して回答に至るかを 1 枚で示す。

### C. 概念図（figure_type: structure）

- 中心に置く概念: RAG パイプライン（質問 → 検索 → 注入 → 回答）
- 周辺の要素: ユーザー、ベクトル DB、取得文書、LLM、回答
- 関係の描き方: 左から右への矢印フロー。ベクトル DB は上段に置き、フローに合流する形


## 会話での使い方例

「社内 FAQ は RAG で組んだら、Fine-tuning より手早く動きました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

外部文書を検索して LLM の文脈に注入する仕組みです。

### 2. うれしさ

モデルを再学習せずに最新情報や社内知識を回答に反映できます。

### 3. 注意点

検索精度が低いと的外れな文書が注入され、回答品質が下がることがあります。

### 4. どこで役立つか

社内 FAQ・ドキュメント Q&A・専門領域の問い合わせ対応で効果が出やすいです。

### 5. はじめに

「質問 → 検索 → 文脈注入 → 回答」の 4 ステップが RAG の基本形です。

### 6. 深掘り先

チャンク分割（G-62）、ハイブリッド検索（G-63）、GraphRAG（G-60）


## 開発フローでの位置（必須）

1. 文書準備 — 社内ドキュメントや FAQ を収集してテキスト化します
2. Embedding 変換 — 文書を数値ベクトルに変換してベクトル DB に格納します
3. 質問受付 — ユーザーの質問を同じ方式でベクトル化します
4. 類似検索 — ベクトル DB から関連文書を取得してプロンプトに追加します
5. LLM 回答 — 文脈付きプロンプトを LLM に渡して回答を生成します


## 関連用語

- Embedding
- ベクトル DB
- Fine-tuning
- Prompt Engineering


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 2〜3 年前に流行ったが、RAG を「固有の技術」として持ち上げるのが微妙になってきました。
- 飛びついて構築しても、モデルが高性能化するにつれ昔のチューニングが陳腐化していきます。
- 実践しやすい反面、「これが本質か？」というモヤモヤが残ります。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: すごい、チャットボットも簡単に作れそうと感じました。
- 👍 良い点: 実際にチャットボットはそこそこのものができました。
- 👎 ダメな点: 全部入れると劣化する。エキスパートシステムとのハイブリッドにしないと使いづらいです。
- 👥 誰向けか: AI レガシーシステムの代表になりつつある印象です。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 質問を持った人 → Embedding 変換 → ベクトル DB 検索 → 文書取得 → LLM → 回答、という左右フロー図
- 登場人物: 担当者（質問を持っている）と LLM キャラクター（箱型ロボット）
- 吹き出し・心の声: 担当者「社内規定って何だっけ？」/ LLM「文書を読んでから答えます。」
- 中央に置くキーワード/ラベル: RAG パイプライン

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 書類の束（文書準備）
- Step 2 のアイコン/絵柄: 変換矢印＋数値列（Embedding）
- Step 3 のアイコン/絵柄: 虫眼鏡（類似検索）
- Step 4 のアイコン/絵柄: プロンプト＋文書合流（注入）
- Step 5 のアイコン/絵柄: 吹き出し（LLM 回答）
- 矢印で示す流れの意図: 左から右への一方向フロー。ベクトル DB からの合流点を分岐で表現する


## コミュニティ補完メモ

- Fine-tuning（J-16）との住み分け：モデル本体を再学習するのが Fine-tuning。外部知識を都度引き渡すのが RAG。費用・更新頻度・根拠明示の観点から RAG が先に検討されることが多い
- Embedding（G-16）との関係：RAG の検索ステップに Embedding を使う。G-16 は仕組みの詳細を扱うため、本エントリは概念と用途に絞る
- ベクトル DB（G-17）との関係：RAG のストレージ層を担う。詳細は G-17 へ
- Prompt Engineering（G-10）との関係：RAG で取得した文書をプロンプトにどう組み込むかに Prompt Engineering の知識が活きる

## 出典メモ

- Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks", arXiv 2020 — checked 2026-04-30
- LangChain Docs (python.langchain.com) — checked 2026-04-30
- LlamaIndex Docs (docs.llamaindex.ai) — checked 2026-04-30


## 備考

- 起源は Meta（C-4）の研究者 Lewis らが 2020 年に発表した論文。「RAG」という略称はこの論文タイトルに由来する
- 代表的な実装フレームワーク：LangChain / LlamaIndex / Haystack / Vertex AI Agent Builder（B-27）/ Anthropic Claude Connectors
- 「RAG を使えば幻覚がなくなる」と誤解されやすいが、検索精度や文書品質に依存するため完全な解決策ではない
