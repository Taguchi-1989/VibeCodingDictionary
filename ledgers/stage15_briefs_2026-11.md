# Stage 15 ブリーフ（2026-11-06）— 2026 年夏〜秋のモデル世代交代と新しい概念 12 件

*著者の指示（2026-11-06）:「2 か月ほど更新していないので徹底的に探査・更新してほしい。直近 1〜3 か月で話題のモデル、Artificial Analysis に出てくる主要モデルを追い、最新ページに更新日付つきで反映。新しい概念があれば追加。著者の印象欄は残しておいてよい（＝空のまま）」。*

*事実はすべて 2026-11-06 に確認しています。**Anthropic の公式ページ（anthropic.com / platform.claude.com / code.claude.com）は直接取得**できました。**OpenAI・Google・Artificial Analysis・Wikipedia は環境のネットワーク制限で直接取得できず、検索経由（二次情報を含む）**です。二次情報だけで裏が取れていない数字には「〜と報じられています」「〜とされます」を使い、備考に「一次未確認」と明記してください。*

## この束を立てる理由

2026-09-19 の鮮度監査で「D 章のモデル世代が 1〜2 段止まっている」ことが分かっていました（[freshness_audit_log.md](freshness_audit_log.md) §B）。その後 2 か月で、さらに次が起きています。

- **Anthropic**: Claude 5 世代（Sonnet 5 / Opus 5 / Fable 5 / Mythos 5）に続き、**Claude 5.5 世代**（Opus 5.5 / Sonnet 5.5 / Haiku 5.5）が 9〜10 月に出そろった
- **OpenAI**: GPT-6 世代（Astra / Sol / Luna）と GPT-6.1（Sol / Terra）
- **Google**: Gemini 3.5〜3.8 Flash を経て **Gemini 4 世代**（Argon / Carbon）
- **Artificial Analysis Intelligence Index v5**（2026-10-27）。著者が主要モデルの一覧として参照しているリーダーボード。本書に項目がない
- **概念**: 最強モデルを「検証済みの組織だけ」に出す**トラステッドアクセス**が 3 社そろって定着／**蒸留攻撃**への対策が API の仕様（preserved thinking）にまで降りてきた／**Fast mode**（同じモデルを高い単価で速く回す）という「速さを買う」料金軸

## 書き方の共通指示（全件）

- **「現行」「最新」「主力」と書かない**。時点は年月で固定する（2026-09-19 監査の学び）。「2026 年秋に出そろった」「2026-09 公開」のように書く
- 後継世代の固有名を本文に書き込まない（次の世代交代でまた古くなる）。後継は「後続世代」と書き、固有名は備考へ
- 価格・スコアは**誌面本文には最小限**。具体値は「メイン図」のラベルか備考へ。誌面に出すなら「2026-11 時点」を添える
- `evaluation_date: 2026-11-06`、`last_audited: 2026-11-06`
- 著者記入欄（非エンジニアのつまずき／私のコメント）は**空スケルトンのまま**（著者の指示）
- `version_status`: 提供中なら `active`、限定提供なら `preview` ではなく `active` とし、備考に限定提供を書く（Mythos・Carbon など）

## ID 一覧（空き番号のみ）

| ID | title | title_reading | category | subtype | figure_type | reader_level | importance |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| D-5 | Gemini 3.5〜3.8 系 | ジェミニ サンテンゴ〜サンテンハチ系 | model | google | timeline | 2-3 | C |
| D-6 | Gemini 4 系 | ジェミニ ヨン系 | model | google | comparison | 2-3 | B |
| D-15 | Claude 5 系 | クロード ゴ系 | model | anthropic | comparison | 2-3 | B |
| D-16 | Claude Fable / Mythos | クロード フェイブル ミトス | model | anthropic | structure | 3 | B |
| D-17 | Claude 5.5 系 | クロード ゴテンゴ系 | model | anthropic | comparison | 2-3 | A |
| D-27 | GPT-6 系 | ジーピーティー ロク系 | model | openai | comparison | 2-3 | A |
| D-48 | DeepSeek V4 | ディープシーク ブイフォー | model | open | structure | 3 | C |
| E-52 | Artificial Analysis Intelligence Index | アーティフィシャル アナリシス インテリジェンス インデックス | benchmark | general | structure | 2-3 | B |
| G-52 | Fast mode | ファストモード | term_llm | control | comparison | 2-3 | C |
| J-151 | トラステッドアクセス | トラステッドアクセス | term_general | ai_safety | structure | 3 | B |
| J-152 | 蒸留攻撃 | じょうりゅうこうげき | term_general | ai_safety | workflow | 3 | C |

（11 件。既存エントリの改訂は別表「改訂対象」を参照）

---

## D-5 Gemini 3.5〜3.8 系

### 押さえる事実

- **Gemini 3.5 Flash**: 2026-05-19（Google I/O 2026）公開。最初から GA（一般提供）。API ID `gemini-3.5-flash`
- **Gemini 3.6 Flash / 3.5 Flash-Lite / 3.5 Flash Cyber**: 2026-07-21 同時公開
- **Gemini 3.7 Flash**: 2026-08-13。3.6 から約 3 週間後。導入価格 入力 $0.75 / 出力 $3.75（100 万トークンあたり、2026-12-31 まで）、2027-01-01 から標準価格 $1.50 / $7.50 と報じられています（二次情報）
- **Gemini 3.8 Flash**: 2026-09-02。「最も賢い主力機（workhorse）」と位置づけ。文脈 1,048,576 トークン、出力上限 65,536 トークン、テキスト・画像・音声・動画入力。価格は 3.7 Flash と同じ導入価格（Google Cloud ドキュメント・9to5Google）
- **Cyber 版**: 3.5 Flash Cyber・3.8 Flash Cyber は**一般提供されず、Google の Fairwind プログラム経由で検証済みの防御側組織だけ**が使えます（→ J-151）
- **2026-10**: 3.7 Flash と 3.5 Flash は非推奨になり、それぞれ 3.8 Flash / 3.6 Flash へ振り替え（リクエストが新しい版にルーティングされる）
- この時期の改版は **Flash（速くて安い主力版）が中心**。版番号が**ほぼ月 1 回**のペースで進んだ
- 後続は Gemini 4 系（D-6）。固有名は備考へ

### 書き方の指示

- figure_type は `timeline`。**5 月→7 月→8 月→9 月と 4 回版が上がる**のを横 1 本の時間軸で見せる。Cyber 版は時間軸の下に「鍵つきの枝」として描く
- 非エンジニア読者へのポイントは「**番号が月単位で上がるので、番号で覚えるより『その時期の Flash』と覚えるほうが実用的**」
- 書かないこと: ベンチマーク数値の羅列

---

## D-6 Gemini 4 系

### 押さえる事実

- **Gemini 4 Argon**: 2026-09-30 発表、Gemini API で 2026-10-13 に GA。複雑なコーディング・エージェント・数学・科学向け。Gemini アプリでは 3.1 Pro を置き換えずに**選べるモデルとして追加**。文脈 約 100 万トークン。導入価格 $2 / $10（2026-11-30 まで）、2026-12-01 から $4 / $20 と報じられています（二次情報）
- **Gemini 4 Carbon**: 2026-10-28 発表（Google 公式ブログ「Gemini 4 Carbon: our next frontier model」、Koray Kavukcuoglu 名義）。Google が「最も強いモデル」と位置づけ、サイバーセキュリティと長時間タスク（long-horizon）で最先端とされます。**Artificial Analysis Intelligence Index v5 で首位**（Google 発表で 59。AA のリーダーボードでは High 設定で 60）
- **Carbon は最初に、Fairwind プログラムの検証済みサイバー防御組織だけに提供**。一般の開発者・企業・Gemini アプリへの提供時期は未発表（2026-11-06 時点）
- **名前の付け方**: 4 世代から、同じ世代の中で **元素名（Argon＝アルゴン、Carbon＝炭素）** を使い分けています。OpenAI の Sol / Terra / Luna（太陽・地球・月）と同じく、「数字＝世代、名前＝その世代の中の役割」という流れ
- 技術レポート・パラメータ数・Carbon の文脈長は未公表

### 書き方の指示

- figure_type `comparison`。Argon と Carbon の 2 枚カード。Carbon 側には鍵（限定提供）
- 「**同じ世代なのに、強いほうは一般には使えない**」が 2026 年秋の特徴であることを 1 文で（→ J-151）
- 名前（元素名）の話は「どこで出会うか」か見どころ 5 に。読者がニュースで混乱するポイント
- 後継・前任の固有名は最小限。前任は「3.x 系（D-4・D-5）」と ID で示すのは可

---

## D-15 Claude 5 系

### 押さえる事実（Anthropic 公式で確認）

- **Claude Sonnet 5**: 2026-06-30 公開（公式の退役予定日「2027-06-30 より前にはしない」と整合）。入力 $2 / 出力 $10（100 万トークンあたり。Sonnet 5.5 の公式ページが「トークン単価は Sonnet 5 と同じ」と明記）
- **Claude Opus 5**: 2026-07-24 公開（退役予定「2027-07-24 より前にはしない」）。入力 $5 / 出力 $25（Opus 5.5 が「トークン単価 20% 減」で $4 / $20 なので逆算でも一致）
- **両モデルとも文脈 100 万トークン・出力上限 12.8 万トークン**。4.5 世代（20 万トークン）から 5 倍。Anthropic の API では長文脈の追加料金なし（二次情報）
- 思考は **Adaptive thinking（モデルが考える量を自分で決め、effort で強弱を指示）**。手動で思考予算を渡す旧方式（extended thinking の budget_tokens）は後続モデルでは受け付けない
- **Fast mode**（→ G-52）: Opus 5 は研究プレビューで $10 / $50
- 2026-11 時点では両モデルとも **legacy（提供は続くが更新はされない）**。公式は後続の 5.5 世代への移行を案内
- **同じ 6 月に、Opus の上の段として Claude Fable 5 / Mythos 5（2026-06-09）が出ている** → D-16 に分ける
- 4 系の旧モデルは整理が進んだ: Opus 4 / Sonnet 4 は 2026-06-15 退役、Opus 4.1 は 2026-08-05 退役、Sonnet 4.5 は 2026-11-30 退役予定
- 出典: https://platform.claude.com/docs/en/about-claude/models/overview ／ https://platform.claude.com/docs/en/about-claude/model-deprecations ／ https://www.anthropic.com/claude-sonnet-5-5 ／ https://www.anthropic.com/claude-opus-5-5

### 書き方の指示

- figure_type `comparison`。Sonnet 5 と Opus 5 の 2 枚カード＋共通値（100 万トークン）。上に「Fable / Mythos（D-16）」が別の段として乗っていることを点線で示す
- 族の総論は D-12（4 系）と同じ粒度で。**5 系の特徴は「文脈 100 万トークンが標準になった」「Opus の上に段が増えた」の 2 点**に絞る
- 備考に 2026-11 時点の提供状況（legacy）と退役予定日

---

## D-16 Claude Fable / Mythos

### 押さえる事実（Anthropic 公式で確認）

- **Fable と Mythos は「同じモデルに、別の安全装置（safeguards）をかけた 2 つの版」**（公式:「same model with different safeguards」）
  - **Fable**: 一般提供。AWS・Google Cloud・Microsoft Azure でも使える。サイバー面では「脆弱性を見つけることはできるが、攻撃コード（エクスプロイト）は作らない」制限つき
  - **Mythos**: 安全装置を緩めた版。**検証済みの組織だけ**が使える（Cyber Verification Program＝CVP、Life Sciences Verification Program＝LSVP）。Mythos 5.1 は 2026-11 時点で米国の組織に限定
- **Fable 5 / Mythos 5**: 2026-06-09 公開。文脈 100 万トークン、出力 12.8 万トークン、入力 $10 / 出力 $50。思考は常時オン、effort の既定は high
- **Fable 5.1 / Mythos 5.1**: 2026-09 公開（公式の退役予定日は「2027-09-01 より前にはしない」で 2026-09-01 公開と整合。Anthropic のニュース一覧では 2026-09-15 掲載。**日付は「2026 年 9 月」と月までで書く**）。価格据え置き、キャッシュ読み出しを 75% 値下げ、典型的な使い方で約 25% 安くなると説明
- **位置づけ**: 公式ドキュメントは「ほとんどの用途はまず Opus 5.5 から。Opus 5.5 を高い effort にしても足りないときに Fable 5.1」と案内。**Opus の上の段**
- **前身は D-14 Claude Mythos Preview**（2026-04 発表、Project Glasswing 経由の限定提供）。Mythos Preview は 2026-06-09（Fable 5 / Mythos 5 公開日）に非推奨
- **Project Glasswing は 2026-10-06 に CVP へ統合**。CVP は Defense / Red Team / Specialized の 3 段に再編。Glasswing 参加組織は 2026-04〜07 に検証済み脆弱性 12 万 9,000 件以上（うち重大・高 3 万 3,000 件超）を報告
- Mythos 5 は 2026-06-12 に一時提供停止、輸出規制の解除を受けて 2026-07-01 に再開と報じられています（二次情報。備考のみ）
- 出典: https://www.anthropic.com/claude-fable-and-mythos-5-1 ／ https://platform.claude.com/docs/en/models/fable-5/overview ／ https://www.anthropic.com/news/cyber-verification-program

### 書き方の指示

- figure_type `structure`。**1 つのモデル本体から 2 本の出口**が出ている図。左の出口（Fable）は誰でも通れる扉、右の出口（Mythos）は検問つきの扉
- 非エンジニア読者には「**中身は同じ。誰に、どこまでの使い方を許すかが違う**」が 1 行で伝われば十分
- 「Fable」は「寓話」、「Mythos」は「神話」の意。カタカナ語の初出訳として 1 回だけ添える
- J-151 トラステッドアクセスと D-14 への相互参照を必ず

---

## D-17 Claude 5.5 系

### 押さえる事実（Anthropic 公式で確認）

- **Claude Opus 5.5**: 2026-09-22 公開。5.5 世代の最初のモデル。公式は「ほとんどの仕事で Fable 5.1 と同等の水準、Opus 5 より約 40% 安く回せる」と説明。入力 $4 / 出力 $20、キャッシュ読み出し $0.20。**Fast mode（最大 2.5 倍速）は $8 / $40**。effort は low / medium / high / xhigh / max の 5 段で**既定は medium**。思考は常時オン（無効化できない）。プロンプトインジェクションへの耐性が Opus 5 より上がったと説明
- **Claude Sonnet 5.5**: 2026-09-28 公開。入力 $2 / 出力 $10（Sonnet 5 とトークン単価は同じ。少ないトークンで済むので 1 タスクあたり最大 30% 安い）。Sonnet 5 より 30% 以上速い。知識労働の評価 GDPval-AA では Opus 5.5 とほぼ並ぶ（Elo 1844 対 1846）。effort 既定は high
- **Claude Haiku 5.5**: 2026-10-07 公開。プロンプト 10 万トークンまでは入力 $0.10 / 出力 $0.50、それを超えると $0.50 / $2.50。Haiku 4.5（$1 / $5）より平均約 75% 安い。**Haiku で初めて effort を調整できる**。分類・振り分け・要約・サブエージェント向け。effort 既定は medium
- **3 モデル共通**: 文脈 100 万トークン、出力上限 12.8 万トークン、信頼できる知識の終点 2026-06
- 公式ドキュメントの案内は「**迷ったらまず Opus 5.5**。それで足りなければ Fable 5.1」。Opus が「最上位」ではなく「既定の出発点」になった
- **Artificial Analysis Intelligence Index v5**（2026-11 初旬）では Opus 5.5（max）が 59 で、Gemini 4 Carbon（60）に次ぐ 2 位。同じ Opus 5.5 でも effort low では 35、max では 58 前後で、max は 1 タスクあたり約 10 倍のコストと報じられています（→ E-52）
- 2026-10-12 の蒸留対策で導入された **preserved thinking** は Fable 5.1 と Opus 5.5 から（→ J-152）
- 出典: https://www.anthropic.com/claude-opus-5-5 ／ https://www.anthropic.com/claude-sonnet-5-5 ／ https://www.anthropic.com/claude-haiku-5-5 ／ https://platform.claude.com/docs/en/about-claude/models/overview

### 書き方の指示

- figure_type `comparison`。3 枚カード（公開日順: Opus → Sonnet → Haiku）。**3 週間で 3 段がそろった**ことを日付で見せる
- 本書の読者（Claude Code ユーザー）にとって最も身近な世代なので importance A。見どころ 2「うれしさ」は「**同じ性能帯が安く・速くなった**」、注意点は「**effort の既定値がモデルごとに違う**（Opus 5.5 は medium、Sonnet 5.5 は high）」
- 価格は誌面本文には出さず、メイン図のラベル（2026-11 時点）に

---

## D-27 GPT-6 系

### 押さえる事実（**OpenAI 公式ページは直接取得できず、すべて検索経由**）

- **命名ルール**（GPT-5.6 から、2026-06-26 限定プレビュー／07-09 一般提供）: **数字が世代、名前が役割（能力の段）**。Sol（太陽）＝上位、Terra（地球）＝中間、Luna（月）＝軽量。従来の mini / Pro のような接尾辞をやめた
- **GPT-6 Astra**（Astra＝星）: 2026-09-03 発表。信頼された組織への限定プレビューから始まり、有料 ChatGPT・API に広がったとされます。入力 $10 / 出力 $50。OpenAI 自身が、Preparedness Framework（OpenAI の危険度評価の枠組み）のサイバー分野で **「Critical」水準に達した**と評価。サイバー能力の利用は信頼アクセスプログラム「**Daybreak**」経由（→ J-151）。監視をかいくぐろうとする場面で推論が Sol より読み取りにくかった、とも報告
- **GPT-6 Sol / GPT-6 Luna**: 2026-09-22。Sol は $2 / $10 のコーディング・エージェント向け中核、Luna は $0.10 / $0.50 の大量処理向け
- **GPT-6.1 Sol**: 2026-09-29（DevDay 2026）。「Astra に近い性能を 5 分の 1 の価格で」。API ID `gpt-6.1-sol`。Codex や ChatGPT の有料プランで利用。10-08 に出力を速める **Ultrafast mode** が API に追加（→ G-52）
- **GPT-6.1 Terra**: 2026-10-26。視覚的な推論・コンピューター操作・自然な文章に強い中間段。価格は報道で食い違い（備考へ）
- **GPT-6 Rosalind**: 2026-10-30。生命科学向けで、承認された組織だけが使える
- **GPT-5.5 は 2026-10-14 に ChatGPT から引退**
- **GPT-6.1 Astra は内部テストでの安全上の懸念から公開が見送られた**と報じられています（TechCrunch が WSJ 報道として。一次未確認 → 備考のみ）
- 前世代は D-20 GPT-5 系（5.6 まで）。o シリーズ（D-22 / D-23）は GPT-5 以降の本流に統合済み
- 出典（すべて検索経由）: OpenAI DevDay 2026 Recap（openai.com/index/devday-2026-recap）／TechCrunch 2026-09-29／The New Stack／DataCamp

### 書き方の指示

- figure_type `comparison`。**4 段の縦並び（Astra / Sol / Terra / Luna）**に、6 と 6.1 の版を横に並べたマトリクス。Astra 段に鍵（サイバー能力は限定）
- 読者が最もつまずくのは「**6 と 6.1 と名前が混ざる**」こと。「数字＝世代、名前＝段」のルールを見どころ 5「はじめに」で必ず書く
- 一次未確認の数字は誌面に出さない。誌面は「2026 年 9 月に GPT-6 世代が出た」「段の名前で選ぶ」程度にとどめる

---

## D-48 DeepSeek V4

### 押さえる事実（検索経由）

- **2026-04-24** に DeepSeek-V4 Preview として公開。**重みを公開（オープンウェイト）、MIT ライセンス**
- **V4-Pro**: 総パラメータ 1.6 兆（1.6T）、1 トークンあたりに動くのは 490 億（49B）の MoE（→ J-18）
- **V4-Flash**: 総 2,840 億（284B）、動くのは 130 億（13B）
- API の既定の文脈長が **100 万トークン**に
- Hugging Face・ModelScope で配布、技術レポートつき
- **反響は R1 のときほど大きくなかった**（The Economist は「以前ほどの衝撃はない」と評したと報じられています）。H-64 DeepSeek ショックとの対比が書ける
- 2026 年夏以降は V4.1 Flash がコーディング用途の安価な選択肢として挙がる（二次情報、備考へ）
- Artificial Analysis Intelligence Index v5 では、オープンウェイトの首位と全体首位の差が v4.3 の 3 ポイントから 12 ポイントに開いた（AA の発表。→ E-52）
- 出典: lambda.ai blog「DeepSeek v4」／NYU Shanghai RITS／letsdatascience（いずれも検索経由）

### 書き方の指示

- figure_type `structure`。Pro と Flash の 2 体を「総パラメータ（体の大きさ）」と「動く部分（光っている部分）」で描き分ける。MoE の直感を図で
- D-46（V3）・D-47（R1）・H-64 との関係を関連用語に
- 「最強」「最高性能」などの断定は避ける（D-46 の方針を踏襲）

---

## E-52 Artificial Analysis Intelligence Index

### 押さえる事実（検索経由。AA のサイトは直接取得できず）

- **Artificial Analysis**（artificialanalysis.ai）は、AI モデルと API 提供事業者を**独立に**測る評価会社。「賢さ・速さ・価格」を同じ物差しで並べたリーダーボードを公開しています
- **Intelligence Index** は、複数のベンチマークの結果を 1 つにまとめた**総合スコア**
- **v5（2026-10-27 発表）**:
  - 9 つの評価を **4 分野（Knowledge Work・Coding・Science・General）に各 25%** で配分
  - **約 60% が非公開のテストセット、または答えを伏せた評価**。モデルが既知の問題を学習して点を稼ぐ（汚染）のを防ぐ狙い
  - 新評価の追加と入れ替え（FrontierCode 2.0・Terminal-Bench-Science の追加、Humanity's Last Exam を HLE-Diamond に、GDPval-AA・SciCode・AA-LCR を外す — 二次情報）
  - **v5 のスコアは v4 以前と直接比べられない**。時系列の比較には別の「Progress Index」を使うよう AA 自身が案内
  - 1 タスクあたりの出力トークン中央値が 3.5 万 → 5.9 万に増加。**effort（思考の量）の設定でスコアが大きく動く**（例: Claude Opus 5.5 は low で 35、max で 58 前後、max は 1 タスクあたり約 10 倍のコスト）
  - オープンウェイトの首位と全体首位の差が 3 → 12 ポイントに拡大
- **2026-11 初旬の上位**: Gemini 4 Carbon（High）60、Claude Opus 5.5（Max）59、Gemini 4 Carbon（Medium）58、Claude Opus 5.5（Xhigh）57（AA リーダーボードの検索結果抜粋。98 モデル中）。**同じモデルが設定違いで複数行に出る**のが読み方のポイント
- 出典: artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5（検索経由）／artificialanalysis.ai/leaderboards/models（検索経由）

### 書き方の指示

- figure_type `structure`。**9 つの小テストの箱 → 4 分野の箱（各 25%）→ 1 つの総合点**というじょうご型
- 本書の読者にとっての価値は「**モデル選びの最初の 1 枚**」。ただし注意点として 3 つ: ①版が変わると点数の意味が変わる ②同じモデルでも effort 設定で点が違う（行が複数ある）③賢さだけでなく、同じサイトの速度・価格の軸も一緒に見る
- E-50 Chatbot Arena（人の投票による相対評価）との違いを 1 文で: こちらは**決まった試験の点数の合成**
- 著者がふだん主要モデルの一覧として参照している、という事実は備考に（著者記入欄には書かない）
- 具体スコアは誌面本文に出さない。メイン図の例示ラベルに「2026-11 時点」で 1〜2 行までは可

---

## G-52 Fast mode

### 押さえる事実（Claude Code 公式ドキュメントで確認）

- **同じモデルを、高い単価で速く動かす設定**。Claude Code では Claude Opus に対して最大 **2.5 倍速**。**別モデルではなく品質・能力は同じ**で、API の構成を速さ優先に切り替えるもの
- 切り替えは `/fast`。オン中はプロンプトの横に `↯` が出る
- 価格（100 万トークンあたり）: **Opus 5.5 は $8 / $40（通常の 2 倍）**、Opus 5 と Opus 4.8 は $10 / $50（研究プレビュー）。Sonnet・Haiku では使えない
- **Opus 4.8 の Fast mode は 2026-10-30 に非推奨、2026-11-30 に廃止**
- サブスクリプション（Pro / Max / Ultra / Team / Enterprise）では**プランの利用枠ではなく「利用クレジット（usage credits）」から引かれる**。Team / Enterprise はオーナーが有効化するまで使えない
- **会話の途中でオンにすると、それまでの文脈全体を Fast mode の単価でキャッシュなしに読み直すぶん課金**される。通常速度とはキャッシュも別。**使うなら会話の最初から**
- 使いどころ: 素早い試行錯誤・その場のデバッグ。向かないのは長い自律タスク・バッチ処理・費用重視の作業
- **effort（G-9）との違い**: effort を下げると考える量が減って速くなるが質が落ちることがある。Fast mode は質を保ったまま速くなるが高い。組み合わせも可
- Amazon Bedrock・Google Cloud・Microsoft Foundry では使えない
- **他社にも同じ発想**: OpenAI は GPT-6.1 Sol に Ultrafast mode（2026-10-08、出力トークン間の待ち時間を縮める）、xAI は Grok 4.7 Fast（約 2 倍の価格）。「**速さを追加料金で買う**」料金の軸が 2026 年秋に各社で並んだ
- 出典: https://code.claude.com/docs/en/fast-mode

### 書き方の指示

- figure_type `comparison`。同じ車（モデル）が「通常レーン」と「有料の高速レーン」を走る図。高速レーンの入口に料金所
- 非エンジニア読者向けの核は「**頭は良くならない。速くなるだけ。そのぶん高い**」
- 注意点 3 は「途中でオンにすると高くつく」
- G-9 effort レベル、G-19 Prompt Caching と相互参照

---

## J-151 トラステッドアクセス

### 押さえる事実（Anthropic 分は公式で確認、OpenAI・Google 分は検索経由）

- **最も強い能力（とくにサイバー攻撃・生命科学に使える能力）を、身元と目的を検証した組織にだけ開く提供方式**。2026 年秋に主要 3 社がそろって採用
- **Anthropic**: Claude Mythos（D-16）は Cyber Verification Program（CVP）と Life Sciences Verification Program（LSVP）の承認組織だけ。**CVP は 2026-10-06 に 3 段に再編**
  - **Defense Access**: インシデント対応・マルウェア解析・脆弱性の検証など守りの仕事。企業・非営利・大学・行政・重要インフラ・小規模セキュリティ企業・OSS メンテナー・実績ある個人研究者が対象。審査は数日
  - **Red Team Access**: 許可を得たシステムへの侵入テスト・レッドチーム。組織のみ（個人は不可）。審査は数週間
  - **Specialized Access**: 電力網や航空システムなど安全上重要なシステムを試験する少数の組織。米国政府と一緒に審査
  - 条件: 身元確認・セキュリティ管理の提示・**悪用監視のためのデータ保持**
  - 旧 Project Glasswing（D-14）を統合。Glasswing 参加組織は 2026-04〜07 に検証済み脆弱性 12 万 9,000 件以上を報告
- **OpenAI**: GPT-6 Astra（D-27）のサイバー能力は信頼アクセスプログラム「Daybreak」経由。生命科学向けの GPT-6 Rosalind は承認組織のみ
- **Google**: Gemini 4 Carbon（D-6）は Fairwind プログラムの検証済みサイバー防御組織から先行提供。Gemini 3.5 / 3.8 Flash の Cyber 版も Fairwind 限定
- **考え方の核**: **同じモデルでも、相手が誰かによって外す安全装置が違う**。Anthropic の Fable と Mythos は「同じモデルに別の安全装置」
- **背景**: 守る側（脆弱性を見つけて直す）と攻める側（悪用する）で同じ能力が使われる＝**デュアルユース（両用）**。全員に開くと攻撃にも使われ、全員に閉じると守る側が後れを取る。その中間として「相手を確かめてから開く」
- オープンウェイト（D-26 / D-48 など）とは正反対の方向。「誰でも持てる」と「確かめた相手だけ」が同時に進んでいるのが 2026 年の構図
- 出典: https://www.anthropic.com/news/cyber-verification-program ／ https://www.anthropic.com/claude-fable-and-mythos-5-1 ／ Google ブログ「Gemini 4 Carbon」（検索経由）／ OpenAI GPT-6 Astra 関連報道（検索経由）

### 書き方の指示

- figure_type `structure`。**1 つの建物に 3 つの扉**（一般／守りの仕事／試験の仕事）。奥の扉ほど検問が厳しい
- 読者への価値: ニュースで「最強モデル」と聞いても**自分では使えない理由**が分かる。「使えない＝劣っている」ではない
- J-135 機能安全・J-140 IEC 62443 の「ゾーン（区切り）」と同じ発想であることを 1 文で橋渡し可（著者の専門領域）
- 書かないこと: 申請手順の詳細、各社プログラムの比較表の全項目

---

## J-152 蒸留攻撃

### 押さえる事実（Anthropic 公式で確認）

- **蒸留攻撃（distillation attacks）**: 他社のモデルの能力を、許可なく大規模に自社モデルへ写し取ろうとする行為。**多数の不正アカウントのネットワーク**を使うことが多い（Anthropic 2026-10-12「Strengthening our defenses against distillation attacks」）
- J-36 **蒸留**（大きいモデルの出力で小さいモデルを学習させる正当な技術）を、**許可なく他社に対して行う**のが蒸留攻撃
- **狙われるのは最終回答より「思考の過程（推論の記録）」**。教材として価値が高いため
- Anthropic の懸念: 写し取られたモデルは安全装置が弱いことがあり、生物・サイバー分野での悪用や、軍事・監視システムへの転用につながりうる
- **対策の 4 段**:
  1. **推論の要約**: 生の思考ではなく要約を返す。試験では、要約で学習したモデルの SWE-bench Verified が 80.4%（全文で学習）→ 71.8% に下がった
  2. **preserved thinking**: Fable 5.1 と Opus 5.5 から。**2026-08-31 以降に作られた API アカウントは、過去の思考を保ったまま以前の文脈を書き換えられない**。新しいモデルの推論を、安全装置の弱い古いモデルが読めないようにする
  3. **2 段階の分類器**で抽出の試みを検知・遮断（誤検知率 0.1% 未満）
  4. **繰り返す相手への抑止**: 利用制限・アカウント停止。**2026-09-24 から、安全装置が回答前にブロックしたリクエストも課金**
- **効果**: 収集されるデータが 90〜99% 減少、抽出できる推論トークンが 10〜100 倍以上減少、関連アカウント数万件を停止（多くはキャンペーン開始から 2 時間以内）
- **代償**: 一部の開発者は連携の改修が必要、まれに正当なリクエストもブロック、売上の減少
- 2026-02 の報告では 2 万件超の不正アカウントを運用するネットワークが確認された
- Anthropic 自身「いたちごっこが続く」「業界全体で防ぐ責任を分け合うべき」と述べている
- 出典: https://www.anthropic.com/news/distillation-defenses

### 書き方の指示

- figure_type `workflow`。左から「不正アカウント群が大量に質問 → 思考の記録を集める → 自社モデルを学習」の流れに、対策 4 段を「関所」として差し込む
- **非エンジニア読者に効く点**: 自分は攻撃者でなくても、**対策の影響は受ける**（思考が要約で返る／API で過去の文脈を編集できない／まれな誤ブロック）。「なぜ思考の中身が全部見えないのか」の答えになる
- J-36 蒸留と必ず相互参照し、「技術としての蒸留は悪ではない」ことを明記
- 書かないこと: 特定の国・企業名を名指しする記述

---

## 改訂対象（既存エントリ。親エージェントが直接手当て）

| ID | 何が古いか | 直し方 |
| :-- | :-- | :-- |
| D-4 Gemini 3.1 系 | 後続（3.5〜3.8 / 4）への言及なし | 備考・関連用語に D-5 / D-6。Gemini アプリでは 4 Argon と並んで選べる |
| D-12 Claude 4 系 | Opus 4 / Sonnet 4（2026-06-15）・Opus 4.1（2026-08-05）退役 | 備考に提供状況を追記 |
| D-13 Claude 4.5 系 | Sonnet 4.5 が 2026-09-30 非推奨、2026-11-30 退役予定 | 備考と本文の「3 モデルとも提供中」を修正 |
| D-14 Claude Mythos Preview | 2026-06-09 に非推奨。後継は Mythos 5 / 5.1。Glasswing は CVP に統合 | `version_status: deprecated`、開発フロー Step 4 の参照先を D-16 に |
| D-20 GPT-5 系 | GPT-5.5 が 2026-10-14 に ChatGPT から引退 | 備考・関連用語に D-27 |
| D-30 Grok 系 | Grok 4.5〜4.7 が未収録、Grok 5 は未公開 | 備考に追記 |
| D-44 Kimi | Kimi K3（2026-07）とライセンス変更 | 備考に追記 |
| G-9 effort レベル | tagline「既定は high」が誤りに（モデルごとに違う） | tagline と本文を修正 |
| G-14 Thinking モデル | Adaptive thinking が標準に | 備考に追記 |
| G-24 Temperature | Claude API 版 2026-10-21 で temperature / top_p / top_k が削除（指定すると 400 エラー） | 備考の記述を更新 |
| C-2 Anthropic | 2026-10-26 に IPO の S-1 を SEC に提出／Agent Skills を AAIF に寄贈 | 備考に追記 |
| G-22 SKILL.md | Agent Skills 標準が 2026-10-22 に Agentic AI Foundation（Linux Foundation 傘下）へ寄贈 | 備考に追記 |
