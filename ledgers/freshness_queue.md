# 鮮度監査キュー（自動生成）

*基準日 2026-11-13 — `python3 scripts/audit_freshness.py` が再生成します。手で編集しないでください。*

このキューは「文章を直す」ための [revision_queue.md](revision_queue.md) とは別で、**事実がまだ正しいかを見に行く**ための台帳です。最新モデル名・料金・提供状況のように、こちらが何もしなくても外の世界が動いて古くなる情報を扱います。

---

## 1. 全体像

- 監査対象: **499 件**（skeleton / sample / archived と前付け・巻末は対象外）
- 期限超過: **226 件**
- 確認日が読めない: 0 件

| Tier | 意味 | 再確認の期限 | 件数 | 期限超過 |
| :-- | :-- | --: | --: | --: |
| S（高） | モデル・サービス・ベンチマーク・MCP・有料/フリーミアム・preview/deprecated | 90 日 | 198 | 125 |
| A（中） | ツール用語・人物組織・ワークフロー、または本文に時変シグナル 3 種以上 | 180 日 | 124 | 101 |
| B（低） | 一般用語・歴史・概念など、外の世界が動いても古くならないもの | 365 日 | 177 | 0 |

### 最終確認からの経過

| 経過 | 件数 |
| :-- | --: |
| 90 日以内 | 141 |
| 91〜180 日 | 81 |
| 181〜365 日 | 277 |

---

## 2. どこから手を付けるか

期限超過を category 別に並べたものです。上から束で片付けるのが速いです（同じ一次情報で複数エントリを確認できるため）。

| category | 期限超過 | 主な確認ポイント |
| :-- | --: | :-- |
| term_tool | 80 | ツールのバージョン・推奨手順の変化 |
| service | 45 | 料金プラン・無料枠・提供地域・名称変更 |
| person_org | 25 | 所属・役職・社名の変更 |
| model | 21 | 後継モデルの有無・提供終了・コンテキスト長 |
| benchmark | 18 | スコアの更新・上位モデルの入れ替わり |
| mcp | 11 | 公式／コミュニティの別・配布場所・対応クライアント |
| term_general | 8 | 本文の時変シグナルを参照 |
| term_llm | 6 | 本文の時変シグナルを参照 |
| history | 5 | 本文の時変シグナルを参照 |
| workflow | 5 | 本文の時変シグナルを参照 |
| tool_agent | 2 | バージョン・対応モデル・提供形態 |

---

## 3. 期限超過エントリ

### Tier S（高） — 125 件（期限 90 日）

| ID | 用語 | category | 最終確認 | 経過 | 時変シグナル | path |
| :-- | :-- | :-- | :-- | --: | :-- | :-- |
| B-2 | Claude | service | 2026-04-23※ | 204 日 | — | `content/entries/service/B-2_claude[済].md` |
| E-1 | SWE-Bench | benchmark | 2026-04-23※ | 204 日 | — | `content/entries/benchmark/E-1_swe_bench[済].md` |
| B-1 | Gemini | service | 2026-04-24※ | 203 日 | モデル名／バージョン／時点表現 | `content/entries/service/B-1_gemini[済].md` |
| B-3 | ChatGPT | service | 2026-04-25※ | 202 日 | モデル名 | `content/entries/service/B-3_chatgpt[済].md` |
| B-4 | Cursor | service | 2026-04-29※ | 198 日 | 価格 | `content/entries/service/B-4_cursor[済].md` |
| B-5 | GitHub Copilot | service | 2026-04-29※ | 198 日 | 価格 | `content/entries/service/B-5_github_copilot[済].md` |
| B-9 | v0 | service | 2026-04-29※ | 198 日 | 提供状況 | `content/entries/service/B-9_v0[済].md` |
| B-10 | Devin | service | 2026-04-29※ | 198 日 | — | `content/entries/service/B-10_devin[済].md` |
| B-11 | Bolt.new | service | 2026-04-29※ | 198 日 | 価格／提供状況 | `content/entries/service/B-11_bolt_new[済].md` |
| B-12 | Perplexity | service | 2026-04-29※ | 198 日 | 時点表現 | `content/entries/service/B-12_perplexity[済].md` |
| B-20 | Vercel | service | 2026-04-29※ | 198 日 | 提供状況 | `content/entries/service/B-20_vercel[済].md` |
| B-21 | Netlify | service | 2026-04-29※ | 198 日 | 価格 | `content/entries/service/B-21_netlify[済].md` |
| B-22 | Cloudflare | service | 2026-04-29※ | 198 日 | 価格 | `content/entries/service/B-22_cloudflare[済].md` |
| B-23 | AWS | service | 2026-04-29※ | 198 日 | — | `content/entries/service/B-23_aws[済].md` |
| B-24 | Google Cloud | service | 2026-04-29※ | 198 日 | — | `content/entries/service/B-24_google_cloud[済].md` |
| B-25 | Azure | service | 2026-04-29※ | 198 日 | — | `content/entries/service/B-25_azure[済].md` |
| B-30 | Amazon Bedrock | service | 2026-04-29※ | 198 日 | モデル名 | `content/entries/service/B-30_amazon_bedrock[済].md` |
| B-51 | ChatGPT の料金プラン | service | 2026-04-29※ | 198 日 | モデル名／価格 | `content/entries/service/B-51_chatgpt_pricing[済].md` |
| B-52 | Gemini の料金プラン | service | 2026-04-29※ | 198 日 | モデル名／バージョン | `content/entries/service/B-52_gemini_pricing[済].md` |
| C-6 | Mistral AI | person_org | 2026-04-29※ | 198 日 | モデル名／バージョン | `content/entries/person/C-6_mistral_ai[済].md` |
| C-7 | Hugging Face | person_org | 2026-04-29※ | 198 日 | モデル名／時点表現 | `content/entries/person/C-7_hugging_face[済].md` |
| C-8 | Microsoft AI | person_org | 2026-04-29※ | 198 日 | — | `content/entries/person/C-8_microsoft_ai[済].md` |
| D-26 | gpt-oss | model | 2026-04-29※ | 198 日 | モデル名／バージョン | `content/entries/model/D-26_gpt_oss[済].md` |
| D-41 | Mistral 系 | model | 2026-04-29※ | 198 日 | モデル名／バージョン | `content/entries/model/D-41_mistral[済].md` |
| D-42 | Gemma 系 | model | 2026-04-29※ | 198 日 | — | `content/entries/model/D-42_gemma[済].md` |
| D-43 | Qwen 系 | model | 2026-04-29※ | 198 日 | モデル名／バージョン／時点表現 | `content/entries/model/D-43_qwen[済].md` |
| D-47 | DeepSeek R1 | model | 2026-04-29※ | 198 日 | モデル名／時点表現 | `content/entries/model/D-47_deepseek_r1[済].md` |
| D-50 | DALL-E | model | 2026-04-29※ | 198 日 | 時点表現 | `content/entries/model/D-50_dall_e[済].md` |
| D-51 | Imagen | model | 2026-04-29※ | 198 日 | — | `content/entries/model/D-51_imagen[済].md` |
| D-52 | Sora | model | 2026-04-29※ | 198 日 | 提供状況 | `content/entries/model/D-52_sora[済].md` |
| D-54 | Stable Diffusion | model | 2026-04-29※ | 198 日 | バージョン | `content/entries/model/D-54_stable_diffusion[済].md` |
| D-71 | Whisper | model | 2026-04-29※ | 198 日 | バージョン | `content/entries/model/D-71_whisper[済].md` |
| E-2 | SWE-Bench Verified | benchmark | 2026-04-29※ | 198 日 | — | `content/entries/benchmark/E-2_swe_bench_verified[済].md` |
| E-4 | HumanEval | benchmark | 2026-04-29※ | 198 日 | 時点表現 | `content/entries/benchmark/E-4_humaneval[済].md` |
| E-20 | MMLU | benchmark | 2026-04-29※ | 198 日 | モデル名／バージョン | `content/entries/benchmark/E-20_mmlu[済].md` |
| E-21 | MMLU-Pro | benchmark | 2026-04-29※ | 198 日 | バージョン／時点表現／提供状況 | `content/entries/benchmark/E-21_mmlu_pro[済].md` |
| E-22 | GPQA | benchmark | 2026-04-29※ | 198 日 | モデル名／バージョン | `content/entries/benchmark/E-22_gpqa[済].md` |
| E-30 | TAU-Bench | benchmark | 2026-04-29※ | 198 日 | — | `content/entries/benchmark/E-30_tau_bench[済].md` |
| E-50 | Chatbot Arena | benchmark | 2026-04-29※ | 198 日 | — | `content/entries/benchmark/E-50_chatbot_arena[済].md` |
| F-60 | GitHub | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-60_github[済].md` |
| F-62 | GitHub Actions | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-62_github_actions[済].md` |
| F-90 | Docker | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-90_docker[済].md` |
| F-122 | Prisma | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-122_prisma[済].md` |
| G-21 | AGENTS.md | tool_agent | 2026-04-29※ | 198 日 | — | `content/entries/tool_agent/G-21_agents_md[済].md` |
| I-2 | MCP Server | mcp | 2026-04-29※ | 198 日 | — | `content/entries/mcp/I-2_mcp_server[済].md` |
| I-3 | MCP Client | mcp | 2026-04-29※ | 198 日 | — | `content/entries/mcp/I-3_mcp_client[済].md` |
| I-5 | MCP SDK | mcp | 2026-04-29※ | 198 日 | — | `content/entries/mcp/I-5_mcp_sdk[済].md` |
| I-10 | Filesystem MCP | mcp | 2026-04-29※ | 198 日 | — | `content/entries/mcp/I-10_filesystem_mcp[済].md` |
| I-20 | Playwright MCP | mcp | 2026-04-29※ | 198 日 | — | `content/entries/mcp/I-20_playwright_mcp[済].md` |
| I-22 | Chrome DevTools MCP | mcp | 2026-04-29※ | 198 日 | — | `content/entries/mcp/I-22_chrome_devtools_mcp[済].md` |
| I-23 | Serena MCP | mcp | 2026-04-29※ | 198 日 | — | `content/entries/mcp/I-23_serena_mcp[済].md` |
| I-24 | Context7 MCP | mcp | 2026-04-29※ | 198 日 | 時点表現 | `content/entries/mcp/I-24_context7_mcp[済].md` |
| I-30 | Notion MCP | mcp | 2026-04-29※ | 198 日 | — | `content/entries/mcp/I-30_notion_mcp[済].md` |
| I-50 | AWS MCP | mcp | 2026-04-29※ | 198 日 | — | `content/entries/mcp/I-50_aws_mcp[済].md` |
| J-16 | Fine-tuning | term_general | 2026-04-29※ | 198 日 | — | `content/entries/term_general/J-16_fine_tuning[済].md` |
| J-72 | H100 | term_general | 2026-04-29※ | 198 日 | モデル名 | `content/entries/term_general/J-72_h100[済].md` |
| B-6 | Windsurf | service | 2026-04-30※ | 197 日 | 時点表現 | `content/entries/service/B-6_windsurf[済].md` |
| B-8 | Codex | service | 2026-04-30※ | 197 日 | 時点表現 | `content/entries/service/B-8_codex[済].md` |
| B-13 | ElevenLabs | service | 2026-04-30※ | 197 日 | — | `content/entries/service/B-13_elevenlabs[済].md` |
| B-14 | Genspark | service | 2026-04-30※ | 197 日 | 価格 | `content/entries/service/B-14_genspark[済].md` |
| B-15 | Microsoft Copilot | service | 2026-04-30※ | 197 日 | — | `content/entries/service/B-15_microsoft_copilot[済].md` |
| B-16 | Microsoft 365 Copilot | service | 2026-04-30※ | 197 日 | 価格 | `content/entries/service/B-16_microsoft_365_copilot[済].md` |
| B-17 | Edge Copilot | service | 2026-04-30※ | 197 日 | — | `content/entries/service/B-17_edge_copilot[済].md` |
| B-18 | Aqua Voice | service | 2026-04-30※ | 197 日 | — | `content/entries/service/B-18_aqua_voice[済].md` |
| B-26 | Azure OpenAI | service | 2026-04-30※ | 197 日 | モデル名 | `content/entries/service/B-26_azure_openai[済].md` |
| B-27 | Vertex AI | service | 2026-04-30※ | 197 日 | — | `content/entries/service/B-27_vertex_ai[済].md` |
| B-28 | Render | service | 2026-04-30※ | 197 日 | 価格／提供状況 | `content/entries/service/B-28_render[済].md` |
| B-29 | Supabase | service | 2026-04-30※ | 197 日 | — | `content/entries/service/B-29_supabase[済].md` |
| B-31 | Excalidraw | service | 2026-04-30※ | 197 日 | — | `content/entries/service/B-31_excalidraw[済].md` |
| B-32 | Figma | service | 2026-04-30※ | 197 日 | — | `content/entries/service/B-32_figma[済].md` |
| B-33 | Canva | service | 2026-04-30※ | 197 日 | 価格 | `content/entries/service/B-33_canva[済].md` |
| B-40 | Reddit | service | 2026-04-30※ | 197 日 | モデル名 | `content/entries/service/B-40_reddit[済].md` |
| B-41 | arXiv | service | 2026-04-30※ | 197 日 | モデル名 | `content/entries/service/B-41_arxiv[済].md` |
| B-60 | Suno | service | 2026-04-30※ | 197 日 | バージョン／価格 | `content/entries/service/B-60_suno[済].md` |
| B-61 | ACE-Step 1.5 | service | 2026-04-30※ | 197 日 | バージョン | `content/entries/service/B-61_ace_step_1_5[済].md` |
| C-11 | Z.ai | person_org | 2026-04-30※ | 197 日 | バージョン／時点表現 | `content/entries/person/C-11_z_ai[済].md` |
| C-13 | Groq | person_org | 2026-04-30※ | 197 日 | 価格 | `content/entries/person/C-13_groq[済].md` |
| D-35 | Cursor Composer | model | 2026-04-30※ | 197 日 | — | `content/entries/model/D-35_cursor_composer[済].md` |
| D-45 | GLM | model | 2026-04-30※ | 197 日 | モデル名／バージョン | `content/entries/model/D-45_glm[済].md` |
| D-53 | Veo | model | 2026-04-30※ | 197 日 | 時点表現 | `content/entries/model/D-53_veo[済].md` |
| D-55 | Nano Banana | model | 2026-04-30※ | 197 日 | モデル名／バージョン | `content/entries/model/D-55_nano_banana[済].md` |
| D-56 | Seedance | model | 2026-04-30※ | 197 日 | — | `content/entries/model/D-56_seedance[済].md` |
| D-57 | Flow | model | 2026-04-30※ | 197 日 | 価格 | `content/entries/model/D-57_flow[済].md` |
| D-58 | Whisk | model | 2026-04-30※ | 197 日 | — | `content/entries/model/D-58_whisk[済].md` |
| D-60 | AlphaGo | model | 2026-04-30※ | 197 日 | 時点表現 | `content/entries/model/D-60_alphago[済].md` |
| D-70 | Amical | model | 2026-04-30※ | 197 日 | — | `content/entries/model/D-70_amical[済].md` |
| E-23 | GSM8K | benchmark | 2026-04-30※ | 197 日 | — | `content/entries/benchmark/E-23_gsm8k[済].md` |
| E-24 | MATH | benchmark | 2026-04-30※ | 197 日 | 時点表現 | `content/entries/benchmark/E-24_math[済].md` |
| E-25 | AIME | benchmark | 2026-04-30※ | 197 日 | モデル名／時点表現 | `content/entries/benchmark/E-25_aime[済].md` |
| E-27 | IQ Bench | benchmark | 2026-04-30※ | 197 日 | — | `content/entries/benchmark/E-27_iq_bench[済].md` |
| E-31 | WebArena | benchmark | 2026-04-30※ | 197 日 | 時点表現 | `content/entries/benchmark/E-31_webarena[済].md` |
| E-32 | GAIA | benchmark | 2026-04-30※ | 197 日 | モデル名／時点表現 | `content/entries/benchmark/E-32_gaia[済].md` |
| E-33 | AgentBench | benchmark | 2026-04-30※ | 197 日 | バージョン／時点表現 | `content/entries/benchmark/E-33_agentbench[済].md` |
| E-34 | OSWorld | benchmark | 2026-04-30※ | 197 日 | モデル名／時点表現 | `content/entries/benchmark/E-34_osworld[済].md` |
| E-51 | LMSYS Arena | benchmark | 2026-04-30※ | 197 日 | モデル名／バージョン／時点表現 | `content/entries/benchmark/E-51_lmsys_arena[済].md` |
| F-170 | EC2 | term_tool | 2026-04-30※ | 197 日 | 価格 | `content/entries/term_tool/F-170_ec2[済].md` |
| F-171 | S3 | term_tool | 2026-04-30※ | 197 日 | バージョン | `content/entries/term_tool/F-171_s3[済].md` |
| G-16 | Embedding | term_llm | 2026-04-30※ | 197 日 | — | `content/entries/term_llm/G-16_embedding[済].md` |
| G-19 | Prompt Caching | term_llm | 2026-04-30※ | 197 日 | 価格 | `content/entries/term_llm/G-19_prompt_caching[済].md` |
| G-23 | .claude/settings.json | tool_agent | 2026-04-30※ | 197 日 | — | `content/entries/tool_agent/G-23_claude_settings_json[済].md` |
| G-34 | Code Interpreter | term_llm | 2026-04-30※ | 197 日 | — | `content/entries/term_llm/G-34_code_interpreter[済].md` |
| G-35 | Deep Research | term_llm | 2026-04-30※ | 197 日 | — | `content/entries/term_llm/G-35_deep_research[済].md` |
| G-36 | Artifact | term_llm | 2026-04-30※ | 197 日 | 時点表現／提供状況 | `content/entries/term_llm/G-36_artifact[済].md` |
| H-56 | Claude のバージョン史 | history | 2026-04-30※ | 197 日 | モデル名／バージョン／時点表現 | `content/entries/history/H-56_claude_version_history[済].md` |
| I-21 | Puppeteer MCP | mcp | 2026-04-30※ | 197 日 | 時点表現／提供状況 | `content/entries/mcp/I-21_puppeteer_mcp[済].md` |
| J-31 | 第 5 世代コンピュータ | term_general | 2026-04-30※ | 197 日 | — | `content/entries/term_general/J-31_fifth_generation_computer[済].md` |
| J-43 | SaaS | term_general | 2026-04-30※ | 197 日 | 価格／時点表現 | `content/entries/term_general/J-43_saas[済].md` |
| J-73 | Blackwell | term_general | 2026-04-30※ | 197 日 | 時点表現／提供状況 | `content/entries/term_general/J-73_blackwell[済].md` |
| J-74 | RTX シリーズ | term_general | 2026-04-30※ | 197 日 | — | `content/entries/term_general/J-74_rtx-series[済].md` |
| J-113 | 生成UIとagent-native設計 | term_general | 2026-06-23※ | 143 日 | — | `content/entries/term_general/J-113_generative_ui_agent_native[済].md` |
| B-34 | NotebookLM | service | 2026-08-10※ | 95 日 | — | `content/entries/service/B-34_notebooklm[済].md` |
| B-35 | Gemini CLI | service | 2026-08-10※ | 95 日 | モデル名／価格 | `content/entries/service/B-35_gemini_cli[済].md` |
| B-36 | Lovable | service | 2026-08-10※ | 95 日 | 提供状況 | `content/entries/service/B-36_lovable[済].md` |
| B-37 | Replit | service | 2026-08-10※ | 95 日 | 価格 | `content/entries/service/B-37_replit[済].md` |
| B-38 | Manus | service | 2026-08-10※ | 95 日 | — | `content/entries/service/B-38_manus[済].md` |
| B-39 | Google AI Studio | service | 2026-08-10※ | 95 日 | 価格 | `content/entries/service/B-39_google_ai_studio[済].md` |
| B-42 | Discord | service | 2026-08-10※ | 95 日 | — | `content/entries/service/B-42_discord[済].md` |
| B-43 | n8n・Dify | service | 2026-08-10※ | 95 日 | — | `content/entries/service/B-43_n8n_dify[済].md` |
| C-16 | DeepSeek | person_org | 2026-08-10※ | 95 日 | モデル名／時点表現 | `content/entries/person/C-16_deepseek[済].md` |
| D-59 | Midjourney | model | 2026-08-10※ | 95 日 | 価格／時点表現 | `content/entries/model/D-59_midjourney[済].md` |
| D-61 | AlphaFold | model | 2026-08-10※ | 95 日 | 時点表現 | `content/entries/model/D-61_alphafold[済].md` |
| E-28 | ARC-AGI | benchmark | 2026-08-10※ | 95 日 | — | `content/entries/benchmark/E-28_arc_agi[済].md` |
| G-17 | ベクトル DB | term_llm | 2026-08-10※ | 95 日 | — | `content/entries/term_llm/G-17_vector_db[済].md` |
| H-60 | Codex → GitHub Copilot の系譜 | history | 2026-08-10※ | 95 日 | モデル名／時点表現 | `content/entries/history/H-60_codex_to_copilot[人書].md` |
| J-116 | TPU | term_general | 2026-08-10※ | 95 日 | — | `content/entries/term_general/J-116_tpu[済].md` |

### Tier A（中） — 101 件（期限 180 日）

| ID | 用語 | category | 最終確認 | 経過 | 時変シグナル | path |
| :-- | :-- | :-- | :-- | --: | :-- | :-- |
| F-50 | git | term_tool | 2026-04-23※ | 204 日 | 時点表現 | `content/entries/term/F-50_git[済].md` |
| H-53 | ChatGPT 登場 | history | 2026-04-23※ | 204 日 | モデル名／バージョン／時点表現 | `content/entries/history/H-53_chatgpt_launch[済].md` |
| C-1 | OpenAI | person_org | 2026-04-25※ | 202 日 | モデル名／時点表現 | `content/entries/person/C-1_openai[済].md` |
| C-3 | Google DeepMind | person_org | 2026-04-29※ | 198 日 | 時点表現 | `content/entries/person/C-3_google_deepmind[済].md` |
| C-5 | xAI | person_org | 2026-04-29※ | 198 日 | 時点表現 | `content/entries/person/C-5_xai[済].md` |
| C-9 | NVIDIA | person_org | 2026-04-29※ | 198 日 | — | `content/entries/person/C-9_nvidia[済].md` |
| C-50 | Sam Altman | person_org | 2026-04-29※ | 198 日 | モデル名／時点表現 | `content/entries/person/C-50_sam_altman[済].md` |
| C-51 | Dario Amodei | person_org | 2026-04-29※ | 198 日 | 時点表現 | `content/entries/person/C-51_dario_amodei[済].md` |
| C-52 | Demis Hassabis | person_org | 2026-04-29※ | 198 日 | 時点表現 | `content/entries/person/C-52_demis_hassabis[済].md` |
| C-53 | Andrej Karpathy | person_org | 2026-04-29※ | 198 日 | 時点表現 | `content/entries/person/C-53_andrej_karpathy[済].md` |
| C-55 | Mira Murati | person_org | 2026-04-29※ | 198 日 | 時点表現 | `content/entries/person/C-55_mira_murati[済].md` |
| C-56 | Yann LeCun | person_org | 2026-04-29※ | 198 日 | 時点表現 | `content/entries/person/C-56_yann_lecun[済].md` |
| C-57 | Geoffrey Hinton | person_org | 2026-04-29※ | 198 日 | 時点表現 | `content/entries/person/C-57_geoffrey_hinton[済].md` |
| C-58 | Elon Musk | person_org | 2026-04-29※ | 198 日 | 時点表現 | `content/entries/person/C-58_elon_musk[済].md` |
| C-59 | Jensen Huang | person_org | 2026-04-29※ | 198 日 | 時点表現 | `content/entries/person/C-59_jensen_huang[済].md` |
| C-60 | Ray Kurzweil | person_org | 2026-04-29※ | 198 日 | 時点表現 | `content/entries/person/C-60_ray_kurzweil[済].md` |
| F-1 | JavaScript | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-1_javascript[済].md` |
| F-2 | TypeScript | term_tool | 2026-04-29※ | 198 日 | 時点表現 | `content/entries/term_tool/F-2_typescript[済].md` |
| F-3 | Python | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-3_python[済].md` |
| F-4 | HTML | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-4_html[済].md` |
| F-5 | CSS | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-5_css[済].md` |
| F-6 | Markdown | term_tool | 2026-04-29※ | 198 日 | 提供状況 | `content/entries/term_tool/F-6_markdown[済].md` |
| F-7 | YAML | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-7_yaml[済].md` |
| F-8 | JSON | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-8_json[済].md` |
| F-9 | SVG | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-9_svg[済].md` |
| F-10 | React | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-10_react[済].md` |
| F-11 | Next.js | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-11_next_js[済].md` |
| F-12 | Electron | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-12_electron[済].md` |
| F-13 | Tauri | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-13_tauri[済].md` |
| F-14 | three.js | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-14_three_js[済].md` |
| F-15 | shadcn/ui | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-15_shadcn_ui[済].md` |
| F-20 | ESLint | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-20_eslint[済].md` |
| F-21 | Prettier | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-21_prettier[済].md` |
| F-30 | VS Code | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-30_vs_code[済].md` |
| F-40 | npm | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-40_npm[済].md` |
| F-41 | Vite | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-41_vite[済].md` |
| F-44 | pnpm | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-44_pnpm[済].md` |
| F-51 | git push | term_tool | 2026-04-29※ | 198 日 | 時点表現 | `content/entries/term_tool/F-51_git_push[済].md` |
| F-52 | git pull | term_tool | 2026-04-29※ | 198 日 | 時点表現 | `content/entries/term_tool/F-52_git_pull[済].md` |
| F-53 | branch | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-53_branch[済].md` |
| F-54 | commit | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-54_commit[済].md` |
| F-55 | merge | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-55_merge[済].md` |
| F-56 | .gitignore | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-56_gitignore[済].md` |
| F-58 | git stash | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-58_git_stash[済].md` |
| F-59 | README.md | term_tool | 2026-04-29※ | 198 日 | 時点表現 | `content/entries/term_tool/F-59_readme_md[済].md` |
| F-61 | Pull Request | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-61_pull_request[済].md` |
| F-71 | ripgrep | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-71_ripgrep[済].md` |
| F-80 | Node.js | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-80_node_js[済].md` |
| F-81 | bash | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-81_bash[済].md` |
| F-82 | WSL | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-82_wsl[済].md` |
| F-83 | PowerShell | term_tool | 2026-04-29※ | 198 日 | バージョン／価格 | `content/entries/term_tool/F-83_powershell[済].md` |
| F-91 | .env | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-91_env[済].md` |
| F-120 | PostgreSQL | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-120_postgresql[済].md` |
| F-121 | SQLite | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-121_sqlite[済].md` |
| F-123 | ORM | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-123_orm[済].md` |
| F-130 | OAuth | term_tool | 2026-04-29※ | 198 日 | — | `content/entries/term_tool/F-130_oauth[済].md` |
| H-1 | TDD | workflow | 2026-04-29※ | 198 日 | — | `content/entries/workflow/H-1_tdd[済].md` |
| H-7 | CI/CD | workflow | 2026-04-29※ | 198 日 | — | `content/entries/workflow/H-7_ci_cd[済].md` |
| H-54 | GPT-4 リリース | history | 2026-04-29※ | 198 日 | モデル名／バージョン／時点表現 | `content/entries/history/H-54_gpt4_release[済].md` |
| H-58 | Transformer 論文 | history | 2026-04-29※ | 198 日 | モデル名／バージョン／時点表現 | `content/entries/history/H-58_transformer_paper[済].md` |
| C-12 | TSMC | person_org | 2026-04-30※ | 197 日 | — | `content/entries/person/C-12_tsmc[済].md` |
| C-14 | AMD | person_org | 2026-04-30※ | 197 日 | — | `content/entries/person/C-14_amd[済].md` |
| C-80 | AI大学 | person_org | 2026-04-30※ | 197 日 | 価格 | `content/entries/person/C-80_ai_daigaku[済].md` |
| C-81 | にゃんた | person_org | 2026-04-30※ | 197 日 | — | `content/entries/person/C-81_nyanta[済].md` |
| C-82 | まさお | person_org | 2026-04-30※ | 197 日 | モデル名 | `content/entries/person/C-82_masao[済].md` |
| F-16 | Tailwind CSS | term_tool | 2026-04-30※ | 197 日 | — | `content/entries/term_tool/F-16_tailwind_css[済].md` |
| F-17 | Astro | term_tool | 2026-04-30※ | 197 日 | — | `content/entries/term_tool/F-17_astro[済].md` |
| F-35 | Markdown Preview Enhanced | term_tool | 2026-04-30※ | 197 日 | 提供状況 | `content/entries/term_tool/F-35_markdown_preview_enhanced[済].md` |
| F-36 | Git Graph | term_tool | 2026-04-30※ | 197 日 | — | `content/entries/term_tool/F-36_git_graph[済].md` |
| F-37 | Japanese Language Pack for VS Code | term_tool | 2026-04-30※ | 197 日 | — | `content/entries/term_tool/F-37_japanese_language_pack_for_vs_code[済].md` |
| F-38 | Markdown All in One | term_tool | 2026-04-30※ | 197 日 | 提供状況 | `content/entries/term_tool/F-38_markdown_all_in_one[済].md` |
| F-42 | ビルド | term_tool | 2026-04-30※ | 197 日 | — | `content/entries/term_tool/F-42_build[済].md` |
| F-43 | テスト | term_tool | 2026-04-30※ | 197 日 | — | `content/entries/term_tool/F-43_test[済].md` |
| F-84 | Ghostty | term_tool | 2026-04-30※ | 197 日 | 提供状況 | `content/entries/term_tool/F-84_ghostty[済].md` |
| F-85 | SuperClaude Framework | term_tool | 2026-04-30※ | 197 日 | — | `content/entries/term_tool/F-85_superclaude_framework[済].md` |
| F-86 | ollama | term_tool | 2026-04-30※ | 197 日 | モデル名 | `content/entries/term_tool/F-86_ollama[済].md` |
| F-87 | sudo | term_tool | 2026-04-30※ | 197 日 | — | `content/entries/term_tool/F-87_sudo[済].md` |
| F-100 | 拡張子早見表 | term_tool | 2026-04-30※ | 197 日 | — | `content/entries/term_tool/F-100_file_extensions_guide[済].md` |
| F-101 | .ico | term_tool | 2026-04-30※ | 197 日 | — | `content/entries/term_tool/F-101_ico[済].md` |
| F-102 | .mp4 | term_tool | 2026-04-30※ | 197 日 | — | `content/entries/term_tool/F-102_mp4[済].md` |
| F-103 | .mp3 | term_tool | 2026-04-30※ | 197 日 | — | `content/entries/term_tool/F-103_mp3[済].md` |
| F-104 | .webp | term_tool | 2026-04-30※ | 197 日 | 時点表現／提供状況 | `content/entries/term_tool/F-104_webp[済].md` |
| F-110 | Lighthouse | term_tool | 2026-04-30※ | 197 日 | バージョン | `content/entries/term_tool/F-110_lighthouse[済].md` |
| F-111 | a11y | term_tool | 2026-04-30※ | 197 日 | — | `content/entries/term_tool/F-111_a11y[済].md` |
| F-140 | Mermaid | term_tool | 2026-04-30※ | 197 日 | — | `content/entries/term_tool/F-140_mermaid[済].md` |
| F-141 | PlantUML | term_tool | 2026-04-30※ | 197 日 | 時点表現 | `content/entries/term_tool/F-141_plantuml[済].md` |
| F-151 | Apache 2.0 | term_tool | 2026-04-30※ | 197 日 | バージョン | `content/entries/term_tool/F-151_apache_2_0[済].md` |
| F-152 | GPL | term_tool | 2026-04-30※ | 197 日 | バージョン | `content/entries/term_tool/F-152_gpl[済].md` |
| F-153 | Creative Commons | term_tool | 2026-04-30※ | 197 日 | バージョン／提供状況 | `content/entries/term_tool/F-153_creative_commons[済].md` |
| F-154 | OSS | term_tool | 2026-04-30※ | 197 日 | モデル名／バージョン | `content/entries/term_tool/F-154_oss[済].md` |
| F-160 | DOM | term_tool | 2026-04-30※ | 197 日 | — | `content/entries/term_tool/F-160_dom[済].md` |
| F-161 | SSR | term_tool | 2026-04-30※ | 197 日 | — | `content/entries/term_tool/F-161_ssr[済].md` |
| F-162 | SSG | term_tool | 2026-04-30※ | 197 日 | — | `content/entries/term_tool/F-162_ssg[済].md` |
| F-172 | IAM | term_tool | 2026-04-30※ | 197 日 | — | `content/entries/term_tool/F-172_iam[済].md` |
| F-180 | OpenGL | term_tool | 2026-04-30※ | 197 日 | — | `content/entries/term_tool/F-180_opengl[済].md` |
| F-181 | WebGL | term_tool | 2026-04-30※ | 197 日 | — | `content/entries/term_tool/F-181_webgl[済].md` |
| F-190 | サブルーチン | term_tool | 2026-04-30※ | 197 日 | — | `content/entries/term_tool/F-190_subroutine[済].md` |
| F-200 | Rust | term_tool | 2026-04-30※ | 197 日 | — | `content/entries/term_tool/F-200_rust[済].md` |
| H-5 | Scrum / Agile | workflow | 2026-04-30※ | 197 日 | — | `content/entries/workflow/H-5_scrum_agile[済].md` |
| H-6 | Git Flow | workflow | 2026-04-30※ | 197 日 | 時点表現 | `content/entries/workflow/H-6_git_flow[済].md` |
| H-8 | DevOps | workflow | 2026-04-30※ | 197 日 | — | `content/entries/workflow/H-8_devops[済].md` |

### Tier B（低） — 0 件（期限 365 日）

_なし_

※ = `last_audited` が未記入で `evaluation_date` を代用しているもの。

---

## 4. 確認すべき本文行（Tier S の期限超過）

エントリを開かなくても「どこを見ればいいか」が分かるように、時変シグナルに当たった行を 1 種類につき 1 行だけ抜いています。

**B-1 Gemini**（203 日経過）

- `モデル名` Gemini 2.5 系、Vertex AI、AI Studio、Workspace 個別機能。
- `時点表現` Google が提供する AI アシスタントのブランド。2024 年に Bard から改名しました。

**B-3 ChatGPT**（202 日経過）

- `モデル名` ChatGPT というブランドの下に、アプリ・カスタム GPT・API という 3 つの入口があることと、それを支えるモデル（GPT-5 系）の関係を 1 枚で示します。

**B-4 Cursor**（198 日経過）

- `価格` 無料枠に月あたりの使用上限があり超過すると有料プランが必要です。

**B-5 GitHub Copilot**（198 日経過）

- `価格` VS Code や JetBrains など既存エディタに拡張として追加して使います。GitHub アカウントでサインインするのが前提で、個人向けの無料枠もあります。

**B-9 v0**（198 日経過）

- `提供状況` 「カード一覧を作って」と入力すると、ブラウザで動く React コンポーネントを生成します。プレビューをその場で確認し、コードをプロジェクトへ貼り付けて使えます。

**B-11 Bolt.new**（198 日経過）

- `価格` 無料枠の月次トークン上限を超えると有料プランへの切り替えが必要です。
- `提供状況` プロンプトを入れてからプレビューが出るまでのワンフローを、左から右に流れる形で示します。

**B-12 Perplexity**（198 日経過）

- `時点表現` - シーン1: 担当者が「〇〇の現在の価格は？」と入力する

**B-20 Vercel**（198 日経過）

- `提供状況` push で URL が出る流れとプレビュー・本番の 2 段階を押さえます。

**B-21 Netlify**（198 日経過）

- `価格` 無料枠で個人サイトが立ち、設定ファイルも最小限で済みます。

**B-22 Cloudflare**（198 日経過）

- `価格` 無料プランで CDN と DDoS 対策が使えます。

**B-30 Amazon Bedrock**（198 日経過）

- `モデル名` - 周辺の要素: Claude（Anthropic）／Llama（Meta）／Titan（Amazon）／Mistral／利用アプリ

**B-51 ChatGPT の料金プラン**（198 日経過）

- `モデル名` ChatGPT、OpenAI、API、GPT-5。
- `価格` Free から Pro（$200/月）まで 5 段階で選べる ChatGPT の利用プランです。

**B-52 Gemini の料金プラン**（198 日経過）

- `モデル名` 「Google AI Pro に入ると Gemini 2.5 Pro が使えるようになりますよね。」

**C-6 Mistral AI**（198 日経過）

- `モデル名` オープンウェイトモデルと商用 API を提供します。Mistral 7B・Mixtral 8x7B を Apache 2.0 で公開し、ローカル利用も可能です。

**C-7 Hugging Face**（198 日経過）

- `モデル名` Llama や Mistral などのオープンモデルを探すとき、最初に行き着く場所です。transformers ライブラリは Python で AI を扱う事実上の標準で、コード…
- `時点表現` - 中心に置く概念: Hugging Face（2016 年設立）

**D-26 gpt-oss**（198 日経過）

- `モデル名` GPT-4o 系のクローズドモデルより性能は下で、GPU 環境が必要です。
- `バージョン` OpenAI が 2025-08 に Apache 2.0 で公開したモデルです。20B・120B の 2 サイズがあり、手元で推論できます。

**D-41 Mistral 系**（198 日経過）

- `モデル名` 仏 Mistral AI が開発するテキスト生成モデル群です。Mixtral（MoE 構造）を含む軽量〜高性能の複数版があり、多くが Apache 2.0 で公開されています。
- `バージョン` 欧州発のオープンモデル代表。Apache 2.0 で自由に使えます。

**D-43 Qwen 系**（198 日経過）

- `モデル名` ローカル LLM の選択肢やアジア言語タスクを調べる場面で名前が出ます。Qwen 2.5・Qwen 3 は Hugging Face のダウンロード数上位に入り、オープンモデル比較…
- `時点表現` Qwen 2.5 が安定した実績版、Qwen 3 が最新世代という世代感が要点です。

**D-47 DeepSeek R1**（198 日経過）

- `モデル名` 2025 年 1 月、o1 系と同等の推論性能をオープンウェイトで達成し「DeepSeek ショック」と呼ばれました。deepseek.com の API や Hugging Fa…

**D-50 DALL-E**（198 日経過）

- `時点表現` - DALL-E 1（2021年1月）：テキストから画像生成の概念実証。品質はまだ荒削り

**D-52 Sora**（198 日経過）

- `提供状況` - 2024-02：Sora 発表（研究プレビュー）— テキスト→動画の衝撃デモが公開

**D-54 Stable Diffusion**（198 日経過）

- `バージョン` SD 1.4 から SD3.5・Flux 系まで世代を追い、「ウェイト公開のモデルがどう進化してきたか」を一目で捉えてもらいます。

**D-71 Whisper**（198 日経過）

- `バージョン` OpenAI が公開した音声認識モデルです。99 言語に対応し、Apache 2.0 ライセンスで無償利用できます。

**E-4 HumanEval**（198 日経過）

- `時点表現` - 関係の描き方: 左から右への一本線フロー。右端に「最新モデルは 90%+ 帯」のスコアバーを小さく添える

**E-20 MMLU**（198 日経過）

- `モデル名` - GPT-4
- `バージョン` 4 カテゴリの傘と、人間水準 89.8% という比較軸を把握します。

**E-21 MMLU-Pro**（198 日経過）

- `バージョン` MMLU、GPQA、arXiv:2406.01574
- `時点表現` 3. スコアの水準を把握 — 70% 台が現在のトップクラスの目安と知る
- `提供状況` 14 分野の問題を 10 択形式で出し、AI が推論してどれだけ正確に答えられるかを測ります。MMLU（4 択）が多くのモデルで 90% 以上に達し飽和したため、難化させた後継指標…

**E-22 GPQA**（198 日経過）

- `モデル名` o1 や o3 などの reasoning（推論特化）モデルが台頭したころ、その実力を示す指標として注目されました。モデル発表資料や論文比較表で GPQA Diamond（最難サブ…
- `バージョン` MMLU-Pro、o1、arXiv:2311.12022

**I-24 Context7 MCP**（198 日経過）

- `時点表現` - 視覚要素: プロンプト（`use context7`）→ Context7 MCP → 公式ドキュメント → 現在の API の回答

**J-72 H100**（198 日経過）

- `モデル名` GPT-4 や Claude 3 などの LLM 学習ニュースで「H100 数万枚」という表現を目にします。AWS p5・GCP A3 などのクラウド GPU インスタンスで時間貸…

**B-6 Windsurf**（197 日経過）

- `時点表現` Codeium が 2024 年 11 月に公開した AI コードエディタ。Cascade が複数ファイルを横断編集します。

**B-8 Codex**（197 日経過）

- `時点表現` 旧 Codex（2021 年エンジン）と同名のため記事の年代に注意が必要です。

**B-14 Genspark**（197 日経過）

- `価格` 料金・機能は時変情報で、無料枠の制限は変わることがあります。

**B-16 Microsoft 365 Copilot**（197 日経過）

- `価格` Word・Excel・Teams などに組み込まれた業務統合 AI です。月額 $30 の有料追加サービスになります。

**B-26 Azure OpenAI**（197 日経過）

- `モデル名` GPT-4o や o1 などの OpenAI モデルを、Azure のインフラ上で API として呼び出せるようにします。データが指定リージョン内に留まるため、情報管理の要件が厳し…

**B-28 Render**（197 日経過）

- `価格` 無料プランは一定時間で休止し、常時稼働には有料プランが必要です。
- `提供状況` - シーン2: PR を出すとプレビュー環境が自動生成され、URL が届く

**B-33 Canva**（197 日経過）

- `価格` 無料プランの範囲とテンプレート操作の流れを把握します。

**B-40 Reddit**（197 日経過）

- `モデル名` - シーン2: 開発者が r/LocalLLaMA で Llama 4 の実機ベンチを確認している

**B-41 arXiv**（197 日経過）

- `モデル名` Transformer 論文（J-13）や GPT・DeepSeek 系の技術報告など、話題の論文の出所として名前を見かけます。Hugging Face Papers や Pape…

**B-60 Suno**（197 日経過）

- `バージョン` ElevenLabs、ACE-Step 1.5、Sora
- `価格` 商用利用の可否はプランで異なり、無料プランは個人利用に限定されます。

**B-61 ACE-Step 1.5**（197 日経過）

- `バージョン` テキストプロンプトからボーカル付きの楽曲を生成します。多言語の歌詞に対応し、ステム分離やスタイル変換も行えます。Apache 2.0 ライセンスで商用利用が可能です。

**C-11 Z.ai**（197 日経過）

- `バージョン` 「Z.ai の GLM-4.6、ローカルで動かすと意外と速いです。」
- `時点表現` Hugging Face で GLM モデルを検索するとヒットします。中国系 LLM 記事では「六小虎」の一角として登場します。2025 年 1 月に米国制裁リスト（Entity …

**C-13 Groq**（197 日経過）

- `価格` 2. API 選定 — GroqCloud の無料枠で速度・料金を OpenAI 互換 API と比較します

**D-45 GLM**（197 日経過）

- `モデル名` DeepSeek V3、Qwen、CodeGeeX
- `バージョン` Hugging Face でオープンウェイト版が公開されており、ローカル GPU で動かす構成を試みる際に名前を見かけます。Cursor や Roo Code などのエディタ連携で…

**D-53 Veo**（197 日経過）

- `時点表現` テキスト・画像・既存動画を入力として、リアルな質感とカメラワークを持つ動画を生成します。Veo 3（2025 年）では環境音・対話・効果音まで含む音声付き動画を出力できます。

**D-55 Nano Banana**（197 日経過）

- `モデル名` 画像の構図を崩さず衣装・背景・追加要素だけを差し替えます。正式名称は Gemini 2.5 Flash Image で、LMArena の画像評価で上位を維持しています。

**D-57 Flow**（197 日経過）

- `価格` AI Pro 以上の有償プランが必要で、無料枠はありません。

**D-60 AlphaGo**（197 日経過）

- `時点表現` Google DeepMind が開発した囲碁 AI です。2016 年にトップ棋士を破り「AI が人間を超えた」と知られます。

**E-24 MATH**（197 日経過）

- `時点表現` 2021 年公開の数学ベンチマークです。代数・幾何・数論・確率など 7 分類 12,500 問を収録し、最終回答を照合して正答率を算出します。

**E-25 AIME**（197 日経過）

- `モデル名` 「AIME 2024 で o3 系が満点近かった、と Twitter で話題になっていましたね。」
- `時点表現` - シーン2: 2024・2025 年版（AIME I/II）が LLM ベンチ比較で標準的に使われる

**E-31 WebArena**（197 日経過）

- `時点表現` カーネギーメロン大学が 2023 年に発表したベンチマークです。Docker で再現した 5 種の擬似 Web サイトに自然言語タスク 812 個を与え、AI エージェントの完了率…

**E-32 GAIA**（197 日経過）

- `モデル名` AI エージェントのリリース記事や研究論文で「GAIA スコア」として登場します。公開時は GPT-4 約 15%・人間約 92%、2025 年には上位勢が 60% 台に到達してい…
- `時点表現` Meta（C-4）と Hugging Face（C-7）が 2023 年末に公開した、AI エージェントの実用能力を測る問題集です。Web 検索・PDF 読解・画像理解など複数ツー…

**E-33 AgentBench**（197 日経過）

- `バージョン` 「AgentBench の OS 環境で GLM-4.6 が伸びていました。」
- `時点表現` OS 操作や DB、Web ショッピングなど 8 環境のマルチターン課題を LLM に解かせ、チャット応答ではなく実行力を数値化します。清華大学・Z.ai が 2023 年に公開し…

**E-34 OSWorld**（197 日経過）

- `モデル名` Computer Use の性能比較記事で登場します。公開時は GPT-4V 約 12% に対し人間 約 72% でしたが、Computer Use や Operator の登場で…
- `時点表現` 2024 年 4 月公開のベンチマークで、実 OS 環境で 369 タスクの到達度を測ります。スクリーンショットを入力してキーやマウス操作で答える形が特徴です。

**E-51 LMSYS Arena**（197 日経過）

- `モデル名` 「LMSYS Arena で Gemini 2.5 Pro が 1 位に上がってきました。」
- `時点表現` - シーン1: LMSYS（2023 年）が Chatbot Arena を公開。UC Berkeley 発の研究基盤として注目を集める

**F-170 EC2**（197 日経過）

- `価格` Amazon Elastic Compute Cloud の略。AWS 上で仮想マシンを従量課金で借りられるサービスです。

**F-171 S3**（197 日経過）

- `バージョン` ファイルを「バケット」に保存し URL やキーで取り出せるストレージです。公称耐久性は 99.999999999%（イレブン・ナイン）とされ、設計上はきわめて失われにくい水準です。

**G-19 Prompt Caching**（197 日経過）

- `価格` - うれしさ: 月額が 30〜40% 削減できることがあります

**G-36 Artifact**（197 日経過）

- `時点表現` Claude.ai でコードや文書を生成すると、会話欄とは別の右側パネルに成果物が表示されます。パネル内で直接編集でき、ファイル単位で履歴が残るため、会話を遡らずに最新版を確認でき…
- `提供状況` - シーン2: HTML プレビューを確認しながら会話で修正指示を出す

**H-56 Claude のバージョン史**（197 日経過）

- `モデル名` Claude 3 系、Claude 4 系、Extended Thinking
- `バージョン` 「Extended Thinking は 3.7 Sonnet から搭載されました。」
- `時点表現` Anthropic が 2023 年以降リリースしてきた Claude シリーズの版数と命名変遷をまとめます。

**I-21 Puppeteer MCP**（197 日経過）

- `時点表現` かつては MCP 公式の参照サーバーの 1 つでしたが、2025 年 5 月に保守対象から外れ、アーカイブ用のリポジトリへ移りました。いまブラウザ操作を任せるなら Playwrig…

**J-43 SaaS**（197 日経過）

- `価格` 月額費用が積み重なるため、複数契約時の総コストに注意が必要です。
- `時点表現` - 視覚要素: ブラウザ → クラウドサーバー → 常に最新版

**J-73 Blackwell**（197 日経過）

- `時点表現` NVIDIA が 2024 年 3 月に発表した GPU アーキテクチャ世代で、Hopper（H100）の後継です。

**B-35 Gemini CLI**（95 日経過）

- `モデル名` 無料枠のままでも Gemini 3 系を試せます。
- `価格` Claude Code（B-7）や Codex（B-8）と並んで比較記事に登場する、無料で試しやすいターミナル型エージェントです。Google アカウントでログインするだけで、無料…

**B-36 Lovable**（95 日経過）

- `提供状況` 3. プレビュー確認 — ブラウザ上で動作を見ながら直します

**B-37 Replit**（95 日経過）

- `価格` 料金は使った分に応じて変わる従量課金へ移行しています。

**B-39 Google AI Studio**（95 日経過）

- `価格` - 周辺の要素（3〜6個）: プロンプト入力欄、応答表示、画像・音声の添付、API キー発行ボタン、無料枠の表示

**C-16 DeepSeek**（95 日経過）

- `モデル名` API 価格の安さを伝えるニュースや、2025 年 1 月の市場の動揺（DeepSeek ショック）を振り返る記事で社名を目にします。オープンウェイトモデルの比較記事でも名前が挙が…

**D-59 Midjourney**（95 日経過）

- `価格` 無料枠がなく、月額プランへの加入が必須です。
- `時点表現` 文章の指示文（プロンプト）を送ると、絵として整った質感の高い画像を生成します。もともとは Discord 上でコマンドを打って使う形式で広まり、現在は Web 版でも操作できます。

**D-61 AlphaFold**（95 日経過）

- `時点表現` タンパク質の立体構造を予測する AI です。2024 年のノーベル化学賞につながりました。

**H-60 Codex → GitHub Copilot の系譜**（95 日経過）

- `モデル名` Codex という名前は 2021 年と 2025 年で 2 回登場しました。1 回目は GPT-3 をコード向けに追加学習したモデル、2 回目は自分で作業を進めるコーディングエー…
- `時点表現` 同じ「Codex」でも 2021 年と 2025 年で中身が違う名前の物語です。

---

## 使い方

1. §2 で束を選ぶ（モデル → サービス → ベンチマーク → MCP の順が安いです）
2. §4 の該当行を見ながら一次情報（公式ドキュメント・料金ページ）を確認する
3. **変更が無かった場合**: frontmatter の `last_audited` を確認日に更新するだけで完了です。`evaluation_date` は執筆時点の記録なので動かしません
4. **変更があった場合**: 本文を直し、出典メモの `checked YYYY-MM-DD` も合わせ、`last_audited` を更新します。本文の改訂は entry-writer サブエージェントに渡せます
5. 監査した範囲と結果は [freshness_audit_log.md](freshness_audit_log.md) に 1 行追記してください

「最新モデル名」「ChatGPT の月額」のように、**1 つ変わると複数エントリが同時に古くなる事実**は、エントリ側から巡回すると取りこぼします。[volatile_facts.md](volatile_facts.md) に事実側の台帳があるので、そちらから影響エントリを引いて束で直す方が速いです。

Tier の判定が実態と合わないときは、frontmatter に `volatility: high | mid | low` を足すと上書きできます（[docs/entry_schema.yaml](../docs/entry_schema.yaml) 参照）。
