---
id: F-38
title: Markdown All in One
title_reading: マークダウン オール イン ワン
category: term_tool
subtype: editor_ext
experience_level: hands_on
reader_level: 2-3
importance: D
figure_type: before_after
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - Markdown
  - VS Code
  - Markdown Preview Enhanced
  - Mermaid
status: ready
---

# Markdown All in One

## tagline

VS Code で Markdown 編集補助を一括提供する定番拡張機能です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

VS Code（F-30）に Markdown の編集補助を追加します。Ctrl+B で太字、Enter で箇条書き継続、目次の自動生成、テーブル整形など反復作業をまとめて引き受けます。

## どこで出会うか

VS Code の拡張機能一覧で「Markdown」と検索すると上位に出てきます。README や設計ドキュメントを書く場面、バイブコーディングで AI が生成した大量のマークダウンを整形する場面で役立ちます。


## メイン図

### 図の狙い

拡張なしと拡張ありの編集体験の差を、同じ Markdown ファイルを操作するシーンで対比します。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: Markdown All in One なし
  - 視覚要素: 目次を手入力、箇条書きのハイフンを毎行打つ、テーブルの縦棒を手で揃える
  - つまずき: 単純作業に時間がかかり、書くリズムが崩れる
- After
  - 状況: Markdown All in One 導入済み
  - 視覚要素: `/toc` コマンドで目次が一括生成、Enter で箇条書きが続く、テーブル保存時に自動整形
  - うれしさ: 書く内容に集中でき、AI が生成した大量のマークダウンも短時間で整えられる


## 会話での使い方例

「Markdown All in One を入れてから目次の更新がとても速くなりました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

VS Code で Markdown の編集補助を一括提供する拡張です。

### 2. うれしさ

目次生成・箇条書き継続などの反復作業が減ります。

### 3. 注意点

プレビューは最小限で、凝った表示には F-35 との併用が必要です。

### 4. どこで役立つか

README・設計書など Markdown 量が多い編集作業に効きます。

### 5. はじめに

目次自動生成と Ctrl+B の動作を確かめると理解できます。

### 6. 深掘り先

Markdown Preview Enhanced（F-35）、Mermaid（F-140）


## 開発フローでの位置（必須）

1. 環境構築 — VS Code に拡張をインストールして有効化します
2. 文書作成 — Ctrl+B / Ctrl+I などのショートカットで書き進めます
3. 構造整理 — `/toc` コマンドで目次を自動生成・更新します
4. 仕上げ — テーブル整形コマンドで列幅を揃えてから保存します


## 関連用語

- Markdown
- VS Code
- Markdown Preview Enhanced
- Mermaid


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 目次生成は便利ですが、LaTeX や Mermaid 入り PDF 印刷でうまくいかずハマりやすかったです。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: Word にある機能を Markdown でも使えるのが便利だな、という感覚でした。
- 👍 良い点: 自分で触るときの細かい効率化につながります。
- 👎 ダメな点: できないことがあり、楽な別の方法もあるため最近は使う機会が減っています。
- 👥 誰向けか: Markdown を自分で直接書いて管理したい人向けです。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左半分に「拡張なし」のエディタ画面（手でハイフンを打つ人物）、右半分に「拡張あり」のエディタ画面（Enterキーを押すだけで箇条書きが続く人物）
- 登場人物: エディタの前でキーボードを打つ人（1 名）。Before と After で同じ人物を配置
- 吹き出し・心の声: Before「またハイフンを手打ちしないと…」、After「Enter を押すだけで続く！」
- 中央に置くキーワード/ラベル: 「Markdown All in One」
- Before / After の場合の対比ポイント: 同じ箇条書き追加操作でも手間が全然違う

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: パズルピースのインストールアイコン
- Step 2 のアイコン/絵柄: キーボードショートカットアイコン
- Step 3 のアイコン/絵柄: 目次リスト自動生成アイコン
- Step 4 のアイコン/絵柄: テーブル整形・チェックマークアイコン
- 矢印で示す流れの意図: インストールから実際に整形完了するまでの一連の作業フロー

## コミュニティ補完メモ

- Markdown Preview Enhanced（F-35）との住み分け：F-38 は編集補助（ショートカット・目次・整形）、F-35 はプレビュー特化（Mermaid 描画・PDF 出力）。両方同時に導入するのが一般的な使い方なので、「どちらを入れるべきか」よりも「両方入れる」と案内する
- VS Code（F-30）のエントリでは「拡張機能を入れると便利になる」として本エントリを参照案内できる
- Mermaid（F-140）との関係：F-38 はプレビュー描画はしないが、Mermaid 記法のショートカットを補助するケースがある。詳細は F-35 と F-140 に委ねる

## 出典メモ

- VS Code Marketplace — Markdown All in One — `https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one` — checked 2026-04-30

## 備考

- インストール数は 1,500 万超（2026-04-30 時点）。時変情報のため evaluation_date で管理
- 無料拡張（pricing_note: none）
- バイブコーディングで AI が大量の Markdown を生成する場面では、目次更新やテーブル整形の自動化が特に効く場面が増えている
