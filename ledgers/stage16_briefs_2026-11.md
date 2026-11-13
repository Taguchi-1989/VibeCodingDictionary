# Stage 16 ブリーフ（2026-11-13）— Muse・Gemini 4 Hydrogen・Fable 5.2、ベンチマークの世代交代、CLAUDE.md の変遷

*著者の指示（2026-11-13、音声入力）:「著者が書いていない部分のモデルや用語を更新してほしい。ジェボンズ（のパラドックス）は LLM の文脈で入れないといけない。Anthropic のブログを見て、CLAUDE.md に書くべきことがどう変遷したか（昔はいろいろ書け → スキルに書け → 今はほとんど書くな）のページを作ってほしい。ベンチマークも上げてほしい。とくにフィジカル AI（RoboDojo）。Humanity's Last Exam は 70% を超えて飽和が近いので別のベンチで測る話、ベンチマーキングをするツール。モデルは Meta の Muse 系、Google の Argon / Carbon / Hydrogen」。*

*「JEF」「ディシジョンズ APIs」は音声認識の崩れで、正しくは **Jev（TypeSafe AI の判断特化モデル）と decisions API**。当初ジェボンズのパラドックスと読み違えて J-153 を立てましたが、著者の指示で同日に削除しました（J-153 は欠番）。Jev は末尾の追補を参照。*

## 情報源の扱い（2026-11-13 確認）

- **直接取得できた一次情報**: code.claude.com（best-practices / memory）、claude.com/blog（steering-claude-code…、using-claude-md-files）、anthropic.com/claude/fable
- **検索経由（二次情報を含む）**: Meta（ai.meta.com）、Google（deepmind.google）、arXiv、Wikipedia、Artificial Analysis、tbench.ai、claude.dev（「The new rules of context engineering…」の本文）。環境のネットワーク制限で直接取得できません
- 二次情報だけの数字には「〜と報じられています」「〜とされます」を使い、備考に「一次未確認」と書く

## 書き方の共通指示（全件）

- **「現行」「最新」「主力」と書かない**。時点は年月で固定する
- 後継の固有名は本文に書き込まず備考へ
- 価格・スコアは誌面本文には最小限。具体値はメイン図のラベル（「2026-11 時点」つき）か備考へ
- `evaluation_date: 2026-11-13`、`last_audited: 2026-11-13`
- 著者記入欄（非エンジニアのつまずき／私のコメント）は**空スケルトンのまま**
- 既存エントリの改訂では `evaluation_date` を動かさず、`last_audited: 2026-11-13` だけ更新する。**著者記入欄には一切触れない**
- 文体・字数は [docs/v2_rules_summary.md](../docs/v2_rules_summary.md) と [docs/entry_schema.yaml](../docs/entry_schema.yaml)。見本は `content/entries/benchmark/E-52_artificial_analysis_index[人書].md`

## ID 一覧（空き番号のみ）

| ID | title | title_reading | category | subtype | figure_type | reader_level | importance |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| D-36 | Muse 系 | ミューズ系 | model | other_closed | comparison | 3 | B |
| E-35 | RoboDojo | ロボドージョー | benchmark | agent | structure | 3 | C |
| E-53 | 評価ハーネス | ひょうかハーネス | benchmark | general | workflow | 3 | C |
| E-54 | ベンチマークの飽和 | ベンチマークのほうわ | benchmark | general | timeline | 2-3 | B |
| H-65 | CLAUDE.md に書くことの変遷 | クロードエムディーにかくことのへんせん | history | timeline | timeline | 3 | B |

---

## D-36 Muse 系

### 押さえる事実（すべて検索経由。Meta 公式は直接取得不可）

- **Meta Superintelligence Labs（MSL）が作るモデル群**。Llama 系（D-40、2023〜2025）の後継と位置づけられている
- **Muse Spark**: 2026-04-08 発表。Muse ファミリーの 1 本目。文字・画像などをまとめて扱う推論モデルで、ツール利用・複数エージェントの取りまとめに対応（Meta 公式ブログ、CNBC、Axios）。Alexandr Wang 氏が率いる体制での最初の主要モデルと報じられた
- **Muse Spark 1.1**: 2026-07-09。**Meta Model API の公開プレビュー**と同時。文脈 100 万トークン、入力 $1.25 / 出力 $4.25（100 万トークンあたり）と報じられています。**Llama と違い、重みを配らずトークン課金で提供する**形に変わった点が大きい
- **Muse Glimmer**: 2026-08-10。**重み公開**（Apache 2.0、30B の小型モデル、Muse Spark からの蒸留、ノート PC で動かす想定）と報じられています（CNBC）
- **Muse Spark Open**: 2026-10-15。Muse Spark の重み公開版。総パラメータ 816B／稼働 42B の MoE、文脈 100 万トークン。ライセンスは独自の「Muse Model License」で、製品への表示義務や一定売上以上の提供事業者への別契約があるとされます（二次情報）
- **API で提供されるほかの名前**: Muse Wonder／Muse Ember／Muse Image／Muse Voice Transcribe（Meta Model API のモデル一覧、検索経由）。Spark は 1.3 まで版が進んだとされます。Muse Wonder（max）は Artificial Analysis の旧版指標（v4.3.2）で 52.4・12 位という記載あり（二次情報）
- **日付の食い違い**: 英語版 Wikipedia の一部は Muse Spark を 2026-07-09 と書くが、Meta の発表は 2026-04-08（07-09 は 1.1 と API）。備考に残す

### 書き方の指示

- figure_type `comparison`。「API で借りる Muse（Spark・Wonder・Ember）」と「重みをもらえる Muse（Glimmer・Spark Open）」の 2 列
- 核は「**Llama は配るモデルだった。Muse は“貸す”が基本で、一部だけ配る**」
- 注意点は「同じ Muse でも、使える場所とライセンスが名前ごとに違う」
- D-40 Llama 系、J-36 蒸留、オープンウェイトに関する既存エントリと相互参照。related_terms は既存エントリのタイトルと一致させる
- `start_date: 2026-04-08`、`version_status: active`、`pricing_note: paid`

---

## E-35 RoboDojo

### 押さえる事実（すべて検索経由。arXiv・公式サイトは直接取得不可）

- **ロボットを動かす汎用モデル（VLA などの操作ポリシー）を、シミュレーションと実機の両方で測る統一ベンチマーク**。論文は arXiv 2607.04434（2026-07-05）「RoboDojo: A Unified Sim-and-Real Benchmark for Comprehensive Evaluation of Generalist Robot Manipulation Policies」
- 規模: **シミュレーション 42 課題＋実機 18 課題**、5 つの能力軸（汎化・精密さ など）、公開時点で 30 のポリシーを統合。**RealEval** という仕組みで、クラウド経由で実機評価を回せる
- **点が低いのが特徴**: 公開時（2026-07）のシミュレーション首位は成功率 8.80%（スコア 13.07）。実機 18 課題の最高平均成功率は 12.8%（π0.5）と報じられています。2026 年夏〜秋にかけて各社が 13〜35% 台の自己申告を出しており、公式の順位表とは別に扱う必要があります
- **言語モデル側も載せ始めた**: Anthropic は 2026-11-09 の Claude Fable 5.2 の発表ページで「RoboDojo Sim」を掲載（Fable 5.2 64.9%、Fable 5.1 27.6%、Opus 5.5 39.4%、GPT-6 Astra 29.8%）。**これは一次情報（anthropic.com/claude/fable）で確認済み**。ただし論文の順位表（ロボット専用ポリシー）とは測り方・設定が違う可能性が高く、**並べて比べない**
- 中国語圏の百科記事は公開日を 2026-08-12 とするが、arXiv の日付（07-05）と合わない。備考へ
- 名前の「Dojo」は道場

### 書き方の指示

- figure_type `structure`。左に「シミュレーション 42 課題」、右に「実機 18 課題」、下で 1 枚の順位表に合流
- 核は「**文章の試験は 7 割を超えたが、ロボットの手仕事はまだ 1〜2 割**。伸びしろが残る試験」
- 注意点は「自己申告の点と公式の順位表は別」「シミュレーションの点と実機の点は別」
- J-6 フィジカル AI、J-7 VLA、J-5 世界モデル、E-54 ベンチマークの飽和 と相互参照
- `start_date: 2026-07-05`、`version_status: active`、`pricing_note: free`

---

## E-53 評価ハーネス

### 押さえる事実

- **ベンチマークを実際に走らせるための道具（実行基盤）**。問題集（ベンチマーク）そのものではなく、「モデルやエージェントに問題を渡し、隔離した環境で動かし、採点して記録する」側の仕組み
- **Harbor**: コンテナ環境でエージェントとモデルを評価・改善するための枠組み。**Terminal-Bench 4.0 は Harbor の上に作られ**、`harbor run -d terminal-bench/terminal-bench@4.0.0` で実行する（tbench.ai・harborframework.com、検索経由）
- **Inspect AI**: 英国 AI Security Institute が公開している評価フレームワーク。研究論文では、ベンチマークを Inspect 互換のラッパー（`inspect_harbor`）経由で読み込む例がある（検索経由）
- **同じモデルでも、ハーネスと設定で点が変わる**: ツールあり／なし、effort（考える量）、時間・CPU・メモリの割り当て。例: Humanity's Last Exam は「ツールあり」と「ツールなし」で別の数字。Terminal-Bench 4.0 は課題ごとの時間・CPU・メモリを較正し直した版（2026-08-28）
- Anthropic の Claude Code 文書でも、モデル（考える側）とハーネス（Claude Code 本体＝実行する側）を分けて説明している。本書の G 章「ハーネス」系エントリがあれば相互参照（タイトルは既存に合わせる）
- 一般の読者にとっての意味: **スコアを読むときは「何で、どの設定で測ったか」をセットで見る**

### 書き方の指示

- figure_type `workflow`。問題集 → ハーネス（隔離環境で実行）→ 採点 → 順位表、の流れ
- 核は「**問題集と試験会場は別物**。会場（ハーネス）が変わると点も変わる」
- E-3 Terminal-Bench、E-52 Artificial Analysis Intelligence Index、effort レベル と相互参照
- `version_status: active`、`pricing_note: free`（多くが OSS）

---

## E-54 ベンチマークの飽和

### 押さえる事実

- **上位モデルの点が満点近くに張りつき、モデルの差を測れなくなること**。問題が学習データに混ざる「汚染」と並ぶ、ベンチマークの寿命の原因
- **歴史の型**: MMLU（E-20）・HumanEval（E-4）・GSM8K（E-23）は飽和 → MMLU-Pro、SWE-bench Verified など難しい後継へ。本書の E 章はその世代交代を並べている
- **2026 年秋の実例**
  - **Humanity's Last Exam（E-26）**: 公開時（2025 年初め）は上位でも 1 桁〜10% 前後だった。**2026-11-09 の Claude Fable 5.2 は「ツールあり」で 74.2%**（Fable 5.1 65.6%、Opus 5.5 67.7%、GPT-6 Astra 57.2%。**anthropic.com/claude/fable で確認した一次情報**）。「人類最後の試験」が 2 年足らずで 7 割を超えた
  - **HLE-Diamond**: Center for AI Safety と Scale AI が元の問題を 1 年かけて磨き直した 1,000 問（推論 500＋知識 500）の版。Artificial Analysis は v5 で元の HLE をこれに入れ替えたとされます（検索経由）
  - **SWE-bench Pro**: 2026-09 時点で「飽和しつつある」と評され、2026-09-22 の V2 もすでに天井近くと報じられています（二次情報）
  - **Terminal-Bench 4.0（2026-08-28）**: 飽和した課題・解法が公開された課題など 8 件を外して 66 課題に。「連続的に更新するベンチマーク」に運用を変えた（tbench.ai、検索経由）
- **次に使われ始めた物差し（2026-11 の Fable 5.2 発表ページに並ぶもの）**: FrontierCode 2.0／FrontierSWE v2（エージェントによるコーディング）、AutomationBench（業務フロー）、Terminal-Bench-Science、OSWorld 2.1（PC 操作）、Remote Labor Index（請負仕事）、AA-Briefcase、RoboDojo Sim（E-35）。**多くがまだ 4〜7 割台、Remote Labor Index は 41.3%**。知識を問う試験から、**長い仕事をやり切れるかを測る試験**へ重心が移っている
- グッドハートの法則（J-114）: 指標が目標になると指標として働かなくなる

### 書き方の指示

- figure_type `timeline`。古い試験が天井に当たるたび、難しい試験にバトンが渡る階段の図。右端に「知識の試験 → 仕事の試験」
- 核は「**満点が近い試験は、もう差を教えてくれない**。記事で引かれている試験が“まだ効く試験か”を見る」
- 具体スコアはメイン図の例示ラベル（「2026-11 時点」）と備考へ。本文は「7 割を超えた」程度
- E-26 Humanity's Last Exam、E-20 MMLU、E-3 Terminal-Bench、E-52、J-114 と相互参照
- `version_status: active`、`pricing_note: free`

---

## H-65 CLAUDE.md に書くことの変遷

### 押さえる事実（Anthropic の公開情報を時系列で。★＝2026-11-13 に直接取得して確認）

| 時期 | 出どころ | 何と言っていたか |
| :-- | :-- | :-- |
| 2025-04 | Anthropic Engineering「Claude Code: Best practices for agentic coding」（2025-04-18。現在は code.claude.com/docs/en/best-practices へ転送され、当時の本文は直接確認できない＝**記憶・二次情報**） | **書くことを勧める時期**。よく使う bash コマンド、主要ファイル、コードスタイル、テストのやり方、リポジトリの作法、開発環境、想定外の挙動や注意点を書く。「IMPORTANT」「YOU MUST」のような強調で従わせやすくなる、`#` キーで指示を CLAUDE.md に追記できる、と案内 |
| 2025-10-16 | 「Introducing Agent Skills」（claude.com/blog/skills、検索経由） | **スキル登場**。必要なときだけ読み込む（プログレッシブディスクロージャ）。常時読み込みの CLAUDE.md と役割が分かれ始める |
| 2025-11-25 ★ | 「Using CLAUDE.md files: Customizing Claude Code for your codebase」 | まだ**足す寄り**。プロジェクトの概要とディレクトリ構成、自作ツールの使い方、標準の作業手順（テスト要件・コミット形式）を書く。ただし「簡潔で人が読める形に」「単純に始めて、困ったときだけ足す」「`/init` の出力は出発点」「長くなったら別ファイルに分ける」も併記 |
| 2026-02 | Claude Code v2.1.59 前後で **auto memory**（検索経由・二次情報） | **Claude が自分でメモを書く**仕組み（MEMORY.md）。人が CLAUDE.md に足していた「学び」の一部が、Claude 側の仕事になる |
| 2026-06-18 ★ | 「Steering Claude Code: when to use CLAUDE.md, skills, hooks, and subagents」（Michael Segner） | **振り分けの時期**。舵取りの手段は 7 つ（CLAUDE.md／rules／skills／subagents／hooks／output styles／システムプロンプトへの追記）。「CLAUDE.md は Claude が常に持っておくべき事実のため」「**手順はスキルへ**」「必ず起きてほしいことはフックへ」「**CLAUDE.md は 200 行未満、持ち主を決め、変更はコードのようにレビュー**」 |
| 2026-07-24 | 「The new rules of context engineering for Claude 5 generation models」（Thariq Shihipar とされる。本文は claude.dev にあり直接取得不可＝**検索経由**） | **削る時期**。Claude Opus 5／Fable 5 向けに Claude Code のシステムプロンプトを 80% 超削っても、コーディング評価で測れる低下はなかった、と公表。「システムプロンプトでも CLAUDE.md やスキルでも、制約をかけすぎていた」。CLAUDE.md を規則集として育てたチームは技術的負債を抱えている、という趣旨の記述があったと報じられています。削減率は実質 70% 前後という第三者の指摘もあり |
| 2026-11 ★ | Claude Code 公式ドキュメント（best-practices / memory） | **「Keep CLAUDE.md short」**。「毎セッション読み込まれるので、どの行も毎回 Claude の注意を少しずつ使う」「**コードから読み取れないことだけ書く**」。アーキテクチャやファイル構成の説明は「Claude が自分でリポジトリを読むので不要」。チームの手順はスキルへ、例外なしのルールはフック・deny ルールへ。「IMPORTANT を足しても直らないなら、長すぎるか、フックに移すべき行」。`/doctor` が削れる箇所を提案、`/doctor prompt-audit`（v2.1.283 以降）が「古いモデル向けに書かれた指示」や矛盾を指摘。目安は 1 ファイル 200 行未満 |

- **3 段の流れ**: ① 足す（2025 年春〜秋）→ ② 分ける（2025 年秋〜2026 年春：スキル・rules・フック・auto memory）→ ③ 削る（2026 年夏〜：モデルが賢くなり、書きすぎが害になる）
- **なぜ変わったか**: モデルが賢くなり、補助輪だった指示が要らなくなった／常時読み込みは毎回文脈（コンテキスト）を使う／手順は必要なときだけ読めばよい（スキル）／守らせたいことは「お願い」ではなく仕組み（フック）で
- **今も残すもの**（2026-11 の公式文書）: コードから分からないこと。チェックを走らせるコマンド、落とし穴、理由、ツールの既定と違う取り決め
- 強調語（IMPORTANT）の評価が 2025-04 と 2026-11 で逆転している点は、変遷を示す分かりやすい 1 例

### 書き方の指示

- figure_type `timeline`。「足す → 分ける → 削る」の 3 段。CLAUDE.md の紙が、だんだん薄くなり、横にスキル・フック・メモの箱が増える
- 核は「**昔の“たくさん書け”は間違いではなく、当時のモデルに合っていた**。モデルが変われば、書く量も変わる」
- 「ほとんど書くな」と断定しない。公式の言い方は「コードから分からないことだけ」「短く保つ」
- 一次未確認の 2 件（2025-04 の原文、2026-07 の本文）は備考に明記
- G-20 CLAUDE.md、G-22 SKILL.md、G-21 AGENTS.md、G-45 プログレッシブディスクロージャ、G-11 コンテキストエンジニアリング、フック関連エントリと相互参照（タイトルは既存に合わせる）
- `start_date: 2025-04-18`、`version_status: active`、`pricing_note: free`
- **このリポジトリ自身の CLAUDE.md（約 200 行）がまさに①〜②の作法で書かれている**ことは誌面に書かない（備考に 1 行だけ）

---

## 改訂対象（既存エントリ。`last_audited: 2026-11-13`、著者記入欄は触らない）

| ID | 何を直すか | 根拠 |
| :-- | :-- | :-- |
| D-6 Gemini 4 系 | **Gemini 4 Hydrogen（2026-11-12）**を追加。Carbon から派生した、エージェント作業を速く回すための版。入力 $1.50 / 出力 $7.50、Gemini 3.8 Flash の置き換えと報じられています。3 本とも文脈 100 万トークン。API ID は `gemini-4-hydrogen` / `-argon` / `-carbon`。「Argon ／ Carbon の 2 本」という記述を 3 本に。Google DeepMind のモデルカード（直接取得不可）は「Carbon と Argon は長く深い推論、Hydrogen はエージェントの速い実行」と位置づけ | 検索経由 |
| D-16 Claude Fable / Mythos | **Fable 5.2 / Mythos 5.2（2026-11-09）**を追記。Fable 5.2 は $8 / $40（5.1 の $10 / $50 から値下げ）、Fast mode $16 / $80（最大 2.5 倍速）、Pro / Max / Ultra / Team / Enterprise で利用可。Mythos 5.2 は引き続き検証プログラム経由。数日単位の作業・数百以上のサブエージェントの取りまとめをうたう | anthropic.com/claude/fable ★ |
| D-40 Llama 系 | 「後継は Muse 系（D-36）」への導線を備考と関連に。本文に Muse の固有名を増やしすぎない | 検索経由 |
| E-26 Humanity's Last Exam | 2026-11 に「ツールあり」で 74.2%（Fable 5.2）。磨き直し版 HLE-Diamond。E-54 への導線。「まだ誰も解けない試験」という書きぶりが残っていれば時点を固定 | anthropic.com ★／検索経由 |
| E-3 Terminal-Bench | 4.0（2026-08-28、66 課題、Harbor 上、連続更新型に）。E-53 への導線 | 検索経由 |
| E-52 AA Intelligence Index | 2026-11-09 以降は Claude Fable 5.2（max）が 65 で首位、Gemini 4 Carbon（high）60 と報じられています。メイン図の例示ラベルと備考を更新 | 検索経由 |
| G-20 CLAUDE.md | 2026-11 の公式ガイド（短く保つ／コードから分からないことだけ／200 行未満／手順はスキルへ／`/doctor`）と食い違う記述がないか確認し、H-65 への導線を足す | code.claude.com ★ |

---

## 追補（2026-11-13 同日）: 「JEF」は Jev だった

著者から「JEV だよ。よく調べて書いて。アウトプット 0 円の」と訂正がありました。**「JEF」＝ Jev（TypeSafe AI の判断特化モデル）、「ディシジョンズ APIs」＝ decisions API** です。J-153 ジェボンズのパラドックスは AI 側の読み違いで立てたもので、著者の指示により削除しました。

| ID | title | title_reading | category | subtype | figure_type | reader_level | importance |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| D-37 | Jev | ジェブ | model | other_closed | comparison | 3 | B |

## D-37 Jev

### 押さえる事実（**すべて検索経由**。typesafe.ai は環境の許可ホストに無く直接取得不可。数字は TypeSafe の自社発表が出どころで、第三者の検証は 2026-11 時点で乏しい）

- **TypeSafe AI が 2026-09-15 に早期アクセスで公開した、文章を書かない「判断だけ」のモデル**。同社はこの種類を **System One モデル**と呼ぶ。名前はカーネマンの「システム 1（速い直感）／システム 2（遅い熟考）」から。LLM を熟考役、Jev を即断役に見立てる
- **創業者は Diogo Almeida 氏**（元 OpenAI の研究者・エンジニアと報じられる。日本語記事では「ChatGPT の共同開発者」という紹介もある）。2 年のステルス期間を経て発表、DCVC 主導で 4,000 万ドルのシード調達と同時（Tom's Hardware、InfoQ、MarkTechPost ほか）
- **入出力の形**: 入力は「状態（state：文章や構造化データ）」＋「型のついた質問」。出力は文章ではなく**型のついた値と確率**。質問の型は 3 つ
  - **Choice**: 用意した選択肢から 1 つ選ぶ（確率分布と confidence つき）
  - **Score**: 度合いを数値で返す
  - **Noul**: はい／いいえの命題が真である確率（0〜1）を返す。0.5 は「中くらい」ではなく「どちらとも言えない」。**はい／いいえに変えるしきい値はアプリ側のコードが決める**
  - 複数の質問を 1 回の並列処理でまとめて答える
- **合言葉**: 「Jev makes judgments, code makes decisions（Jev は見立てを出し、決めるのはコード）」
- **料金: 入力 100 万トークンあたり $0.042、出力は無料**（2026-11 時点、各社の解説記事）。出力トークン数は API の利用量に報告されるが課金されない。質問文や選択肢の説明は入力として数えられる
- **速さ**: 応答 70〜500 ミリ秒と公表。同社は「先端 LLM より 40〜200 倍速い（193 倍という数字も）、40〜400 倍安い（445 倍という数字も）」と主張。**自社発表の数字**
- **文脈は 32,000 トークン**
- **学習法**: 合成データのみで、同社が **RLCD（Reinforcement Learning for Calibrated Decisions＝確率が現実と合うように鍛える強化学習）**と呼ぶ手法。構造は非公開（transformer で、オープンウェイトの LLM が土台ではないかという外部の推測がある）
- **版**: jev-1.13.0（公開時）→ **jev-1.14.0（2026-10-14、`jev-latest` はこれを指す）**
- **使える場所**: TypeSafe の API（`POST api.typesafe.ai/v1/systemone`）と公式 Python / JavaScript SDK。OpenRouter・Vercel AI Gateway・Cloudflare にも掲載があると報じられています。Amazon Bedrock には無いとされます
- **提供状況は情報が割れている**: 2026-09-20〜21 ごろに順番待ち（ウェイトリスト）を外して誰でも登録可にしたという報道と、「一般提供（SLA つき）の日付は未公表」という記述の両方がある。無料クレジット（$5）の有無も食い違い。**本文では「2026-09 に早期アクセスで公開」までにとどめる**
- **使いどころ**: エージェントの**交通整理**（どの担当に回すか）、問い合わせの分類・緊急度判定、ガードレール（通してよいかの判定）、検索結果の並べ替え。「答えの候補が決まっている判断」に向く
- **弱み・注意（同社の文書と第三者レビュー）**
  - **型は必ず正しいが、中身は間違えうる**。存在しない選択肢は返さないが、間違った選択肢を高い確信度で返すことはある。「幻覚の問題を少し利用者側に渡している」（Armin Ronacher 氏の評）
  - **理由を説明しない**。採用選考のような説明が要る判断には向かない（EU AI Act の高リスク領域という指摘）
  - 数える・計算・日付の比較が苦手（同社文書。計算はコード側に置くよう案内）、文字どおりに解釈しがち、選択肢の並び順に左右されることがある、悪意ある入力を既定では疑わない
  - **ベンチマークは自社実施**。4 種の業務フローで 67.8%（比較対象の LLM は 74.1%）。正解との照合ではなく「先端 LLM と答えが一致するか」で測っている。**独立した第三者ベンチマークは未確認**
  - 類似名の非公式サイト（jevtypesafe.org など）は公式ではない
- **なぜ話題か**: エージェントは 1 つの仕事の中で「次はどれ？」「これは通す？」という小さな判断を大量にする。そこに文章を書く大きな LLM を使うと遅くて高い。**判断だけを安く速く切り出す**という発想が受けた。同種の「判断モデル」（Liquid d1 など）も名前が挙がり始めている（二次情報）

### 書き方の指示

- figure_type `comparison`。左「LLM：文章で答える（数秒〜、出力に課金）」／右「Jev：型と確率で答える（1 秒未満、出力は無料）」。右の出力は `{ route: "請求", 緊急: 0.93 }` のような小さな値
- 核は「**文章を書かない AI。選ぶ・点をつける・はい／いいえの確率を出す、だけをする**」
- 注意点は「形は間違えないが、中身は間違える。理由も言わない」
- tagline 冒頭は略称ではないので正式名称の展開は不要。TypeSafe AI の名前は入れる
- 速さ・安さの倍率は**誌面本文に出さない**（自社発表のため）。料金「出力は無料」は本書の読者が出会う特徴なので本文に出してよいが「2026-11 時点」を添えるか図のラベルに置く
- related_terms は既存タイトルから: Structured Outputs／モデルルーティング／自律ループとガードレール／Token／ハーネスエンジニアリング など（4〜5 個、字数上限に注意）
- `start_date: 2026-09-15`、`version_status: active`（提供状況の食い違いは備考へ）、`pricing_note: paid`
- 備考に「全項目が一次未確認（公式サイトを取得できず）」「読みは『ジェブ』と表記している日本語記事に合わせた。公式の読みは未確認」を明記

---

## 追補 2（2026-11-13 同日）: Artificial Analysis に名前が挙がる LLM 企業

著者の指示:「AA のサイトで名前が挙がる LLM 企業を書くようにして。創業とか特徴とか」。**今後の方針として、Artificial Analysis（E-52）のリーダーボードにモデルが載る会社は C 章に項目を立てます**（創業・拠点・代表・主なモデル・特徴）。

- **すでに項目がある会社**: OpenAI（C-1）／Anthropic（C-2）／Google DeepMind（C-3）／Meta AI（C-4）／xAI（C-5）／Mistral AI（C-6）／Microsoft AI（C-8）／NVIDIA（C-9）／Moonshot AI（C-10）／Z.ai（C-11）／DeepSeek（C-16）
- **今回立てる 5 社**（2026-11 の AA 関連の記事で名前が確認できたもの）: 下表
- **候補として残す（今回は AA 掲載を確認できず）**: Amazon（Nova）／Cohere／ByteDance／Tencent／Baidu／Liquid AI／Upstage／IBM。artificialanalysis.ai は環境の許可ホストに無く、掲載企業の一覧そのものを直接確認できていません

| ID | title | title_reading | category | subtype | figure_type | reader_level | importance |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| C-18 | Alibaba | アリババ | person | company | structure | 3 | B |
| C-19 | MiniMax | ミニマックス | person | company | structure | 3 | C |
| C-20 | Xiaomi | シャオミ | person | company | structure | 3 | C |
| C-21 | Thinking Machines Lab | シンキングマシーンズラボ | person | company | structure | 3 | C |
| C-22 | TypeSafe AI | タイプセーフエーアイ | person | company | structure | 3 | C |

### 共通の書き方

- frontmatter の category / subtype / その他の欄は、**既存の会社エントリ（C-16 DeepSeek、C-10 Moonshot AI）と同じ値の入れ方**に合わせる（スケルトンの値より既存エントリを優先）
- 見どころ「5. はじめに」は既存の会社エントリの型（設立年・創業者・代表モデルの 3 点を押さえる、など）に合わせる
- 評価額・売上・順位は誌面本文に出さず備考へ。「最新」「主力」は使わず年月で固定
- すべて検索経由（二次情報を含む）。備考に「一次未確認」
- `evaluation_date` / `last_audited`: 2026-11-13。著者記入欄は空のまま

### C-18 Alibaba

- 中国・杭州の大手 IT 企業。1999 年にジャック・マー（馬雲）氏らが創業した電子商取引の会社で、クラウド部門 Alibaba Cloud（2009 年設立）が AI を担う（一般知識）
- LLM は **Qwen（通義千問、トンイーチェンウェン）**。2023-04 に初公開。**重みを公開するモデルが中心**で、オープンモデルの代表格のひとつ（本書 D-43 Qwen）
- 2026 年: 02 月に Qwen3.5（重み公開）と Qwen3.5-Plus（非公開）。07〜08 月に 2.4 兆パラメータの Qwen3.8-Max を発表、**08-12 に最大モデルの重み**（独自の Qwen3.8-Max License、文字のみ）、**08-14 に Qwen3.8-27B**（Apache 2.0、27B の小型で画像なども扱う、文脈 262K）を公開と報じられています。**同じ世代でもライセンスが 2 種類**ある点が注意
- AA では Qwen3.8 が総合上位 10 位台に載ると報じられている（二次情報）
- 特徴の核: 「**ネット通販の会社が、配る AI の大手でもある**」。小型で手元で動くモデルに強い
- related_terms 候補: Qwen 系（D-43 の正式タイトルを CSV で確認）／オープンモデル／DeepSeek／Moonshot AI

### C-19 MiniMax

- 中国・上海の AI 企業。**2021 年 12 月創業**（2022-01 とする記事もある）。創業者・CEO は Yan Junjie（閆俊傑）氏
- **2026-01-09 に香港取引所へ上場**（約 48 億香港ドルを調達、初日終値は公開価格の約 2 倍と報じられる）。中国の LLM 専業の上場例
- モデル: 文章・コーディングの **MiniMax M 系**（M2.7、**M3**＝2026-06 公開、428B の MoE、文脈 100 万トークン、画像・動画入力と PC 操作に対応、のち重み公開と報じられる）／動画生成の **Hailuo（海螺）**／音声合成
- AA では M2.7・M3 が総合 10〜20 位台に載ると報じられている（二次情報）
- 特徴の核: 「**文章・音声・動画を 1 社でそろえる**。動画の Hailuo で名前を知る人が多い」
- related_terms 候補: Moonshot AI／Z.ai／DeepSeek／MoE／オープンモデル

### C-20 Xiaomi

- 中国・北京の家電・スマートフォンメーカー。**2010 年に雷軍（レイ・ジュン）氏らが創業**（一般知識）。EV も手がける
- LLM は **MiMo（ミモ）**。**MiMo-V2.6-Pro（2026-09-21 または 22）**: 約 1.02 兆パラメータの MoE（稼働約 42B）、文脈 100 万トークン、文字・画像・動画・音声に対応、**MIT ライセンスで重み公開**。軽量版 Flash（309B）も同時
- Xiaomi は「AA Intelligence Index で 46 点、重みを落とせるモデルで最高」と発表。ただし**同じ 46 点で Kimi K3.1 Pro をオープンウェイト首位とする記事もあり、時点で入れ替わる**。自社の比較表でも Claude Opus 5 には多くの項目で及ばないとされる
- 特徴の核: 「**スマホと家電の会社が、配る AI の上位に入ってきた**」。端末を持つ会社が自前のモデルを持つ流れの例
- related_terms 候補: オープンモデル／MoE／DeepSeek／Alibaba／Artificial Analysis Intelligence Index

### C-21 Thinking Machines Lab

- 米国・サンフランシスコの AI 企業。**2025 年 2 月に Mira Murati 氏（元 OpenAI CTO、本書 C-55）が創業**
- 2025 年に 20 億ドルを調達（評価額 120 億ドル、Andreessen Horowitz 主導）と報じられた。2026-11 に追加の大型調達の報道があるが金額は記事で食い違い、会社は非公表
- 製品: モデルを自社向けに作り替える基盤 **Tinker**（収益の中心）／**2026-05 に「interaction models」**（会話に割り込み、文脈を足せるモデル）を予告／**2026-07-15 に最初の公開モデル Inkling**（975B、Apache ライセンスで重み公開）、07-31 に Inkling Small（276B）
- 姿勢: 「1 つの万能モデル」ではなく**用途に合わせて作り替える**ことに賭ける。Inkling は「最高性能ではない」と自ら認めている、と報じられた
- 2026 年前半に共同創業者 2 名が離脱、人員は約 200 人と報じられる。NVIDIA と提携
- AA の掲載企業として名前が挙がっている（二次情報、順位は未確認）
- related_terms 候補: Mira Murati／OpenAI／ファインチューニング／オープンモデル

### C-22 TypeSafe AI

- 米国・サンフランシスコの AI 企業。**2024 年創業**、2026-09-15 にステルスを解除。CEO は Diogo Almeida 氏（元 OpenAI の研究者。RLHF の仕組みや InstructGPT・ChatGPT・GPT-4 に関わったと同社と投資家は説明。その前は Google Brain）、CTO Erik Gafni 氏、COO Sasha Sheng 氏
- **4,000 万ドルのシード調達**（DCVC 主導）。Forbes は評価額 2 億ドルと報じたが会社は未確認
- 製品は **Jev（D-37）**: 文章を書かず、型と確率で答える判断専用モデル。同社は「System One モデル」と呼ぶ
- 特徴の核: 「**チャットしない AI だけを作る会社**。ソフトウェアの中の小さな判断を速く安く」
- 注意: 性能の数字は自社発表。名前の似た非公式サイトがある。AA への掲載は「判断モデル」という別枠の話題として言及されている程度で、Intelligence Index の順位は未確認
- related_terms 候補: Jev／OpenAI／Structured Outputs／モデルルーティング

### 既存エントリの軽い追記（備考とコミュニティ補完メモのみ。誌面本文は必要最小限）

- **C-4 Meta AI**: 2025 年以降は Meta Superintelligence Labs が Muse 系（D-36）を開発、Llama の後継。`last_audited: 2026-11-13`
- **C-10 Moonshot AI**: Kimi K3.1 Pro が 2026-11 時点で AA のオープンウェイト上位（46 点）と報じられている。`last_audited: 2026-11-13`

---

## 追補 3（2026-11-13 同日）: 会社とモデルを対で書く

著者の指示:「会社もモデルも書いてほしい」。追補 2 の方針を広げ、**AA に名前が挙がる会社は「会社（C 章）＋その会社のモデル（D 章）」を対で立てます**。モデル側は空きのある **D-80〜89 を「AA 掲載企業のモデル（追加分）」**として使います（[id_scheme.md](../docs/id_scheme.md) に追記）。

すべて検索経由（二次情報を含む）。artificialanalysis.ai 本体は直接取得できませんが、**Inkling・Inkling Small・MiniMax-M3 は AA の比較ページ／記事の見出しが検索結果に出ており、掲載を確認**。Amazon・ByteDance・Baidu・Tencent・Cohere・Liquid AI は AA への掲載そのものは未確認で、主要な LLM 開発元として立てます（備考に明記）。Upstage・IBM は今回調べきれず未着手。

### 共通の書き方

- 会社: 既存の C-16 DeepSeek／C-10 Moonshot AI と同じ frontmatter の入れ方。モデル: 既存の D-44 Kimi／D-48 DeepSeek V4／D-36 Muse 系に合わせる
- 会社の「5. はじめに」は「創業年・創業者（代表）・代表モデル」の 3 点を押さえる型
- 評価額・売上・順位・ベンチマーク点は誌面本文に出さず備考へ。「最新」「主力」「必ず」は使わない。時点は年月で固定
- 創業年・創業者などの基礎情報は一般知識（AI の学習知識）にもとづく。備考に「一次未確認（検索経由・一般知識）」
- `evaluation_date` / `last_audited`: 2026-11-13、`experience_level: research_only`。著者記入欄は空のまま
- 字数: tagline 25〜45／何をしてくれるか・どこで出会うか 各 60〜100／会話例 25〜50 の 1 文を「」で／見どころ各 15〜30（合計 120〜240）／開発フロー 5 段 80〜180／左ページ合計 155〜250／関連用語 4〜5 個・合計 20〜50 字（entries.csv のタイトルと完全一致。この追補の新規どうしは可）

### 会社 6 件（category は既存に合わせ person_org / company、figure_type structure、reader_level 3）

| ID | title | title_reading | importance |
| :-- | :-- | :-- | :-- |
| C-23 | Amazon | アマゾン | B |
| C-24 | ByteDance | バイトダンス | C |
| C-25 | Baidu | バイドゥ | C |
| C-26 | Tencent | テンセント | C |
| C-27 | Cohere | コヒア | C |
| C-28 | Liquid AI | リキッドエーアイ | C |

- **C-23 Amazon**: 1994 年、ジェフ・ベゾス氏が米国シアトルで創業。クラウドの AWS（2006 年〜）が AI の窓口で、**Amazon Bedrock** は自社と他社（Anthropic など）のモデルをまとめて貸す場。Anthropic への大口出資者でもある。自社モデルは **Nova（D-83）**。2026-07 に Nova の一部（Premier・Omni・Reel・Canvas）を縮小して次の旗艦に集中、社内の AGI Lab を閉じたと報じられる。次の基盤モデルは 2026 年末の re:Invent で発表予定とされる。核:「**自分でも作るが、他社のモデルを貸す場所としての顔が大きい**」。related 候補: Amazon Nova／Anthropic／NVIDIA／Microsoft AI
- **C-24 ByteDance**: 2012 年、張一鳴（チャン・イーミン）氏が北京で創業。TikTok／抖音の会社。AI は **Seed** チームが開発し、対話アプリ **Doubao（豆包）** と、企業向けクラウド **Volcano Engine（火山引擎）** で提供。LLM は **Doubao（Seed）系（D-84）**、動画生成は Seedance（本書 D-56）。核:「**動画アプリの会社。中国で最も使われる対話 AI のひとつを持つ**」。related 候補: Doubao 系／Seedance／Tencent／Alibaba
- **C-25 Baidu**: 2000 年、李彦宏（ロビン・リー）氏が北京で創業。中国の検索最大手。2023-03 に **ERNIE Bot（文心一言）** を中国の大手で最初に公開。モデルは **ERNIE 系（D-85）**、開発基盤は Qianfan（千帆）。自動運転（Apollo）も手がける。2025 年から ERNIE の重み公開に舵を切った。核:「**中国の検索の会社。対話 AI を国内で最初に出し、のちに配る側に回った**」。related 候補: ERNIE 系／Alibaba／Tencent／DeepSeek
- **C-26 Tencent**: 1998 年、馬化騰（ポニー・マー）氏らが深圳で創業。WeChat（微信）とゲームの会社。LLM は **Hunyuan（混元、海外名 Hy）系（D-86）**、対話アプリは **Yuanbao（元宝）**。画像・3D・動画の生成モデルも重み公開している。核:「**WeChat の会社。自前のモデルを、手持ちのアプリに組み込んで届ける**」。related 候補: Hunyuan 系／Alibaba／ByteDance／DeepSeek
- **C-27 Cohere**: 2019 年、カナダ・トロントで創業。創業者は Aidan Gomez 氏（Transformer 論文＝本書 H-58 の共著者のひとり）、Ivan Zhang 氏、Nick Frosst 氏。**企業向け専業**で、自社の環境に置ける（手元やプライベートクラウドで動かせる）ことを売りにする。モデルは **Command 系（D-87）**、検索用の Embed／Rerank、企業向け作業環境 **North**。2026-04 にドイツの Aleph Alpha と統合（買収・合併と報道が割れる）。上場は未定。核:「**一般向けチャットを持たない、企業の中で動かす AI の会社**」。related 候補: Command 系／Transformer 論文／RAG／Embedding（タイトルは CSV で確認）
- **C-28 Liquid AI**: 2023 年、MIT CSAIL からのスピンアウト。米国マサチューセッツ州ケンブリッジ。共同創業者は Ramin Hasani 氏（CEO）、Mathias Lechner 氏（CTO）、Daniela Rus 氏ほか。線虫の神経回路に着想を得た「リキッドニューラルネットワーク」の研究が出発点。2024-12 に AMD 主導で 2.5 億ドルを調達。モデルは **LFM 系（D-88）**: スマホ・PC・車など**端末の上で動く小さなモデル**。判断専用モデル d1 も出しており、Jev（D-37）と同じ「判断モデル」の文脈で名前が挙がる。核:「**データセンターではなく、手元の端末で動く小さな AI を作る会社**」。related 候補: LFM 系／Jev／SLM 系の既存タイトル／AMD

### モデル 9 件（category model、reader_level 3、figure_type は下表）

| ID | title | title_reading | subtype | figure_type | importance |
| :-- | :-- | :-- | :-- | :-- | :-- |
| D-80 | MiniMax M 系 | ミニマックス エム系 | open | structure | C |
| D-81 | MiMo | ミモ | open | structure | C |
| D-82 | Inkling | インクリング | open | comparison | C |
| D-83 | Amazon Nova | アマゾン ノヴァ | other_closed | structure | C |
| D-84 | Doubao 系 | ドウバオ系 | other_closed | structure | C |
| D-85 | ERNIE 系 | アーニー系 | open | timeline | C |
| D-86 | Hunyuan 系 | フンユェン系 | open | structure | C |
| D-87 | Command 系 | コマンド系 | open | structure | C |
| D-88 | LFM 系 | エルエフエム系 | open | structure | C |

- **D-80 MiniMax M 系**（会社 C-19）: 文章・コーディング向け。M2.7 → **M3（2026-06 公開）**。428B の MoE（稼働約 23B）、文脈 100 万トークン、画像・動画入力と PC 操作に対応。重みは公開されているが、**独自の MiniMax Community License**（商用では「Built with MiniMax M3」の表示が要るとされる）。AA に掲載あり。動画の Hailuo は別系統。`start_date: 2026-06`、pricing_note freemium 相当は既存に合わせる
- **D-81 MiMo**（会社 C-20）: **MiMo-V2.6-Pro（2026-09-21 または 22）**。約 1.02 兆パラメータの MoE（稼働約 42B）、文脈 100 万、文字・画像・動画・音声。**MIT ライセンス**で重み公開。軽量の Flash（309B）、高速版 UltraSpeed も。Xiaomi は「AA Intelligence Index で 46 点、重みを落とせるモデルで最高」と発表（同点で Kimi K3.1 Pro を首位とする記事もあり、時点で入れ替わる）。核:「家電メーカーが出した、自由に使える大型モデル」
- **D-82 Inkling**（会社 C-21）: **2026-07-15**。975B の MoE（稼働 41B）、文脈 100 万、**Apache 2.0** で重み公開（学習データと学習コードは非公開）。**Inkling Small（07-31）** は 276B（稼働 12B）、文脈 256K で、AA は「3 分の 1 以下の大きさで Inkling と 1 点差以内」と記事にした。会社自身が「最高性能ではない」と述べ、**Tinker で自社向けに作り替える土台**として出している。comparison 図は「Inkling ／ Inkling Small」の 2 列
- **D-83 Amazon Nova**（会社 C-23）: 2024-12 の re:Invent で初代（Micro／Lite／Pro／Premier、画像の Canvas、動画の Reel）。**Nova 2（2025-12）**: Lite・Sonic（音声）が一般提供、Pro・Omni はプレビュー。**Nova Act**（ブラウザ操作エージェント）、**Nova Forge**（自社モデルづくり）。2026-07 に Premier・Omni・Reel・Canvas を縮小と報道（Premier は 2026-09-14 に提供終了予定とされた）。**Amazon Bedrock 経由でだけ使える**のが特徴。`version_status: active`、備考に縮小の報道
- **D-84 Doubao 系**（会社 C-24）: **Doubao-Seed-2.0（2026-02-14）**: Pro／Lite／Mini の 3 段と Code。**Seed 2.1（2026-06-23、Pro／Turbo、文脈 256K）** と報じられる（二次情報）。Volcano Engine の API は同じモデル ID のまま週 1 回以上更新されるとされ、**版が見えにくい**。重みは非公開。核:「アプリ Doubao の中身。名前は Doubao、開発チームは Seed」
- **D-85 ERNIE 系**（会社 C-25）: 2019 年からの系譜（ERNIE 1.0 は BERT 系の研究）。2023-03 ERNIE Bot。**ERNIE 4.5 を 2025-06 に Apache 2.0 で重み公開**。ERNIE 5.0／5.1（2026-05-08）は API のみ。**ERNIE-5.5-Flash-Base（2026-11-05）**: 280B の MoE（稼働 14B）を重み公開。ただし**仕上げの学習前の“素”のモデル**で、ライセンスは Baidu 独自。5.5 Flash Preview（11-11）は API 提供、Apache 2.0 での重み公開を 11-25 までにと予告（予定）。timeline 図
- **D-86 Hunyuan 系**（会社 C-26）: 2023-09 に初公開。**Hy3 preview（2026-04-23）**: 295B の MoE（稼働 21B）、文脈 256K、重み公開。**Hy3 正式版（2026-07-06）**。ライセンスは Apache 2.0 とする記事と独自ライセンスとする記事があり未確定。Yuanbao・CodeBuddy・ima の中身。Hy4 の記載（2026-11-04）が 1 件あるが裏が取れず備考のみ。「Hy」は海外向けの名前
- **D-87 Command 系**（会社 C-27）: 企業向け。Command R／R+（2024、RAG＝検索して答える用途に強い）→ Command A（2025-03）→ **Command A+（2026-05-20）**: MoE、48 言語、少ないハードウェアで動くことを重視、**Cohere 初の Apache 2.0 での重み公開**と Gomez 氏が投稿。音声認識の Cohere Transcribe（2026-03、Apache 2.0）も。核:「自社の中に置いて動かす前提のモデル」
- **D-88 LFM 系**（会社 C-28）: Liquid Foundation Models。LFM2（2025）→ LFM2.5（2026、2.6B で文脈 128K・ツール呼び出し対応など）→ **LFM3（2026-10-27）**: 約 2B 級の 6 モデル（文章・画像・音声・omni・判断）を 1 つの土台で。LFM3-1.7B は文脈 256K、**LFM Open License v1.0**（独自。一定規模以上の企業は別契約とされる）。判断モデル d1（d1-ultra は 2026-10-15）。核:「**スマホに入る大きさ**。賢さより、手元で速く動くこと」
