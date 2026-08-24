---
# ── 識別・分類 ──
id: F-62
title: GitHub Actions
title_reading: ギットハブ アクションズ
category: term_tool
subtype: ci_cd

# ── 読者・体験 ──
experience_level: partial
reader_level: 2-3
importance: C

# ── 誌面形式 ──
figure_type: workflow
page_layout: spread_v1

# ── 時変情報 ──
start_date: 2019-11-01
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-29

# ── 関係 ──
related_terms:
  - GitHub
  - YAML
  - CI/CD
  - Docker

# ── 制作状態 ──
status: ready
---

<!-- エントリー雛形 v2（2ページ見開き想定、iter 22 準拠） -->

## tagline

GitHub に組み込まれた CI/CD ツールです。push や PR を起点にテスト・デプロイを自動実行します。


<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

`.github/workflows/*.yml` に手順を書くと push や PR を起点にテスト・ビルド・デプロイが自動実行されます。


## どこで出会うか

GitHub の「Actions」タブで確認します。Claude Code が PR を出した後に自動テストを走らせ、失敗時に AI へ戻して修正 PR を作る運用でも使われます。


## メイン図

### 図の狙い

push イベントからワークフローが動き、テスト・デプロイまで流れる全体像を 1 枚で示す。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: 手動でテストとデプロイを実行している
  - 視覚要素: 開発者がターミナルで都度コマンドを打つ場面
  - つまずき: 手順の漏れや環境差が本番障害につながる
- After
  - 状況: push するとワークフローが自動起動
  - 視覚要素: GitHub → Actions → テスト OK → デプロイの流れ図
  - うれしさ: 人為ミスが減り、チーム全員が同じ手順で回せます


## 会話での使い方例

「Actions のテスト失敗ログを Claude に渡すと、修正 PR まで出してくれます。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

push や PR を契機に、テスト・デプロイを自動で実行します。

### 2. うれしさ

繰り返しの手動作業が消え、リリースミスが減ります。

### 3. 注意点

YAML（F-7）のインデントやシークレット未設定が動作不良の主な原因です。

### 4. どこで役立つか

チーム開発の品質維持や、個人プロジェクトの自動公開に使えます。

### 5. はじめに

`on:` でトリガ、`jobs:` でステップを定義する 2 つの概念を押さえます。

### 6. 深掘り先

CI/CD、Docker、GitHub


## 開発フローでの位置（必須）

1. コード変更 — ローカルで実装し GitHub にプッシュします
2. ワークフロー起動 — `.github/workflows/*.yml` が自動で読み込まれます
3. テスト・ビルド実行 — lint・型チェック・ユニットテストが並列で走ります
4. 結果通知 — 成功なら自動デプロイ、失敗なら Logs タブで確認します
5. 修正ループ — 失敗ログを AI に渡して修正 PR を作るサイクルに活用できます


## 関連用語

- GitHub
- YAML
- CI/CD
- Docker


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- エージェントの作業と Actions の自動化の切り分けが難しいです。
- エラーが出て貼り付けるを繰り返す間に 2,000 分の無料枠が溶けた経験があります。
- 性能の低いモデルで回すといきなりうまくいかないことが多いです。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: GitHub を開いたら最初からいた感じです。
- 👍 良い点: ビルドや CI チェックが自動で走るのはありがたいです。
- 👎 ダメな点: 設定次第で 2,000 分の無料枠が一日で溶けます。
- 👥 誰向けか: GitHub を使いながら自動化したい人向けです。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: workflow）

- 描く内容: 開発者が push → GitHub Actions が起動 → テスト合格 → デプロイ完了の横並びフロー
- 登場人物（いれば）: 開発者（ラップトップを前にした人物シルエット）と GitHub ロボット（Octocat 風）
- 吹き出し・心の声: 開発者「push したら勝手に動いてる！」、Actions「テスト通過。デプロイします。」
- 中央に置くキーワード/ラベル: GitHub Actions
- Before / After の場合の対比ポイント: 手動操作の多さ vs. 自動化後の静けさ

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: コードアイコン（{} 括弧）
- Step 2 のアイコン/絵柄: 歯車アイコン（起動）
- Step 3 のアイコン/絵柄: チェックリストアイコン
- Step 4 のアイコン/絵柄: ベルアイコン（通知）
- Step 5 のアイコン/絵柄: ループ矢印（修正サイクル）
- 矢印で示す流れの意図: push から自動実行・通知・修正の一方向サイクル


## コミュニティ補完メモ

- GitHub（F-60）との住み分け：F-60 はリポジトリ管理・コラボ機能全般を扱う。本エントリは Actions の CI/CD 実行機能に絞る
- CI/CD（H-7）との住み分け：H-7 は概念・考え方を説明。本エントリは GitHub Actions という具体ツールの操作に焦点を当てる
- Docker（F-90）との住み分け：F-90 はコンテナ技術全般。本エントリは Actions のジョブが Docker を呼び出す文脈にとどめる


## 出典メモ

- <https://docs.github.com/ja/actions> — checked 2026-04-29
- <https://github.com/marketplace?type=actions> — checked 2026-04-29


## 備考

- パブリックリポジトリは無料。プライベートは月 2,000 分まで無料（Free プラン）。超過分は従量課金。プランにより上限が異なるため、evaluation_date 時点の情報として扱うこと
- YAML のインデントミスが原因のエラーは Logs タブの赤行で確認できる。シークレットは Settings > Secrets and variables > Actions から設定
- `actions/checkout` `actions/setup-node` などマーケットプレイス公開の Action を YAML から `uses:` で呼び出せる
