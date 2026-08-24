---
id: D-35
title: Cursor Composer
title_reading: カーソル コンポーザー
category: model
subtype: other_closed
experience_level: hands_on
reader_level: 2-3
importance: C
figure_type: before_after
page_layout: spread_v1
start_date: 2024-01-01
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-30
related_terms:
  - Cursor
  - Claude Code
  - Windsurf
  - Tool Use
status: ready
---

## tagline

Cursor に搭載された複数ファイル横断の自動編集エージェントです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

「〇〇を実装して」と指示するとリポジトリ全体を参照し複数ファイルの差分を生成します。Apply ボタン 1 つで一括反映でき、ファイルをまたぐリファクタも 1 往復で済みます。

## どこで出会うか

Cursor（B-4）のチャットを Composer モードに切り替えると使えます。「Tab 補完とは別の機能」としてバイブコーディング記事や GitHub Copilot（B-5）との比較で話題になります。

## メイン図

### 図の狙い

Tab 補完（1 行提案）と Composer（複数ファイル横断）の違いを対比し、扱えるスコープの広さを示します。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: Tab 補完でファイルを 1 つずつ手直しする
  - 視覚要素（コード or 概念）: 単一ファイルのインライン提案が 1〜3 行だけ現れる図
  - つまずき: ファイルをまたぐ変更は自分でコピーペーストを繰り返す必要がある
- After
  - 状況: Composer に指示を出すと複数ファイルにまたがる差分がまとめて表示される
  - 視覚要素: 3 つのファイルに同時に diff が当たり Apply ボタンが並ぶ図
  - うれしさ: 変更箇所を確認してから一括反映でき、見落としが減ります

## 会話での使い方例

「Composer で複数ファイル横断のリファクタを 1 発で出してもらいました。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

複数ファイルにまたがる編集をエージェントとして自動生成します。

### 2. うれしさ

リポジトリ全体を対象にしたリファクタを 1 指示で完了できます。

### 3. 注意点

Tab 補完と混同されがちですが、別の操作モードです。

### 4. どこで役立つか

機能追加やリネームなど、複数ファイルに波及する変更に向いています。

### 5. はじめに

Cursor の Composer モードが何か、Tab 補完との違いを押さえるところからです。

### 6. 深掘り先

Claude Code、Windsurf Cascade、Tool Use

## 開発フローでの位置（必須）

1. 要件を整理する — 「どのファイルを変えたいか」を自分で大まかに把握します
2. Composer に指示を出す — チャット欄で「〇〇を実装して」と自然文で依頼します
3. 差分を確認する — 生成された複数ファイルの diff をレビューします
4. Apply で反映する — 問題なければ Apply を押して一括反映します

## 関連用語

- Cursor
- Claude Code
- Windsurf
- Tool Use

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- Cursor を有料課金していないと、そもそも出会いません
- コードを見ながら開発する習慣がないと出会いません
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: コーディング系 YouTuber の評判は良いようです
- 👍 良い点: 出来は良いらしいです。触っていないので未確認です
- 👎 ダメな点: 自社でフロンティアモデルを開発していない点が不安です
- 👥 誰向けか: 自分でコードを全て理解して進めたい人向けでしょうか
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左半分に Tab 補完の 1 ファイル操作、右半分に Composer の複数ファイル diff 画面
- 登場人物（いれば）: エディタの前に座って画面を見ている人物（1 名）
- 吹き出し・心の声: Before「このファイルだけ直しても、あとのファイルは自分でやらないと…」、After「3 ファイルまとめて確認して Apply できた！」
- 中央に置くキーワード/ラベル: Composer
- Before / After の対比ポイント: 編集対象が 1 ファイル → 複数ファイル

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ノートとペン（要件整理）
- Step 2 のアイコン/絵柄: チャットバブル（指示入力）
- Step 3 のアイコン/絵柄: 虫眼鏡（差分レビュー）
- Step 4 のアイコン/絵柄: チェックマーク（Apply 反映）
- 矢印で示す流れの意図: 指示 → 生成 → 確認 → 反映の 1 サイクル

## コミュニティ補完メモ

- B-4 Cursor との住み分け：Cursor はエディタ全体（Tab 補完・チャット・Composer を含む）。D-35 Cursor Composer はそのうち複数ファイル横断エージェント機能に絞ったエントリ
- B-7 Claude Code との住み分け：どちらも複数ファイル横断の自律編集だが、Claude Code は CLI ベース、Composer は Cursor GUI 内での操作
- B-6 Windsurf との住み分け：Windsurf の Cascade が競合機能。IDE の違いをコミュニティ補完メモで整理しておく
- 「Tab 補完」との混同：読者のつまずき最頻で、非エンジニアのつまずき欄に著者自身の経験を記入してもらう

## 出典メモ

- cursor.com/features — checked 2026-04-30
- cursor.com/blog — checked 2026-04-30

## 備考

- Cursor の内部モデル（head F と呼ばれる小型〜中型モデル群 + フロンティアモデルの組み合わせ）が Composer を駆動する。モデル詳細は非公開のため「Cursor 独自のモデル群が裏側を担う」と簡潔に述べるにとどめる
- 2024 年ごろから提供。名称変遷（旧 Composer の UI 変更など）は出版前に要確認
- CSV の title を `Cursor Composer (モデル)` から `Cursor Composer` に更新済み
