---
id: E-54
title: ベンチマークの飽和
title_reading: ベンチマークのほうわ
category: benchmark
subtype: general
experience_level: research_only
reader_level: 2-3
importance: B
figure_type: timeline
page_layout: spread_v1
version_status: active
pricing_note: free
evaluation_date: 2026-11-13
last_audited: 2026-11-13
related_terms:
  - Humanity's Last Exam
  - MMLU
  - Terminal-Bench
  - グッドハートの法則
status: needs_review
---

# ベンチマークの飽和

## tagline

上位モデルが満点近くに並び、差が測れなくなることです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

試験が簡単になりすぎて、上位モデルの点が天井に張りつく状態を指す言葉です。差が見えなくなるので、その試験は役目を終え、より難しい後継の試験にバトンが渡されます。

## どこで出会うか

新モデルの発表記事で、昔の試験が表から消え、聞き慣れない新しい試験が並ぶ場面です。「この試験でもう 7 割を超えた」といった説明でも出てきます。

## メイン図

### 図の狙い

古い試験が天井に当たるたび、難しい試験へバトンが渡る階段を見せます。右端で「知識の試験」から「仕事の試験」へ重心が移ることも添えます。

### C. 概念図（figure_type: timeline）

- 左から右へ上る階段: MMLU・HumanEval・GSM8K（天井） → MMLU-Pro・SWE-bench Verified → Humanity's Last Exam など
- 右端: 知識の試験 → 仕事の試験（長い作業をやり切れるか）
- 例示ラベル「2026-11 時点: Humanity's Last Exam（ツールあり）は 7 割台」

## 会話での使い方例

「HLE は飽和気味なので、Terminal-Bench で見ますよね。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

試験が差を測れなくなった状態を表します。

### 2. うれしさ

古い数字を鵜呑みにしない目が持てます。

### 3. 注意点

満点に近い試験の点差は、能力差と限りません。

### 4. どこで役立つか

発表記事の比較表を読み解くときに役立ちます。

### 5. はじめに

引かれた試験が「まだ効く試験か」を見ることです。

### 6. 深掘り先

MMLU、Humanity's Last Exam、グッドハートの法則

## 開発フローでの位置（必須）

1. 記事で点を見る — 発表記事のスコア表を開く
2. 天井を確かめる — 上位が満点近くに並んでいないか見る
3. 試験の年を調べる — 公開時期と後継の有無を確認する
4. 別の物差しを探す — 新しい試験や仕事型の試験を見る
5. 自分の仕事で試す — 手元の作業で最後に確かめる

## 関連用語

- Humanity's Last Exam
- MMLU
- Terminal-Bench
- グッドハートの法則

<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 
- 
- 
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 
- 👍 良い点: 
- 👎 ダメな点: 
- 👥 誰向けか: 
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: timeline）

- 描く内容: 左下から右上へ上る階段。段ごとに試験名の札（MMLU／HumanEval／GSM8K → MMLU-Pro／SWE-bench Verified → Humanity's Last Exam）。各段の天井に「満点」の線。右端に矢印で「知識の試験 → 仕事の試験」
- 登場人物（いれば）: 読者キャラ（非エンジニア）が階段の途中で天井を見上げ、試験官キャラがバトンを渡している
- 吹き出し・心の声: 読者「みんな満点近い。これじゃ差が分からないね」／試験官「次の試験へどうぞ」
- 中央に置くキーワード/ラベル: 天井に当たったらバトンタッチ ／ 例示「2026-11 時点: Humanity's Last Exam（ツールあり）74.2%（Claude Fable 5.2）、Remote Labor Index 41.3%」

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: スコア表
- Step 2 のアイコン/絵柄: 天井の線と並ぶ点
- Step 3 のアイコン/絵柄: カレンダー
- Step 4 のアイコン/絵柄: 新しい試験の札
- Step 5 のアイコン/絵柄: 手元で試す PC


## コミュニティ補完メモ

- E-26 Humanity's Last Exam との住み分け：個別の試験の説明は E-26 に任せ、こちらは「試験が寿命を迎える」現象の説明に絞る
- E-20 MMLU／E-4 HumanEval／E-23 GSM8K との関係：飽和した試験の歴史的な例。後継は MMLU-Pro、SWE-bench Verified など
- E-3 Terminal-Bench との関係：4.0 で飽和した課題などを外し、連続的に更新する運用に変えたとされる
- E-52 Artificial Analysis Intelligence Index との関係：v5 で約 6 割を非公開または答えを伏せた評価にして、汚染と飽和に備えたという位置づけ
- J-114 グッドハートの法則との関係：指標が目標になると指標として働かなくなる。飽和の背景の 1 つ
- E-35 RoboDojo との関係：文章の試験が 7 割を超えた一方、ロボットの手仕事は 1〜2 割台と点が低く、伸びしろの残る試験
- 汚染（問題が学習データに混ざること）は飽和と並ぶ寿命の原因。詳細は本文に書かず、ここで保持

## 出典メモ

- anthropic.com/claude/fable（Claude Fable 5.2 発表ページ、2026-11-09、直接取得）— checked 2026-11-13
- tbench.ai（Terminal-Bench 4.0、検索経由）— checked 2026-11-13
- artificialanalysis.ai／SWE-bench Pro に関する報道（検索経由・二次情報）— checked 2026-11-13

## 備考

- **一次確認済み**：Humanity's Last Exam（ツールあり）の Claude Fable 5.2 74.2%、Fable 5.1 65.6%、Opus 5.5 67.7%、GPT-6 Astra 57.2%、Remote Labor Index 41.3% は Anthropic の発表ページによります
- **一次未確認**：HLE-Diamond（元の問題を磨き直した 1,000 問、推論 500＋知識 500）、SWE-bench Pro の「飽和しつつある」という評価（2026-09、V2 は 2026-09-22 でも天井近くと報じられた）、Terminal-Bench 4.0（2026-08-28、8 件を外し 66 課題）は検索経由・二次情報です
- HLE は公開時（2025 年初め）、上位でも 1 桁〜10% 前後でした。2 年足らずで 7 割台に達した点が、飽和の速さの例です
- 発表ページに並ぶ新しい物差し：FrontierCode 2.0／FrontierSWE v2、AutomationBench、Terminal-Bench-Science、OSWorld 2.1、Remote Labor Index、AA-Briefcase、RoboDojo Sim。多くは 4〜7 割台
- 点数は時変情報のため、本文には出さず、メイン図の例示ラベルと備考に限定しています
