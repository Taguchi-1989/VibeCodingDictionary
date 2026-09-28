# ポンチ絵・簡素化プロンプト v1.1

作成日: 2026-09-27  
状態: A-6試行で見つかったレイアウト指定漏れを補う改訂案。独立レビューと次のバッチでの検証待ち。

## 目的

現行画像の意味を保ち、確認済みの重複・微細要素だけを減らす image-edit 用テンプレートです。既存pilot-001の各プロンプトは生成履歴なので変更しません。C-9、D-12など意味確認中の項目は、人が `INTENDED_MEANING` を確定するまで候補を作りません。

## 生成前の必須入力

次の情報はプロンプトと同じ場所にある sidecar に記録します。未記入や不一致があれば生成を止めます。

- `ENTRY_ID` / `ENTRY_TITLE`: 管理用。画像にタイトルを描かせない。
- `SOURCE_IMAGE_PATH` / `SOURCE_IMAGE_SHA256` / `SOURCE_IMAGE_VERSION`: 編集対象そのものの識別情報。現在の正本、または明示した候補版を固定する。
- `INTENDED_MEANING`: 人が確定した1文。曖昧なら保留する。
- `LAYOUT_AND_READING_ORDER`: 人が確定した配置・読み順。人手ブリーフが配置を指定していない場合だけ `source` とし、元画像の構図と読み順を保つ。ブリーフと元画像に食い違いがあれば、どちらを優先するか明記する。未解決なら生成を保留する。
- `MUST_KEEP`: 消すと意味が変わる要素・関係・人物・構図群。
- `REMOVE`: 人が確認した削除対象を具体的に記す。
- `BRAND_AUDIT_RECORD`: `docs/brand_usage_audit.md` の該当ブランド項目と、項目別ブランド要件台帳の行。ブランド名・公式素材の状態・使用条件を特定する。
- `OFFICIAL_ASSET_PATH` / `OFFICIAL_ASSET_SHA256` / `OFFICIAL_ASSET_SOURCE_URL` / `OFFICIAL_ASSET_RETRIEVED_AT` / `USE_CONDITIONS_STATUS`: 公式素材を使う項目では記録する。ローカル公式素材を未取得、公式ソース未確認、または出典を特定できない場合は `blocked_brand_asset` として、項目別プロンプトも画像候補も作らない。
- `LOGO_MODE`: `reserve_official_asset` / `internal_base_only` / `not_required`。タイトルに会社・製品・モデル名がある場合は公式素材対象として扱う。`reserve_official_asset` は素材を取得して上記情報を記録し、使用条件が対象用途について確認済みの場合だけ選ぶ。素材は取得済みだが使用条件が未確定で、意味・元画像・削除対象も確定し、内部候補の比較が計画上許可されている場合だけ `internal_base_only` とする。この状態ではベース候補の生成までに止め、公式素材を合成せず、採用・公開に進めない。`not_required` はブランド要件台帳に明示的な根拠がある場合だけ選ぶ。分類や生成可否が曖昧ならプロンプトを作らず保留する。
- `LOGO_RECT`: 公式lockupを後合成する場合のロゴ本体矩形 `[x,y,w,h]`。標準は幅520px、`x=686`, `y=36`、右余白48px。高さは公式素材の縦横比から算出する。
- `LOGO_CLEARSPACE_RECT`: `reserve_official_asset` / `internal_base_only` のとき、レビュー用1254×627画像で図・人物・模様を置かない予約矩形 `[x,y,w,h]`。実際に使うlockupに合わせて毎回寸法を記録する。標準幅520pxの場合は `[686,0,520,180]` を初期値とし、必要に応じて幅520–580px・高さ150–220pxの範囲で調整する。幅を `w` に変える場合は `x=1254-48-w` とし、公式ロゴ本体の座標 `x=1254-48-logo_width` と混同しない。
- `CHARACTER_POLICY`: 入力画像にいる固定キャラクターの人数・役割・扱い。追加が必要なときは参照画像を明示する。
- `OUTPUT_PATH` / 使用モデルと生成日時: 出力の由来を追跡する。

編集入力はロゴ合成前のベース画像に限定します。合成済みロゴ画像をimage-editへ渡しません。現在のベース画像と履歴の画像を特定できない場合は、元画像を確定してから始めます。`internal_base_only` は公式素材を取得・特定済みだが使用条件の確認が残る場合の内部候補専用で、公式ロゴの合成・採用・公開を許可しません。

## 共通 image-edit プロンプト

```text
Edit only the exact logo-free base image attached as the reference.
ENTRY_ID: {ENTRY_ID}
ENTRY_TITLE: {ENTRY_TITLE} (context only; do not draw these words)
SOURCE_IMAGE_PATH: {SOURCE_IMAGE_PATH}
SOURCE_IMAGE_SHA256: {SOURCE_IMAGE_SHA256}
SOURCE_IMAGE_VERSION: {SOURCE_IMAGE_VERSION}

INTENDED MEANING (human-confirmed):
{INTENDED_MEANING}

LAYOUT AND READING ORDER (human-confirmed; preserve exactly):
{LAYOUT_AND_READING_ORDER}

MUST KEEP:
{MUST_KEEP}

REMOVE ONLY THESE CONFIRMED REDUNDANT DETAILS:
{REMOVE}

Preserve the exact 2:1 canvas. Follow LAYOUT_AND_READING_ORDER exactly. If it specifies positions, stacking, grouping, or reading order, retain them; do not reflow a vertical stack into a row or a row into a stack. If it says `source`, preserve the source image's established subject placement and reading order. When the source and human-authored brief disagree, follow only the precedence explicitly recorded in LAYOUT_AND_READING_ORDER; if precedence is unresolved, stop instead of choosing a new layout. Keep every element and relationship listed under MUST KEEP. Remove only the details listed under REMOVE. Do not invent facts or imply a new relationship.

Reduce visual clutter by removing confirmed redundant details and making the remaining essential forms easier to distinguish at 200px thumbnail width. Enlarge the remaining important forms where needed; do not compress many tiny details into the same space.

Make the visual hierarchy clear, but keep independent groups or panels separate whenever their separation carries meaning. Do not merge distinct stages, categories, comparisons, or groups to force a single focal group. A concept may require more than four forms; semantic accuracy and the MUST KEEP list take priority over a fixed count.

Do not add people, robots, cards, panels, arrows, stages, labels, data points, examples, or decorations unless they are explicitly listed under MUST KEEP. Do not remove or redesign a fixed series character that appears in the source unless the human-confirmed REMOVE list explicitly says so.

SERIES STYLE
- Minimal editorial line illustration for a Japanese technical book.
- Wide 2:1 landscape on a pure white #FFFFFF background.
- Use the author-approved palette for diagrams and backgrounds: white #FFFFFF, deep navy #123E82, near-black #1A1A1A, and pale blue #EAF1FB. Do not add gray or any other hue to them. Exception: preserve only neutral gray clothing/body areas already present on a fixed series character in the source image or its attached approved reference; do not add new gray regions or shades. Official asset colors are applied later as a separate unchanged asset.
- Prefer clean flat fills and uniform linework. Gradients are permitted only within the navy-to-pale-blue range; use them sparingly. Never introduce another hue.
- No texture, grain, speckles, decorative or ambient glow, drop shadows, glossy 3D, or decorative background. Preserve only blue active accents already visible on the source image or on an attached approved reference. Do not add halos or glow lines unless an attached reviewed reference explicitly shows them.
- Keep the core meaning clear at 200px thumbnail width.

BRAND AND TEXT
- Never generate or imitate a company/service/product logo, app or product icon, official mark or symbol, official character or mascot, or real/branded UI screen. Use only approved official assets in the later deterministic overlay step.
- LOGO_MODE: {LOGO_MODE}
- LOGO_RECT: {LOGO_RECT}
- LOGO_CLEARSPACE_RECT: {LOGO_CLEARSPACE_RECT}
- For `reserve_official_asset` or `internal_base_only`, require a matching entry in `docs/brand_usage_audit.md` and the recorded official asset path, SHA-256, source URL, retrieval date, and use-condition status. Leave the exact LOGO_CLEARSPACE_RECT empty. On the 1254x627 review image, the standard lockup is 520px wide at x=686, y=36, with 48px right margin. The clearspace rectangle is right-aligned with a 48px margin and separate from the logo rectangle. Keep the main diagram or character group over half of the canvas width. Put no person, face, hand, important node, arrow, pattern, or essential diagram element in the reserved rectangle. Draw no placeholder, border, card, badge, shadow, icon, or text there.
- If LOGO_MODE is reserve_official_asset, the verified official asset may be deterministically composited later, after image review.
- If LOGO_MODE is internal_base_only, do not draw or composite a logo. This mode is valid only after the exact official material has been acquired and its source recorded; use conditions are still under review. Preserve the reserved rectangle for internal comparison only. It is not publication-ready, and it must not be adopted or published until the conditions are resolved and the overlay is separately reviewed. If official material has not been acquired, stop as `blocked_brand_asset` before making a per-entry prompt or image candidate.
- If LOGO_MODE is not_required, do not add a blank logo area. This value is valid only when the brand requirements record explicitly supports it.
- Do not draw words, letters, numbers, fake text, code, captions, labels, or watermarks.

CHARACTERS
CHARACTER_POLICY: {CHARACTER_POLICY}
If the source contains a fixed series character that is not listed under REMOVE, preserve its number, identity, role, and established design. For the pet robot, preserve only blue active accents already visible in the source; do not add glow lines or halos unless an attached reviewed sheet explicitly shows them. Do not add a character just to decorate the scene. If a specified character must be added, attach the matching reference sheet as an actual image input to image-edit and use only that sheet:
- Reader: assets/ponchi/references/character-a-reader-woman.png
- Teacher: assets/ponchi/references/character-b-teacher-man.png
- Pet robot: assets/ponchi/references/character-c-pet-robot.png
Do not invent a replacement design or include all three characters unless MUST KEEP requires them.
If the matching reference image cannot be attached, stop and defer generation; a written path alone is not a visual reference.

OUTPUT
Return one clean 2:1 PNG candidate at the highest supported native resolution. Aim for a long edge of at least 1500px. If the tool cannot produce that natively, report its actual dimensions; do not upscale and claim print-master resolution. Do not alter or overwrite any production file.
```

## 実行とレビューの規則

- image-editへ添付するのは `SOURCE_IMAGE_PATH` とハッシュが一致するロゴなしベース画像です。公式ロゴは条件確認後にのみ、生成後の既存決定論的overlay手順で別合成します。
- `docs/brand_usage_audit.md` の該当項目と、項目別ブランド要件台帳の行を sidecar に記録します。公式素材の出典・ローカルパス・SHA-256・取得日が確認できないブランド項目は `blocked_brand_asset` とし、プロンプトも画像候補も作りません。
- `reserve_official_asset` は公式素材と対象用途の使用条件を確認・記録した場合だけ選びます。素材取得済みで使用条件が未確認の場合に限って `internal_base_only` の内部候補を許可し、合成・採用・公開へ進めません。
- 標準logo clearspaceは `docs/ponchi_brand_asset_rules.md` と `docs/ponchi_logo_overlay_pipeline.md` に合わせます。`LOGO_RECT` と `LOGO_CLEARSPACE_RECT` は別々に座標を記録します。意味・入力元・削除対象まで未確定なら、画像自体を生成しません。
- `not_required` は意味が通るという理由だけでは選べません。ブランド要件台帳に明示的な根拠が必要です。
- 複数群やパネルを残すかは `MUST_KEEP` に基づきます。「一つの焦点群に統合」は指示しません。
- 画像の生成前後で元パス、元SHA-256、テンプレート版、モデル、出力先、寸法、LAYOUT_AND_READING_ORDER、プロンプト本文を記録します。人手ブリーフと元画像のレイアウト差がある場合は、優先根拠も記録します。
- 機械監査の9色許容はこの著者承認スタイルより緩いため、`palette=pass` だけでスタイル適合とは判定しません。
- 1254×627の画像は比較・監査用の縮小版として扱います。長辺1500px未満の生成物を印刷用マスターと呼びません。
- 初回候補を一つ作り、記録済みの問題がある場合だけ一度修正します。意味・元画像・削除対象が未確定なら生成前に保留します。公式素材未取得なら `blocked_brand_asset` として停止し、素材取得済みで使用条件だけ未確定の場合は `internal_base_only` の内部候補までに制限します。
