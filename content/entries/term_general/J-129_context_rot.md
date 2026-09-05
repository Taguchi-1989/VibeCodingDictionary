---
id: J-129
title: コンテキスト腐敗
title_reading:
category: term_general
subtype: agent_loop
experience_level: hands_on
reader_level: 3
importance: C
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-09-05
related_terms:
  - コンテキスト窓
  - オートコンパクト
  - コンテキスト管理
  - サブエージェント
  - リランキング
status: needs_review
---

# コンテキスト腐敗

<!--
バイブコーディング図鑑 スケルトン雛形 v1（2026-04-28 追加）
- 構造だけ先に置いた状態。本文は status を `drafting` に上げた段階で entry-writer が埋める
- validator は status: skeleton を archived/sample と同様にスキップする
- tagline には entry_candidates.md の「一言」を仮で流し込んでいる（本書きで磨き直す）

YAML 補足（本書きで埋める／見直す欄）:
- subtype: candidate.csv の subtype 列を流し込み済み（後で見直す）
- experience_level: hands_on / partial / research_only
- reader_level: 1〜6
- figure_type: before_after / structure / comparison / workflow / timeline（仮で structure を入れている）
- version_status: active / preview / deprecated（時変なら埋める）
- pricing_note: none / paid / freemium（時変なら埋める）
- related_terms: 3〜5 個目安
- status: skeleton → drafting → needs_review → ready
-->

## tagline

<!-- 25〜60 字（推奨 30〜38、略称展開を含む場合 35〜50）。
     タイトルが略称・ヌメロニム（MCP / a11y / LLM 等）なら冒頭に「{展開} の略。」を入れる（2026-04-28 追加）。
     例: `Model Context Protocol の略。LLM とツール・データをつなぐ標準規格です。` -->

入力が長くなるほど、モデルの精度が静かに落ちていく現象です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

context rot（コンテキスト腐敗）は、入力が長くなるほど応答の精度が下がっていく現象そのものを指す語です。文脈窓（コンテキスト窓）に余裕があっても起きるとされ、枠が広いモデルなら安心とは言えません。

## どこで出会うか

長く続くエージェントのセッションや、資料を大量に読ませた会話で出会います。序盤は的確だった応答が、履歴が積み上がるうちに急に的外れになる場面で気づく人が多い現象です。

## メイン図

### 図の狙い

入力の先頭・中央・末尾で情報の拾われやすさが違う「U 字」を示し、真ん中に置いた情報ほど見落とされやすいことを掴んでもらいます。

## 会話での使い方例

「会話が長引いてきたので、コンテキスト腐敗が心配ですね。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

長い文脈で応答精度が落ちる現象に名前をつけた語です。


### 2. うれしさ

原因不明の的外れ回答に、対策を考える手がかりを与えます。


### 3. 注意点

文脈窓が広いモデルでも避けられないと報告されています。


### 4. どこで役立つか

長時間のエージェント運用や RAG 設計の判断で意識します。


### 5. はじめに

会話が長引いたら要点を整理し直す習慣から始めます。


### 6. 深掘り先

オートコンパクト、コンテキスト管理、リランキング


## 開発フローでの位置（必須）

<!-- 4〜5 ステップ。本書きで埋める。 -->

1. セッション開始 — 短い文脈で高い精度から始まります
2. 会話が長引く — 履歴やツール結果が積み上がっていきます
3. 精度が静かに低下 — 中央付近の情報ほど拾われにくくなります
4. 対策を挟む — 圧縮や要点の再整理で立て直します
5. 必要なら分割 — サブエージェントに渡して文脈を保ちます


## 関連用語

<!-- 3〜5 個。本書きで埋める。YAML の related_terms と一致させる。 -->

- コンテキスト窓
- オートコンパクト
- コンテキスト管理
- サブエージェント
- リランキング


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

- 描く内容: 横軸を入力の「先頭・中央・末尾」、縦軸を「拾われやすさ」にした U 字カーブ。中央がへこんでいる形
- 登場人物（いれば）: 長いセッションを続けているエージェント利用者。画面の前で首をかしげている姿
- 吹き出し・心の声: 「さっき渡した資料の真ん中の話、なんで拾ってくれないんだろう…」
- 中央に置くキーワード/ラベル: コンテキスト腐敗（context rot）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 空の吹き出し（まっさらなセッション）
- Step 2 のアイコン/絵柄: 積み上がるログのアイコン
- Step 3 のアイコン/絵柄: 下向き矢印つきの U 字カーブ小図
- Step 4 のアイコン/絵柄: 圧縮・整理を示すじょうごアイコン
- Step 5 のアイコン/絵柄: サブエージェントへ分岐する矢印


## コミュニティ補完メモ

- G-5 コンテキスト窓との住み分け：G-5 は「枠そのもの」の解説、J-129 は「枠に余裕があっても起きる劣化現象」。混同しないよう本文でも一言触れている
- G-47 オートコンパクト・J-105 コンテキスト管理・G-41 サブエージェント・G-64 リランキングは、いずれも J-129 で説明した劣化への対策側のエントリ。詳しい手順はそれぞれの本文に任せ、本エントリは現象の説明に絞る

## 出典メモ

- https://www.morphllm.com/context-rot — checked 2026-09-05
- https://redis.io/blog/context-rot/ — checked 2026-09-05
- https://www.researchgate.net/publication/378284067_Lost_in_the_Middle_How_Language_Models_Use_Long_Contexts — checked 2026-09-05

## 備考

Chroma の検証（GPT-4.1・Claude Opus 4・Gemini 2.5 を含む最前線 18 モデル）では、試した全ての入力長でこの劣化が見られたと報告されています。Liu ら（Stanford、TACL 2024）の "lost in the middle" 研究では、関連情報が入力の真ん中にあると精度が 30% 以上落ちるという U 字のカーブが示されました。どちらも特定モデルの優劣ではなく「どのモデルにも起こりうる」という点が要点です。
