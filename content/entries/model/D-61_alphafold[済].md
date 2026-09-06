---
# ── 識別・分類 ──
id: D-61
title: AlphaFold
title_reading: アルファフォールド
category: model
subtype: historical

# ── 読者・体験 ──
experience_level: research_only
reader_level: 2-3
importance: C

# ── 誌面形式 ──
figure_type: structure
page_layout: spread_v1

# ── 時変情報 ──
start_date: 2021-07-15
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-08-10

# ── 関係 ──
related_terms:
  - Google DeepMind
  - Demis Hassabis
  - Deep Learning
  - AlphaGo

# ── 制作状態 ──
status: ready
---

# AlphaFold

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## tagline

タンパク質の立体構造を予測する AI です。2024 年のノーベル化学賞につながりました。

## 何をしてくれるか

Google DeepMind が開発しました。アミノ酸の配列だけから、タンパク質がどんな立体形に折りたたまれるかを予測します。実験なら数年かかる構造決定を、計算で大きく短縮しました。

## どこで出会うか

創薬や基礎生物学の研究ニュース、2024 年のノーベル化学賞の報道で名前が挙がります。AlphaFold Protein Structure Database では、予測構造が誰でも無料で参照できます。

## メイン図

### 図の狙い

アミノ酸配列から立体構造が予測される流れと、それが創薬にどうつながるかを掴んでもらう。

### C. 概念図（figure_type: structure）

- 中心に置く概念: アミノ酸配列 → AlphaFold → 立体構造
- 周辺の要素: Google DeepMind／実験による構造決定／創薬・研究への応用
- 関係の描き方: 配列から構造へ変わる過程を矢印でつなぎ、周辺に用途を配置

## 会話での使い方例

「AlphaFold のおかげで、タンパク質の構造解析が一気に速くなりましたよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

タンパク質の立体構造を予測する AI です。

### 2. うれしさ

実験で数年かかる構造解析を大幅に短縮します。

### 3. 注意点

予測はモデルであり、実験での検証も必要です。

### 4. どこで役立つか

創薬の標的探索や酵素の機能解明に役立ちます。

### 5. はじめに

AlphaFold DB で公開構造を眺めてみます。

### 6. 深掘り先

AlphaFold DB、Google DeepMind、タンパク質構造

## 開発フローでの位置（必須）

1. 配列準備 — 知りたいタンパク質のアミノ酸配列を用意します。
2. 構造予測 — AI が配列から立体構造を計算します。
3. 信頼度確認 — スコアで予測の確からしさを見ます。
4. 研究・創薬へ応用 — 構造を仮説検証や薬の設計に役立てます。


## 関連用語

- Google DeepMind
- Demis Hassabis
- Deep Learning
- AlphaGo

<!-- ━━━━━━━━ 著者記入欄(右ページ下段に印刷される／AI は触らない) ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- AI の話なのに、なぜ生物の話が出てくるのか分かりません
- 何がそんなに画期的だったのかが伝わりません
- 自分の仕事と接点があるのか見えません
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 決定的な研究だったと思っています
- 👍 良い点: 使わない選択肢はない、と言われる領域です
- 👎 ダメな点: 計算の分野の外なので実感は薄いです
- 👥 誰向けか: AI の射程を知りたい人みんな向けです
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ(誌面には出さない) ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図(左ページ中段 / figure_type: structure)

- 描く内容: アミノ酸配列(文字列)が AI を通り、リボン状の立体構造模型に変わっていく様子
- 登場人物(いれば): 白衣の研究者
- 吹き出し・心の声: 研究者「実験なら何年もかかる構造が、数時間で分かるなんて…」／AI「配列から立体形を予測しました。」
- 中央に置くキーワード/ラベル: 「配列 → AlphaFold → 立体構造」

### 6視点アイコン(右ページ上段)

- 共通アイコン流用(個別演出が要るときだけ書き足す)

### 開発フロー図(右ページ下段)

- Step 1 のアイコン/絵柄: アミノ酸配列のテキストの束
- Step 2 のアイコン/絵柄: 歯車とらせん構造が重なるアイコン
- Step 3 のアイコン/絵柄: 信頼度スコアのグラフ
- Step 4 のアイコン/絵柄: 実験室・薬瓶のアイコン
- 矢印で示す流れの意図: 配列 → 予測 → 信頼度確認 → 研究応用の流れ


## コミュニティ補完メモ

- D-60 AlphaGo との住み分け: D-60 は囲碁というゲーム AI の事例。D-61 は生命科学(創薬・タンパク質研究)での AI 活用事例として書き分ける
- C-3 Google DeepMind との住み分け: C-3 は組織全体(設立・事業・研究領域)を扱う。D-61 は AlphaFold という個別プロジェクトの技術と歴史的意義に絞る
- C-52 Demis Hassabis との住み分け: C-52 は人物の経歴・思想を扱う。D-61 では受賞の事実にのみ触れ、人物解説はしない
- J-11 Deep Learning との住み分け: J-11 は技術原理そのもの。D-61 は「深層学習を生命科学に応用した事例」として位置づける


## 出典メモ

- DeepMind 公式サイト「AlphaFold」<https://deepmind.google/science/alphafold/> — checked 2026-08-10
- AlphaFold Protein Structure Database(EBI) <https://alphafold.ebi.ac.uk/> — checked 2026-08-10
- Nobel Prize 公式サイト 2024年化学賞 <https://www.nobelprize.org/prizes/chemistry/2024/summary/> — checked 2026-08-10


## 備考

- 2021年公開の AlphaFold2 が精度の転換点。CASP14 コンペティションで実験に匹敵する精度を示した
- 2024年公開の AlphaFold3 はタンパク質と薬の候補分子などの複合体予測に対応を広げ、非商用向けにコードが公開された
- 2024年のノーベル化学賞は、新規タンパク質設計の David Baker と、AlphaFold の Demis Hassabis・John Jumper の 2 組に贈られた
- バイブコーディング業界との直接的な技術的つながりは薄いが、「AI が科学研究を進めた象徴的事例」として D-60 AlphaGo と並べて語られる

**著者の指摘（2026-09-06）**: その分野の研究者からは**「使わないという選択肢はない」**と言われるほどの位置づけ。**ディープラーニングがいちばんうまくハマった応用**であり、決定的な研究だったと思う。タイミングも面白い —— **生成 AI 全盛の少し前、いわば前夜に成果を上げていた**。世代を重ねて発展しており、本命の応用だと考えている。一方で、エキスパートシステムや進化計算のような過去の系譜を我々が見逃してきた面もある、という感覚も併せてある。
