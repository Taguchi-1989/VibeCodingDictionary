# 鮮度監査ログ（手で書く台帳）

*「いつ・どの範囲を・何を見て確認し、何を直したか」を残す監査履歴です。自動生成の [freshness_queue.md](freshness_queue.md) と対で使います。*

キューは「今どこが古いか」のスナップショットなので、時間が経つと上書きされて消えます。
**何をもって「確認した」と言えるのか**を後から辿れるように、監査した範囲はここに 1 行足してください。
刊行前に「この本の事実はいつ時点のものか」を説明する根拠にもなります。

## 書き方

| 日付 | 範囲 | 件数 | 見た一次情報 | 結果 | 記入者 |
| :-- | :-- | --: | :-- | :-- | :-- |

- **範囲**: `D 章 model 全件` / `B-1〜B-12` / `F-model-anthropic の影響エントリ`（[volatile_facts.md](volatile_facts.md) の事実 ID）のように、後から再現できる粒度で
- **見た一次情報**: 公式ドキュメント・料金ページ・リリースノートなど。URL は代表 1 本で構いません
- **結果**: `変更なし（last_audited のみ更新）` / `n 件改訂（内容）` のように、直したか直していないかが分かるように
- 確認したエントリは frontmatter の `last_audited` を確認日に更新してください。`evaluation_date` は執筆時点の記録なので動かしません

---

## 履歴

| 日付 | 範囲 | 件数 | 見た一次情報 | 結果 | 記入者 |
| :-- | :-- | --: | :-- | :-- | :-- |
| 2026-09-19 | 仕組み導入（監査はまだ未実施） | — | — | `last_audited` / `volatility` を schema v2.31.0 に追加し、`scripts/audit_freshness.py` と `freshness_queue.md` を新設。初回走査で Tier S の期限超過 131 件（service 38 / model 34 / benchmark 19 / mcp 11 / その他 29）を検出 | Claude Code |
| 2026-09-19 | 時変ファクト watchlist を新設（監査はまだ未実施） | — | — | `volatile_facts.yaml` に事実 15 件を定義し、`update_volatile_facts.py` が影響エントリを自動収集する形に。`touch_last_audited.py` で確認済みの一括押印も可能に。15 件すべて `last_checked` 未記入＝未確認の状態 | Claude Code |
| 2026-09-19 | `F-model-anthropic` / `F-model-openai` / `F-model-openai-reasoning` / `F-model-google` の 4 事実（D 章モデルエントリ中心） | 15 | Anthropic モデル一覧・OpenAI Models / Deprecations・Google Gemini models（いずれも検索経由。環境のネットワークポリシーで公式ページの直接取得は不可） | **世代が 1〜2 段ずれていることを確認**。D-22 / D-23 の `version_status` を実態に合わせて `deprecated` に修正（D-23 は値が空欄だったデータの穴も解消）。10 件は記述が今も正しいと確認して `last_audited` を押印。4 件（D-11 / D-12 / D-13 / D-20）は記述が古く**要改訂として押印を見送り**。2 件（D-14 / D-26）は未確認 | Claude Code |
| 2026-09-19 | 上記で要改訂とした D-11 / D-12 / D-13 / D-20 の本文改訂 | 4 | Anthropic news「Introducing Claude Opus 4.8」（2026-05-28 公開）・OpenAI「GPT-6 Astra」（いずれも検索経由） | **4 件とも改訂して `last_audited` を押印**。「現行」「主力」という書き方を年基準に改め、D-12 には欠落していた Opus 4.8 を版の流れに追加。validator は 4 件とも全チェック通過。期限超過 124 → 121 件 | Claude Code |
| 2026-09-19 | 上記改訂の取りこぼし修正（PR #60 のレビュー指摘より） | 3 | エントリ内の退役予定日との突き合わせ | **裏台帳メモの直し忘れ 2 件**（D-20 の誌面ポンチ絵メモとコミュニティ補完メモ、D-11 のコミュニティ補完メモに「現行フラッグシップ」「現行主力の 4 系」が残存）と、**D-13 の公開日の誤り 2 件**（Haiku 4.5 を 2025-10-01 → 2025-10-15、Opus 4.5 を 2025-11-01 → 2025-11-24）を修正 | Claude Code |
| 2026-11-06 | `F-model-anthropic` / `F-model-openai` / `F-model-google` / `F-model-xai`（新設）/ `F-price-claude` / `F-bench-aa-index`（新設）の影響範囲＋ D 章の世代交代 | 25 | **Anthropic は公式を直接確認**（platform.claude.com の Models overview・Model deprecations・Effort、anthropic.com の各モデル発表・CVP・蒸留対策、claude.com/pricing、code.claude.com の Fast mode）。**OpenAI・Google・xAI・Artificial Analysis・Wikipedia は環境のネットワーク制限で直接取得できず検索経由** | **新規 11 件**（D-5 / D-6 / D-15 / D-16 / D-17 / D-27 / D-48 / E-52 / G-52 / J-151 / J-152、いずれも needs_review）。**改訂 14 件**: D-14 を `deprecated` に（2026-06-09 非推奨、後継 D-16）、G-9 の tagline の誤り「既定は high」を訂正（Opus 5.5 / Haiku 5.5 は medium）、G-24 に Claude API 版 2026-10-21 での temperature 削除、B-50 を個人 4 段 Free〜Ultra に訂正（旧 Max 20x → Ultra）、D-12 / D-13 に退役・非推奨日、D-4 / D-20 / D-30 / D-44 / D-46 / G-14 / C-2 / G-22 に後継・提供状況を追記。いずれも `last_audited: 2026-11-06` | Claude Code |

---

## 監査で見つかった要対応（2026-09-19）

### A. 記述が古いエントリ → ✅ 改訂済み（2026-09-19）

| ID | 用語 | 何が古かったか | どう直したか |
| :-- | :-- | :-- | :-- |
| D-12 | Claude 4 系 | tagline「4.7 が現行の主力」。Claude 5 世代が出ており現行ではない。版の流れに 4.8 が欠落 | 「2025〜2026 年の主力でした」に。タイムラインに 4.8（2026-05）を追加し、後継が Claude 5 世代であることを明記 |
| D-13 | Claude 4.5 系 | 「2026-08 時点では Sonnet 4.5 が中心」。中心ティアが変わっている | 「2025 年秋からの一時期は」に。会話例も過去形の言い回しへ |
| D-11 | Claude 3.5 系 | 「4 系（現行）か 3.5 系（過去）か」という二分。4 系も過去世代 | 「後続世代」という書き方に変更（特定の世代名に依存させない） |
| D-20 | GPT-5 系 | 「現行フラッグシップ」「ChatGPT と API の中心を担います」 | 「5.6 まで版を重ねます」「2025 年から 5.6 まで…担いました」に。GPT-6 Astra の登場を備考に記載 |

いずれも誌面の字数・構造・トーンは validator で全チェック通過しています。4 件とも `last_audited: 2026-09-19` を押印済みです。

**編集上の示唆**: tagline が年で固定されているもの（D-20「OpenAI の 2025 年フラッグシップ世代」、D-2「2025 年 3 月公開の…」など）は**今も正しいまま**でした。古くなったのは例外なく「現行」「最新」「主力」と書いた箇所です。**時点は年で固定して書く**方が陳腐化しにくい、というのが今回いちばん再利用できる学びです。新規執筆・改訂のときはこの方針で書いてください。

また、特定の後継世代名（「Claude 5 が現行」など）を書き込むと次の世代交代でまた古くなるため、D-11 では「後続世代」という**世代名に依存しない書き方**を採りました。固有名は「その世代自身の話」にだけ使うのが安全です。

**監査で踏んだ落とし穴（次回への申し送り）**:

1. **裏台帳メモを見落としやすい**。誌面本文だけ直して `last_audited` を押すと、`誌面ポンチ絵メモ`（デザイン担当への指示書）と `コミュニティ補完メモ` に古い表現が残ります。図が起こされた時点で誌面と矛盾するので、**改訂時は裏台帳メモまで grep してください**（`grep -n "現行\|最新\|主力" <file>`）。
2. **`last_audited` を押すとキューから消える**。押印前に、そのエントリ全体を読んで他の事実も確かめること。今回は D-13 の公開日が 2 件間違っていたのに、モデル世代の事実だけ見て押印してしまいました。
3. **退役予定日は公開日の裏取りに使えます**。Anthropic の「◯◯ より前にはしない」という退役予定日は公開のちょうど 1 年後で揃うため、公開日の検算に使えます（Sonnet 4.5: 公開 2025-09-29 / 退役 2026-09-29）。

### B. 収録漏れ（新エントリの要否は著者判断）

本書の D 章はモデル世代が 1〜2 段ぶん止まっています。

| 空いている範囲 | 実際に出ているもの |
| :-- | :-- |
| Claude 5 世代 | Opus 5（1M 文脈）/ Sonnet 5 / Fable 5.1 / Mythos 5.1、Opus 4.8（2026-05-28） |
| GPT-6 / GPT-5.6 世代 | GPT-6 Astra（フラッグシップ）、GPT-5.6 Sol / Terra / Luna、GPT-5.3-Codex |
| Gemini 3.5〜3.8 世代 | 3.5 Flash / 3.5 Flash-Lite / 3.6 Flash / 3.7 Flash / 3.8 Flash |

### C. 未確認のまま残したもの

D-14 Claude Mythos Preview（Mythos 5.1 が公開されており位置づけの確認が要る）、D-26 gpt-oss（後続版の有無を未確認）。

---

## 未監査の残り（2026-09-19 時点）

初回走査の結果です。上から束で片付けるのが速い順に並べています。

| 優先 | 範囲 | 件数 | 確認ポイント |
| :-- | :-- | --: | :-- |
| 1 | D 章 model | 34 | 後継モデルの有無・提供終了・コンテキスト長。一次情報が各社 1 ページに集まるので最も安く回せます |
| 2 | B 章 service | 38 | 料金プラン・無料枠・名称変更。`価格` シグナルが出ているものを優先 |
| 3 | E 章 benchmark | 19 | スコアと上位モデルの入れ替わり。数字の裏取りが要るので時間がかかります |
| 4 | I 章 mcp | 11 | 公式／コミュニティの別・配布場所・対応クライアント |
| 5 | その他（person_org 7 / term_tool 6 / term_general 6 / term_llm 5 / tool_agent 4 / history 1） | 29 | Tier 判定が実態と合わないものは `volatility: low` で落とす |

最新の内訳は `python3 scripts/audit_freshness.py` を走らせて [freshness_queue.md](freshness_queue.md) を見てください。


---

## 2026-11-06 監査のメモ

### 見つかった誤り（AI が書いた本文が、外の世界の変化で誤りになったもの）

| ID | 何が誤りになっていたか | どう直したか |
| :-- | :-- | :-- |
| G-9 effort レベル | tagline・本文・会話例が「既定は high」。Claude Opus 5.5（2026-09-22）と Haiku 5.5（10-07）で既定が medium に変わった | 「既定値はモデルで違う」に。見どころ 5 も「まず既定値で」に |
| B-50 Claude の料金プラン | 「個人 4 段（Free〜Max）」「Max 5x / 20x」。月 $200 の段が Ultra という別プランになっていた | 「Free〜Ultra」に。備考に 2026-11-06 時点の全プラン価格 |
| D-14 Claude Mythos Preview | `version_status: preview`、「提供されている」。2026-06-09 に非推奨 | `deprecated` に。開発フロー Step 4 を後継 D-16 へ |
| G-24 Temperature | 「非推奨・既定以外はエラー」まで。2026-10-21 の API 版でパラメータ自体が削除 | 備考を更新 |

**教訓（2026-09-19 の学びの再確認）**: 誤りになったのは今回も「既定は high」「4 段（Free〜Max）」のように**その時点の値を一般論の形で書いた箇所**でした。tagline に既定値・段数を入れると、1 モデルの追加でそのまま誤りになります。

### 確認できなかったもの（次回）

- OpenAI・Google・xAI・Artificial Analysis の一次情報（環境の許可ホストに `openai.com` / `developers.openai.com` / `blog.google` / `ai.google.dev` / `docs.x.ai` / `artificialanalysis.ai` が無い）。D-5 / D-6 / D-27 / E-52 の数字は二次情報で、各エントリの備考に「一次未確認」と明記済み
- D-27 の GPT-6.1 Terra の価格（$1/$5 と $6/$18 で報道が食い違い）、GPT-6 Astra の一般提供の時期
- D-16 Fable 5.1 / Mythos 5.1 の公開日（退役予定日からは 2026-09-01、Anthropic のニュース一覧では 2026-09-15）。本文は「2026 年 9 月」で止めた
- 未着手のモデルエントリ: D-26 gpt-oss / D-40 Llama / D-41 Mistral / D-42 Gemma / D-43 Qwen（3.8 系が出ている）/ D-45 GLM（5.2・5.3 が出ている）/ D-55 Nano Banana（2.1 が 2026-10 に GA と報道）ほか画像・動画系
- `model_snapshots.csv` の 2026Q4 行（四半期末に取る。候補: Opus 5.5 $4/$20、Sonnet 5.5 $2/$10、Haiku 5.5 $0.10/$0.50、Fable 5.1 $10/$50、Gemini 4 Argon、GPT-6.1 Sol、Grok 4.7）

---

## 2026-11-13 監査のメモ（Stage 16）

- **確認した事実**: F-model-anthropic（Fable 5.2 / Mythos 5.2、anthropic.com/claude/fable を直接取得）／F-model-google（Gemini 4 Hydrogen、検索経由）／F-model-meta（Muse 系、検索経由。pattern に Muse を追加）／F-bench-aa-index（首位が Fable 5.2 に、検索経由）
- **押印**: D-6 / D-16 / D-40 / E-3 / E-26 / E-52 / G-20。新規 D-36 / E-35 / E-53 / E-54 / H-65
- **古くなっていた記述**: D-6「Argon・Carbon の 2 本」→ Hydrogen で 3 本／E-26 の出会い方と会話例が「30% 台」前提 → 2026-11 に「ツールあり」で 7 割台／G-20 の開発フローが「言語・スタイル・禁止事項をまとめる」→ 公式は「コードから分からないことだけ」
- **確認できなかったもの**: Meta・Google DeepMind・arXiv・tbench.ai・Artificial Analysis・claude.dev（許可ホスト外）。RoboDojo の公式順位表、Terminal-Bench 4.0 の首位（報道が割れている）、HLE-Diamond の公開日（09-22 と 10-30 の 2 説）

