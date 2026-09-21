# ポンチ絵「引き算」プロンプト（clarity-first / 2026-09-20）

これまでのポンチ絵は「誌面が寂しく見えないこと」を優先して作ってきました。その結果、**意味に効かない絵が増え、1 枚あたりの情報量が読者の処理量を超えています**。この文書は、その向きを反転させるための生成プロンプト集です。

**狙いは 1 つだけ**：絵柄や登場人物は問わず、**より少ない情報量で「それが何を意味するか」が分かること**。

**方針は「少なく、大きく」です。** 絵を小さくするのではありません。要素の数を削り、残ったものを大きく描いて画面を使い切ります。そして**全 390 枚でその大きさを揃えます**。寂しく見えるかどうかより、**めくったときにサイズ感が一致していること**を優先します。

- 新規生成にも、既存 390 枚の作り直しにも、そのまま使えるプロンプトを「コピペ用」節に置いています
- 従来ルール [docs/ponchi_image_generation_rules.md](ponchi_image_generation_rules.md) のうち、**密度に関する条項はこの文書が上書きします**（§2 の差分表）
- 色・文字・ロゴの禁則は変えません。制約が少ないほど読みやすくなるので、むしろ強化しています

---

## 1. 合格の定義（これを満たせば採用）

数値の前に、判定の言葉を 1 つに絞ります。

> **キャプションを隠した状態で、3 秒見て「何の話か」を一言で言えるか。**

具体的な関門は 3 つです。

| # | 関門 | 判定 |
| :-- | :-- | :-- |
| G1 | **3 秒テスト** | タイトル・本文を隠して 3 秒見せ、「これは何の絵ですか」に一言で答えられる |
| G2 | **200px テスト** | 幅 200px に縮小しても、主役の塊と関係（流れ／対比）が残る |
| G3 | **白黒テスト** | 青を全部グレーに潰しても、意味の差が消えない |

G1 の実測には既存の [scripts/score_ponchi_blind_quiz.py](../scripts/score_ponchi_blind_quiz.py) を使えます。判定が `semantic_ok` なら合格、`ambiguous` / `generic` / `misleading` は作り直し対象です。

**落ちる原因は「描き足りない」ではなく、ほぼ常に「描きすぎ」です。** 直し方は原則すべて引き算にします。

### 混ぜてはいけない 3 つの軸

ここが今回いちばん大事な整理です。旧ルールは「大きさ」と「情報量」を `density` という 1 語で混ぜていました（[scripts/ponchi_image_audit.py](../scripts/ponchi_image_audit.py) が `density = bbox_coverage(...)` と書いていたのが実体）。**あの指標が測っていたのは「詰まり具合」ではなく「絵がどこまで広がっているか」です。** だから「density を上げろ」という指示が「細かいものを足せ」に化けました。

| 軸 | 何を測るか | どうしたいか |
| :-- | :-- | :-- |
| **span**（大きさ） | インクの外接矩形 ÷ キャンバス | **高く、かつ全枚数で揃える**。0.78〜0.90 |
| **ink**（情報量） | 塗られた画素 ÷ キャンバス | **低く抑える**。0.08〜0.14 |
| **要素数**（意味の個数） | 読者が目を止める塊の数 | **5 個まで**（§3 原則 2） |

目指す形は **span 高 × ink 低**、つまり「少ない要素を大きく描く」です。旧ルールが作っていたのは span 中 × ink 高（細かいものが多い）、前案が作りかけたのは span 低 × ink 低（小さくて寂しく、しかもサイズ感が揃わない）でした。どちらも外します。

---

## 2. 従来ルールとの差分（ここだけ上書きします）

| 項目 | 旧（〜2026-09） | 新（この文書） |
| :-- | :-- | :-- |
| 密度 | `density_gate: bbox coverage ≥ 0.50`（下限のみ） | **span の帯に再定義**：0.78〜0.90。下限だけでは揃わないので上限も引く |
| 情報量 | 指標なし（density と混同） | **ink 0.08〜0.14** を新設。ここだけを下げる |
| 主題サイズ | 「キャンバス幅の半分以上を占める」 | 「**主役の高さがキャンバス高の 60〜75%**」（§4 の規格） |
| 塊の数 | 「2〜4 個の大きな塊で構成する」 | **意味を持つ要素は合計 5 個まで**（塊・人物・記号を通算） |
| 人物 | Character A/B/C を基本に据える | **原則 0〜1 人**。意味に人が要るときだけ出す。キャラ一貫性は任意 |
| 構図の多様性 | バッチ内で family を 3 種以上混ぜる | 維持。ただし**多様性より 1 枚の可読性を優先**する |
| 「軽い絵は作り直し」方針 | `lightweight_quality_regen`＝密度を上げる | **無効**。同じ判定の絵は「密度を下げて作り直す」に読み替える |
| 色・文字・ロゴ | 白黒グレー＋承認済み青／文字禁止／ロゴ禁止 | 維持（青の使用面積はさらに絞る） |

> ⚠️ [scripts/ponchi_prompt_scaffold.py](../scripts/ponchi_prompt_scaffold.py) は現在 1823-1824 行と 1843 行で旧密度ルールを出力に埋め込んでいます。パイプラインを回し直すときは、この文書の §6 のブロックに差し替えてください（スクリプト改修は未実施）。
>
> 計測側の [scripts/ponchi_image_audit.py](../scripts/ponchi_image_audit.py) は **対応済み**です。span と ink を別々に出し、それぞれ帯で判定し、バッチ全体のばらつき（median / min / max / sd / 帯内率）を最後に表示します。

---

## 3. 描く前に決める 5 原則

### 原則 1：1 枚 = 1 文

プロンプトを書く前に、**日本語 1 文**で書きます。書式は固定します。

```
【◯◯】が【△△】になる／を【□□】する
```

例：

- D-11 Git ＝「**作業の履歴が枝分かれして、あとで 1 本に戻る**」
- F-2 TypeScript ＝「**動かす前に、型が間違いを先に見つける**」
- G-1 Context ＝「**窓に入った分だけがモデルに見えていて、外は見えない**」

この 1 文が書けないときは、**その用語に絵は要りません**。§8 の「絵を作らない判断」に進みます。

### 原則 2：要素予算（element budget）

「読者が意味を取るために目を止める塊」を 1 要素と数えます。箱・ノード・人物・デバイス・記号は各 1、装飾は 0（そもそも描かない）。

| 種別 | 上限 | 理想 |
| :-- | :-- | :-- |
| 意味を持つ要素の合計 | **5** | 3〜4 |
| 矢印・接続線 | **3** | 1〜2 |
| 人物 | **1** | 0 |
| 青を載せる要素 | **2** | 1 |
| 階層・段・パネルの分割数 | **3** | 2 |

上限を超えたら、絵が複雑なのではなく**言いたいことが 2 つ以上ある**サインです。1 文に戻って削ります。

### 原則 3：流れか、対比か、どちらか 1 つ

1 枚に「時間の流れ」と「良し悪しの対比」を同居させません。両方要るなら、その用語は 2 文に分かれています。左ページの図を諦めて、本文側で補います。

### 原則 4：差は「形」で作る（色・濃淡・細部で作らない）

違いは **大きさ・向き・数・形** のいずれかで表します。2 倍以上の差をつけます。線の太さ、網掛け、色の濃さ、小さなアイコンの描き分けで差を出すと、縮小した瞬間に消えます。

### 原則 5：削ったら、残りを大きくする

引き算で空いた場所に、**別のものを足すのは失敗、そのまま白く残すのも不足**です。正解は、**残った要素を拡大して画面を使い切ること**。

- 足す ＝ 旧ルールの失敗（ink が上がる）
- 空けたまま ＝ サイズ感が揃わない（span が下がる）
- **残りを大きくする ＝ 正解**（ink は下がったまま span は保つ）

余白率そのものを目標にしません。狙うのは §4 のサイズ規格です。

---

## 4. サイズ規格（全枚数で揃えるための数値）

キャンバスは `1254x627`（2:1）固定です。**「大きく描く」を各自の感覚に任せると揃わない**ので、数値で固定します。

| 項目 | 規格 | 根拠 |
| :-- | :-- | :-- |
| 安全マージン | 外周 **48px** は何も置かない | 断ち落ちと綴じの保険 |
| **主役の高さ** | キャンバス高の **60〜75%**（376〜470px） | これが「サイズ感」の本体。全枚数で揃える |
| 脇役の大きさ | 主役の **50〜70%** | 主役との差を一目で付ける |
| 要素間の最小間隔 | **40px** | 200px 縮小時に塊が分離して見える下限 |
| 主線の太さ | **4〜5px** | 1254px 基準。全枚数で統一 |
| 補助線の太さ | **2〜3px** | 主線と明確に差をつける |
| span | **0.78〜0.90** | 下限は「小さすぎ」、上限は「端まで詰めすぎ」 |
| ink | **0.08〜0.14** | 上限が情報量の天井 |

### 現状（`assets/ponchi/final` 390 枚の実測・2026-09-20）

```
span: median 0.812  min 0.516  max 1.000  sd 0.082  帯内 220/390 (56%)
ink : median 0.126  min 0.050  max 0.476  sd 0.048  帯内 228/390 (58%)
両方の帯に入っている: 111/390 (28%)
```

**サイズ感が一致していない、という見立ては数字で裏が取れています。** span は 0.52〜1.00 まで開いており、ink は最軽量と最重量で約 10 倍差（0.050 対 0.476）があります。両方の帯に収まっているのは 28% だけです。

章ごとの偏りも出ています（median ink）。

| 章 | A | B | C | D | E | F | G | H | I | J |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ink | **0.184** | 0.132 | **0.183** | 0.138 | 0.122 | 0.118 | 0.098 | 0.098 | 0.149 | 0.128 |
| span | 0.907 | 0.830 | 0.847 | 0.848 | 0.799 | 0.778 | **0.744** | 0.776 | 0.816 | 0.820 |

A 章・C 章は G 章・H 章のほぼ 2 倍描き込まれています。章をまたいでめくると、同じ本に見えません。

### 直す順番

1. **ink > 0.20 の 36 枚**（描きすぎ。効果が最も大きい）
   `J-72(0.48) F-84(0.34) J-74(0.33) J-73(0.31) J-31(0.30) J-81(0.28) J-80(0.26) J-70(0.26) B-5(0.25) D-51(0.24) J-71(0.23) A-10(0.23) J-78(0.23) B-6(0.23) D-57(0.23) D-58(0.22) C-51(0.22) J-99(0.22) C-59(0.22) C-56(0.22) C-14(0.21) B-8(0.21) J-23(0.21) A-6(0.21) J-20(0.21) C-52(0.21) J-79(0.21) C-57(0.21) C-5(0.20) J-22(0.20) J-19(0.20) J-75(0.20) E-3(0.20) C-10(0.20) H-62(0.20) J-92(0.20)`
2. **span < 0.70 の 52 枚**（小さすぎ。§6-D で拡大するだけで直るものが多い）
   G 章に集中しています（`G-18 G-31 G-32 G-19 G-11 G-34 G-4 G-3 G-33 G-5 G-10 G-13 G-39 G-41 G-8 G-23`）
3. 残りは章単位で ink を揃える（A・C を先に）

---

## 5. 常に削るもの（旧画像に頻出）

再生成の前に、既存画像からこれらが見つかったら無条件で落とします。

- 机、椅子、マグカップ、観葉植物、床線、壁、窓、書類の山
- 主題ではないモニター・ノート PC・スマホ（「人が PC の前にいる」は意味ではありません）
- 中身のない小カード、並べただけのタイル、意味のないノードの群れ
- 飾りの点・粒・きらめき・スピード線・集中線・ふきだしの尻尾だけの記号
- 枠線、角丸カードの二重枠、影、グラデーション、背景の薄いパターン
- 意味を変えない矢印（「なんとなく右へ」の矢印）
- 読めない文字を装った波線・ダミーテキスト（**文字の気配ごと禁止**）
- 3 人目以降の人物、群衆、後ろ姿のチーム

---

## 6. コピペ用プロンプト

`<ONE_SENTENCE_EN>` に原則 1 の 1 文を英訳して入れます。それ以外は原則そのまま使います。

### A. 新規生成（clarity-first ベース）

```text
Use case: infographic-diagram
Asset type: VibeCodingDictionary ponchi image, 2:1 horizontal, 1254x627, white background.
Primary request: Draw ONE idea and nothing else: "<ONE_SENTENCE_EN>".
Success test: a reader who cannot read any caption must be able to say what this picture means within 3 seconds, and the meaning must survive at 200px wide.

Hard element budget - count the shapes before drawing:
- At most 5 meaningful shapes in total. A box, a node, a person, a device, or a symbol each counts as one.
- At most 3 arrows or connectors. Every arrow must change the meaning if removed.
- At most 1 person, and only if the idea requires a human actor. Zero people is the preferred default.
- At most 3 panels, layers, or stages.
- Zero decorative elements: no desks, chairs, mugs, plants, floors, walls, windows, background props, non-subject screens, filler cards, tiny icons, dots, sparkles, speed lines, frames, borders, drop shadows, gradients, or background patterns.

Few elements, drawn LARGE - this is the core instruction:
- Draw the few shapes you keep at a big, confident scale. The main subject must be 60-75% of the canvas HEIGHT (about 376-470px of 627px). Never draw a small diagram floating in a large empty canvas.
- The composition as a whole should span most of the canvas, stopping about 48px short of every edge. Nothing touches the edges, and no entire corner or half of the canvas is left unused.
- Secondary shapes are 50-70% the size of the main subject, so the hierarchy is obvious at a glance.
- Keep at least 40px of clear space between separate shapes so they stay distinct when the image is reduced.
- Use a single consistent line weight for main outlines (about 4-5px at this canvas size) and a thinner one (2-3px) for secondary lines.
- Empty space comes from having FEW elements, never from drawing them small. Do not add anything to fill space; do not shrink anything to create space.

Make the meaning readable by structure, not by detail:
- The single most important shape must be the largest object on the canvas.
- Express any difference through size, direction, count, or shape, with at least a 2x contrast. Never express it through texture, line weight, color intensity, or small details.
- If deleting a shape does not change what the picture means, do not draw it.

Style: clean editorial line illustration; smooth uniform black lines of even weight; flat fills only; minimal shading; no hatching, no pencil or marker texture, no painterly look, no 3D, no photorealism, no isometric clutter.

Color palette: white, black, gray, plus the approved blues only: #FFFFFF, #F7F9FC, #1A1A1A, #6B7280, #EAF1FB, #D6E6FA, #8DB7E8, #3F7FD1, #123E82. Apply blue to at most two shapes, only to mark the single place where the idea happens. No other colors, no cyan, teal, purple-blue, or brand colors. The image must still read correctly in pure black and white.

Text and brand rule: no readable text, letters, numbers, fake handwriting, or scribbles that imitate words. No company or service logo, app icon, product UI, brand mark, or brand color scheme. No watermark.

Output: exactly one image.
```

### B. 既存画像の作り直し（引き算リライト）

既存画像を参照させられる場合（image-to-image、または旧プロンプトを渡す場合）に使います。

```text
Revise this illustration by subtraction only. Do not add anything.

The picture must say exactly one thing: "<ONE_SENTENCE_EN>".

1. Keep only the shapes that carry that sentence. Delete everything else: background props, desks, mugs, plants, floors, non-subject screens, filler cards, small icons, decorative dots, sparkles, motion lines, frames, borders, shadows, gradients, and any arrow whose removal would not change the meaning.
2. Reduce to at most 5 meaningful shapes, at most 3 arrows, at most 1 person. If the idea works without people, remove all people.
3. Then ENLARGE what remains to fill the canvas again. Scale the main subject up to 60-75% of the canvas height (about 376-470px of 627px) and let the whole composition span the canvas, stopping about 48px short of every edge. Do not leave the surviving shapes at their old small size in a newly empty canvas.
4. Do not add anything to fill the space that opens up. The space is closed by scaling up, not by adding.
5. Keep at least 40px between separate shapes. Keep one consistent main line weight (about 4-5px at this canvas size).
6. Keep the existing line style and the white/black/gray/blue palette. Apply blue to at most two shapes.
7. No readable text, no logos, no brand colors, no watermark.

Output: exactly one image, 2:1 horizontal, 1254x627, white background.
```

### C. 「これは何の絵か分からない」と言われたときの追い込み

G1 に落ちた絵に対する 2 手目です。作り直しではなく、**主役を 1 つ選び直す**指示にします。

```text
This image failed a blind reading test: viewers could not name the concept in 3 seconds.
Do not restyle it and do not add explanatory detail. Instead:
- Choose the ONE shape that means "<ONE_SENTENCE_EN>" and make it at least twice as large as everything else.
- Delete the two or three least important shapes entirely.
- Move the remaining shapes so the reading order is unmistakable: one entry point, one path, one result.
Output: exactly one image, 2:1, 1254x627, white background, no text, no logos.
```

### D. 小さすぎる絵を「拡大するだけ」で直す

`span < 0.70` の 52 枚向けです。**要素は既に足りているので、構図を変えずに大きさだけ直します。** 引き算プロンプトをここに当てると、要素が減りすぎてかえって寂しくなります。

```text
Keep this illustration's composition, elements, and meaning exactly as they are. Change only the scale.

- Do not add, remove, redraw, or rearrange any element.
- Scale the existing drawing up so the main subject reaches 60-75% of the canvas height (about 376-470px of 627px), and the composition as a whole spans the canvas, stopping about 48px short of every edge.
- Scale line weights with the drawing so the main outlines land at about 4-5px and secondary lines at 2-3px.
- Keep the same proportions between elements; enlarge everything together rather than resizing parts individually.
- Keep the white background, the existing palette, and the empty areas that remain after scaling. Do not fill them.

Output: exactly one image, 2:1 horizontal, 1254x627, white background, no text, no logos.
```

---

## 7. 型別の差し込みブロック（A の `Primary request` の直後に 1 つだけ入れる）

構図ファミリーは [docs/ponchi_composition_variety_policy.md](ponchi_composition_variety_policy.md) のままですが、各型に要素数の上限を入れて固定します。

| family | 差し込む英文 |
| :-- | :-- |
| `process_flow` | `Structure: a left-to-right flow with exactly 3 stages joined by 2 arrows. The 3 stages must differ in shape, not only in position. No side branches.` |
| `before_after` | `Structure: two panels split by one thin vertical line. Left is the problem, right is the improvement. Draw the SAME object on both sides, changed in one visible way. No third panel, no extra annotation.` |
| `layer_stack` | `Structure: exactly 3 stacked layers, widest at the bottom. One short arrow marks the layer the reader touches. No labels, no side notes.` |
| `concept_map` | `Structure: one central shape with exactly 3 branches. The center must be at least twice the size of each branch. Do not draw a web of many nodes.` |
| `timeline_scale` | `Structure: one horizontal baseline with 3 marks that grow in size left to right, each at least twice the previous. No tick clutter.` |
| `tool_loop` | `Structure: one closed loop with exactly 3 nodes and 3 arrows in a single direction. The loop silhouette must be recognizable as a loop at 200px.` |
| `collaboration_hub` | `Structure: one shared object in the center and exactly 2 actors reaching it. Do not draw a team, a crowd, or an office.` |
| `brand_clearspace` | `Structure: the simplified diagram (at most 4 shapes) uses the whole canvas as usual. Reserve clean white clearspace for a later official logo overlay in the TOP-RIGHT CORNER ONLY: about 520-580px wide and 150-220px tall on a 1254x627 canvas, well under a quarter of the image. Everything below and left of that corner, including the lower right, is filled by the diagram. Do not draw anything, including faint marks, borders, or placeholders, inside the corner clearspace, and do not leave the whole right side or the whole top of the canvas empty.` |

ブランド枠だけは、旧ルール（[docs/ponchi_image_generation_rules.md](ponchi_image_generation_rules.md) の「2:1 とロゴ余白」）の**余白位置と合成ルールをそのまま踏襲**します。変わるのは、余白の外側に詰め込む図解の密度だけです。

**ロゴ余白は「右上の隅」であって「右 1/3」ではありません。** 旧ルールが「余白を広く取りすぎて右半分や上半分が未使用に見える画像は不採用」「全面の 1/4 を超える白地をロゴのためだけに残さない」と定めているとおりです。隅だけを空ければ、その下は図解で埋まるので**外接矩形はキャンバス全体に届き、span 帯（0.78〜0.90）はそのまま適用できます**。

実測でも確認しています（`logo_need: required` の 133 枚 対 `not_needed` の 211 枚）。

| | span median | 帯内率 |
| :-- | --: | --: |
| ロゴ後合成あり（133 枚） | **0.831** | **79%** |
| ロゴなし（211 枚） | 0.788 | 45% |

ロゴ余白のある絵のほうが span は**高い**ので、ブランド枠用に帯を緩める必要はありません。帯から外れる 18 枚は素直に「小さすぎ」です。

---

## 8. 絵を作らない判断

「1 文が書けない」「書けても絵にすると記号の羅列にしかならない」用語があります。無理に 1 コマを作ると、**意味のない絵が誌面のノイズになります**。次の順で降ります。

1. **1 記号だけにする**：箱 1 つ、矢印 1 本、輪 1 つ。意味の核だけを大きく置く（例：抽象概念、思想、歴史的事件）
2. **図を諦める**：左ページのメイン図枠を、右ページ「見どころ」の強化や関連用語の充実に振り替える
3. **判断を記録する**：`誌面ポンチ絵メモ` に「図は置かない。理由：1 文にできない／記号 1 個で足りる」と残す

「寂しいから何か描く」は禁止します。**絵が 1 枚減ることは品質の低下ではありません。**

---

## 9. scene_brief の変更点

[docs/ponchi_image_generation_rules.md](ponchi_image_generation_rules.md) の `scene_brief` に対する差分です。

追加するフィールド：

```yaml
one_sentence: "動かす前に、型が間違いを先に見つける"   # 原則 1。空なら生成しない
element_budget:
  shapes: 5        # 上限。理想は 3-4
  arrows: 3
  people: 0        # 0 が既定。1 にするのは意味に人が要るときだけ
  blue_shapes: 2
keep_only:         # 1 文を支える要素だけを列挙する
  - 
delete_list:       # 旧画像から落とすもの（再生成時のみ）
  - 
```

削除・変更するフィールド：

- `density_gate` — **削除**
- `composition_density` — 既定値を `balanced` から **`sparse`** に変更
- `main_subject_scale` — 「幅の半分以上」から「**画面内で最大の 1 つ**」に変更
- `characters` — 既定を全部 `omit` に変更（`use` にするのは `one_sentence` に人が出てくるときだけ）
- `temporary_people` — **常に `allowed: no`**

---

## 10. 回し方

```bash
# 1. 現状を測る（どれが描きすぎ / 小さすぎかを機械で出す）
python3 scripts/ponchi_image_audit.py assets/ponchi/final/*.webp \
  --out-csv ledgers/ponchi_scale_audit.csv
#  → 最後に median / min / max / sd / 帯内率 が出ます。ばらつき（sd）が下がれば揃ってきた合図
#  → CSV の span_verdict=too_small / ink_verdict=too_heavy で対象を絞る

# 章単位で揃え具合を見る（A・C が重いので先に）
python3 scripts/ponchi_image_audit.py assets/ponchi/final/C-*.webp

# 2. 1 文を書く（ここが本体。絵の前に必ず埋める）
#    → content/entries/**/*.md の「誌面ポンチ絵メモ」に one_sentence を追記

# 3. プロンプトを作る（症状で使い分ける）
#    → ink_verdict=too_heavy     : §6-B（引き算して、残りを拡大）
#    → span_verdict=too_small のみ: §6-D（構図を変えず拡大だけ）
#    → 新規                      : §6-A ＋ §7 から型を 1 つ

# 4. 生成 → G1/G2/G3 で判定 → 落ちたら §6-C で 1 手だけ追い込む
#    → 2 手目で通らなければ §8 に降りる（絵を作らない）

# 5. 直した絵を測り直す（帯に入ったか）
python3 scripts/ponchi_image_audit.py assets/ponchi/final/J-72.webp
```

**1 枚に 3 回以上プロンプトを打ち込まないでください。** 3 回かかる絵は、絵の問題ではなく 1 文の問題です。

`--span-min/--span-max/--ink-min/--ink-max` で帯は変えられます。**帯の数値より、sd（ばらつき）が縮むことが目的**です。現状は span sd 0.082 / ink sd 0.048。

---

## 11. この文書の位置づけ

- 上書きするもの：[docs/ponchi_image_generation_rules.md](ponchi_image_generation_rules.md) の密度・主題サイズ・塊数・人物既定、および `lightweight_quality_regen` の「密度を上げる」方針
- そのまま残すもの：色ルール、文字禁止、ロゴ禁止と後合成、ブランド余白、[docs/ponchi_brand_asset_rules.md](ponchi_brand_asset_rules.md)、[docs/ponchi_composition_variety_policy.md](ponchi_composition_variety_policy.md) の family 分類
- 対応済みの連動作業：[scripts/ponchi_image_audit.py](../scripts/ponchi_image_audit.py) が span / ink を分離して帯判定し、バッチのばらつきを出すようになりました（旧 `--min-bbox-coverage` は `--span-min` の別名として残しています）
- 未着手の連動作業：[scripts/ponchi_prompt_scaffold.py](../scripts/ponchi_prompt_scaffold.py) の 1823-1824 行・1843 行の差し替え（§2 の ⚠️）
