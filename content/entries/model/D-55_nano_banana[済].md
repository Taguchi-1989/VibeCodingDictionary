---
id: D-55
title: Nano Banana
title_reading: ナノ バナナ
category: model
subtype: image_video
experience_level: partial
reader_level: 2-3
importance: D
figure_type: before_after
page_layout: spread_v1
start_date: 2025-08-01
version_status: active
pricing_note: freemium
evaluation_date: 2026-04-30
related_terms:
  - Imagen
  - DALL-E
  - Stable Diffusion
  - Gemini
status: ready
---

# Nano Banana

<!-- バイブコーディング図鑑 エントリー雛形 v2（2ページ見開き想定、iter 22 準拠） -->

## tagline

Google Gemini 系列の画像編集モデルの愛称です。既存画像の構図を保ったまま部分修正できます。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

画像の構図を崩さず衣装・背景・追加要素だけを差し替えます。正式名称は Gemini 2.5 Flash Image で、LMArena の画像評価で上位を維持しています。

## どこで出会うか

Gemini アプリや Google AI Studio の画像生成画面で出会います。外部サービスの内部モデルとして採用される例もあります。

## メイン図

### 図の狙い

編集前後の画像を並べ、構図が崩れない点を視覚的に示す。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: 商品写真の背景が雑然としている
  - 視覚要素: 商品＋雑多な背景
  - つまずき: 背景だけ差し替えたいが全体再生成になる
- After
  - 状況: 商品の形・質感はそのまま、背景だけ白系スタジオ風に変わる
  - 視覚要素: 同商品＋クリーンな背景
  - うれしさ: 撮り直し不要で複数バリエーションを短時間で用意できる

## 会話での使い方例

「Nano Banana に商品写真の背景だけ差し替えてもらいました。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

既存画像を壊さず部分編集する Google の画像モデルです。

### 2. うれしさ

撮影済み素材を活かしたままバリエーションを量産できます。

### 3. 注意点

愛称と正式名が並立するため、リリースノートでは別の呼称が出ます。

### 4. どこで役立つか

EC 商品画像の背景替えや SNS 用バリエーション生成で実用例があります。

### 5. はじめに

Gemini アプリで画像編集を試すと動作感を一番早く掴めます。

### 6. 深掘り先

Imagen、DALL-E、Stable Diffusion

## 開発フローでの位置（必須）

1. 素材準備 — 編集対象の画像と変更指示テキストを用意します
2. API 呼び出し — Google AI Studio や Vertex AI（バーテックスエーアイ）経由でモデルを指定します
3. プロンプト調整 — 保持したい要素と差し替えたい要素を文章で明示します
4. 出力確認 — 生成結果を確認し、不要な変形がないかチェックします
5. バリエーション展開 — 背景・色・追加要素を変えながら量産します

## 関連用語

- Imagen
- DALL-E
- Stable Diffusion
- Gemini

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 正式名が長く API 設定でどれを選ぶか迷いました。
- 画像生成を頼んでもうまく出ないことがあり不安定に感じました。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象:既存モデルの蓄積進化なのに過大評価されている印象でした
- 👍 良い点:0 からキャラクターを作る用途には十分な性能がありました
- 👎 ダメな点:日本語入力が苦手で、資料作りには使いにくいです
- 👥 誰向けか:クリエイターが案出しに使う用途に向いていると思います
- 後継の Nano Banana 2 や Pro は日本語も上達し、かなり感動しました
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 左に雑然とした背景の商品写真、右に白スタジオ風背景の同商品写真を並置する
- 登場人物（いれば）: EC サイト担当者（女性）が画面を見ている
- 吹き出し・心の声: 「構図そのままで背景だけ変わった！」
- 中央に置くキーワード/ラベル: Nano Banana
- Before / After の場合の対比ポイント: 商品のシルエット・質感は不変、背景のみ差し替え

### 6視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: カメラ（素材写真）
- Step 2 のアイコン/絵柄: クラウド API コネクタ
- Step 3 のアイコン/絵柄: テキスト入力フォーム（プロンプト）
- Step 4 のアイコン/絵柄: 虫眼鏡（確認）
- 矢印で示す流れの意図: 撮影素材 → API 呼び出し → 指示調整 → 確認 → 量産の一方向フロー

## コミュニティ補完メモ

- Imagen（D-51）との住み分け：Imagen はテキストから新規生成が得意。Nano Banana は既存画像の部分編集に強みがある。用途が異なるため競合より補完関係に近い
- DALL-E（D-50）との住み分け：DALL-E は OpenAI 系。サービス選択軸（Google vs OpenAI）での住み分けが主。機能特性も DALL-E は新規生成寄り
- Stable Diffusion（D-54）との住み分け：Stable Diffusion はオープンソース・ローカル実行が特徴。Nano Banana はクラウドマネージド型。導入コストと制御度のトレードオフ

## 出典メモ

- Google Gemini 公式ブログ — checked 2026-04-30
- Google AI Studio 画像生成ドキュメント — checked 2026-04-30
- LMArena 画像評価リーダーボード — checked 2026-04-30

## 備考

- 「Nano Banana」は愛称で、正式名称は Gemini 2.5 Flash Image（後に Gemini 3 Pro Image / Nano Banana Pro と統合予定）。リリースノートでは正式名で記載されることが多く、愛称と正式名が並立する状況が読者の混乱を招きやすい
- 2025 年 8 月時点での情報。モデル統合・名称変更の可能性あり（evaluation_date で管理）
