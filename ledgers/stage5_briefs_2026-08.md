# Stage 5 ブリーフ（2026-08-10）— H 章の歴史・文化 9 件

*台帳に行はあるのにファイルが生成されていなかった 27 件のうち、H 章の歴史・系譜 9 件を本書きするための下準備メモです。[ledgers/stage4_briefs_2026-08.md](stage4_briefs_2026-08.md) と同じ役割で、entry-writer サブエージェントに渡す前提で書いています。*

## この束の性格 — 用語カードではなく「読み物」

他の letter が「用語を引く」ページなのに対し、H-50 台は**出来事の順番を追う**ページです。書き方が変わります。

- `figure_type: timeline` を基本にする（比較が主題のときだけ comparison）
- **年月を必ず添える**。「最近」「近年」で濁さない
- 出来事を並べるだけで終わらせず、**「それで何が変わったのか」を 1 文入れる**
- 既存の H-53 ChatGPT 登場 / H-54 GPT-4 リリース / H-56 Claude のバージョン史 / H-58 Transformer 論文 / H-64 DeepSeek ショック を読んで、書き方と密度を揃えること

## 使い方

- 「押さえる事実」は 2026-08-10 に web で確認した内容です。**出典メモにはここに挙げた URL と `checked 2026-08-10` を書いてください**
- `evaluation_date: 2026-08-10`
- 「書かないこと」は、隣接エントリとスコープが被るため触れない範囲です

## 事実の扱いで注意すること

- **GitHub Copilot の「登場年」は情報源によって 2021 と 2022 で割れます**。実際は **2021 年 6 月にテクニカルプレビュー、2022 年 6 月に一般提供**で、どちらも間違いではありません。**両方を書く**のが正解です
- **「AI エージェント元年」は 2025 年**を指すのが一般的です。ただし「元年」は何度も言われる言葉なので、**唯一の正解として断定しない**書き方にしてください
- **Gemini の世代番号**は動きが速い領域です。1.0 / 1.5 / 2.0 / 2.5 / 3 系という**流れ**を書き、「現行最新は◯◯」という断定は避けるか `evaluation_date` を添えること
- 人物の動機・内心（「〜と考えて辞めた」等）は本人の公表発言の範囲に留め、推測で書かないこと

---

## H-50 Bard → Gemini

- **位置づけ**：「サービス名が変わる」という、この分野で読者がいちばん戸惑う現象の代表例
- **押さえる事実**：Google の対話 AI は 2023 年に **Bard** として登場した／2023 年 12 月に **Gemini** という名前の AI モデル群を発表／**2024 年 2 月 8 日**、サービス名を Bard から Gemini に統一し、最上位モデルを含むアプリを一般公開した／改名の理由は「モデル名（Gemini）とサービス名（Bard）が別々で分かりにくい」という一本化／読者にとっては「昨日まで使っていたサービスの名前が変わった」という体験になる
- **出典**：Google 公式ブログ「Bard から Gemini へ」<https://blog.google/intl/ja-jp/company-news/technology/bard-gemini-ultra-jp/>、日経クロステック <https://xtech.nikkei.com/atcl/nxt/news/24/00220/>
- **書かないこと**：Gemini の世代ごとの中身（H-57）、サービスとしての Gemini の使い方（B-1）
- 目安 reader_level 1-2 / importance B / figure_type timeline

## H-51 Preview から正式版への流れ

- **位置づけ**：**手順と判断材料**の側。H-61「Preview 版という文化」とは役割が違うので、必ず読み分けること
- **押さえる事実**：多くのサービスは 内部テスト → 限定プレビュー → 公開プレビュー → **GA（一般提供）** という段階を踏む／プレビュー段階のものは**サービス品質の保証（SLA）の対象外**で、提供側は予告なく仕様変更や提供終了ができる／公開プレビューは誰でも使えるが、本番業務に乗せることは推奨されていない／画面や公式ドキュメントに「（プレビュー）」と明記されるのが通例／したがって「試すのは自由、業務の土台に据えるのは GA を待つ」が判断の基本形
- **出典**：Google Cloud のリリース段階の説明 <https://cloud.google.com/products?hl=ja#product-launch-stages>、Google Workspace「ソフトウェア テストのフェーズと GA について」<https://knowledge.workspace.google.com/admin/releases/what-are-software-testing-phases-and-ga?hl=ja>
- **書かないこと**：なぜ AI 業界がプレビューを多用するのかという文化論（H-61）
- 目安 reader_level 2-3 / importance C / figure_type timeline

## H-52 Copilot から Claude Code までの流れ

- **位置づけ**：AI コーディングツールが「補完 → 会話 → エージェント」と変わってきた系譜。読者が今使っている道具の来歴
- **押さえる事実**：**2021 年 6 月**、GitHub Copilot がテクニカルプレビューとして登場し、**2022 年 6 月**に一般提供された。役割は「書きかけの行の続きを補完する」こと／**2023 年**、チャットで相談しながら直す形（Copilot Chat 等）が広がる／同じ 2023 年、AI を前提に作られたエディタ **Cursor** が登場し、複数ファイルの編集まで踏み込む／**2024 年**、Devin のように「タスクを渡すと自分で進める」自律型が話題になる／**2025 年**、Anthropic の **Claude Code**（同年 2 月にリサーチプレビュー、5 月に一般提供）や OpenAI の Codex CLI など、ターミナルで動くエージェントが主流の選択肢に加わる／変化の本質は「人が書くのを助ける」から「人が方針を決め、AI が手を動かす」への移動
- **出典**：GitHub Copilot（Wikipedia、沿革の確認用）<https://en.wikipedia.org/wiki/GitHub_Copilot>、Anthropic <https://www.anthropic.com/news/claude-code>
- **書かないこと**：各ツールの使い方（B-5 / B-4 / B-7 / B-10）、Codex ブランドの変遷（H-60）
- 目安 reader_level 2-3 / importance B / figure_type timeline

## H-57 Gemini の命名史

- **位置づけ**：H-56「Claude のバージョン史」の Google 版。番号とサイズ名の読み方が分かるようになるページ
- **押さえる事実**：**2023 年 12 月**の Gemini 1.0 で、**Ultra / Pro / Nano** という「大きさ違いの 3 兄弟」という考え方が示された／**2024 年**の 1.5 系で扱える文脈の量が大きく広がった／2.0 系以降、速さ重視の **Flash**、さらに軽い **Flash-Lite** という呼び名が定着し、Ultra は前面に出なくなった／2.5 系、3 系と続き、番号は「世代」、Pro / Flash は「同じ世代の中での大きさ・速さの違い」を表す／読者にとっての要点は、**数字が大きいほど新しい世代、Pro は賢さ寄り、Flash は速さと安さ寄り**という読み替えができること
- **出典**：Google DeepMind の Gemini モデル一覧 <https://deepmind.google/models/gemini/>、Gemini API のモデル説明 <https://ai.google.dev/gemini-api/docs/models>
- **書かないこと**：個別世代の性能比較（D-1〜D-4）、Bard からの改名の経緯（H-50）
- 目安 reader_level 2-3 / importance B / figure_type timeline

## H-59 AI エージェント元年

- **位置づけ**：G-49「AI エージェント」の歴史側。なぜ 2025 年に一気に言葉が広まったのか
- **押さえる事実**：**2025 年**が「AI エージェント元年」と呼ばれることが多い／2025 年 1 月に OpenAI が Operator（ブラウザを操作するエージェント）を公開したあたりから、主要各社がエージェント関連の製品と構想を相次いで打ち出した／同じ年に Manus のような汎用エージェント、Claude Code のようなコーディングエージェントが実用の選択肢になった／「会話するだけの AI」から「手を動かす AI」への移動が、実務で語られるようになった年という位置づけ／ただし「元年」という言い方は分野を問わず繰り返し使われるので、唯一の正解ではなく「そう呼ばれた」という事実として扱う
- **出典**：ソフトバンク クラウドテクノロジーブログ「AI エージェント元年である 2025 年を振り返ってみよう！」<https://www.softbank.jp/biz/blog/cloud-technology/articles/202512/ai-agents-2025/>、Anthropic「Building effective agents」<https://www.anthropic.com/engineering/building-effective-agents>
- **書かないこと**：エージェントの定義そのもの（G-49）、個別サービスの紹介（B-38 など）
- 目安 reader_level 2-3 / importance B / figure_type timeline

## H-60 Codex → GitHub Copilot の系譜

- **位置づけ**：「Codex」という名前が一度消えて戻ってきた話。H-52 が道具の系譜なのに対し、こちらは**ブランドと中身の変遷**
- **押さえる事実**：**2021 年 8 月**、OpenAI が GPT-3 をコードで追加学習した **Codex** を公開／初代 GitHub Copilot の中身はこの Codex だった／**2023 年 3 月**、OpenAI は API から Codex モデルを提供終了し、Copilot の中身は GPT-4 系など後継モデルへ入れ替わっていった／その後 2 年ほど「Codex」はほぼ使われない名前になる／**2025 年**、OpenAI は同じ名前を、単なるモデルではなく**自分で作業を進めるコーディングエージェント**として復活させた（Codex CLI など）／同じ名前でも 2021 年と 2025 年で指すものが違う、というのが読者のつまずきどころ
- **出典**：OpenAI Codex（Wikipedia、沿革の確認用）<https://en.wikipedia.org/wiki/OpenAI_Codex_(language_model)>、GitHub Blog「Under the hood: Exploring the AI models powering GitHub Copilot」<https://github.blog/ai-and-ml/github-copilot/under-the-hood-exploring-the-ai-models-powering-github-copilot/>
- **書かないこと**：ツール全体の系譜（H-52）、Codex の使い方（B-8）
- 目安 reader_level 2-3 / importance C / figure_type timeline

## H-61 Preview 版という文化

- **位置づけ**：**なぜこの業界はプレビューだらけなのか**という文化の側。H-51（手順と判断材料）とは役割が違うので、必ず読み分けること
- **押さえる事実**：AI 分野では、完成してから出すのではなく、未完成のまま出して使われながら直す進め方が一般的になった／背景には、実際に使われないと弱点が分からない種類の製品であること、競争が速く先に出す価値が大きいことがある／読者側の体感としては、**名前が変わる・機能が急に増える・使えていたものが消える**という形で現れる／一方で、無料または安く最新のものを試せる、フィードバックが製品に反映されるという利点もある／付き合い方は「重要な業務の土台にはしない」「消えても困らない使い方から始める」
- **出典**：Google Cloud のリリース段階の説明 <https://cloud.google.com/products?hl=ja#product-launch-stages>、Anthropic のリサーチプレビューの扱い <https://www.anthropic.com/news/claude-code>
- **書かないこと**：プレビュー → GA の段階の定義（H-51）
- 目安 reader_level 1-2 / importance C / figure_type structure

## H-62 Anthropic 創業の流れ

- **位置づけ**：C-2 Anthropic（会社紹介）の歴史側。なぜ OpenAI から人が離れて別の会社ができたのか
- **押さえる事実**：**2020 年 12 月**、OpenAI は Dario Amodei の退職を発表（在籍約 5 年、研究部門の責任者だった）／**2021 年**、Dario Amodei と妹の Daniela Amodei を中心に、OpenAI 出身の 8 人で Anthropic を設立。Dario が CEO、Daniela が社長／設立の趣旨として、安全性の研究と製品開発が両立する研究所を作る、という考えが公表されている／その後 Claude シリーズを送り出し、Google や Amazon から大型の出資を受けて主要ベンダーの一角になった／「安全性を掲げる会社が、同時に最前線の製品も出す」という立ち位置が特徴
- **出典**：<https://www.anthropic.com/company>、Anthropic（Wikipedia、沿革の確認用）<https://en.wikipedia.org/wiki/Anthropic>
- **書かないこと**：会社の現在の事業内容（C-2）、Claude のバージョン史（H-56）
- 目安 reader_level 2-3 / importance C / figure_type timeline

## H-63 Vibe Coding 命名

- **位置づけ**：**この本のタイトルそのものの由来**。G-40「バイブコーディング（用語）」の歴史側で、本書の中でも特別な 1 本
- **押さえる事実**：**2025 年 2 月 2 日**、Andrej Karpathy（C-53）が X への投稿で "vibe coding" という言い方を示した／趣旨は「雰囲気に身を任せ、コードが存在することすら忘れる、新しい種類のコーディング」／背景として、モデルが十分よくなったことを挙げていた／投稿は数百万回規模で読まれ、短期間で一般語に近い広がり方をした／Karpathy 本人は後に、これは**気軽に投げた思いつきの投稿**だったと振り返っており、元々は捨ててもいい週末の小さな制作を想定した言葉だった／広まる過程で、本人の意図より広い意味（業務開発まで含む）で使われるようになった、という経緯がある
- **出典**：Karpathy の投稿（2025-02-02）<https://x.com/karpathy/status/1886192184808149383>、本人の振り返り投稿 <https://x.com/karpathy/status/2019137879310836075>
- **書かないこと**：バイブコーディングの実践（G-40）、Karpathy の人物紹介（C-53）
- 目安 reader_level 1-2 / importance B / figure_type timeline
