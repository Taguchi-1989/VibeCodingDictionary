# コンポーネント分解仕様 v2（iter 22 / 2026-04-25）

> **⚠️ 実装前に必読（2026-08-09 追記）**: 本書のコンポーネント分解は iter 22 時点の `typescript_spread.html` を基にしており、その後レイアウトが 3 点進化しています。**実装の正は `scripts/preview_gen.py` の出力**（= `drafts/prototypes/preview/*.html`）で、差分は次のとおりです。
>
> 1. 左ページ: Before/After 図＋擬人化ポンチ絵の 2 枠 →「イメージ」**1 枠に統合**（`assets/ponchi/final/*.webp` を差し込み）
> 2. **開発フローでの位置は右ページ → 左ページ下段へ移動**
> 3. 右ページ下段: 4:6 の 2 カラム → つまずき／コメントの**全幅縦スタック**。関連用語 → **備考カード** → 参考 URL の順
>
> 最新の紙面構造は [v2_rules_summary.md](v2_rules_summary.md) §1（v2.29 で同期済み）を参照してください。本書の §0（スタック）・命名・データフローの方針は引き続き有効です。

*実装担当（静的サイト生成器側）への引き渡し資料。現行の [typescript_spread.html](../drafts/prototypes/mockups/design_philosophy_v2/typescript_spread.html) と [overlay.css](../drafts/prototypes/mockups/design_philosophy_v2/overlay.css) を、どう**再利用可能なコンポーネント**に分解し、[entry_schema.yaml](entry_schema.yaml) と [entries.csv](../ledgers/entries.csv) から 335 エントリ分のスプレッドを自動生成するか、の仕様。*

---

## 0. スタック（確定）

**採択: Astro + React コンポーネント（ハイブリッド）**（2026-04-25 著者判断）

採択理由:

- React の書き味（props・hooks・TypeScript）を**コンポーネント本体に残す**
- ページ生成・routing・markdown ロードは **Astro の静的出力**で担う（書籍化 PDF が綺麗）
- `@astrojs/react` を入れるだけで `.astro` ファイルから React コンポーネントを呼べる
- 実装担当が React 慣れの場合でも違和感が最小

### 0-1. 主要パッケージ

```json
{
  "dependencies": {
    "astro": "^5",
    "@astrojs/react": "^4",
    "react": "^19",
    "react-dom": "^19"
  },
  "devDependencies": {
    "typescript": "^5",
    "zod": "^3",            // entry_schema.yaml → Zod スキーマに変換して frontmatter 型付け
    "@astrojs/check": "^0"  // TS チェック
  },
  "optionalDependencies": {
    "pagedjs-cli": "^0"     // PDF 生成
  }
}
```

### 0-2. 想定ディレクトリ構成

```text
/
├── content/entries/              ← markdown（本プロジェクトが維持）
├── ledgers/chapters.yaml         ← 章マップ（本プロジェクトが維持）
├── ledgers/entries.csv           ← エントリ全件（path 列つき、自動同期）
├── docs/entry_schema.yaml        ← 単一真実点（generator + validator 共有）
│
├── site/                         ← 実装担当がここに置く
│   ├── astro.config.mjs          ← @astrojs/react を有効化
│   ├── src/
│   │   ├── content/
│   │   │   ├── config.ts         ← entry_schema.yaml → Zod
│   │   │   └── entries/          ← シンボリックリンク or glob で content/entries を参照
│   │   ├── components/           ← React primitive（tsx）
│   │   │   ├── primitive/
│   │   │   │   ├── PageChromeTop.tsx
│   │   │   │   ├── TitleHero.tsx
│   │   │   │   ├── TaglineBar.tsx
│   │   │   │   ├── BodySection.tsx
│   │   │   │   ├── FigureBeforeAfter.tsx
│   │   │   │   ├── FigureStructure.tsx
│   │   │   │   ├── FigureComparison.tsx
│   │   │   │   ├── FigureWorkflow.tsx
│   │   │   │   ├── FigureTimeline.tsx
│   │   │   │   ├── PonchiSlot.tsx
│   │   │   │   ├── SeepointGrid.tsx
│   │   │   │   ├── FlowRow.tsx
│   │   │   │   └── RelatedRow.tsx
│   │   │   ├── section/
│   │   │   │   ├── PageLeft.tsx
│   │   │   │   └── PageRight.tsx
│   │   │   ├── EntrySpread.tsx   ← 1 エントリ見開き全体
│   │   │   └── DrawerNav.tsx     ← ハンバーガー（chapters.yaml + entries.csv から生成）
│   │   ├── layouts/
│   │   │   └── SpreadLayout.astro  ← <html> + <head> + <EntrySpread entry={entry} />
│   │   ├── pages/
│   │   │   ├── index.astro         ← トップ（章別目次）
│   │   │   ├── entries/[id].astro  ← 動的ルート、getStaticPaths で 335 URL 生成
│   │   │   └── book.astro          ← 全エントリ連結（Paged.js で PDF 化）
│   │   └── styles/
│   │       └── overlay.css         ← drafts/prototypes から移植
│   └── public/                     ← フォント・擬人化イラスト（後日差し込み）
│
└── dist/                           ← Astro build 出力（Web 静的 HTML）
└── dist/book/vibe.pdf              ← Paged.js 出力（書籍用）
```

### 0-3. Astro ← React 呼び出しのイメージ

```astro
---
// src/pages/entries/[id].astro
import { getCollection } from 'astro:content';
import SpreadLayout from '../../layouts/SpreadLayout.astro';
import EntrySpread from '../../components/EntrySpread';

export async function getStaticPaths() {
  const entries = await getCollection('entries');
  return entries.map(entry => ({
    params: { id: entry.data.id },
    props: { entry },
  }));
}

const { entry } = Astro.props;
---
<SpreadLayout title={entry.data.title}>
  <EntrySpread entry={entry.data} body={entry.body} />
</SpreadLayout>
```

`EntrySpread` は React コンポーネントなので、props は型安全・内部は hooks/memo で最適化可能。Astro は「静的 HTML を吐く骨格」として働き、hydration は必要な部分（ドロワー開閉など）だけ `client:load` で。

### 0-4. 不採択となった選択肢

- **Astro 純**: React 経験者にとって `.astro` 記法の学習コストが無視できない
- **Next.js SSG（`output: 'export'`）**: hydration JS が残り Paged.js での PDF 化時に不要な調整が発生。将来 Web 機能拡張時の柔軟性は魅力だが、書籍化第一の本プロジェクトでは過剰

---

## 1. 入力と出力

### 1-1. 入力

| 種別 | パス | 用途 |
|---|---|---|
| エントリ本体 | `content/entries/**/*.md` | 1 エントリ = 1 md = 1 スプレッド |
| 章定義 | `ledgers/chapters.yaml` | letter → ラベル／カテゴリ／ディレクトリ |
| エントリインデックス | `ledgers/entries.csv` | 全 335 エントリのメタ情報・path |
| スキーマ | `docs/entry_schema.yaml` | 節の文字数ルール／必須節／enum |
| スタイル | `drafts/prototypes/mockups/design_philosophy_v2/overlay.css` | **そのまま再利用**（primitive のみの構造） |
| リファレンス実装 | `drafts/prototypes/mockups/design_philosophy_v2/typescript_spread.html` | レイアウトの唯一の見本 |

### 1-2. 出力

| 種別 | パス（提案） | 備考 |
|---|---|---|
| Web サイト | `dist/` or `.vercel/` | 各エントリ 1 URL、ハンバーガー付き |
| 書籍 PDF | `dist/book/vibe_coding_dictionary.pdf` | Paged.js 等で生成、見開き左右ノド非対称 |
| 索引／目次 | `dist/index.html`, `dist/toc.html` | entries.csv から自動生成 |

---

## 2. コンポーネント分解マップ

### 2-1. 粒度

「**ページ → セクション → primitive**」の 3 層で分ける。primitive は再利用可能な原子部品、セクションは左右ページの節、ページは 2 ページ 1 スプレッドのトップコンテナ。

### 2-2. 全 primitive 一覧（14 個）

| # | コンポーネント名 | 現行 CSS セレクタ | 主な props | 用途 |
|---|---|---|---|---|
| 1 | `<PageChromeTop>` | `.page-chrome-top` | leftLabel / pageNumber / bookIcon | 上チロム（章ラベル＋ページ番号） |
| 2 | `<PageChromeBottom>` | `.page-chrome-bottom` | leftFoot / rightFoot | 下チロム（iter 22 で左右非対称） |
| 3 | `<TitleHero>` | `.title-hero` | text | 左ページ大タイトル 96px |
| 4 | `<TaglineBar>` | `.tagline-bar` | text | 青帯タグライン |
| 5 | `<TagChip>` | `.tag-chip` | icon / text | 体験区分／読者レベル 2 ピル |
| 6 | `<BodySection>` | `.body-section` | icon / heading / body | 本文節（何を／どこで） |
| 7 | `<SectionHeading>` | `.section-heading .label` | label | 青バー＋ラベルの小見出し |
| 8 | `<FigureBeforeAfter>` | `.figure-ba` | before / after / caption1 / caption2 | Before/After 二層カード |
| 9 | `<PonchiSlot>` | `.ponchi-slot` | icon / title / hint / todoLabel | メインビジュアル枠（iter 22 で拡大） |
| 10 | `<SeepointGrid>` | `.seepoint-grid` | cells[6] | 6 視点グリッド |
| 11 | `<SeepointCell>` | `.seepoint-cell` | num / icon / title / body | 6 視点セル 1 枚 |
| 12 | `<BottomRow>` | `.bottom-row` | leftBlock / rightBlock | 4:6 下段 2 カラム |
| 13 | `<FlowRow>` | `.flow-row` | steps[4..5] | 開発フロー横並び |
| 14 | `<RelatedRow>` | `.related-row` | pills[3..5] | 関連用語ピル |

### 2-3. セクション層（6 個）

| # | セクション名 | 含む primitive | 対応 markdown 節 |
|---|---|---|---|
| 1 | `<PageLeftHeader>` | TitleHero + TaglineBar + TagRow | YAML title / `## tagline` / YAML タグ |
| 2 | `<PageLeftBody>` | BodySection × 2 + FigureBeforeAfter + PonchiSlot | `## 何をしてくれるか` / `## どこで出会うか` / `## メイン図` / `## 誌面ポンチ絵メモ`（caption のみ抽出） |
| 3 | `<PageRightTop>` | SeepointGrid | `## この用語の見どころ` ＋ 6 subsection |
| 4 | `<PageRightMiddle>` | BottomRow（つまずき / コメント） | `## 非エンジニアのつまずき` / `## 私のコメント` |
| 5 | `<PageRightFlow>` | FlowRow | `## 開発フローでの位置（必須）` |
| 6 | `<PageRightFooter>` | RelatedRow + ReferencesRow | `## 関連用語` / `## 出典メモ` 先頭 URL |

### 2-4. ページ層（2 個）

| # | ページ名 | 構成 |
|---|---|---|
| 1 | `<SpreadLeft>` | PageChromeTop + PageLeftHeader + PageLeftBody + PageChromeBottom |
| 2 | `<SpreadRight>` | PageChromeTop + PageRightTop + PageRightMiddle + PageRightFlow + PageRightFooter + PageChromeBottom |

### 2-5. トップ層（1 個）

| # | 名前 | 役割 |
|---|---|---|
| `<EntrySpread>` | 1 エントリ = SpreadLeft + SpreadRight を横並びで出力（A4 見開き想定） |

---

## 2-6. figure_type 別 primitive（iter 22 / 2026-04-25 検証で追加）

B-3 ChatGPT（structure）を既存テンプレで描画してみた結果、**Before/After 以外の 4 種類の primitive が必要**と判明（[b3_chatgpt_spread.html](../drafts/prototypes/mockups/design_philosophy_v2/b3_chatgpt_spread.html) で確認）。overlay.css にスケッチ段階の CSS を常設化済。実装担当はこれを下書きとして正式版を作る。

| figure_type | CSS class | 構成 | 主な props |
|---|---|---|---|
| **before_after** | `.figure-ba` | 左右 2 カード + 矢印 + キャプション 2 本 | `beforeLabel` / `beforeCode` / `afterLabel` / `afterCode` / `captionBefore` / `captionAfter` |
| **structure** | `.figure-structure` | 中央ハブラベル + 3〜4 ノードカード + 下支えバー | `hubLabel` / `cards: [{title, body}]` / `baseLabel?` / `--st-cols-count` CSS var |
| **comparison** | `.figure-comparison` | 2〜4 列の縦比較。`--highlight` で推奨列強調 | `columns: [{head, rows, highlight?}]` / `--cp-cols-count` CSS var |
| **workflow** | `.figure-workflow` | ステップボックス + 矢印、横スクロール可 | `steps: [{title, body}]`（4〜6） |
| **timeline** | `.figure-timeline` | 横軸 + 点列 + 日付／ラベル | `events: [{date, label}]`（3〜6） |

### 2-6-1. 描画ルール

- **共通コンテナ `.figure`**: 青枠＋角丸＋ padding 18px/16px＋上 margin 6px
- **タイトル下段**: `.figure` の直上に `<div class="section-heading"><span class="label">{図タイトル}</span></div>` を置く。図のタイトル（「Before/After」「3 つの入口」等）は図ごとに自由
- **色トークン**: `--ink-blue` 主青、`--ink-blue-100` 淡青塗り、`--paper-2` セル下地
- **印刷対応**: primitive ごとの高さは概ね 180〜240px。当初設計ではポンチ絵スロット（iter 22 の 340px）との合算で左ページが 1061px に収まる想定だったが、2026-04-28 に実描画が 1424 px に膨らんでいることが判明。**ポンチ絵を旧サイズ（150 / icon 96）に戻し、preview 専用 `overlay-tight.css`（構造図とポンチ絵の枠線融合・6 視点グリッド圧縮・各種余白削減）を新設して 1061px に再収束**（W 案、[v2_rules_summary §4](v2_rules_summary.md#4-ビジュアルトークンcss-側の確定値) 参照）。実装担当は overlay-tight のルールを Paged.js 側でどう扱うか検討してください
- **data 属性**: 実装担当はカード数を `--st-cols-count: 4;` のような CSS カスタムプロパティで外から制御できるようにする

### 2-6-2. 開発フロー（`.flow-row`）の幅ルール

B-3 ChatGPT は 5 ステップを組んだところ、4 ステップ前提で書かれた旧 `.flow-step` だと窮屈だった。iter 22 で以下を確定:

- **推奨 4 ステップ**（誌面が最も美しく収まる）
- **許容 5 ステップ**（入れる場合は flex-basis:0 で等分、5 本目のラベルを 13px に自動縮小）
- **禁止 6 ステップ以上**（横幅破綻。縦並びへの切替や図を分けることを検討）

CSS は overlay.css に設定済み:

```css
.flow-row { display: flex; gap: 6px; flex-wrap: nowrap; }
.flow-row .flow-step { flex: 1 1 0; min-width: 0; }
.flow-row:has(.flow-step:nth-child(9)) .flow-label { font-size: 13px; }
```

`:has()` は Safari 15.4 以降・Chrome 105 以降で動作。対応しない環境向けには JS で step 数カウント → class 付与の代替も用意する。

---

## 3. props 仕様（TypeScript 風）

```ts
// エントリ 1 件全体の入力
interface Entry {
  id: string;                       // "F-1"
  title: string;                    // "TypeScript"
  category: string;                 // "term"
  subtype?: string;                 // "language"
  experienceLevel: 'hands_on' | 'partial' | 'research_only';
  readerLevel: string;              // "2-3"
  figureType: 'before_after' | 'structure' | 'comparison' | 'workflow' | 'timeline';
  evaluationDate: string;           // "2026-04-25"
  versionStatus?: 'active' | 'preview' | 'deprecated';
  pricingNote?: 'none' | 'paid' | 'freemium';
  status: 'drafting' | 'sample' | 'needs_source' | 'needs_review' | 'ready' | 'archived' | 'candidate';
  relatedTerms: string[];           // 3-5 items

  // 本文（markdown 節から抽出）
  tagline: string;
  nanishiteku: string;
  dokodeDeau: string;
  mainFigure: MainFigure;           // figureType によって discriminated union
  ponchi: {
    icon?: string;                  // 後日差し込み。初期は placeholder SVG
    title: string;                  // "TypeScript を使う人"
    caption: string;                // 30-80 字
  };
  seepoint: [Cell, Cell, Cell, Cell, Cell, Cell];
  tsumazuki: string[];              // length 3 (固定)
  watashinoComment: [Comment, Comment, Comment, Comment];  // first/good/bad/who 固定
  kaihatsuFlow: FlowStep[];         // length 4..5
  referencesUrl?: { url: string; checkedDate: string };

  // ナビ用メタ
  chapter: ChapterMeta;             // chapters.yaml から引く
  prev?: EntryNav;                  // 前エントリへのリンク
  next?: EntryNav;                  // 次エントリへのリンク
}

interface Cell {
  num: 1 | 2 | 3 | 4 | 5 | 6;
  title: string;                    // "役割" 等
  body: string;                     // 15-40 (1-5), 15-50 (6)
}

interface Comment {
  label: '第一印象' | '良い点' | 'ダメな点' | '誰向けか';
  body: string;                     // 10-40 字
  badge: '★' | '✓' | '!' | '☺';    // ラベルから導出
}

interface FlowStep {
  icon: string;                     // SVG パス or アイコン名
  label: string;                    // 3-15 字
  note?: string;                    // 20 字以内の補足
}

type MainFigure =
  | { type: 'before_after'; before: CodeBlock; after: CodeBlock; captionBefore: string; captionAfter: string }
  | { type: 'structure'; nodes: Node[]; edges: Edge[] }
  | { type: 'comparison'; columns: Column[] }
  | { type: 'workflow'; steps: Step[] }
  | { type: 'timeline'; events: Event[] };
```

---

## 4. 生成器が担う責務

### 4-1. markdown → Entry オブジェクト変換

1. `content/entries/**/*.md` を読む
2. フロントマターを `entry_schema.yaml:frontmatter` に照らして型チェック
3. 各 H2 / H3 節の本文を文字数検証し、Entry オブジェクトに詰める
4. `ledgers/chapters.yaml` を引いて chapter メタをマージ
5. `ledgers/entries.csv` の並び順に従って prev / next リンクを解決

### 4-2. 静的 HTML 生成

- 各 Entry について `<EntrySpread>` を描画、1 URL（例: `/entries/F-1/`）に出力
- トップページ (`/`) は章別目次（chapters.yaml の順）
- 索引 (`/index/`) は 50 音／ID ソートの一覧
- ハンバーガーナビは全エントリ共通の partial として entries.csv から毎回生成

### 4-3. PDF 生成（書籍化）

- Paged.js で見開きレイアウト
- 想定 `@page { size: 150mm 212mm; }`（A 系 √2 準拠、750×1061px の実寸近似）。preview 段階では `@page 199mm 281mm` ＋ `overlay-tight.css`（W 案）で 750×1061px を維持しているため、Paged.js 側では (a) `overlay-tight.css` のルールを正式化して 150×212mm にスケール、または (b) 別の縮小戦略を採用、を実装担当が選択する
- ノド非対称 margin を `@page :left` / `@page :right` で制御
- PDF/X-1a 出力は印刷所に依存（次の段階で検討）

---

## 5. 未確定事項・実装担当への問い

| # | 問い | 影響 |
|---|---|---|
| 1 | 擬人化ポンチ絵の実イラストをいつ差し込むか？ | 現在は placeholder SVG。本番は書籍化前に差し替え |
| 2 | figure_type ごとの主要図（メイン図）を markdown から再現できるか？ | Before/After はコード対比なので再現可、structure / timeline は図生成の仕様設計が別途必要 |
| 3 | 検索・フィルタ（Web 版）のスコープ | MVP は全文検索なし。目次／章／索引のみで十分 |
| 4 | ダークモード | 本書では不要。書籍化の純白紙面前提 |
| 5 | A/B テスト的な複数レイアウト | `page_layout: spread_v1` 固定。将来的な `spread_v2` は番号で分岐予約 |

---

## 6. 実装開始時のチェックリスト（C: Astro + React 前提）

### 6-1. セットアップ

- [ ] `site/` を作り `npm create astro@latest` で初期化
- [ ] `npx astro add react` で `@astrojs/react` を導入、`astro.config.mjs` に `integrations: [react()]` が入ることを確認
- [ ] `npm install zod` — frontmatter 型付け用
- [ ] `site/src/content/entries` を `content/entries` のシンボリックリンクまたは Astro の `contentDir` 設定で紐付け

### 6-2. スキーマ変換

- [ ] `docs/entry_schema.yaml` の `frontmatter` セクションを `site/src/content/config.ts` に Zod スキーマとして転記。値のズレが出たときは YAML 側を正にする
- [ ] `content collections` の `defineCollection({ schema })` で `getCollection('entries')` が型安全に動くことを確認

### 6-3. コンポーネント移植

- [ ] `overlay.css` と `base.css` を `site/src/styles/` へ移植。デザイントークン（`--ink-blue` 等）は CSS 変数のまま維持
- [ ] `typescript_spread.html` の DOM 構造を §2-2 の 14 primitive に分解し、`site/src/components/primitive/` 以下に `.tsx` で配置
- [ ] 5 種類の figure primitive（before_after / structure / comparison / workflow / timeline）を §2-6 の仕様で実装。overlay.css のスケッチクラスをベースに調整
- [ ] `EntrySpread` で figure_type に応じて discriminated union で primitive を出し分け

### 6-4. ページ生成

- [ ] `src/pages/entries/[id].astro` で `getStaticPaths` により 全 active エントリの静的 URL を生成
- [ ] `src/pages/index.astro` で章別目次（chapters.yaml の順）
- [ ] `src/pages/book.astro` で 全エントリ連結（Paged.js で PDF 化用）
- [ ] `DrawerNav` は `chapters.yaml` + `entries.csv` を build time で読み込み、static に生成

### 6-5. 検証

- [ ] 現存 22 active エントリを generator で描画し、`typescript_spread.html` と pixel diff で一致を確認（`playwright` test で差分 <5% 等）
- [ ] 著者記入欄（非エンジニアのつまずき／私のコメント）が空欄でも描画できる
- [ ] Paged.js で PDF 出力し、A4 実寸プレビューで見開きノド非対称 margin が正しいことを確認
- [ ] Web 版（`dist/`）と PDF 版（`dist/book/vibe.pdf`）の両方が CI で吐ける

### 6-6. 引き渡しのゴール

以下を担当ごとに整理:

- **本プロジェクト（markdown 執筆側）**: `content/entries/`・`ledgers/`・`docs/entry_schema.yaml` の維持
- **実装担当（site/ 側）**: `site/` の Astro + React 実装・Paged.js・CI/CD
- **共通**: `docs/v2_rules_summary.md` と `docs/entry_schema.yaml` は**両担当が同じ内容を読む**。差分があれば YAML 側を正とし、summary を追随させる

---

## 7. 本プロジェクト（markdown 執筆側）の責任範囲

本プロジェクトの Claude Code は以下を維持する:

- markdown エントリの品質（[scripts/validate_entry.py](../scripts/validate_entry.py) / check_entry.py でゼロ違反）
- `ledgers/entries.csv` の状態同期（[scripts/sync_entries_csv.py](../scripts/sync_entries_csv.py)）
- [docs/v2_rules_summary.md](v2_rules_summary.md) と本仕様・entry_schema.yaml の三者整合
- iter 22 以降のレイアウト変更議論（本書内で完結）

**CSS / TSX / ビルド設定・Paged.js 調整**は実装担当のスコープ。
