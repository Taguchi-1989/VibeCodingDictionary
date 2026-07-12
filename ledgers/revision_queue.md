# 要直しキュー（revision queue）

*自動生成: 2026-07-12 20:04 / `scripts/update_review_queue.py`*

1 画面で「次やるべき・見直すべき・適合済み」が見えるダッシュボード。`scripts/validate_entry.py` のチェックを全件で走らせた結果を集計して再生成しています。手で編集しないでください。

## status 内訳

- **drafting**: 36 件
- **needs_review**: 68 件
- **ready**: 252 件
- **archived**: 8 件
- **合計**: 364 件

- **自己学習シェルフ（reader_level 6・刊行外）**: 35 件（誌面には出ません。`scripts/preview_gen.py` が除外）

## ☆ 違反あり（最優先で直す）（35 件）

| ID | title | status | 概要 |
| :-- | :-- | :-- | :-- |
| J-101 | 半導体製造プロセス | drafting | ☆ 704 字（目安 155-250、+454 字超過（100 字超で ☆））; ☆ 716 字（目安 220-430、+286 字超過（100 字超で ☆））; ⚠ 106 字（目安 25-60、+46 字超過） |
| J-102 | チップレットと3D積層 | drafting | ☆ 1178 字（目安 155-250、+928 字超過（100 字超で ☆））; ☆ 625 字（目安 220-430、+195 字超過（100 字超で ☆））; ⚠ 102 字（目安 25-60、+42 字超過） |
| J-103 | ループエンジニアリング | drafting | ☆ 562 字（目安 155-250、+312 字超過（100 字超で ☆））; ⚠ 260 字（目安 60-200、+60 字超過）; ⚠ 250 字（目安 60-200、+50 字超過） |
| J-104 | ReAct | drafting | ☆ 553 字（目安 155-250、+303 字超過（100 字超で ☆））; ⚠ 243 字（目安 60-200、+43 字超過）; ⚠ 259 字（目安 60-200、+59 字超過） |
| J-105 | コンテキスト管理 | drafting | ☆ 555 字（目安 155-250、+305 字超過（100 字超で ☆））; ⚠ 243 字（目安 60-200、+43 字超過）; ⚠ 265 字（目安 60-200、+65 字超過） |
| J-106 | ハーネスエンジニアリング | drafting | ☆ 442 字（目安 155-250、+192 字超過（100 字超で ☆））; ⚠ 65 字（目安 25-60、+5 字超過）; ⚠ 246 字（目安 120-240、+6 字超過） |
| J-107 | 自律ループとガードレール | drafting | ☆ 533 字（目安 155-250、+283 字超過（100 字超で ☆））; ⚠ 240 字（目安 60-200、+40 字超過）; ⚠ 233 字（目安 60-200、+33 字超過） |
| J-108 | Ralph Loop | drafting | ☆ 585 字（目安 155-250、+335 字超過（100 字超で ☆））; ⚠ 91 字（目安 25-60、+31 字超過）; ⚠ 300 字（目安 60-200、+100 字超過） |
| J-109 | モデルルーティング | drafting | ☆ 532 字（目安 155-250、+282 字超過（100 字超で ☆））; ⚠ 226 字（目安 60-200、+26 字超過）; ⚠ 254 字（目安 60-200、+54 字超過） |
| J-110 | 不確実性デファーラル | drafting | ☆ 483 字（目安 155-250、+233 字超過（100 字超で ☆））; ⚠ 221 字（目安 60-200、+21 字超過）; ⚠ 208 字（目安 60-200、+8 字超過） |
| J-111 | 人間の認知ボトルネック | drafting | ☆ 421 字（目安 155-250、+171 字超過（100 字超で ☆））; ☆ 539 字（目安 220-430、+109 字超過（100 字超で ☆））; ⚠ 64 字（目安 25-60、+4 字超過） |
| J-112 | 認知コストの定量化 | drafting | ☆ 397 字（目安 155-250、+147 字超過（100 字超で ☆））; ☆ 573 字（目安 220-430、+143 字超過（100 字超で ☆））; ⚠ 247 字（目安 120-240、+7 字超過） |
| J-113 | 生成UIとagent-native設計 | drafting | ☆ 555 字（目安 155-250、+305 字超過（100 字超で ☆））; ⚠ 70 字（目安 25-60、+10 字超過）; ⚠ 251 字（目安 60-200、+51 字超過） |
| J-114 | グッドハートの法則 | drafting | ☆ 603 字（目安 155-250、+353 字超過（100 字超で ☆））; ⚠ 63 字（目安 25-60、+3 字超過）; ⚠ 261 字（目安 60-200、+61 字超過） |
| J-24 | Encoder-Decoder | drafting | ☆ 1003 字（目安 155-250、+753 字超過（100 字超で ☆））; ☆ 805 字（目安 220-430、+375 字超過（100 字超で ☆））; ⚠ 122 字（目安 25-60、+62 字超過） |
| J-25 | Tokenizer・BPE | drafting | ☆ 2412 字（目安 155-250、+2162 字超過（100 字超で ☆））; ⚠ 107 字（目安 25-60、+47 字超過）; ⚠ 1662 字（目安 60-200、+1462 字超過） |
| J-26 | 潜在空間 | drafting | ☆ 1204 字（目安 155-250、+954 字超過（100 字超で ☆））; ⚠ 69 字（目安 25-60、+9 字超過）; ⚠ 626 字（目安 60-200、+426 字超過） |
| J-27 | RoPE | drafting | ☆ 1479 字（目安 155-250、+1229 字超過（100 字超で ☆））; ⚠ 83 字（目安 25-60、+23 字超過）; ⚠ 946 字（目安 60-200、+746 字超過） |
| J-28 | MLA | drafting | ☆ 933 字（目安 155-250、+683 字超過（100 字超で ☆））; ☆ 565 字（目安 220-430、+135 字超過（100 字超で ☆））; ⚠ 112 字（目安 25-60、+52 字超過） |
| J-29 | KV Cache | drafting | ☆ 821 字（目安 155-250、+571 字超過（100 字超で ☆））; ☆ 656 字（目安 220-430、+226 字超過（100 字超で ☆））; ⚠ 78 字（目安 25-60、+18 字超過） |
| J-30 | Flash Attention | drafting | ☆ 1125 字（目安 155-250、+875 字超過（100 字超で ☆））; ☆ 709 字（目安 220-430、+279 字超過（100 字超で ☆））; ⚠ 103 字（目安 25-60、+43 字超過） |
| J-82 | 投機的デコード | drafting | ☆ 1201 字（目安 155-250、+951 字超過（100 字超で ☆））; ☆ 564 字（目安 220-430、+134 字超過（100 字超で ☆））; ⚠ 93 字（目安 25-60、+33 字超過） |
| J-83 | vLLM | drafting | ☆ 1052 字（目安 155-250、+802 字超過（100 字超で ☆））; ☆ 716 字（目安 220-430、+286 字超過（100 字超で ☆））; ⚠ 81 字（目安 25-60、+21 字超過） |
| J-84 | バッチ推論 | drafting | ☆ 1017 字（目安 155-250、+767 字超過（100 字超で ☆））; ⚠ 557 字（目安 60-200、+357 字超過）; ⚠ 408 字（目安 60-200、+208 字超過） |
| J-85 | スループットとレイテンシ | drafting | ☆ 1382 字（目安 155-250、+1132 字超過（100 字超で ☆））; ☆ 559 字（目安 220-430、+129 字超過（100 字超で ☆））; ⚠ 100 字（目安 25-60、+40 字超過） |
| J-86 | GQA | drafting | ☆ 1036 字（目安 155-250、+786 字超過（100 字超で ☆））; ☆ 615 字（目安 220-430、+185 字超過（100 字超で ☆））; ⚠ 144 字（目安 25-60、+84 字超過） |
| J-87 | QK-Norm | drafting | ☆ 1184 字（目安 155-250、+934 字超過（100 字超で ☆））; ☆ 685 字（目安 220-430、+255 字超過（100 字超で ☆））; ⚠ 140 字（目安 25-60、+80 字超過） |
| J-88 | MTP | drafting | ☆ 1075 字（目安 155-250、+825 字超過（100 字超で ☆））; ☆ 635 字（目安 220-430、+205 字超過（100 字超で ☆））; ⚠ 109 字（目安 25-60、+49 字超過） |
| J-89 | MoE ルーティング | drafting | ☆ 1084 字（目安 155-250、+834 字超過（100 字超で ☆））; ☆ 709 字（目安 220-430、+279 字超過（100 字超で ☆））; ⚠ 118 字（目安 25-60、+58 字超過） |
| J-94 | 並列化戦略 | drafting | ☆ 2046 字（目安 155-250、+1796 字超過（100 字超で ☆））; ☆ 562 字（目安 220-430、+132 字超過（100 字超で ☆））; ⚠ 87 字（目安 25-60、+27 字超過） |
| J-95 | 半導体サプライチェーン | drafting | ☆ 596 字（目安 155-250、+346 字超過（100 字超で ☆））; ☆ 707 字（目安 220-430、+277 字超過（100 字超で ☆））; ⚠ 63 字（目安 25-60、+3 字超過） |
| J-96 | 半導体製造装置 | drafting | ☆ 674 字（目安 155-250、+424 字超過（100 字超で ☆））; ☆ 538 字（目安 220-430、+108 字超過（100 字超で ☆））; ⚠ 67 字（目安 25-60、+7 字超過） |
| J-97 | 電子材料 | drafting | ☆ 804 字（目安 155-250、+554 字超過（100 字超で ☆））; ☆ 574 字（目安 220-430、+144 字超過（100 字超で ☆））; ⚠ 417 字（目安 60-200、+217 字超過） |
| J-98 | 重要鉱物の地政学 | drafting | ☆ 845 字（目安 155-250、+595 字超過（100 字超で ☆））; ☆ 580 字（目安 220-430、+150 字超過（100 字超で ☆））; ⚠ 101 字（目安 25-60、+41 字超過） |
| J-99 | CoWoS | drafting | ☆ 836 字（目安 155-250、+586 字超過（100 字超で ☆））; ☆ 698 字（目安 220-430、+268 字超過（100 字超で ☆））; ⚠ 135 字（目安 25-60、+75 字超過） |

## ⚠️ 警告あり（軽微超過 / 著者か entry-writer で手当て）（139 件）

| ID | title | status | 概要 |
| :-- | :-- | :-- | :-- |
| B-12 | Perplexity | ready | ⚠ 強い断定語「最新」が入っている可能性（要確認） |
| B-13 | ElevenLabs | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| B-18 | Aqua Voice | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| B-19 | Claude Cowork | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| B-20 | Vercel | ready | ⚠ `reader_level` が `"2-3"` — `1`〜`6` の単一値か `2-3` 形式の |
| B-21 | Netlify | ready | ⚠ `reader_level` が `"2-3"` — `1`〜`6` の単一値か `2-3` 形式の |
| B-22 | Cloudflare | ready | ⚠ `reader_level` が `"2-4"` — `1`〜`6` の単一値か `2-3` 形式の |
| B-23 | AWS | ready | ⚠ `reader_level` が `"2-4"` — `1`〜`6` の単一値か `2-3` 形式の |
| B-24 | Google Cloud | ready | ⚠ `reader_level` が `"2-4"` — `1`〜`6` の単一値か `2-3` 形式の |
| B-25 | Azure | ready | ⚠ `reader_level` が `"2-4"` — `1`〜`6` の単一値か `2-3` 形式の |
| B-26 | Azure OpenAI | ready | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3` |
| B-27 | Vertex AI | ready | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3` |
| B-28 | Render | ready | ⚠ `reader_level` が `"2-3"` — `1`〜`6` の単一値か `2-3` 形式の |
| B-29 | Supabase | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| B-3 | ChatGPT | ready | ⚠ `reader_level` が `"1-2"` — `1`〜`6` の単一値か `2-3` 形式の |
| B-30 | Amazon Bedrock | ready | ⚠ `reader_level` が `"3-5"` — `1`〜`6` の単一値か `2-3` 形式の |
| B-31 | Excalidraw | ready | ⚠ `reader_level` の範囲幅が 2 段以上（1-3） — 幅は最大 1 段（例 `2-3` |
| B-32 | Figma | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| B-33 | Canva | ready | ⚠ `reader_level` の範囲幅が 2 段以上（1-3） — 幅は最大 1 段（例 `2-3` |
| B-4 | Cursor | ready | ⚠ `reader_level` が `"2-3"` — `1`〜`6` の単一値か `2-3` 形式の |
| B-40 | Reddit | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| B-41 | arXiv | ready | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3` |
| B-5 | GitHub Copilot | ready | ⚠ `reader_level` が `"2-3"` — `1`〜`6` の単一値か `2-3` 形式の |
| B-50 | Claude の料金プラン | ready | ⚠ `reader_level` が `"2-3"` — `1`〜`6` の単一値か `2-3` 形式の |
| B-51 | ChatGPT の料金プラン | ready | ⚠ `reader_level` が `"2-3"` — `1`〜`6` の単一値か `2-3` 形式の |
| B-52 | Gemini の料金プラン | ready | ⚠ `reader_level` が `"2-3"` — `1`〜`6` の単一値か `2-3` 形式の |
| B-6 | Windsurf | ready | ⚠ `reader_level` が `"2-3"` — `1`〜`6` の単一値か `2-3` 形式の |
| B-60 | Suno | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| C-1 | OpenAI | ready | ⚠ `reader_level` が `"1-2"` — `1`〜`6` の単一値か `2-3` 形式の |
| C-10 | Moonshot AI | needs_review | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| C-12 | TSMC | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3`; ⚠ 75 字（目安 25-60、+15 字超過）; ⚠ 16 字（目安 20-50、-4 字不足） |
| C-13 | Groq | ready | ⚠ 65 字（目安 25-60、+5 字超過） |
| C-14 | AMD | ready | ⚠ 52 字（目安 25-50、+2 字超過）; ⚠ 16 字（目安 20-50、-4 字不足） |
| C-3 | Google DeepMind | ready | ⚠ `reader_level` が `"2-3"` — `1`〜`6` の単一値か `2-3` 形式の |
| C-5 | xAI | ready | ⚠ 強い断定語「最新」が入っている可能性（要確認） |
| C-50 | Sam Altman | needs_review | ⚠ `reader_level` が `"2-3"` — `1`〜`6` の単一値か `2-3` 形式の |
| C-51 | Dario Amodei | ready | ⚠ `reader_level` が `"2-3"` — `1`〜`6` の単一値か `2-3` 形式の |
| C-52 | Demis Hassabis | ready | ⚠ `reader_level` が `"2-3"` — `1`〜`6` の単一値か `2-3` 形式の |
| C-53 | Andrej Karpathy | ready | ⚠ `reader_level` が `"2-3"` — `1`〜`6` の単一値か `2-3` 形式の; ⚠ 強い断定語「最新」が入っている可能性（要確認） |
| C-54 | Ilya Sutskever | ready | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3` |
| C-55 | Mira Murati | ready | ⚠ `reader_level` が `"2-3"` — `1`〜`6` の単一値か `2-3` 形式の |
| C-56 | Yann LeCun | ready | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3` |
| C-57 | Geoffrey Hinton | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3`; ⚠ 55 字（目安 25-50、+5 字超過）; ⚠ 185 字（目安 80-180、+5 字超過） |
| C-58 | Elon Musk | ready | ⚠ 18 字（目安 20-50、-2 字不足） |
| C-59 | Jensen Huang | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3`; ⚠ 194 字（目安 80-180、+14 字超過）; ⚠ 17 字（目安 20-50、-3 字不足） |
| C-6 | Mistral AI | needs_review | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| C-60 | Ray Kurzweil | ready | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3`; ⚠ 198 字（目安 80-180、+18 字超過）; ⚠ 強い断定語「最新」が入っている可能性（要確認） |
| C-7 | Hugging Face | ready | ⚠ `reader_level` が `"2-3"` — `1`〜`6` の単一値か `2-3` 形式の; ⚠ 191 字（目安 80-180、+11 字超過） |
| C-8 | Microsoft AI | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| C-81 | にゃんた | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| C-82 | まさお | ready | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3` |
| C-9 | NVIDIA | ready | ⚠ `reader_level` が `"2-3"` — `1`〜`6` の単一値か `2-3` 形式の |
| D-11 | Claude 3.5 系 | ready | ⚠ `reader_level` が `"2-3"` — `1`〜`6` の単一値か `2-3` 形式の |
| D-20 | GPT-5 系 | needs_review | ⚠ `reader_level` が `"2-3"` — `1`〜`6` の単一値か `2-3` 形式の |
| D-25 | GPT-1 / GPT-2 系 | ready | ⚠ 強い断定語「必ず」が入っている可能性（要確認） |
| D-35 | Cursor Composer | ready | ⚠ `reader_level` が `"2-3"` — `1`〜`6` の単一値か `2-3` 形式の |
| D-45 | GLM | ready | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3` |
| D-53 | Veo | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| D-55 | Nano Banana | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| D-56 | Seedance | ready | ⚠ 18 字（目安 20-50、-2 字不足）; ⚠ 258 字（目安 155-250、+8 字超過） |
| D-60 | AlphaGo | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| D-70 | Amical | needs_review | ⚠ 59 字（目安 60-200、-1 字不足） |
| E-20 | MMLU | ready | ⚠ 73 字（目安 25-60、+13 字超過） |
| E-22 | GPQA | ready | ⚠ 62 字（目安 25-60、+2 字超過）; ⚠ 52 字（目安 25-50、+2 字超過）; ⚠ 257 字（目安 155-250、+7 字超過） |
| E-23 | GSM8K | ready | ⚠ 61 字（目安 25-60、+1 字超過） |
| E-24 | MATH | ready | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3` |
| E-25 | AIME | ready | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3`; ⚠ 強い断定語「最新」が入っている可能性（要確認） |
| E-27 | IQ Bench | ready | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3` |
| E-32 | GAIA | needs_review | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3` |
| E-4 | HumanEval | ready | ⚠ 強い断定語「最新」が入っている可能性（要確認） |
| E-50 | Chatbot Arena | ready | ⚠ 強い断定語「最新」が入っている可能性（要確認） |
| E-51 | LMSYS Arena | needs_review | ⚠ 強い断定語「最新」が入っている可能性（要確認） |
| F-1 | JavaScript | ready | ⚠ `reader_level` が `"2"` — `1`〜`6` の単一値か `2-3` 形式の範囲 |
| F-110 | Lighthouse | needs_review | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| F-111 | a11y | needs_review | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| F-12 | Electron | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| F-120 | PostgreSQL | needs_review | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| F-123 | ORM | needs_review | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| F-130 | OAuth | needs_review | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| F-140 | Mermaid | needs_review | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| F-152 | GPL | needs_review | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3` |
| F-153 | Creative Commons | needs_review | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| F-16 | Tailwind CSS | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| F-161 | SSR | needs_review | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| F-171 | S3 | needs_review | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3`; ⚠ 58 字（目安 60-200、-2 字不足） |
| F-2 | TypeScript | ready | ⚠ `reader_level` が `"2-3"` — `1`〜`6` の単一値か `2-3` 形式の |
| F-20 | ESLint | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| F-200 | Rust | needs_review | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3` |
| F-3 | Python | ready | ⚠ `reader_level` が `"2-3"` — `1`〜`6` の単一値か `2-3` 形式の; ⚠ 53 字（目安 60-200、-7 字不足） |
| F-30 | VS Code | ready | ⚠ `reader_level` が `"2-3"` — `1`〜`6` の単一値か `2-3` 形式の |
| F-38 | Markdown All in One | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| F-4 | HTML | ready | ⚠ `reader_level` が `"2"` — `1`〜`6` の単一値か `2-3` 形式の範囲 |
| F-5 | CSS | ready | ⚠ `reader_level` が `"2"` — `1`〜`6` の単一値か `2-3` 形式の範囲 |
| F-6 | Markdown | ready | ⚠ `reader_level` が `"2"` — `1`〜`6` の単一値か `2-3` 形式の範囲 |
| F-61 | Pull Request | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| F-62 | GitHub Actions | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| F-7 | YAML | ready | ⚠ `reader_level` が `"2"` — `1`〜`6` の単一値か `2-3` 形式の範囲 |
| F-8 | JSON | ready | ⚠ `reader_level` が `"2"` — `1`〜`6` の単一値か `2-3` 形式の範囲 |
| F-83 | PowerShell | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| F-85 | SuperClaude Framework | needs_review | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3` |
| F-86 | ollama | needs_review | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3` |
| G-12 | Agent Design | needs_review | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3` |
| G-13 | Few-shot Learning | ready | ⚠ 48 字（目安 60-200、-12 字不足） |
| G-34 | Code Interpreter | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| G-38 | Plan Mode | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| G-43 | オーケストレーション | ready | ⚠ 強い断定語「最強」が入っている可能性（要確認） |
| G-46 | ナーフ | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| H-5 | Scrum / Agile | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| H-56 | Claude のバージョン史 | ready | ⚠ 54 字（目安 60-200、-6 字不足） |
| H-8 | DevOps | ready | ⚠ 55 字（目安 60-200、-5 字不足） |
| I-10 | Filesystem MCP | ready | ⚠ 57 字（目安 25-50、+7 字超過）; ⚠ 198 字（目安 80-180、+18 字超過）; ⚠ 436 字（目安 220-430、+6 字超過） |
| I-12 | Git MCP | ready | ⚠ 189 字（目安 80-180、+9 字超過） |
| I-13 | Slack MCP | ready | ⚠ 220 字（目安 80-180、+40 字超過）; ⚠ 434 字（目安 220-430、+4 字超過） |
| I-2 | MCP Server | ready | ⚠ 51 字（目安 25-50、+1 字超過）; ⚠ 218 字（目安 80-180、+38 字超過）; ⚠ 456 字（目安 220-430、+26 字超過） |
| I-20 | Playwright MCP | ready | ⚠ 59 字（目安 25-50、+9 字超過） |
| I-21 | Puppeteer MCP | ready | ⚠ 52 字（目安 25-50、+2 字超過）; ⚠ 185 字（目安 80-180、+5 字超過）; ⚠ 435 字（目安 220-430、+5 字超過） |
| I-22 | Chrome DevTools MCP | ready | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3`; ⚠ 199 字（目安 80-180、+19 字超過）; ⚠ 452 字（目安 220-430、+22 字超過） |
| I-23 | Serena MCP | ready | ⚠ 202 字（目安 80-180、+22 字超過） |
| I-24 | Context7 MCP | ready | ⚠ 57 字（目安 25-50、+7 字超過）; ⚠ 204 字（目安 80-180、+24 字超過） |
| I-3 | MCP Client | ready | ⚠ 55 字（目安 25-50、+5 字超過）; ⚠ 185 字（目安 80-180、+5 字超過） |
| I-30 | Notion MCP | ready | ⚠ 226 字（目安 80-180、+46 字超過）; ⚠ 438 字（目安 220-430、+8 字超過） |
| I-4 | MCP Transport | ready | ⚠ 188 字（目安 80-180、+8 字超過）; ⚠ 432 字（目安 220-430、+2 字超過）; ⚠ です・ます外れの疑いあり（(?<![すまりぞ])だ[。\s] のパターン、要目視確認） |
| I-41 | SQLite MCP | ready | ⚠ 220 字（目安 80-180、+40 字超過） |
| I-5 | MCP SDK | ready | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3`; ⚠ 223 字（目安 80-180、+43 字超過）; ⚠ 444 字（目安 220-430、+14 字超過） |
| I-50 | AWS MCP | ready | ⚠ 238 字（目安 80-180、+58 字超過）; ⚠ 474 字（目安 220-430、+44 字超過） |
| J-1 | AGI | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| J-17 | Attention | ready | ⚠ 強い断定語「必ず」が入っている可能性（要確認） |
| J-2 | 強い AI／弱い AI | ready | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3` |
| J-21 | LoRA | ready | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3` |
| J-3 | Singularity | ready | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3` |
| J-4 | ASI | ready | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3` |
| J-42 | Web3 | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |
| J-53 | 著作権法 30 条の 4 | ready | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3` |
| J-54 | ISO/IEC 42001 | ready | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3` |
| J-70 | VRAM | ready | ⚠ 59 字（目安 60-200、-1 字不足） |
| J-72 | H100 | ready | ⚠ `reader_level` の範囲幅が 2 段以上（3-5） — 幅は最大 1 段（例 `2-3` |
| J-73 | Blackwell | ready | ⚠ 強い断定語「最新」が入っている可能性（要確認） |
| J-78 | HDD | ready | ⚠ `reader_level` の範囲幅が 2 段以上（1-3） — 幅は最大 1 段（例 `2-3` |
| J-93 | Ubuntu | ready | ⚠ `reader_level` の範囲幅が 2 段以上（2-4） — 幅は最大 1 段（例 `2-3` |

## ✍️ 書きかけ（drafting・全パス済み・自動昇格漏れ）（0 件）

_なし（drafting で全パスしたものは自動で needs_review に上がります）_

## 📝 著者レビュー待ち（needs_review・全パス）（36 件）

| ID | title | status | 概要 |
| :-- | :-- | :-- | :-- |
| C-11 | Z.ai | needs_review | — |
| C-15 | Intel | needs_review | — |
| D-1 | Gemini 2 系 | needs_review | — |
| D-14 | Claude Mythos Preview | needs_review | — |
| D-2 | Gemini 2.5 系 | needs_review | — |
| D-21 | GPT-4 系 | needs_review | — |
| D-22 | o1 系 | needs_review | — |
| D-24 | GPT-3 系 | needs_review | — |
| D-4 | Gemini 3.1 系 | needs_review | — |
| E-31 | WebArena | needs_review | — |
| E-33 | AgentBench | needs_review | — |
| E-34 | OSWorld | needs_review | — |
| F-100 | 拡張子早見表 | needs_review | — |
| F-101 | .ico | needs_review | — |
| F-102 | .mp4 | needs_review | — |
| F-103 | .mp3 | needs_review | — |
| F-104 | .webp | needs_review | — |
| F-121 | SQLite | needs_review | — |
| F-122 | Prisma | needs_review | — |
| F-141 | PlantUML | needs_review | — |
| F-151 | Apache 2.0 | needs_review | — |
| F-154 | OSS | needs_review | — |
| F-160 | DOM | needs_review | — |
| F-162 | SSG | needs_review | — |
| F-170 | EC2 | needs_review | — |
| F-172 | IAM | needs_review | — |
| F-180 | OpenGL | needs_review | — |
| F-181 | WebGL | needs_review | — |
| F-190 | サブルーチン | needs_review | — |
| F-80 | Node.js | needs_review | — |
| F-84 | Ghostty | needs_review | — |
| F-87 | sudo | needs_review | — |
| F-90 | Docker | needs_review | — |
| F-91 | .env | needs_review | — |
| G-4 | System Prompt | needs_review | — |
| J-43 | SaaS | needs_review | — |

## ✅ 完成（ready・全パス）（134 件）

| ID | title | status | 概要 |
| :-- | :-- | :-- | :-- |
| B-1 | Gemini | ready | — |
| B-10 | Devin | ready | — |
| B-11 | Bolt.new | ready | — |
| B-14 | Genspark | ready | — |
| B-15 | Microsoft Copilot | ready | — |
| B-16 | Microsoft 365 Copilot | ready | — |
| B-17 | Edge Copilot | ready | — |
| B-2 | Claude | ready | — |
| B-61 | ACE-Step 1.5 | ready | — |
| B-7 | Claude Code | ready | — |
| B-8 | Codex | ready | — |
| B-9 | v0 | ready | — |
| C-2 | Anthropic | ready | — |
| C-4 | Meta AI | ready | — |
| C-80 | AI大学 | ready | — |
| D-12 | Claude 4 系 | ready | — |
| D-26 | gpt-oss | ready | — |
| D-30 | Grok 系 | ready | — |
| D-40 | Llama 系 | ready | — |
| D-41 | Mistral 系 | ready | — |
| D-42 | Gemma 系 | ready | — |
| D-43 | Qwen 系 | ready | — |
| D-44 | Kimi | ready | — |
| D-46 | DeepSeek V3 | ready | — |
| D-47 | DeepSeek R1 | ready | — |
| D-50 | DALL-E | ready | — |
| D-51 | Imagen | ready | — |
| D-52 | Sora | ready | — |
| D-54 | Stable Diffusion | ready | — |
| D-57 | Flow | ready | — |
| D-58 | Whisk | ready | — |
| D-71 | Whisper | ready | — |
| E-1 | SWE-Bench | ready | — |
| E-2 | SWE-Bench Verified | ready | — |
| E-21 | MMLU-Pro | ready | — |
| E-26 | Humanity's Last Exam | ready | — |
| E-3 | Terminal-Bench | ready | — |
| E-30 | TAU-Bench | ready | — |
| F-10 | React | ready | — |
| F-11 | Next.js | ready | — |
| F-13 | Tauri | ready | — |
| F-14 | three.js | ready | — |
| F-15 | shadcn/ui | ready | — |
| F-17 | Astro | ready | — |
| F-21 | Prettier | ready | — |
| F-35 | Markdown Preview Enhanced | ready | — |
| F-36 | Git Graph | ready | — |
| F-37 | Japanese Language Pack for VS Code | ready | — |
| F-40 | npm | ready | — |
| F-41 | Vite | ready | — |
| F-42 | ビルド | ready | — |
| F-44 | pnpm | ready | — |
| F-50 | git | ready | — |
| F-51 | git push | ready | — |
| F-52 | git pull | ready | — |
| F-53 | branch | ready | — |
| F-54 | commit | ready | — |
| F-55 | merge | ready | — |
| F-56 | .gitignore | ready | — |
| F-58 | git stash | ready | — |
| F-59 | README.md | ready | — |
| F-60 | GitHub | ready | — |
| F-71 | ripgrep | ready | — |
| F-81 | bash | ready | — |
| F-82 | WSL | ready | — |
| F-9 | SVG | ready | — |
| G-1 | Context | ready | — |
| G-10 | Prompt Engineering | ready | — |
| G-11 | Context Engineering | ready | — |
| G-14 | Thinking モデル | ready | — |
| G-15 | RAG | ready | — |
| G-16 | Embedding | ready | — |
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
| G-35 | Deep Research | ready | — |
| G-36 | Artifact | ready | — |
| G-39 | Permission | ready | — |
| G-40 | バイブコーディング | ready | — |
| G-41 | Subagent | ready | — |
| G-42 | Worktree | ready | — |
| G-44 | マルチエージェント協調 | ready | — |
| G-47 | Auto-compact | ready | — |
| G-5 | Context Window | ready | — |
| G-6 | One-shot | ready | — |
| G-7 | 指示追従性 | ready | — |
| H-1 | TDD | ready | — |
| H-53 | ChatGPT 登場 | ready | — |
| H-54 | GPT-4 リリース | ready | — |
| H-55 | LLaMA のオープン化 | ready | — |
| H-58 | Transformer 論文 | ready | — |
| H-6 | Git Flow | ready | — |
| H-7 | CI/CD | ready | — |
| I-1 | MCP | ready | — |
| I-11 | GitHub MCP | ready | — |
| J-10 | Machine Learning | ready | — |
| J-100 | リテラシー | ready | — |
| J-11 | Deep Learning | ready | — |
| J-12 | Neural Network | ready | — |
| J-13 | Transformer | ready | — |
| J-14 | LLM | ready | — |
| J-15 | VLM | ready | — |
| J-16 | Fine-tuning | ready | — |
| J-18 | MoE | ready | — |
| J-19 | 量子化 | ready | — |
| J-20 | Big Data | ready | — |
| J-23 | 拡散モデル | ready | — |
| J-31 | 第 5 世代コンピュータ | ready | — |
| J-33 | 量子コンピュータ | ready | — |
| J-40 | IoT | ready | — |
| J-41 | DX | ready | — |
| J-51 | Hallucination | ready | — |
| J-52 | Sycophancy | ready | — |
| J-56 | GDPR | ready | — |
| J-71 | RAM | ready | — |
| J-74 | RTX シリーズ | ready | — |
| J-75 | Tensor コア | ready | — |
| J-76 | CPU | ready | — |
| J-77 | GPU | ready | — |
| J-79 | SSD | ready | — |
| J-80 | SATA | ready | — |
| J-81 | M.2 | ready | — |
| J-90 | GUI | ready | — |
| J-91 | CLI | ready | — |
| J-92 | Linux | ready | — |

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
| J-101 | 半導体製造プロセス | drafting | ☆ 704 字（目安 155-250、+454 字超過（100 字超で ☆））; ☆ 716 字（目安 220-430、+286 字超過（100 字超で ☆））; ⚠ 106 字（目安 25-60、+46 字超過） |
| J-102 | チップレットと3D積層 | drafting | ☆ 1178 字（目安 155-250、+928 字超過（100 字超で ☆））; ☆ 625 字（目安 220-430、+195 字超過（100 字超で ☆））; ⚠ 102 字（目安 25-60、+42 字超過） |
| J-103 | ループエンジニアリング | drafting | ☆ 562 字（目安 155-250、+312 字超過（100 字超で ☆））; ⚠ 260 字（目安 60-200、+60 字超過）; ⚠ 250 字（目安 60-200、+50 字超過） |
| J-104 | ReAct | drafting | ☆ 553 字（目安 155-250、+303 字超過（100 字超で ☆））; ⚠ 243 字（目安 60-200、+43 字超過）; ⚠ 259 字（目安 60-200、+59 字超過） |
| J-105 | コンテキスト管理 | drafting | ☆ 555 字（目安 155-250、+305 字超過（100 字超で ☆））; ⚠ 243 字（目安 60-200、+43 字超過）; ⚠ 265 字（目安 60-200、+65 字超過） |
| J-106 | ハーネスエンジニアリング | drafting | ☆ 442 字（目安 155-250、+192 字超過（100 字超で ☆））; ⚠ 65 字（目安 25-60、+5 字超過）; ⚠ 246 字（目安 120-240、+6 字超過） |
| J-107 | 自律ループとガードレール | drafting | ☆ 533 字（目安 155-250、+283 字超過（100 字超で ☆））; ⚠ 240 字（目安 60-200、+40 字超過）; ⚠ 233 字（目安 60-200、+33 字超過） |
| J-108 | Ralph Loop | drafting | ☆ 585 字（目安 155-250、+335 字超過（100 字超で ☆））; ⚠ 91 字（目安 25-60、+31 字超過）; ⚠ 300 字（目安 60-200、+100 字超過） |
| J-109 | モデルルーティング | drafting | ☆ 532 字（目安 155-250、+282 字超過（100 字超で ☆））; ⚠ 226 字（目安 60-200、+26 字超過）; ⚠ 254 字（目安 60-200、+54 字超過） |
| J-110 | 不確実性デファーラル | drafting | ☆ 483 字（目安 155-250、+233 字超過（100 字超で ☆））; ⚠ 221 字（目安 60-200、+21 字超過）; ⚠ 208 字（目安 60-200、+8 字超過） |
| J-111 | 人間の認知ボトルネック | drafting | ☆ 421 字（目安 155-250、+171 字超過（100 字超で ☆））; ☆ 539 字（目安 220-430、+109 字超過（100 字超で ☆））; ⚠ 64 字（目安 25-60、+4 字超過） |
| J-112 | 認知コストの定量化 | drafting | ☆ 397 字（目安 155-250、+147 字超過（100 字超で ☆））; ☆ 573 字（目安 220-430、+143 字超過（100 字超で ☆））; ⚠ 247 字（目安 120-240、+7 字超過） |
| J-113 | 生成UIとagent-native設計 | drafting | ☆ 555 字（目安 155-250、+305 字超過（100 字超で ☆））; ⚠ 70 字（目安 25-60、+10 字超過）; ⚠ 251 字（目安 60-200、+51 字超過） |
| J-114 | グッドハートの法則 | drafting | ☆ 603 字（目安 155-250、+353 字超過（100 字超で ☆））; ⚠ 63 字（目安 25-60、+3 字超過）; ⚠ 261 字（目安 60-200、+61 字超過） |
| J-24 | Encoder-Decoder | drafting | ☆ 1003 字（目安 155-250、+753 字超過（100 字超で ☆））; ☆ 805 字（目安 220-430、+375 字超過（100 字超で ☆））; ⚠ 122 字（目安 25-60、+62 字超過） |
| J-25 | Tokenizer・BPE | drafting | ☆ 2412 字（目安 155-250、+2162 字超過（100 字超で ☆））; ⚠ 107 字（目安 25-60、+47 字超過）; ⚠ 1662 字（目安 60-200、+1462 字超過） |
| J-26 | 潜在空間 | drafting | ☆ 1204 字（目安 155-250、+954 字超過（100 字超で ☆））; ⚠ 69 字（目安 25-60、+9 字超過）; ⚠ 626 字（目安 60-200、+426 字超過） |
| J-27 | RoPE | drafting | ☆ 1479 字（目安 155-250、+1229 字超過（100 字超で ☆））; ⚠ 83 字（目安 25-60、+23 字超過）; ⚠ 946 字（目安 60-200、+746 字超過） |
| J-28 | MLA | drafting | ☆ 933 字（目安 155-250、+683 字超過（100 字超で ☆））; ☆ 565 字（目安 220-430、+135 字超過（100 字超で ☆））; ⚠ 112 字（目安 25-60、+52 字超過） |
| J-29 | KV Cache | drafting | ☆ 821 字（目安 155-250、+571 字超過（100 字超で ☆））; ☆ 656 字（目安 220-430、+226 字超過（100 字超で ☆））; ⚠ 78 字（目安 25-60、+18 字超過） |
| J-30 | Flash Attention | drafting | ☆ 1125 字（目安 155-250、+875 字超過（100 字超で ☆））; ☆ 709 字（目安 220-430、+279 字超過（100 字超で ☆））; ⚠ 103 字（目安 25-60、+43 字超過） |
| J-82 | 投機的デコード | drafting | ☆ 1201 字（目安 155-250、+951 字超過（100 字超で ☆））; ☆ 564 字（目安 220-430、+134 字超過（100 字超で ☆））; ⚠ 93 字（目安 25-60、+33 字超過） |
| J-83 | vLLM | drafting | ☆ 1052 字（目安 155-250、+802 字超過（100 字超で ☆））; ☆ 716 字（目安 220-430、+286 字超過（100 字超で ☆））; ⚠ 81 字（目安 25-60、+21 字超過） |
| J-84 | バッチ推論 | drafting | ☆ 1017 字（目安 155-250、+767 字超過（100 字超で ☆））; ⚠ 557 字（目安 60-200、+357 字超過）; ⚠ 408 字（目安 60-200、+208 字超過） |
| J-85 | スループットとレイテンシ | drafting | ☆ 1382 字（目安 155-250、+1132 字超過（100 字超で ☆））; ☆ 559 字（目安 220-430、+129 字超過（100 字超で ☆））; ⚠ 100 字（目安 25-60、+40 字超過） |
| J-86 | GQA | drafting | ☆ 1036 字（目安 155-250、+786 字超過（100 字超で ☆））; ☆ 615 字（目安 220-430、+185 字超過（100 字超で ☆））; ⚠ 144 字（目安 25-60、+84 字超過） |
| J-87 | QK-Norm | drafting | ☆ 1184 字（目安 155-250、+934 字超過（100 字超で ☆））; ☆ 685 字（目安 220-430、+255 字超過（100 字超で ☆））; ⚠ 140 字（目安 25-60、+80 字超過） |
| J-88 | MTP | drafting | ☆ 1075 字（目安 155-250、+825 字超過（100 字超で ☆））; ☆ 635 字（目安 220-430、+205 字超過（100 字超で ☆））; ⚠ 109 字（目安 25-60、+49 字超過） |
| J-89 | MoE ルーティング | drafting | ☆ 1084 字（目安 155-250、+834 字超過（100 字超で ☆））; ☆ 709 字（目安 220-430、+279 字超過（100 字超で ☆））; ⚠ 118 字（目安 25-60、+58 字超過） |
| J-94 | 並列化戦略 | drafting | ☆ 2046 字（目安 155-250、+1796 字超過（100 字超で ☆））; ☆ 562 字（目安 220-430、+132 字超過（100 字超で ☆））; ⚠ 87 字（目安 25-60、+27 字超過） |
| J-95 | 半導体サプライチェーン | drafting | ☆ 596 字（目安 155-250、+346 字超過（100 字超で ☆））; ☆ 707 字（目安 220-430、+277 字超過（100 字超で ☆））; ⚠ 63 字（目安 25-60、+3 字超過） |
| J-96 | 半導体製造装置 | drafting | ☆ 674 字（目安 155-250、+424 字超過（100 字超で ☆））; ☆ 538 字（目安 220-430、+108 字超過（100 字超で ☆））; ⚠ 67 字（目安 25-60、+7 字超過） |
| J-97 | 電子材料 | drafting | ☆ 804 字（目安 155-250、+554 字超過（100 字超で ☆））; ☆ 574 字（目安 220-430、+144 字超過（100 字超で ☆））; ⚠ 417 字（目安 60-200、+217 字超過） |
| J-98 | 重要鉱物の地政学 | drafting | ☆ 845 字（目安 155-250、+595 字超過（100 字超で ☆））; ☆ 580 字（目安 220-430、+150 字超過（100 字超で ☆））; ⚠ 101 字（目安 25-60、+41 字超過） |
| J-99 | CoWoS | drafting | ☆ 836 字（目安 155-250、+586 字超過（100 字超で ☆））; ☆ 698 字（目安 220-430、+268 字超過（100 字超で ☆））; ⚠ 135 字（目安 25-60、+75 字超過） |

## 動線

- **☆ 違反**（タグ `[AI直]`）: その場で entry-writer を呼んで直す（status は drafting のまま）
- **⚠️ 警告**（タグ `[AI整]`）: 軽微なら手で削る／溜まったらまとめて対応
- **needs_review**（タグ `[人書]`）: 著者本人が「非エンジニアのつまずき」「私のコメント」4 項目を埋める。全項目埋まると保存時に `ready`（`[済]`）へ自動昇格
- このキューは `Edit/Write` のたびに自動更新されます。手動更新は `python3 scripts/update_review_queue.py`
- ファイル名のタグを更新するには `python3 scripts/apply_status_markers.py`
