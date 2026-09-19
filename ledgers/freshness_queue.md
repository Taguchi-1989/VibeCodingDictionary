# 鮮度監査キュー（自動生成）

*基準日 2026-09-19 — `python3 scripts/audit_freshness.py` が再生成します。手で編集しないでください。*

このキューは「文章を直す」ための [revision_queue.md](revision_queue.md) とは別で、**事実がまだ正しいかを見に行く**ための台帳です。最新モデル名・料金・提供状況のように、こちらが何もしなくても外の世界が動いて古くなる情報を扱います。

---

## 1. 全体像

- 監査対象: **458 件**（skeleton / sample / archived と前付け・巻末は対象外）
- 期限超過: **131 件**
- 確認日が読めない: 0 件

| Tier | 意味 | 再確認の期限 | 件数 | 期限超過 |
| :-- | :-- | --: | --: | --: |
| S（高） | モデル・サービス・ベンチマーク・MCP・有料/フリーミアム・preview/deprecated | 90 日 | 162 | 131 |
| A（中） | ツール用語・人物組織・ワークフロー、または本文に時変シグナル 3 種以上 | 180 日 | 122 | 0 |
| B（低） | 一般用語・歴史・概念など、外の世界が動いても古くならないもの | 365 日 | 174 | 0 |

### 最終確認からの経過

| 経過 | 件数 |
| :-- | --: |
| 90 日以内 | 157 |
| 91〜180 日 | 301 |

---

## 2. どこから手を付けるか

期限超過を category 別に並べたものです。上から束で片付けるのが速いです（同じ一次情報で複数エントリを確認できるため）。

| category | 期限超過 | 主な確認ポイント |
| :-- | --: | :-- |
| service | 38 | 料金プラン・無料枠・提供地域・名称変更 |
| model | 34 | 後継モデルの有無・提供終了・コンテキスト長 |
| benchmark | 19 | スコアの更新・上位モデルの入れ替わり |
| mcp | 11 | 公式／コミュニティの別・配布場所・対応クライアント |
| person_org | 7 | 所属・役職・社名の変更 |
| term_general | 6 | 本文の時変シグナルを参照 |
| term_tool | 6 | ツールのバージョン・推奨手順の変化 |
| term_llm | 5 | 本文の時変シグナルを参照 |
| tool_agent | 4 | バージョン・対応モデル・提供形態 |
| history | 1 | 本文の時変シグナルを参照 |

---

## 3. 期限超過エントリ

### Tier S（高） — 131 件（期限 90 日）

| ID | 用語 | category | 最終確認 | 経過 | 時変シグナル | path |
| :-- | :-- | :-- | :-- | --: | :-- | :-- |
| B-2 | Claude | service | 2026-04-23※ | 149 日 | — | `content/entries/service/B-2_claude[済].md` |
| D-12 | Claude 4 系 | model | 2026-04-23※ | 149 日 | モデル名／バージョン | `content/entries/model/D-12_claude4[済].md` |
| E-1 | SWE-Bench | benchmark | 2026-04-23※ | 149 日 | — | `content/entries/benchmark/E-1_swe_bench[済].md` |
| B-1 | Gemini | service | 2026-04-24※ | 148 日 | モデル名／バージョン／時点表現 | `content/entries/service/B-1_gemini[済].md` |
| B-3 | ChatGPT | service | 2026-04-25※ | 147 日 | モデル名 | `content/entries/service/B-3_chatgpt[済].md` |
| D-11 | Claude 3.5 系 | model | 2026-04-25※ | 147 日 | モデル名／バージョン／時点表現／提供状況 | `content/entries/model/D-11_claude35[済].md` |
| B-4 | Cursor | service | 2026-04-29※ | 143 日 | 価格 | `content/entries/service/B-4_cursor[済].md` |
| B-5 | GitHub Copilot | service | 2026-04-29※ | 143 日 | 価格 | `content/entries/service/B-5_github_copilot[済].md` |
| B-9 | v0 | service | 2026-04-29※ | 143 日 | 提供状況 | `content/entries/service/B-9_v0[済].md` |
| B-10 | Devin | service | 2026-04-29※ | 143 日 | — | `content/entries/service/B-10_devin[済].md` |
| B-11 | Bolt.new | service | 2026-04-29※ | 143 日 | 価格／提供状況 | `content/entries/service/B-11_bolt_new[済].md` |
| B-12 | Perplexity | service | 2026-04-29※ | 143 日 | 時点表現 | `content/entries/service/B-12_perplexity[済].md` |
| B-20 | Vercel | service | 2026-04-29※ | 143 日 | 提供状況 | `content/entries/service/B-20_vercel[済].md` |
| B-21 | Netlify | service | 2026-04-29※ | 143 日 | 価格 | `content/entries/service/B-21_netlify[済].md` |
| B-22 | Cloudflare | service | 2026-04-29※ | 143 日 | 価格 | `content/entries/service/B-22_cloudflare[済].md` |
| B-23 | AWS | service | 2026-04-29※ | 143 日 | — | `content/entries/service/B-23_aws[済].md` |
| B-24 | Google Cloud | service | 2026-04-29※ | 143 日 | — | `content/entries/service/B-24_google_cloud[済].md` |
| B-25 | Azure | service | 2026-04-29※ | 143 日 | — | `content/entries/service/B-25_azure[済].md` |
| B-30 | Amazon Bedrock | service | 2026-04-29※ | 143 日 | モデル名 | `content/entries/service/B-30_amazon_bedrock[済].md` |
| B-50 | Claude の料金プラン | service | 2026-04-29※ | 143 日 | — | `content/entries/service/B-50_claude_pricing[済].md` |
| B-51 | ChatGPT の料金プラン | service | 2026-04-29※ | 143 日 | モデル名／価格 | `content/entries/service/B-51_chatgpt_pricing[済].md` |
| B-52 | Gemini の料金プラン | service | 2026-04-29※ | 143 日 | モデル名／バージョン | `content/entries/service/B-52_gemini_pricing[済].md` |
| C-4 | Meta AI | person_org | 2026-04-29※ | 143 日 | — | `content/entries/person/C-4_meta_ai[済].md` |
| C-6 | Mistral AI | person_org | 2026-04-29※ | 143 日 | モデル名／バージョン | `content/entries/person/C-6_mistral_ai[済].md` |
| C-7 | Hugging Face | person_org | 2026-04-29※ | 143 日 | モデル名／時点表現 | `content/entries/person/C-7_hugging_face[済].md` |
| C-8 | Microsoft AI | person_org | 2026-04-29※ | 143 日 | — | `content/entries/person/C-8_microsoft_ai[済].md` |
| C-10 | Moonshot AI | person_org | 2026-04-29※ | 143 日 | モデル名／時点表現 | `content/entries/person/C-10_moonshot_ai[済].md` |
| D-1 | Gemini 2 系 | model | 2026-04-29※ | 143 日 | モデル名／バージョン／時点表現 | `content/entries/model/D-1_gemini2[済].md` |
| D-20 | GPT-5 系 | model | 2026-04-29※ | 143 日 | モデル名／時点表現 | `content/entries/model/D-20_gpt5[済].md` |
| D-21 | GPT-4 系 | model | 2026-04-29※ | 143 日 | モデル名／バージョン／時点表現 | `content/entries/model/D-21_gpt4[済].md` |
| D-22 | o1 系 | model | 2026-04-29※ | 143 日 | モデル名 | `content/entries/model/D-22_o1[済].md` |
| D-24 | GPT-3 系 | model | 2026-04-29※ | 143 日 | モデル名／バージョン／時点表現／提供状況 | `content/entries/model/D-24_gpt3[済].md` |
| D-26 | gpt-oss | model | 2026-04-29※ | 143 日 | モデル名／バージョン | `content/entries/model/D-26_gpt_oss[済].md` |
| D-30 | Grok 系 | model | 2026-04-29※ | 143 日 | — | `content/entries/model/D-30_grok[済].md` |
| D-40 | Llama 系 | model | 2026-04-29※ | 143 日 | モデル名／時点表現 | `content/entries/model/D-40_llama[済].md` |
| D-41 | Mistral 系 | model | 2026-04-29※ | 143 日 | モデル名／バージョン | `content/entries/model/D-41_mistral[済].md` |
| D-42 | Gemma 系 | model | 2026-04-29※ | 143 日 | — | `content/entries/model/D-42_gemma[済].md` |
| D-43 | Qwen 系 | model | 2026-04-29※ | 143 日 | モデル名／バージョン／時点表現 | `content/entries/model/D-43_qwen[済].md` |
| D-44 | Kimi | model | 2026-04-29※ | 143 日 | モデル名／時点表現 | `content/entries/model/D-44_kimi[済].md` |
| D-46 | DeepSeek V3 | model | 2026-04-29※ | 143 日 | モデル名 | `content/entries/model/D-46_deepseek_v3[済].md` |
| D-47 | DeepSeek R1 | model | 2026-04-29※ | 143 日 | モデル名／時点表現 | `content/entries/model/D-47_deepseek_r1[済].md` |
| D-50 | DALL-E | model | 2026-04-29※ | 143 日 | 時点表現 | `content/entries/model/D-50_dall_e[済].md` |
| D-51 | Imagen | model | 2026-04-29※ | 143 日 | — | `content/entries/model/D-51_imagen[済].md` |
| D-52 | Sora | model | 2026-04-29※ | 143 日 | 提供状況 | `content/entries/model/D-52_sora[済].md` |
| D-54 | Stable Diffusion | model | 2026-04-29※ | 143 日 | バージョン | `content/entries/model/D-54_stable_diffusion[済].md` |
| D-71 | Whisper | model | 2026-04-29※ | 143 日 | バージョン | `content/entries/model/D-71_whisper[済].md` |
| E-2 | SWE-Bench Verified | benchmark | 2026-04-29※ | 143 日 | — | `content/entries/benchmark/E-2_swe_bench_verified[済].md` |
| E-3 | Terminal-Bench | benchmark | 2026-04-29※ | 143 日 | — | `content/entries/benchmark/E-3_terminal_bench[済].md` |
| E-4 | HumanEval | benchmark | 2026-04-29※ | 143 日 | 時点表現 | `content/entries/benchmark/E-4_humaneval[済].md` |
| E-20 | MMLU | benchmark | 2026-04-29※ | 143 日 | モデル名／バージョン | `content/entries/benchmark/E-20_mmlu[済].md` |
| E-21 | MMLU-Pro | benchmark | 2026-04-29※ | 143 日 | バージョン／時点表現／提供状況 | `content/entries/benchmark/E-21_mmlu_pro[済].md` |
| E-22 | GPQA | benchmark | 2026-04-29※ | 143 日 | モデル名／バージョン | `content/entries/benchmark/E-22_gpqa[済].md` |
| E-30 | TAU-Bench | benchmark | 2026-04-29※ | 143 日 | — | `content/entries/benchmark/E-30_tau_bench[済].md` |
| E-50 | Chatbot Arena | benchmark | 2026-04-29※ | 143 日 | — | `content/entries/benchmark/E-50_chatbot_arena[済].md` |
| F-60 | GitHub | term_tool | 2026-04-29※ | 143 日 | — | `content/entries/term_tool/F-60_github[済].md` |
| F-62 | GitHub Actions | term_tool | 2026-04-29※ | 143 日 | — | `content/entries/term_tool/F-62_github_actions[済].md` |
| F-90 | Docker | term_tool | 2026-04-29※ | 143 日 | — | `content/entries/term_tool/F-90_docker[済].md` |
| F-122 | Prisma | term_tool | 2026-04-29※ | 143 日 | — | `content/entries/term_tool/F-122_prisma[済].md` |
| G-20 | CLAUDE.md | tool_agent | 2026-04-29※ | 143 日 | — | `content/entries/tool_agent/G-20_claude_md[済].md` |
| G-21 | AGENTS.md | tool_agent | 2026-04-29※ | 143 日 | — | `content/entries/tool_agent/G-21_agents_md[済].md` |
| G-22 | SKILL.md | tool_agent | 2026-04-29※ | 143 日 | — | `content/entries/tool_agent/G-22_skill_md[済].md` |
| I-2 | MCP Server | mcp | 2026-04-29※ | 143 日 | — | `content/entries/mcp/I-2_mcp_server[済].md` |
| I-3 | MCP Client | mcp | 2026-04-29※ | 143 日 | — | `content/entries/mcp/I-3_mcp_client[済].md` |
| I-5 | MCP SDK | mcp | 2026-04-29※ | 143 日 | — | `content/entries/mcp/I-5_mcp_sdk[済].md` |
| I-10 | Filesystem MCP | mcp | 2026-04-29※ | 143 日 | — | `content/entries/mcp/I-10_filesystem_mcp[済].md` |
| I-20 | Playwright MCP | mcp | 2026-04-29※ | 143 日 | — | `content/entries/mcp/I-20_playwright_mcp[済].md` |
| I-22 | Chrome DevTools MCP | mcp | 2026-04-29※ | 143 日 | — | `content/entries/mcp/I-22_chrome_devtools_mcp[済].md` |
| I-23 | Serena MCP | mcp | 2026-04-29※ | 143 日 | — | `content/entries/mcp/I-23_serena_mcp[済].md` |
| I-24 | Context7 MCP | mcp | 2026-04-29※ | 143 日 | 時点表現 | `content/entries/mcp/I-24_context7_mcp[済].md` |
| I-30 | Notion MCP | mcp | 2026-04-29※ | 143 日 | — | `content/entries/mcp/I-30_notion_mcp[済].md` |
| I-50 | AWS MCP | mcp | 2026-04-29※ | 143 日 | — | `content/entries/mcp/I-50_aws_mcp[済].md` |
| J-16 | Fine-tuning | term_general | 2026-04-29※ | 143 日 | — | `content/entries/term_general/J-16_fine_tuning[済].md` |
| J-72 | H100 | term_general | 2026-04-29※ | 143 日 | モデル名 | `content/entries/term_general/J-72_h100[済].md` |
| B-6 | Windsurf | service | 2026-04-30※ | 142 日 | 時点表現 | `content/entries/service/B-6_windsurf[済].md` |
| B-8 | Codex | service | 2026-04-30※ | 142 日 | 時点表現 | `content/entries/service/B-8_codex[済].md` |
| B-13 | ElevenLabs | service | 2026-04-30※ | 142 日 | — | `content/entries/service/B-13_elevenlabs[済].md` |
| B-14 | Genspark | service | 2026-04-30※ | 142 日 | 価格 | `content/entries/service/B-14_genspark[済].md` |
| B-15 | Microsoft Copilot | service | 2026-04-30※ | 142 日 | — | `content/entries/service/B-15_microsoft_copilot[済].md` |
| B-16 | Microsoft 365 Copilot | service | 2026-04-30※ | 142 日 | 価格 | `content/entries/service/B-16_microsoft_365_copilot[済].md` |
| B-17 | Edge Copilot | service | 2026-04-30※ | 142 日 | — | `content/entries/service/B-17_edge_copilot[済].md` |
| B-18 | Aqua Voice | service | 2026-04-30※ | 142 日 | — | `content/entries/service/B-18_aqua_voice[済].md` |
| B-26 | Azure OpenAI | service | 2026-04-30※ | 142 日 | モデル名 | `content/entries/service/B-26_azure_openai[済].md` |
| B-27 | Vertex AI | service | 2026-04-30※ | 142 日 | — | `content/entries/service/B-27_vertex_ai[済].md` |
| B-28 | Render | service | 2026-04-30※ | 142 日 | 価格／提供状況 | `content/entries/service/B-28_render[済].md` |
| B-29 | Supabase | service | 2026-04-30※ | 142 日 | — | `content/entries/service/B-29_supabase[済].md` |
| B-31 | Excalidraw | service | 2026-04-30※ | 142 日 | — | `content/entries/service/B-31_excalidraw[済].md` |
| B-32 | Figma | service | 2026-04-30※ | 142 日 | — | `content/entries/service/B-32_figma[済].md` |
| B-33 | Canva | service | 2026-04-30※ | 142 日 | 価格 | `content/entries/service/B-33_canva[済].md` |
| B-40 | Reddit | service | 2026-04-30※ | 142 日 | モデル名 | `content/entries/service/B-40_reddit[済].md` |
| B-41 | arXiv | service | 2026-04-30※ | 142 日 | モデル名 | `content/entries/service/B-41_arxiv[済].md` |
| B-60 | Suno | service | 2026-04-30※ | 142 日 | バージョン／価格 | `content/entries/service/B-60_suno[済].md` |
| B-61 | ACE-Step 1.5 | service | 2026-04-30※ | 142 日 | バージョン | `content/entries/service/B-61_ace_step_1_5[済].md` |
| C-11 | Z.ai | person_org | 2026-04-30※ | 142 日 | バージョン／時点表現 | `content/entries/person/C-11_z_ai[済].md` |
| C-13 | Groq | person_org | 2026-04-30※ | 142 日 | 価格 | `content/entries/person/C-13_groq[済].md` |
| D-2 | Gemini 2.5 系 | model | 2026-04-30※ | 142 日 | モデル名／バージョン／時点表現 | `content/entries/model/D-2_gemini25[済].md` |
| D-4 | Gemini 3.1 系 | model | 2026-04-30※ | 142 日 | モデル名／バージョン | `content/entries/model/D-4_gemini_3_1[済].md` |
| D-14 | Claude Mythos Preview | model | 2026-04-30※ | 142 日 | モデル名／提供状況 | `content/entries/model/D-14_claude_mythos_preview[済].md` |
| D-25 | GPT-1 / GPT-2 系 | model | 2026-04-30※ | 142 日 | モデル名／時点表現／提供状況 | `content/entries/model/D-25_gpt1_gpt2[済].md` |
| D-35 | Cursor Composer | model | 2026-04-30※ | 142 日 | — | `content/entries/model/D-35_cursor_composer[済].md` |
| D-45 | GLM | model | 2026-04-30※ | 142 日 | モデル名／バージョン | `content/entries/model/D-45_glm[済].md` |
| D-53 | Veo | model | 2026-04-30※ | 142 日 | 時点表現 | `content/entries/model/D-53_veo[済].md` |
| D-55 | Nano Banana | model | 2026-04-30※ | 142 日 | モデル名／バージョン | `content/entries/model/D-55_nano_banana[済].md` |
| D-56 | Seedance | model | 2026-04-30※ | 142 日 | — | `content/entries/model/D-56_seedance[済].md` |
| D-57 | Flow | model | 2026-04-30※ | 142 日 | 価格 | `content/entries/model/D-57_flow[済].md` |
| D-58 | Whisk | model | 2026-04-30※ | 142 日 | — | `content/entries/model/D-58_whisk[済].md` |
| D-60 | AlphaGo | model | 2026-04-30※ | 142 日 | 時点表現 | `content/entries/model/D-60_alphago[済].md` |
| D-70 | Amical | model | 2026-04-30※ | 142 日 | — | `content/entries/model/D-70_amical[済].md` |
| E-23 | GSM8K | benchmark | 2026-04-30※ | 142 日 | — | `content/entries/benchmark/E-23_gsm8k[済].md` |
| E-24 | MATH | benchmark | 2026-04-30※ | 142 日 | 時点表現 | `content/entries/benchmark/E-24_math[済].md` |
| E-25 | AIME | benchmark | 2026-04-30※ | 142 日 | モデル名／時点表現 | `content/entries/benchmark/E-25_aime[済].md` |
| E-26 | Humanity's Last Exam | benchmark | 2026-04-30※ | 142 日 | モデル名／バージョン／時点表現 | `content/entries/benchmark/E-26_humanity_s_last_exam[済].md` |
| E-27 | IQ Bench | benchmark | 2026-04-30※ | 142 日 | — | `content/entries/benchmark/E-27_iq_bench[済].md` |
| E-31 | WebArena | benchmark | 2026-04-30※ | 142 日 | 時点表現 | `content/entries/benchmark/E-31_webarena[済].md` |
| E-32 | GAIA | benchmark | 2026-04-30※ | 142 日 | モデル名／時点表現 | `content/entries/benchmark/E-32_gaia[済].md` |
| E-33 | AgentBench | benchmark | 2026-04-30※ | 142 日 | バージョン／時点表現 | `content/entries/benchmark/E-33_agentbench[済].md` |
| E-34 | OSWorld | benchmark | 2026-04-30※ | 142 日 | モデル名／時点表現 | `content/entries/benchmark/E-34_osworld[済].md` |
| E-51 | LMSYS Arena | benchmark | 2026-04-30※ | 142 日 | モデル名／バージョン／時点表現 | `content/entries/benchmark/E-51_lmsys_arena[済].md` |
| F-170 | EC2 | term_tool | 2026-04-30※ | 142 日 | 価格 | `content/entries/term_tool/F-170_ec2[済].md` |
| F-171 | S3 | term_tool | 2026-04-30※ | 142 日 | バージョン | `content/entries/term_tool/F-171_s3[済].md` |
| G-16 | Embedding | term_llm | 2026-04-30※ | 142 日 | — | `content/entries/term_llm/G-16_embedding[済].md` |
| G-19 | Prompt Caching | term_llm | 2026-04-30※ | 142 日 | 価格 | `content/entries/term_llm/G-19_prompt_caching[済].md` |
| G-23 | .claude/settings.json | tool_agent | 2026-04-30※ | 142 日 | — | `content/entries/tool_agent/G-23_claude_settings_json[済].md` |
| G-34 | Code Interpreter | term_llm | 2026-04-30※ | 142 日 | — | `content/entries/term_llm/G-34_code_interpreter[済].md` |
| G-35 | Deep Research | term_llm | 2026-04-30※ | 142 日 | — | `content/entries/term_llm/G-35_deep_research[済].md` |
| G-36 | Artifact | term_llm | 2026-04-30※ | 142 日 | 時点表現／提供状況 | `content/entries/term_llm/G-36_artifact[済].md` |
| H-56 | Claude のバージョン史 | history | 2026-04-30※ | 142 日 | モデル名／バージョン／時点表現 | `content/entries/history/H-56_claude_version_history[済].md` |
| I-21 | Puppeteer MCP | mcp | 2026-04-30※ | 142 日 | 時点表現／提供状況 | `content/entries/mcp/I-21_puppeteer_mcp[済].md` |
| J-31 | 第 5 世代コンピュータ | term_general | 2026-04-30※ | 142 日 | — | `content/entries/term_general/J-31_fifth_generation_computer[済].md` |
| J-43 | SaaS | term_general | 2026-04-30※ | 142 日 | 価格／時点表現 | `content/entries/term_general/J-43_saas[済].md` |
| J-73 | Blackwell | term_general | 2026-04-30※ | 142 日 | 時点表現／提供状況 | `content/entries/term_general/J-73_blackwell[済].md` |
| J-74 | RTX シリーズ | term_general | 2026-04-30※ | 142 日 | — | `content/entries/term_general/J-74_rtx-series[済].md` |

### Tier A（中） — 0 件（期限 180 日）

_なし_

### Tier B（低） — 0 件（期限 365 日）

_なし_

※ = `last_audited` が未記入で `evaluation_date` を代用しているもの。

---

## 4. 確認すべき本文行（Tier S の期限超過）

エントリを開かなくても「どこを見ればいいか」が分かるように、時変シグナルに当たった行を 1 種類につき 1 行だけ抜いています。

**D-12 Claude 4 系**（149 日経過）

- `モデル名` - Before（4 系登場前）: Claude 3.5 Sonnet でコーディング適性が跳ねた世代
- `バージョン` Claude 第 4 世代。Opus・Sonnet・Haiku の 3 段階で 4.7 が現行の主力です。

**B-1 Gemini**（148 日経過）

- `モデル名` Gemini 2.5 系、Vertex AI、AI Studio、Workspace 個別機能。
- `時点表現` Google が提供する AI アシスタントのブランド。2024 年に Bard から改名しました。

**B-3 ChatGPT**（147 日経過）

- `モデル名` ChatGPT というブランドの下に、アプリ・カスタム GPT・API という 3 つの入口があることと、それを支えるモデル（GPT-5 系）の関係を 1 枚で示します。

**D-11 Claude 3.5 系**（147 日経過）

- `モデル名` Artifacts、Computer use、Claude 4 系。
- `バージョン` バイブコーディング普及前夜の主力。Sonnet 3.5 でコード適性が跳ねた世代です。
- `時点表現` 現在は 4 系が主力のため、過去の記事で「Sonnet 3.5 で試した」という記述を見かける場面が出会いの入口です。どの版・ティアか把握すると 4 系への移行比較に役立ちます。
- `提供状況` 現在は deprecated 扱い。API 提供は要確認です。

**B-4 Cursor**（143 日経過）

- `価格` 無料枠に月あたりの使用上限があり超過すると有料プランが必要です。

**B-5 GitHub Copilot**（143 日経過）

- `価格` VS Code や JetBrains など既存エディタに拡張として追加して使います。GitHub アカウントでサインインするのが前提で、個人向けの無料枠もあります。

**B-9 v0**（143 日経過）

- `提供状況` 「カード一覧を作って」と入力すると、ブラウザで動く React コンポーネントを生成します。プレビューをその場で確認し、コードをプロジェクトへ貼り付けて使えます。

**B-11 Bolt.new**（143 日経過）

- `価格` 無料枠の月次トークン上限を超えると有料プランへの切り替えが必要です。
- `提供状況` プロンプトを入れてからプレビューが出るまでのワンフローを、左から右に流れる形で示します。

**B-12 Perplexity**（143 日経過）

- `時点表現` - シーン1: 担当者が「〇〇の現在の価格は？」と入力する

**B-20 Vercel**（143 日経過）

- `提供状況` push で URL が出る流れとプレビュー・本番の 2 段階を押さえます。

**B-21 Netlify**（143 日経過）

- `価格` 無料枠で個人サイトが立ち、設定ファイルも最小限で済みます。

**B-22 Cloudflare**（143 日経過）

- `価格` 無料プランで CDN と DDoS 対策が使えます。

**B-30 Amazon Bedrock**（143 日経過）

- `モデル名` - 周辺の要素: Claude（Anthropic）／Llama（Meta）／Titan（Amazon）／Mistral／利用アプリ

**B-51 ChatGPT の料金プラン**（143 日経過）

- `モデル名` ChatGPT、OpenAI、API、GPT-5。
- `価格` Free から Pro（$200/月）まで 5 段階で選べる ChatGPT の利用プランです。

**B-52 Gemini の料金プラン**（143 日経過）

- `モデル名` 「Google AI Pro に入ると Gemini 2.5 Pro が使えるようになりますよね。」

**C-6 Mistral AI**（143 日経過）

- `モデル名` オープンウェイトモデルと商用 API を提供します。Mistral 7B・Mixtral 8x7B を Apache 2.0 で公開し、ローカル利用も可能です。

**C-7 Hugging Face**（143 日経過）

- `モデル名` Llama や Mistral などのオープンモデルを探すとき、最初に行き着く場所です。transformers ライブラリは Python で AI を扱う事実上の標準で、コード…
- `時点表現` - 中心に置く概念: Hugging Face（2016 年設立）

**C-10 Moonshot AI**（143 日経過）

- `モデル名` 「Moonshot の Kimi K2、オープンウェイトで DeepSeek 系と並ぶ評価らしいですよね。」
- `時点表現` 2023 年創業の中国 AI 企業。長文処理に強い LLM「Kimi」シリーズを開発しています。

**D-1 Gemini 2 系**（143 日経過）

- `モデル名` Gemini 2.0 の主要モデルを時系列に並べ、Flash・Pro の役割と登場順を 1 枚で掴んでもらいます。
- `時点表現` Gemini アプリや Google AI Studio で試せるほか、API 経由で開発に組み込まれます。2025 年初めに Flash が登場し、Gemini というサービスの…

**D-20 GPT-5 系**（143 日経過）

- `モデル名` テキスト生成・画像理解・コード生成を担うモデル系統です。GPT-4 系からの進化として、推論能力の向上とマルチモーダル（複数の入力形式への対応）強化が主な特徴とされます。
- `時点表現` OpenAI の 2025 年フラッグシップ世代です。ChatGPT と API の両方を通じて使えます。

**D-21 GPT-4 系**（143 日経過）

- `モデル名` ChatGPT を一気に実用へ押し上げた世代です。GPT-4o がマルチモーダル化の起点です。
- `バージョン` GPT-4 → GPT-4 Turbo → GPT-4o → GPT-4.1 の系譜を 1 本の矢印で示し、各版の主な特徴と位置づけを添えます。
- `時点表現` テキスト・コード生成と画像理解を担うモデル系統です。2023 年に登場して ChatGPT の実用水準を引き上げ、GPT-4o でマルチモーダル対応が広がりました。

**D-22 o1 系**（143 日経過）

- `モデル名` 回答の前に内部で段階的な推論（Reasoning）を重ねるモデル系です。数学・論理・コード最適化など一発で答えが出にくい問題に向きます。o1・o1-mini・o1-pro の各バリ…

**D-24 GPT-3 系**（143 日経過）

- `モデル名` GPT-3（2020）→ GPT-3.5（2022-11）→ ChatGPT 公開 の 3 点を時系列で示し、「歴史的起点」としての位置を伝えます。
- `時点表現` テキスト生成・翻訳・要約・コード生成を担ったモデル系統です。2020 年に 175B パラメータで登場し ChatGPT の土台になりました。
- `提供状況` 主に AI 史の文脈で名前が出ます。ChatGPT の初期ベースとして AI 元年（2022 年 11 月）の話題で挙がりますが、新規開発は後継世代が推奨されます。

**D-26 gpt-oss**（143 日経過）

- `モデル名` GPT-4o 系のクローズドモデルより性能は下で、GPU 環境が必要です。
- `バージョン` OpenAI が 2025-08 に Apache 2.0 で公開したモデルです。20B・120B の 2 サイズがあり、手元で推論できます。

**D-40 Llama 系**（143 日経過）

- `モデル名` Meta が開発・公開するテキスト生成モデル群です。ウェイトをダウンロードしてローカルで動かせるため、クラウド API なしで推論できます。Llama 1（2023年）〜 Llam…

**D-41 Mistral 系**（143 日経過）

- `モデル名` 仏 Mistral AI が開発するテキスト生成モデル群です。Mixtral（MoE 構造）を含む軽量〜高性能の複数版があり、多くが Apache 2.0 で公開されています。
- `バージョン` 欧州発のオープンモデル代表。Apache 2.0 で自由に使えます。

**D-43 Qwen 系**（143 日経過）

- `モデル名` ローカル LLM の選択肢やアジア言語タスクを調べる場面で名前が出ます。Qwen 2.5・Qwen 3 は Hugging Face のダウンロード数上位に入り、オープンモデル比較…
- `時点表現` Qwen 2.5 が安定した実績版、Qwen 3 が最新世代という世代感が要点です。

**D-44 Kimi**（143 日経過）

- `モデル名` 中国 AI 動向記事やオープンモデルの比較表で名前が出ます。DeepSeek や Qwen と並んで「中国系モデル」として言及されます。
- `時点表現` - K1（2023 年末〜）: Moonshot AI の初代モデル。長文 Context 処理を前面に打ち出す

**D-46 DeepSeek V3**（143 日経過）

- `モデル名` 中国 DeepSeek 発の大規模オープンモデル。コスト効率で注目されています。

**D-47 DeepSeek R1**（143 日経過）

- `モデル名` 2025 年 1 月、o1 系と同等の推論性能をオープンウェイトで達成し「DeepSeek ショック」と呼ばれました。deepseek.com の API や Hugging Fa…

**D-50 DALL-E**（143 日経過）

- `時点表現` - DALL-E 1（2021年1月）：テキストから画像生成の概念実証。品質はまだ荒削り

**D-52 Sora**（143 日経過）

- `提供状況` - 2024-02：Sora 発表（研究プレビュー）— テキスト→動画の衝撃デモが公開

**D-54 Stable Diffusion**（143 日経過）

- `バージョン` SD 1.4 から SD3.5・Flux 系まで世代を追い、「ウェイト公開のモデルがどう進化してきたか」を一目で捉えてもらいます。

**D-71 Whisper**（143 日経過）

- `バージョン` OpenAI が公開した音声認識モデルです。99 言語に対応し、Apache 2.0 ライセンスで無償利用できます。

**E-4 HumanEval**（143 日経過）

- `時点表現` - 関係の描き方: 左から右への一本線フロー。右端に「最新モデルは 90%+ 帯」のスコアバーを小さく添える

**E-20 MMLU**（143 日経過）

- `モデル名` - GPT-4
- `バージョン` 4 カテゴリの傘と、人間水準 89.8% という比較軸を把握します。

**E-21 MMLU-Pro**（143 日経過）

- `バージョン` MMLU、GPQA、arXiv:2406.01574
- `時点表現` 3. スコアの水準を把握 — 70% 台が現在のトップクラスの目安と知る
- `提供状況` 14 分野の問題を 10 択形式で出し、AI が推論してどれだけ正確に答えられるかを測ります。MMLU（4 択）が多くのモデルで 90% 以上に達し飽和したため、難化させた後継指標…

**E-22 GPQA**（143 日経過）

- `モデル名` o1 や o3 などの reasoning（推論特化）モデルが台頭したころ、その実力を示す指標として注目されました。モデル発表資料や論文比較表で GPQA Diamond（最難サブ…
- `バージョン` MMLU-Pro、o1、arXiv:2311.12022

**I-24 Context7 MCP**（143 日経過）

- `時点表現` - 視覚要素: プロンプト（`use context7`）→ Context7 MCP → 公式ドキュメント → 現在の API の回答

**J-72 H100**（143 日経過）

- `モデル名` GPT-4 や Claude 3 などの LLM 学習ニュースで「H100 数万枚」という表現を目にします。AWS p5・GCP A3 などのクラウド GPU インスタンスで時間貸…

**B-6 Windsurf**（142 日経過）

- `時点表現` Codeium が 2024 年 11 月に公開した AI コードエディタ。Cascade が複数ファイルを横断編集します。

**B-8 Codex**（142 日経過）

- `時点表現` 旧 Codex（2021 年エンジン）と同名のため記事の年代に注意が必要です。

**B-14 Genspark**（142 日経過）

- `価格` 料金・機能は時変情報で、無料枠の制限は変わることがあります。

**B-16 Microsoft 365 Copilot**（142 日経過）

- `価格` Word・Excel・Teams などに組み込まれた業務統合 AI です。月額 $30 の有料追加サービスになります。

**B-26 Azure OpenAI**（142 日経過）

- `モデル名` GPT-4o や o1 などの OpenAI モデルを、Azure のインフラ上で API として呼び出せるようにします。データが指定リージョン内に留まるため、情報管理の要件が厳し…

**B-28 Render**（142 日経過）

- `価格` 無料プランは一定時間で休止し、常時稼働には有料プランが必要です。
- `提供状況` - シーン2: PR を出すとプレビュー環境が自動生成され、URL が届く

**B-33 Canva**（142 日経過）

- `価格` 無料プランの範囲とテンプレート操作の流れを把握します。

**B-40 Reddit**（142 日経過）

- `モデル名` - シーン2: 開発者が r/LocalLLaMA で Llama 4 の実機ベンチを確認している

**B-41 arXiv**（142 日経過）

- `モデル名` Transformer 論文（J-13）や GPT・DeepSeek 系の技術報告など、話題の論文の出所として名前を見かけます。Hugging Face Papers や Pape…

**B-60 Suno**（142 日経過）

- `バージョン` ElevenLabs、ACE-Step 1.5、Sora
- `価格` 商用利用の可否はプランで異なり、無料プランは個人利用に限定されます。

**B-61 ACE-Step 1.5**（142 日経過）

- `バージョン` テキストプロンプトからボーカル付きの楽曲を生成します。多言語の歌詞に対応し、ステム分離やスタイル変換も行えます。Apache 2.0 ライセンスで商用利用が可能です。

**C-11 Z.ai**（142 日経過）

- `バージョン` 「Z.ai の GLM-4.6、ローカルで動かすと意外と速いです。」
- `時点表現` Hugging Face で GLM モデルを検索するとヒットします。中国系 LLM 記事では「六小虎」の一角として登場します。2025 年 1 月に米国制裁リスト（Entity …

**C-13 Groq**（142 日経過）

- `価格` 2. API 選定 — GroqCloud の無料枠で速度・料金を OpenAI 互換 API と比較します

**D-2 Gemini 2.5 系**（142 日経過）

- `モデル名` 2025 年 3 月公開の Gemini 2.5 世代です。Pro／Flash／Flash-Lite の 3 ティアがあります。

**D-4 Gemini 3.1 系**（142 日経過）

- `モデル名` Gemini 3 系のマイナー更新版で、コーディング精度と長文処理の改善が中心とされています。
- `バージョン` Google AI Studio や Gemini アプリで「Gemini 3.1 Pro」として現れます。SWE-Bench（コード評価指標）の比較記事でも見かけます。

**D-14 Claude Mythos Preview**（142 日経過）

- `モデル名` Claude 4 系、Anthropic、B-2 Claude
- `提供状況` サイバーセキュリティ特化の限定プレビューモデルとされます。

**D-25 GPT-1 / GPT-2 系**（142 日経過）

- `モデル名` GPT-1（2018年）は「事前学習＋微調整」という現在の主流パラダイムを確立しました。GPT-2（2019年）はゼロショット学習を示し、規模が増すほど性能が伸びることを実証してい…
- `提供状況` 廃止済みで実用では使いません。歴史知識として扱います。

**D-45 GLM**（142 日経過）

- `モデル名` DeepSeek V3、Qwen、CodeGeeX
- `バージョン` Hugging Face でオープンウェイト版が公開されており、ローカル GPU で動かす構成を試みる際に名前を見かけます。Cursor や Roo Code などのエディタ連携で…

**D-53 Veo**（142 日経過）

- `時点表現` テキスト・画像・既存動画を入力として、リアルな質感とカメラワークを持つ動画を生成します。Veo 3（2025 年）では環境音・対話・効果音まで含む音声付き動画を出力できます。

**D-55 Nano Banana**（142 日経過）

- `モデル名` 画像の構図を崩さず衣装・背景・追加要素だけを差し替えます。正式名称は Gemini 2.5 Flash Image で、LMArena の画像評価で上位を維持しています。

**D-57 Flow**（142 日経過）

- `価格` AI Pro 以上の有償プランが必要で、無料枠はありません。

**D-60 AlphaGo**（142 日経過）

- `時点表現` Google DeepMind が開発した囲碁 AI です。2016 年にトップ棋士を破り「AI が人間を超えた」と知られます。

**E-24 MATH**（142 日経過）

- `時点表現` 2021 年公開の数学ベンチマークです。代数・幾何・数論・確率など 7 分類 12,500 問を収録し、最終回答を照合して正答率を算出します。

**E-25 AIME**（142 日経過）

- `モデル名` 「AIME 2024 で o3 系が満点近かった、と Twitter で話題になっていましたね。」
- `時点表現` - シーン2: 2024・2025 年版（AIME I/II）が LLM ベンチ比較で標準的に使われる

**E-26 Humanity's Last Exam**（142 日経過）

- `モデル名` AI モデルの比較記事でスコアが引用されます。公開当初は正答率 10% 未満が多く、o3 や Gemini 2.5 Pro が 30% 台に達し進歩の指標として注目されています。
- `時点表現` 2025 年 1 月に公開された 3,000 問のテスト群です。数学・物理・人文など 100 以上の分野を横断し、AI の総合的な学力を測ります。

**E-31 WebArena**（142 日経過）

- `時点表現` カーネギーメロン大学が 2023 年に発表したベンチマークです。Docker で再現した 5 種の擬似 Web サイトに自然言語タスク 812 個を与え、AI エージェントの完了率…

**E-32 GAIA**（142 日経過）

- `モデル名` AI エージェントのリリース記事や研究論文で「GAIA スコア」として登場します。公開時は GPT-4 約 15%・人間約 92%、2025 年には上位勢が 60% 台に到達してい…
- `時点表現` Meta（C-4）と Hugging Face（C-7）が 2023 年末に公開した、AI エージェントの実用能力を測る問題集です。Web 検索・PDF 読解・画像理解など複数ツー…

**E-33 AgentBench**（142 日経過）

- `バージョン` 「AgentBench の OS 環境で GLM-4.6 が伸びていました。」
- `時点表現` OS 操作や DB、Web ショッピングなど 8 環境のマルチターン課題を LLM に解かせ、チャット応答ではなく実行力を数値化します。清華大学・Z.ai が 2023 年に公開し…

**E-34 OSWorld**（142 日経過）

- `モデル名` Computer Use の性能比較記事で登場します。公開時は GPT-4V 約 12% に対し人間 約 72% でしたが、Computer Use や Operator の登場で…
- `時点表現` 2024 年 4 月公開のベンチマークで、実 OS 環境で 369 タスクの到達度を測ります。スクリーンショットを入力してキーやマウス操作で答える形が特徴です。

**E-51 LMSYS Arena**（142 日経過）

- `モデル名` 「LMSYS Arena で Gemini 2.5 Pro が 1 位に上がってきました。」
- `時点表現` - シーン1: LMSYS（2023 年）が Chatbot Arena を公開。UC Berkeley 発の研究基盤として注目を集める

**F-170 EC2**（142 日経過）

- `価格` Amazon Elastic Compute Cloud の略。AWS 上で仮想マシンを従量課金で借りられるサービスです。

**F-171 S3**（142 日経過）

- `バージョン` ファイルを「バケット」に保存し URL やキーで取り出せるストレージです。公称耐久性は 99.999999999%（イレブン・ナイン）とされ、設計上はきわめて失われにくい水準です。

**G-19 Prompt Caching**（142 日経過）

- `価格` - うれしさ: 月額が 30〜40% 削減できることがあります

**G-36 Artifact**（142 日経過）

- `時点表現` Claude.ai でコードや文書を生成すると、会話欄とは別の右側パネルに成果物が表示されます。パネル内で直接編集でき、ファイル単位で履歴が残るため、会話を遡らずに最新版を確認でき…
- `提供状況` - シーン2: HTML プレビューを確認しながら会話で修正指示を出す

**H-56 Claude のバージョン史**（142 日経過）

- `モデル名` Claude 3 系、Claude 4 系、Extended Thinking
- `バージョン` 「Extended Thinking は 3.7 Sonnet から搭載されました。」
- `時点表現` Anthropic が 2023 年以降リリースしてきた Claude シリーズの版数と命名変遷をまとめます。

**I-21 Puppeteer MCP**（142 日経過）

- `時点表現` かつては MCP 公式の参照サーバーの 1 つでしたが、2025 年 5 月に保守対象から外れ、アーカイブ用のリポジトリへ移りました。いまブラウザ操作を任せるなら Playwrig…

**J-43 SaaS**（142 日経過）

- `価格` 月額費用が積み重なるため、複数契約時の総コストに注意が必要です。
- `時点表現` - 視覚要素: ブラウザ → クラウドサーバー → 常に最新版

**J-73 Blackwell**（142 日経過）

- `時点表現` NVIDIA が 2024 年 3 月に発表した GPU アーキテクチャ世代で、Hopper（H100）の後継です。

---

## 使い方

1. §2 で束を選ぶ（モデル → サービス → ベンチマーク → MCP の順が安いです）
2. §4 の該当行を見ながら一次情報（公式ドキュメント・料金ページ）を確認する
3. **変更が無かった場合**: frontmatter の `last_audited` を確認日に更新するだけで完了です。`evaluation_date` は執筆時点の記録なので動かしません
4. **変更があった場合**: 本文を直し、出典メモの `checked YYYY-MM-DD` も合わせ、`last_audited` を更新します。本文の改訂は entry-writer サブエージェントに渡せます
5. 監査した範囲と結果は [freshness_audit_log.md](freshness_audit_log.md) に 1 行追記してください

「最新モデル名」「ChatGPT の月額」のように、**1 つ変わると複数エントリが同時に古くなる事実**は、エントリ側から巡回すると取りこぼします。[volatile_facts.md](volatile_facts.md) に事実側の台帳があるので、そちらから影響エントリを引いて束で直す方が速いです。

Tier の判定が実態と合わないときは、frontmatter に `volatility: high | mid | low` を足すと上書きできます（[docs/entry_schema.yaml](../docs/entry_schema.yaml) 参照）。
