# 次セッションへの引き継ぎ（2026-08-10 v12 更新）

## 2026-08-10 セッション成果 — 収録語の抜け監査 34 本を本書き

[docs/design_improvement_proposal_2026-08.md](../docs/design_improvement_proposal_2026-08.md) §4 の追加候補（☆☆☆ 15 件・☆☆ 20 件）を全部書きました。エントリ総数は 364 → 398 件です。

- 事実確認メモ：[ledgers/stage3_briefs_2026-08.md](stage3_briefs_2026-08.md)（各語の「押さえる事実 ＋ 出典 URL ＋ 書かないこと」。すべて 2026-08-10 に web で確認）
- 確定 ID と仮 ID からの変更理由：[ledgers/entry_candidates.md](entry_candidates.md) の「M 差分（2026-08-10）」
- 新規 34 本はすべて `status: needs_review`（☆違反 0・警告 0）。**著者欄（非エンジニアのつまずき／私のコメント）の記入待ち**です
- **F-43 テスト**：提案書は「欠番」としていましたが、実際には v2 テンプレで本書き済み・著者コメントまで入ったエントリが `status: archived` で凍結されていました。取りこぼしと判断して `ready` に戻しています（意図的な凍結だった場合は差し戻してください）
- **G-27 プロンプトインジェクション**：当初 G-37（Cursor Composer 移設で空いた欠番）に置きましたが、著者判断で G-27 へ移動しました。G-37 は欠番のままです
- `scripts/generate_skeleton.py` が `ledgers/entries.csv` を CRLF で書き戻していたのを修正（`lineterminator="\n"`。`sync_entries_csv.py` は元から LF 指定でした）

### 著者欄の対話転記（2026-08-10 開始・途中まで）

音声口述 → Claude 転記の形式で、新規 34 本のうち **6 本まで進みました**。続きは 7 本目（F-47 フロントエンド／バックエンド）から。

| ID | タイトル | 状態 |
| :-- | :-- | :-- |
| G-49 | AI エージェント | つまずき・コメント 記入済み |
| F-213 | API | 記入済み |
| F-214 | API キー | 記入済み |
| F-45 | デプロイ | 記入済み |
| F-46 | デバッグ | 記入済み |
| F-18 | フレームワーク／ライブラリ | つまずき・第一印象のみ。**良い点／ダメな点／誰向けか が空欄** |

転記の進め方（今回確立した手順）：

1. エントリ 1 本につき 1 問。tagline を提示して「つまずき ＋ 第一印象／良い点／ダメな点／誰向けか」を口述してもらう
2. 口述のトーン（「〜だよね」等）はそのまま残して転記する。誌面文体には整えない
3. 音声認識の崩れ（`.env` → 「電武器」、従量課金 → 「十六金」など）は文脈で補い、補ったことを本人に伝えて確認する
4. 1 本ごとに validator を通し、コミット・プッシュする

**F-18 の副産物**：著者本人が tagline「制御の向きが逆です」を読んで意味が取れなかったため、平易な言い回しへ差し替えました（コミット `a37d9f5`）。**著者に読んでもらうと tagline の伝わらなさが検出できる**ので、他エントリでも同じことが起きたら遠慮なく直すのが良さそうです。

### 次にやること（このセッションで見つかった宿題）

1. **著者欄の記入**：新規 34 本のうち残り 28 本（＋ F-18 の 3 項目）と既存分。`cat ledgers/revision_queue.md` の「著者レビュー待ち」から
2. **台帳にあるのにファイルが無い 35 件**：`ledgers/entries.csv` に行はあるのに `path` 列が空＝**一度も生成されていないエントリが 35 件**あります（`C-83 / D-3 / D-10 / D-13 / D-23 / F-34 / F-57 / F-150 / F-210 JSON Schema / F-211 Zod / F-212 OpenAPI / G-8 / G-9 / G-17 / G-45 / G-48 / H-2 / H-3 / H-4 / H-50 / H-51 / H-52 / H-57 / H-59 / H-60 / H-61 / H-62 / H-63 / I-80 / I-81 / J-22 / J-32 / J-50 / J-55 / J-62`）。notes に「v2テンプレ本書き済」と書かれている行も含まれますが、実ファイルは存在しません。今回追加した G-49 AI エージェントが H-59「AI エージェント元年」を、F-213 API が F-212 OpenAPI を参照できなかった原因もこれです。**次セッションの最有力候補**
3. **CSV と実ファイルの status 乖離 47 件**：`ledgers/entries.csv` の status 列が実ファイルの YAML と食い違う行が 47 件あります（例：F-60 GitHub は CSV `needs_review` ／ ファイル `ready`）。`sync_entries_csv.py` は path 列しか同期しないため、status も同期するか、CSV 側を正とするかの方針決めが要ります

## 2026-05-23 セッション成果

### Cloudflare Pages デプロイ
- 管理トップ `drafts/index.html` を新設（全 334 HTML ページへのリンク一覧、検索付き）
- `scripts/generate_site_index.py` でいつでも再生成可能
- `scripts/build_site.sh` を Cloudflare Build command に設定（preview_gen + 画像コピー + index 生成）
- カスタムドメイン `vibe.zealbootcamp.com` を設定中（DNS 伝播待ち）
- Build output directory: `drafts`

### 著者記入欄 対話入力（23 件完了）
音声口述 → Claude 転記の対話形式で進めた。コミット `cf9ba7d`・`865f2fb`・`3321490`。

| グループ | 完了件数 | エントリ |
| :-- | --: | :-- |
| B 群（ツール） | 8 件 | B-1, B-6〜B-12 |
| C 群（人物・企業） | 4 件 | C-6, C-10, C-11, C-50 |
| D 群（モデル系統） | 11 件 | D-1,2,4,11,12,14,20,21,22,24,70 |

### 著者記入 残り 50 件（`ledgers/author_fill_queue.md` に一覧）
- A 群 11 件（前付け：まえがき・凡例類）
- E 群 5 件（ベンチマーク系）
- F 群 31 件（基盤技術：最多）
- G 群 2 件
- J 群 1 件

次セッションは `ledgers/author_fill_queue.md` を開いて続きから。
対話形式（音声口述 → Claude 転記）で進める。

---

# 次セッションへの引き継ぎ（2026-04-30 v10 更新 / 累計 245 件本書き完走）

*2026-04-29〜2026-04-30 にかけて、`entry-writer` 5 並列 × 49 バッチ で letter 横断 245 件を本書き。skeleton 305 → 42（−263）、drafting → 263、needs_review → 39、archived 8 → 23、☆ 違反 0 で着地。残スケルトン約 42 件。次セッションはこのファイルの「2026-04-30 セッション成果」を確認し、残り 42 件のうち 30 件束を `entry-writer` で進めるか、needs_review に積まれた 39 件の著者欄記入に進むか選んでください。*

## 2026-05-14 追記: 本文見開きの PDF 実寸調整

Claude に作業を渡すための専用メモを追加しました。

- 引き渡し文書: [docs/claude_layout_handoff.md](../docs/claude_layout_handoff.md)
- 課題: validator 上は通っても、PDF 実寸では B 章以降の通常エントリ下部が切れることがある
- 方針: A 章ではなく TypeScript 見本を基準に、CSS で押し込まず Markdown 原稿を短くする
- PDF 前提: 片ページ `199mm × 281mm`、1 エントリ 2 ページ
- 最初の対象候補: `B-3 ChatGPT` を TypeScript 見本程度の密度に調整し、そこを基準稿にする

重要: `overflow: hidden` で切れを隠して 2 ページ扱いにするのは禁止。PDF を開いて下部のチロム、開発フロー、関連用語、参考 URL まで見えるか目視してください。

## 2026-04-30: 並列 150 件本書きラウンド（5 並列 × 30 バッチ × 6 ラウンド）

### コミット 6 本（古い順）

- `6b1b0f4` write 30 more stage-3 entries (I/C/J across batches 19-24): I-MCP・C-人物・J-概念
- `0a720fd` write 30 more stage-3 entries (F across batches 25-30): F-言語・UI・git・ランタイム・DB・図/OSS
- `2cbebf3` write 30 more stage-3 entries (B/D across batches 31-36): B-AI ツール・Copilot・クラウド・コミュニティ・D-モデル
- `72757c0` write 30 more stage-3 entries (E/H/I/C/J/G across batches 37-42): E-ベンチマーク・H ワークフロー・I MCP・C 企業・J 概念・G LLM
- `5882ca0` write 30 more stage-3 entries (F/J across batches 43-48): F-VS Code 拡張・CLI・ライセンス・メディア・AWS・GL・J-ストレ・OS
- `52905cd` write 30 more stage-3 entries (A/G/F/H/J across batches 49-54): A メタ全 9 件 + untracked 12 件 + 主要残 9 件

### 書いた 150 件の内訳（batches 19-54）

| ラウンド | 内容 | 件数 |
| :-- | :-- | --: |
| batches 19-24 | I-MCP 10 / C-人物 7 / C-組織 3 / J-概念 8 / 補助 2 | 30 |
| batches 25-30 | F-言語/形式 5 / UI/Linter 5 / git ファイル系 5 / ランタイム/端末 5 / DB 系 5 / 図/OSS 5 | 30 |
| batches 31-36 | B-AI ツール 5 / Copilot 5 / クラウド・PaaS 5 / コミュニティ 5 / D-モデル 10 | 30 |
| batches 37-42 | E-ベンチ前後半 10 / H 系 3 / I-21 / C-企業 4 / J-概念 8 / G-LLM 4 | 30 |
| batches 43-48 | F-VS Code 拡張 4 / 端末 1 / CLI/Web 品質 4 / ライセンス・アイコン・メディア・レンダリング 10 / AWS 3 / GL 2 / J-OS/ストレージ 6 | 30 |
| batches 49-54 | A メタ全 9 / untracked 12（G-15〜19, G-38, G-39, G-47, F-16, F-17, F-200, H-63）/ 主要残 9 | 30 |

詳細は各コミットメッセージを参照。

### 並列実行の知見（前セッションから継続蓄積）

1. **5 並列 × N バッチが安定**：今回 batch30（F-86 ollama 含む）で 5 並列が API タイムアウトで全件失敗 → 単発で再投げて完走。同時に長時間処理が走ると API 側が切れることがあるので、再投げ前提で進めるとよい
2. **status は Python ワンライナーで一括変更**（前 v9 と同じ）。スケルトンテンプレ内コメントに `status: skeleton` が複数あるので必ずフロントマター 1 つだけを置換する正規表現（`^status: skeleton\s*$` + flags=MULTILINE + count=1）を使う
3. **頻発した ☆ 違反パターン**（合計 13 件発生・全件その場で並列トリム解消）
   - 左ページ合計 +100 字超過：C-54 / I-4 / I-5 / I-41 / F-160 / F-91 / I-21 / F-110 / F-16（開発フロー過大）
   - 「非エンジニアのつまずき」欄に AI 記入混入（`- -` のままになる）：I-5 / F-62 / B-40 / H-5
   - entry-writer に「左ページ合計 250 字以内」「つまずき欄は空のまま」を毎回プロンプトで強調しているが、再発するので保存後の validator チェックは必須
4. **新ファイル名分離**：J-19 → J-19_quantization、J-2 → J-2_strong_weak_ai のように entry-writer が新ファイル名で書くケースあり。entries.csv の path も自動更新され、旧スケルトンは archived 化される。実害なし。D-43_qwen / D-54_stable_diffusion なども同様
5. **連体修飾の「だ」 validator 誤検出**（前 v9 と同じ）。「進んだ N 本」→「進んでいる」など現在進行に書き換え

### untracked 残置物（次セッションで判断）

- `assets/covers/` `assets/opening/` `drafts/covers/` `drafts/opening/` `drafts/opening_spread_brief.md` — 別ライン（カバー・開きの試作）の作業
- `ledgers/expansion_plan.md` — 拡張プランのメモ。entry_candidates.md の更新と対応する
- `ledgers/entry_candidates.md` の M（差分）— G-15〜G-19 / G-38 / G-39 / G-47 / F-16 / F-17 / F-200 / H-63 の候補追加。このセッションで対応するスケルトンを本書きしたので、M を取り込んでもよい

### 残タスク

- **残スケルトン約 42 件**（次の 30 件束で粗方片付く）
  - **C 系 4 件**：C-80 AI 大学 / C-81 にゃんた / C-82 まさお / C-83 AI の歴史氏（YouTuber 系）
  - **D 系 4 件**：D-3 Gemini 3 系 / D-4 Gemini 3.1 系 / D-14 Claude Mitos モデル / D-25 GPT-1 / GPT-2 系
  - **F 系 約 7 件**：F-34 VS Code 拡張機能 / F-42 ビルド / F-43 テスト / F-100 拡張子総覧 / F-150（書済）/ F-190 サブルーチン ほか
  - **G 系 約 9 件**：G-7 指示追従性 / G-8 決定論的非決定論的 / G-9 effort レベル / G-35 Deep Research / G-36 Artifact / G-43 オーケストレーション / G-44 マルチエージェント協調 / G-45 段階的開示 / G-46 ナーフ
  - **H 系 約 8 件**：H-51 Preview→正式版 / H-52 Copilot→Claude Code / H-55 LLaMA オープン化 / H-56 Claude バージョン史 / H-57 Gemini 命名史 / H-59 AI エージェント元年 / H-60 Codex→Copilot 系譜 / H-61 Preview 文化 / H-62 Anthropic 創業
  - **I 系 2 件**：I-80 自作 MCP のテンプレ / I-81 MCP の登録設定
  - **J 系 約 8 件**：J-31 第 5 世代 / J-32 ノイマン型 / J-33 量子コンピュータ / J-53 著作権法 / J-55 個人情報法 / J-62 チューリングテスト / J-74 RTX シリーズ / J-75 Tensor コア / J-100 識字
- **既書き 39 件の著者欄記入**（needs_review → ready 昇格は著者本人のみ可能）
- **要直しキューの ⚠ 軽微超過 約 237 件**：著者欄記入のついでに削るのが効率的（数は累積、新規分が 50 件ほど追加）
- **新ファイル名 ↔ entries.csv path の整合性確認**：J-19_quantization / J-2_strong_weak_ai / D-43_qwen など、書き換え時の path 自動更新は確認済みだが念のためチェック

### 次セッションの最短ルート

1. このファイルの「2026-04-30 セッション成果」と最新の `ledgers/revision_queue.md` を見る
2. 残スケルトン約 42 件から 30 件束を選ぶ（C/D/F/G/H/I/J の混成、または H 歴史 + I 自作 MCP + J 一般などテーマ別）
3. `python3 -c "..."` で skeleton → drafting 一括フリップ
4. `Agent` を 5 並列で起動 × 6 バッチ
5. 完走後に `python3 scripts/update_review_queue.py` で確認、☆ 違反があれば並列トリム
6. コミット

### 累計成果（2026-04-29〜2026-04-30 セッション）

- **本書き 245 件**（前セッション 95 + 今セッション 150）
- **コミット 10 本**（v9 の 4 本 + v10 の 6 本）
- **残スケルトン 305 → 42 件（−263、進捗 86%）**

---

## 2026-04-29: 並列 95 件本書きラウンド（5 並列 × 19 バッチ）

### コミット 4 本（古い順）

- `a3784b7` brief entry-writer with parallel-run warning patterns（並列警告パターン §5 を恒久化）
- `79da9f9` write 35 stage-2/3 entries: F-51〜55 git subcommands + 30 across 6 batches
- `6477f41` write 30 more stage-2/3 entries (B/C/D/F/G across batches 7-12)
- `3b91c5e` write 30 more stage-3 entries (D/E/G/H/J across batches 13-18)

### 書いた 95 件の内訳

| ラウンド | バッチ | 件数 | エントリ |
| :-- | :-- | --: | :-- |
| R1 先行 | 1 | 5 | F-51 git push / F-52 git pull / F-53 branch / F-54 commit / F-55 merge |
| R1 batch1 | 1 | 5 | E-2 SWE-Bench Verified / E-20 MMLU / E-50 Chatbot Arena / B-51 ChatGPT 料金 / B-52 Gemini 料金 |
| R1 batch2 | 2 | 5 | D-30 Grok 系 / D-40 Llama 系 / D-1 Gemini 2 系 / D-21 GPT-4 系 / D-22 o1 系 |
| R1 batch3 | 3 | 5 | F-4 HTML / F-5 CSS / F-6 Markdown / F-30 VS Code / F-60 GitHub |
| R1 batch4 | 4 | 5 | G-30 Tool Use / G-20 CLAUDE.md / G-4 System Prompt / G-5 Context Window / G-11 Context Engineering |
| R1 batch5 | 5 | 5 | I-2 MCP Server / I-3 MCP Client / I-11 GitHub MCP / I-10 Filesystem MCP / I-20 Playwright MCP |
| R1 batch6 | 6 | 5 | J-11 Deep Learning / J-10 Machine Learning / J-51 Hallucination / J-77 GPU / H-50 Bard → Gemini |
| R2 batch7 | 7 | 5 | B-7 Claude Code / B-9 v0 / B-10 Devin / B-11 Bolt.new / B-12 Perplexity |
| R2 batch8 | 8 | 5 | B-21 Netlify / B-22 Cloudflare / B-24 Google Cloud / B-25 Azure / B-30 Amazon Bedrock |
| R2 batch9 | 9 | 5 | C-4 Meta AI / C-5 xAI / C-7 Hugging Face / C-52 Demis Hassabis / C-53 Andrej Karpathy |
| R2 batch10 | 10 | 5 | D-10 Claude 3 系 / D-23 o3 系 / D-24 GPT-3 系 / D-41 Mistral 系 / D-42 Gemma 系 |
| R2 batch11 | 11 | 5 | F-7 YAML / F-8 JSON / F-40 npm / F-41 Vite / F-90 Docker |
| R2 batch12 | 12 | 5 | G-3 Dictation / G-13 Few-shot Learning / G-14 Thinking モデル / G-21 AGENTS.md / G-22 SKILL.md |
| R3 batch13 | 13 | 5 | D-50 DALL-E / D-51 Imagen / D-52 Sora / D-54 Stable Diffusion / D-71 Whisper |
| R3 batch14 | 14 | 5 | D-26 gpt-oss / D-43 Qwen 系 / D-44 Kimi / D-46 DeepSeek V3 / D-47 DeepSeek R1 |
| R3 batch15 | 15 | 5 | E-3 Terminal-Bench / E-4 HumanEval / E-21 MMLU-Pro / E-22 GPQA / E-30 TAU-Bench |
| R3 batch16 | 16 | 5 | G-31 Hook / G-32 Slash Command / G-33 Function Calling / G-41 Subagent / G-42 Worktree |
| R3 batch17 | 17 | 5 | H-1 TDD / H-3 バイブコーディングの流儀 / H-7 CI/CD / H-54 GPT-4 リリース / H-58 Transformer 論文 |
| R3 batch18 | 18 | 5 | J-12 Neural Network / J-17 Attention / J-18 MoE / J-23 拡散モデル / J-41 DX |

### 並列実行の知見（次回も使える）

1. **5 並列 × N バッチが安定**：6 並列以上は警告制御が効きにくい印象
2. **status は Python ワンライナーで一括変更**：30 件の `skeleton → drafting` を Edit 30 回ではなく `re.sub` 1 回で。スケルトンテンプレ内コメントに `status: skeleton` が 3 つあるので必ずフロントマター 1 つだけを置換する正規表現（`^status: skeleton\s*$` + flags=MULTILINE + count=1）を使う
3. **頻発した ☆ 違反パターン**（合計 6 件発生・全件その場で並列トリム解消）
   - 左ページ合計 +100 字超過（G-11 / G-20 / D-41 / G-22 / G-31）— entry-writer に「左ページ合計 250 字以内」を毎回伝えるべき
   - 旧スケルトンの archive 漏れ（D-40）— 新ファイル名へ移行した entry は entries.csv の path も合わせて更新すべき。スケルトン側の `status: drafting` を放置すると ☆ 違反として再検出される
4. **D 系モデルで「新ファイル名にせず元のままで書く」と頼んでも、entry-writer は新ファイル名にリネームする傾向**（D-43 → D-43_qwen.md / D-54 → D-54_stable_diffusion.md など）。実害はない（旧スケルトンを archive 化するので validator はスキップする）が、entries.csv の path は手で見直す価値あり
5. **「進んだ N 本」のような連体修飾の「だ」が validator の `(?<![すまりぞ])だ[。\s]` 正規表現で誤検出される**。「進んでいる」など現在進行に書き換える指示を毎回プロンプトに入れている

### 残タスク

- **次の 30 件束（候補）**：
  - **A 系メタ全件 9 件**（A-3 歩き方 / A-4 体験区分 / A-5 読者レベル / A-6 評価日 / A-7 図のタイプ / A-8 色記号 / A-9 索引 / A-10 更新履歴 / A-11 略称表記）— 序文・凡例の整備、本書の入口
  - **F 系言語・ツール残り**（F-12 Electron / F-13 Tauri / F-15 shadcn/ui / F-21 Prettier / F-44 pnpm / F-56 .gitignore / F-57 リポジトリ / F-58 git stash / F-59 README.md / F-61 Pull Request / F-62 GitHub Actions / F-80 Node.js / F-81 bash ほか多数）
  - **I 系 MCP 残り**（I-4 MCP Transport / I-5 MCP SDK / I-12 Git MCP / I-13 Slack MCP / I-22 Chrome DevTools MCP / I-23 Serena MCP / I-24 Context7 MCP / I-30 Notion MCP / I-41 SQLite MCP / I-50 AWS MCP / I-80 自作 MCP / I-81 MCP の登録設定）
  - **J 系残り**（J-1 AGI / J-3 Singularity / J-4 ASI / J-15 VLM / J-16 Fine-tuning / J-19 量子化 / J-21 LoRA / J-22 パラメータ数 / J-40 IoT / J-42 Web3 / J-43 SaaS / J-50 AI 倫理 / J-52 Sycophancy / J-56 GDPR / J-70 VRAM / J-72 H100 / J-76 CPU ほか多数）
  - **G 系残り**（G-6 One-shot / G-7 指示追従性 / G-8 決定論的非決定論的 / G-9 effort レベル / G-12 Agent Design / G-23 settings.json / G-34 Code Interpreter / G-35 Deep Research / G-36 Artifact / G-43 オーケストレーション / G-44 マルチエージェント協調 / G-45 段階的開示 / G-46 ナーフ）
  - **H 系残り**（H-2 ペアプログラミング / H-4 コードレビュー / H-5 Scrum/Agile / H-6 Git Flow / H-8 DevOps / H-51 Preview→正式版 / H-52 Copilot→Claude Code / H-55 LLaMA オープン化 / H-56 Claude バージョン史 / H-57 Gemini 命名史 / H-59 AI エージェント元年 / H-60 Codex→Copilot 系譜 / H-61 Preview 文化 / H-62 Anthropic 創業）
  - **C 系人物残り**（C-54 Ilya Sutskever / C-55 Mira Murati / C-56 Yann LeCun / C-57 Geoffrey Hinton / C-58 Elon Musk / C-59 Jensen Huang / C-60 Ray Kurzweil ほか）
- **既書き 37 件の著者欄記入**（needs_review → ready 昇格は著者本人のみ可能）
- **要直しキューの ⚠ 軽微超過 79 件**：著者欄記入のついでに削るのが効率的
- **新ファイル名 ↔ entries.csv path の整合性確認**：D-43_qwen.md など、書き換え時に path 更新が漏れている可能性あり

### 次セッションの最短ルート

1. このファイルの「2026-04-29 セッション成果」と最新の `ledgers/revision_queue.md` を見る
2. 次の 30 件束を選ぶ（A 系メタ 9 件 + F/I/J/G/H/C のどれか組み合わせ）
3. `python3 -c "..."` で skeleton → drafting 一括フリップ
4. `Agent` を 5 並列で起動 × 6 バッチ
5. 完走後に `python3 scripts/update_review_queue.py` で確認、☆ 違反があれば並列トリム
6. コミット

## 2026-04-28（追記）: タイトル読みスロット `title_reading` を追加

**背景**: 既存サンプルの整合性チェック中に、`Context（コンテキスト）` のような「タイトル文字列に括弧で読みを付ける」表記が、誌面の 96px ヒーロー枠で過剰に大きく出る問題が顕在化。タイトルは純粋名のみ、読みは下に小さく分離する方針に切り替え。

**変更内容**:

- 新 YAML フィールド `title_reading`（任意）— タイトル直下に 14px グレーで表示
- 誌面: タイトル直下に `.title-reading` スロットを新設（`:empty` で非表示制御）
- ルール: `title` は純粋名のみ（括弧書き読みを禁止）
- validator: `title` 末尾の `（…）` を ⚠️ 警告、`title_reading` の字数（2〜30）も ⚠️ 警告

**伝搬済みファイル**（schema_version v2.28.0）:

- [docs/v2_rules_summary.md](../docs/v2_rules_summary.md) §0 / §1 左ページ / §2-2 YAML / §2-3 左ページ本文 / §5 リネーム履歴
- [docs/entry_schema.yaml](../docs/entry_schema.yaml) frontmatter.recommended に `title_reading`、left_page slot 追加
- [docs/quality_checklist.md](../docs/quality_checklist.md) §A / §B tagline
- [templates/entry_template.md](../templates/entry_template.md) YAML コメント追加
- [templates/skeleton_template.md](../templates/skeleton_template.md) YAML に `title_reading:` 行追加
- [scripts/validate_entry.py](../scripts/validate_entry.py) `check_yaml` に括弧チェック・字数チェック追加
- [drafts/prototypes/mockups/design_philosophy_v2/typescript_spread.html](../drafts/prototypes/mockups/design_philosophy_v2/typescript_spread.html) `.title-reading` 要素追加（タイプスクリプト）
- [drafts/prototypes/mockups/design_philosophy_v2/overlay.css](../drafts/prototypes/mockups/design_philosophy_v2/overlay.css) `.title-reading` スタイル追加
- [drafts/prototypes/mockups/design_philosophy_v2.md](../drafts/prototypes/mockups/design_philosophy_v2.md) §2-1.5 / §3 紙面構成 / §6 履歴
- [drafts/prototypes/mockups/design_philosophy_v2/writing_spec.md](../drafts/prototypes/mockups/design_philosophy_v2/writing_spec.md) §1-0 追加

**既存エントリへの適用**: active 13 件すべてに対応済み

| ID | title | title_reading |
|---|---|---|
| B-1 | Gemini | ジェミニ |
| B-2 | Claude | クロード |
| B-3 | ChatGPT | チャットジーピーティー |
| C-1 | OpenAI | オープンエーアイ |
| C-2 | Anthropic | アンソロピック |
| D-11 | Claude 3.5 系 | クロード サンテンゴ系 |
| D-12 | Claude 4 系 | クロード ヨン系 |
| E-1 | SWE-Bench | スウィーベンチ |
| F-50 | git | ギット（tagline 冒頭の「読み方は…」も削除） |
| G-1 | Context（旧 `Context（コンテキスト）`） | コンテキスト |
| H-53 | ChatGPT 登場 | チャットジーピーティー登場 |
| I-1 | MCP（旧 `MCP（Model Context Protocol）`） | Model Context Protocol |
| J-14 | LLM（旧 `LLM（大規模言語モデル）`） | 大規模言語モデル |

A-1 / A-2（common/）は validator 除外済みで対象外。読みが自明な日本語タイトル（「ChatGPT 登場」のうち登場部 etc）の運用は entry-writer の判断に任せる。

---

## 2026-04-28: スケルトン先行運用へ切り替え

**変更内容**:

- 新ステータス `status: skeleton` を追加（[docs/entry_schema.yaml](../docs/entry_schema.yaml) v2.27.0）。validator は archived/sample と同様にスキップ
- スケルトン専用テンプレ：[templates/skeleton_template.md](../templates/skeleton_template.md)
- ジェネレータ：[scripts/generate_skeleton.py](../scripts/generate_skeleton.py)
- B letter 37 件で先にテストし、YAML パーサのインラインコメント問題と既存ファイル上書き事故を発見・修正してから残り 281 件を一括生成

**現状ステータス内訳**（[ledgers/entries.csv](entries.csv)）:

- `needs_review`: 11（A-2, B-1, B-2, C-2, D-12, E-1, F-50, G-1, H-53, I-1, J-14）
- `drafting`: 1（B-3 ChatGPT）
- `candidate`: 3（A-1, C-1, D-11 — 既に書かれているが needs_review に上げる前。手で確認・昇格を）
- `sample`: 6（旧 3 桁 ID、archived 相当）
- `skeleton`: 318（本文未着手）

**次セッションの最短ルート**:

1. [stage2_briefs.md](stage2_briefs.md) の 46 件から 1 件選ぶ（連関の強い B-4 Cursor、C-1 OpenAI などが入口）
2. md ファイルを開いて `status: skeleton` → `status: drafting` に変更
3. `entry-writer` サブエージェント呼び出し（"B-4 Cursor を書いて"）
4. validator で機械チェック → 著者レビュー → `status: needs_review`

---

## （旧）2026-04-26 v6 更新内容（参考）

*v2 レイアウトの 21 世代反復と全エントリ監査・修正が終わり、iter 22 で左右ページの役割再バランスを実施。続く 2026-04-26 セッションで「会話での使い方例」セクションを左ページ末尾に正式追加しました。*

## 2026-04-26: 「会話での使い方例」セクション追加

**誌面追加 1 点**:

「わかってる人風」が自然にこの語を会話で使う 1 例を、左ページ末尾の独立スロット（下チロム右側「（会話での使い方例）」枠）に印字するセクションを正式追加。**25〜50 字（推奨 30〜40）、1 文**。markdown 上は `## メイン図` の後、`<!-- 右ページ -->` の前に置く。

**伝搬済みファイル**:

- [templates/entry_template.md](../templates/entry_template.md) — `## 会話での使い方例` セクション追加
- [docs/v2_rules_summary.md](../docs/v2_rules_summary.md) §1 / §2-3 / §2-6 / §5 リネーム履歴
- [docs/entry_schema.yaml](../docs/entry_schema.yaml) — left_page slot ＋ required_sections に追加（schema_version v2.26.0）
- [docs/quality_checklist.md](../docs/quality_checklist.md) — B 左ページにチェック項目追加
- [skills/write-entry.md](../skills/write-entry.md) — Step 3 左ページの順序リストに追加
- [.claude/agents/entry-writer.md](../.claude/agents/entry-writer.md) — Step 3 字数目安テーブルに行追加
- [scripts/validate_entry.py](../scripts/validate_entry.py) — REQUIRED_SECTIONS / SECTION_TARGETS に追加
- [drafts/prototypes/mockups/design_philosophy_v2/check_entry.py](../drafts/prototypes/mockups/design_philosophy_v2/check_entry.py) — REQUIRED_SECTIONS / SECTION_RULES に追加
- [drafts/prototypes/mockups/design_philosophy_v2/writing_spec.md](../drafts/prototypes/mockups/design_philosophy_v2/writing_spec.md) — §1-8 として追加
- [drafts/prototypes/mockups/design_philosophy_v2.md](../drafts/prototypes/mockups/design_philosophy_v2.md) — §3 紙面構成に項目追加

**既存エントリ**: 既存 20 エントリ（A-1 / A-2 を除く active 13 件 ＋ archived 7 件）に会話での使い方例を 1 文ずつ追加済み。A-1 preface / A-2 reading_guide は本書の序文・読み方ガイドのため対象外。

**字数の決定**: 当初「許容 30-40 / 推奨 30-38」で仮置きしたが、既存エントリ実測（B-2 Claude=29 字、I-1 MCP=42-47 字など）を踏まえて**許容 25-50 / 推奨 30-40** に最終調整。validator は許容外でのみ ⚠️ 警告。

## iter 22（2026-04-25）: 左右ページの役割再バランス

**誌面変更 3 点**:

1. **右ページ冒頭タイトル `{{title}} をどう読むか` を削除**（誌面・markdown 双方）。右ページは「この用語の見どころ」から直接始まる
2. **関連用語ピルを右ページ下段（開発フローの直下）に移動**。markdown 上も右ページ区分に移した
3. **擬人化ポンチ絵スロットをメインビジュアルに拡大**（200px アイコン・340px 高さ）。左ページ最下段、Before/After の下に置く主役ビジュアル

**伝搬済みファイル**:

- [docs/v2_rules_summary.md](../docs/v2_rules_summary.md) §0 チェックリスト／§1 紙面構造／§4 レイアウト／§5 リネーム履歴
- [drafts/prototypes/mockups/design_philosophy_v2/overlay.css](../drafts/prototypes/mockups/design_philosophy_v2/overlay.css) `.ponchi-slot` をデフォルトで大サイズに
- [drafts/prototypes/mockups/design_philosophy_v2/typescript_spread.html](../drafts/prototypes/mockups/design_philosophy_v2/typescript_spread.html) 左ページから関連用語削除・右ページ下段に再配置・右タイトル削除
- [drafts/prototypes/mockups/design_philosophy_v2.md](../drafts/prototypes/mockups/design_philosophy_v2.md) §3 紙面構成
- [drafts/prototypes/mockups/design_philosophy_v2/writing_spec.md](../drafts/prototypes/mockups/design_philosophy_v2/writing_spec.md) §1-7 擬人化スロット／§2-1 右ページ冒頭タイトル削除／§2-6 関連用語（右ページへ）
- [templates/entry_template.md](../templates/entry_template.md) 関連用語ブロックを右ページ区分へ
- [scripts/validate_entry.py](../scripts/validate_entry.py) `related_terms` を `page="right"` に、左右合計目安を左 155-250／右 220-430 に更新

**既存エントリの移行**: [scripts/migrate_iter22_related_terms.py](../scripts/migrate_iter22_related_terms.py) で **active 12 エントリ**（A-1, A-2, B-1, B-2, C-2, D-12, E-1, F-50, G-1, H-53, I-1, J-14）の `## 関連用語` ブロックを `## 開発フローでの位置（必須）` の直後に移動済み（2026-04-25）。archived 7 エントリはスキップ。再実行しても冪等（`already migrated` を返す）。

**既知の注意**: 移行後も v2 validator（check_entry.py）は全 19 エントリ ☆ 警告 0。ただし strict 側の `scripts/validate_entry.py` は既存エントリで文字数超過（tagline / 何をしてくれるか等）を警告する。これは移行前からの編集課題で、移行による新規回帰ではない。

## 2026-04-25 追加: 静的サイト生成器への移行準備（方針 B 採択）

著者判断で **「markdown を正、HTML/PDF はそこから生成する」方針** に倒した。本プロジェクトは markdown ＋ 仕様の維持が主務。実装（CSS / Astro / TSX / Paged.js）は別担当へ引き渡す想定。

**整備済みの引き渡し資産 4 本**:

- [ledgers/chapters.yaml](chapters.yaml) — letter（A〜J）→ 章ラベル／カテゴリ／ディレクトリのマップ。ハンバーガーナビの自動生成元。
- [ledgers/entries.csv](entries.csv) — `path` 列を追加（`scripts/sync_entries_csv.py` で md 実体と自動同期）。15 active エントリに path 埋込み済。
- [docs/entry_schema.yaml](../docs/entry_schema.yaml) — v2_rules_summary §2 の機械可読版。frontmatter 制約・文字数・必須節・リネーム履歴を YAML で集約。**generator / validator / 仕様書の三者が同一入力を参照する単一真実点**。
- [docs/component_spec_v2.md](../docs/component_spec_v2.md) — `typescript_spread.html` を 14 primitive / 6 セクション / 2 ページ / 1 スプレッドに分解した引き渡し仕様。**スタック採択: Astro + React ハイブリッド（C）**（§0 に確定、2026-04-25）。Paged.js で PDF 化想定。

**新規エントリ追加時の運用**:

1. エントリを書く（entry-writer で）
2. `python scripts/sync_entries_csv.py` で path 列を更新
3. `python scripts/validate_entry.py` で字数・トーン検証
4. `python drafts/prototypes/mockups/design_philosophy_v2/check_entry.py` で構造検証
5. （任意）`typescript_spread.html` のドロワーに手動追加（generator 稼働後はこの 5 が不要になる）

---

## 最初の 3 分で把握すべき現状

- **v2 レイアウト凍結済み**: iter 1-21 で確定。全ルールは [docs/v2_rules_summary.md](../docs/v2_rules_summary.md) に集約
- **既存 19 エントリ全て v2 準拠**: `python drafts/prototypes/mockups/design_philosophy_v2/check_entry.py --dir content/entries/` で全 OK
- **テンプレ（templates/entry_template.md）は v2 対応済**: 新規執筆はそのままコピーで OK
- **自動チェッカー稼働中**: 保存時に PostToolUse hook で走る（scripts/validate_entry.py）＋ 手動では check_entry.py

---

## この 2 セッションで完了したこと（2026-04-24 〜 2026-04-25）

### Design System v2 の採択と凍結

- Claude.ai/design が出した見開きサンプル（TypeScript p.04-05）をゴールとし、Playwright で 21 世代の HTML 反復
- 最終 HTML: [drafts/prototypes/mockups/design_philosophy_v2/typescript_spread.html](../drafts/prototypes/mockups/design_philosophy_v2/typescript_spread.html)
- CSS primitive: [drafts/prototypes/mockups/design_philosophy_v2/overlay.css](../drafts/prototypes/mockups/design_philosophy_v2/overlay.css)
- 反復スクショ iter 1-21: [drafts/prototypes/mockups/design_philosophy_v2/screenshots/](../drafts/prototypes/mockups/design_philosophy_v2/screenshots/)
- 右上ハンバーガーナビで A〜J の 2 階層エントリリストを実装

### 仕様ドキュメント 4 本

- [docs/v2_rules_summary.md](../docs/v2_rules_summary.md) — **正式入口**（執筆前に必ず）
- [drafts/prototypes/mockups/design_philosophy_v2.md](../drafts/prototypes/mockups/design_philosophy_v2.md) — 設計思想・CSS トークン・決定履歴
- [drafts/prototypes/mockups/design_philosophy_v2/writing_spec.md](../drafts/prototypes/mockups/design_philosophy_v2/writing_spec.md) — 節ごと文字数・書き方原則
- [drafts/prototypes/mockups/design_philosophy_v2/book_readiness_review.md](../drafts/prototypes/mockups/design_philosophy_v2/book_readiness_review.md) — 書籍化の残課題

### 自動チェッカー

- [drafts/prototypes/mockups/design_philosophy_v2/check_entry.py](../drafts/prototypes/mockups/design_philosophy_v2/check_entry.py)
- 使い方: `python drafts/prototypes/mockups/design_philosophy_v2/check_entry.py --dir content/entries/`
- archived エントリはスキップ、エラー・警告付きで出力

### 既存エントリの v2 対応

**11 新 letter エントリ**を v2 仕様に合わせて修正（[6b58358], [7db1d65]）:

- A-2 / B-1 / B-2 / C-2 / D-12 / E-1 / F-50 / G-1 / H-53 / I-1 / J-14
- 「ひとことで」削除、本文を 200 字以内に圧縮、6 視点セルを 40 字以内、related_terms を 5 個に

**6 旧 3 桁エントリ**を `status: archived` に凍結:

- 201 / 301 / 302 / 303 / 304 / 305 （101 は既に archived）

**新規 A-1 まえがき** を作成（[content/entries/common/A-1_preface.md](../content/entries/common/A-1_preface.md)）

### 節名リネーム（全ファイル伝搬）

| 旧 | 新 | 影響ファイル |
|---|---|---|
| 非エンジニア視点のつまずき | **非エンジニアのつまずき** | 38 |
| 誰に向くか | **誰向けか** | 22 |

### 紙面の確定ビジュアル（iter 1-21 の累積）

- 左タイトル 96px ネイビー、右タイトル 50px ネイビー（純黒はしんどい・純青は目立ちすぎ）
- タグライン帯は淡青塗り（--ink-blue-100）、25〜45 字
- 6 視点セル: 縦スタック、番号バッジ左上、アイコン 52px 中央（4 個差し替え: 的に crosshair / 電球 / 若葉→sprout / file-search）
- つまずき:コメント = **4:6** 比率
- フッター左右分割: 左ページ「YYYY.MM · Draft / （会話での使い方例）」、右ページ「F-01 · language / 📖 バイブコーディング図鑑」
- ノド非対称 margin、縦横比 750×1061（√2 準拠）
- 本文 16px、6 視点本文 14.5px（A4 換算 約 11pt）
- 右上プロトタイプナビ（ハンバーガー → A〜J 2 階層）

---

## 次セッションの TODO

### 最優先: ステージ 2 の執筆着手

[writing_priority.md](writing_priority.md) §ステージ 2 の 46 件を [stage2_briefs.md](stage2_briefs.md) と併読。

新規エントリ執筆手順:

1. [docs/v2_rules_summary.md](../docs/v2_rules_summary.md) の §0 1 分チェックリストに目を通す
2. [templates/entry_template.md](../templates/entry_template.md) を該当ディレクトリへコピー（`content/entries/service/B-3_chatgpt.md` のように）
3. YAML → tagline → 本文 2 節 → Before/After → 関連用語 → 6 視点 → 開発フロー → 裏台帳の順に埋める
4. 著者記入欄（非エンジニアのつまずき／私のコメント）は空スケルトンのまま残す
5. `python drafts/prototypes/mockups/design_philosophy_v2/check_entry.py content/entries/path/to/entry.md` で検証、エラーゼロに
6. `entries.csv` の status を更新

次に書く候補（stage2_briefs の並び）:

1. **B-3 ChatGPT**（H-53 と接続）
2. **C-1 OpenAI**（B-3 との流れ）
3. **D-11 Claude 3.5 系**（D-12 と接続）
4. **G-2 Token**（G-1 Context とセット）
5. **G-40 バイブコーディング**（本書の中心語彙）

### 著者確認の残件

- **Cursor の "head F" モデル**: `cursor-tab-3` のことか、`Composer` か、別物か。回答次第で D-35 の扱いを決定

### 旧 3 桁 ID の letter-ID 書き直し（素材として取り込み）

- 301 JavaScript → F-1（予定）
- 302 TypeScript → F-2（予定）
- 303 ESLint → F-10（予定）
- 304 React → F-11（予定）
- 305 Next.js → F-20（予定）
- 201 Gemini 2.5 系 → D-2（予定）
- 101 Gemini は B-1 に取り込み済（archived）

ステージ 2 執筆と一体で、対応する letter-ID を書くときに旧 3 桁の内容を素材として引用する形。

### 並行: モバイル投入フロー Phase 1

[docs/mobile_inbox_requirements.md](../docs/mobile_inbox_requirements.md) §9 Phase 1。Android Obsidian Mobile 経由のコメント取り込みを一度回して、import-comments スキルの挙動を確認。

### 保留事項

- **論文エントリの配置**（Transformer 論文等）: 現 H-58 のまま、他の論文候補が揃ってから
- **タイムラインの細分化**: Claude 系 / Gemini 系のマイナー版刻みは後回し
- **302_typescript の著者欄 AI 記入**: 新テンプレで F-2 を書き直すときにクリア（archived なので急がない）
- **書籍化の印刷工程**: bleed / CMYK 色校正 / フォント埋め込み確認は別担当に渡す段階で（[book_readiness_review.md](../drafts/prototypes/mockups/design_philosophy_v2/book_readiness_review.md) §5-6）

---

## スコープ外（やらない）

- **CSS・React 実装（v2 仕様の実装）**: 別担当。本プロジェクトは markdown ベースの仕様更新・執筆・検証まで
- ただし v2 仕様自体の**微調整・議論・追加ルールの集約**は引き続き本プロジェクトで OK

---

## セッション再開時の最初の動き

1. このファイルを開く
2. [docs/v2_rules_summary.md](../docs/v2_rules_summary.md) を通読（執筆前の前提を揃える）
3. 著者に Cursor "head F" の再確認（5 分で済む）
4. [stage2_briefs.md](stage2_briefs.md) から 1 件選び、上記の執筆手順で着手

---

## 直近コミット（新しい順）

- `8c44654` add docs/v2_rules_summary.md: consolidated v2 rules for authors
- `6b58358` refine typography, 4:6 bottom split, icons; rename 視点/向くか
- `2f71c65` bump body text sizes one step across the spread
- `9560b01` add prototype hamburger nav with A-J two-level drawer
- `7db1d65` bring entries to v2 spec: trim 11 letter drafts, archive 6 legacy 3-digit
- `4ab0a84` add Design System v2 spec, prototype, and entry validator
- `6d1eb6c` migrate to v2 template from finalized design mockup
