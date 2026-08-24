---
id: B-5
title: GitHub Copilot
title_reading: ギットハブ コパイロット
category: service
subtype: ai_assistant
experience_level: partial
reader_level: 2-3
importance: B
figure_type: before_after
page_layout: spread_v1
start_date: 2021-10-29
end_date:
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-29
related_terms:
  - VS Code
  - Cursor
  - Tab 補完
  - GitHub
status: ready
---

# GitHub Copilot

<!--
バイブコーディング図鑑 エントリー v2（spread_v1 準拠）
-->

## tagline

今使っているエディタに追加する AI コード補完拡張です。Tab を押すだけで次の行を先読みします。


<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

コードの続きをリアルタイムで提案し、Tab キー 1 つで受け入れられます。関数名・コメント・テスト・ドキュメントまで幅広く補完し、書く量を減らします。

## どこで出会うか

VS Code や JetBrains など既存エディタに拡張として追加して使います。GitHub アカウントでサインインするのが前提で、個人向けの無料枠もあります。

## メイン図

### 図の狙い

Copilot なしで手打ちしていた状態と、Copilot が提案を出している状態を対比して、「追加するだけで補完が手に入る」ことを示します。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: エディタ単体で 1 行ずつ手打ち
  - 視覚要素（コード or 概念）: カーソルが止まった空白行
  - つまずき: 関数の骨格を毎回ゼロから書く手間がかかる
- After
  - 状況: Copilot 拡張を追加した同じエディタで作業
  - 視覚要素: グレーのゴースト文字で次行の提案が表示されている
  - うれしさ: Tab を押すだけで続きが入り、思考の流れを止めずに進めます


## 会話での使い方例

「Copilot が入ってれば Tab で補完できるので、骨格は秒で出ますよ。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

既存エディタに後付けで AI 補完を追加する拡張です。

### 2. うれしさ

エディタを替えずに Tab 補完が使え、書く量が減ります。

### 3. 注意点

GitHub アカウントが必要で、無料枠は補完数に上限があります。

### 4. どこで役立つか

定型コードや繰り返しパターンが多い場面で提案精度が上がります。

### 5. はじめに

VS Code に拡張を入れ、Tab で補完を受け入れてみる段階です。

### 6. 深掘り先

Cursor（B-4）、VS Code（F-30）、GitHub（F-60）


## 開発フローでの位置（必須）

1. 拡張を追加 — VS Code マーケットから GitHub Copilot をインストールします
2. ログイン — GitHub アカウントでサインインし、補完を有効にします
3. コードを書く — 関数名やコメントを書くと次行の提案がグレーで表示されます
4. Tab で受け入れ — 提案が適切なら Tab を押してコードに取り込みます


## 関連用語

- VS Code
- Cursor
- Tab 補完
- GitHub


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 「GitHub」という言葉自体にアレルギーがあり入りにくかったです。
- M365 / Edge / GitHub の各 Copilot の違いが分かりにくかったです。
- 入力コードが学習に使われるか不明でした（ビジネス以上なら使われない仕組みです）。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: Claude Code と比べると使いづらく感じました
- 👍 良い点: アップデートが頻繁で、いまではエージェント的な操作もできるようになりました
- 👎 ダメな点: 寛大だった使用量が 2026 年 6 月からトークンベース課金に下がりました。
- 👥 誰向けか: 企業で自分用のツールを作って使いたい市民開発者向けです。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左半分（Before）に手打ちで止まった開発者、右半分（After）に同じエディタでグレーの補完提案が表示されている様子を対比
- 登場人物: 開発者（PC の前に座り、画面のカーソルで手が止まっている）→ After では Tab キーを押そうとしている同じ人物
- 吹き出し・心の声: Before「また同じ骨格を書くのか…」 / After「Tab 押すだけで入った！」
- 中央に置くキーワード/ラベル: Before = 「手打ち」 / After = 「Copilot 補完」
- Before / After の対比ポイント: 手が止まる回数・Tab 一押しでの受け入れ

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: パズルピース — 拡張追加
- Step 2 のアイコン/絵柄: 鍵マーク — GitHub ログイン
- Step 3 のアイコン/絵柄: 鉛筆＋点線 — 補完提案表示
- Step 4 のアイコン/絵柄: Tab キー — 受け入れ
- 矢印で示す流れの意図: 準備（拡張＋ログイン）→ 実際の補完サイクル（提案→受け入れ）を示す


## コミュニティ補完メモ

- Cursor（B-4）との住み分け：Copilot は「既存エディタへの追加拡張」。Cursor は「エディタ自体が AI 統合済み」。どちらも Tab 補完を持つが入手経路が違う点を本文で触れました
- GitHub 本体（F-60）との住み分け：GitHub のリポジトリ管理・CI/CD 機能は F-60 で扱います。本エントリは Copilot サービス（補完機能）のみです
- Copilot Chat・Agent モードなどの派生機能は本エントリのスコープ外です。拡充が続いているため evaluation_date で管理します

## 出典メモ

- https://github.com/features/copilot — checked 2026-04-29

## 備考

- 料金：個人向け Free（月 2,000 補完まで）/ Pro（月 $10）/ Pro+（月 $19）/ Business・Enterprise の多段プランがあり時変性が高いため、本文では触れず evaluation_date で管理します
- 2021-10 に GitHub Next のプレビュー公開、2022-06 に GA（一般提供開始）。本エントリは現行サービスとしての機能説明を主眼とし、歴史は最小限です
- Microsoft（マイクロソフト）が GitHub を所有しており、OpenAI との連携で GPT 系モデルを補完に使っています。モデル詳細は本エントリのスコープ外です
