---
# ── 識別・分類 ──
id: H-8
title: DevOps
title_reading: デブオプス
category: workflow
subtype: methodology

# ── 読者・体験 ──
experience_level: research_only
reader_level: 3-4
importance: C

# ── 誌面形式 ──
figure_type: structure
page_layout: spread_v1

# ── 時変情報 ──
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30

# ── 関係 ──
related_terms:
  - CI/CD
  - GitHub Actions
  - Scrum
  - Docker
  - IaC

# ── 制作状態 ──
status: ready
---

# DevOps

## tagline

開発（Development）と運用（Operations）を融合する文化・実践です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

開発と運用が連携し、障害対応・デプロイ・監視を一体で回せるようにします。CI/CD や IaC が主な実装手段で、リリースの速さと安定を両立させます。

## どこで出会うか

「DevOps エンジニア」の求人票や GitHub Actions の設定ファイルで出会います。AI が PR 作成から自動デプロイまで回すパイプラインとも相性がよい場面です。

## メイン図

### 図の狙い

開発と運用が分断されていた状態から、ループして回る状態への変化を示します。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: 開発と運用が別チームで壁がある
  - 視覚要素: 「開発」と「運用」が壁で分断、リリースが月 1 回
  - つまずき: 「リリースしたら後は運用の仕事」と責任が分断されている
- After
  - 状況: 開発・テスト・デプロイ・監視がループする
  - 視覚要素: CI/CD パイプラインが円環で描かれ、AI が途中で介入
  - うれしさ: 障害検知から修正・再デプロイまでが半自動で回る

## 会話での使い方例

「DevOps の自動化に Claude Code を組み込んだら、障害対応が早くなりました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

開発と運用の壁をなくし、デプロイを高速・安定化させます。

### 2. うれしさ

リリース頻度が上がり、障害から回復するまでの時間が短くなります。

### 3. 注意点

「DevOps エンジニア」は職種名で、DevOps 自体は文化・働き方を指す点に注意です。

### 4. どこで役立つか

チームが分断しがちな中〜大規模プロダクトの運用改善で効果が出ます。

### 5. はじめに

CI/CD と IaC が DevOps の中核ツールであると押さえれば十分です。

### 6. 深掘り先

GitOps、SRE、DevSecOps

## 開発フローでの位置（必須）

1. コード変更 — 開発者が機能追加・バグ修正のコードをプッシュします
2. CI（継続的インテグレーション）— テスト・静的解析が自動で走ります
3. CD（継続的デリバリー）— 承認後にステージング・本番へ自動デプロイします
4. 監視・ロギング — 本番の挙動を計測し、異常をアラートで検知します
5. フィードバック — 障害・改善点を次の開発サイクルに取り込みます


## 関連用語

- CI/CD
- GitHub Actions
- Docker
- Scrum
- IaC


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 2025 年前後で DevOps の意味合いが変わってきている感覚があり、文脈の取り方が難しいです。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 理想論だな、できたらいいな、という感想でした
- 👍 良い点: 運用側の知見が開発側に継続的に反映され、改善ループが回りやすくなります。
- 👎 ダメな点: 案件ベースの仕事だとプロジェクトの区切りが付けづらくなります。
- 👥 誰向けか: 自社サービスを内部で保守し続ける組織向けで、案件ベースとは相性が悪い印象です。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 左側に「開発チーム（コードを書く人）」右側に「運用チーム（サーバを守る人）」が向き合い、中央に CI/CD のループ矢印が描かれる構成
- 登場人物: 開発者（ノートPC）と SRE/運用担当（モニター画面）の 2 名
- 吹き出し・心の声: 開発者「デプロイ完了しました」運用担当「監視ダッシュボード、正常です」
- 中央に置くキーワード/ラベル: DevOps ループ（Plan → Code → Build → Test → Release → Deploy → Operate → Monitor）

### 6視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: コードエディタ画面
- Step 2 のアイコン/絵柄: チェックマーク付きパイプライン
- Step 3 のアイコン/絵柄: ロケット打ち上げ
- Step 4 のアイコン/絵柄: グラフ・アラートベル
- Step 5 のアイコン/絵柄: サイクル矢印
- 矢印で示す流れの意図: 一方通行ではなく円環であることを強調する


## コミュニティ補完メモ

- H-7 CI/CD との住み分け: CI/CD は DevOps を実現するための具体的な自動化手法。DevOps は文化・組織論まで含む上位概念
- H-5 Scrum との住み分け: Scrum はスプリント単位の開発手法。DevOps は開発〜運用の連携まで含む広い概念。重なる部分あり
- GitOps（未収録）: git リポジトリを運用の「正」とする DevOps 派生実践
- SRE（Site Reliability Engineering）との関係: Google 発の運用エンジニアリング手法。DevOps の実装形態のひとつとして位置づけられることが多い
- DevSecOps / MLOps / AIOps: DevOps にセキュリティ・機械学習・AI 運用を組み込む派生概念。本エントリでは概念紹介にとどめ、詳細は別エントリ想定

## 出典メモ

- DevOpsDays 公式サイト <https://www.devopsdays.org/> — checked 2026-04-30
- Patrick Debois / 2009 Velocity Conference — checked 2026-04-30

## 備考

- DevOps は 2009 年、Patrick Debois が「DevOpsDays」を主催したことが起点とされる。同年の Velocity カンファレンス「10+ Deploys Per Day」プレゼンも文化的起爆剤
- 「DevOps エンジニア」という職種名は市場で普及しているが、DevOps 本来の意図は「役職」より「働き方・文化」。読者の混乱ポイントとして左ページではあえて触れていない（著者コメント欄に誘導）
- AIOps（AI による IT 運用支援）は本エントリのスコープ外。深掘り先の候補として備考に記録
