---
id: C-14
title: AMD
title_reading: エーエムディー
category: person_org
subtype: company
experience_level: research_only
reader_level: 3-4
importance: C
figure_type: comparison
page_layout: spread_v1
start_date: 1969-05-01
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - NVIDIA
  - GPU
  - CPU
  - ROCm
  - 半導体製造プロセス
status: ready
---

# AMD

## tagline

Advanced Micro Devices の略。CPU と GPU を両軸で展開する米国の半導体メーカーです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

CPU（Ryzen / EPYC）と GPU（Radeon / Instinct MI シリーズ）を設計・製造します。AI 推論用 MI300X は HBM 容量が大きく大規模モデル向けに採用が増えています。

## どこで出会うか

データセンターの AI 基盤を調べると「NVIDIA か AMD か」の比較文脈で名前が出ます。GPU クラウドの選択肢や ROCm 対応フレームワークの動作確認の話題でも目にします。

## メイン図

### 図の狙い

NVIDIA と AMD の AI 用 GPU を比較し、ソフトウェア対応と HBM 容量のトレードオフを示す。

### B. 登場シーン（figure_type: comparison）

- シーン1: データセンター担当者が NVIDIA H100 と AMD MI300X の仕様表を並べて検討する場面
- シーン2: エンジニアが ROCm 対応を確認しながら PyTorch 環境を構築する場面
- シーン3: クラウド料金を見て「AMD インスタンスのほうが安い」とコメントする場面
- 並べる基準: GPU 製品の用途（コンシューマ vs データセンター AI）と競合対比

## 会話での使い方例

「MI300X は VRAM 192GB あるので、大きな MoE モデルの推論で AMD を選ぶ例が増えました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

CPU と AI 向け GPU を両方展開する半導体メーカーです。

### 2. うれしさ

NVIDIA 一択だったデータセンター AI に選択肢が生まれます。

### 3. 注意点

CUDA（キューダ）エコシステムは NVIDIA 優位で、ROCm の対応範囲は限られます。

### 4. どこで役立つか

GPU クラウドのコスト比較や MoE 大規模モデルの推論環境選定で参照されます。

### 5. はじめに

Instinct MI シリーズがデータセンター向け、Radeon がコンシューマ向けが基本区分です。

### 6. 深掘り先

NVIDIA、ROCm、GPU

## 開発フローでの位置（必須）

1. 要件定義 — 学習・推論どちらの用途か、必要 VRAM を見積もる
2. GPU 選定 — MI300X vs H100 など HBM 容量と CUDA 対応を比較する
3. 環境構築 — ROCm または CUDA 互換レイヤーでフレームワークを導入する
4. 動作確認 — PyTorch / vLLM などの AMD 対応バージョンを確認して実行する


## 関連用語

- NVIDIA
- GPU
- CPU
- ROCm
- 半導体製造プロセス


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 読み方がわかりません
- CPU と GPU とマザーボードの相性が不安です
- Radeon など製品名も読みにくいです
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: Intel と NVIDIA の対抗馬という印象です
- 👍 良い点: 製造を TSMC に委ね微細化で先行しています
- 👎 ダメな点: 知名度と周辺機器の相性に不安が残ります
- 👥 誰向けか: セカンドベンダーとして使いたい人向けです
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: NVIDIA GPU と AMD GPU を左右に並べた仕様比較表。HBM 容量・CUDA 対応・価格帯の 3 行
- 登場人物: インフラ担当者がパソコン画面で仕様表を見ている
- 吹き出し・心の声: 「VRAM 192GB か…大きいモデルが乗るな」
- 中央に置くキーワード/ラベル: AMD vs NVIDIA（AI GPU 比較）

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: メモ帳・要件定義
- Step 2 のアイコン/絵柄: GPU チップ 2 枚の比較
- Step 3 のアイコン/絵柄: ターミナル・インストール画面
- Step 4 のアイコン/絵柄: チェックマーク・動作確認
- 矢印で示す流れの意図: 上流の要件から GPU 選定 → 構築 → 確認の一直線

## コミュニティ補完メモ

- C-9 NVIDIA との住み分け：C-9 は NVIDIA 全体像（H100 / CUDA エコシステム中心）。C-14 AMD は「対抗軸」として MI シリーズと ROCm の現状を扱う。重複する GPU 比較は C-14 に集約する
- J-77 GPU との住み分け：J-77 は GPU という概念・仕組みの説明。C-14 はメーカーとしての AMD の立ち位置を扱う
- ROCm 単体エントリは現時点で未割当。詳細が必要になれば J 系列への追加を検討

## 出典メモ

- AMD Instinct MI300X 製品ページ — checked 2026-04-30
- AMD ROCm 公式ドキュメント — checked 2026-04-30
- OpenAI AMD MI シリーズ採用発表（2024 年）— checked 2026-04-30

## 備考

- MI300X の市場価格は 1 枚あたり $15,000〜$20,000 程度（2024 年時点）で H100 と同価格帯。「AMD = 安価な代替」というイメージは AI GPU では当てはまらない
- Lisa Su CEO は Jensen Huang（C-59）の親戚にあたるが、両社は別法人で独立した競合関係
- CUDA エコシステムとの互換性は ROCm の HIP レイヤー経由で対応するが、対応ライブラリは CUDA より限定的な場合がある
