# Stage 3 ブリーフ（2026-08-10）— 収録語の抜け監査 34 件

*[docs/design_improvement_proposal_2026-08.md](../docs/design_improvement_proposal_2026-08.md) §4 で洗い出した追加語を本書きするための下準備メモです。`ledgers/stage2_briefs.md` と同じ役割で、entry-writer サブエージェントに渡す前提で書いています。*

## 使い方

- 各項目の「押さえる事実」は 2026-08-10 に web で確認した内容です。**出典メモにはここに挙げた URL と `checked 2026-08-10` を書いてください**
- 数字・料金・バージョンは時変情報です。`evaluation_date: 2026-08-10` を必ず入れる
- 「書かないこと」は、隣接エントリとスコープが被るため触れない範囲です
- reader_level / importance は目安。エントリを書きながら妥当な値へ寄せて構いません

## 事実の扱いで注意すること（今回の調査でぶつかった点）

- **Gemini CLI**：まとめ系の記事に「2026-06-18 に個人向け無料ログインが終了した」とする記述がありますが、**公式リポジトリ（GitHub google-gemini/gemini-cli）の README は現在も Google アカウントログインで 60 req/min・1,000 req/日と案内しています**。公式側を採用し、無料枠の終了は書かないでください
- **Sakana AI の調達額**：記事によって「シリーズ B 約 200 億円・累計 520 億円・評価額 4,000 億円」と「約 320 億円・累計 660 億円・評価額 4,320 億円」の 2 系統があり一致しません。**具体的な金額は書かず**「シリーズ B で数百億円規模を調達し、国内有数の評価額になっています」程度に留める
- **ARC-AGI のスコア**：リーダーボードは頻繁に動きます。特定モデル名＋小数点つきスコアは書かず、「人間平均（約 66%）を超える報告が出ている段階です（2026-08 時点）」のように幅を持たせる
- **DeepSeek V4 / NotebookLM の改称**：まとめ記事にのみ出てくる話は採用しない。確実な範囲（V3 / R1 が重み公開された、NotebookLM は Google のソース限定ノートツール）で書く

---

## B — サービス

### B-34 NotebookLM

- **位置づけ**：非エンジニア読者にいちばん刺さっている Google ツール。「自分が渡した資料だけを根拠に答える」点が ChatGPT 等との決定的な違い
- **押さえる事実**：PDF・Google ドキュメント・Web ページ・YouTube 動画などをソースとして登録し、その範囲だけで要約・質問応答する／回答に引用（どのソースのどこか）が付く／音声概要（Audio Overview）は資料を 2 人の会話番組風に変換する機能／動画概要もある／無料版と有料版でノートブック数・ソース数・1 日の質問回数の上限が違う
- **出典**：<https://notebooklm.google.com/>、Google の NotebookLM ヘルプ <https://support.google.com/notebooklm>
- **書かないこと**：Gemini 本体の説明（B-1）、RAG の仕組みそのもの（G-15）
- 目安 reader_level 1-2 / importance B / figure_type structure

### B-35 Gemini CLI

- **位置づけ**：Claude Code（B-7）・Codex（B-8）と並べて比較される、無料で始めやすいターミナル型エージェント
- **押さえる事実**：Google 製のオープンソース（Apache-2.0）／ターミナルで動き、ファイル読み書き・シェル実行・Web 検索・MCP 連携ができる／Google アカウントでログインすると 60 リクエスト/分・1,000 リクエスト/日の枠で Gemini 3 系が使える／API キー方式・Vertex AI 方式も選べる／100 万トークン級の文脈
- **出典**：<https://github.com/google-gemini/gemini-cli>（README、checked 2026-08-10）
- **書かないこと**：Gemini モデル自体の世代比較（D-1〜4）
- 目安 reader_level 2-3 / importance B / figure_type structure

### B-36 Lovable

- **位置づけ**：v0（B-9）・Bolt.new（B-11）と同じ「会話でアプリを作る」棚。フルスタック（画面＋データベース＋ログイン）まで面倒を見るのが特徴
- **押さえる事実**：作りたいものを日本語・英語などの自然文で伝えると、画面・データベース・認証・その配線まで生成する／ターミナルを開かずブラウザで完結／課金はクレジット制で、依頼の複雑さによって消費量が変わる／無料枠と有料プラン（月 25 ドル前後の Pro、50 ドル前後の Business、Enterprise）がある
- **出典**：<https://lovable.dev/>、<https://lovable.dev/pricing>
- 目安 reader_level 2-3 / importance C / figure_type flow

### B-37 Replit

- **位置づけ**：ブラウザだけで書いて動かして公開できる開発環境。学習用としても、AI エージェント（Replit Agent）付きのアプリ生成環境としても使われる
- **押さえる事実**：環境構築なしでブラウザ上にエディタ・実行環境・公開先が揃う／Replit Agent は指示から実装・テスト・デプロイまで自律的に進める（2026 時点の Agent 3 は長時間の自走と多数の外部サービス連携に対応）／料金は無料枠と有料プラン（Core は月 20 ドル前後）があり、2026 年に「作業量に応じた従量課金」へ移行した
- **出典**：<https://replit.com/>、<https://replit.com/pricing>
- **書かないこと**：エージェント一般論（G-49 に譲る）
- 目安 reader_level 2-3 / importance C / figure_type flow

### B-38 Manus

- **位置づけ**：コードに閉じない「汎用タスク代行」型エージェントの代表。調査・資料作成・予約作業などを丸ごと任せる使われ方
- **押さえる事実**：2025 年前半に招待制で登場して話題になり、その後一般公開された／指示を出すと計画を立て、Web を見て回り、成果物（資料・表・簡単なアプリ）まで作る／無料枠と有料プラン（月 20 ドル前後から）があり、クレジット制／2026 年にはデスクトップ版も出て PC 上の作業も任せられる／中国発のサービスであることを理由に、企業では扱うデータを選ぶ判断が要る
- **出典**：<https://manus.im/>
- 目安 reader_level 2-3 / importance C / figure_type flow

### B-39 Google AI Studio

- **位置づけ**：「API キーを取る」の実物に最初に触れる場所。F-214 API キーとセットで読める入口
- **押さえる事実**：ブラウザ上で Gemini を試せる開発者向けの入口／Google アカウントだけで始められ、クレジットカード登録なしの無料枠がある／画面から API キーを発行でき、自分のプログラムや外部ツールに貼って使う／プロンプトの試し書き、画像や音声を入れた実験ができる
- **出典**：<https://aistudio.google.com/>、<https://ai.google.dev/gemini-api/docs/api-key>
- 目安 reader_level 2-3 / importance B / figure_type structure

### B-42 Discord

- **位置づけ**：AI コミュニティの実際の集合場所。「公式 Discord に来て」と言われて戸惑う読者向け
- **押さえる事実**：もともとゲーマー向けに広まったチャットサービス／サーバー（コミュニティ単位）→ チャンネル（話題単位）→ スレッドという構造／AI 分野では開発元の公式サーバーが窓口になり、リリース情報・不具合報告・使い方相談が集まる／Midjourney のように Discord 上での操作が入口だったサービスもある
- **出典**：<https://discord.com/>
- **書かないこと**：Reddit（B-40）との比較を長く書きすぎない（1 文で住み分け）
- 目安 reader_level 1-2 / importance C / figure_type structure

### B-43 n8n・Dify

- **位置づけ**：非エンジニアが「AI を自分の業務に組み込む」ときに名前が挙がる 2 つ。役割が違うので並べて説明する
- **押さえる事実**：n8n はワークフロー自動化ツールで、外部サービス同士をノードでつないで「起点 → 処理 → 通知」を組む／Dify は LLM アプリ構築に特化し、RAG・エージェント・チャットボットをノーコードで作って API として公開できる／どちらもオープンソース版があり、自社サーバーで動かせる／「n8n を手足、Dify を頭脳」として併用する構成も増えている
- **出典**：<https://n8n.io/>、<https://dify.ai/>
- 目安 reader_level 2-3 / importance C / figure_type flow

---

## C — 人・会社

### C-16 DeepSeek（企業）

- **位置づけ**：モデル項目（D-46 V3 / D-47 R1）はあるのに企業項目がなかった穴埋め。H-64 DeepSeek ショックの主役
- **押さえる事実**：2023 年設立、中国・杭州の AI 開発企業／親会社は量的取引のヘッジファンド High-Flyer、創業者は梁文鋒（Liang Wenfeng）／モデルの重みを公開する方針で、V3・R1 が広く使われた／API 価格が主要な商用モデルより大幅に安い／低コストでの学習を主張したことが 2025 年 1 月の市場の動揺につながった
- **出典**：<https://www.deepseek.com/>、<https://en.wikipedia.org/wiki/DeepSeek>
- **書かないこと**：モデル個別の性能比較（D-46 / D-47）、株価の話（H-64）
- 目安 reader_level 2-3 / importance B / figure_type structure

### C-17 Sakana AI

- **位置づけ**：日本の読者にとっていちばん身近な「日本発の AI 研究会社」
- **押さえる事実**：2023 年設立、東京・港区／Transformer 論文の共著者 Llion Jones と、Google Brain 出身の David Ha が創業に関わる／自然界の群れ・進化に着想を得た手法（複数モデルを掛け合わせる進化的モデルマージなど）を打ち出している／シリーズ B で数百億円規模を調達し、国内有数の評価額のスタートアップになった／金融・製造など国内企業との実装連携を進めている
- **出典**：<https://sakana.ai/>、<https://en.wikipedia.org/wiki/Sakana_AI>
- **書かないこと**：具体的な調達額・評価額（情報源で食い違うため）
- 目安 reader_level 2-3 / importance C / figure_type structure

---

## D — モデル

### D-59 Midjourney

- **位置づけ**：画像生成の一般名詞級サービス。DALL-E（D-50）／Stable Diffusion（D-54）／Imagen（D-51）と並ぶ最後の 1 枠
- **押さえる事実**：文章から画像を作るサービスで、独特の作風の強さ（絵として整った出力）で知られる／もともと Discord 上でコマンドを打って使う形式で広まり、現在は Web 版も使える／無料枠はなく、月 10 ドル前後の下位プランから／2026 年時点の最新は V8 系で、高解像度出力や指示の解釈精度が上がっている／動画生成にも対応が広がっている
- **出典**：<https://www.midjourney.com/>、<https://docs.midjourney.com/>
- 目安 reader_level 1-2 / importance B / figure_type structure

### D-61 AlphaFold

- **位置づけ**：AlphaGo（D-60）はあるのにノーベル賞の AlphaFold がない、の穴埋め。「AI が科学を進めた」代表例
- **押さえる事実**：Google DeepMind が作った、タンパク質の立体構造を予測するモデル／2021 年の AlphaFold2 が精度の転換点になり、実験で解くのに数年かかる構造を短時間で高精度に予測した／予測結果は AlphaFold Protein Structure Database で 2 億件規模が公開され、誰でも参照できる／2024 年の AlphaFold3 は複合体（タンパク質と薬の候補分子など）の予測に広がり、非商用向けにコードが公開された／開発の中心だった Demis Hassabis と John Jumper は 2024 年のノーベル化学賞を受賞
- **出典**：<https://deepmind.google/science/alphafold/>、<https://alphafold.ebi.ac.uk/>、<https://www.nobelprize.org/prizes/chemistry/2024/summary/>
- 目安 reader_level 2-3 / importance C / figure_type structure

---

## E — ベンチマーク

### E-28 ARC-AGI

- **位置づけ**：E 章の「数字の読み方」路線。知識量ではなく「その場で規則を見つける力」を測る点が他と違う
- **押さえる事実**：François Chollet が 2019 年に提案した、色つきマス目のパズル形式のベンチマーク／数個の例から規則を推論して、新しい入力に当てはめる／人間には簡単だが AI には長く難しかったため「AGI に近づいたか」の物差しとして参照されてきた／2025 年に難度を上げた ARC-AGI-2 が公開され、ARC Prize というコンペが併走している／2026 年 8 月時点では上位モデルが人間平均（約 66%）を超えたとする報告が出ており、数字は短期間で動く
- **出典**：<https://arcprize.org/>、<https://epoch.ai/benchmarks/arc-agi-2>、ARC-AGI-2 論文 <https://arxiv.org/abs/2505.11831>
- 目安 reader_level 3-4 / importance C / figure_type comparison

---

## F — 従来コーディングの言葉

### F-213 API

- **位置づけ**：非エンジニアの最頻出つまずき語。F-210 JSON Schema / F-212 OpenAPI / G-33 Function Calling が説明なしで使っている土台
- **押さえる事実**：Application Programming Interface の略／ソフト同士が決まった形でやり取りするための窓口で、内部の作りを知らなくても「この形で頼めばこの形で返る」が保証される／Web の API はリクエストを送りレスポンス（多くは JSON）を受け取る形／エンドポイント（宛先の URL）・メソッド・認証がセットで語られる／AI サービスも API 経由で自分のアプリに組み込める
- **出典**：MDN「Web API」<https://developer.mozilla.org/ja/docs/Web/API>、<https://developer.mozilla.org/ja/docs/Glossary/API>
- **書かないこと**：OpenAPI 仕様の詳細（F-212）、Function Calling（G-33）
- 目安 reader_level 1-2 / importance A / figure_type structure

### F-214 API キー

- **位置づけ**：バイブコーディングの最初の関門。B-39 Google AI Studio と対で読める
- **押さえる事実**：API を使う人・アプリを識別するための秘密の文字列で、パスワードと同じ扱いが必要／漏れると第三者に使われ、料金が自分に請求される／`.env` ファイルや環境変数に置き、コードに直接書かない・GitHub に上げないのが基本／公開リポジトリへの誤コミットは実際に多い事故で、気づいたら即座に無効化（ローテーション）する／利用量の上限設定やキーの権限制限で被害を小さくできる
- **出典**：<https://ai.google.dev/gemini-api/docs/api-key>、GitHub「シークレットスキャン」<https://docs.github.com/code-security/secret-scanning>
- 目安 reader_level 1-2 / importance A / figure_type structure

### F-45 デプロイ

- **位置づけ**：F-42 ビルドの対になる語。B-20 Vercel / B-21 Netlify などが前提にしている
- **押さえる事実**：手元で動いているものを、誰でもアクセスできる場所（本番環境）に置いて公開する作業／Web アプリなら「ビルドして生成物をサーバーへ配置し、URL でつながる状態にする」まで／Vercel や Netlify のようなサービスは、GitHub に push すると自動でビルドとデプロイをする／うまくいかないときのために、前のバージョンに戻す（ロールバック）手段が用意されている／本番前に確認用のプレビュー環境を挟むのが一般的
- **出典**：<https://vercel.com/docs/deployments>、<https://docs.netlify.com/>
- **書かないこと**：CI/CD の詳細（H-7）
- 目安 reader_level 2-3 / importance B / figure_type flow

### F-46 デバッグ

- **位置づけ**：AI との開発会話で毎日出る語。「バグ」の定義も本エントリで面倒を見る
- **押さえる事実**：バグ（不具合）の原因を特定して直す作業／再現 → 範囲の切り分け → 仮説 → 修正 → 再確認、という順で進むのが基本／エラーメッセージとログが最大の手がかりで、AI に貼るときも「何をしたら何が出たか」をそのまま渡すと精度が上がる／print やログ出力で値を覗く方法と、デバッガでコードを一時停止して調べる方法がある／「バグ」の語源として 1947 年の実機に挟まった蛾の逸話が知られる
- **出典**：MDN「JavaScript のデバッグ」<https://developer.mozilla.org/ja/docs/Learn_web_development/Howto/Solve_HTML_problems>、VS Code Debugging <https://code.visualstudio.com/docs/editor/debugging>
- 目安 reader_level 1-2 / importance B / figure_type flow

### F-18 フレームワーク／ライブラリ

- **位置づけ**：React（F-10）等の説明文に出てくるメタ語彙。2 語の区別は非エンジニアの定番のつまずき
- **押さえる事実**：ライブラリは「必要なときに自分から呼ぶ部品の集まり」／フレームワークは「土台側が全体の流れを持っていて、自分の書いたコードが呼ばれる」形（制御の逆転と呼ばれる）／例：React はライブラリ寄り、Next.js はフレームワーク／フレームワークは決まりごとが多いぶん、迷わず作れて他人が読みやすい／AI に「どの構成で作る？」と聞かれたときに答える必要がある語
- **出典**：MDN <https://developer.mozilla.org/ja/docs/Learn_web_development/Core/Frameworks_libraries>
- 目安 reader_level 2-3 / importance B / figure_type comparison

### F-47 フロントエンド／バックエンド

- **位置づけ**：開発会話の役割分担語。多くの見開きが暗黙に使っている
- **押さえる事実**：フロントエンドは利用者が見て触る画面側、バックエンドはサーバー側でデータの保存・計算・認証を担う裏側／両者は API（F-213）でつながり、画面から「この情報をください」と頼んで受け取る／両方を扱う人はフルスタックと呼ばれる／AI に依頼するときも「画面の話か、裏側の話か」を分けると通りが良い／個人開発では Supabase（B-29）のように裏側を任せる選択もある
- **出典**：MDN <https://developer.mozilla.org/ja/docs/Learn_web_development/Getting_started/Web_standards>、<https://developer.mozilla.org/ja/docs/Learn_web_development/Extensions/Server-side>
- 目安 reader_level 1-2 / importance B / figure_type comparison

---

## G — バイブコーディング特有の言葉

### G-49 AI エージェント

- **位置づけ**：2025〜26 の中心語。H-59「AI エージェント元年」や G-12「Agent Design」が前提にしている本体の定義項目
- **押さえる事実**：目標を渡すと、手順を自分で決めて、道具（ツール）を使いながら達成まで進める AI システム／1 回答えて終わる使い方との違いは「観察 → 判断 → 行動」を繰り返す点／Anthropic の技術記事は、手順が固定されているものを「ワークフロー」、LLM が自分で手順を決めるものを「エージェント」と区別している／自律性が上がるほど柔軟になる一方、暴走・コスト・権限の問題が増えるため、承認（G-39 Permission）や計画の確認（G-38 Plan Mode）が挟まれる
- **出典**：Anthropic「Building effective agents」<https://www.anthropic.com/engineering/building-effective-agents>
- **書かないこと**：Subagent（G-41）・マルチエージェント協調（G-44）の詳細
- 目安 reader_level 2-3 / importance A / figure_type flow

### G-27 プロンプトインジェクション（当初の仮 ID は G-37）

- **位置づけ**：エージェントに仕事を任せる読者が最初に踏むリスク語。G-39 Permission の隣に置ける
- **押さえる事実**：AI に読ませた文章の中に指示を紛れ込ませ、本来の指示を乗っ取る攻撃／直接型（利用者が入力する）と間接型（Web ページ・メール・課題チケットなど AI が読む資料に仕込む）がある／エージェントがメールやブラウザを扱うほど間接型の危険が上がる／OWASP の LLM 向けリスク一覧で最上位に挙げられ続けている／完全に防ぐ方法は確立しておらず、権限を絞る・重要操作は人が承認する・外部に出る通信を監視する、という多層防御が実務の答え
- **出典**：OWASP Top 10 for LLM Applications <https://owasp.org/www-project-top-10-for-large-language-model-applications/>、Anthropic のセキュリティ解説 <https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks>
- 目安 reader_level 2-3 / importance B / figure_type flow

### G-24 Temperature

- **位置づけ**：設定画面や API で読者が直接触る数値。G-8 決定論的／非決定論的の実装面
- **押さえる事実**：出力の「ばらつき」を決める設定値／低くすると毎回似た無難な答えに、高くすると表現が多様になる代わりに脱線しやすくなる／サービスにより 0〜1 や 0〜2 と範囲が違う／要約・分類・コード生成は低め、アイデア出しやコピー案は高め、が一般的な使い分け／Top-p（候補を上位何割に絞るか）と並んで語られる／同じ設定でも毎回同じ答えになるとは限らない
- **出典**：<https://docs.anthropic.com/en/api/messages>、<https://ai.google.dev/gemini-api/docs/text-generation>
- 目安 reader_level 2-3 / importance C / figure_type comparison

### G-25 AI のメモリ機能

- **位置づけ**：チャット画面の設定欄で読者が実際に触る機能。G-1 Context との違いを説明する枠
- **押さえる事実**：過去の会話から利用者の好み・肩書き・進行中の案件などを覚えておき、次の会話に持ち込む仕組み／その都度の文脈（コンテキスト）が会話を閉じると消えるのに対し、メモリは会話をまたいで残る／主要サービスが順次搭載し、Claude は 2025 年に上位プラン、2026 年に無料プランを含めて開放された／他サービスからメモリを引き継ぐ機能も出てきた／何を覚えているかは一覧で確認・削除でき、仕事の秘密を覚えさせない運用判断が要る
- **出典**：<https://support.anthropic.com/>、<https://help.openai.com/en/articles/8590148-memory-faq>
- 目安 reader_level 1-2 / importance B / figure_type structure

### G-26 Computer Use

- **位置づけ**：「AI が自分の PC を操作する」使い方の名前。エージェント（G-49）の一形態として置く
- **押さえる事実**：画面のスクリーンショットを見て、マウス操作とキーボード入力を出力し、人と同じように PC やブラウザを操作させる使い方／Anthropic が 2024 年 10 月に Claude 3.5 Sonnet で公開したのが最初の大きな一歩／2026 年には Claude Cowork や Claude Code から macOS・Windows で使えるようになった／API を持たない古い業務システムの操作や、複数アプリをまたぐ作業の自動化に向く／誤操作・情報の持ち出しリスクがあるため、操作範囲を絞った環境で使うのが基本
- **出典**：<https://www.anthropic.com/news/3-5-models-and-computer-use>、<https://docs.anthropic.com/en/docs/agents-and-tools/computer-use>
- 目安 reader_level 3-4 / importance C / figure_type flow

---

## H — 歴史

### H-64 DeepSeek ショック

- **位置づけ**：株価まで動かした一般ニュース級の転換点。H 章の歴史記事に足りていない 2025 年の山場
- **押さえる事実**：2025 年 1 月下旬、中国の DeepSeek が高性能かつ低コストを掲げたモデルを公開し、米国市場が大きく動いた／2025 年 1 月 27 日に NVIDIA 株が一時 17% 前後下落し、1 社の 1 日あたりの時価総額減少としては過去最大規模と報じられた／「高価な GPU を大量に積まなくても高性能が出せるのでは」という解釈が引き金／DeepSeek のアプリは米国のアプリランキングで上位に入った／その後の NVIDIA の業績は伸びが続き、需要そのものは減らなかった／「効率化は需要を減らすのか増やすのか」という議論を残した
- **出典**：日経クロステック <https://xtech.nikkei.com/atcl/nxt/mag/nc/18/020800017/013001207/>、ITmedia <https://www.itmedia.co.jp/aiplus/articles/2502/04/news121.html>
- **書かないこと**：企業紹介（C-16）、モデル解説（D-46 / D-47）
- 目安 reader_level 2-3 / importance B / figure_type timeline

---

## J — 一般 AI・テック語彙

### J-5 世界モデル

- **位置づけ**：J-1 AGI・J-2 強い AI／弱い AI の隣。「言葉の次に来る」と言われている方向の名前
- **押さえる事実**：世界がどう動くかを内部でシミュレーションし、次に何が起きるかを予測する仕組み／文章の続きを当てる言語モデルに対し、物理的な動きや空間の一貫性を扱おうとする点が違う／ロボット・自動運転・ゲーム環境の生成などが応用先／Google DeepMind の Genie 系（対話できる 3D 環境を生成）、NVIDIA の Cosmos などが 2026 年の代表例／「映像そのものを生成すべきか、抽象的な表現を予測すべきか」で研究の路線が割れている（後者は Yann LeCun が主張してきた方向）
- **出典**：<https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/>、<https://www.nvidia.com/en-us/ai/cosmos/>
- 目安 reader_level 3-4 / importance C / figure_type structure

### J-34 マルチモーダル

- **位置づけ**：主要 3 サービス全部の売り文句。J-15 VLM より先に読者が出会う語
- **押さえる事実**：文字・画像・音声・動画など複数の種類（モダリティ）の情報をまとめて扱えること／「画像を貼って質問する」「スクリーンショットからコードを直してもらう」「音声で話しかける」がすべてこれ／入力だけでなく出力側も画像・音声に広がっている／内部では、種類の違う情報を同じ形式（ベクトル）に変換して同じ土俵に載せている／エラー画面のスクリーンショットを渡す使い方は非エンジニアにとって効果が大きい
- **出典**：<https://ai.google.dev/gemini-api/docs/vision>、<https://docs.anthropic.com/en/docs/build-with-claude/vision>
- **書かないこと**：VLM の構造（J-15）
- 目安 reader_level 1-2 / importance A / figure_type structure

### J-35 スケーリング則

- **位置づけ**：モデル進化ニュースを読む鍵。H 章の歴史記事の背骨にもなる
- **押さえる事実**：モデルの大きさ・学習データ量・計算量を増やすほど、性能がなだらかに（べき乗則で）上がるという経験則／2020 年の OpenAI の研究、2022 年の DeepMind の Chinchilla 研究で「データと大きさの釣り合い」が整理された／「大きくすれば強くなる」を裏づけたことが、各社の巨額投資の根拠になった／2024 年以降は学習だけでなく「答えるときに長く考えさせる（推論時の計算）」を増やす方向にも軸足が移った／法則は保証ではなく観測された傾向で、頭打ちの議論が続いている
- **出典**：Kaplan et al. 2020 <https://arxiv.org/abs/2001.08361>、Hoffmann et al. 2022（Chinchilla）<https://arxiv.org/abs/2203.15556>
- 目安 reader_level 3-4 / importance B / figure_type comparison

### J-36 蒸留

- **位置づけ**：DeepSeek 以降の報道語。J-19 量子化・J-16 Fine-tuning の隣
- **押さえる事実**：大きくて賢いモデル（教師）の出力を手本にして、小さいモデル（生徒）を鍛える手法／単に正解データで学ぶより、教師の「迷い方（確率の分布）」まで真似できるので、小さいまま性能が近づく／2015 年の Hinton らの研究が原点／小型モデルをスマホや手元の PC で動かしたい場面で使われる／「他社モデルの出力を教師に使ってよいか」は利用規約の論点で、報道でも争点になった
- **出典**：Hinton et al. 2015 <https://arxiv.org/abs/1503.02531>
- 目安 reader_level 3-4 / importance C / figure_type structure

### J-38 ムーアの法則

- **位置づけ**：半導体クラスタ（J-95 以降）と一般語彙をつなぐ古典。読者が新聞で見る語
- **押さえる事実**：1965 年に Gordon Moore（Intel 創業者の 1 人）が示した「集積回路に載るトランジスタ数はおよそ 2 年で倍になる」という観測／物理法則ではなく業界の目標として機能し、半世紀にわたり価格性能比の改善を導いた／2010 年代以降は微細化のペースが鈍り「終わった」という議論が続く／一方で、専用チップ（GPU・TPU・NPU）や積層技術によって、用途を絞った性能向上は続いている／AI の進歩を語るときは J-35 スケーリング則と対で引かれることが多い
- **出典**：Intel <https://www.intel.com/content/www/us/en/newsroom/resources/moores-law.html>、Moore 1965 論文
- 目安 reader_level 2-3 / importance C / figure_type timeline

### J-57 RLHF・アラインメント

- **位置づけ**：J-50 AI 倫理・J-51 Hallucination の隣。「なぜ ChatGPT は急に使いやすくなったのか」の答え
- **押さえる事実**：アラインメントは、AI の振る舞いを人間の意図や価値観に沿わせる取り組み全般／RLHF（人間のフィードバックによる強化学習）はその代表的な方法で、人が出力の良し悪しを比べて順位をつけ、それを報酬として学習させる／2022 年の InstructGPT がこの方法の効果を示し、対話 AI が実用的になった転機とされる／人手の代わりに AI に評価させる方式（Constitutional AI / RLAIF）や、より単純化した手法（DPO）も広く使われる／評価者の偏りがそのまま残る、迎合的になる（J-52 Sycophancy）といった副作用が課題
- **出典**：Ouyang et al. 2022（InstructGPT）<https://arxiv.org/abs/2203.02155>、Anthropic「Constitutional AI」<https://www.anthropic.com/news/claudes-constitution>
- 目安 reader_level 3-4 / importance B / figure_type flow

### J-115 NPU・AI PC

- **位置づけ**：PC 売り場で読者が実際に踏む語。J-70 台のハードウェア棚の続き
- **押さえる事実**：NPU は AI の計算（特に推論）に特化した省電力の処理装置で、CPU・GPU と並んで最近のノート PC に載る／性能は TOPS（1 秒あたり何兆回の演算か）で表される／Microsoft の Copilot+ PC は 40 TOPS 以上の NPU・16GB のメモリなどを条件にしている／利点はクラウドに送らず手元で処理できること（速さ・プライバシー・オフライン動作）／大きなモデルを丸ごと動かす用途はまだ GPU とメモリ量が主役で、NPU は字幕生成・画像処理・要約のような常駐処理が中心
- **出典**：Microsoft「Copilot+ PC」<https://www.microsoft.com/en-us/windows/copilot-plus-pcs>
- 目安 reader_level 2-3 / importance C / figure_type comparison

### J-116 TPU

- **位置づけ**：GPU（J-77）・H100（J-72）・Blackwell（J-73）の隣に置く「Google 版」の答え
- **押さえる事実**：Google が自社開発した AI 計算専用チップ（Tensor Processing Unit）／汎用の GPU と違い、AI の計算パターンに絞って設計されているため電力あたりの効率が高い／Google のサービスと Google Cloud で使われ、外部の企業も Vertex AI 経由で利用できる／2026 年には第 7 世代の Ironwood が一般提供に入り、大量の推論をさばく用途が主眼になっている／市場全体では NVIDIA の GPU が大きなシェアを占め、TPU は「自社で作る」路線の代表例という位置づけ
- **出典**：<https://cloud.google.com/tpu>、<https://cloud.google.com/blog/products/compute/introducing-ironwood-tpus>
- 目安 reader_level 3-4 / importance C / figure_type comparison

### J-117 データセンターと電力

- **位置づけ**：2026 年の電力議論。ニュースで読者が最も目にする AI のインフラ話
- **押さえる事実**：AI の学習と推論はデータセンターの計算資源に支えられ、その電力消費が各国で議論になっている／国際エネルギー機関（IEA）の推計では、世界のデータセンターの消費電力は 2022 年の約 460TWh から 2026 年に 620〜1,050TWh の幅に達しうるとされる／生成 AI への 1 回の問い合わせは、検索 1 回よりかなり多くの電力を使うという試算がある／発熱対策として液冷の採用が進み、立地は電力と水の確保で選ばれるようになった／電力系統の増強が追いつかないという指摘があり、原子力や再生可能エネルギーの調達契約が増えている
- **出典**：IEA「Electricity 2024」<https://www.iea.org/reports/electricity-2024>、IEA「Energy and AI」<https://www.iea.org/reports/energy-and-ai>
- 目安 reader_level 2-3 / importance B / figure_type structure
