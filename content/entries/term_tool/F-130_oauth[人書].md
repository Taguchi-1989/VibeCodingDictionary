---
id: F-130
title: OAuth
title_reading: オーオース
category: term_tool
subtype: auth
experience_level: partial
reader_level: 2-3
importance: D
figure_type: workflow
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-29
related_terms:
  - OpenID Connect
  - Slack MCP
  - .env
  - GitHub
status: needs_review
---

# OAuth

## tagline

Open Authorization の略。パスワードを渡さずにアプリ間で権限を委譲する標準仕様です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

「Google でサインイン」を押すと同意画面を経てアクセストークンが元のアプリに返ります。パスワードを直接渡さずに必要な権限だけを委譲できる仕組みです。

## どこで出会うか

Slack MCP や Notion MCP のワークスペース連携で同じ仕組みが動いており、API キーのコピペが不要になります。Claude Desktop でも OAuth フローが使われます。

## メイン図

### 図の狙い

「Google でサインイン」を例に、ユーザー・アプリ・認可サーバーの三者関係と、トークンが渡る流れを示す。

### C. 概念図（figure_type: workflow）

- 中心に置く概念: 認可コードフロー
- 周辺の要素: ユーザー / アプリ（クライアント） / Google（認可サーバー） / アクセストークン
- 関係の描き方: 矢印で「ボタン押下 → 同意画面 → コード発行 → トークン取得」の順に流れを示す


## 会話での使い方例

「Slack MCP は OAuth 経由で接続するので、トークン管理が楽でした。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

アプリ間でパスワードを渡さずに権限を委譲する仕組みです。

### 2. うれしさ

API キーのコピペが不要になり、権限の取り消しも簡単です。

### 3. 注意点

OAuth は「認可」の仕様であり、「認証」は OpenID Connect が担います。

### 4. どこで役立つか

ソーシャルログインや MCP サーバーのサービス連携で使われます。

### 5. はじめに

「Google でサインイン」の裏側がこの仕組みと知るだけで十分です。

### 6. 深掘り先

OpenID Connect、RFC 6749、アクセストークン


## 開発フローでの位置（必須）

1. ボタン押下 — ユーザーが「Google でサインイン」などのボタンを押します。
2. 同意画面 — 認可サーバー（Google 等）がスコープへの同意を求めます。
3. コード発行 — 同意後、認可コードがアプリにリダイレクトで返ります。
4. トークン取得 — アプリがコードをトークンと交換し、API を呼べる状態になります。


## 関連用語

- OpenID Connect
- Slack MCP
- .env
- GitHub


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- そもそも読み方が難しく、「オーオース」と読むのか別の読みかで迷います。
- 認証の話と結びつかず、バックエンド領域の他の言葉と区別がつきません。
- OAuth という文字面と「認証」という意味がなかなか結びつきません。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: Google 認証を実装するのが意外に簡単で、感動を覚えた仕組みです。
- 👍 良い点: Google アカウントとの紐付けがそこまで難しくなく、導入しやすいです。
- 👎 ダメな点: 簡単に連携できる分、怪しいシステムにも紐付けやすい怖さを感じます。
- 👥 誰向けか: Google アカウントで管理する人やエンタープライズ寄りの実装者に向きます。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: workflow）

- 描く内容: 「Google でサインイン」フローを横スクロール矢印で示す。左からユーザー・アプリ・Google の 3 ブロック。
- 登場人物（いれば）: スマホを持つユーザー（非エンジニア想定）
- 吹き出し・心の声: ユーザー「パスワード入れなくてもいいんだ」、アプリ「トークン受け取った」
- 中央に置くキーワード/ラベル: アクセストークン
- Before / After の場合の対比ポイント: （workflow のため省略）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: ボタンをクリックする手のアイコン
- Step 2 のアイコン/絵柄: チェックリスト（同意画面）
- Step 3 のアイコン/絵柄: QR コード or コード片（認可コード）
- Step 4 のアイコン/絵柄: 鍵マーク（トークン取得）
- 矢印で示す流れの意図: ユーザー操作 → 外部サーバー → 元のアプリへ戻る往復


## コミュニティ補完メモ

- OpenID Connect との住み分け: OAuth は認可（何をしていいか）、OpenID Connect は認証（誰か）。両者はセットで語られることが多いが、本エントリは OAuth の認可フローに絞る。
- F-91 .env との住み分け: .env は API キーをローカルで管理する手段。OAuth を使えば .env にシークレットを書かずに済む場面もある点を補足。
- I-13 Slack MCP との住み分け: Slack MCP の接続方式として OAuth が使われる事実を紹介するにとどめ、MCP の詳細は I-13 に委ねる。


## 出典メモ

- RFC 6749 The OAuth 2.0 Authorization Framework — checked 2026-04-29
- OpenID Foundation / openid.net — checked 2026-04-29


## 備考

- OAuth 2.0（RFC 6749、2012 年）が現在の主流。OAuth 1.0 は署名方式が複雑なため廃れている。
- OpenID Connect は OAuth 2.0 の上に認証層を追加した仕様（OIDC）。「サインイン」用途には OIDC を使うのが正確だが、現場では「OAuth でログイン」とまとめて呼ばれることも多い。
