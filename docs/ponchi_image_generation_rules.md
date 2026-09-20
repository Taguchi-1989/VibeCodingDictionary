# Ponchi Image Generation Rules

> **2026-09-20 追記**：密度に関する条項（「主題はキャンバス幅の半分以上」「2〜4 個の大きな塊」「密度を上げる再生成」）は [docs/ponchi_clarity_first_prompt_2026-09-20.md](ponchi_clarity_first_prompt_2026-09-20.md) が上書きします。以降の生成・再生成では、密度ではなく「少ない情報量で意味が分かること」を優先してください。色・文字・ロゴ・ブランド余白のルールはこの文書のままです。

## 基本方針

ポンチ絵の本番画像は、図鑑全体で同じシリーズに見えることを優先する。個別画像の派手さより、一覧で並べた時の統一感を重視する。

## 色ルール

**白・黒・グレー・青系以外は使わない。**

色の合格判定は `docs/ponchi_color_acceptance_gate.md` に従う。`overlay_audit`
は色ルールの合格を意味しない。公式ロゴ・公式アイコンの色は後合成した
公式素材ピクセルだけの例外であり、生成された本文イラスト側の多色化は
不採用にする。

許可する色:

- `#FFFFFF` pure white: main background
- `#F7F9FC` off-white / paper white: very subtle surface fill only
- `#1A1A1A` black: main linework and official black logos
- `#6B7280` neutral gray: secondary lines, inactive UI strokes, shadows
- `#EAF1FB` pale blue 1: active AI suggestion fill, very light focus area
- `#D6E6FA` pale blue 2: stronger active suggestion line or selected row
- `#8DB7E8` soft blue: small glow ticks, accepted path, connector highlight
- `#3F7FD1` medium blue: small icon accent or active cursor accent only
- `#123E82` deep navy: rare emphasis, arrows, or structural accent

禁止する色:

- 黄
- 緑
- 赤
- 紫
- 茶
- オレンジ
- 虹色
- ブランドカラー
- カラフルなUIやグラフ

色の役割:

- 背景は白を基本にする。薄い紙色や極薄青を使う場合も、面全体を染めない。
- 黒は線画、人物、机、PC、図形の主線に使う。
- グレーは未選択、Before 側、非アクティブな UI 線、軽い影に使う。
- 青は以下の 5 色だけを使う。中間色を増やさない。
  - `#EAF1FB`: 面のごく薄いハイライト、AI 補完候補の背景
  - `#D6E6FA`: 補完候補の行、選択中の薄い帯
  - `#8DB7E8`: 経路、接続線、小さな発光線
  - `#3F7FD1`: 小さいアクティブ点、カーソル、アイコンの一点アクセント
  - `#123E82`: 重要矢印、主ノード、章アクセント。ただし面積は小さくする
- 淡い青は「AI が効いている箇所」「補完候補」「選択中の経路」だけに使う。
- 濃紺は矢印、重要ノード、章ごとのごく小さいアクセントに限定する。
- 青い装飾線、青いスパークル、ランダムな発光、青い背景面は避ける。
- 企業・サービスのブランドカラーは、公式ロゴ素材そのものを後合成する場合を除いて使わない。

画像生成プロンプトでは、以下を必ず入れる。

```text
Color palette: strict white/black/gray plus the approved blue palette only.
Use pure white background (#FFFFFF), optional off-white (#F7F9FC), black
linework (#1A1A1A), neutral gray secondary strokes (#6B7280), and only these
blue values: #EAF1FB, #D6E6FA, #8DB7E8, #3F7FD1, #123E82. Use #EAF1FB or
#D6E6FA for active AI suggestion fills, #8DB7E8 for selected paths or small
glow ticks, #3F7FD1 for tiny active accents, and #123E82 only for rare
structural emphasis. Do not use any other blue, cyan, teal, purple-blue, or
brand blue. Do not use yellow, green, red, purple, brown, orange, rainbow
colors, decorative blue sparkles, blue background fills, or brand colors.
```

## ロゴルール

AI 生成では会社ロゴ・サービスロゴ・公式アイコン・公式マークを描かせない。ロゴやアイコンが読者理解に必要な場合だけ、公式ブランド素材を取得し、生成後に決定論的に合成する。詳細は `docs/ponchi_brand_asset_rules.md` に従う。

## 2:1 とロゴ余白

2:1 の本番ポンチ絵は、横長キャンバス全体を「意味のある誌面」として使う。ただし、公式ロゴ後合成が必要な画像では、画面全体を図形や人物で埋め切らない。ロゴが入る場所を最初から構図の一部として空ける。

余白と密度の基準:

- ロゴ用 clearspace は必要な分だけ残す。余白を広く取りすぎて、右半分や上半分が未使用に見える画像は不採用にする。
- 公式ロゴが必要な画像でも、主図解・人物・フローのまとまりはキャンバス幅の少なくとも半分以上を使う。ロゴ余白以外の領域は意味のある図で埋める。
- `1254x627` では、ロゴ clearspace の実効領域はおおむね横 `520-580px`、縦 `150-220px` までを目安にする。全面の 1/4 を超える白地をロゴのためだけに残さない。
- 人物が主役の画像では、人物の頭から胴体までが小さくなりすぎないようにする。人物を出す場合、主要人物は画像高さの `35-60%` 程度を目安にし、脇役や群衆だけを小さくする。
- 図解が主役の画像では、中央の主図形または主フローを `2-4` 個の大きな塊で構成する。小さいカードや細い線を大量に並べて、縮小時に読めない構図にしない。
- ブランド系の画像は「ロゴを置くために主題を小さくする」のではなく、「主題のまとまり」と「ロゴの白場」が左右または上下で釣り合う構図にする。

ロゴ余白の扱い:

- 余白は後から絵の上にロゴを貼るための空き地ではなく、最初から設計された白い紙面・壁面・余白として見せる。
- ロゴ予定位置の下に、人物、顔、手、重要ノード、矢印、読者が意味を取る主図形を置かない。
- ロゴ予定位置には、枠、カード、ラベル、プレースホルダー、薄いアイコン、薄い文字、装飾線も置かない。
- 2:1 全面に絵が広がって見えても、右上の公式ロゴ用 clearspace は必ず静かに残す。
- 余白が大きすぎて未完成に見える場合は、余白の外側で構図を調整する。余白内に背景模様や小物を足して解決しない。
- ロゴ合成後に、ロゴが主図解を隠す、構図の意味を変える、広告バナーのように見える場合は不採用にする。

ロゴ合成の共通ルール:

- 公式 SVG/PNG/PDF 由来の素材だけを使う。
- ロゴの形、色、縦横比、余白を変えない。
- 白背景に黒ロゴ、または公式が許可する単色版を優先する。
- ロゴの周囲に独自の枠、カード、吹き出し、バッジ、影を足さない。
- 画像生成プロンプトでは、ロゴ用の白い余白だけを予約する。
- `1254x627` の 2:1 ポンチ絵では、主要サービス lockup の目安を横幅 `500-520px` にする。小さな飾りではなく、縮小プレビューでも読める大きさで扱う。
- 小さな補助ロゴや画面内の二次的なロゴは使わない。必要なら本文・キャプションで補う。
- 公式アイコンや公式マークもロゴと同じ扱いにする。AI 生成で似せない。
- 汎用アイコンは使ってよいが、実在ブランドのアイコンに見える形・色にはしない。

ロゴ合成用のプロンプト文:

```text
Logo rule: do not generate, imitate, redraw, or approximate any company or
service logo. Reserve a clean white clearspace area for a later official logo
overlay as an intentional part of the 2:1 page composition. Keep the overall
image full and meaningful, but do not place characters, faces, hands, important
nodes, arrows, diagrams, text, icons, patterns, or decorative marks under the
future logo area. Do not draw a box, border, badge, label, icon, shadow, or
placeholder around this area. On a 1254x627 canvas, leave enough clearspace for
an official logo lockup about 500-520px wide, preserving the official asset's
aspect ratio and built-in clearspace.
```

ブランド素材禁止の追加プロンプト文:

```text
Brand asset rule: do not generate, imitate, redraw, approximate, or stylize any
company logo, service logo, app icon, product icon, official mark, mascot,
trademarked symbol, brand color scheme, or real product UI. If brand
identification is required, reserve a clean white clearspace area for a later
official asset overlay. Generic non-branded icons such as folders, arrows,
browser frames, server boxes, abstract nodes, and simple clouds are allowed
only if they do not resemble any real brand asset.
```

## スタイル

- 白い紙に黒・グレーのシンプルな線画。
- 鉛筆スケッチ風、ラフな手描き線、ハッチング、ざらついた筆致は避ける。
- 線は均一で読みやすく、やや図解・アイコン寄りのクリーンなタッチにする。
- 青系は補助色として使う。ただし意味のある箇所だけに限定する。
- 影やグラデーションは控えめ。
- 200px程度のサムネイルでも意味が分かる。
- ロゴ、商標、実在UIの AI 生成での再現は避ける。
- 人物・ロボットの一貫性は `docs/ponchi_character_bible.md` に従う。
- 同じ構図の量産を避け、用途別の構図ファミリーは `docs/ponchi_composition_variety_policy.md` に従う。

画像生成プロンプトでは、スタイル指定に以下を入れる。

```text
Style: clean simple editorial line illustration, not pencil sketch. Use smooth
uniform black lines, flat light gray fills, minimal shading, no hatching, no
scratchy hand-drawn texture, no marker texture, and no painterly look. The
image should feel like a clear technical-book diagram with friendly human
figures, not a rough drawing.
```

## 生成前 scene_brief

画像生成プロンプトを書く前に、必ず短い `scene_brief` を作る。これを決めずに直接プロンプトを書かない。

`title` やサービス名をそのまま絵にしない。必ず `subject_stack` で「題材」と「絵の主役」を分ける。ロゴが必要な場合でも、絵の主役はロゴではなく、その用語が説明する構造・流れ・使われ方にする。

```yaml
entry_id:
title:
subject_type: brand_or_service | model_family | tool_or_language | benchmark_or_eval | concept | history_or_event | front_matter
subject_stack:
  entry_subject:
  visual_subject:
  supporting_subjects:
  logo_subject:
  excluded_subjects:
brand_asset:
  mode: none | official_overlay_ready | official_overlay_required | blocked_brand_asset
  asset_name:
  local_path:
  source_url:
visual_references:
  character_a: assets/ponchi/references/character-a-reader-woman.png
  character_b: assets/ponchi/references/character-b-teacher-man.png
  character_c: assets/ponchi/references/character-c-pet-robot.png
role_balance:
composition_family:
composition_type:
composition_density: compact | balanced | spacious
view_mode: before_after | operation_flow | structure_map | logo_clearspace | diagram_only
characters:
  - female
  - male
  - robot
character_base:
  female: use | omit
  male: use | omit
  robot: use | omit
temporary_people:
  allowed: yes | no
  count:
  role: background_team | crowd | reviewers | users
  rule: keep temporary people secondary; do not replace Character A/B/C
hands_policy:
  visible_hands_max:
  gesture:
scene_goal:
main_symbols:
clearspace:
main_subject_scale:
avoid:
```

`subject_stack.visual_subject` が空なら生成しない。`role_balance` は `docs/ponchi_character_bible.md` の表から選ぶ。`composition_family` は `docs/ponchi_composition_variety_policy.md` の表から選ぶ。構図は毎回 `2人 + ロボット + 机 + PC` に固定しない。

使える `composition_type`:

| 値 | 使う場面 |
| :-- | :-- |
| `board_review` | ボード上の図を確認する |
| `single_laptop` | 1 人が PC で確認する |
| `standing_board` | 机なしでボードを見る |
| `cards_on_wall` | カードやノードを壁面に並べる |
| `robot_console` | ロボットが小さな記号パネルを示す |
| `diagram_first` | 人物より図解を主役にする |
| `logo_clearspace` | 公式ロゴ後合成用の白い余白を主構図に含める |
| `diagram_only` | 人物もロボットも出さない |

避ける偏り:

- 毎回、机、ノート、マグカップ、PC を置かない。
- 毎回、片方が立って説明し、片方が座って質問する形にしない。
- 毎回、人物 2 人とロボットを全員出さない。
- 毎回、中央ボードと左右人物にしない。
- 5 枚程度のバッチで、同じ `composition_family` だけを繰り返さない。
- 手の演技で説明しようとせず、図形、矢印、ノードで意味を作る。

## 禁則

- 読める文字を画像内に入れない。
- 会社ロゴ・サービスロゴを AI 生成で入れない。
- 実在人物の顔を似せない。
- 暗い背景にしない。
- 1枚だけ目立つカラフルな絵にしない。

## 再生成時の確認

再生成候補を見る時は、まず以下を確認する。

1. 白黒青系だけで成立しているか。
2. 概念を誤解させる小物がないか。
3. 既存シリーズと線の密度が近いか。
4. 被写体が小さすぎないか。
5. 画像内の文字・ロゴ・ブランド色が混ざっていないか。
6. Character A/B/C の同一キャラ感が保たれているか。
7. `role_balance` が連続して偏っていないか。
8. 手、指、持ち物、腕の接続が破綻していないか。
9. 公式ロゴ後合成が必要な場合、白い余白が自然に残っているか。
10. ロゴ余白を広く取りすぎて、主題が片側に小さく寄っていないか。
11. 200px 程度のサムネイルで、主図解の大きな塊が見えるか。
