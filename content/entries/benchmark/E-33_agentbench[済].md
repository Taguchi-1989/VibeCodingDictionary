---
id: E-33
title: AgentBench
title_reading: エージェントベンチ
category: benchmark
subtype: agent_benchmark
experience_level: research_only
reader_level: 4-5
importance: E
figure_type: comparison
page_layout: spread_v1
start_date: 2023-08-07
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - WebArena
  - GAIA
  - OSWorld
  - Z.ai
status: ready
---

# AgentBench

## tagline

LLM がエージェントとして複数環境で行動できるかを多面的に測るベンチマークです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

OS 操作や DB、Web ショッピングなど 8 環境のマルチターン課題を LLM に解かせ、チャット応答ではなく実行力を数値化します。清華大学・Z.ai が 2023 年に公開しました。

## どこで出会うか

新モデルのエージェント性能を伝える論文や業界記事で引用されます。WebArena・GAIA・OSWorld と並ぶエージェント能力ベンチの主要 4 本のひとつです。

## メイン図

### 図の狙い

8 種の評価環境とそのスコアを横並びにして「どの能力を測っているか」を一覧できるようにします。

### B. 登場シーン（figure_type: comparison）

- シーン1: 研究者が論文で複数モデルの AgentBench スコアを表として比較する
- シーン2: エンジニアがモデル選定の根拠に OS 環境の平均スコアを引用する
- シーン3: 業界観察者がブログで「GLM-4 が OS 環境で伸びた」と解説する
- 並べる基準: 評価環境 8 種を横軸、モデル名を縦軸にした比較表

## 会話での使い方例

「AgentBench の OS 環境で GLM-4.6 が伸びていました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

LLM のエージェント実行力を 8 環境で多面的に評価します。

### 2. うれしさ

単一タスクでなく多環境の平均で比べるため偏りが出にくいです。

### 3. 注意点

比較は同じ環境同士が正確で、全体平均のみでの判断は誤解を招きます。

### 4. どこで役立つか

モデル採用の検討や論文の性能比較を読み解く場面で活用できます。

### 5. はじめに

8 環境の構成と「Avg. は参考値」という読み方を押さえると十分です。

### 6. 深掘り先

WebArena、OSWorld、GAIA

## 開発フローでの位置（必須）

1. モデル候補の選定 — エージェント性能の客観指標として AgentBench スコアを参照します
2. 環境別スコアの確認 — OS / DB / Web などタスクに近い環境のスコアを選んで比較します
3. 他ベンチとの照合 — WebArena や GAIA と併読し、苦手領域がないか確認します
4. 採用可否の判断 — 複数ベンチの結果を総合してモデルを絞り込みます

## 関連用語

- WebArena
- GAIA
- OSWorld
- Z.ai


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 今回初めて聞いた語で、他のエージェント系ベンチとの違いが見えにくいです。
- どこまでメジャーで、どのモデルがどれだけ取れるかの相場感が分かりません。
- 8 環境の中で何が得意・苦手かを読み解くには、ある程度の前提知識が必要です。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 今回初めて見たベンチで、清華大学発というところに新鮮さを感じました。
- 👍 良い点: 8 環境という広さで評価するので、単一領域では見えない弱点が出やすい設計です。
- 👎 ダメな点: 全体平均だけでは誤解を生みやすく、環境別で読み解く手間が要ります。
- 👥 誰向けか: AI の進歩を定点観測したい人にとって、多面的な物差しとして役立つ指標です。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 8 種の評価環境アイコンを横に並べ、それぞれにスコアバーを添えた比較表
- 登場人物（いれば）: 研究者風の人物がスコア表を眺めている
- 吹き出し・心の声: 「OS 環境だけで判断しても意味ないか…全部見ないと」
- 中央に置くキーワード/ラベル: 8 Environments

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 虫眼鏡でモデル一覧を見るアイコン
- Step 2 のアイコン/絵柄: バーグラフ（環境別スコア）
- Step 3 のアイコン/絵柄: 複数のグラフを並べる比較アイコン
- Step 4 のアイコン/絵柄: チェックマーク（採用決定）
- 矢印で示す流れの意図: 「選定 → 絞り込み → 検証 → 決定」の直線フロー


## コミュニティ補完メモ

- WebArena（E-31）との住み分け：WebArena は Web ブラウザ操作に特化。AgentBench は 8 環境を横断する多面評価で、より広い能力比較に使います
- GAIA（E-32）との住み分け：GAIA は汎用アシスタント能力を問う。AgentBench はツール実行・環境操作に重点を置きます
- OSWorld（E-34）との住み分け：OSWorld は OS デスクトップ操作の専門特化。AgentBench の OS 環境とは重なりがありますが、OSWorld のほうが操作の粒度が細かいです
- 中国研究機関発のベンチとして GLM（Z.ai）や Qwen の改善報告とセットで引用されることが多いです

## 出典メモ

- AgentBench: Evaluating LLMs as Agents (arXiv:2308.03688) — checked 2026-04-30
- GitHub THUDM/AgentBench — checked 2026-04-30

## 備考

- 2023-08 に清華大学・Zhipu AI（現 Z.ai）が公開。論文は arXiv:2308.03688
- 8 環境の内訳：OS、Database、Knowledge Graph、Card Game、Lateral Thinking Puzzles、House Holding、Web Shopping、Web Browsing
- スコア比較時は「Avg.（全環境平均）」と「環境別スコア」を区別して引用するのが正確。同じ環境同士の比較が前提
- GPT-4 が初期に高成績を記録し、その後 Claude・Gemini・GLM・Qwen 系が追随する形で更新が続いています
- **2026-05 時点の状況メモ**
  - 8 環境構成（OS Shell / DB SQL / 知識グラフ / カードゲーム / 家事シミュ / Web ショッピング / Web ブラウジング / 横思考パズル）はエージェントベンチの中で最も範囲が広く、単一ドメインベンチで見逃す弱点を補う設計
  - 個別モデルの最新スコアは Tsinghua THUDM/AgentBench の GitHub README が一次情報
  - 2026-04 に UC Berkeley/RDI が「報酬ハッキングで主要エージェントベンチ 8 種が攻略可能」と報告。第三者の Epoch AI / BenchLM スコアと併読が推奨される
