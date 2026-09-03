---
id: J-104
title: ReAct
title_reading: リアクト
category: term_general
subtype: agent_loop
experience_level: research_only
reader_level: 6
importance: D
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-06-23
related_terms:
  - ループエンジニアリング
  - 自律ループとガードレール
  - Tool Use
  - Subagent
  - コンテキスト管理
status: ready
---

# ReAct

<!--
Lv6 自己学習シェルフ（reader_level: 6 / 刊行スコープ外）。
validator は reader_level 6 のとき字数・ですます・著者欄チェックを外し、YAML/構造/出典日だけ見る。
内容は専門的に踏み込む。文体は本書と揃えて です・ます維持。著者記入欄は空のまま。
-->

## tagline

Reason + Act（推論と行動）の略。「考える→動く→見る」を繰り返すエージェントループの原型です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

ReAct は、LLM エージェントに Thought（思考）→ Action（行動）→ Observation（観察）を繰り返させる、いちばん素朴なループの型です。まず「何をすべきか」を言葉にして考え（Thought）、次に検索やコード実行などのツールを実際に動かし（Action）、その結果を読み（Observation）、その観察をふまえて次の Thought を組み立てる——この 1 周を目標に届くまで回します。2022 年に提唱され、いま多くのエージェントが暗黙に踏襲している「型」の原点です。

## どこで出会うか

LangChain の AgentExecutor など、ツールを使うエージェントを組む土台としてほぼ既定の挙動になっています。たとえば「最新の為替レートを調べて日本円に換算して」と頼むと、エージェントは Thought で「まず検索が要る」と考え、Action で検索ツールを叩き、Observation で結果を読み、Thought に戻って「次は換算計算が要る」と続けます。Claude Code のようなコーディングエージェントが「ファイルを読む→編集する→テストを走らせて結果を見る」を繰り返すのも、この型の延長線上にあります。

## メイン図

### 図の狙い

Thought → Action → Observation を回る 3 コマの循環図で、1 周ごとに「観察が次の思考に必ず反映される」点を矢印で強調し、単なる自動実行ではなく毎回考え直していることを直感的に伝える。

## 会話での使い方例

「あのエージェント、ReAct っぽく毎回観察してから次を考えてますね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

考える・動く・見るを 1 周とし、目標に届くまで回すループの原型です。

### 2. うれしさ

行き当たりばったりでなく、結果を見て次の一手を選び直せます。

### 3. 注意点

自己批判や過去の失敗を記憶する仕組みはなく、同じ失敗を繰り返しがちです。

### 4. どこで役立つか

検索・コード実行など外部ツールを使う単純なエージェントタスクで役立ちます。

### 5. はじめに

Thought・Action・Observation の 3 語だけ押さえれば芯は掴めます。

### 6. 深掘り先

Reflexion、Plan-and-Execute、OODA ループ、Ralph Loop

## 開発フローでの位置（必須）

1. Thought — 目標を見て「次に何をすべきか」を言葉で考える
2. Action — 検索・コード実行などのツールを実際に呼び出す
3. Observation — ツールの結果を読み取る
4. 反復判定 — 目標に届いたか確認し、届かなければ Thought に戻る
5. 完了 — 目標達成でループを終了し、結果を返す

## 関連用語

- ループエンジニアリング
- 自律ループとガードレール
- Tool Use
- Subagent
- コンテキスト管理

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 「ReAct」と聞くと最初 JavaScript のフレームワーク React を連想してしまう。Reason + Act（推論と行動）の略だとは知らなかった。
- Thought→Action→Observation を回すこと自体は分かる。ビジネスの PDCA サイクルに近い感覚。
- これ「だけ」だと失敗を記憶しない課題があって、次（Reflexion）が生まれた、という流れがなるほどと思った。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: PDCA サイクルのように「回していく」ものだと捉えると入りやすい。結局エージェントは設計なんだと気づく。
- 👍 良い点: 結果を見て次の一手を選び直せるのでうまくいく。この型を土台に設計を組み立てられる。
- 👎 ダメな点: これだけだと課題（失敗を記憶しない）が残る。だから次の手法が生まれた、という発展の起点でしかない。
- 👥 誰向けか: エージェント開発の文脈にいる人。「エージェントとは何か」を、何が課題で何がボトルネックで、どんなアイデアでそれを解いたか、という流れで知りたい人に向く。設計図を自分で描けるようツールを整えていく、という視点が鍵。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 3 つの円（Thought / Action / Observation）を時計回りに矢印でつなぎ、1 周する循環図。Observation から Thought への矢印を太く強調し、「観察が次の思考に反映される」ことを視覚化する。
- 登場人物（いれば）: 調べ物をするエージェント役の小さなロボット・人物 1 名（著者の分身でも可）。虫眼鏡で検索結果を覗き込んでいる。
- 吹き出し・心の声: 「調べた結果を見てから、次にやることを決め直す——それだけの繰り返しなんだ」
- 中央に置くキーワード/ラベル: 「Thought＝考える」「Action＝動く」「Observation＝見る」

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（循環矢印アイコンを差し色で強調）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 吹き出しで考えている人物（Thought）
- Step 2 のアイコン/絵柄: ツールのレバーを引く手（Action）
- Step 3 のアイコン/絵柄: 結果を覗き込む虫眼鏡（Observation）
- Step 4 のアイコン/絵柄: 分岐する矢印（反復判定、Thought へ戻る矢印つき）

## コミュニティ補完メモ

- ループエンジニアリング（J-シリーズ想定）との住み分け: ループエンジニアリングは「ループ全体をどう設計するか」という総論。ReAct はその中でもっとも基本的な 1 周の型（Thought/Action/Observation）を指す各論。
- Reflexion・Plan-and-Execute との住み分け: いずれも ReAct の弱点（自己批判の記憶がない／計画と実行が混ざる）を補う発展形。本エントリは「原型」の説明に徹し、発展形の詳細は各エントリに譲る。
- Tool Use（既存エントリ）との住み分け: Tool Use はエージェントがツールを呼び出す仕組みそのもの。ReAct はその呼び出しを「いつ・なぜ」行うかを決めるループの型。

## 出典メモ

<!-- 形式: URL または誌名 — checked YYYY-MM-DD -->

- ledgers/loop_engineering_landscape_2026.md §2「ループの進化史」— checked 2026-06-23（ReAct(2022) を原型とし Reflexion・Plan-and-Execute・OODA・Ralph Loop へ発展する系譜の整理）
- datasciencedojo.com「agentic-loops」記事（2026）— checked 2026-06-23（ReAct を含むエージェントループの実務的な整理）
- happycapy.ai/blog/loop-engineering-ai-agents — checked 2026-06-23（loop/context/harness engineering の分類と ReAct の位置づけ）

## 備考

- reader_level: 6（自己学習シェルフ／刊行スコープ外）。今季の本には載せず、著者の勉強ノートとして育てる。docs/level_policy.md §2-6 準拠。
- 自動昇格しない設定（reader_level 6 ルート）。status は著者本人が管理する。
- 「まだよく分かっていない」基礎概念という位置づけのため、本文は専門用語の羅列を避け、具体例（為替レート調べ・Claude Code のファイル編集ループ）で直感を優先した。
- 5 段階サイクル（Perceive→Reason→Plan→Act→Observe）は ReAct の 3 段階（Thought/Action/Observation）をより細分化した後続の整理であり、混同しないよう深掘り先に切り分けた。

