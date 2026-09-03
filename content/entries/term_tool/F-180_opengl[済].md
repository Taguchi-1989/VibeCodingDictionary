---
id: F-180
title: OpenGL
title_reading: オープンジーエル
category: term_tool
subtype: graphics
experience_level: research_only
reader_level: 3-4
importance: E
figure_type: structure
page_layout: spread_v1
start_date: 1992-01-01
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - WebGL
  - three.js
  - GPU
  - NVIDIA
status: ready
---

# OpenGL

## tagline

Open Graphics Library の略。GPU に命令を送る 3D グラフィックス API の業界標準です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

GPU へ描画命令を送る低レベル API です。3D オブジェクトの描画・変換・テクスチャ合成を担い、CAD・ゲームエンジン・VR などで採用されています。

## どこで出会うか

Blender など 3D ツールの動作基盤として名前が出ます。WebGL は OpenGL ES のブラウザ移植版で AI の 3D 可視化コードでも遭遇します。

## メイン図

### 図の狙い

OpenGL がソフトウェアと GPU をつなぐ「通訳」として機能する構造を示します。

### C. 概念図（figure_type: structure）

- 中心に置く概念: OpenGL API
- 周辺の要素: アプリケーション / シェーダープログラム / GPU / 画面出力 / OpenGL ES / WebGL
- 関係の描き方: アプリ → OpenGL → GPU → 画面出力の縦方向矢印。OpenGL ES・WebGL は派生として右に分岐

## 会話での使い方例

「OpenGL の知識があれば WebGL の AI 出力コードもすぐ読み解けますよ。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

GPU へ描画命令を送る低レベル API の標準です。

### 2. うれしさ

一度習得するとWebGL や OpenGL ES にも知識が転用できます。

### 3. 注意点

Vulkan・Metal・DirectX への移行が進み、新規採用は減っています。

### 4. どこで役立つか

3D 可視化・ゲーム・CAD の動作原理を理解したい場面で役立ちます。

### 5. はじめに

「GPU に命令を送る API」の役割と派生の WebGL を押さえれば十分です。

### 6. 深掘り先

WebGL、Vulkan、three.js

## 開発フローでの位置（必須）

1. 3D 要件の確認 — CAD・VR・可視化など目的に合わせて API を選ぶ
2. 環境セットアップ — OpenGL 対応ドライバとライブラリをインストールする
3. シェーダー記述 — GLSL で頂点・フラグメントシェーダーを書く
4. 描画ループ実装 — 毎フレーム GPU へ命令を送り画面を更新する
5. 出力確認 — ウィンドウまたはブラウザ（WebGL）で描画結果を確認する


## 関連用語

- WebGL
- three.js
- GPU
- NVIDIA


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 名前から 3D グラフィックスとはすぐ結び付かず、何の API か分かりにくいです。
- 高い GPU で動くのか、どの性能を見ればよいか、選定の指針が掴めません。
- CAD やレンダリングの裏側で動いていると認識するまで、出会いどころが見えません。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: CAD を買う際の PC スペック相談で名前を聞き、初めて存在を知りました。
- 👍 良い点: WebGL や派生 API にも知識が転用でき、3D の入口になります。
- 👎 ダメな点: Vulkan 移行が進みつつあり、レガシー寄りになっていく将来性が気になります。
- 👥 誰向けか: ソフトの仕組みを理解したい人と、CAD・3D ツールに触れる人に必要です。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: アプリ → OpenGL API → GPU → 画面出力の縦方向フロー。右側に OpenGL ES・WebGL の派生ラインを添える
- 登場人物（いれば）: 開発者（男性 or 女性）がコードを書いている姿
- 吹き出し・心の声: 「GPU に命令送ったら画面が動いた！」
- 中央に置くキーワード/ラベル: OpenGL

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: チェックリスト（要件確認）
- Step 2 のアイコン/絵柄: レンチ（環境セットアップ）
- Step 3 のアイコン/絵柄: コードファイル（シェーダー記述）
- Step 4 のアイコン/絵柄: 循環矢印（描画ループ）
- Step 5 のアイコン/絵柄: モニター画面（出力確認）
- 矢印で示す流れの意図: 設計 → 実装 → 確認の直線フロー


## コミュニティ補完メモ

- WebGL（F-181）との住み分け：WebGL は OpenGL ES をブラウザ環境へ移植したもの。本エントリはデスクトップ・ネイティブ環境での OpenGL を主軸に扱う
- Vulkan との住み分け：Vulkan は OpenGL より低レベルで高効率。新規プロジェクトでは Vulkan が選ばれることが増えているが、既存ソフト（Blender 等）は OpenGL を継続使用しており当面共存
- three.js（F-14）との住み分け：three.js は WebGL（OpenGL 派生）の上位抽象。本エントリは仕様の源流として言及する程度にとどめる

## 出典メモ

- Khronos Group — OpenGL Overview <https://www.khronos.org/opengl/> — checked 2026-04-30
- Khronos Group — OpenGL 4.6 Release (2017) — checked 2026-04-30

## 備考

- OpenGL 4.6 は 2017 年リリース。以降バージョンアップは行われておらず、新機能追加は Vulkan へ移行している
- Apple は macOS 10.14（Mojave）で OpenGL を deprecated と宣言。Metal が主力
- Android の OpenGL ES はモバイルゲームや AI 推論 UI で現役
- 「Vulkan に置き換わった」と誤解されやすいが、多くの既存アプリは OpenGL で動き続けており共存状態
- **2026-05 時点の状況メモ**：SolidWorks / NX / CATIA / Creo / Maya / Rhino / Archicad / SketchUp など主要 CAD・3D ツールは依然 OpenGL を主採用。Dassault Systèmes（SolidWorks）が AMD と協力して Vulkan 移行を進行中だが、業界全体の移行はまだ先。「レガシー寄りだが現役」が現状で、半年〜1 年単位で再評価が必要
