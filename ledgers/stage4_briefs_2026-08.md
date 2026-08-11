# Stage 4 ブリーフ（2026-08-10）— 台帳登録済み・未生成だった技術寄り 8 件

*`ledgers/entries.csv` に行はあるのにファイルが生成されていなかったエントリのうち、技術寄りの 8 件を本書きするための下準備メモです。[ledgers/stage3_briefs_2026-08.md](stage3_briefs_2026-08.md) と同じ役割で、entry-writer サブエージェントに渡す前提で書いています。*

## 使い方

- 「押さえる事実」は 2026-08-10 に web で確認した内容です。**出典メモにはここに挙げた URL と `checked 2026-08-10` を書いてください**
- 数字・バージョンは時変情報です。`evaluation_date: 2026-08-10` を必ず入れる
- 「書かないこと」は、隣接エントリとスコープが被るため触れない範囲です

## この束の位置づけ

F-210 / F-211 / F-212 は「型・スキーマ・API 契約パック」の 3 本セットで、先に書いた **F-213 API** が参照したくてもできなかった相手です。G 系 5 本は Claude Code・LLM の設定まわりで、読者が画面や設定ファイルで直接触る語が中心になります。

## 事実の扱いで注意すること

- **effort レベル**：まとめ記事はモデル名や段数の記述がまちまちです。**公式ドキュメント（platform.claude.com の Effort ページ）を採用**し、5 段階（low / medium / high / xhigh / max）・既定は `high` として書いてください。特定モデルの推奨値は変動が速いので、モデル名を挙げた細かい推奨は書かない
- **OpenAPI**：「4.0 が出た」と書かない。**現行は 3.2.0（2025-09 リリース）**で、4.0（Project Moonwalk）は設計段階です
- **Zod**：v4 が現行。「14 倍速い」のような数値はベンダー・ブログ由来なので本文には入れず、必要なら備考に留める
- **ベクトル DB**：製品ごとの優劣は断定しない。「手元の Postgres に載せる pgvector」「運用を任せるマネージド」という**選び方の軸**で書く

---

## F — 型・スキーマ・API 契約

### F-210 JSON Schema

- **位置づけ**：「データの形を決めておく」の共通土台。F-211 Zod・F-212 OpenAPI・G-48 Structured Outputs がすべてこれに乗っている
- **押さえる事実**：JSON データの構造（どのキーが必須か、型は何か、取りうる値は何か）を JSON 自身で書き表す仕様／書いたスキーマで実データを検証でき、多くの言語に実装がある／現行の版は Draft 2020-12 で、`prefixItems` / `items` の整理や `$dynamicRef` の導入などが入った／LLM に「この形で答えて」と指定するときの共通語にもなっている（G-48）
- **出典**：<https://json-schema.org/>、Draft 2020-12 <https://json-schema.org/draft/2020-12>
- **書かないこと**：Zod の書き味（F-211）、API 全体の設計（F-212）
- 目安 reader_level 3-4 / importance D / figure_type structure

### F-211 Zod

- **位置づけ**：TypeScript を書く人がいちばん最初に触る「形の検証」ライブラリ。AI に「Zod でスキーマ切って」と頼む場面が多い
- **押さえる事実**：TypeScript 向けのスキーマ定義・検証ライブラリで、スキーマを書くと**その型が自動で TypeScript の型として使える**（二重管理が要らない）のが最大の特徴／フォーム入力・API のレスポンス・環境変数など「外から来る値」を境界で検証する用途／現行は v4 で、内部が書き直され、文字列フォーマットが `z.email()` のようなトップレベル関数になるなどの変更が入った／Standard Schema という共通インターフェースに対応し、他の検証ライブラリと差し替えやすくなっている
- **出典**：<https://zod.dev/>、リリース一覧 <https://github.com/colinhacks/zod/releases>
- **書かないこと**：TypeScript の型システム一般（F-2）、JSON Schema の仕様（F-210）
- 目安 reader_level 3-4 / importance D / figure_type structure

### F-212 OpenAPI

- **位置づけ**：API の「取扱説明書」を機械可読で書く標準。F-213 API の次に来る語
- **押さえる事実**：Web API のエンドポイント・パラメータ・レスポンスの形を、決まった書式（YAML / JSON）で記述する仕様／書いておくと、ドキュメント生成・クライアントコードの自動生成・モックサーバー・テストがそこから作れる／2026-08 時点の現行版は **3.2.0（2025-09 リリース）**で、3.1 からの破壊的変更はなく、ストリーミング対応やタグの階層化などが加わった／次期メジャー版 4.0 は「Project Moonwalk」として設計が進んでいる段階で、まだリリースされていない／旧称 Swagger で、ツール名としては今も Swagger UI 等が使われる
- **出典**：<https://www.openapis.org/>、仕様 <https://spec.openapis.org/oas/latest.html>、Moonwalk SIG <https://github.com/OAI/sig-moonwalk>
- **書かないこと**：API そのものの説明（F-213）
- 目安 reader_level 3-4 / importance D / figure_type structure

---

## G — バイブコーディング特有の言葉

### G-8 決定論的／非決定論的

- **位置づけ**：「同じことを聞いたのに毎回答えが違う」の正体。G-24 Temperature の親にあたる概念
- **押さえる事実**：同じ入力に対して必ず同じ出力が返るのが決定論的、返るとは限らないのが非決定論的／従来のプログラムは基本的に決定論的で、だからテストが書ける／LLM は確率的に次の語を選ぶため非決定論的で、設定を固定しても完全な再現は保証されない／この性質が「テストしづらい」「同じ手順でも結果が揺れる」というつまずきの根っこになる／付き合い方は、揺れても困らない使い方（案出し）と、揺れると困る使い方（分類・抽出）を分け、後者は出力の形を縛る（G-48）
- **出典**：<https://platform.claude.com/docs/en/api/messages>、<https://ai.google.dev/gemini-api/docs/text-generation>
- **書かないこと**：Temperature の設定値の話（G-24）
- 目安 reader_level 2-3 / importance C / figure_type comparison

### G-9 effort レベル

- **位置づけ**：Claude Code や API で読者が直接指定する設定値。「賢さと速さとコストのつまみ」
- **押さえる事実**：応答にどれだけトークンを使うかを指定するパラメータで、**low / medium / high / xhigh / max の 5 段階**／**既定は `high`**（`high` を指定することと、指定しないことは同じ挙動）／思考の量だけでなく、ツール呼び出しの回数や説明の丁寧さも含めて応答全体に効く／トークン予算そのものではなく「振る舞いの signal」で、低くしても難しい問題では考える／低いほど速く安く、高いほど深く探索する／会話の途中で値を変えるとプロンプトキャッシュが効かなくなる
- **出典**：Anthropic 公式「Effort」<https://platform.claude.com/docs/en/build-with-claude/effort>
- **書かないこと**：特定モデルごとの推奨値（変動が速い）、Thinking の詳細（G-14）
- 目安 reader_level 2-3 / importance C / figure_type comparison

### G-17 ベクトル DB

- **位置づけ**：G-15 RAG・G-16 Embedding の受け皿。「社内文書を AI に読ませる」話で必ず出てくる
- **押さえる事実**：文章を数値の並び（ベクトル、G-16）に変換して保存し、「意味が近いもの」を高速に探すためのデータベース／キーワード一致ではなく意味の近さで引けるので、言い回しが違っても該当箇所を拾える／RAG の「関連する資料を探してくる」部分を担う／選び方の軸は、既に PostgreSQL があるなら拡張機能の pgvector を載せる、運用を任せたいならマネージドサービス、自前で速度と絞り込みを詰めたいなら専用の OSS、という 3 択／件数が数万〜数十万程度なら専用製品を入れなくても足りることが多い
- **出典**：<https://github.com/pgvector/pgvector>、<https://www.pinecone.io/>、<https://qdrant.tech/>
- **書かないこと**：RAG の流れ全体（G-15）、Embedding の仕組み（G-16）
- 目安 reader_level 3-4 / importance C / figure_type structure

### G-45 段階的開示

- **位置づけ**：Skill（G-22 SKILL.md）や CLAUDE.md（G-20）が「なぜあの形なのか」の答え。文脈を食い潰さないための設計思想
- **押さえる事実**：必要になった分だけ情報を読み込ませる考え方／全部を最初から文脈に載せると、それだけで文脈の枠を使い切ってしまうため、まず「見出しだけ」を持たせ、使うと決まったときに本体を読ませ、さらに必要なら参照ファイルを開かせる、という段階に分ける／Agent Skills はこの三段構えで作られていて、1 つのスキルの見出しぶんは百トークン程度に収まるため、スキルを増やしても常時の負担がほとんど増えない／同じ発想は CLAUDE.md や README を「入口だけ短く、詳細はリンク先」に書く指針としても効く／人間向け UI 設計の用語がもとで、初心者には基本だけ見せ、慣れた人に詳細を出す考え方
- **出典**：Anthropic「Agent Skills」<https://platform.claude.com/docs/ja/agents-and-tools/agent-skills/overview>
- **書かないこと**：SKILL.md の書式（G-22）、Auto-compact（G-47）
- 目安 reader_level 3-4 / importance C / figure_type structure

### G-48 Structured Outputs

- **位置づけ**：「AI の答えをプログラムで受け取る」ための仕組み。F-210 JSON Schema と G-33 Function Calling の間に立つ
- **押さえる事実**：出力の形をスキーマ（多くは JSON Schema）で指定し、その形どおりの応答を得る機能／「JSON で返して」とお願いするだけの方式と違い、必須項目の欠落や型の食い違いが起きないため、後続の処理がそのまま書ける／主要各社が対応しており、Anthropic は 2026-02 に一般提供を開始した／実現方式は各社で違い、生成時に形を強制する方式と、ツール呼び出しの仕組みを使う方式がある／表を作る・分類する・項目を抜き出す、といった業務寄りの用途と相性が良い
- **出典**：Anthropic <https://platform.claude.com/docs/en/build-with-claude/structured-outputs>、OpenAI <https://developers.openai.com/api/docs/guides/structured-outputs>
- **書かないこと**：Function Calling の仕組み（G-33）、JSON Schema の仕様（F-210）
- 目安 reader_level 3-4 / importance C / figure_type structure
