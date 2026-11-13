# ID 体系ルール（v0.5・確定版）

*2026-04-22 v0.1 → v0.2（6→8）→ v0.3（MCP を I）→ v0.4（一般語彙を J）→ 2026-04-23 v0.5（10 区切り確定・番号運用ルール固定）。*

*大分類 10 区切りは**確定**。サブ範囲の詳細・候補エントリは [ledgers/entry_candidates.md](../ledgers/entry_candidates.md) を正とする（本ファイルは governance 側、entry_candidates.md は living list）。*

*現行の3桁連番（101, 201, 301…）は残し、新体系への切り替えは後で実施する。*

## 目的

- ID は「ページ番号」ではなく「管理番号」として扱う
- 後で番号を付け替えやすい構造にする
- 区切り文字（英字1字）＋連番で大分類を表す

## 基本形式

```text
{区切り文字}-{連番}[-{派生}]
```

- 例: `A-1` / `B-1` / `C-50` / `E-1` / `F-2` / `G-20`
- 区切り文字: 1字の英大文字（大分類）
- 連番: 区切り内で採番。欠番・飛び番は許容、詰め直さない
- 派生: `-a` `-b` … 時期差分・比較分冊に任意で使う

## 大分類（現行案：10 区切り）

| 区切り | 内容 | 対応する category |
| --- | --- | --- |
| **A** | はじめに・共通（前書き／凡例／体験区分／読者レベル説明） | 共通 |
| **B** | サービス（AI アシスタント・ホスティング・IDE 等） | service |
| **C** | 人・会社（Sam Altman、OpenAI、Anthropic など） | person / organization |
| **D** | モデル（Gemini 2.5 系、Claude Sonnet 系、GPT-5 系） | model |
| **E** | ベンチマーク・評価指標（SWE-Bench、Terminal-Bench など） | benchmark |
| **F** | 従来コーディングの言葉・道具（言語・FW・Git・CLI） | term / tool |
| **G** | バイブコーディング特有の言葉・ファイル（CLAUDE.md、Hook 等） | term (llm 系) / tool (agent 設定系) |
| **H** | 進め方・歴史（ワークフロー／系譜） | workflow / history |
| **I** | MCP（プロトコル／主要サーバー／連携サービス） | term (mcp) / tool (mcp server) |
| **J** | **一般 AI・テック語彙**（AGI、ディープラーニング、IoT、DX など） | term (general) |
| **Z** | 保留・実験・未整理 | — |
| **X** | ボツ・非公開（裏台帳のみ） | — |

## 読み順（誌面掲載順の推奨）

letter は保管用の識別子として固定する（並び替えたらリンクが死ぬため）。読者が迷いにくい順で**掲載順は別に定義**する。

推奨する掲載順は次のとおり。「読者が耳にしたことのある広い語」から入り、だんだん専門に降りて、最後に歴史で締める構成。

| 掲載順 | letter | 見出し | 理由 |
| --- | --- | --- | --- |
| 1 | A | はじめに・共通 | 読み方と凡例 |
| 2 | J | 一般 AI・テック語彙 | AGI・DX・IoT など「ニュースで聞いたことがある」語彙で読者を温める |
| 3 | B | サービス | Claude・ChatGPT・Gemini のように読者が名前を知っている入口 |
| 4 | C | 人・会社 | サービスを作っている主体。B の直後に置くと系譜が見える |
| 5 | D | モデル | サービスの中身。B → C → D の順で「何 → 誰 → 何が動く」が一直線になる |
| 6 | E | ベンチマーク・評価指標 | モデルをどう見るか。D の直後 |
| 7 | F | 従来コーディングの言葉・道具 | 実際の作業の基礎語彙 |
| 8 | G | バイブコーディング特有 | 従来語彙の上に立つ新しい語彙 |
| 9 | I | MCP | さらに踏み込んだ連携の話。専門度が上がるので後半に置く |
| 10 | H | 進め方・歴史 | 最後に全体を時系列で振り返る |

*letter 順（A→J）とは一致しない。誌面のページ番号は掲載順で採番し、ID（letter）は検索用に保つ。*

## C・E・I・J を独立させた理由

- **C（人・会社）**: サービスと「誰が作っているか」は別の棚として扱うほうが、読者が Sam Altman を引くときに迷わない。企業と人物は隣り合わせで置けるので同じ区切りに入れる。
- **E（ベンチマーク）**: モデル性能の話は「どのベンチマークで見るか」で解釈が変わる。モデルと同じ棚に混ぜず、評価軸として独立させた。
- **I（MCP）**: MCP は「プロトコル自体の話」「個別 MCP サーバー（GitHub MCP / Playwright MCP / Notion MCP など）」「MCP 経由で連携するサービスの話」と粒度が混ざりやすい。件数も多く増え続ける領域なので、G（バイブコーディング特有）に混ぜず独立させた。
- **J（一般 AI・テック語彙）**: AGI・強い AI・ディープラーニング・第 4／第 5 世代コンピューター・IoT・DX のように、**ニュースや雑談で耳にしたことはあるが輪郭があやふや**な語彙は、F（従来コーディング）にも G（バイブコーディング特有）にも収まらない。読者の「聞いたことはある」を拾うための棚として独立させた。

## 区切り内のサブ範囲（10 番刻み）

### A — はじめに・共通

| 範囲 | 意味 | 例 |
| --- | --- | --- |
| A-1〜9 | 前書き・読み方 | A-1 まえがき / A-2 この本の読み方 |
| A-10〜19 | 凡例・メタ | A-10 体験区分 / A-11 読者レベル |

### B — サービス

| 範囲 | 意味 | 候補 |
| --- | --- | --- |
| B-1〜19 | AI アシスタント系 | B-1 Gemini / B-2 Claude / B-3 ChatGPT / B-4 Cursor / B-5 Copilot / B-6 Windsurf / B-7 Claude Code |
| B-20〜29 | ホスティング・クラウド | B-20 Vercel / B-21 Google Cloud / B-22 AWS |
| B-30〜39 | IDE・エディタ提供 | B-30 VS Code（サービスとして）/ B-31 JetBrains |

### C — 人・会社

| 範囲 | 意味 | 候補 |
| --- | --- | --- |
| C-1〜29 | 会社・組織 | C-1 OpenAI / C-2 Anthropic / C-3 Google DeepMind / C-4 Meta AI |
| C-30〜39 | 会社・組織（追加分、2026-11-13 新設） | C-30 IBM。C-1〜29 が埋まったため続きに使う |
| C-50〜79 | 人物 | C-50 Sam Altman / C-51 Dario Amodei / C-52 Demis Hassabis / C-53 Andrej Karpathy |

### D — モデル

| 範囲 | 意味 | 候補 |
| --- | --- | --- |
| D-1〜9 | Google 系 | D-1 Gemini 2.5 系（Pro/Flash/Flash-Lite 比較） |
| D-10〜19 | Anthropic 系 | D-10 Claude Sonnet 系 / D-11 Claude Opus 系 / D-12 Claude Haiku 系 |
| D-20〜29 | OpenAI 系 | D-20 GPT-5 系 / D-21 o 系 |
| D-30〜39 | オープンモデル | D-30 Llama / D-31 Mistral |
| D-80〜99 | AA 掲載企業のモデル（追加分、2026-11-13 新設） | D-80 MiniMax M 系 / D-81 MiMo / D-82 Inkling。Artificial Analysis に名前が挙がる会社のモデルで、既存のサブ範囲に空きが無いものを置く |

### E — ベンチマーク・評価指標

| 範囲 | 意味 | 候補 |
| --- | --- | --- |
| E-1〜19 | コーディング・エンジニアリング | E-1 SWE-Bench / E-2 Terminal-Bench / E-3 HumanEval |
| E-20〜29 | 推論・知識 | E-20 MMLU / E-21 GPQA |
| E-30〜39 | エージェント・タスク完遂 | E-30 TAU-Bench / E-31 WebArena |
| E-50〜59 | その他・総合 | E-50 Chatbot Arena |

### F — 従来コーディングの言葉・道具

| 範囲 | 意味 | 候補 |
| --- | --- | --- |
| F-1〜9 | 言語 | F-1 JavaScript / F-2 TypeScript / F-3 Python |
| F-10〜19 | フレームワーク | F-10 React / F-11 Next.js / F-12 Vue |
| F-20〜29 | Linter・静的検査 | F-20 ESLint / F-21 Prettier |
| F-30〜39 | エディタ・IDE（道具として） | F-30 VS Code / F-31 Cursor(IDE) |
| F-40〜49 | CLI・ビルド・パッケージ | F-40 tsc / F-41 npm / F-42 pnpm / F-43 Vite |
| F-50〜59 | Git | F-50 git / F-51 git push / F-52 git pull / F-53 branch / F-54 commit / F-55 merge |
| F-60〜69 | GitHub | F-60 GitHub / F-61 Pull Request / F-62 Issue / F-63 GitHub Actions |
| F-70〜79 | 検索・探索 | F-70 grep / F-71 ripgrep (rg) / F-72 glob |
| F-210〜219 | 型・スキーマ・API契約 | F-210 JSON Schema / F-211 Zod / F-212 OpenAPI |

### G — バイブコーディング特有の言葉・ファイル

| 範囲 | 意味 | 候補 |
| --- | --- | --- |
| G-1〜9 | 基礎概念 | G-1 Context / G-2 Token / G-3 Dictation / G-4 System Prompt |
| G-10〜19 | エンジニアリング技法 | G-10 Prompt Engineering / G-11 Context Engineering / G-12 Agent Design |
| G-20〜29 | AI エージェント設定ファイル | G-20 CLAUDE.md / G-21 AGENTS.md / G-22 SKILL.md / G-23 .claude/settings.json |
| G-30〜39 | 連携・制御（MCP は I に分離） | G-30 Tool Use / G-31 Hook / G-32 Slash Command |
| G-40〜49 | バイブコーディング固有・運用 | G-40 バイブコーディング（用語）/ G-41 Subagent / G-42 Worktree / G-48 Structured Outputs |

### I — MCP（プロトコル／主要サーバー／連携サービス）

> 件数が多く、粒度も「プロトコル／個別サーバー／連携サービス」と分かれる。サブ範囲は用途で棚を切る。

| 範囲 | 意味 | 候補 |
| --- | --- | --- |
| I-1〜9 | MCP 基礎（プロトコル・仕組み） | I-1 MCP（概念） / I-2 MCP Server / I-3 MCP Client / I-4 MCP Transport (stdio / SSE / HTTP) / I-5 MCP SDK |
| I-10〜19 | 公式・リファレンス MCP | I-10 Filesystem MCP / I-11 GitHub MCP（公式）/ I-12 Git MCP / I-13 Slack MCP |
| I-20〜29 | 開発・自動化系 MCP | I-20 Playwright MCP / I-21 Puppeteer MCP / I-22 Chrome DevTools MCP |
| I-30〜39 | コラボ・業務系 MCP | I-30 Notion MCP / I-31 Linear MCP / I-32 Figma MCP / I-33 Jira MCP |
| I-40〜49 | データ・検索系 MCP | I-40 Postgres MCP / I-41 SQLite MCP / I-42 Elasticsearch MCP |
| I-50〜59 | クラウド・インフラ系 MCP | I-50 AWS MCP / I-51 GCP MCP / I-52 Vercel MCP |
| I-60〜69 | 「何と連携する？」軸のサービス棚 | MCP 経由で繋がる相手側を扱うページ（LLM ↔ ツール境界の図解中心） |
| I-80〜89 | 自作・運用 | I-80 自作 MCP のテンプレ / I-81 MCP の登録・設定 / I-82 トラブル・デバッグ |

#### I 系の命名方針

- 個別 MCP のページ名は「◯◯ MCP」で統一（「Notion MCP」等）
- 連携相手のサービス自体が独立したページになる場合は B 系に入れ、I 系からは相互リンクでつなぐ
  - 例：`B-40 Linear` ／ `I-31 Linear MCP` が両立し、互いに related_terms で参照し合う

### H — 進め方・歴史

| 範囲 | 意味 | 候補 |
| --- | --- | --- |
| H-1〜19 | ワークフロー | H-1 TDD / H-2 ペアプロ / H-3 バイブコーディングの流儀 |
| H-50〜69 | 歴史・系譜 | H-50 Bard → Gemini / H-51 Preview → 正式版 / H-52 Copilot から Claude Code までの流れ |

*歴史は「別コーナーでまとめて扱う」案もある。その場合は H-50 以降を 1 本の通し読み記事として組む。*

### J — 一般 AI・テック語彙

> 読者が「ニュースや会話で聞いたことがあるけれど、輪郭があやふや」な語彙を拾う棚。
> 必ずしもバイブコーディングの現場で毎日使う言葉とは限らないが、会話の前提として抑えておきたい語を集める。

| 範囲 | 意味 | 候補 |
| --- | --- | --- |
| J-1〜9 | AI の大概念 | J-1 AGI / J-2 強い AI ／ 弱い AI / J-3 Singularity（技術的特異点）/ J-4 ASI（超知能） |
| J-10〜19 | 機械学習・深層学習の基礎 | J-10 Machine Learning / J-11 Deep Learning / J-12 Neural Network / J-13 Transformer / J-14 LLM |
| J-20〜29 | データ・分析 | J-20 Big Data / J-21 Data Science / J-22 統計的機械学習 |
| J-30〜39 | コンピューティング史・パラダイム | J-30 第 4 世代コンピューター / J-31 第 5 世代コンピューター / J-32 ノイマン型 / J-33 量子コンピューター |
| J-40〜49 | 社会実装バズワード | J-40 IoT / J-41 DX（デジタルトランスフォーメーション）/ J-42 Web3 / J-43 クラウド（概念）/ J-44 SaaS |
| J-50〜59 | 倫理・安全・社会 | J-50 AI 倫理 / J-51 Alignment / J-52 Hallucination / J-53 バイアス |
| J-60〜69 | 周辺分野・原典系 | J-60 認知科学 / J-61 記号主義 vs 接続主義 / J-62 チューリングテスト |

## 派生 ID（`-a`, `-b`）

- 同じテーマの時期差分・比較分冊に使う
- 例：
  - `D-1` Gemini 2.5 系比較ページ
  - `D-1-a` Gemini 2.5 Pro の時期差分メモ
  - `D-1-b` Gemini 2.5 Flash のバージョン履歴

## 現行3桁IDとの暫定対応

| 現行ID | タイトル | 提案 ID | 区切り |
| --- | --- | --- | --- |
| 101 | Gemini | B-1 | B サービス |
| 201 | Gemini 2.5 Pro / Flash / Flash-Lite | D-1 | D モデル |
| 301 | JavaScript | F-1 | F 従来 |
| 302 | TypeScript | F-2 | F 従来 |
| 303 | ESLint | F-20 | F 従来 |
| 304 | React | F-10 | F 従来 |
| 305 | Next.js | F-11 | F 従来 |

## ユーザー要望から抜き出した新規候補

### サービス（B）

- B-2 Claude / B-3 ChatGPT / B-4 Cursor / B-7 Claude Code

### 人・会社（C）

- C-1 OpenAI / C-2 Anthropic / C-3 Google DeepMind
- C-50 Sam Altman / C-51 Dario Amodei

### モデル（D）

- D-10 Claude Sonnet 系 / D-20 GPT-5 系

### ベンチマーク（E）

- E-1 SWE-Bench / E-2 Terminal-Bench / E-20 MMLU

### 従来コーディング（F）

- F-50 git / F-51 git push / F-52 git pull / F-53 branch
- F-60 GitHub / F-61 Pull Request
- F-71 ripgrep (rg)

### バイブコーディング特有（G）

- G-10 Prompt Engineering / G-11 Context Engineering
- G-20 CLAUDE.md / G-21 AGENTS.md / G-22 SKILL.md
- G-31 Hook / G-32 Slash Command

### MCP（I）

- I-1 MCP（概念）/ I-2 MCP Server / I-3 MCP Client
- I-11 GitHub MCP / I-20 Playwright MCP / I-30 Notion MCP

### 一般 AI・テック語彙（J）

- J-1 AGI / J-2 強い AI ／ 弱い AI / J-11 Deep Learning / J-14 LLM
- J-30 第 4 世代コンピューター / J-31 第 5 世代コンピューター
- J-40 IoT / J-41 DX

## 採番の運用ルール（v0.5 で確定）

1. **形式**: `{英大文字1字}-{連番}[-{派生}]`（例 `B-15`、`D-2`、`C-1-a`）
2. **1 始まり**: 各サブ範囲は 1 から連番（A-1, B-1, ...）
3. **サブ範囲は 10 番刻みを基本**: A-1〜9／A-10〜19 のようにサブ分類単位で割り当てる。サブが膨らむときは 20 番幅・30 番幅で予約（例: D-30〜34 xAI 系 / D-35〜39 その他クローズド）
4. **欠番は詰め直さない**: 削除や移設で空いた番号はそのまま欠番として残す
5. **renumber は草案期のみ**: 初版確定前（本 v0.5 時点）は構造整理のため renumber 許容。初版以降は `legacy_id` を残して移す方式に切り替え、本体 ID は変えない
6. **上限は設けない**: letter 毎に 200〜300 番までは自然に伸びる前提。運用上の上限管理はしない
7. **ページ番号は誌面組み時に決める**: ID とページ番号は独立
8. **派生 ID（-a, -b）**: 同一テーマの時期差分・比較分冊にだけ使う。本体 ID と区別しやすく保つ

### 今回（v0.5）で確定させたこと

- 大分類 **ABCDEFGHIJ の 10 区切り**を確定
- 掲載順（A→J→B→C→D→E→F→G→I→H）を確定
- サブ範囲の設計粒度（10 番刻み基準、必要に応じて幅を広げる）を確定
- renumber は本 v0.5 で最後にして、以降は固定方針

### 今後触らない原則

- **letter の再割り当てはしない**（ABCDEFGHIJ を動かさない）
- **サブ範囲の意味も揺らさない**（例：D-30〜34 は xAI 系で固定）
- 追加は空き番号・空きサブ範囲・末尾サブ新設のいずれかで対応
- どうしても renumber が必要になった場合は `legacy_id` で相互参照を残す

## 切替の段取り（設計のみ・実施は未定）

- [ ] 大分類（8区切り）とサブ範囲の採択を確定
- [ ] `ledgers/entries.csv` に `new_id` と `legacy_id` 列を追加
- [ ] 本文 YAML の `id:` を順次差し替え
- [ ] ファイル名は最後にまとめてリネーム

## 未決の論点

1. **歴史（H-50〜）を個別エントリか、1 本の通し読み記事か**
2. **派生 ID（`-a`, `-b`）を誌面に出すか、裏台帳のみか**
3. **10 番刻みのサブ範囲を全区切りで採用するか、必要になるまで決めないか**
4. **IDE の扱い**：サービスとしての `B-30 VS Code` と道具としての `F-30 VS Code` をどう整理するか（2 エントリに分ける／どちらか片方に寄せる）
5. **MCP 連携相手サービスの扱い**：B（サービス）側にも独立エントリを作るか、I 側だけに寄せるか（例：Linear を `B-40` に立てるか、`I-31 Linear MCP` の中でカバーするか）
