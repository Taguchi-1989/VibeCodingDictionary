---
id: J-115
title: NPU・AI PC
title_reading: エヌピーユー・エーアイピーシー
category: term_general
subtype: hardware
experience_level: research_only
reader_level: 2-3
importance: C
figure_type: comparison
page_layout: spread_v1
start_date: 2024-05
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-09-06
related_terms:
  - CPU
  - GPU
  - VRAM
  - 量子化
  - Neural Network
status: ready
---

# NPU・AI PC

## tagline

Neural Processing Unit の略。AI 処理に特化した省電力チップと、それを搭載する PC の総称です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

CPU・GPU と並んでノート PC に載る、AI 推論に特化した処理装置です。性能は TOPS（1 秒あたり何兆回の演算をこなせるかの単位）で表され、消費電力を抑えたまま AI 機能を常時動かせます。

## どこで出会うか

PC 売り場やカタログのスペック表で「AI PC」「Copilot+ PC」という表示とともに出会います。対応条件には NPU の TOPS 値やメモリ容量が挙げられ、購入時の比較ポイントとして目にします。

## メイン図

### 図の狙い

NPU が支える「常駐する軽い AI 処理」と、GPU とメモリが支える「大きなモデルの実行」を並べて、NPU さえあれば何でも動くわけではないと掴んでもらいます。

### B. 登場シーン（figure_type: comparison）

- シーン1: NPU — 字幕生成・背景ぼかし・要約などの常駐処理を省電力でこなす
- シーン2: GPU + VRAM — 大きな LLM や画像生成モデルの実行を担う
- シーン3: 「NPU があれば大きなモデルも動く」という誤解と、その訂正
- 並べる基準: 処理の重さと常駐性で NPU と GPU の役割を対比する

## 会話での使い方例

「AI PC の NPU は常駐処理向けで、大きなモデルは結局 GPU 頼みです。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

AI 処理に特化した省電力の演算チップです。

### 2. うれしさ

クラウドに送らず手元で速く動かせます。

### 3. 注意点

大きなモデルの実行は GPU とメモリ量が主役です。

### 4. どこで役立つか

字幕生成や要約などの常駐 AI 機能に向きます。

### 5. はじめに

NPU は大きなモデルの代役ではないと知ることです。

### 6. 深掘り先

GPU、VRAM、量子化

## 開発フローでの位置（必須）

1. 用途確認 — 常駐 AI 機能か大きなモデル実行かを見極めます
2. スペック確認 — カタログの NPU TOPS 値とメモリ容量を見ます
3. 購入・導入 — 条件を満たす AI PC を選び使い始めます
4. 使い分け — 重い処理は GPU やクラウド API に任せます


## 関連用語

- CPU
- GPU
- VRAM
- 量子化
- Neural Network


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 自分の PC に載っているのかどうか、確かめ方が分かりません
- TOPS の数字が大きいことの、実感が湧きません
- CPU・GPU と何が違い、どれが使われるのか分かりません
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: どこまで積まれているのか掴めません
- 👍 良い点: 電池を食わずに AI 機能が動きます
- 👎 ダメな点: 対応チップの範囲が見えにくいです
- 👥 誰向けか: 次に PC を買う人向けです
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: 左に「NPU」ラベルの省電力チップと、字幕生成・背景ぼかし・要約アイコンが常駐して回っている様子。右に「GPU + VRAM」ラベルの大きな箱と、大型モデルが重そうにロードされる様子を対比配置する
- 登場人物: PC 売り場で AI PC のスペック表を見比べている買い物客
- 吹き出し・心の声: 買い物客「NPU があれば大きなモデルも動くと思ってた…」、隣の吹き出しで「常駐処理はここ、大きなモデルは GPU 頼みです」と訂正が入る
- 中央に置くキーワード/ラベル: NPU（常駐・省電力）vs GPU＋メモリ（大型モデル）
- Before / After の場合の対比ポイント: 該当なし（比較図）

### 6視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 天秤（常駐処理 vs 大型モデル実行の見極め）
- Step 2 のアイコン/絵柄: カタログ・スペック表と虫眼鏡
- Step 3 のアイコン/絵柄: PC 本体とレシート
- Step 4 のアイコン/絵柄: 分岐矢印（NPU で処理／GPU・クラウドへ）
- 矢印で示す流れの意図: 用途を先に決めてからスペックを見比べ、購入後も処理を使い分ける流れを示す


## コミュニティ補完メモ

- CPU（J-76）との住み分け: J-76 は汎用処理を担う頭脳チップそのものの解説。NPU は「AI 専用に切り出された省電力の演算装置」として、CPU・GPU と並ぶ第三の処理装置という位置づけで書く
- GPU（J-77）との住み分け: J-77 は大規模な並列演算を担う概念解説。本エントリでは「大きなモデルの実行は GPU とメモリ量が主役」という対比役として GPU を参照するに留め、詳細は J-77 に委ねる
- VRAM（J-70）との住み分け: J-70 は GPU 専用メモリの容量計算が主題。本エントリは「NPU には同種の大容量メモリ勝負は起きない」という文脈でのみ軽く触れる
- 本エントリは PC 売り場・カタログで読者が実際に踏む語という位置づけに絞り、NPU の内部アーキテクチャ（回路構成など）には踏み込まない

## 出典メモ

- Microsoft「Copilot+ PC」— <https://www.microsoft.com/en-us/windows/copilot-plus-pcs> — checked 2026-08-10


## 備考

- Copilot+ PC の条件（NPU 40 TOPS 以上・メモリ 16GB 以上など）は時変情報のため、具体的な数値は evaluation_date 時点の目安として扱います。数値そのものは本文では固定値として断定しません。
- Apple の M シリーズや Qualcomm Snapdragon など、メーカーごとに NPU の呼び方（Neural Engine 等）が異なりますが、本エントリでは総称としての NPU・AI PC を扱います。

**著者の指摘（2026-09-06）**: 「Intel や AMD のどのチップに、どこまで NPU が載っているのか」が見えにくいのが最大の引っかかり。代表的なチップ世代と TOPS の目安が一覧できると価値が上がる（→ 下記「対応チップの現況」に整理）。

### 対応チップの現況（2026-09-06 時点の目安）

著者の「どのチップにどこまで載っているのか」という問いに対する調べ物のメモです。誌面に数値をそのまま載せるかは判断が要ります（時変情報のため）。

| 世代 | NPU 性能の目安 | Copilot+ PC（40 TOPS 以上）の線 |
|---|---|---|
| Intel Core Ultra 第 1 世代（Meteor Lake） | 約 11 TOPS | 届かない |
| Intel Core Ultra 200V（Lunar Lake） | 40〜48 TOPS | 満たす |
| AMD Ryzen AI 7040 | 約 10 TOPS | 届かない |
| AMD Ryzen AI 8040 | 約 16 TOPS | 届かない |
| AMD Ryzen AI 300（XDNA 2 / HX 370） | 約 50 TOPS | 満たす |

- **要点は「NPU が載っている＝Copilot+ PC ではない」**こと。同じ Core Ultra でも第 1 世代は基準の 4 分の 1 ほどで、世代で大きく段差があります。読者のつまずき「自分の PC に載っているか分からない」に対する実質的な答えは、**世代名まで見ないと分からない**、になります
- Copilot+ PC の要件は NPU 40 TOPS 以上 ＋ メモリ 16GB 以上（Microsoft の要件）。2026 年時点では Intel Core Ultra 200V / 300、AMD Ryzen AI 300 / 400、Qualcomm Snapdragon X / X2 が該当します
- 出典: <https://learn.microsoft.com/en-us/windows/ai/npu-devices/>（checked 2026-09-06）、<https://www.microsoft.com/en-us/windows/learning-center/copilot-plus-pcs-windows-pcs-differences>（checked 2026-09-06）
