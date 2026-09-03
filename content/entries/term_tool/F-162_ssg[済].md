---
id: F-162
title: SSG
title_reading: エスエスジー
category: term_tool
subtype: web_foundation
experience_level: partial
reader_level: 2-3
importance: D
figure_type: comparison
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - SSR
  - Astro
  - Cloudflare Pages
  - Netlify
status: ready
---

# SSG

## tagline

Static Site Generation の略。ビルド時に HTML を生成し、CDN から静的ファイルで配信する方式です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

ビルド実行時にすべてのページを HTML として書き出し、その静的ファイルをそのまま配信します。リクエストのたびにサーバで処理する必要がなく、表示速度が極めて速くなります。

## どこで出会うか

Hugo・Jekyll・Astro などのフレームワーク設定や Vercel / Cloudflare Pages へのデプロイ手順で目にします。AI が作ったブログを公開するときの選択肢として登場します。

## メイン図

### 図の狙い

SSG（ビルド時生成）と SSR（リクエスト時生成）の違いを、処理タイミングの対比で示す。

### B. 登場シーン（figure_type: comparison）

- シーン1: SSG — ビルド時に全 HTML を生成 → CDN に配置 → 閲覧者はファイルを受け取るだけ
- シーン2: SSR — 閲覧者がアクセス → サーバが HTML を都度生成 → 返却
- シーン3: SSG 向き用途 — ブログ・ドキュメント・LP など更新頻度が低いページ
- 並べる基準（誰視点か、用途か、時系列か）: 処理タイミングの違いを時系列で並べる


## 会話での使い方例

「ブログとドキュメントは SSG にして、Cloudflare Pages にぽんと置きました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

ビルド時に HTML を生成し、CDN 配信だけで完結させます。

### 2. うれしさ

サーバ負荷ゼロで表示が速く、CDN だけで運用できます。

### 3. 注意点

ページ数が増えるとビルド時間が長くなります。

### 4. どこで役立つか

更新頻度が低いブログ・LP・ドキュメントに向きます。

### 5. はじめに

SSR との違い（生成タイミング）を押さえるのが最初の一歩です。

### 6. 深掘り先

SSR, ISR, Astro


## 開発フローでの位置（必須）

1. コンテンツ作成 — Markdown や CMS でページのソースを用意します
2. ビルド実行 — フレームワーク（Astro・Hugo 等）が全ページを HTML に変換します
3. 静的ファイル配置 — 生成した HTML を CDN（Cloudflare Pages / Netlify）にデプロイします
4. 閲覧者アクセス — CDN がキャッシュ済みファイルをそのまま返し、表示が完了します


## 関連用語

- SSR
- Astro
- Cloudflare Pages
- Netlify


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 更新頻度の低いページのはずなのに、ビルド対象が膨らむと負荷が大きくなります。
- 継続運用でビルドコストが膨らみ、Vercel Pro などの料金で痛い目を見ます。
- ベストプラクティスもプロジェクト次第で変わり、最適解を見つけづらいです。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 小さいプロジェクトならこれで進めるのが良さそうだ、と感じました。
- 👍 良い点: Vercel のホビープランで無料運用でき、立ち上げが軽いところが嬉しいです。
- 👎 ダメな点: Pro プランになるとビルド回数だけで料金がかさみ、運用設計が必要です。
- 👥 誰向けか: 継続的に運用する人向けで、規模拡大時のコスト設計が肝になります。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: SSG と SSR の処理フローを左右に並べた比較図。SSG 側は「ビルド時」→「CDN」→「閲覧者」、SSR 側は「閲覧者リクエスト」→「サーバ処理」→「HTML 返却」の流れ
- 登場人物（いれば）: 左に開発者（ビルドを実行する人）、右に閲覧者（サイトを見る人）
- 吹き出し・心の声: 開発者「ビルドしておいたよ」、閲覧者「速い！」
- 中央に置くキーワード/ラベル: SSG vs SSR
- Before / After の場合の対比ポイント: SSG はリクエスト時に処理ゼロ、SSR は都度処理が発生

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 文書アイコン（コンテンツ作成）
- Step 2 のアイコン/絵柄: 歯車アイコン（ビルド実行）
- Step 3 のアイコン/絵柄: クラウドアイコン（CDN デプロイ）
- Step 4 のアイコン/絵柄: ブラウザアイコン（閲覧者アクセス）
- 矢印で示す流れの意図: コンテンツ → ビルド → 配置 → 表示の一方向フロー


## コミュニティ補完メモ

- SSR（F-161）との住み分け：F-162 は「事前生成 → CDN 配信」の静的方式に集中。動的データが必要な場面は F-161 SSR へ誘導する。ISR（Incremental Static Regeneration）は SSG と SSR の中間で、本エントリの「深掘り先」に含める
- Astro（F-17）との住み分け：F-17 はフレームワーク自体の解説。F-162 は SSG という方式の概念説明に集中し、Astro は「SSG の代表的ツール」として言及するにとどめる
- Cloudflare Pages（F-22）・Netlify（B-21）は配信インフラ側。本エントリは「何を配置するか（静的ファイル）」の説明にとどめ、配信の詳細は各エントリへ

## 出典メモ

- Next.js 公式ドキュメント "Static Site Generation" — checked 2026-04-30
- Astro 公式ドキュメント "Build your Astro site" — checked 2026-04-30
- Cloudflare Pages ドキュメント "Static sites" — checked 2026-04-30


## 備考

- ビルド時間問題の緩和策として ISR（Incremental Static Regeneration）がある。Next.js の `revalidate` オプションが代表例。本エントリでは「SSG + 一部動的更新」として深掘り先に置く
- Hugo や Jekyll は古参の SSG ツールで、特に Jekyll は GitHub Pages と密接な関係がある
- 本書のレンダリング基盤も Astro + SSG 方式で生成予定
