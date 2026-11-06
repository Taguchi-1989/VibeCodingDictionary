---
id: D-16
title: Claude Fable / Mythos
title_reading: クロード フェイブル ミトス
category: model
subtype: anthropic
experience_level: partial
reader_level: 3
importance: B
figure_type: structure
page_layout: spread_v1
start_date: 2026-06-09
end_date:
version_status: active
pricing_note: paid
evaluation_date: 2026-11-06
last_audited: 2026-11-06
related_terms:
  - Claude Mythos Preview
  - トラステッドアクセス
  - Claude 5 系
  - Claude 5.5 系
status: needs_review
---

# Claude Fable / Mythos

## tagline

同じモデルに別の安全装置をかけた 2 つの版。使える相手が違います。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

Fable（寓話）は一般提供、Mythos（神話）は検証済みの組織だけが使える版です。中身は同じモデルで、安全装置の強さが違います。Opus の上の段に当たります。

## どこで出会うか

Fable は API のほか、AWS・Google Cloud・Microsoft Azure でも使えます。Mythos は検証プログラムの承認組織が対象です。公式は、まず Opus 5.5 を試し、足りないときに Fable を案内しています。

## メイン図

### 図の狙い

1 つのモデル本体から出口が 2 本あり、誰でも通れる扉（Fable）と検問つきの扉（Mythos）に分かれる構造を見せます。「中身は同じ、許す範囲が違う」を伝えます。

### B. 登場シーン（figure_type: structure）

- 中央: モデル本体（Fable 5 / Mythos 5 は 2026-06-09 公開、5.1 は 2026 年 9 月公開）
- 左の出口: Fable — 誰でも通れる扉。サイバー面では脆弱性を見つけられるが攻撃コードは作らない
- 右の出口: Mythos — 検問つきの扉。CVP・LSVP の承認組織のみ
- 共通値: 文脈 100 万トークン・出力 12.8 万トークン・入力 $10 / 出力 $50（2026-11 時点）

## 会話での使い方例

「Fable と Mythos は同じモデルで、安全装置と使える相手が違うそうです。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

同じモデルを、相手に応じて 2 通りに出します。

### 2. うれしさ

一般は安全に使え、専門家は深く使えます。

### 3. 注意点

Mythos は申請と審査が要り、誰でも使えません。

### 4. どこで役立つか

高度な開発や、セキュリティ調査の場面です。

### 5. はじめに

まず Opus 5.5 を試し、足りなければ Fable です。

### 6. 深掘り先

トラステッドアクセス、Claude Mythos Preview

## 開発フローでの位置（必須）

1. まず Opus 5.5 で試す — 多くの用途はここで足ります
2. 足りなければ Fable — effort を上げても届かない場合です
3. 専門業務は Mythos — 検証プログラムの承認が前提です
4. 提供範囲を確認する — 組織や国の条件を見ます

## 関連用語

- Claude Mythos Preview
- トラステッドアクセス
- Claude 5 系
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

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に 1 つのモデル本体（箱）。そこから出口が 2 本。左は開いた扉（Fable）、右は検問所つきの扉（Mythos）。右の扉の前に「CVP / LSVP」の札を持つ係員を置く
- 登場人物: 著者キャラクターが左の扉を通り、右の扉の前では専門家が身分証を見せている
- 吹き出し・心の声: 著者「中身は同じなのに、通れる扉が違うのか」／係員「身元と目的を確認します」
- 中央に置くキーワード/ラベル: 同じモデル、別の安全装置

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1: Opus 5.5 のバッジ（まず試す）
- Step 2: Fable の開いた扉
- Step 3: Mythos の検問つき扉
- Step 4: 地図アイコン（提供範囲の確認）

## コミュニティ補完メモ

- 前身の Claude Mythos Preview（D-14、2026-04 発表、Project Glasswing 経由の限定提供）は、2026-06-09 に非推奨になりました。本エントリはその後継にあたります。
- 検証済みの組織だけに開く提供方式の一般論は J-151 トラステッドアクセスが担当します。本エントリは Anthropic の Fable / Mythos に絞ります。
- 5 系の総論は D-15、5.5 世代は D-17 を参照してください。

## 出典メモ

- Anthropic「Claude Fable and Mythos 5.1」https://www.anthropic.com/claude-fable-and-mythos-5-1 — checked 2026-11-06
- Anthropic 公式ドキュメント「Fable 5 overview」https://platform.claude.com/docs/en/models/fable-5/overview — checked 2026-11-06
- Anthropic「Cyber Verification Program」https://www.anthropic.com/news/cyber-verification-program — checked 2026-11-06

## 備考

モデル名・価格・提供状況は時変情報です。公式は Fable と Mythos を「same model with different safeguards」と説明しています。Mythos 5.1 は 2026-11 時点で米国の組織に限定されています。Fable 5.1 / Mythos 5.1 は 2026 年 9 月公開で、価格は据え置き、キャッシュ読み出しを 75% 値下げし、典型的な使い方で約 25% 安くなると説明されています。公式の退役予定日は「2027-09-01 より前にはしない」で、Anthropic のニュース一覧の掲載日は 2026-09-15 のため、日付は月までで書いています。思考は常時オンで、effort の既定は high です。Project Glasswing は 2026-10-06 に Cyber Verification Program（CVP）へ統合され、CVP は Defense / Red Team / Specialized の 3 段に再編されました。Glasswing 参加組織は 2026-04〜07 に検証済み脆弱性 12 万 9,000 件以上を報告しています。Mythos 5 は 2026-06-12 に一時提供停止、輸出規制の解除を受けて 2026-07-01 に再開と報じられています（二次情報）。
