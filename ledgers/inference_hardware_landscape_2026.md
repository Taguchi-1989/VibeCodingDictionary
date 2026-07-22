# 推論ハードウェア勢力図とエッジ/クラウド3層構造（2026-06-23 調査）

*Lv6 シェルフ（J-83 vLLM ほか）執筆中、著者との対話で深掘りした裏取りメモ。誌面には直接出さないが、J 章の推論基盤系エントリの背景・将来予測の根拠として参照する。*
*注記: 2025年8月以降の動きが速い領域。書籍化前に一次情報で再確認すること。時期予測は確度が低いものを明記した。*

## 0. 出発点の問い

「最上級モデル（Kimi K2 級 1T、GLM-4.6 級 355B）を量子化せずローカルで動かすのは高い。これは変わりうるか？ 変わるならどういう道筋か？ 半導体的にそういう商品が出ればできるのか？ NVIDIA/Apple のマージンを迂回して民主化できるか？」

## 1. なぜ高いのか＝真のボトルネックは GPU ではなく HBM

- **HBM = High Bandwidth Memory**（DRAM を縦積みして GPU 直結、数 TB/s）。普通の DDR5（スロット挿し、数十 GB/s）と桁違い
- 真のボトルネックは HBM。「HBM が遅れれば次世代 GPU はただの紙のスペック」
- **SK Hynix が市場62%寡占**、その90%を NVIDIA が買い占め。**HBM は2026年分完売・2027年まで逼迫**
- HBM 営業利益率は2023年赤字→**2025年49%**。NVIDIA は HBM4 で従来の2倍（1枚$500）払う見込み
- → 高いのは NVIDIA のマージンというより**上流の HBM が構造的に足りず高いから**。民主化には(a)HBM 寡占を崩す か (b)HBM を使わないアーキに逃げる

## 2. メモリ必要量（巨大 MoE のローカル限界）

| モデル | 精度 | サイズ | 必要 RAM+VRAM |
| :-- | :-- | :-- | :-- |
| Kimi K2.6（1T総/32B active） | FP16 | 約2TB | 8×H100/H200 |
| 同上 | Q4 | 約630GB | 〜600GB |
| 同上 | Q2（最低） | 340GB | 最低350GB |
| GLM-4.6（約355B） | Q4 | 約180-200GB | M3 Ultra 256GB+ で可 |

**ローカルで動くか早見:**
- Kimi K2 級(1T): ❌ ほぼ無理。512GB Mac で Q2 ギリ、実用はクラウド(8×H100)
- GLM-4.6 級(355B): △ M3 Ultra 256GB+ で Q4 が現実的
- 70B 級: ⭕ Strix Halo 128GB / M4 Max で快適
- 32B 以下: ⭕ 64GB 級で十分

## 3. 統合メモリ競争（Apple 優位は崩れつつある）

| プレイヤー | 製品 | 統合メモリ | 帯域 | 位置づけ |
| :-- | :-- | :-- | :-- | :-- |
| Apple | M3 Ultra | 96-512GB | 819 GB/s | 帯域トップ |
| Apple | M4 Max | 〜128GB | 546 GB/s | |
| AMD | Strix Halo (Ryzen AI Max+ 395) | 128GB | 256 GB/s | x86初。CES2026で235B MoE実演。$25.77/GB |
| AMD | Gorgon Halo(次世代) | 最大192GB | 向上見込 | Zen5+RDNA3.5 |
| NVIDIA | DGX Spark/GB10 | 128GB | — | 直接対抗機 |

- Apple の残る強み＝帯域（token生成は帯域律速なので同容量なら Mac が速い）。容量・価格は AMD に並ばれ、帯域でまだ逃げている
- Intel は大容量統合メモリ勝負に踏み込まず NPU 路線

## 4. 推論専用チップ＝HBM を迂回する本命の道筋

全員の共通の敵は「HBM 経由のメモリ転送」。「重みをチップに住まわせる/焼く」で迂回する点で共通。**汎用↔専用のグラデーション**で並ぶ。

| 会社 | 賭けたもの | 捨てたもの | 狙い | 速度の証拠 |
| :-- | :-- | :-- | :-- | :-- |
| Taalas (HC1) | 重みを Mask ROM に焼込（完全ハード化） | 汎用性（1モデル専用） | 特定モデル超高throughput | Llama 8B 16,960 tok/s（B200の48倍）2026/2発表 |
| Etched (Sohu) | Transformer 構造を焼く | 非Transformer | Transformer 全部で速く | Llama 70B 8チップ50万tok/s（H100の20倍） |
| Groq (LPU) | SRAM 常駐＋決定的実行 | HBM・大容量 | リアルタイムAPI | Llama 70B 300 tok/s。NVIDIA が $20B 買収(2025/12) |
| Cerebras (WSE-3) | ウェハ丸ごと1枚 | 歩留まり・コスト | 超高速クラウド | 405B 1,000 tok/s。2026/5 上場 |

- 業界の賭け: NVIDIA が Groq を $20B 買収、OpenAI が Cerebras と $10B+ 提携、**カスタムASIC出荷2026に+44.6%成長**(GPUは+16.1%)、**推論コストは3年で50分の1**
- **罠**: SRAM/ROM は速いが容量が小さい→巨大MoEは載らない、中規模が得意。「巨大MoEを量子化なしでローカル民主化」は SRAM 容量か CXL のブレイクスルー待ち

## 5. PCIe / CXL / 将来の賭け先

- 現ボトルネック: マルチGPU を PCIe5 x16=128GB/s で繋ぐと詰まる（NVLink 900GB/s で7倍速）
- PCIe 7.0 が x16 256GB/s/方向 策定中だが HBM の数TB/s から見れば一桁遅い＝根本解決にならない
- 本命は **CXL（メモリプール化）＋ near-data processing（運ばずメモリ近傍で計算）**。Beluga(arXiv:2511.20172)／PNM for 1M-token(arXiv:2511.00321)／GTC2026 で Penguin が CXL KV キャッシュサーバ製品発表
- KV キャッシュ階層化: LMCache(arXiv:2510.09665)が GPU HBM→CPU DRAM→NVMe SSD 3階層、レイテンシ3-10倍削減。Tutti(arXiv:2605.03375)が SSD 退避を実用化

## 6. 「いつ来るか」の時期感（確度つき）

| 技術 | 時期感 | 確度 |
| :-- | :-- | :-- |
| CXL プール化 | 既に製品化開始（GTC2026）。普及はこれから数年 | 高め |
| SRAM 常駐チップ（Groq/Cerebras） | もう動いている（中規模なら現役） | 高い |
| SRAM 大容量化で巨大モデル丸載せ | 明確な時期予測なし（物理制約でブレイクスルー待ち） | 低い／未確定 |

- 「2027-2028 に CXL 本格普及」という投資筋の見方もあるが確度低。書籍化前に裏取り

## 7. エッジ/クラウド3層構造（著者仮説の検証 → ほぼ正解）

```
【オンデバイス層】NPU 80→TOPS / 7-13B / RAG で自分のデータ
   得意: プライバシー・低遅延・オフライン・常時起動 / 限界: 中規模まで
【ローカル高性能層】Strix Halo / M3 Ultra / DGX Spark（統合メモリ128-512GB）
   得意: 70B快適〜355B(GLM級)をQ4 / 限界: 帯域律速、1T級はQ2ギリ
【クラウド・フロンティア層】8×H100 / 推論専用ASIC(Groq等)
   得意: 1T級フル精度・超高throughput・最新最大 / 限界: API借り＝マージン乗せ、データ外出
```

- NPU 性能 45→80 TOPS（前年比+78%）、消費者チップで最速の伸び
- オンデバイスで動くモデルが 今1-3B→2026末に7-13B へ。7B がファンレス15Wで20-30 tok/s
- 棲み分けの明文: 「クラウドはフロンティアモデルを持ち続ける。NPU は on-device で十分・プライバシー/低遅延/オフラインが効くものを取る」
- さらに先: Microsoft が NPU と iGPU に推論を層分割（7Bの attention を NPU、FFN を iGPU、GPU単独より35%省エネ）。Build 2026 で「NPU だけ」をやめ NPU+GPU+クラウドのハイブリッド前提に方針転換

## 8. 結論（著者の問いへの答え）

- 「変わりうるか」= **YES。ただし鍵は GPU ではなくメモリの構造そのもの**
- 「大容量メモリ GPU を作る」方向は HBM 寡占のマージンに乗るだけ。本当の民主化は **HBM を使わないチップ**（SRAM常駐・ウェハスケール・ASIC焼込）＝ TSMC で作れる（Groq/Cerebras はファブレス）
- ただし当面うまくいくのは中規模モデル。「一人の手元で Kimi K2 級フル精度」は SRAM 大容量化か CXL 待ち
- 民主化は「巨大モデルをローカルで」ではなく「推論専用チップでクラウドのコストを50分の1に」という形で既に進行中
- 著者の仮説（Copilot PC 高性能版がコンシューマに降り、中規模はエッジ・重い計算はクラウドで棲み分け）は業界の動きと完全に整合

## 9. なぜ HBM は寡占か（特許ではなく製造難易度）

著者の問い「特許の独占か、技術的なものか」への切り分け。
- **特許主因ではない証拠**: Micron は HBM 特許を2018-2026に621件出願（SK Hynix 315件の約2倍）。なのにシェアは SK Hynix 50-62% / Micron 10-21%。特許の量より製造能力と先行投資が効く
- **本当の壁は4層**: ①TSV（数千本の極小via、ダイを30μm以下に削る、ホコリ1粒で数千ドルの不良）②歩留まりの学習曲線（積層・接合・反り）③資本（新工場$15B超・量産まで18-36ヶ月）④先行者累積優位（SK Hynix が TSV 早期投資＋NVIDIA と共同開発で GPU 認定先取り）
- 過去10年で新規参入ゼロ。中国 CXMT が2026末に国産HBM3狙うが先頭から3-4年遅れ＋EUV使えず歩留まり苦戦見込み

## 10. HBM を支える装置ベンダー（キー技術 × 過去5年株価）

各工程に別々の独占企業が張り付く「入れ子寡占」。株価は2026-06時点スナップショット（検索ベース、エントリ化時に一次情報で要再確認）。

| 企業 | 国 | 工程（キー技術） | 寡占度 | 過去5年(2021→2026) |
| :-- | :-- | :-- | :-- | :-- |
| ASML | 蘭 | EUV露光 | 100%独占 | 直近1年+112% |
| BESI | 蘭 | ハイブリッドボンディング(10nm精度) | 首位 | +332% |
| DISCO | 日 | ウェハ薄化(30μm)・切断 | 世界独占 | 直近1年+147% |
| Lam Research | 米 | エッチ・成膜(TSV穴/銅埋め) | 寡占 | +381% |
| KLA | 米 | 検査・計測 | 寡占 | +571%(最強) |
| Applied Materials | 米 | 成膜・CMP・薄化 | 寡占 | 数倍 |
| Tokyo Electron | 日 | 成膜・エッチ・洗浄 | 寡占 | 要確認 |
| Lasertec | 日 | EUVマスク検査 | 独占 | 要確認 |
| Zeiss | 独 | ASML向け光学(非上場) | 独占 | 非上場 |
| 〔参考〕SK Hynix | 韓 | HBM本体 | 62%首位 | 直近3年+1,068% |

- 構図: 「AIバブルの受益者はAI企業でなくツルハシを売る装置メーカー」。各社が別工程を独占し競合せず需要を分け合う

## 11. NVIDIA→TSMC ライン（CoWoS こそ真のボトルネック）

- GPUは2段階: ①前工程 TSMC 3nm/2nm + ASML EUV ②後工程 TSMC CoWoS（GPUとHBMを1枚に統合）
- **ボトルネックが HBM から CoWoS へ移動**。複数分析が「CoWoSこそAI供給の最大ボトルネック、HBMではない」
- NVIDIA が TSMC CoWoS能力の50-60%を単独予約（2026約60万ウェハ）。TSMC は月3.5万枚(2024末)→月13万枚(2026末)へ約4倍増産。足りずAmkor/ASEにも発注
- **TSMC 3D Fabric Alliance（タッグ相手）**:
  - 接合: ASMPT(星・TCB首位) / BESI(蘭)
  - 検査: KLA(米) / Camtek(イスラエル) / Onto(米)
  - ABF基板: Unimicron(台・稼働率90%逼迫) / Ibiden・Shinko・Toppan(日) / Samsung電機(韓) / Nanya(台)
  - HBM物理統合: SK Hynix/Micron/Samsung（HBM4をCoWoSで論理ダイに接合）

## 12. 材料層（装置の下の電子材料・ほぼ日本に集中）

| 材料 | 企業 | 国 | 独占度 |
| :-- | :-- | :-- | :-- |
| ABF(基板絶縁フィルム) | 味の素 | 日 | 95%(PC向け実質100%)。2026Q3に30%値上げ、AI需要で品薄。市場2026 115億ドル→2032 496億ドル |
| Pimel(感光性ポリイミドPSPI・RDL絶縁) | 旭化成 | 日 | HBM/CoWoSのRDL絶縁に必須。2024 TSMC優秀賞。出荷絞り噂でTSMC/ASE懸念=代替不可 |
| EUVフォトレジスト | JSR/東京応化(TOK)/信越化学 | 日 | 3社でEUVの90%超、高純度は95%。sub-7nmは日本が事実上唯一。JSRは2024/6上場廃止 |
| シリコンウェハ | 信越化学/SUMCO | 日 | 2社で世界過半 |
| CCL(銅張積層板) | Resonac/三菱ガス化学 | 日 | |

- 地政学: 2025/11 経産省がEUVレジスト含む12材料を輸出規制リスト→中国42社へ供給制限、TOK/信越が対中出荷停止
- 本質: 「装置は多国籍だが、材料は日本がボトルネックを握る」。日本はGPUもHBMも作らないが材料の最上流で詰まりどころを押さえる

## 13. 原料ツリー（石化系=日本の知 / 元素系=中国の精錬）

著者の問い「材料の原料を掘るとツリーになるか」への答え=なる。枝の先で日本と中国に分岐する。

```
系統A 石油化学(樹脂・溶剤)由来 → 日本・先進国(合成ノウハウ)
  味の素ABF = エポキシ樹脂(石化/ナフサ) + 硬化剤(味の素アミノ酸化学) + シリカフィラー(鉱物)
    → 味の素は「資本の軽い独占」(レシピが障壁、原料は石化品を購入)。基板メーカーは「資本の重い寡占」(巨額工場投資)
  EUVレジスト = ベース樹脂+感光材PAG(企業秘密) + 溶剤PGMEA(石化)
    → 障壁は「配合と純度」。日本の強みは元素でなく超高純度の合成・配合ノウハウ

系統B 鉱物・元素由来 → 中国が精錬を握る
  ガリウム(GPU化合物) → ボーキサイト/亜鉛の副産物。中国が精錬99%
  ゲルマニウム → 石炭灰/亜鉛の副産物。中国88%
  ネオン等希ガス(EUV/エッチ用) → ウクライナ・中国
  レアアース(研磨・磁石) → 中国圧倒的
  シリコン → 珪石。ウェハ精製は信越/SUMCO(日)、金属シリコン生産は中国優位
    → 中国も輸出規制の武器化(2023ガリウム規制、2026/11まで一時停止中)
```

- **層を下がるほど寡占が固い**: チップ(数社)→装置(各工程1-数社)→材料(日本集中)→原料元素(中国集中)。最下層が最も動かしにくい
- **地政学の構図**: 配合・合成の知(樹脂/レジスト)=日本 vs 元素の精錬(ガリウム等)=中国。日米と中国がサプライチェーンの違う層を人質に取り合う

## 14. 統合（チップ→装置→材料→原料の4層入れ子）

```
【チップ】 GPU:NVIDIA(米) HBM:SK Hynix(韓) 製造:TSMC(台)
   ↑
【装置】  露光ASML(蘭) 薄化DISCO(日) 接合ASMPT(星)/BESI(蘭) 検査KLA(米) 光学Zeiss(独)
   ↑
【材料】  ABF味の素(日95%) RDL旭化成(日) EUVレジストJSR/TOK/信越(日95%) ウェハ信越/SUMCO(日)
   ↑
【原料】  石化系(樹脂・溶剤)→日本の知 / 元素系(Ga/Ge/希ガス/レアアース)→中国の精錬
```

直列ボトルネック: EUV(ASML) → HBM(SK Hynix+DISCO薄化) → CoWoS(TSMC+ASMPT接合+味の素ABF+旭化成Pimel)。どれか1つ詰まればGPUが出ない。だからNVIDIAは全層を先に押さえる。

## 15. 微細化の物理（リーク電流）とトランジスタ構造の進化

著者の問い「7nm世代でリーク電流が問題化したのに、なぜ3nm/2nmで問題なくなった？」への答え=問題は消えていない。ゲートの静電制御を保つためトランジスタの構造を世代ごとに作り変えて封じてきた。

- **リークの正体**: 短チャネル効果。微細化でソース/ドレインが近づき、ゲートをOFFにしても電流が漏れる
- **構造進化（ゲートがチャネルを囲む面を増やす）**:
  - プレーナ型(〜28nm): ゲートが上1面のみ制御→限界
  - FinFET(22nm〜3nm, 2011〜): チャネルをヒレ状に立て3面を囲む→リーク激減。「7nmでも動いた」理由
  - GAA/ナノシート(2nm〜, 2025〜): チャネルを板状にしゲートが全周4面を包む(Gate-All-Around)→さらに抑制。TSMC N2/Intel 18A RibbonFET/Samsung SF2
- **もう一段前の危機**: 45nm(2007)でゲート酸化膜が薄すぎてトンネルリーク→High-k(高誘電率)メタルゲートで物理的に厚いまま電気的に薄く振る舞わせ解決
- 注意: 今の"2nm"は物理ゲート長でなくほぼマーケティングのラベル。実際のフィン間隔/ゲート長はもっと大きい
- 次の敵: CFET(N/Pトランジスタを縦積み)。方法論どおり「短チャネル効果という敵を囲み面積で世代ごとに潰し、次の敵が顔を出す」

## 16. Intel 微細化の盛衰（EUV採用遅れ＝自滅 → 18Aで復活途上）

著者の問い「Intelが微細化で苦戦したのは外圧か、解決したか」への答え=外圧でなく自滅。2026に18Aで一応復活、ただし黒字化はこれから。

- **つまずき(2015〜2022頃)**: ①14nm→10nmで密度2.7倍を狙い欲張りすぎ(通常1.5-2倍) ②EUVを渋りDUVのマルチパターニングで粘る(1つの線に6回露光=hexa patterning)→欠陥増・歩留まり激減・コスト爆発 ③7nmも「欠陥モード」で2年遅延。この間にTSMCがEUV先行採用で独走、Apple/NVIDIAを獲得
- 構図: 「日本/TSMCに抑えられた」のでなく、Intel自身がEUV採用を渋って自爆、隙にTSMCが独走
- **復活(2026-06時点)**: 18A(1.8nm級)が2025/10量産開始(TSMC N2より先)。Panther Lake(Core Ultra Series 3)が2026/1出荷=完全自社18A製。歩留まり月7-8%改善。18A-Pが2026/6リスク生産入り。外部顧客Microsoft/AWS確定、NVIDIAはI/Oダイを18A/14Aで検討
- **残る課題**: 歩留まりが黒字ライン未達(早くて2026末)。NVIDIAは18Aテストし「先に進むのやめた」報道も。Intel Foundryは赤字。地力ではまだTSMC圧倒的(顧客基盤/歩留まり/CoWoS)。「追いついたように見える」段階
- 出典: Tom's Hardware(Intel 7nm broken / 18A production before N2), Motley Fool(Intel Stealing Foundry Spotlight), TechTimes(18A-P risk production) — checked 2026-06-23
- 関連既存エントリ: C-9 NVIDIA / C-12 TSMC / C-14 AMD（company）。Intel は未エントリ

## 17. 微細化から3D積層へ（CPU/GPUアーキの進化・More than Moore）

著者の問い「CPU/GPUの進歩は微細化以外に何があるか。積層・3次元方向か？」への答え=その通り。進歩は2本柱（①微細化=横に小さく・限界接近 / ②積層・統合=縦＋分割・いま主戦場）。

- **チップレット**: 大きな1枚（モノリシック）をやめ機能ごとに小チップに分割し最適プロセスで作って後で繋ぐ。小ダイは歩留まり高＋旧プロセスの枝は安い。AMDが先行（RDNA 3でGPU消費者向け初のチップレット化、TSMC InFO-RDLで接続）
- **3D積層**: チップを縦に重ねる。AMD 3D V-Cache（CPU上にSRAMダイを直接積む、TSV＋ハイブリッドボンディング、帯域従来比10倍、2026/4 Ryzen 9 9950X3D2は両CCDに積層）。HBMのメモリ縦積みも同類
- **CFET（次世代）**: トランジスタ自体を縦積み（NMOSの上にPMOS）。GAAの次、TSMC研究中
- **裏面給電（BSPDN）**: 電源を裏面に回し表を信号専用に。混雑解消＋抵抗減。Intel PowerVia（18Aの目玉）、TSMCも
- **材料・加工**: ハイブリッドボンディング（はんだ無し銅直接接合、20μm以下ピッチ、3D積層の要）、ガラスコア基板（樹脂より平坦・大型化に強い、AMD/Intel/Samsung）、マイクロ流路冷却（チップに水路を彫り直接冷却）
- **パラダイム転換**: Moore's Law（2次元微細化）→ More than Moore / CMOS 2.0（3次元の積層・分割・統合へ主戦場が移る）。方法論どおり「2次元微細化という手段が限界＝敵→3次元という新手段で突破」
- 出典: IEEE Spectrum(3D Chip Stacking), CMOS 2.0(arXiv:2510.04535), Tom's Hardware(AMD 2nd-gen 3D V-Cache), PatSnap(Advanced packaging 2026) — checked 2026-06-23
- エントリ化: J-102「チップレットと3D積層」(Lv6) として展開（2026-06-23）

## エントリ化メモ（2026-06-23 著者と合意）

この4層構造は Lv6 独立エントリ群に育てる。候補（J章の空き番号は要確認）:
- 半導体サプライチェーン全体（4層入れ子の俯瞰・直列ボトルネック）
- 半導体製造装置ベンダー（ASML/DISCO/BESI/KLA…キー技術×株価）
- 電子材料（味の素ABF/旭化成Pimel/EUVレジスト＝日本の材料支配）
- 重要鉱物の地政学（ガリウム等＝中国の精錬支配、輸出規制の応酬）
- CoWoS / 先端パッケージ（GPUとHBMをどう1枚に統合するか）

## 出典

- The AI Inference Wars (Taalas/Cerebras/Groq/Etched/NVIDIA) https://themenonlab.blog/blog/ai-inference-accelerators-compared
- Hybrid Bonding: SK Hynix/Applied Materials/BESI (Counterpoint) https://counterpointresearch.com/en/insights/Hybrid-Bonding-Expands-from-Logic-to-Memory-SK-Hynix-Applied-Materials-BESI-Drive-Co-optimization-to-Scale-Next-gen-HBM
- DISCO Corporation World Leader (SemiAnalysis) https://semianalysis.com/2022/07/19/disco-corporation-the-world-leader/
- ASML EUV Dominance (TrendForce) https://www.trendforce.com/insights/asml-euv
- Why is HBM so Hard to Manufacture (Vik's Newsletter) https://www.viksnewsletter.com/p/why-is-hbm-so-hard-to-manufacture
- China's CXMT Targets 2026 HBM3 (FinancialContent) https://www.financialcontent.com/article/tokenring-2026-1-23-chinas-cxmt-targets-2026-hbm3-production-with-42-billion-ipo
- Advanced Packaging: Nvidia Secures 60% of CoWoS (Astute Group) https://www.astutegroup.com/news/industrial/advanced-packaging-demand-soars-nvidia-secures-60-of-cowos-capacity/
- CoWoS Not HBM Is the Real Bottleneck (Medium) https://medium.com/@Elongated_musk/cowos-not-hbm-is-the-real-ai-supply-bottleneck-d0ae8f3f7ce4
- TSMC 3D Fabric Alliance Substrate (Asia Business Daily) https://www.asiae.co.kr/en/article/2026043014033228020
- Ajinomoto 95% ABF, 30% price hike (BigGo Finance) https://finance.biggo.com/news/ZU2KJZ4BpwxG186NIOsE
- Asahi Kasei Pimel PSPI for Advanced Packaging (Asahi Kasei) https://www.asahi-kasei.com/news/2026/e260521
- Japanese Lock on Photolithography (Private Markets News) https://privatemarketsnews.substack.com/p/the-japanese-lock-on-photolithography
- ABF The Material Beneath the Model (Nikhs) https://nikhs.substack.com/p/abf-the-material-beneath-the-model
- Beyond Rare Earths: China's Gallium (CSIS) https://www.csis.org/analysis/beyond-rare-earths-chinas-growing-threat-gallium-supply-chains
- 装置/材料/原料の株価・シェアは2026-06時点スナップショット。エントリ化前に一次情報で再確認
- 上記すべて checked 2026-06-23

## （旧）出典

- The AI Inference Wars (Taalas/Cerebras/Groq/Etched/NVIDIA) https://themenonlab.blog/blog/ai-inference-accelerators-compared
- Taalas Etches AI Models Onto Transistors (NextPlatform) https://www.nextplatform.com/2026/02/19/taalas-etches-ai-models-onto-transistors-to-rocket-boost-inference/
- The Inference Economy Arrives (TrendForce) https://insights.trendforce.com/p/ai-inference-chip-architecture
- The AI Memory Supercycle (Introl) https://introl.com/blog/ai-memory-supercycle-hbm-2026
- SK Hynix: The Memory Bottleneck (Longyield) https://longyield.substack.com/p/sk-hynix-the-memory-bottleneck-powering
- NPU Guide 2026 (SolidAITech) https://www.solidaitech.com/2026/05/npu-neural-processing-unit-complete-guide.html
- Build 2026: Microsoft Drops NPU-Only Focus (Windows News) https://windowsnews.ai/article/build-2026-microsoft-drops-copilot-npu-only-focus-for-gpu-and-on-device-ai.423596
- LMCache (arXiv:2510.09665) https://arxiv.org/abs/2510.09665
- Beluga CXL KVCache (arXiv:2511.20172) https://arxiv.org/pdf/2511.20172
- PNM for 1M-token (arXiv:2511.00321) https://arxiv.org/pdf/2511.00321
- Kimi K2.6 How to Run Locally (Unsloth) https://unsloth.ai/docs/models/kimi-k2.6
- 全て checked 2026-06-23
