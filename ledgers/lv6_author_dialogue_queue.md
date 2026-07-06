# Lv6 自己学習シェルフ 著者欄 対話記入キュー

*2026-06-22 作成。Lv6（reader_level 6・刊行スコープ外）16 本の著者記入欄を、**著者の口述 → Claude が転記**する対話形式で効率よく埋めるためのドライバです。*

## 使い方

1. このファイルを開いて、上から1本ずつ進める。
2. 各エントリの「聞くこと」を Claude が質問 → 著者が口頭/メモで答える。
3. Claude が答えを各 md の **user-input ブロック**（`## 非エンジニアのつまずき` / `## 私のコメント`）に転記する。
   - 転記先マーカー: `<!-- user-input:start key="stumble" -->` と `key="my_comment"`。
   - 著者本人の言葉だけを入れる。Claude は事実補足を勝手に本文化しない（CLAUDE.md §3）。
4. 埋めたら下のチェックを ☑ にする。

> Lv6 は自己学習ノートなので、本書の「非エンジニア読者向け」より **自分用の理解メモ**として書いてOK。
> - `## 非エンジニアのつまずき` → ここでは「**自分が最初どこで引っかかったか / まだ曖昧な点**」として使う。
> - `## 私のコメント`（🙂 第一印象 / 👍 良い点 / 👎 ダメな点 / 👥 誰向けか）→「腹落ちした瞬間 / 実務でどう効くと感じたか / まだ腑に落ちない所 / これを知ると良い人」に読み替えてOK。

---

## 推論の効率化

### ☐ J-29 KV Cache — `content/entries/term_general/J-29_kv_cache.md`
- 聞くこと: 「K と V だけ使い回す」がスッと入った？ どこで「あ、なるほど」と思った？／メモリと速度のトレードオフ、実務でどう効くと感じる？

### ☐ J-30 Flash Attention — `content/entries/term_general/J-30_flash_attention.md`
- 聞くこと: 「中間行列を書き出さない（IO を削る）」と「再計算を省く KV Cache」の違いは腹落ちした？／SRAM/HBM のメモリ階層の話で曖昧な所は？

### ☐ J-82 投機的デコード — `content/entries/term_general/J-82_speculative_decoding.md`
- 聞くこと: 「品質を変えずに速くなる」のカラクリ（受理/棄却）は納得した？／ドラフトモデルの的中率に効く、という感覚はある？

## アーキテクチャの中身

### ☐ J-24 Encoder-Decoder — `content/entries/term_general/J-24_encoder_decoder.md`
- 聞くこと: cross-attention と self-attention の違いは区別できた？／「なぜ今の LLM は Decoder-only に寄ったか」は納得した？

### ☐ J-27 RoPE — `content/entries/term_general/J-27_rope.md`
- 聞くこと: 「回転で相対位置を埋め込む」は直感的に掴めた？ どこが難しかった？／長文脈化（YaRN 等）の土台、という位置づけはピンと来た？

### ☐ J-28 MLA — `content/entries/term_general/J-28_mla.md`
- 聞くこと: GQA（ヘッド共有）と MLA（低ランク圧縮）の「削り方の違い」は区別できた？／DeepSeek/GLM が使う理由は腹落ちした？

### ☐ J-86 GQA — `content/entries/term_general/J-86_gqa.md`
- 聞くこと: MHA→GQA→MQA の「ほどよい中間」の感覚は掴めた？／KV キャッシュ削減との関係は？

### ☐ J-87 QK-Norm — `content/entries/term_general/J-87_qk_norm.md`
- 聞くこと: 「内積が暴走して softmax が固まる」問題はイメージできた？／1/√d との違いで引っかかった所は？

### ☐ J-88 MTP — `content/entries/term_general/J-88_mtp.md`
- 聞くこと: 「学習の工夫」と「投機的デコードのドラフト」を1つの仕組みで兼ねる、は納得した？／どこが新鮮だった？

## 表現・基礎の数理

### ☐ J-25 Tokenizer・BPE — `content/entries/term_general/J-25_tokenizer_bpe.md`
- 聞くこと: 「日本語がトークンを食う」理由は腹落ちした？／課金・コンテキスト長の物差し、という実感はある？

### ☐ J-26 潜在空間 — `content/entries/term_general/J-26_latent_space.md`
- 聞くこと: 「意味の近さ＝距離」の地図イメージは掴めた？／king−man+woman≈queen はピンと来た？ 曖昧な所は？

## MoE

### ☐ J-89 MoE ルーティング — `content/entries/term_general/J-89_moe_routing.md`
- 聞くこと: routing collapse（偏り）と loss-free 負荷分散の話は納得した？／sigmoid gating の意味で引っかかった所は？

## 推論基盤・運用

### ☐ J-83 vLLM — `content/entries/term_general/J-83_vllm.md`
- 聞くこと: PagedAttention と continuous batching の2本柱は区別できた？／「概念を実装に落とした道具」という位置づけは？

### ☐ J-84 バッチ推論 — `content/entries/term_general/J-84_batch_inference.md`
- 聞くこと: スループット↔レイテンシの綱引きは実感できた？／静的バッチと連続バッチの違いは？

### ☐ J-85 スループットとレイテンシ — `content/entries/term_general/J-85_throughput_latency.md`
- 聞くこと: TTFT と TPOT の違いは掴めた？／チャット vs バッチ処理で優先軸が変わる、は納得した？

### ☐ J-94 並列化戦略 — `content/entries/term_general/J-94_parallelism.md`
- 聞くこと: TP/PP/EP/DP の4軸は区別できた？／「1台で束ねる（バッチ推論）」と「複数台に分散（並列化）」の違いは？

---

## 進め方の提案

- 1 セッションで 3〜5 本ずつが目安（口述が続くと疲れるため）。
- 関連が近い順（KV Cache → GQA → MLA、など）でまとめて話すと記憶が繋がりやすい。
- 「まだ分からない」も立派な記入。`つまずき` 欄にそのまま残すと、後で深掘りの種になる。

---

## 進捗（2026-06-23 更新）

推論効率化シェルフ **16 本すべて著者欄記入済み**（J-24〜30, J-82〜89, J-94）。
半導体サプライチェーン系 Lv6 を新設: J-95 サプライチェーン / J-96 製造装置 / J-97 電子材料 / J-98 重要鉱物の地政学 / J-99 CoWoS / J-101 製造プロセス / J-102 チップレットと3D積層（＋刊行 C-15 Intel）。これら 8 本は本文執筆済み・validator パス・**著者欄は空**（次回口述記入待ち）。調査集約は [inference_hardware_landscape_2026.md](inference_hardware_landscape_2026.md)。

## 次セッションの深掘り候補（著者リクエスト 2026-06-23）

Lv6 を勉強用にもっと深く育てたい意向。次の 2 テーマを中心に「深掘り調査 → 構造理解 → Lv6 エントリ化」で進める。

1. **ループエンジニアリング系（最優先）** — エージェントのループ機構（ゴール→コマンド→ループ）、コンテキストエンジニアリング、ハーネス設計。J-94 で触れた「エージェント並列の抽象度ズレ」の延長。必要技術を洗い出してエントリ化。
2. **GLM 5.2 のアーキテクチャ** — 公開済みアーキの採用技術をまとめる。既存 Lv6 の MLA(J-28)/MoE ルーティング(J-89)/GQA(J-86)/MTP(J-88)/RoPE(J-27) と接続し、最新モデルの技術スタック実例集にする。

まず上記 8 本の空著者欄を口述記入で埋めつつ、深掘りテーマの調査に入るのが自然。
