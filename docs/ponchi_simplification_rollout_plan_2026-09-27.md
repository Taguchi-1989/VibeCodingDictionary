# ポンチ絵の簡素化 横展開計画

更新日: 2026-09-28  
対象: 現行シリーズのポンチ絵を、意味とシリーズ調を保ったまま必要な分だけ簡素化する候補作業  
状態: 横展開の管理と内部候補監査を進行中。候補画像の採用と `assets/ponchi/final/` の変更は未許可。

## 1. 現在の対象と件数

| 区分 | 件数 | 扱い |
| :-- | --: | :-- |
| 辞書エントリ | 452 | `ledgers/entries.csv` のID・タイトルを起点にする |
| 現行 final WebP | 390 | 実ファイルを基準に簡素化対象を判定 |
| 現行 final がないエントリ | 62 | 既存画像の簡素化と分離し、新規作成レーンへ |
| pilot-001 の候補 | 20 | 全行が人の決定待ち。19件は現行 final あり、F-43 は final なし |
| pilot-001 外の現行 final | 371 | 今後の簡素化トリアージ母集団。全件生成する意味ではない |
| 以前の lightweight 候補履歴 | 92 | pilotと8件重複。非pilotの84件は過去昇格ID数で、81件がtriage待ち、A-6/I-81/J-76の3件はBatch 001の候補・保留レーン |
| 旧品質スコア | 350 | 2026-06-03 時点の参考情報。現行画像への再監査が必要。40件は旧スコアなし |

pilot-001の20件はまだ `human_decision=pending`、`final_adoption=not_authorized` です。したがって、19件を「簡素化完了」と数えず、「候補あり・選定待ち」として管理します。現行 final 390件はこの計画作成で一切変更していません。

`ledgers/ponchi_generation_queue.csv` は452件の現行辞書IDを含まず、62件を欠く古い派生スナップショットでした。今回の全件台帳は `ledgers/entries.csv` と `assets/ponchi/final/` の実ファイルから作成しています。更新時は実ファイルで再照合してください。

### A-6 プロンプト適用例（2026-09-27）

- `ponchi-simplification-v1` をA-6へ適用。候補v1の指摘を受けて一度だけ修正し、候補v2は意味・縮小可読性・配色の独立レビューに合格しました。
- 人手ブリーフの「カレンダー＋時計を上、3つの時変フラグを縦並び」と候補の横3群構成に差が残っています。候補v2は人の決定待ちとし、finalへ採用していません。
- 差の再発を防ぐため `assets/ponchi/experiments/prompts/ponchi-simplification-v1.1/00_template.md` に人手確認済みの `LAYOUT_AND_READING_ORDER` 欄を追加し、独立プロンプトレビューに合格しました。各項目で人手ブリーフに沿って欄を埋め、配置差の優先根拠が曖昧なら生成を保留します。
- 候補、ハッシュ、独立監査、配置差は `ledgers/ponchi_simplification_candidate_ledger_20260927.csv` と候補フォルダの `metadata.json` / `review_v2.md` に記録しています。

### G-19 プロンプト適用例（2026-09-27）

- v1.1で十件ずつのリクエスト行とキャッシュの意味を保ち、ノーブランドの比較図に整理しました。独立監査では十行、再利用、人物の一人制、配色、縮小表示の簡素さは通過しました。
- 初回書込バーの1.25倍が画像生成で守られず、v1→v2→v3→v4と比率だけを指示して編集しました。v4で後続ヒットは約0.105倍まで一致しましたが、初回書込は約1.19倍のままです。監査結果と各SHAは候補台帳と `G-19/metadata.json` に記録し、この候補は未採用です。
- 同じ測定可能な欠陥が二回の対象編集後も残る場合、プロンプトを反復するだけの編集は停止します。候補を `partial` にして保留し、同種の次項目へ知見を反映します。正確な比率が必須なら、別の承認済みで検証可能な作図手段が整ってから再開します。

## 2. 横展開用の管理台帳

- 全452エントリ: `ledgers/ponchi_simplification_rollout_queue_20260927.csv`
- 1行1IDで、現行PNG/WebPの有無、WebPのSHA-256、旧品質スコア、旧候補・昇格履歴、pilot状態、次の作業を記録。
- `historical_*` と `prior_*` は過去記録です。現在の画像の合否や、簡素化済みの証拠としては扱いません。
- `rollout_status` は作業の振り分け用です。対象選定の最終判断は200px確認と人の判定で記録します。
- 20枠の初回選定: `ledgers/ponchi_simplification_batch_001_selection_20260927.csv`。現行画像のハッシュを再確認した17件を選び、3枠（B章2件、J章1件）はブランド・意味条件を満たす候補がなく空けています。候補と保留理由を同じ台帳に残しました。
- 候補生成と独立監査: `ledgers/ponchi_simplification_candidate_ledger_20260927.csv`。A-6は配置判断待ち、G-19は書込比率未達の部分合格です。C-51/C-59は意味・スタイル監査に合格し、必須の機械監査と人の判断待ちです。F-55は椅子を除いた候補v2が意味・スタイル監査に合格し、機械監査と人の判断待ちです。F-160はv3で6点を除去し、意味内容・スタイル・200px確認は合格しましたが、v2からの画素差が指定領域外へ広がったため、修正範囲条件で部分保留です。二回の対象編集上限に達したため再生成せず、最終画像への採用も未許可です。残る11件はソース・意味・ブランド・複雑さの未解決条件で保留しています。

### Batch 002/003 — parallel triage and prompt-readiness gate (2026-09-27)

- Two priority-sampled triage files cover 60 distinct current WebP files outside pilot-001. Chapter counts are A2 / B2 / C3 / D2 / E6 / F9 / G13 / H5 / I3 / J15; all chapters appear, but G/J are overrepresented. Batch 002 has 8 `simplify_candidate`, 1 `keep`, and 21 `hold_for_brand_or_semantics`; batch 003 has 17 candidates, 1 `minor_edit`, and 12 holds. Totals: 25 candidates, 1 keep, 1 minor edit, and 33 holds.
- All 60 current WebP hashes and `entries.csv` brief paths were checked. Eight batch-002 and five batch-003 historical generation-ledger path mismatches or blanks remain recorded in the audit rows; `entries.csv` remains authoritative and the historical ledger was not repaired in place.
- The 452-row rollout queue retains its previous fields and now syncs the latest triage batch/disposition, Batch 002 v2 selection status, per-row prompt readiness, Batch 002 candidate path/hash, and candidate-review status. The 20 selected IDs and held/reserve IDs are therefore visible from the central management ledger.
- Independent brand review moved F-51 to hold: its brief calls for a GitHub cloud mark while the matrix says `logo_avoid`. It is not prompt-eligible until the conflict is resolved; a generic unbranded remote would require a brief-level change.
- The v1 selection ledger records the first proposal: 19 active selections plus held F-51. Review found a text-dependent legend in A-8 and exact-term/value dependencies in E-25, G-5, I-5, J-81, and J-100. A-8 remains held. Proposed v2 replaces A-8/F-51 with E-27/G-1. E-25/E-31/I-5 facts are anchored in the article. G-1 has its five inputs and Context Window boundary in the article, but the authored figure memo also specifies 128K→1M; those values are absent from the article body. Hold G-1 until a human confirms omitting that figure-only fact or adds it to approved article prose; do not draw the values. Human confirmation is still required before using qualitative-only imagery for E-27 (the IQ100/~80 values are only in the figure instruction), G-5 (model/value mapping), J-81 (exact speeds), J-100 (six-stage order), H-8 (eight-stage mapping), and F-6 (formatting concept vs literal syntax). All stay pending in the v2 ledger.
- Proposed selection v2 is recorded in `ledgers/ponchi_simplification_batch_002_selection_v2_20260927.csv`: 20 unique rows, with E-27 replacing A-8 and G-1 replacing F-51. Chapter counts are E4 / F2 / G5 / H2 / I2 / J5. Rows retain their own prompt-readiness gates; the 20-slot quota does not force a candidate. Other available candidates E-26, E-33, H-58, and J-70 stay in reserve; G-9 remains a minor-edit item.
- Five entries reached internal candidate generation: E-25, E-30, G-44, H-6, and I-3. Candidates are 1774×887 (2:1), with prompts, hashes, and provenance in the sidecars and `ledgers/ponchi_simplification_candidate_ledger_20260927.csv`. E-25 and H-6 pass the current image, color, and independent semantic/style gates but remain pending human selection. G-44 is clear in the independent 200px review, while its automated bounding-box coverage is 0.443 against the 0.50 review threshold. E-30 and I-3 each reached the two-revision cap: palette normalization made the color audit pass but introduced visible speckling; E-30 v2 has a color-review flag and I-3 v2 fails the color audit. Both remain partial holds; do not continue prompt retries. The candidate v3 paths, hashes, and outcomes are recorded in both ledgers.
- E-31/G-14/G-16/I-5/J-71の5 sidecarは独立プロンプトレビューに合格し、各候補・入力prompt・SHA・監査履歴を記録。Batch 002の20枠は維持し、本文スコープ不一致のF-102/J-90、人の判断が必要なE-27/G-1/G-5/J-81/J-100/H-8/F-6、参照根拠待ちのJ-12はholdのまま。

#### Batch 002 内部候補の現在地

| ID | 最新候補 | 独立監査・機械ゲート | 次の扱い |
| :-- | :-- | :-- | :-- |
| E-31 | v3（修正2/2） | 意味/style HOLD。5本のmeterが塗られ、透明画素75.05%、色監査0.061910 fail | 修正上限。内部hold |
| G-14 | v3（修正2/2） | 意味/style PASS。色監査0.011872 review | 内部保留。色review未解消、採用しない |
| G-16 | v2（修正1/2） | 意味/style/寸法/bbox/color PASS。色監査0.000859 | 人の選定待ち。自動採用しない |
| I-5 | v3（修正2/2） | 意味PASS、style HOLD。色監査0.059222 fail | 修正上限。内部hold |
| J-71 | v3（修正2/2） | 意味/style HOLD。SSD保存データの読み順が逆に読め、列に人物が重なる。色監査0.063911 fail | 修正上限。内部hold |

全候補はimage_genのネイティブ寸法1774×887で出力され、元finalの1254×627とピクセル数は異なるが、2:1の縦横比は維持。リサイズはしていない。機械画像監査は候補標準の1774×887で実施した。画像はすべて実験フォルダにあり、`assets/ponchi/final/` とproduction採用状態は未変更。
- G-1 remains held for human confirmation: the figure memo requests 128K→1M, which is absent from the approved article body. The other semantic/number/order/syntax gates remain pending as listed above; candidate generation is limited to rows whose sidecars passed review without those gates.

#### Batch 004 — 30件の横断トリアージ（2026-09-27）

- 未監査294件から章別の目安 A2 / B4 / C4 / D4 / E3 / F3 / G3 / H2 / I2 / J3 で抽出。旧品質スコアは章内の抜き取り順だけに使い、候補判定には使っていない。
- 3人が10件ずつ、現行WebP・本文・ロゴ資料を照合。30件すべて1254×627で、実ファイルSHA-256はキュー値と一致。本文の正本は `ledgers/entries.csv:path`。
- 一次は `simplify_candidate` 11件、hold 19件。候補全件とhold標本4件を独立確認し、G-8をholdへ変更。最終は候補10件、hold 20件。
- 4候補（C-82/G-40/I-1/I-41）の内部画像を作成。C-82 v3・G-40 v3・I-1 v3・I-41 v3はいずれもHOLD。C-82/G-40/I-1は純白背景と指定色の機械条件を満たさず、I-1 v3は200pxの意味・人数は通るが中央ブリッジの立体感も残る。各項目とも修正上限に達し、再生成を停止した。I-41は予約clearspace侵入と意味ずれもあり、上限到達で停止。
- F-84はsidecarが独立レビューに合格して内部候補v3まで進んだが、予約領域 `[1239,14,1731,321]` に151,044画素中132,334画素があり、四隅も純白でない。HOLD・修正上限。公式Ghosttyカード利用も未承認。
- B-27はレイアウトの人判断待ち。B-30はロゴなし内部ベースに限定。C-81は2人のうちどちらを残すか未確定でhold。公式素材の合成・採用・公開は未許可。

#### Batch 005 — 次波の対象選定・候補レビュー（2026-09-28）

- 未棚卸し264件を母集団に章別比例30件を選び、画像SHA・本文ブリーフを30/30件照合。3人に10件ずつ割当。
- 一次は候補6件、keep 1件、hold 23件。独立確認でI-50をブランドmatrix未登録等によりholdへ変更。最終は候補5件（F-59/G-33/J-13/F-5/J-41）、keep 1件、hold 24件。非候補標本5件はholdを確認し、18件はprimary-onlyで閉じた。
- F-59/G-33/J-13/J-41のsidecarは独立prompt review合格、F-5は固定キャラ数の不一致でprompt-readinessをhold。4候補を内部生成しv3まで独立レビューした。F-59/G-33/J-13/J-41は意味の一部が通るものもあるが、純白背景・指定色の不一致や例外関係の欠落が残り、修正上限2/2で全件HOLD。これ以上生成しない。
- ロゴなし内部候補に限り、ロゴ合成・本番採用・公開は未許可。F-5は人物数を人が確定するまで生成しない。

#### Batch 006–007 — 横展開の継続運用（2026-09-28時点）

- Batch 006の30件を監査し、最終判定は `simplify_candidate` 7件（B-20/E-4/F-58/F-91/G-39/G-43/J-16）、hold 22件、keep 1件（B-13）。候補11件すべてと一次hold19件のSHA-256昇順20%標本4件（D-55/D-53/F-87/J-10）を独立確認した。H-3/I-22/J-2/J-43の4件はキャラクター対応・公式ブランド・brief意味核の不一致を理由にholdへ変更した。
- Batch 006の現行画像30/30件は1254×627、選定・triage台帳と実ファイルSHAが一致。`entries.csv:path` とbrief実在も30/30一致。ロゴ要件matrixの行も30/30件で確認済み。選定台帳の割当スナップショットSHA-256は `6023AE1D3A27E0AE90E35354E4E445FB8D9165B037D5BF74EC0F6F7B2108284E`、一次監査反映後の選定台帳SHA-256は `e543a66ec375be49adc4ee352648bd5af10bb2456b4cd7b6e0f2a6925bf059b6`、triage SHA-256は `faf62b881e55d390da841d8715ae8b6d8b465bce26bc9b25a9dd498efe636811`。
- Batch 006候補7件分のsidecarを作成。独立prompt reviewはE-4/F-58/F-91/G-39/G-43/J-16の6件がPASS、B-20はVercel素材の取得日未記録でHOLD。6件をv1→v2→v3まで生成し、各v3を別担当が200px意味・構図、文字/ロゴ、寸法、背景で最終確認した。6件すべて意味の主要改善は確認できたが、厳密な不透明純白キャンバス条件に失敗し、修正上限2/2で最終HOLD。各v3のSHA・レビュー根拠・次の扱いをcandidate ledger、中央queue、sidecar、個別履歴、strict-white監査へ同期済み。これ以上生成しない。標準の許容色監査PASSは純白合格の代替証拠にならない。B-20は素材の出典・取得日を確認するまで生成しない。
- Batch 005完了後の未棚卸し204件からBatch 007を比例抽出。現行画像SHA・brief path・brief実在は30/30照合済み。章枠は A1 / B4 / C2 / D3 / E1 / F8 / G2 / H1 / I1 / J7。一次監査をA/B/C各10件、二次監査をA/B各15件の独立レーンで完了した。F-171/G-47/J-62を独立裁定し、B-15/D-26/J-4のprimary文言も修正後に再確認済み。最終判定は候補29件、keep 1件（G-30）。
- Batch 007の対象には未登録だった一般概念のlogo_avoid行を追加し、B-40/C-83/D-45/F-11/F-34/F-171等はローカル公式素材と現行適用状態をbrand auditに合わせて同期した。C-83は正本タイトルを `AI時代の羅針盤` に修正。個別利用条件が未確認の素材は、取得日・出典・hashをsidecarへ記録したロゴなし内部ベースまでに限る。
- Batch 007の一次・二次監査30/30件と例外3件の独立再確認が完了し、選定台帳と中央queueへ同期済み。最終候補29件、keep 1件（G-30）。候補29件から全10章を含む20件をprompt wave 001に選定。15件のv1.3 sidecarを独立レビューし、14件PASS、1件HOLD。E-23のキャラクター同一性、A-4の固定キャラクター削除、公式素材の取得日4件の計6件は人の確認待ちとして生成対象外。残り14件はsidecar/source/reference SHAを二台帳で照合済み。
- Prompt wave 001は、内部生成を許可された14項目すべてで初回候補を生成済み。生成物は合計22枚（D-40/F-50/F-34/F-54は各v1–v3、残る10項目は各v1）。すべてexperiments内に保存し、採用・公開は未実施。E-23の同一性、A-4の固定キャラクター削除、公式素材の取得日4件の計6 readiness holdは引き続き生成対象外。
- 現行候補の厳密白背景ゲートは14項目すべてHOLD。四隅/登録点とfail-fastを機械記録し、白塗り後処理もmaskによる失敗の隠蔽も行わない。color許容監査PASSは背景合格の代替にならない。白背景だけでなく、疑似文字・予約ROI侵入・不要UI/マークを項目別に独立レビューする。
- D-40/F-50/F-34/F-54はcandidate v3で修正上限2/2。4件とも厳密白でHOLDし、追加生成なし。F-34には疑似文字と予約ROI侵入、F-50には戻り矢印の予約ROI侵入、D-40には厳密色/白、F-54は白不合格（v3の独立候補レビュー待ち）が残る。
- v1独立候補レビューでF-40/F-11/G-47/H-57/J-17/J-62/J-1/J-21もHOLD。F-40は疑似文字・bbox不足、F-11は製品mark/cloud示唆と予約ROI、H-57は第二タイムライン/疑似文字/予約ROIと色REVIEW、J-62は質問カードの重複、J-1はbrain/疑似文字/?/visual cue、ほかは白不合格が主課題。これらは修正上限内の対象プロンプト修正を独立レビュー後に検討する。F-40/F-11のv2とJ-1/J-62のv2は草案中。
- I-80/J-15は初回候補レビュー待ち（両方とも機械的な厳密白に不合格）。J-21のレビューでは左右比較/意味と色・幾何はPASS、白背景はHOLD。F-54 v3も独立レビュー待ち。次は各itemの独立レビューを確定し、修正可能な問題だけv2 promptへ反映して再度別レビューを行う。修正上限後も候補HOLDを保ち、すべて人の最終判断待ち。
- 監査のcontact sheetは項目別experimentsフォルダへ保存する。以前の監査で `docs/ponchi_batch_audits/ponchi-color-audit-contact-sheet.png` を上書きしてしまったが、その時点のD-40シートはD-40実験フォルダに保存済み。共有シートの元データは復元できていない。2026-09-28のJ-17 v3監査でも初回コマンドが `--contact-sheet` を欠いて同じ共有シートを再上書きした。直後に正しい `--out-md` とitem-local `--contact-sheet` を付けて再実行し、J-17のCSV/Markdown/contact sheetを実験フォルダに作成した。再上書き前の共有シートはこのworkspaceに複製がなく、復元できないため現状を保持する。以降は全色監査で項目別 `--contact-sheet` を明示し、共有シートは出力先にしない。
- Batches 002–004は35/90、Batch 005は5/30、Batch 006は7/30、Batch 007は最終候補29/30で、合計76/180（約42.2%）が候補確定。次の30件の容量見積りは候補約13件、非候補標本約4件、二次レビュー約17件、一次を含む監査記録約47件。これは容量計画であり候補ノルマではない。
- Batch 007も終了すると未棚卸しは174件の見込み。現行204件の章別件数は A1 / B24 / C15 / D22 / E5 / F52 / G17 / H10 / I9 / J48。標準比例配分の見込みは A1 / B4 / C2 / D3 / E1 / F8 / G2 / H1 / I1 / J7、終了時は A1 / B20 / C13 / D19 / E4 / F44 / G15 / H9 / I8 / J41。Batch007の確定数で再計算する。
- 各波で画像SHAかbriefが不一致なら当該行をholdし、正本を確認するまで候補化しない。同じ手順誤解が二次監査で2件以上あれば次波の前にチェック票を直す。候補判定基準は緩めない。

### 次波から全件棚卸しまでのロードマップ

- Batch 006の6候補はv3最終レビュー済みで、全件HOLD・修正2/2として閉じた。レビュー記録と画像hashは同期済みで、再生成しない。Batch 007の二次監査・裁定も30/30件完了。意見が割れた行は第三者裁定までholdにし、裁定前にプロンプトや画像を作らない。Batch 006の背景不合格を反映したprompt template v1.3は独立レビューPASS（2026-09-28）。同条件を確認する `scripts/ponchi_background_mask_audit.py` は独立コードレビューで透明度メタデータとメモリ使用の指摘を修正し、最終レビューPASS・構文確認済み。prompt wave 001とBatch 008以降に適用し、各sidecarは別途独立レビューする。
- 174件・30件単位という旧見込みは更新前の概算として扱う。Batch 008選定後の次波母集団は、中央rollout queueで `latest_triage_disposition` が空かつ `rollout_status=needs_complexity_triage` の現行finalに絞り、記事statusが `ready` の126件と `needs_review` の6件を分けて数える。過去バッチのtriage結果が残る46行は、表示上の `needs_complexity_triage` だけを根拠に再選定しない。次の20件を作るたび、母集団と章別比率を最新キューから再計算する。
- 各30件波は3レーン×10件の一次監査、候補全件＋非候補のSHA-256決定論20%標本の二次監査を行う。候補の prompt-ready 件数だけを最大20件の次の制作波にする。
- 直近180件の候補率76/180（42.2%）から次30件の候補約13件を作業容量の目安に置く。これは出力目標ではなく、keep / hold / 空き枠をそのまま許容する。
- 毎波の締めに選定・一次・二次の各CSV、中央452行キュー、brand matrix/audit、sidecar、candidate ledger、画像ハッシュを同時に同期する。次波の開始条件は未解決の素材・意味条件が台帳へ明示され、現行finalとの照合が済んでいること。
- 生成直後に要求された2:1寸法・不透明度・四隅の厳密な `#FFFFFF` を独立ゲートで確認する。sidecarへ事前登録した背景点はfail-fast専用とし、背景PASSは候補と同寸の検査maskが示す全背景画素が許容差なしの `#FFFFFF` である場合に限る。maskは図形と輪郭アンチエイリアスだけを除外し、独立レビューで大きな空白領域を隠していないことを確かめる。palette許容差や全体の白画素率は代替にしない。Batch 006の実出力は1774×887。修正は最大2回で打ち切り、背景失敗を理由に上限後の再生成や後処理での白塗りをしない。

### 横展開の運用単位と次の棚卸し

| 単位 | 入力・作業 | 出口条件 |
| :-- | :-- | :-- |
| 棚卸し | 現行 final の実ファイル、SHA-256、`entries.csv` の正本ブリーフを照合。30件を章横断でサンプリング | 30行すべてに画像所見、brief path/hash、ブランド仮判定を記録 |
| 一次監査 | 3人の監査者に10件ずつ割当。全員同じ200pxチェック票を使う | `keep` / `minor_edit` / `simplify_candidate` / `hold` を根拠付きで付与 |
| 独立ゲート | 候補全件を別監査者が意味・レイアウト・公式素材・文字禁止で再確認。hold/keep/minor_editの20%を別の人が再点検 | サンプル数は切上げ、`SHA-256(batch_id|entry_id)` 昇順で決めて台帳に記録。意見不一致はhold |
| 20件以下の候補波 | 章の偏りとprompt-readinessを確認して最大20件選ぶ | 全項目で source hash、意味、読み順、削除範囲、文字の扱い、ブランド、人物参照が埋まる。足りなければ枠を空ける |
| 候補生成・評価 | 1項目1枚から開始し、問題を指定した修正は最大2回。並列に意味・200px/シリーズ調・機械・ブランド監査 | 根拠・出力hash・監査結果・人の判断が全て台帳へ記録される |

Batch 006の30件は一次・二次監査が完了。Batch 007はpilotと監査済み186件を除いた204件から30件を比例選定し、一次・二次監査30/30件と例外3件の再確認を完了した。結果は候補29件、keep 1件（G-30）。候補のうち20件はprompt wave 001、残る9件は次の候補waveに回す。過去スコアは章内の確認順にだけ使い、候補判定は現行画像・本文・ブランド条件の根拠で決める。

横展開で共通化するのは、入力照合・200px判定票・ブランド/文字適格性・独立レビュー・候補名付け・停止条件です。各エントリの意味、読順、削除要素、公式素材、固定キャラ参照は個別sidecarに残し、共通プロンプトだけで一括生成しません。

初期分類では、現行finalなし61件とF-43を別レーン、pilotの既存final19件を人の選定待ち、非pilotの過去昇格84件とその他287件を既存finalの棚卸し母集団に置きました。過去昇格84件のうち81件は初期 `historical_promotion_current_asset_needs_triage`、3件（A-6/I-81/J-76）はBatch 001の候補・保留状態です。Batch 001は17件を個別レビュー対象として処理し、3枠を空けています。

## 3. 作業の流れ

### Stage 0 — 正本とルールを一本化

次の候補生成を増やす前に、スタイル・ブランド・画像寸法の基準を一箇所へまとめます。

- 著者決定済みの見た目は、図解・背景を白・濃紺・黒・薄青（#EAF1FB）の4色基調にします。固定キャラの参照画像にすでにあるニュートラルグレーの服・体色だけはそのまま保持し、図解や背景へ新たに広げません。正規化・色監査が受け入れる9色はスタイル定義そのものではないため、この例外以外へ広げないように合わせます。
- 旧ブリーフには #F3F6FB と #EAF1FB、グラデーション禁止と青系グラデーション許可の差が残っています。後段の著者決定（#EAF1FB、青と薄青の範囲だけでグラデーション可）に統一し、古い指定を文書・スクリプトから解消します。
- 実際のポンチ枠に合わせて2:1を正式な比率にする。1254×627は比較・監査用の縮小画像、長辺1500px以上の生成元は保存用マスターとして区別する。
- `docs/ponchi_brand_asset_rules.md` はタイトルに会社・製品・モデル名がある場合、公式ロゴを原則対象とし、素材や利用条件が未確認なら保留としています。pilot READMEの「意味が通ればロゴを省略」という扱いと衝突するため、例外条件を確定します。
- ロゴや公式マークを画像生成させない。必要なら `docs/brand_usage_audit.md` で公式素材の取得元・ローカルファイル・ハッシュ・取得日・使用条件を記録してから後合成します。公式素材を未取得の項目は `blocked_brand_asset` としてプロンプトも候補も作りません。素材取得済みで使用条件だけ未確定の項目は `internal_base_only` に限り、内部ベース候補の比較までに止めて採用・公開へ進めません。
- 公式ロゴの合成後は色監査でロゴ領域と生成本文を分けます。ブランド色が色監査を通ることだけで使用許諾を推定しません。

### Stage 1 — 現行画像の複雑さを仕分け

旧品質スコアの `線密度`、既知padding、色・濃淡のフラグを候補抽出に使い、現行finalを改めて200pxで見ます。ファイルサイズや密度スコアだけでは再生成を決めません。密度監査の `review` は人の目で理由を記録する合図です。

各候補に次を記録します。

1. 200pxで主題を短い一文に言い表せるか。
2. 主役と補助要素の順番がすぐ分かるか。
3. 縮小時に読めない細部・重複した小アイコンが意味を足さずに残っていないか。
4. 何を削ると主題の区別まで失われるか。
5. 判定は `keep` / `minor_edit` / `simplify_candidate` / `hold_for_brand_or_semantics` のいずれか。

意図的に複数の関係を説明する図は、情報が多いという理由だけで簡素化しません。削除対象を具体的に説明できる画像だけを候補化します。

### Stage 2 — 過去候補の照合と20件バッチ

まずpilot-001の人による選定を終え、その結果を台帳へ戻します。非pilotの過去昇格84件は現行画像で再確認しますが、内訳は81件が未棚卸し、A-6/I-81/J-76の3件はBatch 001の候補・保留レーンです。Batch 001の17件とBatch 002/003の60件は新規棚卸しに重ねず、各候補・保留レーンで進捗を追います。

新規の候補作成は、複雑さが確認された項目に限って1件ずつ行います。A-6例で使ったテンプレートv1とv1.1は履歴として残します。次の項目は独立レビューPASS済みの `assets/ponchi/experiments/prompts/ponchi-simplification-v1.3/00_template.md` を基準にし、項目別sidecarも生成前に独立レビューします。既存pilotのプロンプトは履歴として変更せず、生成前に `INTENDED_MEANING` / `LAYOUT_AND_READING_ORDER` / `MUST_KEEP` / `TEXT_FREE_TRANSLATION` / `FACTS_RETAINED_OUTSIDE_IMAGE` / `REMOVE` / ロゴ・キャラクター条件を埋めたエントリ別コピーを作ります。初回候補の後に行う修正は、監査で特定された問題を対象に最大二回までにします。同じ測定可能な問題が二回後も残る場合は `partial` として保留し、その項目への反復編集を止めます。ID順の連続抽出ではなく、優先度順の中から章の偏りを抑えて最大20件に区切ります。

初回20件の章別配分は、候補としての意味・ブランド条件とprompt-readinessが揃った行から決めます。章別件数は作業目安であり、候補を埋めるための自動選定ではありません。次の30件は現在の未棚卸し量を反映したA2 / B4 / C4 / D4 / E3 / F3 / G3 / H2 / I2 / J3を目安にします。

pilot-001を除く既存finalは371件です。Batch 001の17件とBatch 002/003の60件を差し引いた新規棚卸し母集団は294件で、すべてが再生成対象とは限りません。単純な上限見積りなら最大15波（20件×14波＋14件）ですが、`keep` / `minor_edit` / `hold` は候補生成から外します。新規画像が必要な61件とF-43は別レーンで進めます。

### Stage 3 — 監査と人の選定

各バッチの候補と現行画像を、同じ1254×627・同じ200px縮小で比較できるコンタクトシートにします。監査は独立レーンで並列に行います。

- 意味: エントリの内容と候補が一致するか。特に省略で必要な区別を壊していないか。
- 縮小表示とシリーズ調: 200pxで主題が分かり、既存画像の白地・線・余白・青の濃淡と揃うか。
- 文字なしの意味保持: 専門語・数値を画像から省く場合は、記事本文の事実アンカーと、図に残る具体的な関係をsidecarで照合する。読める文字を無断で許容したり、本文にない事実を画像用に捏造しない。
- 機械監査: 寸法、色、密度、誤生成テキスト・ロゴ、ロゴ余白。
- 公式素材: 出典、ローカルファイル、改変の有無、使用条件。

機械監査の `review`、未解決の意味確認、未確認のロゴ条件は人へ戻します。密度の `pass` や寸法の合格だけで採用しません。最後に人が `採用` / `再修正` / `見送り` を明示するまで候補のまま維持します。

## 4. 最終画像へ進むゲート

昇格できるのは、意味確認、200px可読性、シリーズ調、必要な機械監査、公式素材条件、人の明示承認がすべて揃った行だけです。現在の `scripts/ponchi_promote_lightweight_candidates.py` は人の承認状態を検査せず `assets/ponchi/final/` に書き込みます。また `--dry-run` でも出力台帳を上書きし、状態を `promoted` と記録します。このスクリプトは現状で使いません。承認列、全監査列、入力ハッシュ、出力先を検証してから書き込むゲートに直し、実際に何も変更しないdry-runができることを確認します。

## 5. 次の実行順

1. pilot-001の20件について、人の意味確認と採否を完了する。F-43は新規画像レーンとして区別する。
2. v1.2テンプレートとBatch 002選定v2は独立レビュー済みで、方針・入替判断は了承された。了承は個別プロンプトや画像生成の承認を含まず、項目別のreadinessは引き続き確認する。
3. E-27/G-1/G-5/J-81/J-100/H-8/F-6について、数値・順序・構文を本文へ追加するか、概念図に縮約するか、holdするかを人が確定する。本文にない正確な比較や順序を画像だけに残そうとしない。
4. E-31/G-14/G-16/I-5/J-71は候補生成と最大2回の対象修正、独立意味/style監査、機械監査を実施済み。現在地は上表のとおり。G-16は人の選定待ち、G-14は色review、残り3件はhold。E-30/I-3を含め修正上限到達候補は再生成しない。人の判断を要する行はholdを維持する。
5. Batch 004–007の選定・一次・二次監査、Batch 007の選定キュー同期は完了。Batch 006は候補7・hold22・keep1、prompt PASSは6件で、内部候補6件のv2まで作成済み。Batch 007は候補29・keep1で閉じ、候補20件をprompt wave 001へ送った。
6. Prompt wave 001の残作業は、14件のPASS sidecarと正確な入力/sidecar hashを照合後、その14件の内部候補を各1案生成し、候補ごとの意味・200px/シリーズ調・機械監査と台帳記録を行う。監査で確認した問題に限り最大2回修正する。出力はexperimentsに保存し、現行finalへ触れない。E-23は人がロボットの固定キャラクターIDと削除可否を決めるまで生成しない。
7. A-4の固定キャラクター削除、B-15/B-50/C-1/D-26の公式素材取得日、その他本文・事実・人物同一性が未確定の項目は人の決定までHOLD。Batch 004のC-82/G-40/I-1とF-84、Batch 005のF-59/G-33/J-13/J-41およびBatch 006の修正上限到達候補は再生成しない。残るBatch 007候補9件は次のprompt waveへ回す。Batch 008以降の棚卸し枠と章配分は現時点の未棚卸し数・直近の独立レビュー誤解から再計算し、候補ノルマを置かない。過去昇格記録は現行画像確認を省略する根拠にしない。

既存の `docs/ponchi_20_item_batch_workflow.md` や進捗概要にある350件の記述は現行件数と一致しないため、横展開の完了数には使いません。

## 6. 2026-09-28 進捗と次波への引き継ぎ

### Prompt wave 001 の確定状況

- 20枠の内訳: 人判断・出典確定待ち6件（A-4 / B-15 / B-50 / C-1 / D-26 / E-23）、過去の修正上限到達4件（D-40 / F-50 / F-34 / F-54）、v3候補まで進めた10件（F-40 / F-11 / G-47 / H-57 / I-80 / J-1 / J-15 / J-17 / J-21 / J-62）。人判断待ちを埋めるための生成枠は設けない。
- 10件のv3プロンプトは独立レビュー10/10 PASS、内部候補生成10/10完了、独立候補レビュー10/10完了。候補はすべて最終修正2/2でHOLD。厳密白fail-fastも10/10で、背景mask・白塗り・色補正は一件もない。追加生成を停止する。
- 個別所見: F-40の実行/play cue欠落とROI侵入、F-11のcanopyによるROI侵入、G-47の左余白越境、H-57の擬似UIとROI侵入、I-80の立体サーバー過剰表現、J-1の文書風記号と絵の識別性、J-15の禁止した第2入力泡、J-17の椅子/机による左3%余白違反、J-21の承認済み構図からの退行、J-62の質問応答経路・回答者・端末種別の曖昧さ。各レビュー票と機械数値を項目別記録へ結んだ。
- F-40 / F-11 / H-57は公式ロゴを合成していない内部ベースのみ。ロゴ予約ROIは一般clearspace比率で代用しない。F-11のレビュー時に既定サイズ/一般ROIの不一致が判明したため、1774×887の実寸と項目別ROIで再監査した。監査スクリプトの既定値は1254×627と右上の一般領域なので、次回から実寸・項目別ポリシーCSVを必ず指定する。
- 正本はwave ledger（20行）、中央rollout queue（452行）、candidate ledger（45行）、項目別sidecar・生成記録・監査票。v3 candidate path/hash、レビュー、prompt本文SHA、現在のsidecar SHA、2/2上限とHOLDを同期した。 候補レビュー票に記録したsidecar全体SHAはレビュー時点のスナップショットであり、後から生成/確定記録を追記した8件と、HOLD状態を整理したF-40/J-17では現在値と異なる。prompt本文SHAは変えておらず、現行のsidecar全体SHAはwave/queueと実ファイルで一致させている。

### 次の20件へ横展開する手順

1. `entries.csv`と現行finalの実ファイルから母集団を作る。記事/図版ブリーフ、現在画像、公式素材の出典・取得日・利用条件、固定キャラクター参照をIDごとにSHA照合し、未確定情報は人判断待ちにする。
2. 現行絵を200pxで独立確認し、主題・読順・残す要素・削る要素を固定する。ロゴ等の予約領域は正確な矩形として記録し、人物や役割が複数なら参照素材と役割を個別に対応づける。
3. 共通テンプレートはチェック欄と停止条件に限定し、意味・レイアウト・数量・役割・禁止形状・ROIは個別sidecarに記録する。prompt本文SHAに結んで独立レビューし、sidecar全体SHAは生成記録を追加した後の値を台帳へ同期する。
4. 生成画像は編集せずexperimentsへ複製し、生成元と同一SHAを確認する。実測寸法、色モード、LOGO_MODE、項目別ROIを明示して監査する。予約ROIがある場合は正確な矩形を別監査し、汎用右上掃引では代替しない。サイズの違う既定値での結果は使わない。
5. 色監査ごとにitem-localな`--contact-sheet`と`--out-md`を必ず指定する。J-17 v3初回コマンドが共有 `docs/ponchi_batch_audits/ponchi-color-audit-contact-sheet.png` を再上書きした。正しい項目別再実行でJ-17の成果物は保存できたが、上書き前の共有ファイルは復元不能。この事故記録は維持し、共有シートを出力先にしない。
6. 四隅・登録点・3%周縁の厳密白を最初にfail-fast検査する。失敗した場合はHOLDで止め、mask・白塗り・後処理を行わない。通過後だけ同寸法maskと輪郭の独立確認、palette/geometry/ROI、200px意味・シリーズ調監査へ進む。色PASSや汎用clearspace PASSを他ゲートの代用にしない。
7. 1項目あたり生成は合計2回まで。上限時に必須条件が残れば停止して再生成枠へ戻さない。候補の機械監査と独立レビュー後も、人の明示選定と別の採用手続きが必要。候補生成・監査の完了だけで`assets/ponchi/final/`を変更しない。

Batch 007の所見を反映した共通テンプレートv1.4ドラフトは `assets/ponchi/experiments/prompts/ponchi-simplification-v1.4/00_template.md` に分離した。共通手順は独立レビューPASS（2026-09-28、`/root/review_wave001_b`）、現行SHA-256 `B43DAC3C12DE12CEEE699E834BA9F2C00787FD08C4A916814353D67A585FF299`。各項目sidecarの独立レビューは別途必須。Batch 007の10候補は内部HOLDとして閉じ、採用判断は人の段階に残す。


## 7. Batch 008 triage proposal and cross-review (2026-09-28)

- 未選定・未監査の現行final 152件を母集団にし、章別母数比例で20件を提案した（B2 / C2 / D2 / E1 / F6 / G2 / H1 / J4）。A/I章は未監査プールに残っていない。過去品質スコアは章内の抽出補助だけに使用。
- 20/20件について現行WebPのSHAとブリーフ実在を確認し、実画像・200×100縮小で一次確認した。別レーン担当者による独立クロスチェックは16/20件。proposal ledgerに担当者・根拠・次アクション・prompt readinessを記録。
- クロスチェック後の複雑さ判定は `simplify_candidate` 10件（B-11 / B-14 / C-8 / C-54 / E-20 / F-3 / F-7 / F-16 / F-90 / G-12）、`hold_for_brand_or_semantics` 7件（D-20 / D-25 / F-14 / F-44 / G-4 / H-56 / J-103）、`hold_for_scope` 3件（J-97 / J-83 / J-114）。F-44 / H-56 / J-97 / J-83は一次holdのまま二次レビュー未割当。J-114はfrontmatterの`reader_level: 6`・`research_only`と刊行外コメントを照合して対象外へ訂正。
- B-14/C-8は一次監査がブランド/意味ゲートと複雑さを混同したため、独立レビュー後に「簡素化候補」とprompt readinessを分離した。B-14はGenspark official faviconのみ手元にあり、full lockup取得/overlay reviewが未完了なのでlogo-free internal baseに限定。C-8のlogo-less `logo_avoid`はbrand auditの根拠に合わせてmatrixへ同期済み。4製品群を保ち、Microsoft AIと別会社OpenAIの境界を図で明示する。
- 意味を正すために図の主張をbriefへ合わせる再構成も候補に含むが、事実の補完はしない。C-54の現行briefは5節目（AlexNet 2012 / OpenAI設立 2015 / GPT設計参画 / 2023ガバナンス / SSI設立 2024）。GPT設計参画にbrief記載の年がないため年を創作しない。F-7は同じデータによるJSON/YAML比較へ再構成。G-4は現画像のdictationとSystem/User promptのbriefが別概念のためhold。
- D-20のbriefにある「GPT-5 current flagship」は更新が必要。2026-09-28のOpenAI公式ページはGPT-5をprevious model、GPT-6をlatestとして案内（[GPT-5 model page](https://developers.openai.com/api/docs/models/gpt-5)、[GPT-5 page](https://openai.com/gpt-5/)）。著者がbriefを更新するまでhold。D-25もGPT系列とClaudeを同じ系譜に含める誤読リスクがあるため事実整理が先。J-103はJ-103を含む5項目共通のscope-map geometryが確定するまで単独で進めない。
- ブランド要件matrixはB-14/C-8/F-14/F-16/F-90の監査済み5行だけ、ローカル素材/取得記録またはlogo_avoidの一次根拠へ同期した。B-14/F-14/F-16/F-90の利用条件はなお未確認。
- ロゴのある最終合成画像をimagegen入力へ渡さない。B-11/B-14/F-16/F-90などはプロンプト草案を作る場合もlogo-free internal baseにし、公式素材は別overlayゲートへ分離する。利用許諾や公式素材の確認状況を画像生成で推定しない。
- G-4/G-12について、現行brief・simplification queueは`[済]`/`ready`を指す一方、`ponchi_generation_batches.csv`のBatch012行は旧`[人書]`/`needs_review`を記録している。Batch012を当時の履歴として保持し、候補プロンプトは現行brief path/hashに結ぶ。G-12の画像生成前にはこの履歴行との関係を再確認する。既存の行を無言で上書きしない。
- Batch008は20件の選定提案を継続し、全件`human_decision=pending`、`final_adoption=not_authorized`、`generation_status=not_authorized`とする。独立クロスチェック済み候補10件のうち、v1.4で安全な参照入力がある6件（C-8/C-54/E-20/F-3/F-7/G-12）のsidecar草案をexperimentsに作成し、独立prompt review待ち。B-11/B-14/F-16/F-90は現在finalがロゴ合成済みで、v1.4に適合するロゴなし編集入力がないためsidecarを作らない。別途作成したtext-only new-base addendum v1.5 draft（後述）の独立レビュー後にsidecar作成可否を判断する。候補10件の残りの生成・採用ゲートは未完了。
- Batch008の非候補10件のうち16/20件は独立クロスチェック済み。F-44/H-56/J-97/J-83はprimary-onlyのまま二次確認待ち。全20件のselection proposal、triage結果、sidecar path/hash、prompt status、次アクションを `ledgers/ponchi_simplification_batch_008_selection_proposal_20260928.csv` と452行中央queueへ同期した。
- Batch008終了前でも、次波の選定準備はできる。中央queueの古いBatch002/003/004由来46行は、各一次triage ledgerとdispositionを照合してstatus/next actionを修正済み。`latest_triage_disposition` が空欄かつ `needs_complexity_triage` の132件にはreadyが126件、needs_reviewが6件ある。次の20枠はreadyだけから章別比例で配分し、四捨五入の残りを比例端数順に配る。枠はB2/C2/D2/E1/F6/G2/H0/J5。sidecarまたは生成へ進むのは、Batch008の個別プロンプト独立レビューと入力ゲートが閉じた後に限る。

## 8. Batch 008 prompt execution status and safe input expansion (2026-09-28)

- Batch008の6 sidecarはすべてドラフト。独立レビュー第1回はF-7/G-12がhash-bound PASS、C-8/F-3がPASSだが参照SHA・共通基盤の注記を追加、C-54/E-20がHOLD指摘を修正済み。C-8/C-54/E-20/F-3の新SHAを再レビューへ送り、F-7/G-12は第1回のPASS SHAから変更していない。各ラウンドのreview status/sidecar SHA/findingsを選定台帳へ記録し、中央queueにも反映。現時点の生成許可数は0、現行finalへの書込み数は0。
- B-11/B-14/F-16/F-90のブロッカーは図の意味ではなく、v1.4の入力モードが「ハッシュ一致のロゴなし画像を編集する」一択である点。current finalを画像生成へ渡さない条件は維持する。新規text-only baseを作り、項目sidecarだけを入力にする分岐を `assets/ponchi/experiments/prompts/ponchi-simplification-v1.5-draft/00_text_only_new_base_addendum.md` に作成した。これは独立template review待ちの追加案で、v1.4を変更せず、生成承認でもない。
- text-only分岐は current final を比較・監査メタデータだけに使い、実際のtool inputに添付しない。固定キャラクターが必要な場合は承認済みの該当キャラクター参照だけを添付する。ロゴ素材、ロゴ合成画像、過去イラスト、コンタクトシートは入力にしない。配置は人が確定した項目sidecar内に完全記述し、`source` や「元画像と同じ構図」を認めない。テンプレートと個別promptの独立レビューを両方通過しても、最初の出力は内部候補に限る。
- Batch008の次に使う母集団は、最新triage dispositionの空欄と現行final/ready条件で定義する。旧triage済み46行は参照台帳との照合後にstatusを修正済み。更新日時点でreadyの未triage母集団126件、needs_review 6件を記録し、次回の選定前に再計算する。
- 生成、logo overlay、`assets/ponchi/final/`への変更、採用、公開は未実施。Batch008全件の人の決定はpendingのまま。

## 9. Batch 009 selection proposal (2026-09-28)

- Batch009 proposalは、中央queue上で `rollout_status=needs_complexity_triage`、`latest_triage_disposition` 空欄、`entry_status=ready`、現行finalありの126件から20件を抽出した。`needs_review` の6件は選定母集団から外し、人手/本文状態の確認待ちに残す。
- 章別割当はHamilton比例配分 B2 / C2 / D2 / E1 / F6 / G2 / H0 / J5。各章内で `SHA-256("ponchi-simplification-rollout-009|entry_id")` 昇順に選び、過去品質スコアは選定にも候補判定にも使わない。
- 20/20件についてcurrent finalの実ファイルSHA、画像パス、`entries.csv` のready状態・human brief path、brief実在を照合した。proposalは `ledgers/ponchi_simplification_batch_009_selection_proposal_20260928.csv` にあり、全件 `proposed_triage_only` / `pending_triage` / `human_decision=pending` / `generation_status=not_authorized`。
- Primary 200px triageは10件ずつの2レーンで開始。レーン結果と独立cross-checkが揃うまでprompt sidecarを作らない。候補数ノルマは設けず、hold/keep/minor-editは空き枠のままにする。


## 10. Batch 008 prompt traceability and Batch 009 horizontal rollout (2026-09-28 update)

- Batch 008のC-8/C-54/E-20/F-3 sidecarに、Round 1指摘と承認済みCharacter B参照SHA `6CE81EA4957F8E2522292E5F48CAB2CE718A5E807024F755794079C7283F9C99`を反映した。Round 2ではC-8 `1AE3EB8EDB1A3A80A2B2B4306E83D5F64A07B7057FFB557B244388E7208A7A90`、C-54 `710FFEFBC784DC60CB9763326BEF84DCD68B122F64FBEA3039AB0D9453968146`、F-3 `3CED15FD47C319753EB38B70FFF4E9FB8D4C389AE7A1C6B73379A4B0151D320E`がHOLD、E-20 `280C1EA0C5D19074BFD9B6DF6E291310658FCEE7BF0DD80217753038D5A18A3A`がPASS。HOLD所見に基づく3件の改稿と再レビューを開始したため、上記3 SHAは履歴値で現行版ではない。F-7/G-12はRound 1 PASSのhashから変更なし。レビュー判定と対象SHAはproposal ledgerへ、中央queueには最新のレビュー状態と所見を同期した。生成許可0件。
- Text-only addendumの独立Round 1はHOLD（SHA `95B35B769F8BBFC41C00D7552E2ABD9BFFF6A794C4AE876A7C7EA75D6AD5E751`）。CURRENT_SOURCE_VISUAL_NOTESとREMOVE内容がcurrent final由来の視覚情報をgenerator promptへ持ち込む余地があると指摘された。source path/hash/visual notesのprompt assembly完全除外と、REMOVEをbrief・承認済policy・human-confirmed targetの明示テキストに限定する修正はRound 2 PASS（SHA `8835CAED30C63D8390E1D99B529B28BA77650D6E46AB827FFD0D108C880351CC`）。後続の台帳監査で、status headerを含むSHA `AAECE013BC51E9498188D5F80ADB9E9D718A1E71122EE90DFC3FC3195511EC7C`のreviewer欄が作成担当者と同一と判明したため、これは独立レビュー要件を満たさず、template PASSを撤回した。ステータス行だけを修正した現行SHA `EAE5B6A45A35A234C2FAC2738149DE68CB31F71058931305E280126241E45578`は独立レビュー待ち。B-11/B-14/F-16/F-90のsidecarも個別レビューが必要で、テンプレートPASSを得ても生成許可にはならない。
- Batch 009の一次監査は20/20完了。現行final画像SHAと対応brief SHAを記録し、20件すべてのlogo-free base実ファイルをSHA・1254×627で照合した。primary-only判定は簡素化候補14（B-31/C-12/D-22/F-15、F-20/F-181/F-80/G-36/G-34/J-24/J-88/J-104/J-87/J-108）、minor edit 1（C-50）、hold 5（B-33/D-44/E-51/F-62/F-212）。一次所見、brief hash、base path/hash、ブロッカー、review担当をproposal ledgerに記録。全20件が独立cross-review待ちでfinal disposition未確定。
- Batch 009のブランド/レイアウト共通ブロッカーは、B-31/B-33/D-44/F-15/F-62の公式assetと別overlay候補、F-212のno-logo判断。5件はmatrixに `official_logo_overlay_candidate_unreviewed` を追加し、asset path/SHA、別実験の `overlay_audit=not_reviewed`、current finalがlogo-freeであることを明記した。状態表現は独立matrix review PASS（SHA `84355D402E824D30C32E8A011F7A24009C86B6C69B7E442E0B6B2556EBA21607`）。利用条件とoverlay監査は未確認。F-212は公式style guideが区別するOpenAPI SpecificationとOpenAPI Initiativeを混同しないよう汎用仕様書図・`logo_avoid`を追加。matrix review PASS。C-12は `required/source_review_required` と旧ledger `logo_avoid/no asset` の矛盾が未解決。各項目の図意図・character・ROI等のprimary blockersも記録済み。これらが残る項目はsidecar前に解消し、current finalをimage inputにしない。素材やlogo-free baseの存在は使用許可や意味確認の代わりにならない。
- 追加のscope検査でJ-24/J-88/J-104/J-87/J-108はfrontmatter `reader_level: 6`、自己学習棚・刊行スコープ外の明記を確認した。一次complexity所見は探索記録として残し、現刊行スコープではsidecar/生成/採用をblock。別目的の一般的な画像改善対象として続ける場合も、範囲を正本で確認してから再開する。
- 横展開の反復単位は「20件提案→2レーン×10件の一次監査→別レーンの全20件クロスレビュー→合意したDispositionのみ中央queueへ同期→prompt-ready候補のみ次工程」とする。各batchでimage SHAとhuman brief SHAを両方固定し、`ready`以外は抽出対象外にする。意味・ブランド・キャラクター・ROIの未解決事項はcandidate扱いでも `hold` の次アクションへ残し、prompt readinessを独立して閉じる。次batchを選ぶ前に母集団・章別quotaを中央queueから再計算する。各段階で `human_decision=pending`、`final_adoption=not_authorized`、`generation_status=not_authorized` を維持し、画像生成はレビュー済みsidecarと別途明示ゲートがそろった項目だけに限定する。

## 11. 横展開の再現手順と監査追記（2026-09-28）

### 次バッチの選定前に行うこと

- Batch009は「ready」かつ未triageの126件から選んだ後で刊行スコープを検査し、J-24/J-88/J-104/J-87/J-108がreader_level 6・刊行外と判明した。現選定の履歴は保持し、この5件は探索記録のみ。Batch009内で別IDに差し替えない。
- 同じ126件を正本`ledgers/entries.csv`の`notes`と各briefのfrontmatterで再点検した結果、29件に`Lv6自己学習シェルフ（刊行外）`が明記され、すべてJ章のreader_level 6だった。除外後のスコープ内母集団は97件。次回選定ではスコープ外行を章別quota算出前に除き、母数・Hamilton配分・hash順をその時点の中央queueから再計算する。
- `entry_status=ready`は刊行スコープ内の証明ではない。`entries.csv`の刊行外注記とfrontmatterが一致しない行、範囲不明の行は`scope_review_required`として抽出から外す。`experience_level: research_only`だけでは除外しない。例としてB-24はその値を持つがreader_level 2-3で、刊行外注記はない。
- current queueの項目状態は452行中央rollout queueに置き、20件の根拠はbatch別proposal CSV、共通ルールと例外はこの計画書に置く。手作業の重複台帳は作らない。複雑さ判定・刊行スコープ・ブランド/prompt readiness・人の判断・生成/採用許可を別々に記録する。

### 直近レビューから反映する共通ルール

- Batch009 slots 11-20の独立クロスレビューは、複雑さについて全10件`simplify_candidate`で合意。J-24/J-88/J-104/J-87/J-108は刊行外なのでproduction側では`hold_for_scope`。F-20/F-181/F-80は公式素材・現final状態・matrix記録・clearspaceに不一致があり、G-36/G-34はbrand matrix行がない。これら5件はブランド条件が台帳と根拠で一致するまでprompt作成を止める。10件とも人の採否・生成・最終採用は未承認。
- Batch008のC-8/C-54/F-3 Round 3はexact sidecar SHAに対してHOLD。全3件の参照brand-matrix SHAが古く、現行reviewed SHA `84355D402E824D30C32E8A011F7A24009C86B6C69B7E442E0B6B2556EBA21607`に更新が必要。C-8はbriefのMicrosoft AI中心・4製品放射配置へ合わせて修正してから再レビューする。C-54/F-3は意味内容は整合しているが、SHA更新後に再レビューする。生成は未許可。
- Text-only addendum v1.5の初版`AAECE013BC51E9498188D5F80ADB9E9D718A1E71122EE90DFC3FC3195511EC7C`はreviewer欄が作成者自身だったため、独立reviewとしての記録を撤回した。current file SHA `740CA346ABE0D4E2CF87F1A6E072F9DD373CC467A63D4C77D88FD99353102B67`は`/root/batch008_secondary_a`が再確認してPASS。レビュー状態はledgerで管理し、個別4 sidecarのexact SHA reviewは別途必須。テンプレートPASSは画像生成・採用許可ではない。

### 1波の標準手順

1. 中央queueの現行画像・brief・entry状態を照合し、刊行スコープを先に確定する。未解決行は除外する。
2. scope内の現行final/未triage/readyから最大20件をHamilton配分し、章内は`SHA-256(batch_id|entry_id)`順で選ぶ。候補数を埋める目的の追加選択はしない。
3. 一次監査を2レーン×10件に分け、全20件を別担当がクロスレビューする。異論はHOLDにし、合意した複雑さ dispositionだけをqueueへ同期する。
4. scope・意味・公式素材/利用条件・character・ROIに未解決があればprompt readinessはHOLDのままにする。prompt-readyになった項目だけsidecarを作り、templateとitem sidecarをそれぞれexact SHAで独立レビューする。
5. 画像生成は別の明示ゲート後に限る。1項目最大2回、内部experimentsに保存。人の採用判断がない間は`assets/ponchi/final/`を変更しない。

## 12. 監査を踏まえた横展開の再開順（2026-09-28）

### 現在の同期状態

- Batch009の独立クロスレビューは20件分そろい、proposalと中央queueに同期済み。slots 01–10の再判定によりC-12/F-15のcomplexity分類も分離・更新した。matrixのSHA `B00A9B3C…` に対する独立レビューではE-51の誤分類とC-12/G-36の旧generation ledgerとの不一致が見つかり、FAIL。修正版SHAを別担当が再レビューするまでprompt-ready判定に進めない。
- slots 01–10のreview結果を台帳へ同期した。再判定後のBatch009全体は、複雑さ候補9、minor edit 2、内容/意味のhold 4、刊行scope外のhold 5。C-12はcomplexityをminor edit、F-15はsimplify candidateとし、どちらもprompt/brand/ROI gateとは別に記録した。prompt-ready候補はC-50/F-212の2件だが、matrix修正後の独立PASSまではsidecarを作らない。全20件は人の決定待ち、生成未許可。
- ロゴ要件マトリクスは、B-31/B-33/D-22/D-44/F-15/F-20/F-62/F-80/F-181の現行finalに公式マークが見えること、別のlogo-free baseが存在すること、旧generation ledgerが `official_logo_applied / overlay_audit / not_reviewed` を記録することに合わせて改稿中。これは利用条件の確認、overlay監査、採用、公開を意味しない。
- F-20/F-80/F-181の1254×627 baseではclearspace `[686,0,520,180]` に純白でない画素がそれぞれ2,766 / 2,555 / 128。F-15/F-62はそれぞれ4,429 / 1,817画素が純白でなく、2,733 / 1,355はRGB<245の厳しい閾値で数えた値。純白条件は満たさない。該当sidecarは領域を空けて再監査するまで止める。汎用範囲の白監査は、この矩形の代用にしない。
- G-34は複数provider共通の実行概念として `not_needed/logo_avoid` を追加した。G-36はClaude.ai固有のArtifact機能なので `required/official_logo_source_review_required` に変更し、Claude公式markの機能適合・個別利用条件・配置を確認するまでは合成しない。どちらもmatrixの独立レビューまではsidecarを止める。
- 旧matrix SHA `B00A9B3CFC6CF0E7A78296B7FC7381A1D26E36D4DBC935BFC0230104D4E60F6F` の独立レビューはFAIL。E-51/C-12/G-36の旧 `logo_avoid` との食い違いを履歴として修正し、Batch010の不足行とmark/sourceの事実も補完した。`812B028F...A767F9` はE-34とF-121訂正前、`950CCA...BB607` はstatus定義の幅が狭い版として失敗履歴に保持する。source review定義とD-22の素材SHAを直した最新matrix SHA `E37D9B0322A6E82675B4630A724747D54C194BD3D9EEE7D5F6E812EB20F802CA` は、2026-09-28に `/root/batch008_secondary_a` が35対象行・素材パス・明記SHAを独立照合してPASS。これは要件表の内容確認であり、個別ロゴの利用許可・合成・採用承認ではない。Batch009刊行範囲15件とBatch010全20件にreviewer/date/current SHAを記録し、刊行外J 5件はmatrix審査N/Aのままにした。

### 次の実行波

1. 最新matrix SHA `E37D9B0322A6E82675B4630A724747D54C194BD3D9EEE7D5F6E812EB20F802CA` の独立レビューPASSをB9刊行範囲15件とB10全20件に同期済み。J-24/J-88/J-104/J-87/J-108はscope外のため審査N/Aを保つ。
2. 最初のsidecar波はBatch009のC-50/F-212（両方 `ready_for_sidecar`）。v1.3テンプレートで検証済みlogo-free baseを固定し、C-50は匿名話者と4節timeline、F-212は中央OpenAPI仕様書から3出力への一方向分岐・Engineer A/Character Cを必ず保持する。
3. 完成した各sidecarの本文SHAと入力image/brief/matrix SHAをproposal/中央queueへ記録し、別担当がexact SHAに対する独立prompt reviewを行う。PASSするまで画像生成はしない。生成許可、人の採否、final昇格も引き続き未承認。
4. B9の他の13 scope内項目はprompt-readinessの個別blockerを解消してから順に準備する。旧clearspace値、意味hold、未解決公式source/use条件、人物同一性が残る項目はsidecarを作らずHOLDを保つ。
5. Batch010はmatrix review済みだが、B-61/F-83比較意味、C-3/C-4/D-14/D-41/D-4/E-34のfacts、ブランド利用条件、F-60/F-121のclearspace、G-23のsource/use、F-151/G-35の意味holdなどitem gateが開いている。blocker解消前にsidecarを作らない。
6. 次batchはBatch009のsidecar gate・中央queue同期後に、central queueと`entries.csv`からscope内・ready・現行finalあり・未triageを再抽出する。最新母集団・Hamilton章配分・chapter内hash順を保存し、最大20件単位で監査する。

### 2026-09-28 Batch009/010台帳同期

- Batch009/010のproposal・queue再監査は独立担当PASS。両バッチ40件で正準path、current final/brief SHA、final disposition、prompt readiness、human/generation/adoption gatesが一致。B9の古いtriage/status 10件、C-12/E-51の旧logo blocker、J 5件のbrand statusを修正した。人の判断は全件pending、generation/adoptionは全件not_authorized。
- Batch010のsecondary reviewとG-35第三者裁定を同期。G-35はbrief内矛盾のためHOLD、F-121は構図を確定してbrand-use/clearspaceのみ残す。matrix PASS後、C-50/F-212のsidecarを別担当が作成中。sidecar独立レビュー前に画像生成しない。

### 波ごとの記録・停止条件

中央queueには最新triageバッチ、complexity disposition、prompt readiness、sidecar SHA/review、generation authorization、candidate SHA/review、人の決定、採用状態をそれぞれ記録する。proposalは同じ列をバッチ単位で保持し、image/brief/matrix/sidecarそれぞれの入力SHAを記録する。二つの台帳で差があれば次の波を開始しない。

進捗数は「監査対象 / 独立クロスレビュー済み / 複雑さ候補 / prompt-ready / sidecar PASS / 生成許可 / 内部候補 / 人が採用 / final昇格」に分けて集計する。現在Batch009/010は各20件の選定・一次・独立クロスレビュー・proposal/queue同期を完了。matrix PASS後のprompt-readyはC-50/F-212の2件、sidecar独立PASSは0、生成許可0、人の採用0、final昇格0。

### Batch010 選定済み・一次/二次監査完了、matrix PASS・item blocker解消待ち

- 2026-09-28に中央queueと`entries.csv`から抽出母集団を再構築した。ready・現行finalあり・未triageは106件。刊行範囲外reader level 6を24件除外し、刊行範囲を確定できない項目は0件、scope内は82件だった。全82件でbriefのfrontmatter `reader_level` を確認した。
- Batch010は20件を章別Hamilton配分 B3 / C2 / D3 / E1 / F8 / G3（H0 / J0）で選定。章内は `SHA-256("ponchi-simplification-rollout-010|entry_id")` 昇順。選定した20件は一意で、current final画像SHAとbrief SHAを実ファイルで照合済み。
- 詳細なID・slot・根拠・reader level・各SHAは `ledgers/ponchi_simplification_batch_010_selection_proposal_20260928.csv`。同時に中央queueの20行を `batch010_selected_pending_primary_triage` として同期し、二重選定を防ぐ。
- Batch010の一次監査・二つの独立クロスレビューは20/20完了。複雑さ判定は `simplify_candidate` 16件、`minor_edit` 2件、semantic hold 2件。B-61/F-83の比較意味・単位、B-32の3役、C-3の4〜5関係などprimary所見をsecondary evidenceで修正した。F-60のscreening ROIはitem-specific clearspaceでないと訂正し、F-121は中心比較＋3補助cueとして整理。G-35はbrief内矛盾のため第三者HOLD。matrix SHA E37D9B...は独立review PASS、proposal/queueにreviewer・SHA・日付を記録済み。ただしE-34のscore/date/variantとmark source/use、各公式markの利用条件、個別clearspace、F-151/G-35意味hold等が残るため、B10からsidecarを作らない。legacy queue path/statusの不一致は履歴差分として記録。全件 `human_decision=pending`、`generation_status=not_authorized`、`final_adoption=not_authorized`。

## 13. 2026-09-28 現行プロンプト波の同期状態と次の手順

本節は、前節までの「sidecar作成中」「sidecar review 0件」などの同日スナップショットを更新する。履歴は残し、現在状態は本節を正とする。

### Batch009: 初回sidecarレビュー完了

- 現行ロゴ要件matrix SHA `E37D9B0322A6E82675B4630A724747D54C194BD3D9EEE7D5F6E812EB20F802CA` は独立レビューPASS。C-50/F-212は `not_needed / logo_avoid` の根拠と一般OpenAIブランド監査をプロンプトへ反映した。
- C-50 sidecar `assets/ponchi/experiments/prompts/ponchi-simplification-rollout-009/C-50.md` の現行SHA `A8BD9E8CA0EFDBD94EA20893BE5D49CC72C43980051B0F1B5130B6781CA3B83E` は `/root/review_c50_sidecar` が2026-09-28にPASS。4つの元カード位置とtimeline nodeを1対1対応させ、空の吹き出しへ置換する。旧3版のREQUEST_CHANGES/HOLDと各SHAをsidecar review historyに保持した。
- F-212 sidecar `assets/ponchi/experiments/prompts/ponchi-simplification-rollout-009/F-212.md` の現行SHA `F920B5A7301AA2272597EB0C0DD1598C29E236001AD0838FEA4C4F98718F4C61` は `/root/review_f212_sidecar` が2026-09-28にPASS。単一仕様書からdocs・generated code skeleton・mock serverへの3本の一方向出力とCharacter A/Cを保つ。以前の部分確認PASSと、全文テンプレート監査でのHOLDを記録し、全テンプレート本文を展開した版をreview対象にした。
- 両sidecarともv1.3の全共通prompt fieldを埋め、共通image-edit prompt本文と実行・レビュー規則を全文収録。レビューはプロンプトだけを対象とする。画像候補は存在せず、生成・採用・公開・リリースは未許可。
- Batch009 proposalと中央queueにsidecar path/current SHA/reviewed SHA/verdict/reviewer/date/findingsを同期済み。proposal側は `prompt_reviewed_sha256` / `prompt_reviewed_by` / `prompt_review_date` / `prompt_review_findings`、中央queue側は対応する `latest_prompt_reviewed_*` 欄を使う。reviewed SHAは必ず当該時点のsidecar SHAと一致させ、改稿時は旧判定をhistoryへ残したうえで新SHAの独立レビューをやり直す。

### Batch010: sidecarレビュー済み項目と停止中の項目（追記で更新）

- F-210とG-48は現行matrixレビューPASS後の項目監査を行い、ロゴなしbaseの実在SHAと1254×627寸法を再照合した。`ledgers/ponchi_simplification_batch_010_selection_proposal_20260928.csv` と中央queueへbase path/SHA/statusを同期し、両件を `ready_for_sidecar` に更新した。F-210はrequired/type/allowed-valuesの構造検証に限定し、意味的正しさを主張しない。G-48はprovider中立のshape制約だけを示し、既存ロボットをsourceどおり保つ。
- F-4/F-42/F-81もmatrixとlogo-free baseの照合はPASS。ただし人物・ロボットの扱いを確定できる証拠がそろっていない。人手確認を得ずに削除、追加、identity変更をしないため、`pending_character_policy_confirmation` に保留し、中央queueに理由と次アクションを同期した。matrix reviewは完了済みなので、現行statusはcharacter policyだけを示す。
- Batch010の5件すべてで `human_decision=pending`、`generation_status=not_authorized`、`final_adoption=not_authorized` を保持する。F-210/G-48は全文テンプレートのexact-SHA独立レビューPASS済み。生成は別途の明示認可待ち。

### 次回20件を選ぶ前に保存するselection snapshot

Batch011は過去の97件/82件という母数を再利用しない。中央queueと `ledgers/entries.csv` の当日版からscope内eligible poolを作り、次の順でsnapshotとproposalを保存する。

1. 各入力CSVのSHA-256と抽出日時を記録する。current-finalの実ファイルSHA、canonical briefのpath/SHAも各eligible rowで再照合する。
2. `entries.csv` notesとbrief frontmatterで刊行scopeを確認してからquotaを算出する。`reader_level: 6` の刊行外、scope不明、brief不一致、既選定・triage済み、current finalなし、非readyはpoolから除外し、除外理由をsnapshotに残す。
3. `ledgers/ponchi_simplification_batch_011_eligible_pool_YYYYMMDD.csv` にscope内eligible全行、chapter別母数、pool SHAを保存する。Hamilton比例配分と `SHA-256("ponchi-simplification-rollout-011|entry_id")` の昇順を再計算し、20件を超えない。候補不足ならslotを空け、scope外で補充しない。
4. proposal側にreader level、scope判定、画像・brief・matrix SHA、chapter quota、選定hashを保持する。中央queueとproposalのID/statusが一致しない場合は次工程を開始しない。

### 進捗の現行集計

Batch009/010は各20件の選定・一次監査・独立クロスレビュー・matrix確認を完了。sidecar独立PASSは4（C-50/F-212/F-210/G-48）、Batch010のcharacter policy holdは3（F-4/F-42/F-81）。生成許可0、内部画像候補0、人の採用0、final昇格0。画像生成と本番変更は別途明示ゲートを得るまで行わない。


### 2026-09-28 追記: Batch010 sidecarレビュー完了と横展開再開

- Batch010のF-210/G-48はexact SHAの独立レビューを完了し、proposalと中央queueへレビュー済みSHA・担当・日付・所見を同期した。現行matrix・brief・logo-free base・source hashesとv1.3全文テンプレートを照合し、sidecar review PASSとなった。
- F-210は初版SHA `44DC9EEBEEA0DE4F426B19F0AEB12AECA99AF95CF08636F0BCDCD8DCCBC0B684` が色モードのRGBA誤記でHOLD。実物のbase/raw/finalはいずれもRGBで、raw companion SHAも正準ファイルと再照合して訂正した。現行SHA `04F610BA05907C7427AC5C2168953F133975CD7760D83C91A4C796FFE486595F` は `/root/review_c50_sidecar` がPASS。Briefにない意味正しさの主張を追加しない制約、人物要件、8点確認と全面背景mask gateも確認済み。
- G-48 sidecar SHA `3C0D6DE186A2E223B830E6123938949671388050189A72C1742BDBE223394871` は `/root/review_g48_sidecar` がPASS。既存ロボット、Character Cの実参照添付、provider中立の意味を保持。MUST KEEPのbackticks欠落は非ブロッキングの書式差として所見に記録した。
- Batch009/010の40件のtriage・独立クロスレビュー・台帳同期を維持し、sidecar exact-SHA PASSは4件（C-50/F-212/F-210/G-48）。Batch010のcharacter policy holdはF-4/F-42/F-81の3件。全件の人による決定はpending、生成・採用・公開・final昇格は未許可。
- Batch011は過去母数を流用せず、現在のqueueと`entries.csv`からscope eligible poolを再構築し、入力SHA・完全なpool・scope除外理由・chapter別Hamilton quota・章内selection hash・各画像/brief SHAを保存した。独立監査PASS後に20件を中央queueへ`batch011_selected_pending_primary_triage`として同期した。生成・採用は対象外。


### 2026-09-28 追記: Batch011選定監査PASSと中央queue同期

- 独立担当 `/root/ledger_recheck` がeligible pool・20件proposal・入力SHA・画像/brief実ファイルハッシュ・scope・選定計算を再検証してPASS。matrix SHA `E37D9B0322A6E82675B4630A724747D54C194BD3D9EEE7D5F6E812EB20F802CA` は当日レビュー済み正本と一致。
- 現行入力SHAは選定snapshot作成時点でqueue `08677EAE1CC0EC7748BC0424D14018BDAA397E04AD975C01A7C91B01B3BD63BD`、`entries.csv` `C881D2DC0CC13EF25E488AC6E05CE184D53E6CC5EB567A4AEE1DF9F0EC55045D`、matrix `E37D9B0322A6E82675B4630A724747D54C194BD3D9EEE7D5F6E812EB20F802CA`。snapshotは中央queue全452行から、quota前候補103件→brief title mismatchのG-46/J-77を除外して101件→刊行外reader_level 6を24件除外してscope eligible 77件。scope不明0件。
- 章別poolはB13/C7/D10/E1/F23/G7/H2/I8/J6。20件のHamilton quotaはB3/C2/D3/E0/F6/G2/H0/I2/J2。章内は `SHA-256(ponchi-simplification-rollout-011|entry_id)` 昇順。pool hash `0436AFF27FC2FFA5FBC52E984360417491E38A286D7CA12135DA5383456A51CB`、selection-set hash `DF6D10E125E40D4F6C1CD4B55EDF416DF48ED8711C209E6258E1C429144CB32E`。
- pool snapshot `ledgers/ponchi_simplification_batch_011_eligible_pool_20260928.csv` のSHA `41851FB9A2BA6BA085CC7A82213C6C2CD08FB4005A283DB1756A57B9FEE140A2`。proposal `ledgers/ponchi_simplification_batch_011_selection_proposal_20260928.csv` のSHA `D923A7E9F9426B62708B57EEB6F22D1ABB13C2790946D1EC4600DF6A435DA38A`。独立監査は77件すべてのcurrent-final画像とbriefを再hashし、すべて一致。Proposalとpoolの選定ID・順序・quotaも一致する。
- 選定20件（B-60/B-2/B-1/C-7/C-15/D-2/D-70/D-46/F-35/F-101/F-111/F-130/F-13/F-52/G-22/G-6/I-13/I-11/J-51/J-106）を中央queueへ同期した。現行中央queue SHAは `7CD997162A88F89BE45C25854DD426690361FCB7C67EC5FAB17D54C2DF49CAC0`。全件 `human_decision=pending`、`generation_status=not_authorized`、候補未生成。複雑さprimary監査はこれから2レーン×10件で開始し、独立cross-review後にDispositionを確定する。
- 台帳独立監査では、20件以外へのstatus/note拡張はなく、snapshotに保存された現行状態・source SHA・IDは整合した。一方、同期前queue全体が未追跡で保存されていなかったため、自由記述`next_action`/`notes`の完全なbefore/after差分は第三者検証できない。次回のqueue更新では変更前の対象行全列スナップショットまたはインメモリ列差分を保全してから書き込む。
- 非ブロッカーとしてJ-127 briefのYAML frontmatterにインデント不整合が見つかったが、quota前候補外（current final不在）のため本batchには影響しない。`ponchi_batch_011_progress_summary.md` は別の `ponchi-batch-011` 画像生成レーンを指すため、名称の番号重複を混同しない。


### 2026-09-28 追記: Batch011 primary triage・独立cross-review完了

- 2レーンのprimary triageは20/20件を200×100で確認し、current-final/brief SHAを再照合。Lane A CSV SHA `C6CB93DBAF82A63576DF72BC284F7AA8BF831AD67308A16F63628A719971AECB`、Lane B CSV SHA `1D4A43CB37E6ADF8F467B0DD732D4FB1D63173A72EC9AAA010134B166385E872`。
- 独立cross-review CSV `ledgers/ponchi_simplification_batch_011_triage_crossreview_20260928.csv` SHA `F9AC0DAE8BDE80ABE2AD63FBB6C1AB3865AC3F5102FCF58892BF17999CC4BFA7`。20件すべての画像・brief SHAと一次所見を照合し、結果は12件agree、2件corrected、6件hold。全体cross-review verdictはHOLD（6件の個別blocker残存）。
- 最終complexity dispositionは`simplify_candidate` 12件、`minor_edit` 2件、`hold` 6件。C-7はTransformersをHosted platformの第4/5柱として扱わず、別のPython libraryとする。D-46は37B active parameter数から速度優位を推論する因果主張を削る。これらは修正所見としてproposalとqueueに記録。
- HOLDはC-15（職業コスプレとmatrix行不足）、D-70（白衣人物・限定出典）、F-13（Electron vs Tauri比較を現finalが示さない）、I-13（archived 2025とpresent-tense official claimの矛盾）、I-11（時点依存のGitHub MCP statusとmark/UI/ROI）、J-106（5兄弟共通scope-map geometry依存）。事実・policy・構図を解決し再レビューするまでpromptへ進めない。
- Batch011 proposalの現行SHAは `21242342177DEC7D79E5418F5910B6F730F163DCFEBBA6C3CA562D694DBA90CE`。中央queueの現行SHAは `4DDCC09D3C1C7D5F145CDB510F88F74C955D15E9024291E5A88FBDE09AFA131B`。proposalとqueueに一次/二次reviewer・所見・final disposition・blocker・次アクションを同期し、queue notesにも一次lane reviewerと各CSV SHAを追記した。全20件を`human_decision=pending`、`generation_status=not_authorized`、`final_adoption=not_authorized`に維持した。Batch011の新規candidate画像は0件。以前のpromoted lightweight履歴`prior_candidate_path`が残る5件（B-1/B-2/I-11/I-13/J-51）は履歴のまま保持し、新規Batch011 candidateと混同しない。
- queue更新は20 proposal IDだけに制限。更新時のin-memory full-row比較では変更列allowlistを確認し、proposal外の行に変更がないことをassertした。次回は同期前の対象行全列とcurrent queue SHAを別snapshotに保存し、同じ差分証跡を再現可能にする。
- 次工程は候補12件・軽微修正2件のprompt-readiness監査。全件でcurrent-finalは閲覧専用で、使えるexact 2:1 base、brief/facts、matrixのitem row、公式mark source/use/ROI、character referenceを確認してからsidecar作成可否を判定する。未解決ならHOLDを保ち、prompt PASSも画像生成許可とは扱わない。生成0、採用0、昇格0を維持。


## 14. 2026-09-28 Batch011 readiness完了と横展開同期

- readiness対象14件の独立監査記録は `readiness_review_20260928.csv` にlaneごとに範囲を分けて記録した。`/root/b11_readiness_verify` はgeneric laneのbase/brief/matrix/character参照を実ファイル照合し、公式素材laneではbase/公式asset hash・寸法・matrix・usage/ROI条件とF-35修正を確認してPASS。加えて `/root/b11_plan_review` が全14件のcanonical brief・記載済みCharacter A/B/C参照hashを実ファイルと照合しsupplemental PASS。結果は `ready_for_sidecar` 4件（F-101/F-111/F-130/G-6）、HOLD 10件（B-60/B-2/B-1/C-7/D-2/D-46/F-35/F-52/G-22/J-51）。triage段階のHOLD 6件（C-15/D-70/F-13/I-11/I-13/J-106）はreadiness対象に混ぜず、元のHOLDを維持した。
- Generic readiness ledger `ledgers/ponchi_simplification_batch_011_readiness_generic_20260928.csv` SHA `DEDE989E9D826A921E9212BD910CF4F370AE7B741AFA8B9FFAF982AD997542B4`。公式素材対象のledger `ledgers/ponchi_simplification_batch_011_readiness_official_20260928.csv` はF-35 canonical brief SHAの1文字誤記を実ファイル・proposalに合わせて訂正し、現行SHA `87ADC77AED3EFFCB8155CB95BAA64657015145C186131B0EC57AB1C3CAB19B98`。修正前SHA `EA7B1AFFBD589225620BCC5B03F53C7857192CE0575DA5C2AB28C14FE275F4BC` と独立reviewerの差分照合により、値の変更がその1文字だけで他のバイト・行は不変と確認した。
- 独立readiness review記録 `ledgers/ponchi_simplification_batch_011_readiness_review_20260928.csv` SHA `C0A9ED7072A46256189DA612E6B901D6978548C05B0ED7338199B3CFA7CF4111`。2つのprimary lane結果に加え、3行目でbrief/character referenceの補足hash照合を記録した。Genericは4 ready/3 hold、公式素材対象は0 ready/7 hold。F-52はgit pull設定によりmerge以外の挙動もあるためscope再確認、G-22/J-51はmatrix行不足（J-51は「文脈で正確さが保証される」とする表現を避ける）、公式素材7件は利用条件または対象mark許諾とbase SHAに結びつくROIが未解決のためHOLD。公式素材がローカルにあることは使用許諾を意味しない。
- F-101/F-111/F-130/G-6のbaseはすべて1254×627 RGB。current-finalは比較・由来確認のみで、入力画像には使わない。F-130ではユーザー・アプリ・認可サーバーを別主体として保ち、同意→認可コード→token交換の流れを描き、パスワード共有を示さない。F-111ではbefore/afterとキーボード/読み上げの概念を保ち、aria-labelのみからWCAG準拠を主張しない。F-101の16/48/256は例示とし、全OS/ブラウザーで常に最適サイズが自動選択されるとは断定しない。G-6はZero-shot/One-shotの差と例1件による形式の影響に限定し、正確性全般の向上を示唆しない。
- readiness結果・独立reviewer/date・lane ledger path/SHAはBatch011 proposalと中央queueへ同期済み。readiness同期前proposal SHA `21242342177DEC7D79E5418F5910B6F730F163DCFEBBA6C3CA562D694DBA90CE`、queue SHA `4DDCC09D3C1C7D5F145CDB510F88F74C955D15E9024291E5A88FBDE09AFA131B`。同期後proposal SHA `4A9369BED472D07D912581DB8074E68E675A60BA1917E207DB295EA62BA55E32`、queue SHA `D64163C1D9717862586234BB937E7A25B2537A38C013F15F6D470757A76B92E8`。review ledger path/SHAの補足追記後はproposal SHA `FB6FD7C30D2882D5EF41A5E48B354F2F2902902D4F686196610BEA486529044E`、queue SHA `A8F9043E6951847C0C100B3139E9607066572BEA9BB2D4224B3C40D0F62C2609`。human decision pending、generation/adoption unauthorized、current candidateなしを維持。
- 差分保全: 20件proposalの同期前全列snapshot SHA `A615819CF51C8351D4CDB6EE14A0DE85D2B16E7C59C3C2B9C6EC1D77BEB6254B`、queueの対象20行snapshot SHA `81B464941EC6DD0FD2DF58A4282361B381F8FE938D10BA15E03E45EFC92261E2`。同期処理内では現行452行全体のbefore/afterを比較し、選定外432行の値が変わらないことをassertしたが、保存した最初のpre-sync snapshotは対象20行のみで、第三者は432行の比較を再現できなかった。この証跡限界を記録し、次の更新前には全452行snapshotを保存した。readiness参照追記前の全queue snapshotは452行で、SHA `861D6E40D441AEE916B2E80A3E771733F9AA4A85C169E14070E9EAFDAD9D5124`。その更新では14行のnotesとproposal metadataの許可列だけを変更した。補足review参照へ差し替える直前にも全452行をsnapshot化し（`ledgers/ponchi_simplification_batch_011_full_queue_before_supplemental_review_ref_20260928.csv`、SHA `D64163C1D9717862586234BB937E7A25B2537A38C013F15F6D470757A76B92E8`）、queueは14行のnotes列だけを更新した。
- 各batchで最初に現行queueと`entries.csv`からscope内eligible poolを再構築し、chapter quota・selection hashを保存して20件を提案・queueへ同期する。その後の横展開順を固定する: (1) lane別primary CSVを凍結しSHA記録、(2)別担当cross-review、(3) base/brief/matrix/brand/character readinessをlane別CSVで記録、(4) readiness CSVのexact SHAを別reviewerが照合、(5)中央queue/proposalの更新直前に全行snapshot、(6)単独担当が対象20 IDと許可列だけ直列同期しfull-row diffを保存、(7)sidecarを作成したらexact-SHA独立review、(8)画像生成・採用・final昇格はそれぞれ別ゲートとする。未解決は候補枠を補充せずHOLDへ残す。
- 将来の効率化案として、`base_sidecar_ready`（意味・事実・人物参照・構図・logo-free base確定）と `overlay_ready`（公式素材出典/SHA・用途条件・対象画像ROI確認済み）を別状態に分ける案がある。現行v1.3の許容条件・既存承認との整合が未確定なのでBatch011公式7件のHOLDは変更せず、この状態分割を過去結果へ遡及適用しない。画像生成許可0、採用0、final昇格0。



## 15. 2026-09-28 Batch011 prompt sidecar PASS・同期完了

- v1.3の全文展開sidecarを4件作成し、現行exact SHAの独立prompt reviewがすべてPASSした。F-101 assets/ponchi/experiments/prompts/ponchi-simplification-rollout-011/F-101.md SHA 15CCEB7DDD0C648F6ACDECC48C7FE01482DB9029EE13706EBB2BA8284FD4027B、F-111同ディレクトリ F-111.md SHA 2DF5D1A157B54479F811DE28094DC1BA4D0FCFD1E185180D4446C36A6F76C07C は /root/b11_prompt_review_a、F-130 F-130.md SHA 82136C8A1DCABDB7E85EDD49FEAE41A6A03FA5EA0EAFEA3334AE0BC0500B9A95 とG-6 G-6.md SHA 15623AE07D650F84511010F334059C42299EB346540E506EE9BB772FE560757A は /root/b11_prompt_review_b が2026-09-28にPASS。全件でreviewed SHAはsidecar SHAと一致する。
- 独立レビュー履歴は ledgers/ponchi_simplification_batch_011_prompt_reviews_20260928.csv に11レコードで保存した。改稿前HOLDと中間SHAの判定も保持し、最新ラウンドだけが現行SHAのPASSを示す。review ledger SHAは 3379AB61A344B256D6C1B86A3AD55427249A9CFD6273C87543D18274EEF0DAA6。共通templateは assets/ponchi/experiments/prompts/ponchi-simplification-v1.3/00_template.md、SHA FEA6200B5C3936D6B3927B51417FB70938CEE12270E9607F2ECAF8A99691B833。
- レビューで見つかった食い違いを全4件へ共通修正した。「削除確認済み」と誤解される見出しを「削除提案・人手確認待ち」に変更。F-111は読み上げcueをAfter側の空の名前マーカーだけに、キーボードcueを両状態に共通する入力方法に固定。F-130は実験baseだけを編集対象とし、Character Aシートは別添のidentity参照、現行finalは添付禁止と明記した。
- Batch011 proposal/queueにsidecar path/SHA、prompt review verdict/reviewed SHA/reviewer/date/findings、base path/SHA、template SHA、review ledger path/SHAを同期した。同期前proposal snapshot ledgers/ponchi_simplification_batch_011_proposal_before_prompt_sync_20260928.csv SHA FB6FD7C30D2882D5EF41A5E48B354F2F2902902D4F686196610BEA486529044E（20行）、queue snapshot ledgers/ponchi_simplification_batch_011_full_queue_before_prompt_sync_20260928.csv SHA A8F9043E6951847C0C100B3139E9607066572BEA9BB2D4224B3C40D0F62C2609（452行）。同期後proposal SHA 7446A4B6A500842B7CB0B32A047D791046BDF990FE3157EAE9BCD91C93D3392F、queue SHA C8DECB5637FE3EABF8D863A2DE6084165C5D107453F4611651A9E526F15FC754。/root/b11_plan_review が全snapshotを独立比較し、変更行はF-101/F-111/F-130/G-6の4件だけ、新規列は対象外で空欄、既存列の変更は許可範囲内とPASSした。
- 4件の人の構図判断はpending、画像生成・候補採用・final昇格は引き続き未許可。candidate fileは0件。Prompt review PASSは画像や削除内容の人手承認ではない。Batch011の現行進捗は選定20件、triage simplify_candidate 12 / minor_edit 2 / hold 6、readiness 4 ready-for-sidecar / 10 HOLDに加えてtriage HOLD 6、prompt sidecar PASS 4、生成0、採用0。
- 横展開の次波は、前waveのqueue同期後に毎回current central queueとentries.csvからpoolを再抽出して20件を選ぶ。pool/quota/source hashesを先に独立確認し、2レーンの一次監査と全件cross-review、意味・brand/usage/ROI・character readiness、sidecar exact-SHA reviewの順で進める。今回の独立同期PASSを起点にBatch012の現行eligible poolと章別枠を再構築する。公式マーク許諾や意味・人物判断など人の決定を要する項目はHOLDのまま残し、Batch011の人手確認と各項目の明示的な画像生成許可を代替しない。
## 16. 2026-09-28 Batch012選定・中央queue同期と横展開進捗

- Batch012は中央queue 452行・`entries.csv` 452行から当日poolを再構築。eligible抽出前83件、source integrity確認後81件、刊行外reader_level 6を除外して57件。scope不明0件。章別eligibleはB10/C5/D7/E1/F17/G5/H2/I6/J4、Hamilton quotaはB4/C2/D2/E0/F6/G2/H1/I2/J1。
- Batch012 selection proposalはB-18/B-26/B-28/B-17/C-2/C-5/D-1/D-43/F-154/F-38/F-152/F-120/F-103/F-86/G-21/G-2/H-53/I-12/I-10/J-56の20件。`SHA-256(ponchi-simplification-rollout-012|entry_id)`章内順と選定hashを使い、過去quality scoreは選定に使っていない。pool content hash `A1DCC43B6E63D2414762A5244922E63267C09AA843F60B6B7B5A6549591984B9`、selection-set hash `52D92F59472DC3F68D77939CB9C8CF1BFF73C9E8B9B9D74DBE326A87D11DE6AB`。
- 入力snapshotはqueue `C8DECB5637FE3EABF8D863A2DE6084165C5D107453F4611651A9E526F15FC754`、entries `C881D2DC0CC13EF25E488AC6E05CE184D53E6CC5EB567A4AEE1DF9F0EC55045D`。eligible pool CSV SHA `EA2899972BA3473CEA6915FDC1CB02B40F83BA8684EE3EFF5BEBC8CB10967A85`、proposal SHA `ACD2B7C000BC3257EACA5C5F2FCA7E23A7780CB1B82DECF62FCD069AAA97B953`。
- 独立選定監査 `/root/b11_plan_review` は452行すべてのID・source hash、390個の現存current-final、452 brief、57件のeligibility、pool/set hash、章quota・hash順・20 slotsを再計算してPASS。選定段階のbrand matrix row presenceは未確認として記録されているため、このPASSはブランド、意味、prompt readinessの承認を意味しない。
- 中央queueへ20件だけを `batch012_selected_pending_primary_triage` として同期。変更前452行snapshot `ledgers/ponchi_simplification_batch_012_full_queue_before_selection_sync_20260928.csv` SHA `C8DECB5637FE3EABF8D863A2DE6084165C5D107453F4611651A9E526F15FC754`。同期後queue SHA `EC6B216A3E71054FEF93877F643D7FC2E6B076E71F4607B25DFDA93512C260E`。独立同期監査PASSでは、proposal 20 IDだけ・許可7列だけが変わり、非対象行変更0・許可外変更0。画像・brief参照と既存notes prefixは維持した。
- Batch012の現在状態はprimary triage 2レーン×10件を実行中。全件 `human_decision=pending`、generation/adoption `not_authorized`。selection PASSをreadiness PASSと取り違えず、まず意味・小サイズ表示・シリーズ様式・公式mark/source/use・character・exact-SHA ROIをitem単位で監査し、全20件cross-review後にだけcomplexity dispositionを確定する。人の意味判断、公式mark利用許諾、生成許可がない項目はHOLDにし、画像候補生成やfinal変更を行わない。
- 横展開の運用ルールは「同期済みqueueから当日scope poolを作り直す→全pool/sourceをhash固定→scope確定後にHamilton quotaとchapter内hash orderで最大20件選ぶ→2レーンprimary→全件独立cross-review→readinessを別記録→全行snapshotからallowlist同期」。未解決枠を20件に埋めるために補充せず、Batch011と同じくprompt review、画像生成、人の採用、final昇格を別ゲートで管理する。

## 17. 2026-09-28 Batch012監査・中央queue同期完了

- Batch012は20件のprimary・全件cross-reviewを完了し、統合台帳 `ledgers/ponchi_simplification_batch_012_triage_final_20260928.csv`（37列、20行、SHA-256 `319d008a227f12f04c396bd7138483b7d8fdb4d1a526c53af4a7408e9a536fb5`）に確定結果を集約した。最終処分は `simplify_candidate` 11、`minor_edit` 1、`hold` 8。triage narrativeのreadinessは `HOLD` / `Not ready`、中央queueの機械判定値は全20件 `hold`。human decisionはpending、generation/adoptionはnot authorized。
- 独立レビューは20 ID順、primary/cross-reviewとの対応、current-final/brief実ファイルのSHA、全件の停止ゲートをPASSした。レビュー後のfinal dispositionを20件すべて記録したが、これはprompt-readyや生成承認を意味しない。代表的な未解決事項はB-26のdeployment typeに依存するデータ処理地域の説明、B-28の競合するbase lineageとROI、F-152のGPL説明範囲、G-2の現finalとtokenization briefの不一致、G-21の `AGENTS.md` / `CLAUDE.md` の意味、J-56のGDPR/DPO条件である。公式根拠としてMicrosoft Learn、GNU GPL FAQ、欧州委員会、MCP reference server資料を照合し、各項目の次アクションに残した。
- 中央queueは変更前snapshot `ledgers/ponchi_simplification_batch_012_full_queue_before_triage_sync_20260928.csv` SHA `EC6B216A3E71054FEF93877F643D7FC2E6B076E71F4607B25DFDA93512C260E5` から現行SHA `E65C54B34831C5EAD8073FC83D304B7C1A7A9A4E334E24A2BF7CB72253AA7BEB` へ更新。独立差分監査で、Batch012選定20 IDの5列（rollout status、triage disposition、prompt readiness、next action、notes）だけが変更され、非対象432行・許可外列は不変と確認した。
- Batch012 proposalはSHA `2bc993e2d1eefcca439c58b9fcfdb8eece64760bb72f88ea2be8e5678a1f3771`。既存選定列のうち `next_action` 以外は変えず、triage・review参照の15列を追加した。人判断・生成・採用のゲートは開けていない。元のreadiness文字列は `HOLD` と `Not ready` が混在するが、記録を改変せず、queueの機械判定値は全件 `hold` に正規化した。
- 次の選定Batch013は、Batch012のtriage同期後の現行queueから母集団・scope・source hashを再構築し、独立監査が終わるまで中央queueへ同期しない。

## 18. 以後の横展開を簡潔に保つ標準案

### 画像の共通基準

- 各項目のbriefから「必ず残す意味・関係」を先に短く列挙し、重複UI、装飾ループ、意味を増やさない小パネルだけを削減候補とする。各図を一律の汎用レイアウトに置換せず、製品ごとの比較軸・工程・役割を保つ。
- 200×100表示で主題と必要な関係が読めるかを毎件確認する。小さくしてしか入らない説明は文字を縮めず、図の分割または構成の再検討を提案する。2:1の出力寸法、Ponchiの色・線・密度・キャラクター方針は共通の枠として守る。
- 公式ロゴは生成せず、ブランド要件表・公式素材の出所・個別使用判断・clearspace/ROIを独立して確認する。Character A/B/Cを使う場合は承認済み参照と役割を照合する。一時キャラは、人数自体が意味を持つ構図で、キャラクターバイブルの一時キャラ条件を満たす場合に限る。current finalを生成入力やキャラクター参照に転用しない。

### 20件バッチのゲート

1. 現行queueとcanonical entriesから最大20件を再抽出し、公開範囲、画像/brief実SHA、章quota、決定論的な章内順を固定する。pool/選定を独立監査した後、選定予約syncを行い、対象IDの重複選定を防ぐ。
2. primaryは2レーン各10件までに分け、選定した全件を別担当がcross-reviewする。レビュー担当は自分のprimaryをcross-reviewしない。意味・製品事実・シリーズ様式・ブランド利用条件・キャラクター・個別baseのROIのいずれかが未解決ならprompt readinessをHOLDする。
3. primary/cross-review/readinessを確定した後、triage結果syncを別に行う。選定予約syncと結果syncのそれぞれで全行のpre/post SHA、許可ID/列、snapshot pathを記録し、独立差分監査がPASSするまで次段へ進まない。sidecarは全入力SHAと本文SHAを別担当がPASSした後だけ次段へ送る。
4. 画像生成、内部候補の評価、人の採否、`assets/ponchi/final/`への昇格は独立ゲートとして維持する。prompt review PASSだけで生成や採用を許可しない。

### queue/proposal同期の競合防止

- 選定予約syncとtriage結果syncは別々の更新単位とする。各更新の直前に、queue全行とproposal全行のsnapshotを各1つ保存し、path/SHAを記録する。同一バイト列のsnapshotは再複製せず、同じ不変snapshot path/SHAを参照する。
- 書き込み直前にcanonical queue/proposalのSHAを再計算し、保存snapshotのSHAと両方一致する場合だけ続行する。不一致なら書き込みを中断し、現行状態からpool/選定またはtriageを再確認する。古いsnapshotでcanonical全体を上書きしない。
- 更新CSVは一時ファイルに作り、行数・列・一意ID・許可対象ID・許可変更列・status gateを照合してからqueue/proposalを置換する。両方の`human_decision=pending`、`generation_status=not_authorized`、`final_adoption=not_authorized`を確認し、prompt readinessはtriage結果sync時だけ監査済みの個別判定へ更新する。置換が一部だけ失敗した場合はqueue/proposalの両方を直前snapshotへ戻し、両SHAを確認してから停止する。
- 更新後のqueue/proposal SHAと全行差分を保存し、独立担当が対象ID・許可列・非対象不変・人/生成/採用gateを確認する。selection syncと結果syncをそれぞれ独立にPASSさせる。

### 台帳の重複を減らす変更案

- current queueは最新状態、batch item ledgerは項目別判断、review ledgerは独立証跡、rollout planは共通手順と例外を正本とする。同じ所見全文を全てへ複写せず、queueには短いnext actionと正本ledgerのpath/hashを置く。
- 次batch以降、source queue/entries等の不変なbatch共通値を1行manifestへまとめ、item ledgerにはslot・ID・画像/brief SHA・scope・Dispositionなど項目固有値を残す案を試す。同期前の同一snapshotを別名で重複保存しない。既存Batch001–012の証跡は遡及変更しない。
- cross-review結果の新規語彙は `agree`（判定維持）、`correct`（根拠・blockerを訂正するがDisposition維持）、`reclassify`（Disposition変更）、`hold`（解決不能）に統一する。Batch012までの `corrected` 等の履歴値は編集せず、集計時のみ意味を対応づける。
- 横展開の成果数は「選定 / primary完了 / cross-review完了 / keep・simplify候補・minor・hold / prompt-ready / sidecar PASS / 生成許可 / human adoption / final昇格」に分ける。分母を埋めるための代替選定はせず、HOLD数を進捗不足として扱わない。
- 将来のmanifest案ではsource queue/entries/matrixのSHAに加え、共通template/sidecarのpath・SHAと独立reviewer/dateも一度だけ保存する。item ledgerには項目別SHA、例外、個別reviewer所見を残す。Batch013までは現行記録形式を維持し、manifest移行は旧履歴を変更せず別batchで検証する。

## 19. 2026-09-28 Batch013 triage・横展開ゲート完了

- Batch013はqueue/entriesからeligible 37件を再構築し、Hamilton配分B3/C2/D3/E0/F6/G2/H0/I2/J2、決定論的chapter内hash順で20件を選んだ。source queue SHA `e65c54b34831c5ead8073fc83d304b7c1a7a9a4e334e24a2bf7cb72253aa7beb`、entries SHA `c881d2dc0cc13ef25e488ac6e05ce184d53e6cc5eb567a4aee1df9f0ec55045d`、brand matrix SHA `e37d9b0322a6e82675b4630a724747d54c194bd3d9eee7d5f6e812eb20f802ca`、eligible pool SHA `ae4c28ecd15a87a3ef82c28646f41d49668f6c71c64c58a535dc019a3aa35fa2`。選定20 IDは `ledgers/ponchi_simplification_batch_013_selection_proposal_20260928.csv` に記録。
- Primary lane A SHA `c39b6972935f93d8f31844b7a9bedcdc1c8be339796b880db3faf462ffdc5dae`、lane B SHA `a174fa65eef306e4f257ee862e8f8e67a049231ab5dd283487b9247c99a537fd`。別担当cross-review lane A SHA `b5da0e8f840fb07c9261933eff7cef76ef1091276f73dcbc5cdc10c4a8073f1b`、lane B SHA `f8f909a4ae3f1b3921333bc49033fce6db326f5f61eed765c4c0d8e74cc68575`。review語彙はagree 12 / correct 6 / reclassify 2 / hold 0。D-11/D-42は画像の複雑度をHOLDとせず `simplify_candidate` に再分類し、事実確認はreadiness側へ分離した。F-9/F-100/G-3は過去のreviewer-side baseが存在しても入力許可されていないため、一次のprompt readiness PASSをcross-reviewでHOLDへ訂正した。
- Final ledger `ledgers/ponchi_simplification_batch_013_triage_final_20260928.csv` は20行・37列、SHA `28998663b9649b3a2ea5e3bf896f777d5398b6c5616be5340307148980c8c90e`。最終dispositionはsimplify_candidate 16 / minor_edit 4 / hold 0、prompt readiness HOLD 20。current-final/briefの実ファイル40件はproposalのpath/SHAと一致。Viteの現行bundle移行、Puppeteer MCPのarchive、Serenaの導入・release、sycophancyのdated historical scopeなど時間依存の記述は公式情報との再確認が必要。ブランドmatrix/brand audit間の不一致、ROI、承認済みbase不足、著者判断の必要な項目もHOLDに残した。
- 人のsimplification decisionは全20件pending、generation/adoptionは全件not_authorized。prompt sidecar・画像候補は0件。公式出典や記事本文、ブランドmatrix、人物方針、base入力許可を解決するまで各項目のpromptを作らない。
- 結果sync前queue snapshot SHA `0a01e330ceb5d0281fca1ffe8fae2633316fc02f8bc5d8690b61d57145c2885e`、proposal snapshot SHA `604f91c64ca86baf72108dcb92e94990f8660d2de39a2b8b3f9f9f478886a4ad`。同期後queue SHA `2b923d73f36485dfe598c7c1d8ea215f02c13ae2e94cdb6254587f4d05d97b7e`、proposal SHA `c73d1a78e56fc111a28fd7e9b5434960addc8ab0a02807db14503d1f752179ff`。同期diff `ledgers/ponchi_simplification_batch_013_triage_sync_diff_20260928.csv` は40行、SHA `d805d5af7be70892e390a6e45e9b2013d326d4f48f8efb92c08a7128b8863d20`。独立監査PASSでは対象20 IDだけをqueueの5列とproposalの16列で更新し、非対象432行・許可外列は不変。同期前snapshotとcurrent SHAを照合してから書き込み、human/generation/adoption gateも維持した。
- 次waveはBatch013同期後のcurrent queueとentriesからeligible poolを再構築し、前waveと同じselection/primary/crossreview/readiness/result-syncの段階を独立に実行する。現行finalや未承認の過去baseを入力に流用せず、prompt readiness PASSと承認済み入力baseの両方が揃った項目だけsidecarへ進める。

## 20. v1.6共通プロンプト改訂とBatch014選定・予約同期

- v1.3/v1.4とtext-only addendum v1.5を別担当がread-only監査し、200px可読性・意味保持・追加禁止の重複と、generator向け指示とsidecar/機械監査手順の混在を確認した。既存版は書き換えず、3層を分けたexperiment-only草案 `assets/ponchi/experiments/prompts/ponchi-simplification-v1.6-draft/00_template.md` を作成した。
- v1.6の共通テンプレ本文は、3%境界の丸め規則を含むSHA `4BCF885988500AAA8B15C17C658CF4639B25439A33B9AB2DD2BAD79EE6087B9C`で独立review PASS。200pxで識別不能ならHOLD、第三者ブランドの公式キャラクター禁止と承認済みPonchi参照の条件分け、長辺1500pxのネイティブ出力目標、全インク四辺3%内側と実寸検査を含む。境界の端数は `int(0.03*W+0.5)` / `int(0.03*H+0.5)`（0.5切り上げ）に固定した。現ファイルSHA `01A589092F2FC0791D44670BCD4447B8F8F372137DE75709A26C4F82E93BF270` はstatus行のみの最終版で、`/root/b11_plan_review`がこの現SHAの再確認をPASSした。item sidecar・生成・採用・overlay・公開は未許可のままとする。
- Batch014は現行queue 452行からpre-scope候補43件を再構築。brief/titleなどsource整合性を通過した41件から刊行範囲外reader_level 6の24件を除外し、scope不明0、eligible 17件を確定した。G-46/J-77はqueueとbriefのタイトル不一致で除外。20件に埋めず17件を選定し、Hamilton quota B3/C1/D2/E1/F5/G1/H1/I2/J1、選定hash `8653449b753ff2689f30a71a5e5cb1d6b082d21e97ad2a2d021603cf6b8ad48a`。pool semantic hash `89de6a0ee9ba1cf794cf58e89131afff8dbc4e059abfa65aec4f51758560d0c8`。
- Batch014 proposal `ledgers/ponchi_simplification_batch_014_selection_proposal_20260928.csv` SHA `bcc6459c90008446450552bacad8976c80998d443f95c49a6cb09e5e90e0bc5c` は `/root/prompt_simplify_audit` により独立選定監査PASS。source queue snapshot SHA `2b923d73f36485dfe598c7c1d8ea215f02c13ae2e94cdb6254587f4d05d97b7e`、entries snapshotはB013 immutable snapshotを再利用しSHA `c881d2dc0cc13ef25e488ac6e05ce184d53e6cc5eb567a4aee1df9f0ec55045d`、brand matrix SHA `e37d9b0322a6e82675b4630a724747d54c194bd3d9eee7d5f6e812eb20f802ca`。17件すべて現画像とbriefの実SHA・寸法が確認され、人の判断pending、生成/採用not_authorized。
- 予約同期前queue snapshotは上記source queue snapshotを同じSHAの不変ファイルとして再利用。proposal直前snapshot `ledgers/ponchi_simplification_batch_014_proposal_before_selection_sync_20260928.csv` SHA `bcc6459c90008446450552bacad8976c80998d443f95c49a6cb09e5e90e0bc5c`。同期後queue SHA `92320f62ad0b93d5ab03a5ca689311a2b8ca750c757422af8cc56f05fc6fcddf`、proposal SHA `9c2229d885d3c42c8a9da4760dc9d69ae99fea08f134ebdf33a021451dc2e457`、cell diff `ledgers/ponchi_simplification_batch_014_selection_sync_diff_20260928.csv` 170件・SHA `f5d19fecd7aa1ce23f9e0b9e4327d750394e2f36b70043c3246332098f7319dd`。`/root/b11_plan_review`の独立同期監査PASSでは、queue選択17 IDの7列とproposal同17 IDの3列だけが変わり、非対象435行・許可外列は不変。人pending、generation/adoption未許可。
- Batch014 primary lane A `ledgers/ponchi_simplification_batch_014_triage_primary_lane_a_20260928.csv` は9×20、SHA `d766ff92880230b3f2d96514c80d5cad86d189512dde18be26e6c433e65c7a91`、simplify_candidate 8 / hold 1。lane B `...primary_lane_b...csv` は8×20、SHA `1886f4e6bac06a74c59fddc04b6906e48428389b8aba2bc1e0df75bd80ea5b70`、simplify_candidate 8。全17件の入力画像・briefはproposalと実ファイルpath/SHA一致、200×100表示を確認。
- Cross-review lane A SHA `30bd631e1434ee6f9c2fe65f2174241a855c754779f770db226487ab49090fef` は9行、agree 5 / correct 4。lane B SHA `ab3a011de160636f10a085c3a245c337fcc0e05e3232350bebdd3654726496d4` は8行、agree 1 / correct 7。合計agree 6 / correct 11、reclassify 0 / hold 0。D-30の現行xAI世代、E-22のGPQA比較条件などを修正し、F-153のbrief内ライセンス例不一致、F-10の子インスタンス数、複数ブランドmatrix/audit conflict等をHOLD根拠へ反映。すべて別担当cross-review済み。
- Final ledger `ledgers/ponchi_simplification_batch_014_triage_final_20260928.csv` は17×37、SHA `0ec5f579056707aa201d3d01ef590dbcafae5be10b9ae3b699b52ea7443d5758`、final disposition simplify_candidate 16 / hold 1、prompt readiness HOLD 17。人判断pending 17、generation/adoption not_authorized 17。prompt sidecar・生成候補は0件。current final画像は監査表示用だけで、既存の歴史的baseはB014の許可入力として扱っていない。
- 結果sync前queue snapshot `ledgers/ponchi_simplification_batch_014_full_queue_before_triage_sync_20260928.csv` SHA `92320f62ad0b93d5ab03a5ca689311a2b8ca750c757422af8cc56f05fc6fcddf`、proposal snapshot `ledgers/ponchi_simplification_batch_014_proposal_before_triage_sync_20260928.csv` SHA `9c2229d885d3c42c8a9da4760dc9d69ae99fea08f134ebdf33a021451dc2e457`。同期後queue SHA `cbd6357844e8d42f14efa1252fa1e5c15c31d725b52885b855413f95dda321a8`、proposal SHA `07e0fef1c85ec3b10984d382ec57f40d714800f3f4c2da9d9f93a24b1ca8021e`。diff `ledgers/ponchi_simplification_batch_014_triage_sync_diff_20260928.csv` は357×8、SHA `d01532194504101f78b521594bac3bad21942299f930a1e9630b9667eb751afe`。`/root/b11_plan_review`独立監査PASS: queue対象17 IDの5列85セルとproposal同17 IDの16列272セルのみ変更、非対象435行・許可外列は不変。dated selection noteのpending文言は履歴として保持し、現行status/next_actionはtriage完了を示す。human/generation/adoption gateとsidecar/candidate未作成も確認済み。
- v1.6共通テンプレreview PASSは項目別sidecar reviewや画像生成・採用を許可しない。Batch014は全件readiness HOLDのためprompt sidecarは作らない。次waveはresult-sync後のcurrent queueとcanonical entriesからeligible poolを再構築し、前waveと同じselection/primary/crossreview/readiness/result-syncゲートで開始する。

## 21. 2026-09-28 Batch015 eligible pool再構築・空poolで停止

- Batch014結果sync後のcurrent queue（452行、SHA `cbd6357844e8d42f14efa1252fa1e5c15c31d725b52885b855413f95dda321a8`）、canonical entries（452行、SHA `c881d2dc0cc13ef25e488ac6e05ce184d53e6cc5eb567a4aee1df9f0ec55045d`）、brand matrix（SHA `e37d9b0322a6e82675b4630a724747d54c194bd3d9eee7d5f6e812eb20f802ca`）を不変snapshotへ固定。各snapshotは作成時のcanonicalファイルとbyte-identical。
- Batch015 eligibility audit `ledgers/ponchi_simplification_batch_015_eligibility_audit_20260928.csv` は全452行、SHA `53ec0b9a8b3bf8c1ed9bb1a6a0d060fbd4fd6542b10cfddaebf79f2f15449762`。route/ready/untriaged/unselected/current-final gateの交差は26件。source-integrity PASSの24件は全て`reader_level=6`かつ刊行範囲外。G-46/J-77はbrief frontmatter titleがqueue/entries titleと異なるため除外。scope未判定0、eligible 0。
- Empty eligible pool `ledgers/ponchi_simplification_batch_015_eligible_pool_20260928.csv` はheaderのみ・データ0行、SHA `47ce66d413c9a7b41ce0eadeb6e2d77fbcbc93e6b86c852dfd061d4755cb2b12`。semantic pool/set hashは空集合SHA `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`、全章quota 0。closure summary `ledgers/ponchi_simplification_batch_015_selection_summary_20260928.csv` は1行、SHA `61d0b453449210b47e09ea3aa05d8686e8bd6a26bb8bbf2f6eb0bed5d6d4dc23`。
- `/root/b11_plan_review`の独立再計算PASSでは、452行joinでsource map error 0、26候補すべての画像/brief実SHAとfrontmatterを確認。24件は刊行外、G-46/J-77のみbrief-title mismatch、eligible/selected 0、proposalなし、top-upなし、queue syncなし。current queueはsnapshotと同じSHA。human decisionはpending、generation/adoptionはnot_authorized。
- Batch015は選定proposal、予約sync、primary/cross-reviewを作らずここで停止。次回選定は、新規または前回未対象の「source整合済み・刊行範囲内・未triage」項目が現行queueにある場合に、current queueからpoolを再構築して開始する。刊行scopeを広げる場合は別途明示判断を要する。G-46/J-77はcanonical entry/brief titleの整合確認後にscope判定へ戻すが、その時点でeligibleとはみなさない。Batch014 17件のHOLD要因（人の意味判断、承認済みlogo-free inputとcharacter参照、brand matrix/audit/use条件・clearspace/ROI等）の解消は別ゲートであり、Batch015へ補充しない。

