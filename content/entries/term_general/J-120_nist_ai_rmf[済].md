---
id: J-120
title: NIST AI RMF
title_reading: ニストエーアイアールエムエフ
category: term_general
subtype: ethics_law
experience_level: research_only
reader_level: 3-4
importance: D
figure_type: structure
page_layout: spread_v1
start_date: 2023-01-26
version_status: active
pricing_note: none
evaluation_date: 2026-09-05
related_terms:
  - ISO/IEC 42001
  - ISO/IEC 23894
  - AI 倫理
  - EU AI Act
status: ready
---

# NIST AI RMF

<!-- バイブコーディング図鑑 エントリー雛形 v2 -->

## tagline

NIST AI Risk Management Framework の略。米国 NIST が示す、AI のリスク管理の枠組みです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

組織が AI のリスクを洗い出し、評価し、対応するための考え方を 4 つの機能に整理します。法律ではなく、使うかどうかは任意です。

## どこで出会うか

AI ガバナンスの資料や、海外ベンダーのリスク説明、42001・23894 などの規格を調べる過程で名前が出てきます。米国発の枠組みとして参照されます。

## メイン図

### 図の狙い

GOVERN が土台として全体を覆い、MAP・MEASURE・MANAGE がその上でシステムごとに回る構造を見せます。

### C. 概念図（figure_type: structure）

- 中心に置く概念: NIST AI RMF
- 周辺の要素: GOVERN（土台）／ MAP（文脈把握）／ MEASURE（評価）／ MANAGE（対応）／ Playbook・Roadmap 等の付随物
- 関係の描き方: GOVERN を最下段の帯として全体を覆い、その上に MAP → MEASURE → MANAGE を横並びの矢印で配置

## 会話での使い方例

「NIST AI RMF の GOVERN はどのフェーズにも掛かる土台なんですよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

AI リスクを 4 機能で整理する、米国発の任意の枠組みです。

### 2. うれしさ

リスクの洗い出しと対応を、共通の言葉で説明できます。

### 3. 注意点

準拠しても安全が保証されるわけではありません。

### 4. どこで役立つか

海外取引先へのリスク説明や、規格同士の比較検討です。

### 5. はじめに

まず GOVERN だけ全体に掛かる、の一点を押さえます。

### 6. 深掘り先

ISO/IEC 42001、ISO/IEC 23894、EU AI Act

## 開発フローでの位置（必須）

1. GOVERN — 組織横断の方針と責任を先に定めます
2. MAP — 対象 AI システムごとに文脈とリスクを把握します
3. MEASURE — リスクを定量・定性の両面で評価します
4. MANAGE — 評価結果に基づき対応・事故対応を行います
5. 継続運用 — Playbook や Crosswalk を使い他規格と突き合わせます

## 関連用語

- ISO/IEC 42001
- ISO/IEC 23894
- AI 倫理
- EU AI Act

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 4 つの機能が何を指すのか、名前だけでは分かりません
- 任意なら守らなくてよいのか、扱いに迷います
- ISO の枠組みとどう使い分けるのか見えません
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 4 つの機能の中身を知りたくなります
- 👍 良い点: 任意なので取り入れやすいです
- 👎 ダメな点: 任意ゆえに強制力はありません
- 👥 誰向けか: 枠組みから入りたい組織向けです
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 最下段に「GOVERN」の帯を横一杯に描き、その上に MAP → MEASURE → MANAGE の 3 つの箱を矢印でつなぐ構造図
- 登場人物: リスク管理担当者（男性）が GOVERN の帯を指しながら説明している姿
- 吹き出し・心の声: 「GOVERN だけは全部の土台なんです」
- 中央に置くキーワード/ラベル: NIST AI RMF
- Before / After の場合の対比ポイント: （該当なし）

### 6視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: GOVERN（土台の帯アイコン）
- Step 2 のアイコン/絵柄: MAP（地図アイコン）
- Step 3 のアイコン/絵柄: MEASURE（定規・グラフアイコン）
- Step 4 のアイコン/絵柄: MANAGE（盾アイコン）
- Step 5 のアイコン/絵柄: 継続運用（ループ矢印とドキュメント）
- 矢印で示す流れの意図: GOVERN が全ステップの下敷きであり、MAP〜MANAGE はシステムごとに回ることを示す

## コミュニティ補完メモ

- J-54 ISO/IEC 42001 との住み分け: どちらもガバナンスの枠組み作りが主眼。42001 は第三者認証が取れる国際規格、NIST AI RMF は米国発の任意フレームワークで認証制度ではない
- J-119 ISO/IEC 23894 との住み分け: 23894 は実務のリスクプロセス寄りの guidance、NIST AI RMF はより組織全体の機能整理（GOVERN/MAP/MEASURE/MANAGE）に寄る
- J-50 AI 倫理との住み分け: J-50 は概念論、本エントリは具体的な枠組み・機能構成の説明に絞る

## 出典メモ

- NIST AI RMF Playbook（nist.gov） — checked 2026-09-05
- AIRC AI RMF Resources / Playbook（airc.nist.gov） — checked 2026-09-05
- securiti.ai NIST AI RMF 解説 — checked 2026-09-05

## 備考

- 2023-01-26 公表の NIST AI RMF 1.0 を指す。法律ではなく任意（voluntary）の枠組み
- Playbook・Roadmap・Crosswalk（他フレームワークとの対応表）・分野別視点・生成 AI 向け手引きが付随する
- 米国の政権交代にともなう政策動向の予測は書かない

**著者の指摘（2026-09-06）**: 「4 つの機能に整理する」で止めず、その中身を説明してほしい。

### 4 つの機能（2026-09-06 時点の調べ物）

| 機能 | 担うこと |
|---|---|
| **GOVERN（統治）** | 組織全体に AI リスクを扱う文化・方針・責任分担を敷く。**唯一、組織全体にまたがる機能**で、他の 3 つの上に立ち、それらを繰り返し回せるものにする |
| **MAP（把握）** | 対象の AI システム・使われる文脈・関係者を describe し、枠を決める |
| **MEASURE（測定）** | 定量・定性の両面でリスクを評価する |
| **MANAGE（対応）** | リスク対応に資源を割り当て、実際に管理策を当てる |

- 各機能はカテゴリ／サブカテゴリに分かれ、さらに具体的な行動と成果に落ちます
- **要点は GOVERN の位置づけ**。MAP・MEASURE・MANAGE と横並びの 4 つではなく、GOVERN だけが上に立つ構造です。ここを誌面の図で表せると、ただの 4 分割より格段に伝わります
- 出典: <https://airc.nist.gov/airmf-resources/airmf/5-sec-core/>（checked 2026-09-06）、<https://www.ispartnersllc.com/hubs/nist-ai-rmf/core-functions/>（checked 2026-09-06）
