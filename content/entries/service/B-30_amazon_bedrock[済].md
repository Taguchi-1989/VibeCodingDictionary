---
id: B-30
title: Amazon Bedrock
title_reading: アマゾンベッドロック
category: service
subtype: managed_ai
experience_level: research_only
reader_level: 3-4
importance: C
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: paid
evaluation_date: 2026-04-29
related_terms:
  - AWS
  - Claude
  - Llama
  - Vertex AI
  - IAM
status: ready
---

# Amazon Bedrock

## tagline

AWS 上で Claude・Llama など複数モデルを統一 API で呼び出せるマネージドサービスです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

複数ベンダーの基盤モデル（Foundation Model）を AWS の統一 API で呼び出せるサービスです。モデルの切り替えやアクセス管理を AWS コンソールで一元化できます。

## どこで出会うか

AI 機能を AWS 上のシステムに組み込む際に登場します。「Bedrock で Claude を使って要約機能を作る」のように、開発会議やアーキテクチャ図で名前を目にすることがあります。

## メイン図

### 図の狙い

Bedrock という「窓口」を通じて、複数の AI モデルが同じ API で呼び出せる構造を示します。

### C. 概念図（figure_type: structure）

- 中心に置く概念: Amazon Bedrock（統一 API の窓口）
- 周辺の要素: Claude（Anthropic）／Llama（Meta）／Titan（Amazon）／Mistral／利用アプリ
- 関係の描き方: 中央に Bedrock、左側から各モデルが矢印で入り、右側へアプリが API を呼び出す。担当者が「どのモデルにしようか」と選んでいる構図


## 会話での使い方例

「Bedrock 経由で Claude を呼んでいるので、IAM（アクセス管理）の権限設定が必要です。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

AWS 上で複数 AI モデルを統一 API で提供します。

### 2. うれしさ

モデルを切り替えてもコード変更が最小限で済みます。

### 3. 注意点

AWS アカウントと IAM 設定が事前に必要です。

### 4. どこで役立つか

エンタープライズの AI 機能組み込みに向いています。

### 5. はじめに

AWS と API の基本を押さえてから触ると理解しやすいです。

### 6. 深掘り先

AWS、Claude、Vertex AI。

## 開発フローでの位置（必須）

1. AWS アカウント準備 — IAM ロールとアクセス権限を設定します
2. モデル選定 — Bedrock コンソールで使うモデルを有効化します
3. API 呼び出し — SDK 経由でモデルにプロンプトを送ります
4. アプリ組み込み — 返ってきた応答をシステムの機能として使います

## 関連用語

- AWS
- Claude
- Llama
- Vertex AI
- IAM


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- AWS（IAM・コンソール）の知識なしでは API 呼び出しまで辿り着けません
- 2026 年に gpt-oss 等が追加されるまで OpenAI モデルは非対応でした
- ガバナンス面の判断材料が分かりづらく、本番運用の根拠を掴みにくいです
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: セキュアな業務利用を相談すると候補に挙がってきました
- 👍 良い点: エンタープライズのセキュリティ・データ保護要件を満たせるそうです
- 👎 ダメな点: 個人未実装で LiteLLM 等との差別化が掴めていません
- 👥 誰向けか: 企業の情報システム・インフラ担当エンジニア向けです
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に「Amazon Bedrock」のノード。左側から Claude・Llama・Titan・Mistral の各モデルが矢印で入り、右側へ「利用アプリ」が矢印で出る構造。手前に担当者が「どれを使おうか」とモデル一覧を眺めている構図
- 登場人物: 非エンジニアの担当者（タブレットで AWS コンソールのモデル選択画面を眺める人）
- 吹き出し・心の声: 「Claude も Llama も同じ方法で呼べるのか」「モデルを変えてもコードをあまり直さなくていいのか」
- 中央に置くキーワード/ラベル: Amazon Bedrock ＝ AI の統一窓口

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 鍵アイコン — IAM 設定
- Step 2 のアイコン/絵柄: モデル一覧アイコン — モデル選定
- Step 3 のアイコン/絵柄: 矢印と API アイコン — API 呼び出し
- Step 4 のアイコン/絵柄: アプリ画面アイコン — アプリ組み込み
- 矢印で示す流れの意図: 権限設定 → モデル選定 → 呼び出し → 組み込み の順


## コミュニティ補完メモ

- AWS（B-23）との住み分け：B-23 は AWS 全体の傘と代表サービス（EC2/S3/Lambda）を扱います。本エントリは AI モデル呼び出し専用サービスとしての Bedrock に絞ります
- Claude（B-2）/ Llama（D-40）との住み分け：各モデルの詳細はモデルエントリへ。本エントリは「AWS 経由でどう呼ぶか」の視点に絞ります
- Vertex AI（B-27）/ Azure OpenAI（B-26）との関係：「マネージド AI API」軸での競合。各クラウドの AI 基盤サービスとして並列に学ぶ候補です
- エンタープライズ向けの特徴（IAM 統合・データガバナンス・AWS リージョン内データ保持）は本エントリの独自色として簡潔に記載しています


## 出典メモ

- <https://aws.amazon.com/bedrock/> — checked 2026-04-29


## 備考

- モデル対応状況・料金は時変情報です。evaluation_date: 2026-04-29 を持たせています
- experience_level: research_only（著者は利用側の立場）
- 対応モデルは Claude / Llama / Titan / Mistral 等。モデル追加があるため具体的な列挙は最小限にしています
