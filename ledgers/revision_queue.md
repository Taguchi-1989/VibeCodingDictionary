# 要直しキュー（revision queue）

*自動生成: 2026-08-24 03:44 / `scripts/update_review_queue.py`*

1 画面で「次やるべき・見直すべき・適合済み」が見えるダッシュボード。`scripts/validate_entry.py` のチェックを全件で走らせた結果を集計して再生成しています。手で編集しないでください。

## status 内訳

- **drafting**: 1 件
- **needs_review**: 159 件
- **ready**: 266 件
- **archived**: 7 件
- **合計**: 433 件

- **自己学習シェルフ（reader_level 6・刊行外）**: 35 件（誌面には出ません。`scripts/preview_gen.py` が除外）

## ☆ 違反あり（最優先で直す）（0 件）

_なし_

## ⚠️ 警告あり（軽微超過 / 著者か entry-writer で手当て）（0 件）

_なし_

## ✍️ 書きかけ（drafting・全パス済み・自動昇格漏れ）（0 件）

_なし（drafting で全パスしたものは自動で needs_review に上がります）_

## 📝 著者レビュー待ち（needs_review・全パス）（148 件）

| ID | title | status | 概要 |
| :-- | :-- | :-- | :-- |
| B-34 | NotebookLM | needs_review | — |
| B-35 | Gemini CLI | needs_review | — |
| B-36 | Lovable | needs_review | — |
| B-37 | Replit | needs_review | — |
| B-38 | Manus | needs_review | — |
| B-39 | Google AI Studio | needs_review | — |
| B-42 | Discord | needs_review | — |
| B-43 | n8n・Dify | needs_review | — |
| C-10 | Moonshot AI | needs_review | — |
| C-11 | Z.ai | needs_review | — |
| C-15 | Intel | needs_review | — |
| C-16 | DeepSeek | needs_review | — |
| C-17 | Sakana AI | needs_review | — |
| C-50 | Sam Altman | needs_review | — |
| C-6 | Mistral AI | needs_review | — |
| C-83 | AI時代の羅針盤 | needs_review | — |
| D-1 | Gemini 2 系 | needs_review | — |
| D-10 | Claude 3 系 | needs_review | — |
| D-13 | Claude 4.5 系 | needs_review | — |
| D-14 | Claude Mythos Preview | needs_review | — |
| D-2 | Gemini 2.5 系 | needs_review | — |
| D-20 | GPT-5 系 | needs_review | — |
| D-21 | GPT-4 系 | needs_review | — |
| D-22 | o1 系 | needs_review | — |
| D-23 | o3 系 | needs_review | — |
| D-24 | GPT-3 系 | needs_review | — |
| D-3 | Gemini 3 系 | needs_review | — |
| D-4 | Gemini 3.1 系 | needs_review | — |
| D-59 | Midjourney | needs_review | — |
| D-61 | AlphaFold | needs_review | — |
| D-70 | Amical | needs_review | — |
| E-28 | ARC-AGI | needs_review | — |
| E-31 | WebArena | needs_review | — |
| E-32 | GAIA | needs_review | — |
| E-33 | AgentBench | needs_review | — |
| E-34 | OSWorld | needs_review | — |
| E-51 | LMSYS Arena | needs_review | — |
| F-100 | 拡張子早見表 | needs_review | — |
| F-101 | .ico | needs_review | — |
| F-102 | .mp4 | needs_review | — |
| F-103 | .mp3 | needs_review | — |
| F-104 | .webp | needs_review | — |
| F-110 | Lighthouse | needs_review | — |
| F-111 | a11y | needs_review | — |
| F-120 | PostgreSQL | needs_review | — |
| F-121 | SQLite | needs_review | — |
| F-122 | Prisma | needs_review | — |
| F-123 | ORM | needs_review | — |
| F-130 | OAuth | needs_review | — |
| F-140 | Mermaid | needs_review | — |
| F-141 | PlantUML | needs_review | — |
| F-150 | MIT ライセンス | needs_review | — |
| F-151 | Apache 2.0 | needs_review | — |
| F-152 | GPL | needs_review | — |
| F-153 | Creative Commons | needs_review | — |
| F-154 | OSS | needs_review | — |
| F-160 | DOM | needs_review | — |
| F-161 | SSR | needs_review | — |
| F-162 | SSG | needs_review | — |
| F-170 | EC2 | needs_review | — |
| F-171 | S3 | needs_review | — |
| F-172 | IAM | needs_review | — |
| F-18 | フレームワーク／ライブラリ | needs_review | — |
| F-180 | OpenGL | needs_review | — |
| F-181 | WebGL | needs_review | — |
| F-190 | サブルーチン | needs_review | — |
| F-200 | Rust | needs_review | — |
| F-34 | VS Code 拡張機能 | needs_review | — |
| F-47 | フロントエンド／バックエンド | needs_review | — |
| F-57 | リポジトリ | needs_review | — |
| F-80 | Node.js | needs_review | — |
| F-84 | Ghostty | needs_review | — |
| F-85 | SuperClaude Framework | needs_review | — |
| F-86 | ollama | needs_review | — |
| F-87 | sudo | needs_review | — |
| F-90 | Docker | needs_review | — |
| F-91 | .env | needs_review | — |
| G-12 | Agent Design | needs_review | — |
| G-24 | Temperature | needs_review | — |
| G-25 | AI のメモリ機能 | needs_review | — |
| G-26 | Computer Use | needs_review | — |
| G-27 | プロンプトインジェクション | needs_review | — |
| G-4 | System Prompt | needs_review | — |
| H-2 | ペアプログラミング | needs_review | — |
| H-3 | バイブコーディングの流儀 | needs_review | — |
| H-4 | コードレビュー | needs_review | — |
| H-50 | Bard → Gemini | needs_review | — |
| H-51 | Preview から正式版への流れ | needs_review | — |
| H-52 | Copilot から Claude Code までの流れ | needs_review | — |
| H-57 | Gemini の命名史 | needs_review | — |
| H-59 | AI エージェント元年 | needs_review | — |
| H-60 | Codex → GitHub Copilot の系譜 | needs_review | — |
| H-61 | Preview 版という文化 | needs_review | — |
| H-62 | Anthropic 創業の流れ | needs_review | — |
| H-63 | Vibe Coding 命名 | needs_review | — |
| H-64 | DeepSeek ショック | needs_review | — |
| I-80 | 自作 MCP のテンプレ | needs_review | — |
| I-81 | MCP の登録・設定 | needs_review | — |
| J-101 | 半導体製造プロセス | needs_review | — |
| J-102 | チップレットと3D積層 | needs_review | — |
| J-103 | ループエンジニアリング | needs_review | — |
| J-104 | ReAct | needs_review | — |
| J-105 | コンテキスト管理 | needs_review | — |
| J-106 | ハーネスエンジニアリング | needs_review | — |
| J-107 | 自律ループとガードレール | needs_review | — |
| J-108 | Ralph Loop | needs_review | — |
| J-109 | モデルルーティング | needs_review | — |
| J-110 | 不確実性デファーラル | needs_review | — |
| J-111 | 人間の認知ボトルネック | needs_review | — |
| J-112 | 認知コストの定量化 | needs_review | — |
| J-113 | 生成UIとagent-native設計 | needs_review | — |
| J-114 | グッドハートの法則 | needs_review | — |
| J-115 | NPU・AI PC | needs_review | — |
| J-116 | TPU | needs_review | — |
| J-117 | データセンターと電力 | needs_review | — |
| J-22 | パラメータ数の単位 | needs_review | — |
| J-24 | Encoder-Decoder | needs_review | — |
| J-25 | Tokenizer・BPE | needs_review | — |
| J-26 | 潜在空間 | needs_review | — |
| J-27 | RoPE | needs_review | — |
| J-28 | MLA | needs_review | — |
| J-29 | KV Cache | needs_review | — |
| J-30 | Flash Attention | needs_review | — |
| J-32 | ノイマン型 | needs_review | — |
| J-34 | マルチモーダル | needs_review | — |
| J-35 | スケーリング則 | needs_review | — |
| J-36 | 蒸留 | needs_review | — |
| J-38 | ムーアの法則 | needs_review | — |
| J-43 | SaaS | needs_review | — |
| J-5 | 世界モデル | needs_review | — |
| J-50 | AI 倫理 | needs_review | — |
| J-55 | 個人情報保護法 | needs_review | — |
| J-57 | RLHF・アラインメント | needs_review | — |
| J-62 | チューリングテスト | needs_review | — |
| J-82 | 投機的デコード | needs_review | — |
| J-83 | vLLM | needs_review | — |
| J-84 | バッチ推論 | needs_review | — |
| J-85 | スループットとレイテンシ | needs_review | — |
| J-86 | GQA | needs_review | — |
| J-87 | QK-Norm | needs_review | — |
| J-88 | MTP | needs_review | — |
| J-89 | MoE ルーティング | needs_review | — |
| J-94 | 並列化戦略 | needs_review | — |
| J-95 | 半導体サプライチェーン | needs_review | — |
| J-96 | 半導体製造装置 | needs_review | — |
| J-97 | 電子材料 | needs_review | — |
| J-98 | 重要鉱物の地政学 | needs_review | — |
| J-99 | CoWoS | needs_review | — |

## ✅ 完成（ready・全パス）（266 件）

| ID | title | status | 概要 |
| :-- | :-- | :-- | :-- |
| B-1 | Gemini | ready | — |
| B-10 | Devin | ready | — |
| B-11 | Bolt.new | ready | — |
| B-12 | Perplexity | ready | — |
| B-13 | ElevenLabs | ready | — |
| B-14 | Genspark | ready | — |
| B-15 | Microsoft Copilot | ready | — |
| B-16 | Microsoft 365 Copilot | ready | — |
| B-17 | Edge Copilot | ready | — |
| B-18 | Aqua Voice | ready | — |
| B-19 | Claude Cowork | ready | — |
| B-2 | Claude | ready | — |
| B-20 | Vercel | ready | — |
| B-21 | Netlify | ready | — |
| B-22 | Cloudflare | ready | — |
| B-23 | AWS | ready | — |
| B-24 | Google Cloud | ready | — |
| B-25 | Azure | ready | — |
| B-26 | Azure OpenAI | ready | — |
| B-27 | Vertex AI | ready | — |
| B-28 | Render | ready | — |
| B-29 | Supabase | ready | — |
| B-3 | ChatGPT | ready | — |
| B-30 | Amazon Bedrock | ready | — |
| B-31 | Excalidraw | ready | — |
| B-32 | Figma | ready | — |
| B-33 | Canva | ready | — |
| B-4 | Cursor | ready | — |
| B-40 | Reddit | ready | — |
| B-41 | arXiv | ready | — |
| B-5 | GitHub Copilot | ready | — |
| B-50 | Claude の料金プラン | ready | — |
| B-51 | ChatGPT の料金プラン | ready | — |
| B-52 | Gemini の料金プラン | ready | — |
| B-6 | Windsurf | ready | — |
| B-60 | Suno | ready | — |
| B-61 | ACE-Step 1.5 | ready | — |
| B-7 | Claude Code | ready | — |
| B-8 | Codex | ready | — |
| B-9 | v0 | ready | — |
| C-1 | OpenAI | ready | — |
| C-12 | TSMC | ready | — |
| C-13 | Groq | ready | — |
| C-14 | AMD | ready | — |
| C-2 | Anthropic | ready | — |
| C-3 | Google DeepMind | ready | — |
| C-4 | Meta AI | ready | — |
| C-5 | xAI | ready | — |
| C-51 | Dario Amodei | ready | — |
| C-52 | Demis Hassabis | ready | — |
| C-53 | Andrej Karpathy | ready | — |
| C-54 | Ilya Sutskever | ready | — |
| C-55 | Mira Murati | ready | — |
| C-56 | Yann LeCun | ready | — |
| C-57 | Geoffrey Hinton | ready | — |
| C-58 | Elon Musk | ready | — |
| C-59 | Jensen Huang | ready | — |
| C-60 | Ray Kurzweil | ready | — |
| C-7 | Hugging Face | ready | — |
| C-8 | Microsoft AI | ready | — |
| C-80 | AI大学 | ready | — |
| C-81 | にゃんた | ready | — |
| C-82 | まさお | ready | — |
| C-9 | NVIDIA | ready | — |
| D-11 | Claude 3.5 系 | ready | — |
| D-12 | Claude 4 系 | ready | — |
| D-25 | GPT-1 / GPT-2 系 | ready | — |
| D-26 | gpt-oss | ready | — |
| D-30 | Grok 系 | ready | — |
| D-35 | Cursor Composer | ready | — |
| D-40 | Llama 系 | ready | — |
| D-41 | Mistral 系 | ready | — |
| D-42 | Gemma 系 | ready | — |
| D-43 | Qwen 系 | ready | — |
| D-44 | Kimi | ready | — |
| D-45 | GLM | ready | — |
| D-46 | DeepSeek V3 | ready | — |
| D-47 | DeepSeek R1 | ready | — |
| D-50 | DALL-E | ready | — |
| D-51 | Imagen | ready | — |
| D-52 | Sora | ready | — |
| D-53 | Veo | ready | — |
| D-54 | Stable Diffusion | ready | — |
| D-55 | Nano Banana | ready | — |
| D-56 | Seedance | ready | — |
| D-57 | Flow | ready | — |
| D-58 | Whisk | ready | — |
| D-60 | AlphaGo | ready | — |
| D-71 | Whisper | ready | — |
| E-1 | SWE-Bench | ready | — |
| E-2 | SWE-Bench Verified | ready | — |
| E-20 | MMLU | ready | — |
| E-21 | MMLU-Pro | ready | — |
| E-22 | GPQA | ready | — |
| E-23 | GSM8K | ready | — |
| E-24 | MATH | ready | — |
| E-25 | AIME | ready | — |
| E-26 | Humanity's Last Exam | ready | — |
| E-27 | IQ Bench | ready | — |
| E-3 | Terminal-Bench | ready | — |
| E-30 | TAU-Bench | ready | — |
| E-4 | HumanEval | ready | — |
| E-50 | Chatbot Arena | ready | — |
| F-1 | JavaScript | ready | — |
| F-10 | React | ready | — |
| F-11 | Next.js | ready | — |
| F-12 | Electron | ready | — |
| F-13 | Tauri | ready | — |
| F-14 | three.js | ready | — |
| F-15 | shadcn/ui | ready | — |
| F-16 | Tailwind CSS | ready | — |
| F-17 | Astro | ready | — |
| F-2 | TypeScript | ready | — |
| F-20 | ESLint | ready | — |
| F-21 | Prettier | ready | — |
| F-210 | JSON Schema | ready | — |
| F-211 | Zod | ready | — |
| F-212 | OpenAPI | ready | — |
| F-213 | API | ready | — |
| F-214 | API キー | ready | — |
| F-3 | Python | ready | — |
| F-30 | VS Code | ready | — |
| F-35 | Markdown Preview Enhanced | ready | — |
| F-36 | Git Graph | ready | — |
| F-37 | Japanese Language Pack for VS Code | ready | — |
| F-38 | Markdown All in One | ready | — |
| F-4 | HTML | ready | — |
| F-40 | npm | ready | — |
| F-41 | Vite | ready | — |
| F-42 | ビルド | ready | — |
| F-43 | テスト | ready | — |
| F-44 | pnpm | ready | — |
| F-45 | デプロイ | ready | — |
| F-46 | デバッグ | ready | — |
| F-5 | CSS | ready | — |
| F-50 | git | ready | — |
| F-51 | git push | ready | — |
| F-52 | git pull | ready | — |
| F-53 | branch | ready | — |
| F-54 | commit | ready | — |
| F-55 | merge | ready | — |
| F-56 | .gitignore | ready | — |
| F-58 | git stash | ready | — |
| F-59 | README.md | ready | — |
| F-6 | Markdown | ready | — |
| F-60 | GitHub | ready | — |
| F-61 | Pull Request | ready | — |
| F-62 | GitHub Actions | ready | — |
| F-7 | YAML | ready | — |
| F-71 | ripgrep | ready | — |
| F-8 | JSON | ready | — |
| F-81 | bash | ready | — |
| F-82 | WSL | ready | — |
| F-83 | PowerShell | ready | — |
| F-9 | SVG | ready | — |
| G-1 | Context | ready | — |
| G-10 | Prompt Engineering | ready | — |
| G-11 | Context Engineering | ready | — |
| G-13 | Few-shot Learning | ready | — |
| G-14 | Thinking モデル | ready | — |
| G-15 | RAG | ready | — |
| G-16 | Embedding | ready | — |
| G-17 | ベクトル DB | ready | — |
| G-18 | Chain of Thought | ready | — |
| G-19 | Prompt Caching | ready | — |
| G-2 | Token | ready | — |
| G-20 | CLAUDE.md | ready | — |
| G-21 | AGENTS.md | ready | — |
| G-22 | SKILL.md | ready | — |
| G-23 | .claude/settings.json | ready | — |
| G-3 | Dictation | ready | — |
| G-30 | Tool Use | ready | — |
| G-31 | Hook | ready | — |
| G-32 | Slash Command | ready | — |
| G-33 | Function Calling | ready | — |
| G-34 | Code Interpreter | ready | — |
| G-35 | Deep Research | ready | — |
| G-36 | Artifact | ready | — |
| G-38 | Plan Mode | ready | — |
| G-39 | Permission | ready | — |
| G-40 | バイブコーディング | ready | — |
| G-41 | Subagent | ready | — |
| G-42 | Worktree | ready | — |
| G-43 | オーケストレーション | ready | — |
| G-44 | マルチエージェント協調 | ready | — |
| G-45 | 段階的開示 | ready | — |
| G-46 | ナーフ | ready | — |
| G-47 | Auto-compact | ready | — |
| G-48 | Structured Outputs | ready | — |
| G-49 | AI エージェント | ready | — |
| G-5 | Context Window | ready | — |
| G-6 | One-shot | ready | — |
| G-7 | 指示追従性 | ready | — |
| G-8 | 決定論的／非決定論的 | ready | — |
| G-9 | effort レベル | ready | — |
| H-1 | TDD | ready | — |
| H-5 | Scrum / Agile | ready | — |
| H-53 | ChatGPT 登場 | ready | — |
| H-54 | GPT-4 リリース | ready | — |
| H-55 | LLaMA のオープン化 | ready | — |
| H-56 | Claude のバージョン史 | ready | — |
| H-58 | Transformer 論文 | ready | — |
| H-6 | Git Flow | ready | — |
| H-7 | CI/CD | ready | — |
| H-8 | DevOps | ready | — |
| I-1 | MCP | ready | — |
| I-10 | Filesystem MCP | ready | — |
| I-11 | GitHub MCP | ready | — |
| I-12 | Git MCP | ready | — |
| I-13 | Slack MCP | ready | — |
| I-2 | MCP Server | ready | — |
| I-20 | Playwright MCP | ready | — |
| I-21 | Puppeteer MCP | ready | — |
| I-22 | Chrome DevTools MCP | ready | — |
| I-23 | Serena MCP | ready | — |
| I-24 | Context7 MCP | ready | — |
| I-3 | MCP Client | ready | — |
| I-30 | Notion MCP | ready | — |
| I-4 | MCP Transport | ready | — |
| I-41 | SQLite MCP | ready | — |
| I-5 | MCP SDK | ready | — |
| I-50 | AWS MCP | ready | — |
| J-1 | AGI | ready | — |
| J-10 | Machine Learning | ready | — |
| J-100 | リテラシー | ready | — |
| J-11 | Deep Learning | ready | — |
| J-12 | Neural Network | ready | — |
| J-13 | Transformer | ready | — |
| J-14 | LLM | ready | — |
| J-15 | VLM | ready | — |
| J-16 | Fine-tuning | ready | — |
| J-17 | Attention | ready | — |
| J-18 | MoE | ready | — |
| J-19 | 量子化 | ready | — |
| J-2 | 強い AI／弱い AI | ready | — |
| J-20 | Big Data | ready | — |
| J-21 | LoRA | ready | — |
| J-23 | 拡散モデル | ready | — |
| J-3 | Singularity | ready | — |
| J-31 | 第 5 世代コンピュータ | ready | — |
| J-33 | 量子コンピュータ | ready | — |
| J-4 | ASI | ready | — |
| J-40 | IoT | ready | — |
| J-41 | DX | ready | — |
| J-42 | Web3 | ready | — |
| J-51 | Hallucination | ready | — |
| J-52 | Sycophancy | ready | — |
| J-53 | 著作権法 30 条の 4 | ready | — |
| J-54 | ISO/IEC 42001 | ready | — |
| J-56 | GDPR | ready | — |
| J-70 | VRAM | ready | — |
| J-71 | RAM | ready | — |
| J-72 | H100 | ready | — |
| J-73 | Blackwell | ready | — |
| J-74 | RTX シリーズ | ready | — |
| J-75 | Tensor コア | ready | — |
| J-76 | CPU | ready | — |
| J-77 | GPU | ready | — |
| J-78 | HDD | ready | — |
| J-79 | SSD | ready | — |
| J-80 | SATA | ready | — |
| J-81 | M.2 | ready | — |
| J-90 | GUI | ready | — |
| J-91 | CLI | ready | — |
| J-92 | Linux | ready | — |
| J-93 | Ubuntu | ready | — |

## 📖 前付け（front_*・著者本人レビュー必須）（12 件）

| ID | title | status | 概要 |
| :-- | :-- | :-- | :-- |
| A-1 | まえがき | needs_review | — |
| A-10 | 更新履歴と更新方針 | needs_review | — |
| A-11 | 略称表記 | needs_review | — |
| A-2 | この本の読み方 | needs_review | — |
| A-3 | 図鑑の歩き方 | needs_review | — |
| A-4 | 体験区分の凡例 | needs_review | — |
| A-5 | 読者レベルの凡例 | needs_review | — |
| A-6 | 評価日・時変情報の見方 | needs_review | — |
| A-7 | 図のタイプ | needs_review | — |
| A-8 | 色・記号の凡例 | needs_review | — |
| A-9 | 索引 | needs_review | — |
| front_concept | 扉 | drafting | — |

## 📚 自己学習シェルフ（reader_level 6・今季は刊行しない）（35 件）

| ID | title | status | 概要 |
| :-- | :-- | :-- | :-- |
| J-101 | 半導体製造プロセス | needs_review | — |
| J-102 | チップレットと3D積層 | needs_review | — |
| J-103 | ループエンジニアリング | needs_review | — |
| J-104 | ReAct | needs_review | — |
| J-105 | コンテキスト管理 | needs_review | — |
| J-106 | ハーネスエンジニアリング | needs_review | — |
| J-107 | 自律ループとガードレール | needs_review | — |
| J-108 | Ralph Loop | needs_review | — |
| J-109 | モデルルーティング | needs_review | — |
| J-110 | 不確実性デファーラル | needs_review | — |
| J-111 | 人間の認知ボトルネック | needs_review | — |
| J-112 | 認知コストの定量化 | needs_review | — |
| J-113 | 生成UIとagent-native設計 | needs_review | — |
| J-114 | グッドハートの法則 | needs_review | — |
| J-24 | Encoder-Decoder | needs_review | — |
| J-25 | Tokenizer・BPE | needs_review | — |
| J-26 | 潜在空間 | needs_review | — |
| J-27 | RoPE | needs_review | — |
| J-28 | MLA | needs_review | — |
| J-29 | KV Cache | needs_review | — |
| J-30 | Flash Attention | needs_review | — |
| J-82 | 投機的デコード | needs_review | — |
| J-83 | vLLM | needs_review | — |
| J-84 | バッチ推論 | needs_review | — |
| J-85 | スループットとレイテンシ | needs_review | — |
| J-86 | GQA | needs_review | — |
| J-87 | QK-Norm | needs_review | — |
| J-88 | MTP | needs_review | — |
| J-89 | MoE ルーティング | needs_review | — |
| J-94 | 並列化戦略 | needs_review | — |
| J-95 | 半導体サプライチェーン | needs_review | — |
| J-96 | 半導体製造装置 | needs_review | — |
| J-97 | 電子材料 | needs_review | — |
| J-98 | 重要鉱物の地政学 | needs_review | — |
| J-99 | CoWoS | needs_review | — |

## 動線

- **☆ 違反**（タグ `[AI直]`）: その場で entry-writer を呼んで直す（status は drafting のまま）
- **⚠️ 警告**（タグ `[AI整]`）: 軽微なら手で削る／溜まったらまとめて対応
- **needs_review**（タグ `[人書]`）: 著者本人が「非エンジニアのつまずき」「私のコメント」4 項目を埋める。全項目埋まると保存時に `ready`（`[済]`）へ自動昇格
- このキューは `Edit/Write` のたびに自動更新されます。手動更新は `python3 scripts/update_review_queue.py`
- ファイル名のタグを更新するには `python3 scripts/apply_status_markers.py`
