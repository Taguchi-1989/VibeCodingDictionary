# Ponchi sequential generation experiments — 2026-09-05

目的: 未生成エントリを一件ずつ確認し、誌面ポンチ絵メモと共通生成ルールが一致する候補だけを次工程へ送る。ここは実験候補置き場であり、assets/ponchi/final/ と生成台帳は変更しない。

## 固定したルール

- docs/ponchi_prompt_pipeline.md を生成順序と scene brief の基準にする。
- docs/ponchi_composition_variety_policy.md に従い、意味に合わせて構図ファミリーを分ける。
- docs/ponchi_character_bible.md の Character A/B/C を参照し、人物は主題を補助する。
- 本体は白・黒・グレー・指定青だけ。読める文字、ロゴ、公式マーク、実在 UI、ブランド色は生成しない。
- 候補は 1254x627（2:1）へ正規化し、色監査・密度監査・200px縮小確認を行う。
- 公式ロゴが必要な項目は、公式素材の後合成が終わるまで assets/ponchi/final/ に昇格しない。

## 候補一覧

| entry | 主構図 | 候補ファイル | 機械監査 | 目視メモ |
| --- | --- | --- | --- | --- |
| F-18 | 左右比較・逆向きの制御矢印 | F-18_library-framework_v2_1254x627.png | size pass / bbox 0.730 / color pass | 200pxでもライブラリとフレームワークの矢印方向が読める。v1は左の向きが弱く不採用 |
| F-43 | 3層テストピラミッド＋検証ループ | F-43_test_pyramid_v1_1254x627.png | size pass / bbox 0.767 / color pass | 200pxでも3層と安全網ループが読める |
| F-45 | 手元 → 成果物 → サーバー → 公開画面 | F-45_deploy_v1_1254x627.png | size pass / bbox 0.609 / color pass | 透明生成物を白背景へ決定的に合成。ロールバックは点線で補助 |
| F-46 | 虫眼鏡・切り分け・仮説・修正・再確認のループ | F-46_debug_v1_1254x627.png | size pass / bbox 0.663 / color pass | 赤を使わず、エラーは紺の記号で表現 |
| F-47 | 画面側 ↔ 中央ゲートウェイ ↔ サーバー側 | F-47_frontend-backend_v1_1254x627.png | size pass / bbox 0.645 / color pass | 双方向の API 境界が200pxでも判別できる |
| F-213 | 受付カウンターによるリクエスト／レスポンス往復 | F-213_api_v1_1254x627.png | size pass / bbox 0.570 / color pass | 窓口の比喩と往復矢印が成立 |
| F-214 | 秘密鍵・安全保管・漏えい・ローテーション | F-214_api-key_v1_1254x627_palette.png | size pass / bbox 0.649 / color pass | 元候補は色 review。パレット正規化版を候補扱い |
| G-24 | 入力 → 低／高設定 → 出力のばらつき比較 | G-24_temperature_v2_1254x627.png | size pass / bbox 0.765 / color pass | v1の装飾きらめきを不採用。v2は安定／多様の差が読める |
| G-25 | 消える会話と残るメモリの対比 | G-25_memory_v1_1254x627.png | size pass / bbox 0.621 / color pass | 点線の一時情報、棚の保存情報、確認・削除を分離 |
| G-26 | スクリーンショット → 観察 → 操作 → 承認ループ | G-26_computer-use_v1_1254x627.png | size pass / bbox 0.741 / color pass | AI操作と人の監督を別役割で表現 |
| G-27 | 直接入力／外部資料 → AI → 権限ゲート | G-27_prompt-injection_v1_1254x627.png | size pass / bbox 0.756 / color pass | 攻撃文面は描かず、混入経路と防御だけを表現 |
| G-49 | 目標 → 観察 → 判断 → ツール実行 → 承認 | G-49_ai-agent_v1_1254x627.png | size pass / bbox 0.814 / color pass | 自律ループを主役にし、承認ゲートを残した |

## 保留

- B-34 NotebookLM: 公式情報で 2026-07-16 に Gemini Notebook への改称が確認でき、現行本文のタイトル・ロゴ対象とずれている。本文・ブランド方針が確定するまで生成しない。

## 次工程

候補はまだ assets/ponchi/final/ へ昇格しない。人手で意味・シリーズ内の重複・文字要素を確認し、採用候補を決めた後に、必要な文字・公式素材・誌面プレビューを別工程で統合する。生成台帳の同期は別タスクとする。
