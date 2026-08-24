---
id: F-6
title: Markdown
title_reading: マークダウン
category: term_tool
subtype: language
experience_level: partial
reader_level: 2
importance: C
figure_type: before_after
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - HTML
  - README
  - GitHub
  - CommonMark
  - LLM
status: ready
---

# Markdown

## tagline

記号だけで見出し・箇条書き・太字を表現できる軽量な文書記法です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

プレーンテキストに `#` や `-` などの記号を加えるだけで整形された文書をブラウザで表示できます。AI プロンプトや設定ファイルの標準形式として広く使われています。

## どこで出会うか

GitHub のリポジトリ画面・README・Claude Code の設定ファイル CLAUDE.md で日常的に目にします。LLM の回答も Markdown 形式で返ってくることが多いです。

## メイン図

### 図の狙い

「記号だらけのテキスト」が整形された文書へ変わる Before / After を並べて、Markdown の変換の仕組みを直感で掴んでもらいます。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: `#` や `-` の記号が並ぶプレーンテキスト
  - 視覚要素（コード）: `# 見出し` / `- 箇条書き` / `**太字**`
  - つまずき: 記号が邪魔で読みにくく感じる
- After
  - 状況: ブラウザや GitHub の画面で整形・表示された状態
  - 視覚要素: 大きな見出し・箇条書きリスト・太字テキスト
  - うれしさ: HTML を書かなくてもきれいな文書になる

## 会話での使い方例

「CLAUDE.md は Markdown で書けば、見出しも箇条書きも自動で整います。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

記号でテキストを構造化し、整形された文書に変換する軽量記法です。

### 2. うれしさ

HTML を書かなくても見出し・箇条書き・リンクが手軽に表現できます。

### 3. 注意点

方言（GFM・CommonMark 等）が複数あり、見え方がツールで変わります。

### 4. どこで役立つか

README・設定ファイル・AI プロンプトなど、文書を書く場面全般で使えます。

### 5. はじめに

`#` で見出し、`-` で箇条書き、`**太字**` の 3 記法で十分です。

### 6. 深掘り先

GFM（GitHub Flavored Markdown）、CommonMark、Mermaid。

## 開発フローでの位置（必須）

1. ドキュメント作成 — README や設定ファイルを Markdown で書き、構造をわかりやすくする
2. AI への指示 — プロンプトや CLAUDE.md を Markdown で整えると AI が意図を読みやすくなる
3. AI からの受け取り — LLM が返す回答の多くは Markdown 形式で構造化されている
4. レンダリング確認 — GitHub や VS Code のプレビュー機能で表示を確かめる

## 関連用語

- HTML
- README
- GitHub
- CommonMark
- LLM


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- AI 出力に `#` や `※` が混じると Markdown の記法か否かが分かりにくいです。
- 記法として理解するまでに少し時間がかかりました。
- 標準記法と拡張の境界が曖昧な場面があります。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 何のために使うのかよく分からず、`#` などの記法が少し使いにくそうな印象でした。
- 👍 良い点: AI エージェントとの相性が良く、Mermaid や YAML など他の記法も埋め込める点も優秀です。
- 👎 ダメな点: 基本的にはないと思っています。
- 👥 誰向けか: すべての人が習得するべきだと思っています。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左半分にプレーンテキスト（`# 見出し` / `- 箇条書き` / `**太字**` が並ぶ画面）、右半分に整形後の文書画面を並べた Before / After 対比
- 登場人物: 非エンジニアの人物 1 人がノートパソコン画面を見比べている
- 吹き出し・心の声: 「記号を書いただけなのに、ちゃんとした文書になっています。」
- 中央に置くキーワード/ラベル: Markdown → 変換 → 文書
- Before / After の場合の対比ポイント: 記号が並ぶ生テキスト（Before）と整形された見出し・箇条書き画面（After）

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 鉛筆（ドキュメント作成）
- Step 2 のアイコン/絵柄: チャット吹き出し（AI への指示）
- Step 3 のアイコン/絵柄: ロボットアイコン（AI からの受け取り）
- Step 4 のアイコン/絵柄: ブラウザウィンドウ（レンダリング確認）
- 矢印で示す流れの意図: 書く → AI に渡す → AI から受け取る → 表示確認 の 4 ステップ

## コミュニティ補完メモ

- HTML（F-4）との住み分け：HTML はブラウザが直接解釈するマークアップ言語。Markdown は HTML に変換されて表示される上位の記法。HTML の詳細な文法は F-4 へ。
- README（F-59）との住み分け：README はプロジェクトの説明ファイルそのもので、Markdown で書かれることが多い。ファイルとしての役割・書き方は F-59 へ。
- CLAUDE.md（G-20）との住み分け：CLAUDE.md は Claude Code 向けの設定ファイル。Markdown 形式で書くが、設定ファイルとしての意味は G-20 へ。
- GFM（GitHub Flavored Markdown）はテーブル・チェックボックスなど GitHub 独自の拡張を含む方言。本エントリは記法の基礎に絞り、GFM の拡張は深掘り先に留める。
- Mermaid はコードブロックで図を描く拡張記法。GitHub や一部の Markdown レンダラーで対応しているが、本エントリのスコープ外として深掘り先に留める。

## 出典メモ

- daringfireball.net/projects/markdown — checked 2026-04-29
- CommonMark Spec: <https://spec.commonmark.org> — checked 2026-04-29

## 備考

- Markdown は 2004 年に John Gruber が公開した軽量マークアップ言語。実装が複数あり CommonMark が仕様統一を試みている。
- LLM が回答を Markdown で返す挙動は、モデルや API の設定で変わる時変情報。本エントリは記法の特性に絞り、モデル依存の挙動差分には踏み込まない。
- GFM（GitHub Flavored Markdown）は CommonMark の上位互換で、GitHub が定義。テーブル・打ち消し線・自動リンクなどを追加している。
