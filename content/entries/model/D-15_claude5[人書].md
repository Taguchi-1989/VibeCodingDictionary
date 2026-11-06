---
id: D-15
title: Claude 5 系
title_reading: クロード ゴ系
category: model
subtype: anthropic
experience_level: hands_on
reader_level: 2-3
importance: B
figure_type: comparison
page_layout: spread_v1
start_date: 2026-06-30
end_date:
version_status: active
pricing_note: paid
evaluation_date: 2026-11-06
last_audited: 2026-11-06
related_terms:
  - Claude Code
  - Claude 4.5 系
  - Claude Fable / Mythos
  - Claude 5.5 系
status: needs_review
---

# Claude 5 系

## tagline

Claude 第 5 世代。Sonnet 5 と Opus 5 が 2026 年夏に出ました。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Sonnet 5 と Opus 5 の 2 モデルで、速さと賢さのバランスを選べます。文脈は共通で 100 万トークン（4.5 世代の 5 倍）まで扱え、考える量はモデルが自分で決めます。

## どこで出会うか

Claude Code や Claude.ai、API で触れる世代です。Sonnet 5 は 2026-06-30、Opus 5 は 2026-07-24 に公開されました。2026-11 時点では legacy 扱いで、後続の 5.5 世代（D-17）への移行が案内されています。

## メイン図

### 図の狙い

Sonnet 5 と Opus 5 の違いと、共通の 100 万トークン文脈を 1 枚で掴んでもらいます。上に Fable / Mythos（D-16）が別の段として乗っていることも見せます。

### B. 登場シーン（figure_type: comparison）

- シーン1: Sonnet 5（2026-06-30 公開）— 入力 $2 / 出力 $10（100 万トークンあたり、2026-11 時点）
- シーン2: Opus 5（2026-07-24 公開）— 入力 $5 / 出力 $25（同上）
- 共通値: 文脈 100 万トークン・出力上限 12.8 万トークン
- 上の段: Fable / Mythos（D-16）を点線で示す

## 会話での使い方例

「5 世代から文脈が 100 万トークンになり、長い資料も入りやすくなりました。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Claude 第 5 世代の Sonnet 5 と Opus 5 です。

### 2. うれしさ

文脈 100 万トークンで、長い資料も扱えます。

### 3. 注意点

2026-11 時点では legacy で、更新されません。

### 4. どこで役立つか

長いコードや資料を丸ごと渡す場面です。

### 5. はじめに

Opus の上に別の段（D-16）がある点を見ます。

### 6. 深掘り先

Claude Fable / Mythos、Claude 5.5 系、Claude 4.5 系

## 開発フローでの位置（必須）

1. 用途を見積もる — 長文脈が要るか、軽い作業かを判断します
2. 段を選ぶ — Sonnet 5 か Opus 5 かを決めます
3. 経路を選ぶ — Claude Code や API から使います
4. 移行を確認する — 後続世代への切り替え時期を見ます

## 関連用語

- Claude Code
- Claude 4.5 系
- Claude Fable / Mythos
- Claude 5.5 系

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

- 描く内容: 横に 2 枚のカード（Sonnet 5／Opus 5）を並べ、公開日と価格（2026-11 時点）を注記。下部に「文脈 100 万トークン・出力 12.8 万トークン」の共通帯。カードの上に点線で Fable / Mythos（D-16）の別の段を描く
- 登場人物: 著者キャラクターが 2 枚のカードの上に積み上がった段を見上げる仕草
- 吹き出し・心の声: 著者「文脈が一気に 5 倍。Opus の上にも段が増えたぞ」
- 中央に置くキーワード/ラベル: Claude 5 系＝文脈 100 万トークンが標準になった世代

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1: 天秤アイコン（用途の見積もり）
- Step 2: 2 つのバッジ（Sonnet／Opus）
- Step 3: 経路アイコン（Claude Code／API）
- Step 4: カレンダーアイコン（移行時期の確認）

## コミュニティ補完メモ

- 族の総論の粒度は D-12 Claude 4 系と同じです。5 系の特徴は「文脈 100 万トークンが標準になった」「Opus の上に段が増えた」の 2 点に絞りました。
- Fable / Mythos の詳細は D-16、後続の 5.5 世代は D-17 が担当します。
- 4.5 世代との比較は D-13 を参照してください。

## 出典メモ

- Anthropic「Models overview」https://platform.claude.com/docs/en/about-claude/models/overview — checked 2026-11-06
- Anthropic「Model deprecations」https://platform.claude.com/docs/en/about-claude/model-deprecations — checked 2026-11-06
- Anthropic「Claude Sonnet 5.5」https://www.anthropic.com/claude-sonnet-5-5 — checked 2026-11-06（Sonnet 5 の単価の確認）
- Anthropic「Claude Opus 5.5」https://www.anthropic.com/claude-opus-5-5 — checked 2026-11-06（Opus 5 の単価の逆算確認）

## 備考

モデル名・価格・提供状況は時変情報です。2026-11 時点では Sonnet 5・Opus 5 とも legacy（提供は続くが更新はされない）で、公式は後続の 5.5 世代への移行を案内しています。公式の退役予定日は Sonnet 5 が「2027-06-30 より前にはしない」、Opus 5 が「2027-07-24 より前にはしない」です。Anthropic の API では長文脈の追加料金はないとされます（二次情報）。思考は Adaptive thinking（モデルが考える量を自分で決め、effort で強弱を指示）で、手動で思考予算を渡す旧方式（budget_tokens）は後続モデルでは受け付けません。Opus 5 の Fast mode は研究プレビューで $10 / $50（G-52）。同じ 6 月に Fable 5 / Mythos 5（2026-06-09）が出ており、D-16 で扱います。4 系の旧モデルは整理が進み、Opus 4 と Sonnet 4 は 2026-06-15、Opus 4.1 は 2026-08-05 に退役、Sonnet 4.5 は 2026-11-30 退役予定です。後続世代の固有名は、次回の世代交代時に追記します。
