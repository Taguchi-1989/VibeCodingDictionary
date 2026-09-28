# Ponchi Logo Requirement Matrix 2026-06-01

最終確認日: 2026-09-28（Batch008–011を再照合。B-31/B-33/D-22/D-44/F-15/F-20/F-62/F-80/F-181の現行finalには公式マークが見える。旧overlay監査は未レビュー、個別利用条件も未確認。これは採用・公開承認を示さない。F-212はSpecificationとInitiativeを区別し、組織ロゴを使わない）

## 目的

ポンチ絵再生成で、ロゴを入れるべき項目と入れない項目を先に分ける。ロゴが必要でも、公式素材と利用条件が確認できていないものは後合成しない。AI 生成でロゴ風の図形やブランドカラーを作らせることも禁止する。

対象は、この台帳の `マーキング` 表に明示したエントリです。横展開バッチを選ぶ前に当該IDを追加し、会社・製品・モデル名の有無とロゴ要件の根拠を記録します。

## ステータス定義

| status | 意味 |
| :-- | :-- |
| `logo_avoid` | ロゴ不要。汎用アイコンだけで説明する |
| `base_2to1_ready_logo_blocked` | 元絵の 2:1 ベースは再生成済み。ロゴは公式素材・利用条件・ローカルパスが未確定のため未反映 |
| `official_logo_source_available_needs_import` | 公式ソースは確認済み。まだローカル素材化・利用条件記録・合成監査が未完了 |
| `official_logo_source_review_required` | 公式ロゴの公式source/brand guide自体、対象項目での具体mark選定、取得経路、または用途条件のいずれかが未確認。公式性や利用可否を推定せず、未確認が解消するまで合成を止める |
| `official_logo_available` | 公式素材がローカルにあり、出典が記録済み。個別用途の利用条件は別途確認する |
| `official_logo_applied` | 公式素材を後合成した画像が存在する。対象画像が現行finalか実験候補かは注記で区別し、個別用途の利用許諾・採用とはみなさない |
| `official_logo_applied_unreviewed` | 公式マークが現行finalに存在することを画像/生成記録で確認したが、対応するoverlay監査は未レビュー。用途条件・採用・公開を承認した状態ではない |
| `official_logo_overlay_candidate_unreviewed` | 公式素材を合成した実験overlay候補があるが、独立overlay監査は未完了。現行final・採用状態とは別に管理する |

## 判定方針

ブランド名・製品名・モデル系列名そのものが見出しになっている項目は、本文だけで足りるとしてロゴを避けない。公式ロゴ、公式 lockup、公式アイコンのソースが確認できる場合は、2:1 ベース再生成後に公式素材を取得し、未改変で後合成する。

ただし、AI 生成でロゴ風の図形を描かせることは引き続き禁止する。公式ソースが未確認、利用条件が不明、または具体的なロゴ選定が未確定なら、合成は止めて `official_logo_source_review_required` または `base_2to1_ready_logo_blocked` に置く。

この表の `status` は素材の取得・画像への適用状況を示し、利用許諾を示さない。新しい候補で対象用途の条件が確認できない場合は、公式素材を合成せず `internal_base_only` の内部ベースに限定する。出典の確認や既存画像への適用実績から、公開・商用利用の権利を推定しない。

## マーキング

| entry_id | title | logo_need | status | local official asset | action |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `A-2` | この本の読み方 | not_needed | `logo_avoid` | none | 本文の読み方と図の対応を示す説明用概念図。出版社・製品ロゴは使わない |
| `A-4` | 体験区分の凡例 | not_needed | `logo_avoid` | none | 塗りつぶし/半塗り/空円の一般凡例。会社・製品名や公式マークを使わない。
| `A-8` | 色・記号の凡例 | not_needed | `logo_avoid` | none | 一般的な配色・記号の凡例。会社・製品・モデル名ではなく、ブランド識別素材は不要 |
| `B-1` | Gemini | required | `official_logo_source_review_required` | none | 2:1 ベース生成済み。Google Brand Resource Center の利用条件を前提に、Gemini に使う公式プロダクトアイコン/lockup と許諾要否を確認してから合成 |
| `B-2` | Claude | required | `official_logo_applied` | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/1 Claude logo/PNG/Claude logo - Slate.png` | B-focus ベースに公式 Claude ロゴを後合成済み。`overlay_candidates_contact_sheet.png` で目視確認 |
| `B-3` | ChatGPT | required | `official_logo_source_review_required` | none | 2:1 ベース生成済み。OpenAI 公式ブランドガイドを前提に、OpenAI wordmark と ChatGPT 固有表現のどちらを使うか決めてから合成 |
| `B-4` | Cursor | required | `official_logo_applied` | `assets/logos/cursor/cursor-brand-assets/General Logos/Lockup Horizontal/PNG/LOCKUP_HORIZONTAL_2D_LIGHT.png` | B-focus ベースに公式 Cursor horizontal lockup を後合成済み。`overlay_candidates_contact_sheet.png` で目視確認 |
| `B-5` | GitHub Copilot | required | `official_logo_applied` | `assets/logos/github/GitHub_Logos/GitHub Logos/PNG/GitHub_Copilot_Lockup_Black_Clearspace.png` | 本番 `assets/ponchi/final/B-5.webp` に公式 lockup 合成済み |
| `B-7` | Claude Code | required | `official_logo_applied` | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/2 Claude Code logo/PNG/Claude Code logo - Slate.png` | B-focus ベースに公式 Claude Code ロゴを後合成済み。`overlay_candidates_contact_sheet.png` で目視確認 |
| `B-8` | Codex | required | `official_logo_source_review_required` | none | 2:1 ベース生成済み。OpenAI 公式ブランドガイドを前提に、Codex 固有 lockup があるか、OpenAI wordmark で扱うかを確認してから合成 |
| `B-9` | v0 | required | `official_logo_applied` | `assets/logos/vercel/v0-assets/v0/Light/v0-logo-light.png` | B-focus ベースに公式 v0 ロゴを後合成済み。180px配置で final 候補へ昇格 |
| `B-10` | Devin | required | `official_logo_available` | `assets/logos/devin/devin-official-header-mark.svg` | 公式Devin homepage header markを取得済み（`brand_usage_audit.md`、2026-06-03）。個別利用条件は未確認。生成ロゴは禁止し、使用条件確認まではロゴなし`internal_base_only`に限定。
| `B-11` | Bolt.new | required | `official_logo_applied` | `assets/logos/bolt/bolt-logo-text-official-512.png` | batch-002 ベースに公式 StackBlitz `bolt.new` repo の Bolt wordmark を後合成済み。`.new` suffix は合成・生成しない |
| `B-12` | Perplexity | required | `official_logo_applied` | `assets/logos/perplexity/Perplexity-Primary-Lockup-Offblack.svg` | batch-002 ベースに公式 Perplexity Brand Guidelines の offblack primary lockup を後合成済み |
| `B-13` | ElevenLabs | required | `official_logo_applied` | `assets/logos/elevenlabs/elevenlabs-logo-black.svg` | batch-002 ベースに公式 ElevenLabs black SVG を後合成済み。final 候補で目視確認 |
| `B-14` | Genspark | required | `official_logo_available` | `assets/logos/genspark/genspark-favicon.ico` | 公式 favicon は取得済み（brand audit、2026-06-03）がfull lockupは未取得・overlay review-pending。利用条件確定まで新候補はlogo-free `internal_base_only`。AI生成でmarkを再現しない |
| `B-15` | Microsoft Copilot | required | `official_logo_available` | `assets/logos/microsoft-copilot/copilot-official-inline-icon.svg` | 公式Copilot homepageのicon SVGを取得済み（`brand_usage_audit.md`）。product-specific final useはreview-pending。retrieval date/use条件を確認するまで合成・採用せず、候補はロゴなし内部ベースに限定。
| `B-16` | Microsoft 365 Copilot | required | `official_logo_applied_unreviewed` | `assets/logos/microsoft-copilot/copilot-official-inline-icon.svg` | 現行finalにCopilot-family markが見える。legacy batch-002は `official_logo_applied / overlay_audit`。local asset SHA-256 `DF416DD72A55B503D5D85D9F5E096C2000E3AE03AA4314BF30B9AC21964995A8`。専用Microsoft 365 Copilot lockup・用途条件・item-local clearspaceは未確認。baseの共有screening ROI `[686,0,520,180]` に5,389非白画素があり、この標準ROIは個別ブランド規定ではない。別baseを再構成し独立監査するまでsidecar/generationを止める |
| `B-17` | Edge Copilot | required | `official_logo_source_review_required` | none | batch-002 対象。Edge/Copilot のどちらの公式表現にするか決めるまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-18` | Aqua Voice | required | `official_logo_source_review_required` | none | batch-002 対象。公式ロゴ素材・利用条件・ローカルパスを確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-19` | Claude Cowork | required | `official_logo_source_review_required` | none | batch-002 対象。正式名称と Claude ロゴ適用可否を Anthropic 公式ソースで確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-20` | Vercel | required | `official_logo_applied` | `assets/logos/vercel/vercel-assets/Vercel/logotype/light/vercel-logotype-light.png` | batch-002 ベースに公式 Vercel ロゴを後合成済み。final 候補で目視確認 |
| `B-21` | Netlify | required | `official_logo_applied` | `assets/logos/netlify/netlify-logo-full/netlify-logo-full/large/lightmode/logo-netlify-large-monochrome-lightmode.png` | batch-002 ベースに公式 Netlify ロゴを後合成済み。`ponchi-batch-002-base-contact-sheet.png` と final 候補で目視確認 |
| `B-22` | Cloudflare | required | `official_logo_applied` | `assets/logos/cloudflare/Cloudflare_logo_kit/Cloudflare_logo_kit/Cloudflare_logo_kit/Cloudflare logo/png/CF_logo_horizontal_singlecolor_blk.png` | batch-002 ベースに公式 Cloudflare ロゴを後合成済み。`ponchi-batch-002-base-contact-sheet.png` と final 候補で目視確認 |
| `B-23` | AWS | required | `official_logo_source_review_required` | none | batch-002 対象。ローカルの AWS Architecture Icons はブランド lockup と別扱い。公式ロゴ/利用条件を確認してから合成 |
| `B-24` | Google Cloud | required | `official_logo_source_review_required` | none | batch-002 対象。Google Cloud の公式ロゴ素材・利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-25` | Azure | required | `official_logo_source_review_required` | none | batch-002 対象。Microsoft Azure の公式ロゴ素材・利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-26` | Azure OpenAI | required | `official_logo_source_review_required` | none | batch-002 対象。Azure と OpenAI のどちらの公式表現にするか決めるまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-27` | Vertex AI | required | `official_logo_applied` | `assets/logos/google-cloud/product-icons/core-products-icons/Unique Icons/Vertex AI/SVG/VertexAI-512-color.svg` | 現行 final は公式 Vertex AI 製品アイコンの後合成版。旧overlayは利用条件レビュー待ち。新候補は条件確認まで `internal_base_only` とし、公式素材を合成しない |
| `B-28` | Render | required | `official_logo_applied` | `assets/logos/render/render-wordmark-from-press.png` | batch-002 ベースに公式 Render wordmark を後合成済み。final 候補で目視確認 |
| `B-29` | Supabase | required | `official_logo_applied` | `assets/logos/supabase/brand-assets/supabase-logo-wordmark--light.png` | batch-002 ベースに公式 Supabase ロゴを後合成済み。final 候補で目視確認 |
| `B-30` | Amazon Bedrock | required | `official_logo_applied` | `assets/logos/aws/aws-architecture-icons-2026-01-30/Architecture-Service-Icons_01302026/Arch_Artificial-Intelligence/64/Arch_Amazon-Bedrock_64.svg` | 現行 final は Bedrock 専用の AWS Architecture サービスアイコンを後合成済み。これはAWS一般ロゴとは区別する。新候補は用途条件の確認まで `internal_base_only` |
| `B-31` | Excalidraw | required | `official_logo_applied_unreviewed` | `assets/logos/excalidraw/excalidraw-favicon.svg` | Local official asset: official Excalidraw GitHub repository, retrieved 2026-06-03; SHA-256 `FF042440A415C5E3F0B3C77DFBF2A367906E38CBABDD5B2270E6E01FF4F8A97F`. Current final contains the mark; legacy generation record is `official_logo_applied` / `overlay_audit` / `not_reviewed`. A separate logo-free base exists at `assets/ponchi/experiments/batches/ponchi-batch-003/B-31_base_1254x627.png`. Presence does not establish overlay audit PASS, usage permission, adoption, or publication. Do not attach the composite to image generation; any future use needs item-specific clearspace and usage-condition review. |
| `B-32` | Figma | required | `official_logo_applied_unreviewed` | `assets/logos/figma/figma-favicon.svg` | 現行finalにFigma faviconが見える。legacy batch-003は `official_logo_applied / overlay_audit`。local asset SHA-256 `E6227B7DBC49C86DA6F4CCFA02BA439428106B0CA627A0A33EA6AD1E09F335B3`。用途条件・item-local clearspace未確認。Batch003 baseの共有screening ROI `[686,0,520,180]` は93,600画素中92,451画素が非白で、余白再構成が必要。標準ROIは個別ブランド規定ではない。 |
| `B-33` | Canva | required | `official_logo_applied_unreviewed` | `assets/logos/canva/Canva-logos/Canva logos/png/512x512/Canva type logo_512x180.png` | Local official asset: Canva official developer brand-guidelines package, retrieved 2026-06-03; SHA-256 `6B9BF772EE1AC4F8C4969BBD0875C1787A9DA7ABF806F244D5CFFCB9C304D754`. Current final contains the mark; legacy generation record is `official_logo_applied` / `overlay_audit` / `not_reviewed`. A separate logo-free base exists at `assets/ponchi/experiments/batches/ponchi-batch-003/B-33_base_1254x627.png`. Presence does not establish overlay audit PASS, usage permission, adoption, or publication. Do not attach the composite to image generation; any future use needs item-specific clearspace and usage-condition review. |
| `B-40` | Reddit | required | `official_logo_applied` | `assets/logos/reddit/Reddit_Lockup_Logo.svg` | 現行finalに公式Reddit lockupを適用済み。公式brand page由来、取得2026-06-03。個別利用条件は未確認。新候補はロゴなし`internal_base_only`に限定し、合成・採用・公開は条件確認後。
| `B-41` | arXiv | required | `official_logo_source_review_required` | none | batch-003 対象。公式ロゴ/識別マークの有無と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-50` | Claude の料金プラン | required | `official_logo_applied` | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/1 Claude logo/PNG/Claude logo - Slate.png` | 現行finalに公式Claudeロゴを適用済み。個別利用条件・料金図での使用条件は未確認。新候補はロゴなし`internal_base_only`に限定。
| `B-51` | ChatGPT の料金プラン | required | `official_logo_source_review_required` | none | OpenAI/ChatGPT 関連の料金プラン項目。OpenAI wordmark か ChatGPT 固有表現かを決めてから合成 |
| `B-52` | Gemini の料金プラン | required | `official_logo_available` | `assets/logos/gemini/gemini_sparkle_4g_512_lt.png` | 公式 `gemini.google.com` 由来の素材。2026-06-03 取得、SHA256 `5e7cfecaa53f4f65a313fe89b0f389548126544a78fad8489510c70ae641a4a1`。料金比較図での用途適合・利用条件・許諾は未確認のため、確認までは合成しない |
| `B-60` | Suno | required | `official_logo_source_review_required` | none | batch-003 対象。公式ロゴ素材・利用条件・ローカルパスを確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `B-61` | ACE-Step 1.5 | required | `official_logo_applied_unreviewed` | `assets/logos/ace-step/acestep_logo.png` | 現行finalにACE-Step markが見える。legacy batch-003は `official_logo_applied / overlay_audit`。公式GitHub repo由来のlocal asset SHA-256 `C79FD7BDBE424100DC0601E204234AAE2DA237B4F3D2609C1A35FB14D00578BC`。元画像の黒背景をcrop/recolorしない。用途条件・item-local clearspace未確認。 |
| `C-1` | OpenAI | required | `official_logo_applied` | `assets/logos/openai/openai_wordmark_black_official_template_layer.png` | 現行finalに公式OpenAI wordmarkを適用済み。`brand_usage_audit.md`に公式package由来を記録。個別用途条件は未確認。新候補のロゴは生成せず、条件確認まではロゴなし`internal_base_only`。
| `C-2` | Anthropic | required | `official_logo_available` | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Anthropic logos/1 Anthropic logo/PNG/Anthropic logo - Slate.png` | Anthropic 公式ロゴはローカルにある。C-2 用ベース生成後に後合成可 |
| `C-3` | Google DeepMind | required | `official_logo_applied_unreviewed` | `assets/logos/google-deepmind/google_deepmind_48dp.svg` | 現行finalにGoogle DeepMind iconが見える。legacy batch-003は `official_logo_applied / overlay_audit`。local asset SHA-256 `1327A382A5A6FDC51E1CA385F5354FB3A1731EC024B150A692A8297BC4AAEF71`。用途条件とitem-local clearspace未確認。 |
| `C-4` | Meta AI | required | `official_logo_applied_unreviewed` | `assets/logos/meta-ai/meta-ai-orbit-logo-gradient-3d_light.goto.png` | 現行finalにMeta AI orbが見える。legacy batch-003は `official_logo_applied / overlay_audit`。公式SVG由来のlocal render SHA-256 `D16D719198281BC792212AD0A6C1195811DD3D50A1DCB57C58B66FE89943223D`。用途条件とitem-local clearspace未確認。 |
| `C-5` | xAI | required | `official_logo_source_review_required` | none | xAI の公式ロゴ/利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `C-6` | Mistral AI | required | `official_logo_source_review_required` | none | Mistral AI の公式ロゴ/利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `C-7` | Hugging Face | required | `official_logo_source_review_required` | none | Hugging Face の公式ロゴ/利用条件と mascot 使用可否を確認するまで、AI 生成ロゴ・mascotは禁止してベースだけ作る |
| `C-8` | Microsoft AI | not_needed | `logo_avoid` | none | 現brand auditで専用logo/organization lockup未確認。logo-less `logo_avoid` / `color_audit`に確定。Microsoft markを創作せず、製品関係だけ一般形状で表現 |
| `C-9` | NVIDIA | required | `official_logo_source_review_required` | none | NVIDIA の公式ロゴ/利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `C-10` | Moonshot AI | required | `official_logo_source_review_required` | none | Batch004 対象。公式ロゴ/利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `C-11` | Z.ai | required | `official_logo_source_review_required` | none | Batch004 対象。公式ロゴ/利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `C-12` | TSMC | required | `official_logo_source_review_required` | none | Batch004 対象。旧generation ledgerは `not_available_after_source_review / logo_avoid / assetなし`。見出しが企業名のため本マトリクス方針に沿って要件を更新し、旧判定を履歴として明示した。公式素材/利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `C-13` | Groq | required | `official_logo_source_review_required` | none | Batch004 対象。公式ロゴ/利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `C-14` | AMD | required | `official_logo_source_review_required` | none | Batch004 対象。公式ロゴ/利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `C-50` | Sam Altman | not_needed | `logo_avoid` | none | 人物項目。公式ロゴではなく、実在人物の写実的 likeness も避け、抽象タイムライン/関係図としてベースを作る |
| `C-51` | Dario Amodei | not_needed | `logo_avoid` | none | 人物項目。公式ロゴではなく、実在人物の写実的 likeness も避け、抽象タイムライン/関係図としてベースを作る |
| `C-52` | Demis Hassabis | not_needed | `logo_avoid` | none | 人物項目。公式ロゴではなく、実在人物の写実的 likeness も避け、抽象タイムライン/関係図としてベースを作る |
| `C-53` | Andrej Karpathy | not_needed | `logo_avoid` | none | 人物項目。公式ロゴではなく、実在人物の写実的 likeness も避け、抽象タイムライン/関係図としてベースを作る |
| `C-54` | Ilya Sutskever | not_needed | `logo_avoid` | none | 人物項目。公式ロゴではなく、実在人物の写実的 likeness も避け、抽象タイムライン/関係図としてベースを作る |
| `C-55` | Mira Murati | not_needed | `logo_avoid` | none | 人物項目。公式ロゴではなく、実在人物の写実的 likeness も避け、抽象タイムライン/関係図としてベースを作る |
| `C-56` | Yann LeCun | not_needed | `logo_avoid` | none | 人物項目。公式ロゴではなく、実在人物の写実的 likeness も避け、抽象タイムライン/関係図としてベースを作る |
| `C-57` | Geoffrey Hinton | not_needed | `logo_avoid` | none | 人物項目。公式ロゴではなく、実在人物の写実的 likeness も避け、抽象タイムライン/関係図としてベースを作る |
| `C-58` | Elon Musk | not_needed | `logo_avoid` | none | 人物項目。公式ロゴではなく、実在人物の写実的 likeness も避け、抽象タイムライン/関係図としてベースを作る |
| `C-59` | Jensen Huang | not_needed | `logo_avoid` | none | 人物項目。公式ロゴではなく、実在人物の写実的 likeness も避け、抽象タイムライン/関係図としてベースを作る |
| `C-60` | Ray Kurzweil | not_needed | `logo_avoid` | none | 人物項目。公式ロゴではなく、実在人物の写実的 likeness も避け、抽象タイムライン/関係図としてベースを作る |
| `C-80` | AI大学 | required | `official_logo_source_review_required` | none | YouTube チャンネル/媒体項目。公式チャンネルアイコン等の扱いを確認するまで、AI 生成ロゴ・チャンネルアイコンは禁止してベースだけ作る |
| `C-81` | にゃんた | required | `official_logo_applied` | `assets/logos/nyanta/youtube-channel-avatar.jpg` | 現行 final は公式 YouTube アバターを未改変で後合成済み。出所確認は公開・商用利用許諾の確認ではない。新候補は条件確認まで `internal_base_only` とし、アバターを描き直さない |
| `C-82` | まさお | required | `official_logo_applied` | `assets/logos/masao/youtube-channel-avatar.jpg` | 現行 final は公式 YouTube アバターを未改変で後合成済み。出所確認は公開・商用利用許諾の確認ではない。新候補は条件確認まで `internal_base_only` とし、アバターを描き直さない |
| `C-83` | AI時代の羅針盤 | required | `official_logo_applied` | `assets/logos/ai-compass/youtube-channel-avatar.jpg` | 現行finalに保存済み公式YouTube avatarを未改変適用済み。個別利用許諾は未確認。記事/辞書タイトルをAI時代の羅針盤に修正済み。新候補はavatar領域を空けたロゴなし`internal_base_only`に限定。
| `D-1` | Gemini 2 系 | required | `official_logo_source_review_required` | none | Batch005 対象。Gemini/Google の公式プロダクト表現と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-2` | Gemini 2.5 系 | required | `official_logo_source_review_required` | none | Batch005 対象。Gemini/Google の公式プロダクト表現と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-3` | Gemini 3 系 | required | `official_logo_source_review_required` | none | Batch005 対象。Gemini/Google の公式プロダクト表現と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-4` | Gemini 3.1 系 | required | `official_logo_applied_unreviewed` | `assets/logos/gemini/gemini_sparkle_4g_512_lt.png` | 現行finalにGemini sparkleが見える。legacy batch-005は `official_logo_applied / overlay_audit`。local asset SHA-256 `5E7CFECAA53F4F65A313FE89B0F389548126544A78FAD8489510C70AE641A4A1`。用途条件・item-local clearspace未確認。 |
| `D-10` | Claude 3 系 | required | `official_logo_source_available_needs_import` | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/1 Claude logo/PNG/Claude logo - Slate.png` | Batch005 対象。Claude 公式ロゴはローカルにあるが、モデル系列図での使用可否と配置を確認してから合成 |
| `D-11` | Claude 3.5 系 | required | `official_logo_source_available_needs_import` | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/1 Claude logo/PNG/Claude logo - Slate.png` | Batch005 対象。Claude 公式ロゴはローカルにあるが、モデル系列図での使用可否と配置を確認してから合成 |
| `D-12` | Claude 4 系 | required | `official_logo_source_available_needs_import` | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/1 Claude logo/PNG/Claude logo - Slate.png` | モデル系列名に Claude が入るためロゴ対象。公式素材はローカルにあるが、モデル系列図での使用可否と配置を確認してから合成 |
| `D-13` | Claude 4.5 系 | required | `official_logo_source_available_needs_import` | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/1 Claude logo/PNG/Claude logo - Slate.png` | Batch005 対象。Claude 公式ロゴはローカルにあるが、モデル系列図での使用可否と配置を確認してから合成 |
| `D-14` | Claude Mythos Preview | required | `official_logo_applied_unreviewed` | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/1 Claude logo/PNG/Claude logo - Slate.png` | 現行finalにClaude wordmarkが見える。legacy batch-005は `official_logo_applied / overlay_audit`。local official asset SHA-256 `F95E9DD722B51B10312B1E62E139389293C8A31CD6101A694290BF767765F85B`。用途条件とitem-local clearspace未確認。Mythosの提供状況・利用条件など時変事実はprompt前に更新確認する。 |
| `D-20` | GPT-5 系 | required | `official_logo_available` | `assets/logos/openai/openai_wordmark_black_official_template_layer.png` | Batch005 対象。OpenAI 公式 wordmark はローカルにある。モデル系列図での使用可否と配置を確認してから合成 |
| `D-21` | GPT-4 系 | required | `official_logo_available` | `assets/logos/openai/openai_wordmark_black_official_template_layer.png` | Batch005 対象。OpenAI 公式 wordmark はローカルにある。モデル系列図での使用可否と配置を確認してから合成 |
| `D-22` | o1 系 | required | `official_logo_applied_unreviewed` | `assets/logos/openai/openai_wordmark_black_official_template_layer.png` | Current final contains the OpenAI wordmark; local source asset SHA-256 `665AAB5B3A7221F66EDF868F8654078E22518BD335764E578E31E4EE6D86478B`. Legacy generation record is `official_logo_applied` / `overlay_audit` / `not_reviewed`. The distinct logo-free base is `assets/ponchi/experiments/batches/ponchi-batch-005/D-22_base_1254x627.png` (SHA-256 `40D5CEF7AE69EA7C0F65C235F318C7CB12A27044EE7726C42D066CA484E3A477`). Mark presence is not a review or use authorization. Any future overlay needs item-specific review; never use the current composite as generation input. |
| `D-23` | o3 系 | required | `official_logo_available` | `assets/logos/openai/openai_wordmark_black_official_template_layer.png` | Batch005 対象。OpenAI 公式 wordmark はローカルにある。モデル系列図での使用可否と配置を確認してから合成 |
| `D-24` | GPT-3 系 | required | `official_logo_available` | `assets/logos/openai/openai_wordmark_black_official_template_layer.png` | Batch005 対象。OpenAI 公式 wordmark はローカルにある。モデル系列図での使用可否と配置を確認してから合成 |
| `D-25` | GPT-1 / GPT-2 系 | required | `official_logo_available` | `assets/logos/openai/openai_wordmark_black_official_template_layer.png` | Batch005 対象。OpenAI 公式 wordmark はローカルにある。モデル系列図での使用可否と配置を確認してから合成 |
| `D-26` | gpt-oss | required | `official_logo_available` | `assets/logos/openai/openai_wordmark_black_official_template_layer.png` | Batch005 対象。OpenAI 関連モデル名として扱い、公式 wordmark の使用可否と配置を確認してから合成 |
| `D-30` | Grok 系 | required | `official_logo_source_review_required` | none | Batch005 対象。xAI/Grok の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-35` | Cursor Composer | required | `official_logo_applied` | `assets/logos/cursor/cursor-brand-assets/General Logos/Lockup Horizontal/PNG/LOCKUP_HORIZONTAL_2D_LIGHT.png` | 現行 final は公式 Cursor horizontal lockup を後合成済み。Composer項目での新規使用条件と配置は別途確認し、新候補は確認まで `internal_base_only` |
| `D-40` | Llama 系 | required | `official_logo_applied` | `assets/logos/llama/llama-official-preload.svg` | 現行finalで見えるのは公式Meta組織マーク（Llama製品固有lockupではない）。brand_usage_audit.mdの2026-06-03記録を正とし、個別使用条件はreview-pending。新候補はロゴなしinternal_base_only。AI生成ロゴは禁止。 |
| `D-41` | Mistral 系 | required | `official_logo_applied_unreviewed` | `assets/logos/mistral/mistral-cover-logo-icon-gradient.transparent.png` | 現行finalにMistral iconが見える。legacy batch-005は `official_logo_applied / overlay_audit`。local official asset SHA-256 `C08DE8EB11749B15C493688695EB911EA4FB116FCC9EFB9BA77B42EEA220E73D`。用途条件・item-local clearspace未確認。ライセンスは版ごとに確認し一括表記しない。 |
| `D-42` | Gemma 系 | required | `official_logo_source_review_required` | none | Batch006 対象。Google/Gemma の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-43` | Qwen 系 | required | `official_logo_source_review_required` | none | Batch006 対象。Qwen/Alibaba Cloud の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-44` | Kimi | required | `official_logo_applied_unreviewed` | `assets/logos/kimi/kimi-icon-official.webp` | Local official asset: official Moonshot AI homepage, retrieved 2026-06-03; SHA-256 `EC4E731C4232D36B72A7AB12253F34E8D95F83486C0E60DDCAB50ACD9E144418`. Current final contains the mark; legacy generation record is `official_logo_applied` / `overlay_audit` / `not_reviewed`. A separate logo-free base exists at `assets/ponchi/experiments/batches/ponchi-batch-006/D-44_base_1254x627.png`. Presence does not establish overlay audit PASS, usage permission, adoption, or publication. Do not attach the composite to image generation; any future use needs item-specific clearspace and usage-condition review. |
| `D-45` | GLM | required | `official_logo_applied` | `assets/logos/z-ai/z-ai-logo-official.512.png` | 現行finalの後合成はZ.ai組織アイコンでありGLM専用ロゴではない。公式z.ai由来・取得2026-06-03。適用妥当性/個別利用条件はreview-pending。新候補はロゴなし`internal_base_only`、再合成しない。
| `D-46` | DeepSeek V3 | required | `official_logo_source_review_required` | none | Batch006 対象。DeepSeek の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-47` | DeepSeek R1 | required | `official_logo_source_review_required` | none | Batch006 対象。DeepSeek の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-50` | DALL-E | required | `official_logo_available` | `assets/logos/openai/openai_wordmark_black_official_template_layer.png` | Batch006 対象。OpenAI 公式 wordmark はローカルにある。画像生成モデル項目での使用可否と配置を確認してから合成 |
| `D-51` | Imagen | required | `official_logo_source_review_required` | none | Batch006 対象。Google/Imagen の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-52` | Sora | required | `official_logo_available` | `assets/logos/openai/openai_wordmark_black_official_template_layer.png` | Batch006 対象。OpenAI 公式 wordmark はローカルにある。動画生成モデル項目での使用可否と配置を確認してから合成 |
| `D-53` | Veo | required | `official_logo_source_review_required` | none | Batch006 対象。Google/Veo の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-54` | Stable Diffusion | required | `official_logo_source_review_required` | none | Batch006 対象。Stability AI / Stable Diffusion の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-55` | Nano Banana | required | `official_logo_source_review_required` | none | Batch006 対象。公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-56` | Seedance | required | `official_logo_source_review_required` | none | Batch006 対象。Seedance/提供元の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-57` | Flow | required | `official_logo_source_review_required` | none | Batch006 対象。Flow/提供元の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-58` | Whisk | required | `official_logo_source_review_required` | none | Batch006 対象。Whisk/提供元の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-60` | AlphaGo | required | `official_logo_source_review_required` | none | Batch006 対象。Google DeepMind/AlphaGo の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-70` | Amical | required | `official_logo_source_review_required` | none | Batch006 対象。公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `D-71` | Whisper | required | `official_logo_applied` | `assets/logos/openai/openai_wordmark_black_official_template_layer.png` | 現行 final は OpenAI 公式 wordmark を後合成済み。これは Whisper 固有マークではない。OpenAI mark の用途条件を別途確認し、新候補は確認まで `internal_base_only` |
| `E-1` | SWE-Bench | not_needed | `logo_avoid` | none | Batch006 対象。ベンチマーク項目として汎用評価図で説明し、ロゴや公式アイコンは使わない |
| `E-2` | SWE-Bench Verified | not_needed | `logo_avoid` | none | Batch006 対象。ベンチマーク項目として汎用評価図で説明し、ロゴや公式アイコンは使わない |
| `E-3` | Terminal-Bench | not_needed | `logo_avoid` | none | Batch007 対象。ベンチマーク項目として汎用評価図で説明し、ロゴや公式アイコンは使わない |
| `E-4` | HumanEval | not_needed | `logo_avoid` | none | Batch007 対象。ベンチマーク項目として汎用評価図で説明し、ロゴや公式アイコンは使わない |
| `E-20` | MMLU | not_needed | `logo_avoid` | none | Batch007 対象。知識・推論ベンチマークの汎用評価図で説明し、ロゴや公式アイコンは使わない |
| `E-21` | MMLU-Pro | not_needed | `logo_avoid` | none | Batch007 対象。知識・推論ベンチマークの汎用評価図で説明し、ロゴや公式アイコンは使わない |
| `E-22` | GPQA | not_needed | `logo_avoid` | none | Batch007 対象。専門問題ベンチマークの汎用評価図で説明し、ロゴや公式アイコンは使わない |
| `E-23` | GSM8K | not_needed | `logo_avoid` | none | Batch007 対象。算数推論ベンチマークの汎用評価図で説明し、ロゴや公式アイコンは使わない |
| `E-24` | MATH | not_needed | `logo_avoid` | none | Batch007 対象。数学推論ベンチマークの汎用評価図で説明し、ロゴや公式アイコンは使わない |
| `E-25` | AIME | not_needed | `logo_avoid` | none | Batch007 対象。競技数学ベンチマークの汎用評価図で説明し、ロゴや公式アイコンは使わない |
| `E-26` | Humanity's Last Exam | not_needed | `logo_avoid` | none | Batch007 対象。総合難問ベンチマークの汎用評価図で説明し、ロゴや公式アイコンは使わない |
| `E-27` | IQ Bench | not_needed | `logo_avoid` | none | Batch007 対象。知能評価ベンチマークの汎用評価図で説明し、ロゴや公式アイコンは使わない |
| `E-30` | TAU-Bench | not_needed | `logo_avoid` | none | Batch007 対象。エージェント評価の汎用図で説明し、ロゴや公式アイコンは使わない |
| `E-31` | WebArena | not_needed | `logo_avoid` | none | Batch007 対象。Web 操作評価の汎用図で説明し、ロゴや公式アイコンは使わない |
| `E-32` | GAIA | not_needed | `logo_avoid` | none | Batch007 対象。複合タスク評価の汎用図で説明し、ロゴや公式アイコンは使わない |
| `E-33` | AgentBench | not_needed | `logo_avoid` | none | Batch007 対象。エージェント評価の汎用図で説明し、ロゴや公式アイコンは使わない |
| `E-34` | OSWorld | required | `official_logo_source_review_required` | none | 見出しの正式benchmark名はmatrix方針に沿ってブランド対象として扱う。旧batch-007 ledgerの `not_needed / logo_avoid` は旧判定として残し、本matrix方針により再評価。公式markの有無・適用要否・利用条件を確認するまでAI生成や推測合成は禁止し、概念図は内部ベースに止める。別件のMay 2026スコア/variantはbrief date/sourceと照合が必要 |
| `E-50` | Chatbot Arena | not_needed | `logo_avoid` | none | Batch007 対象。モデル比較・投票評価の汎用図で説明し、ロゴや公式アイコンは使わない |
| `E-51` | LMSYS Arena | required | `official_logo_source_review_required` | none | briefはLMSYS研究グループ→Chatbot Arena→LMArena独立の沿革を主題とし、見出しにも固有名を含む。旧generation ledgerの `not_needed / logo_avoid` を本マトリクス方針に沿って更新。どの公式markが各時点・主体を正しく表すか、公式素材と個別利用条件を確認するまで採用・合成せず、AI生成のロゴも禁止 |
| `F-1` | JavaScript | not_needed | `logo_avoid` | none | JS, TypeScript, React, Node.js などのロゴを使わない。汎用ファイル、ブラウザ、サーバ記号だけにする |
| `F-2` | TypeScript | not_needed | `logo_avoid` | none | TypeScript ロゴを使わない。Before/After の汎用型チェック表現で説明する |
| `F-3` | Python | not_needed | `logo_avoid` | none | Batch007 対象。Python ロゴや蛇のマスコット表現を使わず、汎用コード・実行・データ処理の図で説明する |
| `F-4` | HTML | not_needed | `logo_avoid` | none | Batch008 対象。HTML5 ロゴは使わず、文書構造とブラウザ表示の汎用図で説明する |
| `F-5` | CSS | not_needed | `logo_avoid` | none | Batch008 対象。CSS3 ロゴは使わず、スタイル適用の汎用図で説明する |
| `F-6` | Markdown | not_needed | `logo_avoid` | none | Batch008 対象。Markdown ロゴは使わず、原稿からプレビューへの変換図で説明する |
| `F-7` | YAML | not_needed | `logo_avoid` | none | Batch008 対象。ロゴ不要。設定ファイルと構造化データの汎用図で説明する |
| `F-8` | JSON | not_needed | `logo_avoid` | none | Batch008 対象。ロゴ不要。API データと構造化オブジェクトの汎用図で説明する |
| `F-9` | SVG | not_needed | `logo_avoid` | none | Batch008 対象。SVG ロゴは使わず、ベクター図形と拡大縮小の汎用図で説明する |
| `F-10` | React | required | `official_logo_source_review_required` | none | Batch008 対象。公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-11` | Next.js | required | `official_logo_applied` | `assets/logos/nextjs/nextjs-assets/NEXTJS/logotype/light-background/nextjs-logotype-light-background.svg` | 現行finalに公式Next.js logotypeを適用済み。公式Vercel brand assets由来、取得2026-06-03。個別利用条件は未確認。新候補はロゴなし`internal_base_only`。
| `F-12` | Electron | required | `official_logo_source_review_required` | none | Batch008 対象。公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-13` | Tauri | required | `official_logo_source_review_required` | none | Batch008 対象。公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-14` | three.js | required | `official_logo_available` | `assets/logos/threejs/icon.svg` | 公式three.js repository由来、取得2026-06-03（brand audit）。用途条件未確認。AI生成に公式iconを使わず、再設計候補はlogo-free internal baseまで |
| `F-15` | shadcn/ui | required | `official_logo_applied_unreviewed` | `assets/logos/shadcn-ui/apple-touch-icon.png` | Local official asset: official shadcn/ui site, retrieved 2026-06-03; SHA-256 `87FE38764DA1304F7238C3B2BCF24BC768008DCBD2B127EE44CDDC6D26D070ED`. Current final contains the mark; legacy generation record is `official_logo_applied` / `overlay_audit` / `not_reviewed`. A separate logo-free base exists at `assets/ponchi/experiments/batches/ponchi-batch-008/F-15_base_1254x627.png`. In ROI `[686,0,520,180]`, 4,429 pixels are not pure white; 2,733 is the stricter RGB `<245` count and does not satisfy the blank-area gate. Do not create a sidecar until the ROI is pure white and independently re-audited. Usage conditions, adoption, and publication remain unapproved. |
| `F-16` | Tailwind CSS | required | `official_logo_available` | `assets/logos/tailwindcss/tailwindcss-logotype.svg` | 公式Tailwind CSS site repo由来、取得2026-06-03（brand audit）。用途条件未確認。新候補はlogo-free internal base、公式assetは別overlay review |
| `F-17` | Astro | required | `official_logo_source_review_required` | none | Batch008 対象。公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-20` | ESLint | required | `official_logo_applied_unreviewed` | `assets/logos/eslint/eslint-logo-color.svg` | Official ESLint repo asset, retrieved 2026-06-03; SHA-256 `04886AA1B790E600A1478060723FA23FA5A615E32A8C5BB374534FDCBA9DD7D5`. Current final SHA-256 `128ec9c622a24ad82ed4adc33d69c8d802c4bb5f804316614d4fd8f8e6f99df5` contains the mark; legacy generation record is `official_logo_applied` / `overlay_audit` / `not_reviewed`. Separate logo-free base is `assets/ponchi/experiments/batches/ponchi-batch-008/F-20_base_1254x627.png` (SHA-256 `44cb15c898ed0b502a1b6796630a7397729086d73cbfc62f18b05363fa186402`). On that base, `[686,0,520,180]` has 2,766 nonwhite pixels; hold sidecar/generation until cleared and independently re-audited. Use conditions remain unverified. |
| `F-21` | Prettier | required | `official_logo_source_review_required` | none | Batch008 対象。公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-30` | VS Code | required | `official_logo_source_review_required` | none | Batch008 対象。Microsoft / VS Code の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-34` | VS Code 拡張機能 | required | `official_logo_applied` | `assets/logos/vscode/visual-studio-code-icons/visual-studio-code-icons/vscode.svg` | 現行finalに公式VS Code iconを適用済み。公式brand page由来、取得2026-06-03。個別利用条件は未確認。新候補はロゴなし`internal_base_only`。Copilot/Claudeロゴや偽UIは禁止。
| `F-35` | Markdown Preview Enhanced | required | `official_logo_source_review_required` | none | Batch008 対象。拡張機能の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-36` | Git Graph | required | `official_logo_source_review_required` | none | Batch008 対象。拡張機能の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-37` | Japanese Language Pack for VS Code | required | `official_logo_available` | `assets/logos/vscode-language-pack-ja/languagepack.png` | Microsoft `vscode-loc` (`https://github.com/microsoft/vscode-loc`) 公式リポジトリ由来。2026-06-03 取得、SHA256 `00446b52fa5fe7550f8618f5fe8a8dbba6d1b241fecb01490dc9ac4c90da04ac`。個別用途の適合・利用条件・許諾は未確認。メニュー対応の正確な表示も保留し、確認までは合成しない |
| `F-38` | Markdown All in One | required | `official_logo_source_review_required` | none | Batch009 対象。拡張機能の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-40` | npm | required | `official_logo_applied` | `assets/logos/npm/npm-logo-black.svg` | 現行finalにローカル公式npmロゴを適用済み（brand_usage_audit.mdに出典・2026-06-03取得を記録）。個別の利用条件は未確認。新候補はロゴなしinternal_base_only。AI生成ロゴは禁止。 |
| `F-41` | Vite | required | `official_logo_source_review_required` | none | Batch009 対象。Vite 公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-42` | ビルド | not_needed | `logo_avoid` | none | Batch009 対象。概念図。ロゴ不要 |
| `F-44` | pnpm | required | `official_logo_source_review_required` | none | Batch009 対象。pnpm 公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-50` | git | required | `official_logo_available` | `assets/logos/git/Git-Logo-Black.svg` | 公式Gitロゴをローカル保存済み（brand_usage_audit.mdに出典・2026-06-03取得を記録）。個別の利用条件は未確認。internal_base_onlyを上限とし、AI生成ロゴは禁止。
| `F-51` | git push | not_needed | `logo_avoid` | none | Batch009 対象。Git 操作の概念図として扱い、ロゴや公式アイコンは使わない |
| `F-52` | git pull | not_needed | `logo_avoid` | none | Batch009 対象。Git 操作の概念図として扱い、ロゴや公式アイコンは使わない |
| `F-53` | branch | not_needed | `logo_avoid` | none | Batch009 対象。Git 分岐概念図として扱い、ロゴや公式アイコンは使わない |
| `F-54` | commit | not_needed | `logo_avoid` | none | Batch009 対象。Git 履歴概念図として扱い、ロゴや公式アイコンは使わない |
| `F-55` | merge | not_needed | `logo_avoid` | none | Batch009 対象。Git 統合概念図として扱い、ロゴや公式アイコンは使わない |
| `F-56` | .gitignore | not_needed | `logo_avoid` | none | Batch009 対象。ファイル除外概念図として扱い、ロゴや公式アイコンは使わない |
| `F-57` | リポジトリ | not_needed | `logo_avoid` | none | Batch009 対象。リポジトリ概念図として扱い、ロゴや公式アイコンは使わない |
| `F-58` | git stash | not_needed | `logo_avoid` | none | Batch009 対象。一時退避概念図として扱い、ロゴや公式アイコンは使わない |
| `F-59` | README.md | not_needed | `logo_avoid` | none | Batch009 対象。ドキュメント概念図として扱い、ロゴや公式アイコンは使わない |
| `F-60` | GitHub | required | `official_logo_applied_unreviewed` | `assets/logos/github/GitHub_Logos/GitHub Logos/PNG/GitHub_Lockup_Black_Clearspace.png` | 現行finalに公式 lockup が見える。legacy batch-009は `official_logo_applied / overlay_audit`。local asset SHA-256 `0F09C631536DD9EB8588975573560D810CD84A3A29094EFD27257A030DAA95E0`。用途条件・item-local clearspace未確認。Batch010の別base候補では右上の予約範囲 x=686,y=36,w=520px を空ける条件を記録したが、ベースとROIは独立再監査まで未承認。 |
| `F-61` | Pull Request | required | `official_logo_source_review_required` | none | Batch009 対象。GitHub 関連項目として公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-62` | GitHub Actions | required | `official_logo_applied_unreviewed` | `assets/logos/github/GitHub_Logos/GitHub Logos/PNG/GitHub_Lockup_Black_Clearspace.png` | Local official asset: official imported GitHub logo package; local asset hash verified 2026-09-28; SHA-256 `0F09C631536DD9EB8588975573560D810CD84A3A29094EFD27257A030DAA95E0`. Current final contains the mark; legacy generation record is `official_logo_applied` / `overlay_audit` / `not_reviewed`. A separate logo-free base exists at `assets/ponchi/experiments/batches/ponchi-batch-009/F-62_base_1254x627.png`. In ROI `[686,0,520,180]`, 1,817 pixels are not pure white; 1,355 is the stricter RGB `<245` count and does not satisfy the blank-area gate. Keep sidecar/generation blocked until the ROI is pure white and independently re-audited. The manual-vs-push meaning and usage conditions also remain unresolved. |
| `F-71` | ripgrep (rg) | not_needed | `logo_avoid` | none | Batch009 対象。検索ツール概念図として扱い、ロゴや公式アイコンは使わない |
| `F-80` | Node.js | required | `official_logo_applied_unreviewed` | `assets/logos/nodejs/nodejsDark.svg` | Official Node.js repo asset, retrieved 2026-06-03; SHA-256 `69FE820A6DFDB829A0767EB2450B42A7D376257B4C15DE72D4361E4D888459B3`. Current final SHA-256 `7bca9ceeb486a21a66fc35ddc7a7df40537ef19415123db555ad0aa64d299c88` contains the mark; legacy generation record is `official_logo_applied` / `overlay_audit` / `not_reviewed`. Separate logo-free base is `assets/ponchi/experiments/batches/ponchi-batch-010/F-80_base_1254x627.png` (SHA-256 `2315e348608d4f079e52f7fe575e943608848a115fb349bab76f9cea657a5a04`). On that base, `[686,0,520,180]` has 2,555 nonwhite pixels; hold sidecar/generation until cleared and independently re-audited. Use conditions remain unverified. |
| `F-81` | bash | not_needed | `logo_avoid` | none | Batch010 対象。シェル概念図として扱い、ロゴや公式アイコンは使わない |
| `F-82` | WSL | required | `official_logo_source_review_required` | none | Batch010 対象。Microsoft/WSL 関連素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-83` | PowerShell | required | `official_logo_applied_unreviewed` | `assets/logos/powershell/logo-powershell-core.svg` | 現行finalにPowerShell markが見える。legacy batch-010は `official_logo_applied / overlay_audit`。Microsoft Learn公式asset SHA-256 `9D7F87766799B55A73112A9A160F39EADBAA482406EF86CDC2C138BB1FE40471`。用途条件・item-local clearspace未確認。baseの共有screening ROI `[686,0,520,180]` は4,025非白画素で、標準ROIは個別ブランド規定ではない。 |
| `F-84` | Ghostty | required | `official_logo_applied` | `assets/logos/ghostty/social-share-card.jpg` | 現行 final は Ghostty 公式 social-share card を未改変で縮小合成済み。単体ロゴではない。新候補は用途条件の確認まで `internal_base_only` |
| `F-85` | SuperClaude Framework | required | `official_logo_source_review_required` | none | 公式リポジトリ調査で SuperClaude 固有の logo/icon/lockup は見つからず、Claude/Anthropic のマークは代用しない。タイトルに製品名を含むため required のまま。公式の個別表示方法・利用条件が決まるまで、AI 生成 wordmark や代替ロゴは禁止 |
| `F-86` | ollama | required | `official_logo_source_review_required` | none | Batch010 対象。Ollama 公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-87` | sudo | not_needed | `logo_avoid` | none | Batch010 対象。権限昇格の概念図として扱い、ロゴや公式アイコンは使わない |
| `F-90` | Docker | required | `official_logo_available` | `assets/logos/docker/Docker-Logos-1/docker-logos/SVG/docker-logo-black.svg` | Docker公式media resources由来、取得2026-06-03（brand audit）。用途条件未確認。新候補はlogo-free internal base、公式assetは別overlay review |
| `F-91` | .env | not_needed | `logo_avoid` | none | Batch010 対象。環境変数ファイルの概念図として扱い、ロゴや公式アイコンは使わない |
| `F-100` | 拡張子早見表 | not_needed | `logo_avoid` | none | Batch010 対象。ファイル形式の概念図として扱い、ロゴや公式アイコンは使わない |
| `F-101` | .ico | not_needed | `logo_avoid` | none | Batch010 対象。アイコンファイル形式の概念図として扱い、ロゴや公式アイコンは使わない |
| `F-102` | .mp4 | not_needed | `logo_avoid` | none | Batch010 対象。動画ファイル形式の概念図として扱い、ロゴや公式アイコンは使わない |
| `F-103` | .mp3 | not_needed | `logo_avoid` | none | Batch010 対象。音声ファイル形式の概念図として扱い、ロゴや公式アイコンは使わない |
| `F-104` | .webp | not_needed | `logo_avoid` | none | Batch010 対象。画像ファイル形式の概念図として扱い、ロゴや公式アイコンは使わない |
| `F-110` | Lighthouse | required | `official_logo_source_review_required` | none | Batch010 対象。Google/Chrome Lighthouse の公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-111` | a11y | not_needed | `logo_avoid` | none | Batch010 対象。アクセシビリティ概念図として扱い、ロゴや公式アイコンは使わない |
| `F-120` | PostgreSQL | required | `official_logo_source_review_required` | none | Batch010 対象。PostgreSQL 公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-121` | SQLite | required | `official_logo_applied_unreviewed` | `assets/logos/sqlite/sqlite370_banner.svg` | 現行final SHA-256 `941E4A1C9220DF19DDF25BB4EED73DE76ED2434D5D8DEC59CD7E5051CC2E92C2` にSQLite markが見える。旧batch-010 ledgerは `official_logo_applied / overlay_audit / not_reviewed`。SQLite公式素材はlocalにありasset SHA-256 `462C4CE8229B585DD6880CD308B121D9DE63EB619DB05E469598594E80D7B151`。用途条件未確認。正準briefは左の単一 `.db` file と右のPostgreSQL server rackを中心比較に指定し、開発者ローカル・mobile app・SQLite MCPの3利用場面も列挙する。中心比較を維持し、3場面は同じ構図内の控えめな補助cueとして過密化せず保持する。旧promptの予約範囲 x≥752,y<157 は個別公式clearspaceと確認されておらず、現行規定として扱わない。 |
| `F-122` | Prisma | required | `official_logo_source_review_required` | none | Batch010 対象。Prisma 公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-123` | ORM | not_needed | `logo_avoid` | none | Batch011 対象。概念図として表現し、DB/製品ロゴは使わない |
| `F-130` | OAuth | not_needed | `logo_avoid` | none | Batch011 対象。認可フローの概念図。プロバイダロゴ不要 |
| `F-140` | Mermaid | required | `official_logo_source_review_required` | none | Batch011 対象。Mermaid 公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-141` | PlantUML | required | `official_logo_source_review_required` | none | Batch011 対象。PlantUML 公式素材と利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-150` | MIT ライセンス | not_needed | `logo_avoid` | none | Batch011 対象。一般的な許諾条件の図解で表現する |
| `F-151` | Apache 2.0 | not_needed | `logo_avoid` | none | Batch011 対象。ライセンス条項の図解で表現し、Apache マークは使わない |
| `F-152` | GPL | not_needed | `logo_avoid` | none | Batch011 対象。コピーレフトの図解で表現し、GNU/FSF マークは使わない |
| `F-153` | Creative Commons | required | `official_logo_source_review_required` | none | Batch011 対象。CC 公式アイコンと利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-154` | OSS | not_needed | `logo_avoid` | none | Batch011 対象。オープンソース協働の概念図。財団ロゴ不要 |
| `F-160` | DOM | not_needed | `logo_avoid` | none | Batch011 対象。文書ツリーの概念図。ブラウザ/フレームワークロゴ不要 |
| `F-161` | SSR | not_needed | `logo_avoid` | none | Batch011 対象。サーバーからブラウザへの描画フロー。フレームワークロゴ不要 |
| `F-162` | SSG | not_needed | `logo_avoid` | none | Batch011 対象。ビルド時の静的ページ生成フロー。フレームワークロゴ不要 |
| `F-170` | EC2 | required | `official_logo_source_review_required` | none | Batch011 対象。AWS EC2 公式アイコンと利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-171` | S3 | required | `official_logo_applied` | `assets/logos/aws/aws-architecture-icons-2026-01-30/Architecture-Service-Icons_01302026/Arch_Storage/64/Arch_Amazon-Simple-Storage-Service_64.svg` | 現行finalに公式Amazon S3 service iconを適用済み（一般AWSロゴではない）。AWS Architecture Icons package由来、取得2026-06-03。個別利用条件は未確認。新候補はロゴなし`internal_base_only`。
| `F-172` | IAM | required | `official_logo_available` | `assets/logos/aws/aws-architecture-icons-2026-01-30/Architecture-Service-Icons_01302026/Arch_Security-Identity/64/Arch_AWS-Identity-and-Access-Management_64.svg` | 公式AWS IAMアイコンをローカル保存済み（brand_usage_audit.mdに出典・2026-06-03取得を記録）。個別の利用条件は未確認。internal_base_onlyを上限とし、AI生成ロゴは禁止.
| `F-180` | OpenGL | required | `official_logo_source_review_required` | none | Batch011 対象。OpenGL 公式ロゴと利用条件を確認するまで、AI 生成ロゴは禁止してベースだけ作る |
| `F-181` | WebGL | required | `official_logo_applied_unreviewed` | `assets/logos/khronos/WebGL-Logo.svg` | Official Khronos WebGL resources asset, retrieved 2026-06-03; SHA-256 `9F63C2323B417EA77138AFDB49139D2C6D6C66CFB23C49221466298E68BAB87B`. Current final SHA-256 `ac687f43d8d8e00c0b8f2a4a1a88ea2910e54943a1074488bda9b55893918423` contains the mark; legacy generation record is `official_logo_applied` / `overlay_audit` / `not_reviewed`. Separate logo-free base is `assets/ponchi/experiments/batches/ponchi-batch-011/F-181_base_1254x627.png` (SHA-256 `d8d2adc28b830e5bdc761836357321e205a101d2e6ed916be217572d41c526fc`). On that base, `[686,0,520,180]` has 128 nonwhite pixels; hold sidecar/generation until cleared and independently re-audited. Use conditions remain unverified. |
| `F-190` | サブルーチン | not_needed | `logo_avoid` | none | Batch011 対象。関数呼び出しと再利用の概念図。言語ロゴ不要 |
| `F-200` | Rust | required | `official_logo_available` | `assets/logos/rust/rust-logo.svg` | 公式 `rust-lang/rust-artwork` 由来。2026-06-03 取得、SHA256 `9a9549ea02d34dec3a610b8299f1b8121c7b10b14a44d3baec46ba15e9a06ca2`。個別用途の適合・利用条件・許諾は未確認のため、確認までは合成しない |
| `F-210` | JSON Schema | not_needed | `logo_avoid` | none | 標準的なJSONデータ構造の検証概念。特定製品ではなく、必須キー/型/許容値の汎用スキーマと検証ゲートで示す |
| `F-212` | OpenAPI | not_needed | `logo_avoid` | none | OpenAPI Specification の説明図。OpenAPI Initiative の組織ロゴとは区別し、汎用の仕様書/出力図で表す。公式style guideはSpecificationとInitiativeは別物と明記: https://www.openapis.org/style-guide 。InitiativeロゴをSpecificationの製品ロゴとして流用しない |
| `G-1` | Context | not_needed | `logo_avoid` | none | 概念図。ロゴ不要 |
| `G-2` | Token | not_needed | `logo_avoid` | none | Batch012 対象。トークン化の概念図。AI 企業ロゴ不要 |
| `G-3` | Dictation | not_needed | `logo_avoid` | none | Batch012 対象。音声入力から文字化の概念図。アプリロゴ不要 |
| `G-4` | System Prompt | not_needed | `logo_avoid` | none | Batch012 対象。指示階層の概念図。モデル/プロバイダロゴ不要 |
| `G-5` | Context Window | not_needed | `logo_avoid` | none | Batch012 対象。文脈容量の概念図。モデル/プロバイダロゴ不要 |
| `G-6` | One-shot | not_needed | `logo_avoid` | none | Batch012 対象。1例からの学習/誘導の概念図。モデル/プロバイダロゴ不要 |
| `G-7` | 指示追従性 | not_needed | `logo_avoid` | none | Batch012 対象。指示と出力の照合図。モデル/プロバイダロゴ不要 |
| `G-8` | 決定論的／非決定論的 | not_needed | `logo_avoid` | none | Batch012 対象。同じ入力からの安定/ゆらぎ比較。モデル/プロバイダロゴ不要 |
| `G-9` | effort レベル | not_needed | `logo_avoid` | none | Batch012 対象。推論労力の調整図。モデル/プロバイダロゴ不要 |
| `G-10` | Prompt Engineering | not_needed | `logo_avoid` | none | Batch012 対象。プロンプト改善の概念図。モデル/プロバイダロゴ不要 |
| `G-11` | Context Engineering | not_needed | `logo_avoid` | none | Batch012 対象。文脈組み立ての概念図。モデル/プロバイダロゴ不要 |
| `G-12` | Agent Design | not_needed | `logo_avoid` | none | Batch012 対象。エージェント設計の概念図。モデル/プロバイダロゴ不要 |
| `G-13` | Few-shot Learning | not_needed | `logo_avoid` | none | Batch012 対象。複数例による誘導の概念図。モデル/プロバイダロゴ不要 |
| `G-14` | Thinking モデル | not_needed | `logo_avoid` | none | Batch012 対象。内部作業領域の概念図。モデル/プロバイダロゴ不要 |
| `G-15` | RAG | not_needed | `logo_avoid` | none | Batch012 対象。検索拡張生成の概念図。モデル/プロバイダロゴ不要 |
| `G-16` | Embedding | not_needed | `logo_avoid` | none | Batch012 対象。ベクトル化の概念図。モデル/プロバイダロゴ不要 |
| `G-17` | ベクトル DB | not_needed | `logo_avoid` | none | Batch012 対象。ベクトル検索の概念図。DB/製品ロゴ不要 |
| `G-18` | Chain of Thought | not_needed | `logo_avoid` | none | Batch012 対象。段階的推論の概念図。モデル/プロバイダロゴ不要 |
| `G-19` | Prompt Caching | not_needed | `logo_avoid` | none | Batch012 対象。再利用される文脈キャッシュの概念図。モデル/プロバイダロゴ不要 |
| `G-20` | CLAUDE.md | not_needed | `logo_avoid` | none | Batch012 対象。エージェント指示ファイルの汎用図解。Claude/Anthropic ロゴ不要 |
| `G-21` | AGENTS.md | not_needed | `logo_avoid` | none | Batch012 対象。複数エージェント指示ファイルの汎用図解。製品ロゴ不要 |
| `G-23` | .claude/settings.json | required | `official_logo_source_review_required` | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/2 Claude Code logo/PNG/Claude Code logo - Slate.png` | Claude Code固有の設定ファイルを扱う。local official Claude Code mark SHA-256 `80DD500873626ABB6A71B5CA6722060FFA3CFB03005B6F5FC967EC7D7A1A9C39` は存在するが、この設定ファイル概念へのmark適合性・用途条件は未確認。legacy batch-013の `not_needed / logo_avoid` を本マトリクス方針に沿って再評価。選定と合成はレビュー完了まで行わず、AI生成ロゴや実UI模倣もしない |
| `G-30` | Tool Use | not_needed | `logo_avoid` | none | ユーザー→LLM→tool host実行→LLM→回答の一般フロー。特定製品UIや会社・製品ロゴは不要 |
| `G-33` | Function Calling | not_needed | `logo_avoid` | none | 複数製品に共通する function calling の概念図。質問→構造化呼び出し→host 実行→結果返却を汎用図形で示し、特定社・製品のロゴは使わない |
| `G-34` | Code Interpreter | not_needed | `logo_avoid` | none | 複数providerに共通するCSV→Python sandbox実行→結果/グラフの概念図。ChatGPT/Claude/Geminiの公式マークや実製品UIは使わず、汎用パネルで示す |
| `G-35` | Deep Research | not_needed | `logo_avoid` | none | ChatGPT/Gemini/Perplexityに共通する反復検索・出典確認・レポート化の概念。3つの利用場面がbriefにあっても特定1社の公式マークは不要。現行finalは汎用ループ。 |
| `G-36` | Artifact | required | `official_logo_source_review_required` | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/1 Claude logo/PNG/Claude logo - Slate.png` | Claude.ai固有のArtifact機能。旧generation ledgerは `not_needed / logo_avoid`。機能がClaude.aiに固有であるため本マトリクス方針に沿って要件を更新し、旧判定を履歴として明示した。公式Claude markはローカルにある（SHA-256 `F95E9DD722B51B10312B1E62E139389293C8A31CD6101A694290BF767765F85B`、2026-06-03取得をbrand auditに記録）。Artifact機能図でのmark適合性・個別利用条件・配置をレビューするまでは合成しない。候補ベースは汎用の会話→編集可能な成果物パネルに限定し、Claude.aiの実UIを模倣しない。 |
| `G-39` | Permission | not_needed | `logo_avoid` | none | ツール許可の一般概念図。設定ファイル名や製品UI、会社・製品ロゴは使わない |
| `G-40` | バイブコーディング | not_needed | `logo_avoid` | none | 人・AI・コードの一般的な反復フロー。本文中のCursor/Claude Codeは例示にとどめ、特定製品のUIやロゴは使わない |
| `G-43` | オーケストレーション | not_needed | `logo_avoid` | none | 司令塔と専門エージェントの一般的な役割分担図。特定のエージェント製品UIや公式アイコンは使わない |
| `G-44` | マルチエージェント協調 | not_needed | `logo_avoid` | none | Planner/Executor/Reviewer の役割分担を示す一般的な協調フロー。特定製品UIや公式アイコンは使わない |
| `G-47` | Auto-compact | not_needed | `logo_avoid` | none | 会話→要約→継続の一般処理図。Claude Codeのロゴ、Anthropic mark、実在product UIは描かない。ブリーフにブランドロゴ指定なし。
| `G-48` | Structured Outputs | not_needed | `logo_avoid` | none | Claude/ChatGPTなど複数providerにまたがる構造化出力概念。実装差を保ち、特定providerの公式markや実製品UIは使わない |
| `H-3` | バイブコーディングの流儀 | not_needed | `logo_avoid` | none | 依頼・確認・記録・修正の一般的な循環。会社・製品・モデルのロゴは使わない |
| `H-6` | Git Flow | not_needed | `logo_avoid` | none | Git のブランチ運用モデル。会社・製品名ではない。汎用ブランチ図形を使い、GitHub ロゴは使わない |
| `H-8` | DevOps | not_needed | `logo_avoid` | none | 開発・運用の一般的な循環。会社・製品名ではなく、汎用工程図形を使う |
| `H-57` | Gemini の命名史 | required | `official_logo_available` | `assets/logos/gemini/gemini_sparkle_4g_512_lt.png` | 公式Gemini site由来・取得2026-06-03（`brand_usage_audit.md`のH-57追加記録）。世代タイムライン用の個別使用条件は未確認。合成せずロゴなし内部ベースに限定。
| `H-58` | Transformer 論文 | not_needed | `logo_avoid` | none | 2017 年の研究論文と技術史の項目。会社・製品・モデル名ではなく、ChatGPT 等は汎用UIとして示し、公式ロゴを使わない |
| `I-1` | MCP | not_needed | `logo_avoid` | none | LLM・client・server・外部サービスを結ぶ共通プロトコルの概念図。特定の製品実装を描かず汎用図形を使う |
| `I-3` | MCP Client | not_needed | `logo_avoid` | none | MCP クライアント・サーバーのプロトコル構造を示す概念図。特定のクライアント製品は含めず、汎用図形を使う |
| `I-5` | MCP SDK | not_needed | `logo_avoid` | none | SDK の登録要素と MCP 通信を示すプロトコル概念図。特定の SDK 製品は扱わない |
| `I-22` | Chrome DevTools MCP | required | `official_logo_source_review_required` | none | Chrome/DevToolsを題名に含む項目。適用すべき公式表現と利用条件を確認するまでロゴを描画・合成しない。内部候補も汎用ブラウザ表現に限る |
| `I-41` | SQLite MCP | required | `official_logo_source_review_required` | `assets/logos/sqlite/sqlite370_banner.svg` | SQLite公式素材はローカルにあるが、このMCPサーバー項目への適合と用途条件は未確認。解決まではベースのみ・公式素材は合成しない |
| `I-50` | AWS MCP | required | `official_logo_source_review_required` | none | AWS のサービス名を含む項目。適用すべき公式 AWS 表現・素材と個別利用条件を確認するまでロゴ合成しない。AWS Architecture Icons を一般ロゴの代用にせず、AI 生成マークも使わない |
| `I-80` | 自作 MCP のテンプレ | not_needed | `logo_avoid` | none | MCPサーバー/Tools・Resources・Promptsとstdio/HTTPの一般構造。公式ブランドアイコンや製品UIは不要 |
| `J-1` | AGI | not_needed | `logo_avoid` | none | 特化型AIと仮説上のAGIの一般比較。会社・製品ロゴや現実の達成を示すブランド表示は不要。
| `J-2` | 強い AI／弱い AI | not_needed | `logo_avoid` | none | AI能力の一般概念と仮説の比較。会社・製品・モデルのロゴは使わない |
| `J-4` | ASI | not_needed | `logo_avoid` | none | 現在AIからAGI/仮説上のASIへ進む一般概念図。会社・製品ロゴは不要。
| `J-10` | Machine Learning | not_needed | `logo_avoid` | none | 機械学習の一般的な階層・分類図。会社・製品・モデルのロゴは使わない |
| `J-11` | Deep Learning | not_needed | `logo_avoid` | none | 深層学習の一般概念図。会社・製品・モデルのロゴは使わない |
| `J-12` | Neural Network | not_needed | `logo_avoid` | none | 一般的なニューラルネットワークの概念図。会社・製品・モデル名ではなく、ブランド素材は不要 |
| `J-13` | Transformer | not_needed | `logo_avoid` | none | Transformer アーキテクチャの一般概念図。Encoder・Attention・Decoder の構造を汎用図形で示し、会社・製品・モデルのロゴは使わない |
| `J-14` | LLM | not_needed | `logo_avoid` | none | 概念図。ロゴ不要 |
| `J-15` | VLM | not_needed | `logo_avoid` | none | 画像入力から視覚エンコーダー・LLM・回答へ進む一般概念。会社・製品・モデルロゴは不要 |
| `J-16` | Fine-tuning | not_needed | `logo_avoid` | none | PromptとFine-tuningの一般比較。会社・製品・モデルのロゴは使わない |
| `J-17` | Attention | not_needed | `logo_avoid` | none | Attention/Q-K-Vの一般的な学習図。会社・製品・モデルロゴは不要。
| `J-21` | LoRA | not_needed | `logo_avoid` | none | Full Fine-tuningとLoRAの一般比較。会社・製品・モデルロゴは不要。
| `J-22` | パラメータ数の単位 | not_needed | `logo_avoid` | none | M/B/Tの単位と桁を示す一般概念図。会社・製品・モデルのロゴは使わない |
| `J-33` | 量子コンピュータ | not_needed | `logo_avoid` | none | 重ね合わせと量子もつれの一般概念図。会社・製品ロゴは不要 |
| `J-41` | DX | not_needed | `logo_avoid` | none | 業務変革と業務の単純な IT 化を比べる一般概念図。特定企業・製品の識別を目的にせず、汎用図形だけを使う |
| `J-43` | SaaS | not_needed | `logo_avoid` | none | インストール型とブラウザSaaS型の一般比較。特定プロバイダのUIや製品ロゴは使わない |
| `J-53` | 著作権法 30 条の 4（日本） | not_needed | `logo_avoid` | none | 日本法の適用範囲と条件を説明する一般図。省庁・会社・製品ロゴは使わない |
| `J-62` | チューリングテスト | not_needed | `logo_avoid` | none | 人間と機械の応答を審査員が比較する一般概念。会社・製品ロゴは不要。
| `J-70` | VRAM | not_needed | `logo_avoid` | none | CPU/GPU の記憶領域を比べる一般概念。GPU/VRAM のメーカー名や製品系列は扱わない |
| `J-71` | RAM | not_needed | `logo_avoid` | none | RAM/VRAM/SSD の一般的な記憶階層。メーカーや製品系列の識別は目的にしない |
| `J-81` | M.2 | not_needed | `logo_avoid` | none | M.2 の形状と接続規格を示す一般概念図。特定メーカー製品は扱わない |
| `J-90` | GUI | not_needed | `logo_avoid` | none | Graphical User Interface の一般概念。汎用画面と人物/エージェントだけで表す |
| `J-100` | 識字（リテラシー） | not_needed | `logo_avoid` | none | 識字能力の段階的な広がりを示す一般概念。会社・製品ロゴは不要 |

## ローカル公式素材あり

以下はこの台帳の対象項目に関連する公式素材のローカル記録であり、公式ソースの確認だけで個別用途の公開・商用利用許諾が確認されたことを意味しない。用途条件が未確認なら合成しない。

| brand | asset | entries |
| :-- | :-- | :-- |
| GitHub Copilot | `assets/logos/github/GitHub_Logos/GitHub Logos/PNG/GitHub_Copilot_Lockup_Black_Clearspace.png` | `B-5` |
| GitHub | `assets/logos/github/GitHub_Logos/GitHub Logos/PNG/GitHub_Lockup_Black_Clearspace.png` | `F-60` |
| Claude | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/1 Claude logo/PNG/Claude logo - Slate.png` | `B-2` |
| Claude Code | `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/2 Claude Code logo/PNG/Claude Code logo - Slate.png` | `B-7` |
| Cursor | `assets/logos/cursor/cursor-brand-assets/General Logos/Lockup Horizontal/PNG/LOCKUP_HORIZONTAL_2D_LIGHT.png` | `B-4`, `D-35` |
| v0 | `assets/logos/vercel/v0-assets/v0/Light/v0-logo-light.png` | `B-9` |
| Vercel | `assets/logos/vercel/vercel-assets/Vercel/logotype/light/vercel-logotype-light.png` | `B-20` |
| Netlify | `assets/logos/netlify/netlify-logo-full/netlify-logo-full/large/lightmode/logo-netlify-large-monochrome-lightmode.png` | `B-21` |
| Cloudflare | `assets/logos/cloudflare/Cloudflare_logo_kit/Cloudflare_logo_kit/Cloudflare_logo_kit/Cloudflare logo/png/CF_logo_horizontal_singlecolor_blk.png` | `B-22` |
| Render | `assets/logos/render/render-wordmark-from-press.png` | `B-28` |
| Supabase | `assets/logos/supabase/brand-assets/supabase-logo-wordmark--light.png` | `B-29` |
| Vertex AI | `assets/logos/google-cloud/product-icons/core-products-icons/Unique Icons/Vertex AI/SVG/VertexAI-512-color.svg` | `B-27` |
| Amazon Bedrock | `assets/logos/aws/aws-architecture-icons-2026-01-30/Architecture-Service-Icons_01302026/Arch_Artificial-Intelligence/64/Arch_Amazon-Bedrock_64.svg` | `B-30` |
| にゃんた YouTube avatar | `assets/logos/nyanta/youtube-channel-avatar.jpg` | `C-81` |
| まさお YouTube avatar | `assets/logos/masao/youtube-channel-avatar.jpg` | `C-82` |
| OpenAI wordmark | `assets/logos/openai/openai_wordmark_black_official_template_layer.png` | `D-71` |
| Ghostty social-share card | `assets/logos/ghostty/social-share-card.jpg` | `F-84` |
| SQLite banner | `assets/logos/sqlite/sqlite370_banner.svg` | `F-121`; `I-41` usage review required |
| Gemini sparkle | `assets/logos/gemini/gemini_sparkle_4g_512_lt.png` | `B-52`; official source checked, retrieved 2026-06-03; SHA256 `5e7cfecaa53f4f65a313fe89b0f389548126544a78fad8489510c70ae641a4a1`; item-specific use conditions pending |
| VS Code Japanese Language Pack | `assets/logos/vscode-language-pack-ja/languagepack.png` | `F-37`; official Microsoft vscode-loc source, retrieved 2026-06-03; SHA256 `00446b52fa5fe7550f8618f5fe8a8dbba6d1b241fecb01490dc9ac4c90da04ac`; item-specific use conditions pending |
| Rust | `assets/logos/rust/rust-logo.svg` | `F-200`; official rust-lang/rust-artwork source, retrieved 2026-06-03; SHA256 `9a9549ea02d34dec3a610b8299f1b8121b10b14a44d3baec46ba15e9a06ca2`; item-specific use conditions pending |

AWS Architecture Icons はローカルにあるが、B-23 にそのまま使うブランド lockup とは別扱いにする。B-23 は公式ロゴ/利用条件を確認するまで `official_logo_source_review_required` のまま止める。Ruby の素材は今回の対象には直接該当しない。

## 次の処理

1. この台帳を先にコミットする。
2. `official_logo_applied` は目視と寸法監査だけ行い、追加のロゴ生成はしない。
3. `official_logo_source_available_needs_import` は、公式素材の取得、`docs/brand_usage_audit.md` への記録、ローカル PNG/SVG 参照化、合成監査の順に進める。
4. `official_logo_source_review_required` は、具体ロゴ・取得経路・許諾条件を確認するまで本番ロゴ合成と本番差し替えを進めない。
5. `base_2to1_ready_logo_blocked` は、公式素材の取得・利用条件確認ができるまで、本番ロゴ合成と本番差し替えを進めない。
6. `logo_avoid` は、汎用図解として本番候補を進めてよい。

## 適用監査

`official_logo_applied` の確認結果は `docs/ponchi_logo_application_audit_2026-06-01.md` に記録する。

## 2:1 ベース再生成

ブランド系の元絵 2:1 ベース再生成結果は `docs/ponchi_brand_base_regeneration_2026-06-01.md` に記録する。
