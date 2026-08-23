# Stage 6 ブリーフ（2026-08-23）— D 系モデル系統 4 件

*台帳に行はあるのにファイルが生成されていなかった 18 件のうち、D 章のモデル系統 4 件を本書きするための下準備メモです。[ledgers/stage5_briefs_2026-08.md](stage5_briefs_2026-08.md) と同じ役割で、entry-writer サブエージェントに渡す前提で書いています。*

## この束の性格 — 時変情報のかたまり

モデル系統のページは、**書いた瞬間から古くなる**種類の原稿です。

- `evaluation_date: 2026-08-23` を必ず入れる。出典メモは `— checked 2026-08-23`
- **「最新」「現行」と書かない**。書くなら「2026-08 時点では」と時点を添える
- 価格・文脈長・モデル ID のような数字は、**公式ドキュメントで確認できたものだけ**書く
- 既存の D-2 Gemini 2.5 系 / D-11 Claude 3.5 系 / D-12 Claude 4 系 / D-22 o1 系 を読み、書き方と密度を揃えること

## 使い方

- 「押さえる事実」は 2026-08-23 に確認した内容です。Claude 系は Anthropic 公式ドキュメント（モデル一覧・提供終了ページ）が一次情報です
- 「書かないこと」は、隣接エントリとスコープが被るため触れない範囲です

---

## D-3 Gemini 3 系

- **位置づけ**：D-2 Gemini 2.5 系の次の世代。後継の 3.1 系は D-4 が扱うので、ここは 3 系そのものに徹する
- **押さえる事実**：**2025 年 11 月 18〜19 日**に Gemini 3 Pro が公開され、推論とマルチモーダルが大きく伸びた世代とされる／**2025 年 12 月 18 日**に Gemini 3 Flash が加わった。Pro のマルチモーダル・コーディング・エージェント機能を受け継ぎつつ、コストを大きく下げた位置づけ／Flash は前世代の上位モデル（Gemini 2.5 Pro）を上回る性能を、より速い処理で出したと案内されている／さらに深く考えさせる Deep Think という使い方も用意されている／世代の中では Pro が賢さ寄り、Flash が速さと安さ寄り、という H-57 で説明した読み方がそのまま当てはまる
- **出典**：Google「Gemini 3」<https://blog.google/products/gemini/gemini-3/>、Google DeepMind のモデル一覧 <https://deepmind.google/models/gemini/>、Google Cloud ブログ（Gemini 3 Flash）<https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-flash-for-enterprises>
- **書かないこと**：3.1 系（D-4）、命名の体系そのもの（H-57）、サービスとしての Gemini（B-1）
- 目安 reader_level 2-3 / importance B / figure_type comparison

## D-10 Claude 3 系

- **位置づけ**：**Claude の型が決まった世代**。今も続く「Opus / Sonnet / Haiku」という 3 兄弟の呼び方はここから始まった。2026-08 時点では全モデルが提供終了しており、**歴史として読む 1 本**になる
- **押さえる事実**：**2024 年 3 月 4 日**（日本時間 3 月 5 日）に発表され、Opus・Sonnet・Haiku の 3 つが同時に示された／名前は詩の形式に由来し、俳句（短い）→ ソネット（定型詩）→ 大作（Opus）と、そのまま大きさの順を表す。この命名の型が以降のすべての世代に受け継がれた／当時の最上位 Opus は GPT-4 と比較される水準として受け止められ、Anthropic が主要ベンダーとして広く認識される節目になった／モデル ID は `claude-3-opus-20240229` / `claude-3-sonnet-20240229` / `claude-3-haiku-20240307`／**提供終了は Sonnet 3 が 2025 年 7 月 21 日、Opus 3 が 2026 年 1 月 5 日、Haiku 3 が 2026 年 4 月 20 日**。この世代は 2026-08 時点で公式のモデル一覧に載っていない／読者にとっての要点は「モデルには寿命があり、使っていたものが数年で使えなくなる」という事実
- **出典**：Anthropic「Model deprecations」<https://platform.claude.com/docs/en/about-claude/model-deprecations>、Anthropic「Models overview」<https://platform.claude.com/docs/en/about-claude/models/overview>
- **書かないこと**：3.5 系（D-11）、4 系の総論（D-12）、バージョン史の通し（H-56）
- 目安 reader_level 2-3 / importance C / figure_type timeline

## D-13 Claude 4.5 系

- **位置づけ**：D-12「Claude 4 系」が族の総論を担い、**こちらは 4.5 世代 1 つに絞った深掘り**（D-12 のコミュニティ補完メモで明示的にそう分担されている）。Claude Code が広まった時期の主力帯にあたる
- **押さえる事実**：3 つのモデルが順に出た世代で、**Sonnet 4.5 が 2025 年 9 月 29 日**（`claude-sonnet-4-5-20250929`）、**Haiku 4.5 が 2025 年 10 月 1 日**（`claude-haiku-4-5-20251001`）、**Opus 4.5 が 2025 年 11 月 1 日**（`claude-opus-4-5-20251101`）／いずれも文脈は 20 万トークン、最大出力は 6.4 万トークン／API 価格は Sonnet 4.5 が 100 万トークンあたり入力 3 ドル・出力 15 ドル、Haiku 4.5 が 1 ドル・5 ドル、Opus 4.5 が 5 ドル・25 ドル／**2026-08 時点でも 3 つとも提供中**で、公式は退役予定日を「Sonnet 4.5 は 2026 年 9 月 29 日より前にはしない」「Haiku 4.5 は 2026 年 10 月 15 日より前にはしない」「Opus 4.5 は 2026 年 11 月 24 日より前にはしない」と案内している／とくに **Haiku 4.5 は 2026-08 時点の公式モデル比較表にも現行モデルとして載っており**、速さ重視の枠として長く使われている
- **出典**：Anthropic「Models overview」<https://platform.claude.com/docs/en/about-claude/models/overview>、「Model deprecations」<https://platform.claude.com/docs/en/about-claude/model-deprecations>
- **書かないこと**：4 系全体の流れ（D-12）、Claude Code の使い方（B-7）、バージョン史の通し（H-56）
- 目安 reader_level 2-3 / importance B / figure_type comparison

## D-23 o3 系

- **位置づけ**：D-22「o1 系」の後継。「考えてから答える」路線が実用に入った世代
- **押さえる事実**：**o3-mini が 2025 年 1 月 31 日**、**o3 が 2025 年 4 月 16 日**、**o3-pro が 2025 年 6 月 10 日**に公開された／o1 の後継として、答える前に段階的に考える時間を取る設計を引き継いでいる／OpenAI は、外部の専門家評価で o3 が難しい実務タスクにおいて o1 より重大な誤りを約 20% 減らしたと説明している／o3-pro はより長く考える版で、Web 検索・ファイル解析・画像を使った推論・Python 実行などの道具も使える／o3-mini は科学・数学・コーディングに強みを持ちつつ、費用と待ち時間を抑えた枠／o3 と同時に o4-mini も公開されている
- **出典**：OpenAI「Introducing OpenAI o3 and o4-mini」<https://openai.com/index/introducing-o3-and-o4-mini/>、OpenAI「OpenAI o3-mini」<https://openai.com/index/openai-o3-mini/>
- **書かないこと**：o1 系そのもの（D-22）、GPT-5 系（D-20）、Thinking モデルの一般論（G-14）
- 目安 reader_level 2-3 / importance C / figure_type comparison
