# エントリ候補リスト

*2026-04-23 更新。letter 別・サブ分類付き。各エントリは「ID — タイトル — 一言」の三点セット。*

*リポジトリ：<https://github.com/Taguchi-1989/VibeCodingDictionary>（以下ここで管理）*

*この回の変更： (1) xAI を 4 番目ベンダーとして D-30〜34 に挿入、その他クローズド（Cursor）を D-35〜39 に新設し、以降の D サブを全て +10 シフト、(2) Cursor Composer は G-37 → D-35 へ移動（モデルとして扱う）、(3) 「アクロミトス」→「Claude Mitos モデル」に訂正し D-14 に追加、(4) 「A step」→「ACE-Step 1.5」として B-61 で確定、(5) D-30 Grok（xAI 系）・F-44 pnpm を追加、(6) 番号運用の再検討を TODO 化。*

## A — はじめに・共通

### 凡例・読み方

- **A-1 まえがき** — 本書の趣旨・読者像
- **A-2 この本の読み方** — 読者レベル別の使い方
- **A-3 図鑑の歩き方** — letter 順と掲載順の違い
- **A-4 体験区分の凡例** — hands_on / partial / research_only
- **A-5 読者レベルの凡例** — Level 1〜6 の目安
- **A-6 評価日・時変情報の見方** — 「いつ時点の情報か」の扱い
- **A-7 図のタイプ** — Before/After・概念図・登場シーン
- **A-8 色・記号の凡例** — 青系・ローズ差し色などの意味
- **A-9 索引** — letter 別／五十音順
- **A-10 更新履歴と更新方針** — 版ごとの変更と補完の呼びかけ
- **A-11 略称表記** — 本書で使う略称（CC = Claude Code など）

## B — サービス

### AI アシスタント系（B-1〜19）

- **B-1 Gemini** — Google の AI アシスタント（チャット／API／Vertex）
- **B-2 Claude** — Anthropic の AI アシスタント
- **B-3 ChatGPT** — OpenAI の AI アシスタント
- **B-4 Cursor** — AI を中核にしたエディタ／IDE サービス
- **B-5 GitHub Copilot** — GitHub × OpenAI のコード補完
- **B-6 Windsurf** — Codeium 社の AI エディタ
- **B-7 Claude Code（略称: CC）** — Anthropic の CLI／エージェント型開発支援
- **B-8 Codex（OpenAI）** — OpenAI の開発者向けエージェント（2025 再登場）
- **B-9 v0** — Vercel の UI 生成 AI
- **B-10 Devin** — Cognition 社の自律 AI 開発者
- **B-11 Bolt.new** — StackBlitz のフルスタック AI アプリ生成
- **B-12 Perplexity** — AI 検索・回答サービス
- **B-13 ElevenLabs** — 高品質な音声生成・音声クローン AI
- **B-14 Genspark** — AI 検索・生成のオールインワン系サービス
- **B-15 Microsoft Copilot** — Microsoft の AI アシスタント・ブランド傘（旧 Bing Chat 系）
- **B-16 Microsoft 365 Copilot** — Office（Word／Excel／PowerPoint 等）に組み込まれた Copilot
- **B-17 Edge Copilot** — Microsoft Edge ブラウザ内の Copilot
- **B-18 Aqua Voice** — AI への入力に向いた高速な音声書き起こしツール
- **B-19 Claude Cowork** — Anthropic が 2026-01 末にリサーチプレビューで公開した、Claude のコーディング支援能力をナレッジワーカーに拡張する機能。Enterprise プランに含まれる（checked 2026-04-24）

### ホスティング・クラウド・BaaS・マネージド AI（B-20〜30）

- **B-20 Vercel** — Next.js を主軸にしたデプロイ／ホスティング
- **B-21 Netlify** — 静的サイト／JAMStack ホスティング
- **B-22 Cloudflare** — CDN／エッジコンピュート／Workers
- **B-23 AWS** — Amazon のクラウド
- **B-24 Google Cloud** — Google のクラウド
- **B-25 Azure** — Microsoft のクラウド
- **B-26 Azure OpenAI** — Azure 上で OpenAI モデルを業務利用する窓口
- **B-27 Vertex AI** — Google Cloud 上で Gemini 等を業務利用する窓口
- **B-28 Render** — シンプルなアプリ／DB のホスティング（Heroku 系）
- **B-29 Supabase** — OSS の BaaS（Postgres ベース。Firebase 代替）
- **B-30 Amazon Bedrock** — AWS 上で複数ベンダーの基盤モデルを使えるマネージドサービス

### 開発・デザインツール SaaS（B-31〜39）

- **B-31 Excalidraw** — 手描き風で素早く描ける共同作図ツール
- **B-32 Figma** — クラウド型の UI／UX デザインツール（業界標準）
- **B-33 Canva** — 非デザイナー向けのテンプレ豊富なデザインツール

### 情報源・コミュニティ・論文（B-40〜49）

- **B-40 Reddit** — AI の話題・速報・議論が集まる英語コミュニティ
- **B-41 arXiv** — AI／物理／数学の論文プレプリントサーバー

### 料金プラン比較（B-50〜59）

> 料金・ティア情報は時変情報。各エントリは `evaluation_date` を必ず持たせて運用する。

- **B-50 Claude の料金プラン** — Free／Pro（$20、年払 $17）／Max 5x（$100）／Max 20x（$200）／Team（$25、年払 $20／席）／Enterprise（個別）の 6 段階（checked 2026-04-24）
- **B-51 ChatGPT の料金プラン** — 無料／Plus（$20）／Pro（$200）の 3 段階
- **B-52 Gemini の料金プラン** — 無料／AI Pro（$20）／AI Ultra（$200 前後）

### 創作・メディア生成 AI（B-60〜69）

- **B-60 Suno** — 歌詞・メロディ・ボーカルを合成する音楽生成 AI
- **B-61 ACE-Step 1.5** — 音楽生成 AI。StepFun 系のオープン音楽モデル／サービス

## C — 人・会社

### 会社・組織（C-1〜29）

- **C-1 OpenAI** — ChatGPT／GPT を提供
- **C-2 Anthropic** — Claude を提供
- **C-3 Google DeepMind** — Gemini を提供
- **C-4 Meta AI** — LLaMA を提供
- **C-5 xAI** — Grok を提供（イーロン・マスク創業）
- **C-6 Mistral AI** — 仏発のオープンモデル企業
- **C-7 Hugging Face** — モデル・データセット共有のプラットフォーム
- **C-8 Microsoft AI** — MS の AI 部門（Copilot 等）
- **C-9 NVIDIA** — GPU 供給で AI の物理層を握る
- **C-10 Moonshot AI** — 中国 AI 企業、Kimi モデルを提供
- **C-11 Z.ai** — 中国 AI 企業、GLM モデルを提供（旧 Zhipu）
- **C-12 TSMC** — 台湾の半導体ファウンドリ世界首位。AI チップの実製造を担う
- **C-13 Groq** — LPU を設計する AI 推論特化チップ企業
- **C-14 AMD** — NVIDIA の競合、CPU／GPU 両方を作る半導体企業

### 人物（C-50〜79）

- **C-50 Sam Altman** — OpenAI CEO。ChatGPT を主導
- **C-51 Dario Amodei** — Anthropic CEO。元 OpenAI の VP of Research
- **C-52 Demis Hassabis** — Google DeepMind CEO。AlphaGo の立役者、2024 ノーベル化学賞
- **C-53 Andrej Karpathy** — 元 OpenAI／Tesla の AI リーダー。YouTube で LLM 教育を発信
- **C-54 Ilya Sutskever** — 元 OpenAI 共同創業者・チーフサイエンティスト。Safe Superintelligence 創業
- **C-55 Mira Murati** — 元 OpenAI CTO。Thinking Machines Lab 創業
- **C-56 Yann LeCun** — Meta のチーフ AI サイエンティスト。CNN の父、2018 チューリング賞
- **C-57 Geoffrey Hinton** — 深層学習の父、2024 ノーベル物理学賞。AI の危険性を警告
- **C-58 Elon Musk** — xAI 創業、Tesla／SpaceX CEO
- **C-59 Jensen Huang** — NVIDIA CEO。基調講演で AI の文脈を作る
- **C-60 Ray Kurzweil（レイ・カーツワイル）** — 未来学者。Singularity 概念の提唱者

### 情報発信者・YouTuber（C-80〜99）

- **C-80 AI大学** — 一般向け AI 情報を広く扱う YouTube チャンネル
- **C-81 にゃんた** — 業務系・実用系の AI 活用を扱う YouTube チャンネル
- **C-82 まさお** — 本質系・日次配信の AI 解説 YouTube チャンネル
- **C-83 AIの羅針盤** — 論文解説中心の AI YouTube チャンネル

## D — モデル

### Google 系（D-1〜9）

- **D-1 Gemini 2 系** — 最初の本格 Gemini 世代
- **D-2 Gemini 2.5 系** — Pro／Flash／Flash-Lite の 3 ティア構成が定着した世代
- **D-3 Gemini 3 系** — 次世代の深掘り版
- **D-4 Gemini 3.1 系** — 3 系のマイナー更新

### Anthropic 系（D-10〜19）

- **D-10 Claude 3 系** — Opus／Sonnet／Haiku の 3 ティア初期
- **D-11 Claude 3.5 系** — Sonnet 3.5 でコーディング適性が跳ねた世代
- **D-12 Claude 4 系** — Opus／Sonnet／Haiku の次世代
- **D-13 Claude 4.5 系** — 4 系のマイナー更新（Claude Code 主力帯）
- **D-14 Claude Mythos（Preview）** — Anthropic が 2026-04-07 に発表した最先端モデル。サイバーセキュリティ特化。限定公開プログラム "Project Glasswing"（Apple／Google／Microsoft／Cisco／Amazon 等）経由で、一般提供はなし。2026-04-21 に不正アクセス事案が報じられた（checked 2026-04-24）

### OpenAI 系（D-20〜29）

- **D-20 GPT-5 系** — OpenAI の最新世代
- **D-21 GPT-4 系** — GPT-4o 等の系譜
- **D-22 o1 系** — 推論特化（Reasoning Model）
- **D-23 o3 系** — o 系の後継
- **D-24 GPT-3 系** — ChatGPT の前身世代（2020）。大型化で衝撃を与えた
- **D-25 GPT-1 / GPT-2 系** — OpenAI 初期の言語モデル（2018-2019）
- **D-26 gpt-oss（OpenAI オープンモデル）** — 2025-08 に公開された gpt-oss-20b／120b。OpenAI 初の公式オープンウェイトモデル

### xAI 系（D-30〜34）

- **D-30 Grok 系** — xAI の言語モデル。Grok 3／4 系と Grok 4 Fast／Heavy 等の派生

### その他クローズドモデル（D-35〜39）

- **D-35 Cursor Composer（モデル）** — Cursor 独自の大規模モデル。マルチファイル編集エージェント Composer を駆動する

### オープンモデル（D-40〜49）

- **D-40 Llama 系** — Meta のオープンモデル
- **D-41 Mistral 系** — Mistral AI のオープンモデル
- **D-42 Gemma 系** — Google のオープンモデル
- **D-43 Qwen 系** — Alibaba のオープンモデル
- **D-44 Kimi** — Moonshot AI のモデル
- **D-45 GLM** — Z.ai のモデル
- **D-46 DeepSeek V3** — DeepSeek の大規模言語モデル（V3 世代、オープン公開）
- **D-47 DeepSeek R1** — DeepSeek の推論特化モデル。思考過程を出す Reasoning 系

### 画像・動画・マルチモーダル（モデル＋ツール）（D-50〜59）

- **D-50 DALL-E** — OpenAI の画像生成
- **D-51 Imagen** — Google の画像生成
- **D-52 Sora** — OpenAI の動画生成
- **D-53 Veo** — Google の動画生成
- **D-54 Stable Diffusion** — Stability AI の画像生成
- **D-55 Nano Banana** — Google の Gemini 画像生成モデル（通称）
- **D-56 Seedance** — ByteDance の動画生成モデル
- **D-57 Flow** — Google Labs の動画作成ツール（Veo ベース）
- **D-58 Whisk** — Google Labs の画像作成ツール（Imagen ベース）

### 歴史的・非 LLM モデル（D-60〜69）

- **D-60 AlphaGo** — Google DeepMind の囲碁 AI。2016 年にトッププロを破った

### 音声・音楽モデル（D-70〜79）

- **D-70 Amical** — ローカルで動く音声認識モデル／ツール（著者確認済で実在）。一次情報 URL は執筆時に確定する（2026-04-24 時点の WebSearch では該当なし、表記ゆれか新興モデルの可能性）
- **D-71 Whisper** — OpenAI が公開したオープンな音声認識モデル。多言語対応、ローカル実行可能（whisper.cpp などの派生あり）。音声書き起こしの事実上の標準

## E — ベンチマーク・評価指標

### コーディング・エンジニアリング（E-1〜19）

- **E-1 SWE-Bench** — 実 OSS の issue を AI が解けるか
- **E-2 SWE-Bench Verified** — 人手で検証済みの SWE-Bench サブセット
- **E-3 Terminal-Bench** — CLI 操作タスクでの成功率
- **E-4 HumanEval** — 関数実装の正解率（古典）

### 推論・知識（E-20〜29）

- **E-20 MMLU** — 57 分野の大学レベル知識
- **E-21 MMLU-Pro** — MMLU の難化版
- **E-22 GPQA** — 大学院レベル科学（特に STEM）
- **E-23 GSM8K** — 小〜中学レベル算数
- **E-24 MATH** — 競技数学
- **E-25 AIME** — 米数学オリンピック予選
- **E-26 Humanity's Last Exam** — 現時点で最難関とされる総合ベンチ
- **E-27 IQ Bench** — IQ テスト形式の推論評価

### エージェント・タスク完遂（E-30〜39）

- **E-30 TAU-Bench** — 対話エージェントの接客タスク
- **E-31 WebArena** — Web 操作タスク
- **E-32 GAIA** — 多面的なエージェント評価
- **E-33 AgentBench** — エージェント総合評価
- **E-34 OSWorld** — デスクトップ OS 操作エージェント

### その他・総合（E-50〜）

- **E-50 Chatbot Arena** — 人間投票の対戦ベンチ（モデル vs モデル）
- **E-51 LMSYS Arena** — Chatbot Arena の旧名／運営団体

## F — 従来コーディングの言葉・道具

### 言語・記法（F-1〜9）

- **F-1 JavaScript** — Web の中核言語
- **F-2 TypeScript** — JS に型を足す言語
- **F-3 Python** — AI やスクリプトで広く使用
- **F-4 HTML** — Web ページの構造を書くマークアップ言語
- **F-5 CSS** — Web ページの見た目を書くスタイル言語
- **F-6 Markdown** — 軽量な文書記法。README や本書のソースにも使う
- **F-7 YAML** — インデント式の設定データ形式
- **F-8 JSON** — 括弧と引用符で書くデータ形式
- **F-9 SVG** — 文字で書けるベクター画像形式

### フレームワーク（F-10〜19）

- **F-10 React** — UI を部品で作る JS ライブラリ
- **F-11 Next.js** — React ベースのフルスタック FW
- **F-12 Electron** — Web 技術でデスクトップアプリを作る FW（重め）
- **F-13 Tauri** — Rust ベースの軽量デスクトップアプリ FW
- **F-14 three.js** — ブラウザ上で 3D を描画する JavaScript ライブラリ（WebGL 上に立つ高レベル層）
- **F-15 shadcn/ui** — React 用のコンポーネント集。npm パッケージではなく CLI でコードを **コピーして配布** するモデル（Radix UI ＋ Tailwind CSS ベース）。Next.js 生態圏で定番

### Linter・整形（F-20〜29）

- **F-20 ESLint** — JS／TS のコードチェッカー
- **F-21 Prettier** — 書式整形ツール

### エディタ・IDE・拡張機能（F-30〜39）

- **F-30 VS Code** — Microsoft のエディタ（業界標準）
- **F-34 VS Code 拡張機能** — 機能を足すプラグインの総称
- **F-35 Markdown Preview Enhanced** — Markdown プレビューを強化する VS Code 拡張
- **F-36 Git Graph** — git 履歴をグラフ表示する VS Code 拡張
- **F-37 Japanese Language Pack for VS Code** — VS Code の日本語化拡張
- **F-38 Markdown All in One** — Markdown 編集を便利にする VS Code 拡張

### CLI・ビルド・パッケージ（F-40〜49）

- **F-40 npm** — Node.js のパッケージ管理
- **F-41 Vite** — 高速フロントエンドビルドツール
- **F-42 ビルド** — ソースコードを配布可能な形へ変換する工程
- **F-43 テスト** — コードが期待通り動くかを自動確認する工程
- **F-44 pnpm** — 高速・省容量なパッケージマネージャ（npm 代替）

### Git（F-50〜59）

- **F-50 git** — バージョン管理システム
- **F-51 git push** — ローカル変更をリモートへ送る
- **F-52 git pull** — リモートから取ってきてマージ
- **F-53 branch** — 並行作業のための枝
- **F-54 commit** — 変更を記録する単位
- **F-55 merge** — 別の枝を取り込む
- **F-56 .gitignore** — git の追跡除外ルールを書くファイル
- **F-57 リポジトリ** — git で管理されるプロジェクトの保管単位
- **F-58 git stash** — 作業中の変更を一時退避する機能
- **F-59 README.md** — プロジェクトの玄関ファイル。全員が最初に見る

### GitHub（F-60〜69）

- **F-60 GitHub** — git のリモートホスティング
- **F-61 Pull Request** — 変更の取り込み依頼
- **F-62 GitHub Actions** — GitHub 上の CI/CD

### 検索・探索（F-70〜79）

- **F-71 ripgrep（rg）** — 高速 grep。Claude Code 等が裏で使う

### ランタイム・シェル・ターミナル（F-80〜89）

- **F-80 Node.js** — JavaScript のサーバー／CLI 実行環境
- **F-81 bash** — Unix 系の標準シェル
- **F-82 WSL** — Windows 上で Linux を動かす仕組み
- **F-83 PowerShell** — Windows 標準のシェル
- **F-84 Ghostty** — 新興の高速ターミナルエミュレータ（Mitchell Hashimoto 作）
- **F-85 SuperClaude Framework** — Claude Code を拡張するコミュニティ OSS。18 のスラッシュコマンド／9 つの専門ペルソナ／トークン最適化を提供。**Anthropic 非公式**。"Supercell" は "SuperClaude" の聞き違いと判明（checked 2026-04-24）
- **F-86 ollama** — ローカルで LLM を動かす実行環境／CLI
- **F-87 sudo** — UNIX 系の権限昇格コマンド（super user do）。一時的に管理者権限で 1 コマンドを実行する。Linux／macOS の基本中の基本

### コンテナ・環境（F-90〜99）

- **F-90 Docker** — コンテナ仮想化。AI 実行環境も一式で配れる
- **F-91 .env** — 環境変数を書いた設定ファイル

### 拡張子早見・メディア形式（F-100〜109）

- **F-100 拡張子早見表** — .js / .ts / .html / .css / .md / .yaml / .json / .svg / .ico / .mp4 / .mp3 等の対応一覧
- **F-101 .ico** — ファビコン（タブに出る小さい画像）
- **F-102 .mp4** — 動画コンテナ形式（MPEG-4 Part 14）
- **F-103 .mp3** — 音声圧縮形式（MPEG-1 Audio Layer III）
- **F-104 .webp** — 高圧縮の次世代 Web 画像形式（Google 策定）

### 品質・計測（F-110〜119）

- **F-110 Lighthouse** — Google の Web 品質監査（性能／SEO／アクセシビリティ）
- **F-111 a11y** — アクセシビリティ（a と y の間に 11 文字）の略

### データベース・ORM（F-120〜129）

- **F-120 PostgreSQL** — OSS の本格 RDB
- **F-121 SQLite** — ファイル一つで完結する軽量 DB
- **F-122 Prisma** — TypeScript 向けの型安全な ORM
- **F-123 ORM** — Object-Relational Mapping。DB の行とオブジェクトを橋渡しする仕組み

### 認証・セキュリティ（F-130〜139）

- **F-130 OAuth** — 他サービスのアカウントでログインを実現する認可の仕組み

### ダイアグラム記法（F-140〜149）

- **F-140 Mermaid** — テキストで描くダイアグラム（GitHub も対応）
- **F-141 PlantUML** — UML 中心のテキスト作図。学習リソースが少なく LLM に書かせにくい例として扱う

### ライセンス・著作権（F-150〜159）

- **F-150 MIT ライセンス** — 「自由に使って、責任は負いません」系の最も緩い OSS ライセンス
- **F-151 Apache 2.0** — 特許条項を含む商用利用寛容な OSS ライセンス
- **F-152 GPL** — 派生物にも同じライセンスを強制するコピーレフト型
- **F-153 Creative Commons（CC）** — 作品（主に非ソフト）の共有ルールを定める一連のライセンス
- **F-154 OSS（Open Source Software）** — ソースコードが公開され利用・改変・再配布が許可された仕組みの総称

### Web の基盤概念（F-160〜169）

- **F-160 DOM** — Document Object Model。ブラウザ上で HTML をツリー構造として扱う仕組み
- **F-161 SSR** — Server-Side Rendering。サーバー側で HTML を組み立てて返す方式
- **F-162 SSG** — Static Site Generation。ビルド時に HTML を生成して静的配信する方式

### クラウドの基本サービス（F-170〜179）

- **F-170 EC2** — AWS の仮想サーバー（Elastic Compute Cloud）
- **F-171 S3** — AWS のオブジェクトストレージ（Simple Storage Service）
- **F-172 IAM** — Identity and Access Management。認証と権限の管理

### グラフィックス・レンダリング（F-180〜189）

- **F-180 OpenGL** — クロスプラットフォームの 3D グラフィックス API（業界標準の古参）
- **F-181 WebGL** — ブラウザ上で OpenGL 相当の 3D 描画を行う Web API

### プログラミングの基礎概念（F-190〜199）

- **F-190 サブルーチン** — 処理の「まとまり」を名前で呼び出せるようにする仕組み。関数・メソッドの元になる古典的概念

### 型・スキーマ・API契約（F-210〜219）

- **F-210 JSON Schema** — JSON の形を機械が検査できるように書くための標準的なルール表
- **F-211 Zod** — TypeScript でデータの形を書き、実行時に検証できるスキーマバリデーションライブラリ
- **F-212 OpenAPI** — API の URL、入力、出力、認証方法を YAML / JSON で記述する仕様

## G — バイブコーディング特有の言葉・ファイル

### 基礎概念（G-1〜9）

- **G-1 Context（コンテキスト）** — LLM に渡す文脈全般
- **G-2 Token** — LLM が数える最小単位（≒単語未満）
- **G-3 Dictation** — 音声入力。会議や指示をテキスト化
- **G-4 System Prompt** — LLM に最初に渡す役割定義
- **G-5 Context Window** — モデルが一度に読める長さの上限
- **G-6 One-shot（例 1 つ提示）** — 1 例だけ見せて解かせる与え方
- **G-7 指示追従性** — 指示にどれだけ素直に従うかの性質
- **G-8 決定論的／非決定論的** — 同じ入力で毎回同じ出力か、揺らぐか
- **G-9 effort レベル** — 推論の深さを指定する設定。low / medium / high / xhigh の粒度で切り替える（各値は個別ページにせず本エントリで束ねて扱う）

### エンジニアリング技法・モデル活用（G-10〜19）

- **G-10 Prompt Engineering** — プロンプトの設計術
- **G-11 Context Engineering** — LLM に渡す文脈全体の設計（より広い概念）
- **G-12 Agent Design** — AI エージェントの振る舞い設計
- **G-13 Few-shot Learning** — 少数の例示で学習させる手法
- **G-14 Thinking モデル（推論モデル）** — 思考過程を明示して出す型のモデル（o1、Claude Extended Thinking、DeepSeek-R1 等）

### AI エージェント設定ファイル（G-20〜29）

- **G-20 CLAUDE.md** — Claude Code 用のプロジェクト説明書
- **G-21 AGENTS.md** — 汎用エージェント向けの説明書
- **G-22 SKILL.md** — エージェントのスキル定義ファイル
- **G-23 .claude/settings.json** — Claude Code の設定

### 連携・制御・機能（G-30〜39）

- **G-30 Tool Use** — LLM がツールを呼び出す機能全般
- **G-31 Hook** — 特定イベントで自動実行する仕組み
- **G-32 Slash Command** — `/` で呼ぶ短縮コマンド
- **G-33 Function Calling** — LLM から関数を呼ぶ API 機能
- **G-34 Code Interpreter** — LLM が Python 等を実行して結果を返す機能（ChatGPT 由来）
- **G-35 Deep Research** — LLM が能動的に複数ステップで Web を調査し長文レポートを返す機能
- **G-36 Artifact（アーティファクト）** — 成果物を独立パネルに出す UI 機能（Claude Artifacts 等）。広義には「生成物／ビルド出力」の総称

> G-37 は旧 Cursor Composer。著者の指示でモデルとして扱うことになり D-35 へ移設（この番号は欠番として残す）。

### 運用・品質（G-40〜49）

- **G-40 バイブコーディング** — AI との対話で作るコーディングの流儀
- **G-41 Subagent** — 親エージェントが呼ぶ子エージェント
- **G-42 Worktree** — git の並行作業用別ディレクトリ
- **G-43 オーケストレーション** — 複数エージェント／ツールを束ねて動かす設計
- **G-44 マルチエージェント協調** — 複数 AI が役割分担しながら解く方式
- **G-45 段階的開示** — 情報をいきなり全部出さず、段階的に見せる与え方
- **G-46 ナーフ（モデルの劣化）** — ユーザー体感で「最近弱くなった」と言われる現象
- **G-48 Structured Outputs** — LLM の返答を JSON Schema などで決まった形に寄せる出力制御

## H — 進め方・歴史

### ワークフロー（H-1〜19）

- **H-1 TDD** — テスト駆動開発
- **H-2 ペアプログラミング** — 2 人で同じ画面を書く進め方
- **H-3 バイブコーディングの流儀** — AI と一緒に書く流れ
- **H-4 コードレビュー** — 変更を他人の目で確認する
- **H-5 Scrum / Agile** — 小刻みに進める開発枠組み
- **H-6 Git Flow** — git のブランチ運用モデル
- **H-7 CI/CD** — 自動テスト・自動デプロイ
- **H-8 DevOps** — 開発と運用を一体で回す文化

### 歴史・系譜（H-50〜69）

- **H-50 Bard → Gemini** — Google AI アシスタントの改名史
- **H-51 Preview から正式版への流れ** — プレビュー文化の説明
- **H-52 Copilot から Claude Code までの流れ** — AI コーディング世代
- **H-53 ChatGPT 登場** — 2022-11
- **H-54 GPT-4 リリース** — 2023-03
- **H-55 LLaMA のオープン化** — 2023〜 オープンモデル隆盛
- **H-56 Claude のバージョン史** — Claude 2 → 3 → 4 系
- **H-57 Gemini の命名史** — Bard → Gemini → 1.5／2.0／2.5
- **H-58 Transformer 論文** — 2017 "Attention is All You Need"
- **H-59 AI エージェント元年** — 2024 頃〜エージェントの一般化
- **H-60 Codex → GitHub Copilot の系譜** — 2021 Copilot → 2025 Codex 再始動
- **H-61 Preview 版という文化** — 正式版前の先行提供の慣習
- **H-62 Anthropic 創業の流れ** — OpenAI 分派の背景

## I — MCP（プロトコル／主要サーバー／連携サービス）

### MCP 基礎（I-1〜9）

- **I-1 MCP** — Model Context Protocol。LLM とツールをつなぐ規格
- **I-2 MCP Server** — MCP を提供する側（ツール・データを出す）
- **I-3 MCP Client** — MCP を呼ぶ側（Claude Code、Cursor 等）
- **I-4 MCP Transport** — 通信方式（stdio / SSE / HTTP）
- **I-5 MCP SDK** — MCP 実装用の開発キット

### 公式・リファレンス MCP（I-10〜19）

- **I-10 Filesystem MCP** — ファイル操作
- **I-11 GitHub MCP** — GitHub 連携（公式）
- **I-12 Git MCP** — git 操作
- **I-13 Slack MCP** — Slack 連携

### 開発・自動化系 MCP（I-20〜29）

- **I-20 Playwright MCP** — ブラウザ自動操作
- **I-21 Puppeteer MCP** — Chrome 操作
- **I-22 Chrome DevTools MCP** — Chrome 開発者ツール操作
- **I-23 Serena MCP** — セマンティックなコード編集を LLM に与える MCP
- **I-24 Context7 MCP** — 最新のライブラリドキュメントを取ってくる MCP

### コラボ・業務系 MCP（I-30〜39）

- **I-30 Notion MCP** — Notion 連携

### データ・検索系 MCP（I-40〜49）

- **I-41 SQLite MCP** — SQLite DB 操作

### クラウド・インフラ（I-50〜59）

- **I-50 AWS MCP** — AWS 操作

### 自作・運用（I-80〜89）

- **I-80 自作 MCP のテンプレ** — MCP 自作のスタート雛形
- **I-81 MCP の登録・設定** — 使うための設定手順

## J — 一般 AI・テック語彙

### AI の大概念（J-1〜9）

- **J-1 AGI** — 汎用人工知能。人間レベルで何でもできる AI
- **J-2 強い AI ／ 弱い AI** — 意識や理解を持つか／道具に留まるかの哲学区分
- **J-3 Singularity（技術的特異点／シンギュラリティ）** — AI が人間知を超えるとされる時点
- **J-4 ASI** — 人類を超えた超知能

### 機械学習・深層学習の基礎（J-10〜19）

- **J-10 Machine Learning** — データから学ぶ仕組み全般
- **J-11 Deep Learning** — 層の深いニューラルネットによる機械学習
- **J-12 Neural Network** — 神経細胞を模した計算構造
- **J-13 Transformer** — 現代 LLM の基盤アーキテクチャ
- **J-14 LLM** — 大規模言語モデル
- **J-15 VLM** — Vision Language Model。画像も理解できる言語モデル
- **J-16 Fine-tuning** — 既存モデルに追加学習して特化させる
- **J-17 Attention** — Transformer の核。入力のどこに注目するかを決める仕組み
- **J-18 MoE（Mixture of Experts）** — モデル内の「専門家」を選んで使い分ける設計
- **J-19 量子化** — モデルの重みを低ビット化して小型・高速化する技法

### データ・分析・学習技法・アーキテクチャ（J-20〜29）

- **J-20 Big Data** — 大規模データ活用の総称
- **J-21 LoRA** — Low-Rank Adaptation。少ない追加パラメータでモデルを微調整する手法
- **J-22 パラメータ数の単位（B / T）** — 7B、70B など。B = Billion（10 億）、T = Trillion（1 兆）
- **J-23 拡散モデル（Diffusion Model）** — 画像・動画生成の主流アーキテクチャ。ノイズから徐々に像を立ち上げる仕組み。LLM（言葉の AI）と並ぶ代表的な生成アーキテクチャ

### コンピューティング史・パラダイム（J-30〜39）

- **J-31 第 5 世代コンピューター** — 1980s 日本の国家 AI プロジェクト
- **J-32 ノイマン型** — 現代コンピュータの基本設計
- **J-33 量子コンピューター** — 量子力学で計算するコンピュータ

### 社会実装バズワード（J-40〜49）

- **J-40 IoT** — モノのインターネット
- **J-41 DX** — デジタルトランスフォーメーション
- **J-42 Web3** — ブロックチェーンベースの次世代 Web
- **J-43 SaaS** — クラウド上のソフトウェア提供形式

### 倫理・安全・法律（J-50〜59）

- **J-50 AI 倫理** — 公平性・透明性・責任など
- **J-51 Hallucination** — LLM が事実でない情報を生成する現象
- **J-52 Sycophancy（迎合／シカパシー）** — LLM がユーザーに媚びる／同意しすぎる傾向
- **J-53 著作権法 30 条の 4（日本）** — AI 学習のための著作物利用を原則許容する日本の条項
- **J-54 ISO/IEC 42001** — AI マネジメントシステムの国際規格（AIMS）。AI ガバナンスの枠組みを定める（2023 年発行）
- **J-55 特定商取引法** — 日本の法律。通販・EC 等で事業者表示を義務付ける
- **J-56 GDPR** — EU の一般データ保護規則（2018 施行）。個人情報の扱いを強く規律

### 周辺分野（J-60〜69）

- **J-62 チューリングテスト** — 機械が人間と区別できないかの判定

### ハードウェア・半導体・記憶装置（J-70〜89）

- **J-70 VRAM** — GPU 内のメモリ。LLM のサイズに効く
- **J-71 RAM（メモリ）** — 一般メモリ
- **J-72 H100** — NVIDIA の AI 学習・推論用フラッグシップ GPU
- **J-73 Blackwell** — NVIDIA 次世代 GPU アーキテクチャ（H100 の後継世代）
- **J-74 RTX シリーズ** — NVIDIA の消費者向け／クリエイター向け GPU
- **J-75 Tensor コア** — NVIDIA GPU 内の AI 計算専用ユニット
- **J-76 CPU** — 中央演算装置。汎用計算の要
- **J-77 GPU（概念）** — グラフィックス／並列計算ユニット。AI の実行を担う
- **J-78 HDD** — 磁気ディスク式の記憶装置
- **J-79 SSD** — フラッシュメモリ式の記憶装置（高速）
- **J-80 SATA** — ストレージ接続規格の一種（HDD／SSD 向け）
- **J-81 M.2** — 小型ストレージのフォームファクタ（NVMe SSD で多用）

### UI・OS 基盤（J-90〜99）

- **J-90 GUI** — Graphical User Interface。絵とクリックで操作する UI
- **J-91 CLI** — Command Line Interface。文字入力で操作する UI
- **J-92 Linux** — OSS の Unix 系 OS。サーバー・開発環境の標準
- **J-93 Ubuntu** — Linux ディストリビューションの代表例

### AI コミュニティ・文化（J-100〜109）

- **J-100 驚き屋** — AI 情報を過剰に煽るクリエイター類型（YouTube サムネ・SNS 煽り）

## 要確認（2026-04-24 調査結果）

- **Claude Mythos（D-14）** — ✅ 正式名称は **Claude Mythos Preview**（Anthropic 公式）。限定公開プログラム "Project Glasswing" 経由のみ、一般提供なし。エントリ化する場合は「限定公開の実験的モデル」として扱う
- **Amical（D-70）** — ✅ 著者確認済で実在。URL は執筆時に一次情報を当てて補足する。Whisper（D-71）は別物として併設
- **Claude Cowork（B-19）** — ✅ 正式名 "Claude Cowork"（Anthropic 2026-01 末リサーチプレビュー、Enterprise プランに含まれる）
- **Supercell（F-85）** — ⚠️ 正式名は **"SuperClaude Framework"**（コミュニティ OSS、Anthropic 非公式）。"Supercell" は聞き違い。エントリ名を既に修正済
- **Cursor の head F モデル** — ⚠️ 該当名称を公式で確認できず。Cursor の独自モデルは **cursor-tab-3（Tab 補完）** と **Composer（2025-10 発表）** のみ。D-35 のまま Composer を主軸に扱うのが無難
- **料金プラン（B-50〜52）** — ✅ 2026-04-24 時点数値を取得済み（B-50 に反映）。公開直前に再確認推奨

調査実施：サブエージェント（document-specialist）による WebSearch + WebFetch、2026-04-24。

## 構成・配置の検討事項

### 論文エントリの扱い（Transformer 論文 "Attention is All You Need" など）

- 現状は H-58 Transformer 論文（歴史サブ）に配置
- 著者メモ：人物系（C）に入れる選択肢もある — 論文＝著者の業績という見方
- 案 A：H に残す（歴史イベントとして、発表日が明確）
- 案 B：C-100 番台に「論文」サブを新設（Attention is All You Need、GPT-3、AlphaFold などを束ねる）
- 案 C：H に残しつつ、論文著者（例：Ashish Vaswani 等）を C 人物に足す
- 決め手待ち：他の論文候補（GPT-3、AlphaFold、Chinchilla など）を先にリストアップしてから判断

### タイムラインの切り方（H 系全般）

- H-50 系譜は「誰が・いつ・何を出したか」を時系列で示す趣旨
- 切り方の候補：
  - (a) **主要イベント直列**：ChatGPT 登場 → GPT-4 → Claude 3 → 4 系 → Gemini 2.5 …
  - (b) **系譜別**：GPT 系／Claude 系／Gemini 系のそれぞれで独立したタイムライン
  - (c) **性能基準**：各時点の「最高性能モデル」を辿る
  - (d) **ベンチマーク更新**：SWE-Bench／MMLU などの最高スコアがどう更新されてきたか
- 決め手待ち：主要 2〜3 パターンをラフで描いてから決める

- **1 始まりでよいか**：現在は letter-{1始まりの連番}。OK なら確定
- **飛ばし方（欠番幅）の目安**：現在は 10 番刻みでサブ分類を切り、各サブ内は 1 始まり連番。採用ルールを id_scheme.md に明記するか
- **番号の上限**：実質的に letter 毎に 100〜200 番くらいまで到達しそうな勢い。上限管理が要るか（不要なら無制限で）
- **欠番の扱い**：詰め直さないルール（id_scheme.md 既定）を徹底する。今回のように renumber する場合は「草案期のみ」など明示した方が安全

> 現時点で最も動いたのは D の renumber（D-30〜 を全て +10 シフト）。今後は renumber を避けたいので、今回で基礎構造を固定したい。

## 前回からの変更点（作業メモ）

### 新規追加

- B-61 ACE-Step 1.5（「A step」の正体として確定）
- D-14 Claude Mitos モデル（「アクロミトス」訂正）
- D-30 Grok 系（xAI 系サブを新設）
- D-35 Cursor Composer（モデルとして扱う、G-37 から移動）
- F-44 pnpm

### renumber（D 系を +10 シフト）

- D-30〜35 オープンモデル → **D-40〜45**
- D-40〜48 画像・動画 → **D-50〜58**
- D-50 AlphaGo → **D-60**
- D-60 Amical → **D-70**

### 移動

- **Cursor Composer**：G-37（機能）→ D-35（モデル）。G-37 は欠番として残す

### リポジトリ

- 管理場所：<https://github.com/Taguchi-1989/VibeCodingDictionary>

## カウント

| letter | 件数 |
| --- | --- |
| A | 11 |
| B | 40 |
| C | 29 |
| D | 36 |
| E | 19 |
| F | 78 |
| G | 32 |
| H | 21 |
| I | 19 |
| J | 50 |
| **合計** | **335** |

---

## M 差分（2026-08-10）— 収録語の抜け監査による追加 34 件

*[docs/design_improvement_proposal_2026-08.md](../docs/design_improvement_proposal_2026-08.md) §4「収録語の抜け監査」で洗い出した候補を、空き番号に割り当てて台帳へ登録しました。仮 ID から変更した箇所は末尾の「ID 調整メモ」に理由を書いています。*

### ☆☆☆ 明らかな抜け（14 件＋復活 1 件）

- **G-49 AI エージェント** — 目標を渡すと自分で手順を決めて動く AI システムの総称
- **F-213 API** — ソフト同士が決まった形でやり取りするための窓口
- **F-214 API キー** — API を使う人を識別する秘密の文字列。漏えい対策が要る
- **F-45 デプロイ** — 作ったものを本番環境に置いて公開する作業
- **F-46 デバッグ** — 不具合の原因を特定して直していく作業
- **F-18 フレームワーク／ライブラリ** — 土台として使う枠組みと、部品として呼ぶ道具箱の違い
- **F-47 フロントエンド／バックエンド** — 画面側と裏側という開発の役割分担
- **J-34 マルチモーダル** — 文字・画像・音声・動画をまとめて扱える性質
- **J-35 スケーリング則** — 計算量・データ量・パラメータ数を増やすほど性能が伸びる経験則
- **G-27 プロンプトインジェクション** — 外部の文章に仕込んだ指示で AI を乗っ取る攻撃
- **E-28 ARC-AGI** — 見たことのない規則をその場で推論できるかを測るベンチマーク
- **B-34 NotebookLM** — 手元の資料だけを根拠に答えさせる Google のノートツール
- **B-35 Gemini CLI** — ターミナルで動く Google 製のオープンソース AI エージェント
- **D-59 Midjourney** — 作風の強さで知られる画像生成サービス
- **F-43 テスト**（既存）— archived だった既存エントリを復活。新規採番なし

### ☆☆ 検討枠（20 件）

- **B-36 Lovable** — 会話だけでアプリ一式を作るバイブコーディング系サービス
- **B-37 Replit** — ブラウザだけで書いて動かして公開できる開発環境
- **B-38 Manus** — 汎用タスクを任せられる自律型 AI エージェント
- **B-39 Google AI Studio** — Gemini と API キーを無料で試せる入口
- **B-42 Discord** — AI コミュニティの実際の集合場所になっているチャットサービス
- **B-43 n8n・Dify** — 非エンジニアでも組める AI ワークフロー自動化ツール
- **C-16 DeepSeek** — 重みを公開する中国・杭州の AI 開発企業（モデルは D-46 / D-47）
- **C-17 Sakana AI** — 自然界の知能に着想を得た日本発の AI スタートアップ
- **D-61 AlphaFold** — タンパク質の立体構造を予測しノーベル賞につながったモデル
- **G-24 Temperature** — 出力のばらつきを決める設定値
- **G-25 AI のメモリ機能** — 過去の会話から好みや前提を覚えておく仕組み
- **G-26 Computer Use** — 画面を見てマウスとキーボードを操作させる使い方
- **J-36 蒸留** — 大きいモデルの出力を教師にして小さいモデルを鍛える手法
- **J-57 RLHF・アラインメント** — 人間の評価で学習させ、AI の振る舞いを目的に合わせる取り組み
- **J-115 NPU・AI PC** — PC 内で AI 処理を担う専用チップと、それを積んだ PC
- **J-116 TPU** — Google が自社開発した AI 計算専用チップ
- **J-117 データセンターと電力** — AI の計算を支える施設と、その電力消費の議論
- **J-5 世界モデル** — 世界の動きを内部でシミュレーションして予測する AI
- **J-38 ムーアの法則** — 半導体の集積度が一定周期で倍増するという経験則
- **H-64 DeepSeek ショック** — 2025-01 に株式市場まで動かした低コスト AI の衝撃

### ID 調整メモ（提案書の仮 ID からの変更）

- **F-43 テスト**：提案書は「欠番」と書いていましたが、実際には v2 テンプレで書き上げ済みのエントリが `status: archived` で凍結されていました。新規採番せず、既存ファイルを復活させます
- **E-5 → E-28 ARC-AGI**：E-1〜19 は「コーディング・エンジニアリング」棚。ARC-AGI は推論系のため「E-20〜29 推論・知識」の空き番号へ
- **J-34/J-35 → 据え置き、J-72〜74 → J-115〜117**：提案書の仮 ID のうち J-72〜74 は H100 / Blackwell / RTX シリーズで既に使用済みでした。ハードウェア棚（J-70 台）に空きがないため、末尾の空き番号へ回しています
- **G-27 プロンプトインジェクション**：当初は G-37（Cursor Composer を D-35 へ移した際の欠番）に置きましたが、著者判断で **G-27 へ移動**しました。G-37 は引き続き欠番のまま残します。今回追加した G-24 Temperature / G-25 メモリ機能 / G-26 Computer Use と同じ並びに入ります
