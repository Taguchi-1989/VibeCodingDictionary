---
id: D-13
title: Claude 4.5 系
title_reading: クロード ヨンテンゴ系
category: model
subtype: anthropic
experience_level: hands_on
reader_level: 2-3
importance: B
figure_type: comparison
page_layout: spread_v1
start_date: 2025-09-29
end_date:
version_status: active
pricing_note: paid
evaluation_date: 2026-08-23
related_terms:
  - Claude
  - Anthropic
  - Claude Code
  - Claude 4 系
  - Claude 3.5 系
status: needs_review
---

# Claude 4.5 系

## tagline

Claude 第 4.5 世代。3 モデルが 2025 年秋に出そろいました。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Sonnet 4.5・Haiku 4.5・Opus 4.5 の 3 モデルで、賢さと速さと価格のバランスを選べます。文章生成やコード生成、ツール呼び出しをこなし、文脈は共通で 20 万トークンまで扱えます。

## どこで出会うか

Claude Code や Claude.ai、API 経由で日常的に触れる主力モデル帯です。2026-08 時点では Sonnet 4.5 が中心、軽い作業は Haiku 4.5、重い作業は Opus 4.5 と使い分けます。

## メイン図

### 図の狙い

3 モデルの公開順と、文脈長・価格の違いを 1 枚のカード比較で掴んでもらいます。

### B. 登場シーン（figure_type: comparison）

- シーン1: Sonnet 4.5（2025-09-29 公開）— 中心的な主力ティア
- シーン2: Haiku 4.5（2025-10-01 公開）— 速さと価格を優先するティア
- シーン3: Opus 4.5（2025-11-01 公開）— 最も重い仕事向けのティア
- 並べる基準: 公開日順。文脈 20 万トークン・出力上限 6.4 万トークンは 3 モデル共通

## 会話での使い方例

「Sonnet 4.5 が主力ですが、重い設計は Opus 4.5 に振っています。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Claude 4 系の中でも 4.5 世代、3 段のモデル群です。

### 2. うれしさ

軽重に応じて 3 段から選べ、費用も抑えられます。

### 3. 注意点

3 モデルとも文脈は 20 万トークンが上限です。

### 4. どこで役立つか

コーディングから日常業務まで幅広く使えます。

### 5. はじめに

公開順と 3 段の役割分担を押さえます。

### 6. 深掘り先

Claude 4 系、Claude Code、Claude のバージョン史

## 開発フローでの位置（必須）

1. 重さを見積もる — 調査系か実装系かを判断します
2. 段階を選ぶ — Haiku／Sonnet／Opus
3. 経路を選ぶ — Claude Code や API 経由で使う
4. 結果を確認する — 必要なら別の段へ切り替えます

## 関連用語

- Claude
- Anthropic
- Claude Code
- Claude 4 系
- Claude 3.5 系

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

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

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 横に 3 枚のカードを並べ、Sonnet 4.5・Haiku 4.5・Opus 4.5 それぞれの公開日（2025-09-29／2025-10-01／2025-11-01）を注記。共通値として文脈 20 万トークン・出力上限 6.4 万トークンを下部にまとめて表示
- 登場人物: 著者キャラクターが 3 枚のカードを見比べる仕草
- 吹き出し・心の声: 著者「1 か月ちょっとで 3 兄弟がそろった」
- 中央に置くキーワード/ラベル: Claude 4.5 系＝2025 年秋にそろった 3 段のティア

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1: 天秤アイコン（重さを見積もる）
- Step 2: 3 つのバッジ（Haiku／Sonnet／Opus）
- Step 3: 経路アイコン（Claude Code／API）
- Step 4: チェックアイコン（結果確認・切替）
- 矢印: 見積もる → 選ぶ → 使う → 確認 のループ

## コミュニティ補完メモ

- 族の総論・版の流れ全体は D-12 Claude 4 系が担当します。本エントリは 4.5 世代（Sonnet 4.5／Haiku 4.5／Opus 4.5）単体の公開日・仕様・提供状況に絞ります。
- 体感やナーフの話題は D-12・G-46 を参照してください。
- 3.5 系との比較は D-11 Claude 3.5 系を参照してください。

## 出典メモ

- Anthropic「Models overview」https://platform.claude.com/docs/en/about-claude/models/overview — checked 2026-08-23
- Anthropic「Model deprecations」https://platform.claude.com/docs/en/about-claude/model-deprecations — checked 2026-08-23

## 備考

モデル名・価格・提供状況は時変情報です。2026-08 時点では Sonnet 4.5・Haiku 4.5・Opus 4.5 の 3 モデルとも提供中で、公式は退役予定日を「Sonnet 4.5 は 2026-09-29 より前にはしない」「Haiku 4.5 は 2026-10-15 より前にはしない」「Opus 4.5 は 2026-11-24 より前にはしない」と案内しています。本番判断の前に公式ページを再確認してください。
