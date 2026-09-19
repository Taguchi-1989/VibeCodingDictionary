# 時変ファクト watchlist（自動生成）

*基準日 2026-09-19 — `python3 scripts/update_volatile_facts.py` が再生成します。定義を変えるときは [volatile_facts.yaml](volatile_facts.yaml) を編集してください。この .md は手で編集しないでください。*

「最新の Claude は何か」「ChatGPT の月額はいくらか」のような事実は、1 つ変わるだけで複数のエントリが同時に古くなります。エントリ側から鮮度を見る [freshness_queue.md](freshness_queue.md) と対で、こちらは**事実側から影響範囲を引く**ための台帳です。

---

## 1. 一覧

| 事実ID | 事実 | 種別 | 最終確認 | 期限 | 影響エントリ |
| :-- | :-- | :-- | :-- | :-- | --: |
| `F-model-anthropic` | Anthropic の最新モデル世代 | モデル世代 | 2026-09-19（0 日前） | 90 日 | 8 |
| `F-model-openai` | OpenAI の最新モデル世代（GPT 系） | モデル世代 | 2026-09-19（0 日前） | 90 日 | 22 |
| `F-model-openai-reasoning` | OpenAI の推論モデル系列（o シリーズ） | モデル世代 | 2026-09-19（0 日前） | 90 日 | 10 |
| `F-model-google` | Google の最新モデル世代（Gemini 系） | モデル世代 | 2026-09-19（0 日前） | 90 日 | 11 |
| `F-model-meta` | Meta のオープンウェイトモデル（Llama 系） | モデル世代 | ⏰ **未確認** | 180 日 | 6 |
| `F-spec-context-length` | 主要モデルのコンテキスト長 | 仕様 | ⏰ **未確認** | 90 日 | 6 |
| `F-price-chatgpt` | ChatGPT の料金プラン | 料金 | ⏰ **未確認** | 90 日 | 2 |
| `F-price-claude` | Claude の料金プラン | 料金 | ⏰ **未確認** | 90 日 | 3 |
| `F-price-gemini` | Gemini の料金プラン・無料枠 | 料金 | ⏰ **未確認** | 90 日 | 2 |
| `F-price-dev-tools` | 開発ツールの料金（Cursor / Copilot / ホスティング等） | 料金 | ⏰ **未確認** | 90 日 | 24 |
| `F-bench-swebench` | SWE-Bench 系のスコア水準 | ベンチマーク | ⏰ **未確認** | 90 日 | 15 |
| `F-bench-leaderboard` | ベンチマークのスコア・順位（数値を書いている箇所） | ベンチマーク | ⏰ **未確認** | 90 日 | 10 |
| `F-spec-mcp` | MCP の仕様と公式サーバーの顔ぶれ | 仕様 | ⏰ **未確認** | 90 日 | 19 |
| `F-availability-preview` | ベータ・プレビュー表記 | 提供状況 | ⏰ **未確認** | 90 日 | 16 |
| `F-availability-deprecated` | 提供終了・非推奨の表記 | 提供状況 | ⏰ **未確認** | 180 日 | 11 |

⏰ = 再確認の期限を過ぎているもの（**11 / 15 件**）。

---

## 2. 事実ごとの影響範囲

### `F-model-anthropic` Anthropic の最新モデル世代

- **本書の記述**: D-13「Claude 4.5 系」を現行の主力、D-14「Claude Mythos Preview」を先行版として扱う
- **最後に確認した実際の値**: Claude 5 世代が現行。Opus 5（1M 文脈）／Sonnet 5／Fable 5.1／Mythos 5.1。Opus 4.8 は 2026-05-28 公開。本書が現行とする 4.5〜4.7 は既に過去世代
- **最終確認**: 2026-09-19（0 日前）（期限 90 日）
- **確認先**: Anthropic 公式ドキュメント（モデル一覧） — https://docs.anthropic.com/en/docs/about-claude/models/overview
- **注意**: 世代が増えたら D 章に新エントリが要る。旧世代の deprecated 化も同時に確認する
- **影響エントリ**: 8 件

  D-10 Claude 3 系、D-11 Claude 3.5 系、D-12 Claude 4 系、D-13 Claude 4.5 系、D-14 Claude Mythos Preview、E-26 Humanity's Last Exam、G-5 Context Window、J-72 H100

### `F-model-openai` OpenAI の最新モデル世代（GPT 系）

- **本書の記述**: D-20「GPT-5 系」を現行、D-21「GPT-4 系」以前を過去世代として扱う
- **最後に確認した実際の値**: GPT-6 Astra がフラッグシップ。GPT-5.6 系は Sol／Terra／Luna の 3 構成、ほかに GPT-5.3-Codex・GPT-5.4／5.5 系。本書が現行とする GPT-5 系は過去世代
- **最終確認**: 2026-09-19（0 日前）（期限 90 日）
- **確認先**: OpenAI 公式ドキュメント（Models） — https://developers.openai.com/api/docs/models
- **注意**: 本書では 26 件が GPT の世代名に触れている。世代交代時の影響が最も大きい
- **影響エントリ**: 22 件

  B-3 ChatGPT、B-26 Azure OpenAI、B-51 ChatGPT の料金プラン、C-1 OpenAI、C-50 Sam Altman、C-82 まさお、D-20 GPT-5 系、D-21 GPT-4 系、D-22 o1 系、D-23 o3 系、D-24 GPT-3 系、D-25 GPT-1 / GPT-2 系、D-26 gpt-oss、D-46 DeepSeek V3、E-20 MMLU、E-26 Humanity's Last Exam、E-32 GAIA、E-34 OSWorld、G-5 Context Window、J-25 Tokenizer・BPE、J-52 Sycophancy、J-72 H100

### `F-model-openai-reasoning` OpenAI の推論モデル系列（o シリーズ）

- **本書の記述**: D-22「o1 系」・D-23「o3 系」を収録。o3 系が最新として書かれている
- **最後に確認した実際の値**: o1-preview は 2025-07-28、o1-mini は 2025-10-27 に API から削除済み。o3 は 2026-08-26 に ChatGPT から引退、API 側も 2026-12-11 削除予定。推論は GPT-5 以降の本流モデルに統合された
- **最終確認**: 2026-09-19（0 日前）（期限 90 日）
- **確認先**: OpenAI 公式ドキュメント（Models） — https://developers.openai.com/api/docs/deprecations
- **注意**: 通常モデルへの推論機能統合が進むと、系列そのものの位置づけが変わる
- **影響エントリ**: 10 件

  B-26 Azure OpenAI、D-20 GPT-5 系、D-21 GPT-4 系、D-22 o1 系、D-23 o3 系、D-47 DeepSeek R1、E-22 GPQA、E-25 AIME、E-26 Humanity's Last Exam、G-14 Thinking モデル

### `F-model-google` Google の最新モデル世代（Gemini 系）

- **本書の記述**: D-4「Gemini 3.1 系」を現行、D-1〜D-3 を過去世代として扱う
- **最後に確認した実際の値**: Gemini 3.8 Flash まで到達。3.5 Flash／3.5 Flash-Lite／3.6 Flash／3.7 Flash が GA。本書の最新収録は D-4 Gemini 3.1 系で、3.5 以降が未収録
- **最終確認**: 2026-09-19（0 日前）（期限 90 日）
- **確認先**: Google AI 公式ドキュメント（Gemini models） — https://ai.google.dev/gemini-api/docs/models
- **注意**: 旧 3 桁 ID の残骸（201 番）も Gemini 2.5 を扱っているので併せて確認する
- **影響エントリ**: 11 件

  B-1 Gemini、B-35 Gemini CLI、B-52 Gemini の料金プラン、D-1 Gemini 2 系、D-2 Gemini 2.5 系、D-3 Gemini 3 系、D-4 Gemini 3.1 系、D-55 Nano Banana、E-26 Humanity's Last Exam、E-51 LMSYS Arena、G-5 Context Window

### `F-model-meta` Meta のオープンウェイトモデル（Llama 系）

- **本書の記述**: D-40「Llama 系」で Llama 1〜4 の系譜を扱う
- **最後に確認した実際の値**: _未確認_
- **最終確認**: **未確認**（期限 180 日）
- **確認先**: Meta Llama 公式サイト — https://www.llama.com/
- **注意**: ライセンス条項の変更もここで拾う（商用利用の条件は本書の説明に効く）
- **影響エントリ**: 6 件

  B-40 Reddit、D-40 Llama 系、F-86 ollama、J-19 量子化、J-22 パラメータ数の単位、J-86 GQA

### `F-spec-context-length` 主要モデルのコンテキスト長

- **本書の記述**: 「◯万トークン」「◯K トークン」の具体数値が複数エントリに入っている
- **最後に確認した実際の値**: _未確認_
- **最終確認**: **未確認**（期限 90 日）
- **確認先**: 各社のモデル一覧ページ（URL 未設定）
- **注意**: 数値そのものが入っているので、世代交代のたびに実数がずれる
- **影響エントリ**: 6 件

  D-2 Gemini 2.5 系、D-13 Claude 4.5 系、G-5 Context Window、J-25 Tokenizer・BPE、J-27 RoPE、J-85 スループットとレイテンシ

### `F-price-chatgpt` ChatGPT の料金プラン

- **本書の記述**: B-51「ChatGPT 料金」が本体。金額そのものは B-51 に集約されている
- **最後に確認した実際の値**: _未確認_
- **最終確認**: **未確認**（期限 90 日）
- **確認先**: OpenAI 公式料金ページ — https://openai.com/chatgpt/pricing/
- **注意**: プラン名の改称（Plus / Pro / Team 等）も記述に効く
- **影響エントリ**: 2 件

  B-51 ChatGPT の料金プラン、G-25 AI のメモリ機能

### `F-price-claude` Claude の料金プラン

- **本書の記述**: B-50「Claude 料金」が本体。B-7 Claude Code は「時変情報のため本文への記載は最小限」として金額を書かない方針
- **最後に確認した実際の値**: _未確認_
- **最終確認**: **未確認**（期限 90 日）
- **確認先**: Anthropic 公式料金ページ — https://www.anthropic.com/pricing
- **注意**: Claude Code の利用上限は変動が激しい。B-50 に集約し、他エントリへ金額を散らさない方針を保つ
- **影響エントリ**: 3 件

  B-35 Gemini CLI、B-50 Claude の料金プラン、G-25 AI のメモリ機能

### `F-price-gemini` Gemini の料金プラン・無料枠

- **本書の記述**: B-52「Gemini 料金」が本体。B-35 Gemini CLI の無料枠記述が連動する
- **最後に確認した実際の値**: _未確認_
- **最終確認**: **未確認**（期限 90 日）
- **確認先**: Google AI 公式料金ページ — https://ai.google.dev/pricing
- **注意**: 無料枠の上限とフォールバック先はエントリ本文でも「分かりにくい」と書いている箇所
- **影響エントリ**: 2 件

  B-35 Gemini CLI、G-25 AI のメモリ機能

### `F-price-dev-tools` 開発ツールの料金（Cursor / Copilot / ホスティング等）

- **本書の記述**: B 章の各サービスエントリに月額・無料枠の記述が散在している
- **最後に確認した実際の値**: _未確認_
- **最終確認**: **未確認**（期限 90 日）
- **確認先**: 各サービスの公式料金ページ（URL 未設定）
- **注意**: 件数が多いので、まず金額が具体的に書かれているエントリだけ拾うと速い
- **影響エントリ**: 24 件

  B-4 Cursor、B-5 GitHub Copilot、B-7 Claude Code、B-11 Bolt.new、B-14 Genspark、B-16 Microsoft 365 Copilot、B-21 Netlify、B-22 Cloudflare、B-28 Render、B-33 Canva、B-35 Gemini CLI、B-37 Replit、B-39 Google AI Studio、B-51 ChatGPT の料金プラン、B-60 Suno、C-13 Groq、C-80 AI大学、D-57 Flow、D-59 Midjourney、F-83 PowerShell、F-170 EC2、G-19 Prompt Caching、G-25 AI のメモリ機能、J-43 SaaS

### `F-bench-swebench` SWE-Bench 系のスコア水準

- **本書の記述**: E-1 / E-2 でベンチマークの位置づけとスコア水準に触れる
- **最後に確認した実際の値**: _未確認_
- **最終確認**: **未確認**（期限 90 日）
- **確認先**: SWE-bench 公式リーダーボード — https://www.swebench.com/
- **注意**: 上位スコアはモデル更新のたびに動く。「◯% 程度」と幅で書いてあれば直す頻度は下がる
- **影響エントリ**: 15 件

  B-10 Devin、D-4 Gemini 3.1 系、E-1 SWE-Bench、E-2 SWE-Bench Verified、E-3 Terminal-Bench、E-4 HumanEval、E-20 MMLU、E-22 GPQA、E-26 Humanity's Last Exam、E-30 TAU-Bench、E-50 Chatbot Arena、E-51 LMSYS Arena、G-46 ナーフ、G-50 Evals、J-114 グッドハートの法則

### `F-bench-leaderboard` ベンチマークのスコア・順位（数値を書いている箇所）

- **本書の記述**: E 章を中心に、具体的なパーセンテージが本文に入っている
- **最後に確認した実際の値**: _未確認_
- **最終確認**: **未確認**（期限 90 日）
- **確認先**: 各ベンチマークの公式リーダーボード — https://lmarena.ai/
- **注意**: 数値を残すか「水準」の表現に逃がすかは編集判断。刊行物としては幅表現が安全
- **影響エントリ**: 10 件

  E-1 SWE-Bench、E-2 SWE-Bench Verified、E-4 HumanEval、E-20 MMLU、E-21 MMLU-Pro、E-22 GPQA、E-24 MATH、E-26 Humanity's Last Exam、E-32 GAIA、E-34 OSWorld

### `F-spec-mcp` MCP の仕様と公式サーバーの顔ぶれ

- **本書の記述**: I 章全体（19 件）が MCP の仕様・公式/コミュニティ別・配布場所を前提にしている
- **最後に確認した実際の値**: _未確認_
- **最終確認**: **未確認**（期限 90 日）
- **確認先**: Model Context Protocol 公式サイト — https://modelcontextprotocol.io/
- **注意**: 「公式サーバー」の一覧は入れ替わる。I-10 以降の個別サーバーの現存確認も要る
- **影響エントリ**: 19 件

  I-1 MCP、I-2 MCP Server、I-3 MCP Client、I-4 MCP Transport、I-5 MCP SDK、I-10 Filesystem MCP、I-11 GitHub MCP、I-12 Git MCP、I-13 Slack MCP、I-20 Playwright MCP、I-21 Puppeteer MCP、I-22 Chrome DevTools MCP、I-23 Serena MCP、I-24 Context7 MCP、I-30 Notion MCP、I-41 SQLite MCP、I-50 AWS MCP、I-80 自作 MCP のテンプレ、I-81 MCP の登録・設定

### `F-availability-preview` ベータ・プレビュー表記

- **本書の記述**: 16 件が「ベータ」「プレビュー」として紹介している
- **最後に確認した実際の値**: _未確認_
- **最終確認**: **未確認**（期限 90 日）
- **確認先**: 各サービスの公式アナウンス（URL 未設定）
- **注意**: 一般提供（GA）に移ると記述が古くなる。version_status の preview も併せて直す
- **影響エントリ**: 16 件

  B-9 v0、B-11 Bolt.new、B-19 Claude Cowork、B-20 Vercel、B-28 Render、B-36 Lovable、D-14 Claude Mythos Preview、D-52 Sora、F-6 Markdown、F-35 Markdown Preview Enhanced、F-38 Markdown All in One、F-84 Ghostty、G-36 Artifact、H-51 Preview から正式版への流れ、H-52 Copilot から Claude Code までの流れ、H-61 Preview 版という文化

### `F-availability-deprecated` 提供終了・非推奨の表記

- **本書の記述**: 11 件が deprecated・提供終了・後継ありとして書かれている
- **最後に確認した実際の値**: _未確認_
- **最終確認**: **未確認**（期限 180 日）
- **確認先**: 各サービスの公式アナウンス（URL 未設定）
- **注意**: 完全終了すると「まだ使える」前提の記述が崩れる。version_status: deprecated と揃える
- **影響エントリ**: 11 件

  D-10 Claude 3 系、D-11 Claude 3.5 系、D-24 GPT-3 系、D-25 GPT-1 / GPT-2 系、F-104 .webp、F-153 Creative Commons、H-51 Preview から正式版への流れ、I-4 MCP Transport、J-93 Ubuntu、J-142 文書化した情報と力量、J-149 第三者認証と自己宣言

---

## 使い方

1. §1 で ⏰ が付いている事実を選ぶ
2. 確認先の一次情報を見て、**本書の記述が今も成り立つか**を判断する
3. `volatile_facts.yaml` の `current_value` と `last_checked` を更新する
4. 記述が変わっていたら、§2 の影響エントリを直す。同じ事実に依存しているので、まとめて直すのが速いです
5. 直したエントリ（変更が無かったものも含む）は `last_audited` を更新する。`python3 scripts/touch_last_audited.py --fact <事実ID>` で一括できます
6. 監査した範囲を [freshness_audit_log.md](freshness_audit_log.md) に 1 行追記する

事実を足したいときは `volatile_facts.yaml` に 1 ブロック書いてください。影響エントリの収集は `pattern`（正規表現）で自動化されるので、手で一覧を書く必要はありません。
