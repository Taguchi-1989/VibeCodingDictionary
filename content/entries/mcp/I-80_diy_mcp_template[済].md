---
id: I-80
title: 自作 MCP のテンプレ
title_reading:
category: mcp
subtype: diy
experience_level: hands_on
reader_level: 3-4
importance: C
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-08-23
related_terms:
  - MCP
  - MCP Server
  - MCP SDK
  - MCP Transport
  - MCP の登録・設定
status: ready
---

# 自作 MCP のテンプレ

## tagline

自分で MCP Server を組み立てるときに使う、最小構成のひな型です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

MCP は Host／Client／Server の 3 層で動き、自分で作るのは Server です。公式 SDK を使えば、Tools（操作）・Resources（データ）・Prompts（定型の頼み方）の 3 種類を数十行から公開できます。

## どこで出会うか

欲しい連携が見当たらないときに、自作の入り口として登場します。自分の PC だけで使うなら標準入出力（stdio）でつなぐのが手軽で、チームで共有したりリモートに置くなら HTTP を使います。

## メイン図

### 図の狙い

MCP Server の中に Tools・Resources・Prompts という 3 つの引き出しがあり、公開の仕方を選べることを 1 枚で見せます。ローカルなら stdio、共有なら HTTP という分かれ道も添えます。

## 会話での使い方例

「自作するなら、まず Tools を 1 個だけ公開するところから始めるのが安全です。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

自分で MCP Server を組む、公式テンプレの土台です。

### 2. うれしさ

数十行から Tool を公開でき、着手が軽いです。

### 3. 注意点

SDK は改訂が速く、細部は公式で確認が要ります。

### 4. どこで役立つか

社内 API や手元のスクリプトを AI に繋ぐ場面です。

### 5. はじめに

公開できるのは Tools・Resources・Prompts の 3 種類です。

### 6. 深掘り先

MCP SDK、MCP Server、MCP Transport

## 開発フローでの位置（必須）

1. 公開したい操作を決める — Tool・Resource・Prompt のどれにするか考えます
2. 公式 SDK を選ぶ — TypeScript や Python など言語ごとの SDK から選びます
3. ローカルで動作確認する — stdio でつなぎ、公式サンプルどおりに試します
4. 公開範囲を決める — 自分だけなら stdio のまま、共有するなら HTTP に切り替えます

## 関連用語

- MCP
- MCP Server
- MCP SDK
- MCP Transport
- MCP の登録・設定


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- テンプレの中身が何を意味するのか分かりません
- 仕様が変わると作り直しなのか不安です
- 自分で作る必要があるのか判断できません
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 中身より、仕組みを知るほうが大事です
- 👍 良い点: 書くこと自体はエージェントに任せられます
- 👎 ダメな点: 仕様が変わると互換性が切れます
- 👥 誰向けか: 自前の連携を作りたい人向けです
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に「MCP Server（自作）」の箱を置き、箱の中に Tools／Resources／Prompts の 3 つの引き出しラベルを並べる。箱の下から線が 2 本に分岐し、それぞれ「ローカル: stdio」「共有: HTTP」に繋がる
- 登場人物: 開発者が箱（Server）を自分で組み立てている
- 吹き出し・心の声: 「作るのは Server だけ。中身は 3 種類から選ぶ」
- 中央に置くキーワード/ラベル: 自作 MCP ＝ Tools／Resources／Prompts を公開する Server

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: チェックリスト（公開する操作を決める）
- Step 2 のアイコン/絵柄: パッケージ箱（SDK を選ぶ）
- Step 3 のアイコン/絵柄: ターミナル（ローカル動作確認）
- Step 4 のアイコン/絵柄: 分岐矢印（公開範囲を決める）


## コミュニティ補完メモ

- **I-81 MCP の登録・設定との住み分け**：本エントリ（I-80）は「自分で MCP Server を作る」側。I-81 は「作った、あるいは配布されている MCP Server を使えるようにする」側（登録・設定の手続き）。作る／使えるようにする、で明確にスコープを分けます。
- **I-1 MCP との住み分け**：Host／Client／Server の関係や MCP 全体の概念説明は I-1 に譲り、本エントリは「自作するときに何を組み立てるか」に絞ります。
- **I-2 MCP Server との住み分け**：Server 一般の役割・仕組みは I-2 の担当。本エントリは自作の手順・構成に集中します。
- **I-4 MCP Transport との住み分け**：stdio と HTTP の選び方の詳細は I-4 が深掘り先。本エントリでは「ローカルなら stdio、共有なら HTTP」の 1 行に留めます。
- **I-5 MCP SDK との住み分け**：SDK 自体の中身（JSON-RPC 処理やライフサイクル管理）は I-5 に譲り、本エントリは自作の全体像に絞ります。

## 出典メモ

- Model Context Protocol 公式サイト <https://modelcontextprotocol.io/> — checked 2026-08-23
- MCP 公式 SDK（GitHub, modelcontextprotocol 組織）<https://github.com/modelcontextprotocol> — checked 2026-08-23

## 備考

MCP の SDK は改訂が速い領域です。Python SDK は 2026-07 に v2 が出てクラス名が変わり、SSE（Server-Sent Events）は 2025-03 の改訂で Streamable HTTP に置き換わりました。特定のクラス名やコマンドの細部はここでは扱わないので、着手時には必ず公式ドキュメントを確認してください。

**著者の指摘（2026-09-06）**: 自作の MCP サーバーを実際に立てている立場から。**テンプレそのものは変わってきており、互換性が切れたこともあった**という認識。

**そのうえで、著者の結論は「そこは大きな問題ではない」。****テンプレを書くこと自体はエージェントに任せられる**からです。大事なのは 2 つ。

1. **テンプレとしてどういう要素が必要か、仕組みとして知っておくこと**
2. **出てきたものが自分の意図と合っているかをチェックできる状態にしておくこと**——バリデーションの仕組みを用意しておけばよい

**「書けること」ではなく「確認できること」が価値になっている**、という転換が、この項目の読ませどころ。（J-139 説明可能性で述べた「責任＝承認プロセスを回すこと」と同じ構図。）
