---
id: F-71
title: ripgrep
title_reading: リップグレップ
category: term_tool
subtype: search
experience_level: hands_on
reader_level: 3-4
importance: D
figure_type: before_after
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - Rust
  - git
  - VS Code
  - bash
status: ready
---

# ripgrep (rg)

## tagline

grep の現代的な代替。Rust 製の高速文字列検索ツールです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

ファイルやディレクトリを横断し、キーワードや正規表現にマッチする行を一覧表示します。Rust と SIMD 命令による並列処理で、grep より 2〜10 倍速く動く場合があります。

## どこで出会うか

VS Code の横断検索バックエンドとして採用されており、エディタ検索の速さを担います。Claude Code の `Grep` ツールも内部で ripgrep を呼ぶため、AI エージェントの調査でも動いています。

## メイン図

### 図の狙い

grep と ripgrep の速度差と `.gitignore` 尊重の違いを対比で示す。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: 従来の grep でリポジトリ全体を検索
  - 視覚要素: `grep -r "keyword" .` → node_modules や `.git` まで走査、時間がかかる
  - つまずき: 結果に不要なファイルが混じり、速度も遅い
- After
  - 状況: ripgrep（rg）で同じ検索
  - 視覚要素: `rg "keyword"` → `.gitignore` を自動尊重、一瞬で結果が出る
  - うれしさ: 誤ヒットが減り、探索が数秒から数十ミリ秒に縮む


## 会話での使い方例

「ripgrep を許可しておくとリポジトリ横断の調査が秒で終わります。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

ファイル横断の文字列検索を高速に実行します。

### 2. うれしさ

`.gitignore` を自動尊重し、不要ファイルへの誤ヒットが減ります。

### 3. 注意点

grep とオプション体系が一部異なるため、慣れが必要なことがあります。

### 4. どこで役立つか

大規模リポジトリでの関数名・定数の一括検索に効きます。

### 5. はじめに

コマンド `rg "検索語"` だけで即使えます。

### 6. 深掘り先

Rust、bash、VS Code


## 開発フローでの位置（必須）

1. リポジトリ調査 — `rg "関数名"` でコードベース全体から該当箇所を素早く洗い出します
2. AI エージェント連携 — Claude Code の Grep ツールが内部で rg を呼びます
3. エディタ検索 — VS Code の検索バックエンドとして Ctrl+Shift+F の速度を支えます
4. 保守・リファクタリング — `--type ts` 等で種別を絞り、変更箇所を特定します


## 関連用語

- Rust
- git
- VS Code
- bash
- grep


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 名前から検索機能だと結びつかず、ちゃんと調べるまで何なのか分かりませんでした。
- AI エージェントの処理履歴で出てくることがあり、ずっと何なのか気になっていました。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: AI エージェントの処理中に見かけて気になっていました。
- 👍 良い点: 検索が速いのが強みで、エージェントの調査も速く終わります。
- 👎 ダメな点: 名前から機能が全くイメージできません。
- 👥 誰向けか: エージェントで開発している人向けです。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左に grep を使う人、右に rg を使う人の対比。左は砂時計が降り注ぐイメージ、右は一瞬で結果が出るイメージ
- 登場人物: 検索中のエンジニア風の人物（1 名）。Before 側は眉をひそめ待ち状態、After 側は満足の表情
- 吹き出し・心の声: Before「node_modules も全部調べてる…遅い」After「.gitignore を無視してくれるから速い！」
- 中央に置くキーワード/ラベル: `rg "keyword"` vs `grep -r "keyword" .`
- Before / After の対比ポイント: 走査対象のファイル量と処理時間の差

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 虫眼鏡
- Step 2 のアイコン/絵柄: ロボット（AI エージェント）
- Step 3 のアイコン/絵柄: VS Code ロゴ風のエディタ
- Step 4 のアイコン/絵柄: スパナ（リファクタリング）
- 矢印で示す流れの意図: 調査→エージェント活用→エディタ検索→保守の順に用途が広がる

## コミュニティ補完メモ

- bash（F-81）との住み分け：bash は shell 全般の文法・実行環境。ripgrep は grep 系ツールの高速代替であり、bash スクリプト内から呼ばれる道具の 1 つとして補完関係にある
- git（F-50）との住み分け：git は版管理。ripgrep は git 管理リポジトリの検索に特化した恩恵（.gitignore 尊重）があり、利用場面が重なる
- VS Code（F-30）との住み分け：VS Code はエディタ全体。ripgrep は VS Code が内部で使う検索エンジンの一部として依存関係にある

## 出典メモ

- [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep) — checked 2026-04-29
- [VS Code: Advanced search options](https://code.visualstudio.com/docs/editor/codebasics#_advanced-search-options) — checked 2026-04-29


## 備考

- コマンド名は `rg`（ripgrep の略）。インストール後は `rg` で呼び出す
- Andrew Gallant（GitHub 名 BurntSushi）が 2016 年に公開
- Claude Code の Grep ツールは内部的に ripgrep を呼ぶ（Claude Code の仕様として公開情報に基づく）
