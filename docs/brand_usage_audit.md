# Brand usage audit for ponchi regeneration

This audit records only confirmed sources that can be used for deterministic
brand asset overlays. It is not permission advice; it is a working ledger for
avoiding AI-generated fake logos, icons, marks, mascots, and brand-style
substitutes.

## GitHub / GitHub Copilot

- Source checked: `https://brand.github.com/foundations/logo`
- Official asset package: `https://brand.github.com/GitHub_Logos.zip`
- Local path: `assets/logos/github/GitHub_Logos/`
- Relevant local assets:
  - `GitHub Logos/SVG/GitHub_Invertocat_Black.svg`
  - `GitHub Logos/SVG/GitHub_Lockup_Black.svg`
  - `GitHub Logos/SVG/GitHub_Copilot_Lockup_Black.svg`
  - `GitHub Logos/PNG/Copilot_Icon_Black_Clearspace.png`
- Working rule:
  - Use unchanged official files only.
  - Prefer black marks on white backgrounds for this book's image palette.
  - Do not modify the mark shape or recolor it.
  - Do not imply GitHub sponsorship or endorsement.

## OpenAI / ChatGPT / Codex

- Source checked: `https://openai.com/brand/`
- Source status: official brand guidance confirmed. The page identifies the
  OpenAI name/logo plus ChatGPT and GPT brands as OpenAI trademarks, describes
  wordmark and Blossom usage, and exposes logo downloads subject to OpenAI marks
  terms.
- Official asset package checked: `https://cdn.openai.com/brand/OpenAI-Partnership-Templates-2025.zip`
- Local package: `assets/logos/openai/OpenAI-Partnership-Templates-2025.zip`
- Local extracted source:
  - `assets/logos/openai/OpenAI-Partnership-Templates-2025/02.03_Brand Partnerships_Templates/Brand Partnerships_Template_Horizontal.psb`
- Relevant local asset:
  - `assets/logos/openai/openai_wordmark_black_official_template_layer.png`
- Local status: OpenAI wordmark layer imported from the official partnership
  template. ChatGPT-specific and Codex-specific lockups are still not imported.
- Working rule:
  - Do not generate OpenAI, ChatGPT, or Codex logos, marks, icons, or product UI
    from prompts.
  - Use the OpenAI wordmark only where OpenAI brand identification is acceptable.
  - B-3 ChatGPT, B-8 Codex, and B-51 ChatGPT の料金プラン use the official OpenAI
    wordmark as an OpenAI-brand overlay. Dedicated ChatGPT/Codex lockups remain
    unimported, so these candidates stay review-pending before final promotion.
  - Current chapter trials using this asset:
    - `C-1_openai_chapter_trial_v3_official_openai_logo_480w_1254x627.png`
    - `H-53_chatgpt-launch_chapter_trial_v3_official_openai_logo_480w_1254x627.png`

## Anthropic / Claude

- Source checked: `https://www.anthropic.com/news`
- Official asset package checked: `https://anthropic.com/press-kit`
- Local package: `assets/logos/anthropic/anthropic-media-resources.zip`
- Local extracted source:
  - `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/`
- Relevant local assets:
  - `Claude logos/1 Claude logo/PNG/Claude logo - Slate.png`
  - `Claude logos/2 Claude Code logo/PNG/Claude Code logo - Slate.png`
- Local status: Claude and Claude Code official logo assets imported.
- Working rule:
  - Do not generate Claude or Anthropic marks, icons, or brand-style substitutes
    from prompts.
  - Use the official Claude logo for B-2 and the official Claude Code logo for
    B-7.
  - Treat D-12 as a Claude-family logo item only after deciding whether the
    Claude logo or a model-family-specific treatment is appropriate.

## Google / Gemini

- Source checked: `https://about.google/brand-resource-center/`
- Source status: official Google Brand Resource Center exists and redirects to
  Partner Marketing Hub. Gemini still needs a concrete official product
  icon/lockup selection and any required permission review before use.
- Local status: no local Gemini asset imported yet.
- Working rule:
  - Do not generate Gemini, Google, Android, Gmail, Docs, or Google Cloud marks,
    icons, logos, app UI, or brand-color substitutes from prompts.
  - Keep B-1 in `official_logo_source_review_required` until the exact Gemini
    asset and usage conditions are recorded.

## Cursor / Windsurf

- Cursor source checked: `https://cursor.com/brand`
- Cursor source status: official brand guidelines confirm downloadable brand
  assets, including logos, app icons, avatars, and a preferred horizontal lockup.
- Cursor official asset package checked:
  `https://ptht05hbb1ssoooe.public.blob.vercel-storage.com/assets/brand/cursor-brand-assets.zip`
- Cursor local package: `assets/logos/cursor/cursor-brand-assets.zip`
- Cursor local extracted source: `assets/logos/cursor/cursor-brand-assets/`
- Relevant local asset:
  - `General Logos/Lockup Horizontal/PNG/LOCKUP_HORIZONTAL_2D_LIGHT.png`
- Windsurf source checked: `https://windsurf.com/brand`
- Windsurf source status: official brand guidelines confirm wordmark and symbol
  assets and state the Windsurf wordmark should be used in references to
  Windsurf as space allows.
- Windsurf local source page: `assets/logos/windsurf/windsurf-brand.html`
- Windsurf official assets saved:
  - `assets/logos/windsurf/windsurf-black-wordmark.svg`
  - `assets/logos/windsurf/windsurf-black-wordmark.png`
  - `assets/logos/windsurf/windsurf-black-symbol.svg`
  - `assets/logos/windsurf/windsurf-black-symbol.png`
- B-6 overlay: `assets/ponchi/experiments/batches/ponchi-batch-001/B-6_overlay_1254x627.png`
- B-6 overlay metadata: `assets/ponchi/experiments/batches/ponchi-batch-001/B-6_overlay_1254x627.meta.json`
- B-6 decision: official black Windsurf wordmark applied as a
  review-pending deterministic overlay. The generated body was palette
  normalized; the overlay remains visual-review required because the base
  density warning was accepted only as `warn-only` for this spacious logo
  composition.
- Working rule:
  - Do not generate Cursor or Windsurf marks, icons, logos, or product UI from
    prompts.
  - Use the official Cursor horizontal lockup for B-4.
  - Use the official Windsurf black wordmark for B-6; do not recolor, outline,
    rotate, stretch, shadow, or otherwise modify it.

## Vercel / v0

- Source checked: `https://vercel.com/design/brands`
- v0 product docs checked: `https://vercel.com/docs/v0`
- Source status: Vercel publishes brand guidelines and identifies the v0 name
  and logo as Vercel trademarks. The v0 docs confirm v0 as a Vercel product.
- Official v0 asset package checked:
  `https://k2mkucxia43oc7fa.public.blob.vercel-storage.com/front/press/v0-assets.zip`
- Official Vercel asset package checked:
  `https://assets.vercel.com/image/upload/v1662130559/front/press/vercel-assets.zip`
- Local packages:
  - `assets/logos/vercel/v0-assets.zip`
  - `assets/logos/vercel/vercel-assets.zip`
- Local extracted sources:
  - `assets/logos/vercel/v0-assets/v0/`
  - `assets/logos/vercel/vercel-assets/Vercel/`
- Relevant local asset:
  - `Light/v0-logo-light.png`
  - `logotype/light/vercel-logotype-light.png`
- Local status: v0 and Vercel official logo assets imported.
- Working rule:
  - Do not generate v0 or Vercel marks, icons, logos, product UI, or brand-color
    substitutes from prompts.
  - Use the official v0 light logo for B-9 on white logo clearspace.
  - Use the official Vercel light logotype for B-20 on white logo clearspace.

## StackBlitz / Bolt.new

- Source checked: `https://stackblitz.com/github/stackblitz/bolt.new`
- Official repository asset checked:
  `https://github.com/stackblitz/bolt.new/blob/main/icons/logo-text.svg`
- Local assets:
  - `assets/logos/bolt/bolt-logo-text-official.svg`
  - `assets/logos/bolt/bolt-logo-text-official-512.png`
  - `assets/logos/bolt/bolt-public-logo-official.svg`
- Local status: official Bolt wordmark asset imported from the official
  StackBlitz `bolt.new` repository and applied to B-11. A distinct `.new`
  suffix lockup was not used.
- Working rule:
  - Do not generate Bolt.new marks, icons, logos, product UI, or brand-color
    substitutes from prompts.
  - Use the official Bolt wordmark from the StackBlitz `bolt.new` repository
    on white logo clearspace.
  - Do not synthesize a `.new` wordmark suffix.

## Perplexity

- Source checked: `https://www.perplexity.ai/hub/about`
- Official brand guidelines checked: `https://live.standards.site/perplexity`
- Official asset checked:
  `https://firebasestorage.googleapis.com/v0/b/standards-site-beta.appspot.com/o/documents%2F6t12iheczyb%2F732776432bb%2FPerplexity-Primary-Lockup-Offblack.svg?alt=media&token=d99f057b-1d7e-46b5-92d7-545a258ff0f5`
- Local assets:
  - `assets/logos/perplexity/Perplexity-Primary-Lockup-Offblack.svg`
  - `assets/logos/perplexity/Perplexity-Primary-Lockup-Offblack-512.png`
- Local status: Perplexity official primary offblack lockup imported and
  applied to B-12.
- Working rule:
  - Do not generate Perplexity marks, icons, logos, product UI, or brand-color
    substitutes from prompts.
  - Use the official offblack primary lockup for B-12 on white logo clearspace.

## Netlify

- Source checked: `https://www.netlify.com/press/`
- Official asset package checked:
  `https://www.netlify.com/assets/logos/netlify-logo-full.zip`
- Local package: `assets/logos/netlify/netlify-logo-full.zip`
- Local extracted source:
  - `assets/logos/netlify/netlify-logo-full/netlify-logo-full/`
- Relevant local asset:
  - `large/lightmode/logo-netlify-large-monochrome-lightmode.png`
- Local status: Netlify official full logo asset imported.
- Working rule:
  - Do not generate Netlify marks, icons, logos, product UI, or brand-color
    substitutes from prompts.
  - Use the official monochrome lightmode logo for B-21 on white logo
    clearspace.

## Cloudflare

- Source checked: `https://www.cloudflare.com/logo/`
- Official asset package checked:
  `https://cf-assets.www.cloudflare.com/slt3lc6tev37/7c5EBeF7oxPPYzZiDkSEMM/b8c81838b468bf520767aa47347ac8f3/Cloudflare_logo_kit.zip`
- Local package: `assets/logos/cloudflare/Cloudflare_logo_kit.zip`
- Local extracted source:
  - `assets/logos/cloudflare/Cloudflare_logo_kit/Cloudflare_logo_kit/Cloudflare_logo_kit/Cloudflare logo/`
- Relevant local asset:
  - `png/CF_logo_horizontal_singlecolor_blk.png`
- Local status: Cloudflare official logo assets imported.
- Working rule:
  - Do not generate Cloudflare marks, icons, logos, product UI, or brand-color
    substitutes from prompts.
  - Use the official single-color black horizontal logo for B-22 on white logo
    clearspace.

## Render

- Source checked: `https://render.com/press`
- Official logo source checked:
  `https://render.com/brand/render_1105076560.svg`
- Local source:
  - `assets/logos/render/render_1105076560.svg`
  - `assets/logos/render/render-wordmark-from-press.svg`
- Relevant local asset:
  - `assets/logos/render/render-wordmark-from-press.png`
- Local status: Render official wordmark imported from the official press page
  header SVG, with black fill applied for white clearspace compositing.
- Working rule:
  - Do not generate Render marks, icons, logos, product UI, or brand-color
    substitutes from prompts.
  - Use the official Render wordmark for B-28 on white logo clearspace.

## Supabase

- Source checked: `https://supabase.com/brand-assets`
- Official asset package checked:
  `https://supabase.com/brand-assets.zip`
- Local package: `assets/logos/supabase/brand-assets.zip`
- Local extracted source:
  - `assets/logos/supabase/brand-assets/`
- Relevant local asset:
  - `supabase-logo-wordmark--light.png`
- Local status: Supabase official logo assets imported.
- Working rule:
  - Do not generate Supabase marks, icons, logos, product UI, or brand-color
    substitutes from prompts.
  - Use the official Supabase light wordmark for B-29 on white logo
    clearspace.

## ElevenLabs

- Source checked: `https://elevenlabs.io/press`
- Official logo assets checked:
  - `ElevenLabs Logo black (SVG)`
  - `Download all`
- Local assets:
  - `assets/logos/elevenlabs/elevenlabs-logo-black.svg`
  - `assets/logos/elevenlabs/elevenlabs-logos.zip`
- Local status: ElevenLabs official black SVG imported from the official press
  page and applied to B-13.
- Working rule:
  - Do not generate ElevenLabs marks, icons, logos, product UI, or brand-color
    substitutes from prompts.
  - Use the official black SVG for B-13 on white logo clearspace.

## Genspark

- Source checked: `https://www.genspark.ai/brand`
- Source status: official brand guidelines confirmed. The page documents logo
  variants, light/dark usage, co-branding rules, and official downloads in
  Figma, Adobe Illustrator, and PDF formats.
- Local status: official source is confirmed, but the full lockup asset import
  remains incomplete because direct local download is blocked by the site's
  Cloudflare/403 response in the shell environment. The official site favicon
  was accessible at `https://www.genspark.ai/favicon.ico`.
- Working rule:
  - Do not generate Genspark marks, icons, logos, product UI, or brand-color
    substitutes from prompts.
  - Use the official favicon for B-14 as a review-pending overlay while the
    full official lockup remains unavailable from this environment.

## Canva

- Source checked: `https://www.canva.dev/docs/connect/guidelines/brand/`
- Official asset package checked:
  `https://www.canva.dev/assets/connect/Canva-logos.zip`
- Local package: `assets/logos/canva/Canva-logos.zip`
- Local extracted source: `assets/logos/canva/Canva-logos/Canva logos/`
- Relevant local asset:
  - `png/512x512/Canva type logo_512x180.png`
- Local status: Canva official logo package imported from Canva developer brand
  guidelines and ZIP metadata files removed from the extracted folder.
- Working rule:
  - Do not generate Canva marks, icons, logos, product UI, or brand-color
    substitutes from prompts.
  - Use the official Canva type logo for B-33 on white logo clearspace.

## Stability AI / Stable Diffusion

- Source checked: `https://stability.ai/`
- Official asset checked:
  `https://images.squarespace-cdn.com/content/v1/6213c340453c3f502425776e/a3485d53-7e65-42b5-bc62-e2e55f8409b9/stability-ai-white-dot-desktop.png`
- Local source page: `assets/logos/stability-ai/stability-ai-homepage.html`
- Relevant local assets:
  - `assets/logos/stability-ai/stability-ai-white-dot-desktop.png`
  - `assets/logos/stability-ai/stability-ai-white-dot-on-approved-blue-plate.png`
- Local status: official Stability AI header logo imported from the official
  site. A dedicated Stable Diffusion product logo was not confirmed in this
  pass.
- Working rule:
  - Do not generate Stability AI or Stable Diffusion marks, icons, logos,
    product UI, or brand-color substitutes from prompts.
  - Use the official white Stability AI organization logo on an approved
    `#123E82` plate for D-54 as a review-pending organization overlay, not as a
    dedicated Stable Diffusion product logo.

## Google Flow

- Source checked: `https://labs.google/fx/tools/flow`
- Canonical source checked: `https://flow.google/` redirects to the Google Labs
  Flow page.
- Official assets checked:
  - `https://labs.google/fx/icons/favicon/flow_favicon_b.png`
  - `https://labs.google/fx/icons/favicon/flow_favicon_w.png`
- Local source page: `assets/logos/google-flow/flow-google-page.html`
- Relevant local assets:
  - `assets/logos/google-flow/flow_favicon_b.png`
  - `assets/logos/google-flow/flow_favicon_w.png`
  - `assets/logos/google-flow/flow_favicon_w_on-approved-blue-plate.png`
- Local status: official Flow favicon assets imported from the official Google
  Labs Flow page. A standalone Flow lockup was not confirmed in this pass.
- Working rule:
  - Do not generate Flow, Google, Veo, Imagen, Gemini, or Google Labs marks,
    product UI, or brand-color substitutes from prompts.
  - Use the official white Flow favicon on an approved `#123E82` plate for D-57
    as a review-pending official icon overlay, not as a standalone product
    lockup.

## Google Whisk

- Source checked: `https://labs.google/fx/tools/whisk`
- Official assets checked:
  - `https://labs.google/fx/icons/favicon/whisk_favicon_b.svg`
  - `https://labs.google/fx/icons/favicon/whisk_favicon_w.svg`
- Local source page: `assets/logos/google-whisk/whisk-google-page.html`
- Relevant local assets:
  - `assets/logos/google-whisk/whisk_favicon_b.svg`
  - `assets/logos/google-whisk/whisk_favicon_w.svg`
  - `assets/logos/google-whisk/whisk_favicon_b.preview.png`
  - `assets/logos/google-whisk/whisk_favicon_w.preview.png`
- Local status: official Whisk favicon assets imported from the official Google
  Labs Whisk page. A standalone Whisk lockup was not confirmed in this pass.
- Working rule:
  - Do not generate Whisk, Google, Gemini, Imagen, or Google Labs marks, product
    UI, or brand-color substitutes from prompts.
  - Use the official black Whisk favicon for D-58 as a review-pending official
    icon overlay, not as a standalone product lockup.

## Seedance

- Source checked: `https://seed.bytedance.com/en/seedance`
- Official assets checked:
  - `https://lf3-static.bytednsdoc.com/obj/eden-cn/lapzild-tss/ljhwZthlaukjlkulzlp/favicon_1/favicon.ico`
- Local source page: `assets/logos/seedance/seedance-bytedance-page.html`
  and `assets/logos/seedance/seedance-official-page-2026-06-03.html`
- Relevant local assets:
  - `assets/logos/seedance/bytedance-seed-favicon.ico`
  - `assets/logos/seedance/bytedance-seed-favicon.preview.png`
- Local status: the official Seedance page was accessible and saved. The page
  confirms the Seedance page/title and contains shared site mark/favicon
  material, but no distinct Seedance-specific product logo or lockup was
  confirmed in the fetched page. The prior small shared ByteDance Seed favicon
  is not sufficient as a Seedance product logo.
- Working rule:
  - D-56 is now a confirmed logo-less `logo_avoid` / `color_audit` candidate.
  - Use the palette-normalized generated base as the review-pending candidate;
    do not apply the shared favicon as a Seedance product logo.
  - Do not substitute ByteDance, Doubao, Jimeng, fal.ai, or Replicate branding
    for the Seedance model logo.

## SuperClaude Framework

- Source checked:
  - `https://github.com/NomenAK/SuperClaude`
  - `https://github.com/SuperClaude-Org/SuperClaude_Framework`
- Local source file:
  - `assets/logos/superclaude/SuperClaude_Framework_README.md`
- Local status: the original repository redirects to the official
  `SuperClaude-Org/SuperClaude_Framework` repository. The README image
  references are badges and external service marks; the repository tree did
  not expose a SuperClaude-specific logo, icon, or lockup asset.
- Working rule:
  - The repository review did not find a SuperClaude-specific logo, icon, or
    lockup. The logo requirement matrix still classifies F-85 as brand-required
    with official-usage review pending. A generic, logo-free internal base may
    be considered separately, but do not describe the entry as cleared for a
    logo-free publication image or overlay until the matrix and use conditions
    are reconciled.
  - Do not use Claude / Anthropic marks because the entry explicitly describes
    SuperClaude as a community OSS framework and Anthropic-unofficial.
  - Do not synthesize a "SuperClaude" wordmark or use GitHub/SuperClaude org
    badges as a product logo.

## YouTube creator channel icons

- C-80 AI大学 source checked:
  - `https://www.youtube.com/channel/UCXo1SsIDZ_dke2Nr1r3qk6w`
  - Page `og:title`: `AI大学【AI&ChatGPT最新情報】`
  - Official avatar source: YouTube `og:image`
  - Local files:
    - `assets/logos/ai-daigaku/youtube-channel-page.html`
    - `assets/logos/ai-daigaku/youtube-channel-avatar.jpg`
- C-81 にゃんた source checked:
  - `https://www.youtube.com/channel/UCZQVTC3uLCyuJUOcRlguazA`
  - Page `og:title`: `にゃんたのAIチャンネル`
  - Official avatar source: YouTube `og:image`
  - Local files:
    - `assets/logos/nyanta/youtube-channel-page.html`
    - `assets/logos/nyanta/youtube-channel-avatar.jpg`
- C-82 まさお source checked:
  - `https://www.youtube.com/channel/UCvHpETRVi1tXeRJoYiXHJqw`
  - Page `og:title`: `まさおAIじっくり解説ch`
  - Official avatar source: YouTube `og:image`
  - Local files:
    - `assets/logos/masao/youtube-channel-page.html`
    - `assets/logos/masao/youtube-channel-avatar.jpg`
- C-83 AI の羅針盤 source checked:
  - `https://www.youtube.com/@compassinai`
  - Page `og:title`: `AI時代の羅針盤`
  - Official avatar source: YouTube `og:image`
  - Local files:
    - `assets/logos/ai-compass/youtube-channel-page.html`
    - `assets/logos/ai-compass/youtube-channel-avatar.jpg`
- Local status: official channel pages and unchanged 900x900 YouTube avatar
  images were saved for C-80, C-81, C-82, and C-83. C-83's canonical title is
  `AI時代の羅針盤` in the current entry and matrix. The legacy Batch 004 prompt
  still uses `AI の羅針盤` and must be corrected before any reuse.
- Working rule:
  - Use the saved YouTube `og:image` avatar only as a deterministic official
    channel-icon overlay.
  - Do not generate channel icons, YouTube UI, thumbnails, mascot-like
    substitutes, portrait likenesses, or creator branding in the illustration
    body.
  - The avatar rectangle is the only allowed off-palette color exception;
    normalize or regenerate the generated body if non-icon colors drift.

## Amical

- Source checked:
  - `https://github.com/amicalhq/amical`
  - `https://amical.ai/`
- Official repo assets checked:
  - `apps/www/public/amical-icon.svg`
  - `apps/www/public/amical-icon.png`
  - `apps/www/public/github-readme-header-light.png`
- Local files:
  - `assets/logos/amical/README.md`
  - `assets/logos/amical/github-tree-main.json`
  - `assets/logos/amical/amical-homepage.html`
  - `assets/logos/amical/amical-icon.svg`
  - `assets/logos/amical/amical-icon.png`
  - `assets/logos/amical/amical-icon.preview.png`
  - `assets/logos/amical/github-readme-header-light.png`
- Local status: official GitHub/website assets confirm Amical as a local-first
  AI dictation and note-taking app. This conflicts with the current D-70 entry
  prose, which still describes a Korean/NHN medical AI solution. Keep D-70
  review-pending before final promotion until the entry text and visual subject
  are reconciled.
- Working rule:
  - Use `assets/logos/amical/amical-icon.png` as a review-pending official app
    icon overlay for D-70.
  - Do not use the README badges, store buttons, third-party integration icons,
    product UI screenshots, or generated Amical wordmarks as brand substitutes.
  - The official app icon rectangle is the only off-palette exception; generated
    body colors remain restricted to the ponchi palette.

## Mistral AI / Hugging Face / Groq / AMD

- Mistral source checked: `https://mistral.ai/brand`
- Mistral official source assets checked:
  - `https://mistral.ai/_astro/cover-logo-lockup-black_Z1AaSCB.webp?dpl=6a1ef9e39e8df50008a787ed`
  - `https://mistral.ai/_astro/cover-logo-icon-gradient_Z1vzKon.webp?dpl=6a1ef9e39e8df50008a787ed`
- Mistral local source assets:
  - `assets/logos/mistral/mistral-cover-logo-lockup-black.webp`
  - `assets/logos/mistral/mistral-cover-logo-icon-gradient.webp`
- Mistral local overlay assets:
  - `assets/logos/mistral/mistral-cover-logo-lockup-black.transparent.png`
  - `assets/logos/mistral/mistral-cover-logo-icon-gradient.transparent.png`
- Hugging Face source checked: `https://huggingface.co/brand`
- Hugging Face official asset checked:
  `https://huggingface.co/datasets/huggingface/brand-assets/resolve/main/hf-logo-with-title.svg`
- Hugging Face local asset:
  - `assets/logos/huggingface/hf-logo-with-title.svg`
- ACE-Step source checked: `https://github.com/ace-step/ACE-Step-1.5`
- ACE-Step official repo assets checked:
  - `https://raw.githubusercontent.com/ace-step/ACE-Step-1.5/main/assets/acestep_logo.png`
  - `https://raw.githubusercontent.com/ace-step/ACE-Step-1.5/main/assets/acemusic-logo.svg`
  - `https://raw.githubusercontent.com/ace-step/ACE-Step-1.5/main/assets/acestudio_logo.png`
  - `https://raw.githubusercontent.com/ace-step/ACE-Step-1.5/main/assets/Logo_StepFun.png`
- ACE-Step local assets:
  - `assets/logos/ace-step/ACE-Step-1.5-README.md`
  - `assets/logos/ace-step/acestep_logo.png`
  - `assets/logos/ace-step/acemusic-logo.svg`
  - `assets/logos/ace-step/acestudio_logo.png`
  - `assets/logos/ace-step/Logo_StepFun.png`
- ACE-Step working decision: use `acestep_logo.png` for B-61 as the
  ACE-Step-specific official repo logo. Preserve the black square source
  artwork unchanged; do not crop, recolor, synthesize a transparent wordmark,
  or substitute ACE Music / ACE Studio / StepFun logos for the model logo.
- AMD source checked: `https://www.amd.com/en.html`
- AMD official asset checked:
  `https://www.amd.com/content/dam/code/images/header/amd-header-logo.svg`
- AMD local asset:
  - `assets/logos/amd/amd-header-logo.svg`
- Groq source checked: `https://groq.com/`
- Groq official source asset checked:
  - Inline SVG embedded in the official homepage header branding link
    (`SiteNavigation_nav__branding__DRcTS`).
  - Rejected source-reviewed candidate:
    `https://cdn.sanity.io/images/chol0sk5/production/8776faec2ef547091786cde2fca3aaa3ca1a2fc6-423x89.svg`
    is an official Groq page asset but includes a McLaren Formula 1 partner
    lockup, so it is not used for the standalone Groq entry.
- Groq local asset:
  - `assets/logos/groq/groq-wordmark-official-inline.svg`
- Working rule:
  - Use Mistral official brand-page assets only after preserving logo geometry;
    local transparent PNGs remove only the official page canvas background.
  - Use the Hugging Face official brand asset as supplied.
  - Use AMD's official white header logo without recoloring; if the white logo
    must sit on a non-white field, place it on a plain blue composition plate
    and keep the logo itself unchanged.
  - Use the Groq official homepage inline wordmark as supplied; customer logos
    and partner lockups from the same page are not valid substitutes.

## Moonshot AI

- Moonshot AI source checked: `https://www.moonshot.cn/`
- Moonshot AI official source asset checked:
  - Base64 PNG logo embedded in official site chunk
    `https://statics.moonshot.cn/moonshot-ai/assets/chunks/chunk-CKQj9p3E.js`
  - `https://statics.moonshot.cn/moonshot-ai/assets/static/kimi-icon.ByIGCGon.webp`
    referenced by the official homepage HTML for Kimi.
- Moonshot AI local asset:
  - `assets/logos/moonshot-ai/moonshot-inline-logo.png`
  - `assets/logos/kimi/kimi-icon-official.webp`
- Working rule:
  - Use the official white Moonshot AI logo PNG unchanged. Because it is a
    white transparent logo, place it unchanged on a plain dark-blue composition
    plate for visibility.

## Z.ai

- Z.ai source checked: `https://z.ai/`
- Z.ai official source asset checked:
  - `https://z-cdn.chatglm.cn/z-ai/static/logo.svg`
- Z.ai local assets:
  - `assets/logos/z-ai/z-ai-logo-official.svg`
  - `assets/logos/z-ai/z-ai-logo-official.512.png`
- Working rule:
  - Use the official Z.ai icon as supplied. For compositing, use the 512px PNG
    rendered from the official SVG so the small icon stays crisp.

## Qwen

- Qwen source checked: `https://qwen.ai/`
- Qwen official source assets checked:
  - `https://img.alicdn.com/imgextra/i4/O1CN01Ue4htA1hduZMvHQlx_!!6000000004301-2-tps-270-90.png`
  - `https://img.alicdn.com/imgextra/i4/O1CN01a6pmNi24dfWQwmMp3_!!6000000007414-2-tps-270-90.png`
  - Both URLs are exported by official site JS module `58809` in
    `https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.60/js/9496.js` and used by
    the official `QWenLogo` header component.
- Qwen local assets:
  - `assets/logos/qwen/qwen-logo-official-dark-header.png`
  - `assets/logos/qwen/qwen-logo-official-light-header.png`
- Working rule:
  - Use the official Qwen header logo PNG as supplied. Prefer the darker
    `qwen-logo-official-light-header.png` variant on white ponchi canvases.

## DeepSeek

- DeepSeek source checked: `https://www.deepseek.com/`
- DeepSeek official source asset checked:
  - `https://cdn.deepseek.com/logo.png?x-image-process=image%2Fresize%2Cw_1920`
- DeepSeek local asset:
  - `assets/logos/deepseek/deepseek-logo-official.png`
- Working rule:
  - Use the official DeepSeek horizontal logo PNG as supplied.

## NVIDIA / Excalidraw / arXiv / TSMC

- NVIDIA source checked:
  `https://www.nvidia.com/en-us/about-nvidia/legal-info/logo-brand-usage/`
- NVIDIA official asset checked:
  `https://www.nvidia.com/content/nvidiaGDC/us/en_US/about-nvidia/legal-info/logo-brand-usage/_jcr_content/root/responsivegrid/nv_container_392921705/nv_container_412055486/nv_image.coreimg.svg/1776076920317/nvidia-logo-horz.svg`
- NVIDIA local asset:
  - `assets/logos/nvidia/nvidia-logo-horz.svg`
- Excalidraw source checked:
  `https://github.com/excalidraw/excalidraw`
- Excalidraw official repo asset checked:
  `https://raw.githubusercontent.com/excalidraw/excalidraw/master/public/favicon.svg`
- Excalidraw local asset:
  - `assets/logos/excalidraw/excalidraw-favicon.svg`
- arXiv sources checked:
  - `https://arxiv.org/`
  - `https://static.arxiv.org/static/arxiv.marxdown/0.1/about/arXiv_Brand_Guide_2021.pdf`
- arXiv official asset checked:
  `https://arxiv.org/static/browse/0.3.4/images/arxiv-logo-one-color-white.svg`
- arXiv local asset:
  - `assets/logos/arxiv/arxiv-logo-one-color-white.svg`
- TSMC source checked: `https://www.tsmc.com/english`
- TSMC source status: the official site returned a Cloudflare JavaScript /
  cookie challenge in the shell environment during the 2026-06-03 pass, so no
  official TSMC logo asset was imported.
- Working rule:
  - Use NVIDIA's official horizontal logo from its logo/brand usage page.
  - Use Excalidraw's official repository favicon as the product mark; do not
    synthesize a wordmark.
  - Use arXiv's official white logo unchanged, placed on a plain dark
    composition plate for visibility.
  - Move TSMC to confirmed logo-less `logo_avoid` / `color_audit`; no usable
    official TSMC logo asset was confirmed in this environment.
  - Do not use third-party logo mirrors or redraw the TSMC wordmark.

## Amazon Bedrock / Figma / Reddit / Canva

- Amazon Bedrock source checked:
  `https://aws.amazon.com/architecture/icons/`
- Amazon Bedrock official asset checked:
  `assets/logos/aws/aws-architecture-icons-2026-01-30/Architecture-Service-Icons_01302026/Arch_Artificial-Intelligence/64/Arch_Amazon-Bedrock_64.svg`
  from the imported official AWS Architecture Icons package.
- Figma source checked:
  `https://www.figma.com/using-the-figma-brand/`
- Figma official asset checked:
  `https://static.figma.com/app/icon/2/favicon.svg`
- Figma local asset:
  - `assets/logos/figma/figma-favicon.svg`
- Reddit source checked: `https://www.redditinc.com/brand`
- Reddit official asset checked:
  `https://redditinc.com/hubfs/raw_assets/public/redditinc/images/Reddit_Lockup_Logo.svg`
- Reddit local asset:
  - `assets/logos/reddit/Reddit_Lockup_Logo.svg`
- Canva source checked: `https://www.canva.com/newsroom/logos/`
- Canva source status: official page returned 403 in the shell environment
  during this pass, so no local official asset was imported.
- Working rule:
  - Use Amazon Bedrock's official AWS Architecture service icon for the
    Bedrock-specific entry, not a generic AWS brand mark.
  - Use Figma's official app/favicon mark from the official Figma domain; do
    not synthesize a Figma wordmark.
  - Use Reddit's official lockup SVG from the Reddit brand page.
  - Keep Canva in `overlay_wait` until an official source can be accessed and
    recorded.

## shadcn/ui and VS Code extension icons

- shadcn/ui source checked: `https://ui.shadcn.com/`
- shadcn/ui official asset checked:
  `https://ui.shadcn.com/apple-touch-icon.png`
- shadcn/ui local asset:
  - `assets/logos/shadcn-ui/apple-touch-icon.png`
- Markdown Preview Enhanced source checked:
  `https://github.com/shd101wyy/vscode-markdown-preview-enhanced`
- Markdown Preview Enhanced official repo asset checked:
  `https://raw.githubusercontent.com/shd101wyy/vscode-markdown-preview-enhanced/master/media/mpe.png`
- Markdown Preview Enhanced local asset:
  - `assets/logos/markdown-preview-enhanced/mpe.png`
- Git Graph source checked:
  `https://github.com/mhutchie/vscode-git-graph`
- Git Graph official repo asset checked:
  `https://raw.githubusercontent.com/mhutchie/vscode-git-graph/master/resources/icon.png`
- Git Graph local asset:
  - `assets/logos/git-graph/git-graph-icon.png`
- Japanese Language Pack for VS Code source checked:
  `https://github.com/microsoft/vscode-loc`
- Japanese Language Pack official repo asset checked:
  `https://raw.githubusercontent.com/microsoft/vscode-loc/main/i18n/vscode-language-pack-ja/languagepack.png`
- Japanese Language Pack local asset:
  - `assets/logos/vscode-language-pack-ja/languagepack.png`
- Markdown All in One source checked:
  `https://github.com/yzhang-gh/vscode-markdown`
- Markdown All in One official repo asset checked:
  `https://raw.githubusercontent.com/yzhang-gh/vscode-markdown/master/images/Markdown-mark.png`
- Markdown All in One local asset:
  - `assets/logos/markdown-all-in-one/Markdown-mark.png`
- Working rule:
  - Use the official app/extension icon files only; do not synthesize wordmarks
    for extension entries.
  - Keep icon colors and backgrounds unchanged.

## Batch 002 unresolved source decisions

These items remain blocked because the official-source question is not the same
as having a recognizable logo somewhere on the web.

- Devin:
  - Source checked: `https://devin.ai/`
  - Official source asset checked: inline header SVG under
    `<a id="site-header__logo">` on the official Devin homepage.
  - Local assets:
    - `assets/logos/devin/devin-homepage.html`
    - `assets/logos/devin/devin-official-header-mark.svg`
    - `assets/logos/devin/devin-official-header-mark.preview.png`
  - Working decision: use the official Devin header mark as a review-pending
    official overlay for B-10. The SVG was extracted from the official homepage
    and kept as a black mark on white; do not synthesize a Devin wordmark.
- Microsoft / Copilot / Azure:
  - Source checked: `https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks`
  - Source status: Microsoft confirms that product names, logos, app icons, and
    related designs are Microsoft brand assets and that many logo/app-icon uses
    require a license first.
  - Microsoft Copilot official source checked: `https://copilot.microsoft.com/`
  - Microsoft Copilot source status: the official Copilot homepage exposes an
    inline Copilot icon SVG in the sidebar brand button and a Copilot wordmark
    SVG under `/static/cmc/assets/`. The specific Microsoft.com marketing pages
    for Microsoft Copilot, Microsoft 365 Copilot, Edge Copilot, and Microsoft AI
    returned 403 from local shell access, so the generic Copilot icon is kept
    review-pending for product-specific final review.
  - Azure architecture icon source checked:
    `https://learn.microsoft.com/en-gb/azure/architecture/icons/`
  - Azure architecture icon package:
    `https://arch-center.azureedge.net/icons/Azure_Public_Service_Icons_V23.zip`
  - Local package:
    `assets/logos/azure/Azure_Public_Service_Icons_V23.zip`
  - Local assets:
    - `assets/logos/microsoft-copilot/copilot-homepage.html`
    - `assets/logos/microsoft-copilot/copilot-official-inline-icon.svg`
    - `assets/logos/microsoft-copilot/copilot-official-inline-icon.preview.png`
    - `assets/logos/microsoft-copilot/copilot-wordmark-DvWA6bVb.svg`
    - `assets/logos/microsoft-copilot/favicon.svg`
    - `assets/logos/microsoft-ai/microsoft.ai_favicon.ico`
    - `assets/logos/microsoft-ai/microsoft-ai-favicon.preview.png`
    - `assets/logos/azure/Azure_Public_Service_Icons_V23/Azure_Public_Service_Icons/Icons/other/10018-icon-service-Azure-A.svg`
    - `assets/logos/azure/Azure_Public_Service_Icons_V23/Azure_Public_Service_Icons/Icons/ai + machine learning/03438-icon-service-Azure-OpenAI.svg`
  - Working decision: use the official Azure service icons for B-25 Azure and
    B-26 Azure OpenAI. Use the unchanged official Copilot homepage icon for
    B-15 Microsoft Copilot as a review-pending official icon overlay. Use that
    same official Copilot-family icon for B-16 Microsoft 365 Copilot and B-17
    Edge Copilot as review-pending overlays because dedicated product lockups
    were not confirmed locally. Move C-8 Microsoft AI to confirmed logo-less
    `logo_avoid` / `color_audit`; the saved official Microsoft AI page confirms
    the Microsoft AI page title and UHF text brand link, but no dedicated
    Microsoft AI logo image or organization lockup was confirmed.
- Google Cloud / Vertex AI:
  - Sources checked:
    - `https://about.google/brand-resource-center/`
    - `https://cloud.google.com/icons/`
    - `https://services.google.com/fh/files/misc/core-products-icons.zip`
  - Source status: Google Cloud's official icon page links the official Core
    Products Icons ZIP. The ZIP contains a `Unique Icons/Vertex AI` product
    icon in SVG and PNG form.
  - Working decision: use the Google Cloud lockup for B-24; use the official
    Vertex AI product icon for B-27 as a review-pending official overlay.
- AWS:
  - Source checked: `https://aws.amazon.com/trademark-guidelines/`
  - Additional source checked: `https://aws.amazon.com/architecture/icons/`
  - Local source pages:
    - `assets/logos/aws/brand-review/aws-trademark-guidelines.html`
    - `assets/logos/aws/brand-review/aws-architecture-icons-page.html`
  - Source status: AWS trademark guidance covers AWS marks and AWS logos. The
    local AWS Architecture Icons package is useful for architecture diagrams but
    is not the same as a primary AWS brand lockup for B-23.
    The official architecture icons page confirms AWS-approved diagram icons,
    not a general permission to use the AWS Smile Logo as a primary logo
    overlay for this dictionary image.
  - Working decision: move B-23 to confirmed logo-less `logo_avoid` /
    `color_audit`. Do not use the AWS Smile Logo, architecture icons as a
    primary AWS brand lockup, or third-party logo mirrors for this entry.
- Claude Cowork:
  - Sources checked:
    - `https://support.claude.com/en/articles/9266767-what-is-the-claude-team-plan`
    - `https://claude.com/pricing/team`
  - Source status: official sources use Claude Team / Team plan language. A
    distinct official `Claude Cowork` product logo has not been confirmed.
  - Working decision: move B-19 to confirmed logo-less `logo_avoid` /
    `color_audit` and stage the generated base as a review-pending candidate.
    Do not apply a generic Claude or Anthropic logo unless the entry is renamed
    and the brand decision is reopened.
- Aqua Voice:
  - Source checked: `https://aquavoice.com/`
  - Official assets checked:
    - `https://framerusercontent.com/images/KO3UUG0mbyyUBnMxZ3jjJyQu8I.png`
    - `https://framerusercontent.com/images/XEjM4qCuuNRdTthHiLmrnhQXyto.png`
  - Local assets:
    - `assets/logos/aqua-voice/aquavoice-homepage.html`
    - `assets/logos/aqua-voice/aquavoice-favicon.png`
    - `assets/logos/aqua-voice/aquavoice-apple-touch-icon.png`
  - Working decision: use the official Aqua Voice favicon for B-18 as a
    review-pending official icon overlay. A standalone Aqua Voice lockup was
    not confirmed in this pass, so do not synthesize wordmarks or brand-like
    substitutes.

## Overlay application progress

Current deterministic official-logo overlays staged as review-pending
final candidates:

- `ponchi-batch-002`: B-10 uses
  `assets/logos/devin/devin-official-header-mark.svg`, extracted from the
  official Devin homepage header (`https://devin.ai/`, inline
  `site-header__logo` SVG), retrieved 2026-06-03.
- `ponchi-batch-002`: B-18 uses
  `assets/logos/aqua-voice/aquavoice-favicon.png`, the official favicon linked
  from the official Aqua Voice homepage (`https://aquavoice.com/`, asset
  `https://framerusercontent.com/images/KO3UUG0mbyyUBnMxZ3jjJyQu8I.png`),
  retrieved 2026-06-03. This is a review-pending official icon overlay, not a
  generated logo or synthesized Aqua Voice wordmark.
- `ponchi-batch-003`: B-30 uses the Amazon Bedrock service icon
  `assets/logos/aws/aws-architecture-icons-2026-01-30/Architecture-Service-Icons_01302026/Arch_Artificial-Intelligence/64/Arch_Amazon-Bedrock_64.svg`
  from the imported official AWS Architecture Icons package, retrieved
  2026-06-03.
- `ponchi-batch-003`: B-31 uses
  `assets/logos/excalidraw/excalidraw-favicon.svg` from the official Excalidraw
  repo (`https://github.com/excalidraw/excalidraw`, raw path
  `public/favicon.svg`), retrieved 2026-06-03.
- `ponchi-batch-003`: B-32 uses `assets/logos/figma/figma-favicon.svg` from the
  official Figma brand usage page (`https://www.figma.com/using-the-figma-brand/`,
  asset `https://static.figma.com/app/icon/2/favicon.svg`), retrieved
  2026-06-03.
- `ponchi-batch-003`: B-40 uses `assets/logos/reddit/Reddit_Lockup_Logo.svg`
  from the official Reddit brand page (`https://www.redditinc.com/brand`, asset
  `https://redditinc.com/hubfs/raw_assets/public/redditinc/images/Reddit_Lockup_Logo.svg`),
  retrieved 2026-06-03.
- `ponchi-batch-003`: B-41 uses
  `assets/logos/arxiv/arxiv-logo-one-color-white.svg` from the official arXiv
  site (`https://arxiv.org/`, asset path
  `/static/browse/0.3.4/images/arxiv-logo-one-color-white.svg`), retrieved
  2026-06-03. The official white logo is placed unchanged on a plain dark
  composition plate for visibility.
- `ponchi-batch-001`: B-3 and B-8 use the imported official OpenAI wordmark
  because the entries identify OpenAI services and no dedicated ChatGPT/Codex
  lockup has been imported.
- `ponchi-batch-003`: B-50 uses the official Claude logo; B-51 and C-1 use the
  imported official OpenAI wordmark; C-2 uses the imported official Anthropic logo.
- `ponchi-batch-003`: C-6 uses
  `assets/logos/mistral/mistral-cover-logo-lockup-black.transparent.png`
  derived from the official Mistral brand page lockup asset, retrieved
  2026-06-03.
- `ponchi-batch-003`: C-7 uses
  `assets/logos/huggingface/hf-logo-with-title.svg` from the official Hugging
  Face brand page (`https://huggingface.co/brand`, asset
  `https://huggingface.co/datasets/huggingface/brand-assets/resolve/main/hf-logo-with-title.svg`),
  retrieved 2026-06-03.
- `ponchi-batch-003`: C-9 uses `assets/logos/nvidia/nvidia-logo-horz.svg` from
  NVIDIA's official logo/brand usage page
  (`https://www.nvidia.com/en-us/about-nvidia/legal-info/logo-brand-usage/`),
  retrieved 2026-06-03.
- `ponchi-batch-004`: C-10 uses
  `assets/logos/moonshot-ai/moonshot-inline-logo.png`, extracted from the
  official Moonshot AI homepage JavaScript chunk (`https://www.moonshot.cn/`,
  chunk `https://statics.moonshot.cn/moonshot-ai/assets/chunks/chunk-CKQj9p3E.js`),
  retrieved 2026-06-03. The official white transparent logo is placed
  unchanged on a plain dark-blue composition plate for visibility.
- `ponchi-batch-004`: C-11 uses `assets/logos/z-ai/z-ai-logo-official.svg`
  from the official Z.ai homepage (`https://z.ai/`, asset
  `https://z-cdn.chatglm.cn/z-ai/static/logo.svg`), retrieved 2026-06-03.
  The overlay uses `assets/logos/z-ai/z-ai-logo-official.512.png`, rendered
  from the official SVG to preserve crisp edges.
- `ponchi-batch-006`: D-45 GLM uses the same official Z.ai icon
  `assets/logos/z-ai/z-ai-logo-official.512.png` as the developer/organization
  overlay. The entry identifies GLM as a Z.ai model family. A dedicated GLM
  product logo was not confirmed, so this remains a review-pending organization
  overlay before final promotion.
- `ponchi-batch-006`: D-44 uses `assets/logos/kimi/kimi-icon-official.webp`
  from the official Moonshot AI homepage (`https://www.moonshot.cn/`, asset
  `https://statics.moonshot.cn/moonshot-ai/assets/static/kimi-icon.ByIGCGon.webp`),
  retrieved 2026-06-03.
- `ponchi-batch-006`: D-43 uses
  `assets/logos/qwen/qwen-logo-official-light-header.png` from the official
  Qwen homepage (`https://qwen.ai/`), exported by official site JS module
  `58809` in `https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.60/js/9496.js`,
  retrieved 2026-06-03.
- `ponchi-batch-006`: D-46 and D-47 use
  `assets/logos/deepseek/deepseek-logo-official.png` from the official
  DeepSeek homepage (`https://www.deepseek.com/`, asset
  `https://cdn.deepseek.com/logo.png?x-image-process=image%2Fresize%2Cw_1920`),
  retrieved 2026-06-03.
- `ponchi-batch-004`: C-13 uses
  `assets/logos/groq/groq-wordmark-official-inline.svg`, extracted unchanged
  from the official Groq homepage header branding SVG (`https://groq.com/`),
  retrieved 2026-06-03. A separate official Groq page Sanity asset containing a
  McLaren Formula 1 partner lockup was source-reviewed and rejected for this
  standalone Groq entry.
- `ponchi-batch-004`: C-14 uses `assets/logos/amd/amd-header-logo.svg` from the
  official AMD homepage header (`https://www.amd.com/en.html`, asset
  `https://www.amd.com/content/dam/code/images/header/amd-header-logo.svg`),
  retrieved 2026-06-03. The official white logo is placed unchanged on a plain
  blue composition plate for visibility.
- `ponchi-batch-005`: D-10, D-11, D-12, D-13, and D-14 use the official Claude
  logo; D-20, D-21, D-22, D-23, D-24, D-25, and D-26 use the imported official
  OpenAI wordmark; D-35 uses the official Cursor horizontal lockup.
- `ponchi-batch-005`: D-41 uses
  `assets/logos/mistral/mistral-cover-logo-icon-gradient.transparent.png`
  derived from the official Mistral brand page icon asset, retrieved
  2026-06-03.
- `ponchi-batch-006`: D-50, D-52, and D-71 use the imported official OpenAI
  wordmark.
- `ponchi-batch-008`: F-10 uses `assets/logos/react/wordmark_light.svg` from
  the official React docs repo (`https://github.com/reactjs/react.dev`, raw path
  `public/images/brand/wordmark_light.svg`), retrieved 2026-06-03.
- `ponchi-batch-008`: F-11 uses
  `assets/logos/nextjs/nextjs-assets/NEXTJS/logotype/light-background/nextjs-logotype-light-background.svg`
  from the official Vercel Next.js brand assets page
  (`https://vercel.com/design/brands#next-js`, download
  `https://k2mkucxia43oc7fa.public.blob.vercel-storage.com/front/press/nextjs-assets.zip`),
  retrieved 2026-06-03.
- `ponchi-batch-008`: F-12 uses
  `assets/logos/electron/electron-logo-wide-black.svg` from the OpenJS
  Foundation official artwork repo
  (`https://github.com/openjs-foundation/artwork`, raw path
  `projects/electron/electron-logo-wide-black.svg`), retrieved 2026-06-03.
- `ponchi-batch-008`: F-13 uses
  `assets/logos/tauri/logopack/TAURI LOGOPACK/TAURI Monochrome/TAURI_Logo_Mono_Black.svg`
  from the official Tauri trademark page logopack
  (`https://tauri.app/about/trademark/`, download
  `https://tauri.app/assets/logopack.zip`), retrieved 2026-06-03.
- `ponchi-batch-008`: F-14 uses `assets/logos/threejs/icon.svg` from the
  official three.js repo (`https://github.com/mrdoob/three.js`, raw path
  `files/icon.svg`), retrieved 2026-06-03.
- `ponchi-batch-008`: F-15 uses
  `assets/logos/shadcn-ui/apple-touch-icon.png` from the official shadcn/ui
  site (`https://ui.shadcn.com/`, asset `/apple-touch-icon.png`), retrieved
  2026-06-03.
- `ponchi-batch-008`: F-16 uses
  `assets/logos/tailwindcss/tailwindcss-logotype.svg` from the official
  Tailwind CSS site repo (`https://github.com/tailwindlabs/tailwindcss.com`,
  raw path `src/app/(docs)/brand/img/tailwindcss-logotype.svg`), retrieved
  2026-06-03.
- `ponchi-batch-008`: F-17 uses `assets/logos/astro/astro-logo-dark.svg` from
  the official Astro press page (`https://astro.build/press`, download path
  `/assets/press/astro-logo-dark.svg`), retrieved 2026-06-03.
- `ponchi-batch-008`: F-20 uses `assets/logos/eslint/eslint-logo-color.svg`
  from the official ESLint site repo (`https://github.com/eslint/eslint.org`,
  raw path `src/assets/images/logo/eslint-logo-color.svg`), retrieved
  2026-06-03.
- `ponchi-batch-008`: F-21 uses
  `assets/logos/prettier/prettier-centered-logo-static.svg` from the official
  Prettier repo (`https://github.com/prettier/prettier`, raw path
  `website/static/prettier-centered-logo-static.svg`), retrieved 2026-06-03.
- `ponchi-batch-008`: F-30 and F-34 use
  `assets/logos/vscode/visual-studio-code-icons/visual-studio-code-icons/vscode.svg`
  from the official Visual Studio Code brand page
  (`https://code.visualstudio.com/brand`, download
  `https://code.visualstudio.com/assets/branding/visual-studio-code-icons.zip`),
  retrieved 2026-06-03.
- `ponchi-batch-008`: F-35 uses
  `assets/logos/markdown-preview-enhanced/mpe.png` from the official Markdown
  Preview Enhanced repo (`https://github.com/shd101wyy/vscode-markdown-preview-enhanced`,
  raw path `media/mpe.png`), retrieved 2026-06-03.
- `ponchi-batch-008`: F-36 uses `assets/logos/git-graph/git-graph-icon.png`
  from the official Git Graph repo (`https://github.com/mhutchie/vscode-git-graph`,
  raw path `resources/icon.png`), retrieved 2026-06-03.
- `ponchi-batch-009`: F-37 uses
  `assets/logos/vscode-language-pack-ja/languagepack.png` from the official
  Microsoft `vscode-loc` repo (`https://github.com/microsoft/vscode-loc`, raw
  path `i18n/vscode-language-pack-ja/languagepack.png`), retrieved 2026-06-03.
- `ponchi-batch-009`: F-38 uses
  `assets/logos/markdown-all-in-one/Markdown-mark.png` from the official
  Markdown All in One repo (`https://github.com/yzhang-gh/vscode-markdown`, raw
  path `images/Markdown-mark.png`), retrieved 2026-06-03.
- `ponchi-batch-009`: F-40 uses `assets/logos/npm/npm-logo-black.svg` from the
  official npm logos repo (`https://github.com/npm/logos`, raw path
  `npm logo/npm-logo-black.svg`), retrieved 2026-06-03.
- `ponchi-batch-009`: F-41 uses `assets/logos/vite/vite-dark.svg` from the
  official Vite repo (`https://github.com/vitejs/vite`, raw path
  `docs/public/vite-dark.svg`), retrieved 2026-06-03.
- `ponchi-batch-009`: F-44 uses `assets/logos/pnpm/pnpm-standard.svg` from the
  official pnpm site repo (`https://github.com/pnpm/pnpm.io`, raw path
  `static/img/logos/pnpm-standard.svg`), retrieved 2026-06-03.
- `ponchi-batch-009`: F-50 uses `assets/logos/git/Git-Logo-Black.svg` from the
  official Git logo downloads page
  (`https://git-scm.com/community/logos.html`), retrieved 2026-06-03.
- `ponchi-batch-009`: F-60, F-61, and F-62 use the official GitHub lockup from
  the imported GitHub logo package.
- `ponchi-batch-010`: F-80 uses `assets/logos/nodejs/nodejsDark.svg` from the
  official Node.js site repo (`https://github.com/nodejs/nodejs.org`, raw path
  `apps/site/public/static/logos/nodejsDark.svg`), retrieved 2026-06-03.
- `ponchi-batch-010`: F-82 uses `assets/logos/wsl/wsl-icon.svg` from the
  official Microsoft Learn WSL page (`https://learn.microsoft.com/en-us/windows/wsl/`,
  asset `https://learn.microsoft.com/windows/wsl/media/wsl-icon.svg`), retrieved
  2026-06-03.
- `ponchi-batch-010`: F-83 uses
  `assets/logos/powershell/logo-powershell-core.svg` from the official
  Microsoft Learn PowerShell digital art page
  (`https://learn.microsoft.com/en-us/powershell/scripting/community/digital-art`,
  asset `https://learn.microsoft.com/media/logos/logo-powershell-core.svg`),
  retrieved 2026-06-03.
- `ponchi-batch-010`: F-86 uses `assets/logos/ollama/logo-image.png` from the
  official Ollama repo (`https://github.com/ollama/ollama`, raw path
  `docs/images/logo.png`), retrieved 2026-06-03.
- `ponchi-batch-010`: F-90 uses
  `assets/logos/docker/Docker-Logos-1/docker-logos/SVG/docker-logo-black.svg`
  from Docker's official media resources page
  (`https://www.docker.com/company/newsroom/media-resources/`, download
  `https://www.docker.com/static/Docker-Logos-1.zip`), retrieved 2026-06-03.
- `ponchi-batch-010`: F-110 uses
  `assets/logos/lighthouse/lighthouse-logo.svg` from the official Chrome
  developer Lighthouse overview page
  (`https://developer.chrome.com/docs/lighthouse/overview`, asset
  `/static/docs/lighthouse/overview/image/lighthouse-logo.svg`), retrieved
  2026-06-03.
- `ponchi-batch-010`: F-120 uses `assets/logos/postgresql/elephant.png` from
  the official PostgreSQL trademark/press assets page
  (`https://www.postgresql.org/about/policies/trademarks/`, asset path
  `/media/img/about/press/elephant.png`), retrieved 2026-06-03.
- `ponchi-batch-010`: F-121 uses `assets/logos/sqlite/sqlite370_banner.svg`
  from the official SQLite site (`https://www.sqlite.org/`, asset path
  `images/sqlite370_banner.svg`), retrieved 2026-06-03.
- `ponchi-batch-010`: F-122 uses `assets/logos/prisma/logo-dark.svg` from the
  official Prisma docs repo (`https://github.com/prisma/docs`, raw path
  `apps/docs/public/img/logo-dark.svg`), retrieved 2026-06-03.
- `ponchi-batch-011`: F-140 uses
  `assets/logos/mermaid/mermaid-logo-horizontal.svg` from the official Mermaid
  repo (`https://github.com/mermaid-js/mermaid`, raw path
  `docs/public/mermaid-logo-horizontal.svg`), retrieved 2026-06-03.
- `ponchi-batch-011`: F-141 uses `assets/logos/plantuml/logo3.png` from the
  official PlantUML site (`https://plantuml.com/`, referenced as
  `https://cdn-0.plantuml.com/logo3.png`), retrieved 2026-06-03.
- `ponchi-batch-011`: F-153 uses
  `assets/logos/creative-commons/cc.logo.svg` from the official Creative
  Commons downloads page (`https://creativecommons.org/about/downloads/`, asset
  `https://mirrors.creativecommons.org/presskit/logos/cc.logo.svg`), retrieved
  2026-06-03.
- `ponchi-batch-011`: F-170 uses the Amazon EC2 service icon
  `assets/logos/aws/aws-architecture-icons-2026-01-30/Architecture-Service-Icons_01302026/Arch_Compute/64/Arch_Amazon-EC2_64.svg`
  from the imported official AWS Architecture Icons package, retrieved
  2026-06-03.
- `ponchi-batch-011`: F-171 uses the Amazon S3 service icon
  `assets/logos/aws/aws-architecture-icons-2026-01-30/Architecture-Service-Icons_01302026/Arch_Storage/64/Arch_Amazon-Simple-Storage-Service_64.svg`
  from the imported official AWS Architecture Icons package, retrieved
  2026-06-03.
- `ponchi-batch-011`: F-172 uses the AWS IAM service icon
  `assets/logos/aws/aws-architecture-icons-2026-01-30/Architecture-Service-Icons_01302026/Arch_Security-Identity/64/Arch_AWS-Identity-and-Access-Management_64.svg`
  from the imported official AWS Architecture Icons package, retrieved
  2026-06-03.
- `ponchi-batch-011`: F-180 uses `assets/logos/khronos/opengl.svg` from the
  official Khronos OpenGL page (`https://www.khronos.org/opengl/`, asset path
  `/assets/images/api_logos/opengl.svg`), retrieved 2026-06-03.
- `ponchi-batch-011`: F-181 uses `assets/logos/khronos/WebGL-Logo.svg` from
  the official Khronos WebGL registry resources page
  (`https://registry.khronos.org/webgl/resources/`, asset
  `WebGL-Logo.svg`), retrieved 2026-06-03.
- `ponchi-batch-011`: F-200 uses `assets/logos/rust/rust-logo.svg` from the
  official Rust artwork repo (`https://github.com/rust-lang/rust-artwork`, raw
  path `logo/rust-logo.svg`), retrieved 2026-06-03.
- `ponchi-batch-003`: B-60 uses `assets/logos/suno/Suno_wordmark.svg` from the
  official Suno about site (`https://about.suno.com/`, asset path
  `/img/life-at-suno/Suno_wordmark.svg`), retrieved 2026-06-03. The official
  light wordmark sits on a plain dark-blue composition plate for visibility; the
  wordmark itself is not recolored.
- `ponchi-batch-003`: C-3 uses
  `assets/logos/google-deepmind/google_deepmind_48dp.svg` from the official
  Google DeepMind site icon (`https://deepmind.google/`, asset
  `https://storage.googleapis.com/gdm-deepmind-com-prod-public/icons/google_deepmind_48dp.svg`),
  retrieved 2026-06-03.
- `ponchi-batch-003`: C-5 uses `assets/logos/xai/xai-favicon.ico` from the
  official xAI site root (`https://x.ai/favicon.ico`), retrieved 2026-06-03.
  The main xAI site and brand-guidelines page returned Cloudflare/403 responses
  from this environment, so this is recorded as an official favicon overlay and
  remains review-pending before any final promotion.
- `ponchi-batch-005`: D-30 uses `assets/logos/xai/xai-favicon.ico` from the
  official xAI site root (`https://x.ai/favicon.ico`), retrieved 2026-06-03.
  This uses the same source-reviewed favicon as C-5.
- `ponchi-batch-006`: D-60 uses
  `assets/logos/google-deepmind/google_deepmind_48dp.svg` from the official
  Google DeepMind site icon (`https://deepmind.google/`, asset
  `https://storage.googleapis.com/gdm-deepmind-com-prod-public/icons/google_deepmind_48dp.svg`),
  retrieved 2026-06-03. This uses the same source-reviewed icon as C-3.
- `ponchi-batch-006`: D-42 Gemma, D-51 Imagen, and D-53 Veo use the same
  official Google DeepMind icon as a review-pending organization icon overlay.
  The official Google DeepMind models page (`https://deepmind.google/models/`)
  lists Gemma, Imagen, and Veo as Google DeepMind models. Dedicated product
  lockups were not imported in this pass, so these overlays remain
  review-pending before final promotion.
- `ponchi-batch-006`: D-54 Stable Diffusion uses
  `assets/logos/stability-ai/stability-ai-white-dot-on-approved-blue-plate.png`,
  which centers the unchanged official white Stability AI header logo
  `assets/logos/stability-ai/stability-ai-white-dot-desktop.png` on an approved
  `#123E82` plate for white-canvas visibility. The source was the official
  Stability AI homepage (`https://stability.ai/`, asset
  `https://images.squarespace-cdn.com/content/v1/6213c340453c3f502425776e/a3485d53-7e65-42b5-bc62-e2e55f8409b9/stability-ai-white-dot-desktop.png`),
  retrieved 2026-06-03. A dedicated Stable Diffusion product logo was not
  confirmed, so this remains a review-pending organization overlay before final
  promotion.
- `ponchi-batch-005`: D-40 Llama 系 uses
  `assets/logos/llama/llama-official-favicon.svg` from the official Llama site
  (`https://www.llama.com/`, referenced as
  `https://static.xx.fbcdn.net/rsrc.php/yf/r/-7pQO6hUGK_.svg`), retrieved
  2026-06-03. The saved preload SVG
  `assets/logos/llama/llama-official-preload.svg` is the official Meta wordmark.
  No dedicated Llama product lockup was confirmed in this pass, so D-40 uses
  the official Meta organization icon as a review-pending overlay, not as a
  Llama-specific product logo.
- `ponchi-batch-003`: C-4 Meta AI uses
  `assets/logos/meta-ai/meta-ai-orbit-logo-gradient-3d_light.goto.png`, a
  Chrome-rendered PNG from the official
  `https://www.meta.ai/images/meta-ai-orbit-logo-gradient-3d_light.svg` asset,
  saved as `assets/logos/meta-ai/meta-ai-orbit-logo-gradient-3d_light.svg`.
  ImageMagick rendered the SVG as blank/white because of SVG mask handling, so
  the unchanged official SVG was opened directly in local Chrome and captured
  as a transparent PNG before deterministic overlay. Treat the purple/blue
  orbit mark as an official-asset color exception only inside the overlay
  rectangle.
- `ponchi-batch-003`: B-33 Canva uses
  `assets/logos/canva/Canva-logos/Canva logos/png/512x512/Canva type logo_512x180.png`
  from Canva's official developer brand guidelines package
  (`https://www.canva.dev/docs/connect/guidelines/brand/`, ZIP
  `https://www.canva.dev/assets/connect/Canva-logos.zip`), retrieved
  2026-06-03. Treat the cyan/blue/purple logo gradient as an official-asset
  color exception only inside the overlay rectangle.
- `ponchi-batch-010`: F-84 uses `assets/logos/ghostty/social-share-card.jpg`
  from the official Ghostty site (`https://ghostty.org/`, referenced as
  `https://ghostty.org/social-share-card.jpg`), retrieved 2026-06-03. The
  official social card is used as-is and scaled down; the Ghostty mark is not
  redrawn or recolored.
- `ponchi-batch-001`, `ponchi-batch-003`, and `ponchi-batch-005`: B-1, B-52,
  and D-1 - D-4 use `assets/logos/gemini/gemini_sparkle_4g_512_lt.png` from
  the official Gemini site (`https://gemini.google.com/`, referenced as
  `https://www.gstatic.com/lamda/images/gemini_sparkle_4g_512_lt_f94943af3be039176192d.png`),
  retrieved 2026-06-03. The matching official SVG
  `assets/logos/gemini/gemini_sparkle_aurora.svg` was also saved for source
  comparison; overlays use the PNG so gradient rendering stays faithful.
- `ponchi-batch-006`: D-55 Nano Banana uses the same official Gemini sparkle
  `assets/logos/gemini/gemini_sparkle_4g_512_lt.png` as a Gemini-family overlay.
  The entry identifies Nano Banana as the nickname for Gemini 2.5 Flash Image.
  A dedicated Nano Banana product logo was not confirmed, so this remains a
  review-pending family/organization overlay before final promotion.
- `ponchi-batch-006`: D-57 Flow uses
  `assets/logos/google-flow/flow_favicon_w_on-approved-blue-plate.png`, which
  centers the unchanged official white Flow favicon
  `assets/logos/google-flow/flow_favicon_w.png` on an approved `#123E82` plate
  for white-canvas visibility. The source was the official Google Labs Flow
  page (`https://labs.google/fx/tools/flow`, canonical `https://flow.google/`,
  asset `/fx/icons/favicon/flow_favicon_w.png`), retrieved 2026-06-03. A
  standalone Flow lockup was not confirmed, so this remains a review-pending
  official icon overlay before final promotion.
- `ponchi-batch-006`: D-58 Whisk uses
  `assets/logos/google-whisk/whisk_favicon_b.svg`, the official black Whisk
  favicon linked from the official Google Labs Whisk page
  (`https://labs.google/fx/tools/whisk`, asset
  `/fx/icons/favicon/whisk_favicon_b.svg`), retrieved 2026-06-03. A standalone
  Whisk lockup was not confirmed, so this remains a review-pending official
  icon overlay before final promotion.
- `ponchi-batch-002`: B-24 uses
  `assets/logos/google-cloud/google-cloud-logo-fullcolor.svg` from the official
  Google Cloud site (`https://cloud.google.com/`, referenced as
  `https://www.gstatic.com/cgc/google-cloud-logo-fullcolor.svg`), retrieved
  2026-06-03.
- `ponchi-batch-002`: B-27 uses
  `assets/logos/google-cloud/product-icons/core-products-icons/Unique Icons/Vertex AI/SVG/VertexAI-512-color.svg`,
  imported from the official Google Cloud Core Products Icons ZIP linked by
  `https://cloud.google.com/icons/`
  (`https://services.google.com/fh/files/misc/core-products-icons.zip`),
  retrieved 2026-06-03. Treat this as a review-pending product-icon overlay,
  not a generated logo.
- `ponchi-batch-002`: B-25 uses the official Azure-A service icon
  `assets/logos/azure/Azure_Public_Service_Icons_V23/Azure_Public_Service_Icons/Icons/other/10018-icon-service-Azure-A.svg`;
  B-26 uses the official Azure OpenAI service icon
  `assets/logos/azure/Azure_Public_Service_Icons_V23/Azure_Public_Service_Icons/Icons/ai + machine learning/03438-icon-service-Azure-OpenAI.svg`.
  Both were imported from the official Microsoft Azure Architecture Icons
  package (`https://learn.microsoft.com/en-gb/azure/architecture/icons/`, ZIP
  `https://arch-center.azureedge.net/icons/Azure_Public_Service_Icons_V23.zip`),
  retrieved 2026-06-03. Overlays use PNG previews rendered from those SVGs for
  sharper deterministic compositing.
- `ponchi-batch-002`: B-14 uses `assets/logos/genspark/genspark-favicon.ico`
  from the official Genspark site (`https://www.genspark.ai/favicon.ico`),
  retrieved 2026-06-03. The brand page lockup download still returned 403 from
  the local shell, so this favicon overlay remains review-pending.
- `semantic-regen-007`: B-15 Microsoft Copilot and B-16 Microsoft 365 Copilot
  use `assets/logos/microsoft-copilot/copilot-official-inline-icon.preview.png`,
  a local PNG preview rendered from the official Copilot inline icon asset
  saved under `assets/logos/microsoft-copilot/`. The generated bodies were kept
  logo-free and the official icon was composited deterministically after
  clearspace cleanup.
- `semantic-regen-008`: B-4 Cursor uses the official Cursor horizontal lockup
  `assets/logos/cursor/cursor-brand-assets/General Logos/Lockup Horizontal/PNG/LOCKUP_HORIZONTAL_2D_LIGHT.png`.
  B-7 Claude Code uses the official Claude Code Slate logo
  `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/Claude logos/2 Claude Code logo/PNG/Claude Code logo - Slate.png`.
  Both generated bodies were kept logo-free and the official assets were
  composited deterministically after clearspace cleanup.

All of these overlays were generated deterministically from local official
assets, primarily by `scripts/composite_official_logo.py`; AMD uses an
equivalent ImageMagick composite so the official white logo remains visible on
the white ponchi canvas. They are staged under
`assets/ponchi/final_candidates/` and do not overwrite `assets/ponchi/final/`.

- `ponchi-simplification-rollout-007`: H-57 Gemini の命名史 uses the same
  unchanged official Gemini sparkle at `assets/logos/gemini/gemini_sparkle_4g_512_lt.png`
  verified from `https://gemini.google.com/`; source and 2026-06-03 retrieval are
  recorded above for B-1/B-52/D-1-D-4. Add the verified asset SHA to the sidecar.
  Historical-generation timeline use conditions remain pending, so no overlay,
  adoption, or publication; an eligible simplified base remains logo-free.
