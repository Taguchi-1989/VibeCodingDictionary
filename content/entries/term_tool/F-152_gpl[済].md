---
id: F-152
title: GPL
title_reading: ジーピーエル
category: term_tool
subtype: license
experience_level: research_only
reader_level: 3-4
importance: E
figure_type: structure
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - Apache 2.0
  - MIT ライセンス
  - Creative Commons
  - OSS
status: ready
---

# GPL

## tagline

GNU General Public License の略。派生物にも同じライセンスを強制するコピーレフト型の規格です。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

利用・改変・再配布を自由に認める一方、派生物のソースも同じ GPL で公開する義務を課します。Linux カーネルなどが採用し、OSS の自由を保つ仕組みです。

## どこで出会うか

OSS ライブラリの LICENSE ファイルで「GPL v2」「GPL v3」を見かけます。法務チェックで「GPL を取り込むと製品全体に公開義務が生じる」と警告が出る場面が典型です。

## メイン図

### 図の狙い

GPL の「コピーレフト伝染」のしくみを、コードを取り込む前後の対比で示す。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: 社内製品に GPL ライブラリを取り込もうとしている
  - 視覚要素（コード or 概念）: 「MIT ライセンス ✓」「Apache 2.0 ✓」「GPL v3 ⚠」の 3 択リスト
  - つまずき: ライセンスの違いを意識せずに使ってしまう
- After
  - 状況: GPL ライブラリを取り込んだ場合、製品全体への GPL 適用が必要になる
  - 視覚要素: GPL が外側に広がる「伝染」のイメージ図
  - うれしさ: Apache 2.0 の代替を選ぶことで義務を回避できる

## 会話での使い方例

「GPL は取り込めないので、Apache 2.0 の代替を Claude に探してもらいました。」

<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

派生物にも GPL を強制するコピーレフト型ライセンスです。

### 2. うれしさ

OSS の自由を守り、改変コードが非公開になるのを防げます。

### 3. 注意点

GPL コードを組み込むと自社製品全体に公開義務が生じる場合があります。

### 4. どこで役立つか

ライブラリ選定時のライセンス審査で判断基準になります。

### 5. はじめに

「コピーレフト＝派生物にも同じ条件を継承する仕組み」と覚えると理解が早いです。

### 6. 深掘り先

Apache 2.0、MIT ライセンス、AGPLv3

## 開発フローでの位置（必須）

1. ライブラリ調査 — 使いたい OSS のライセンスが GPL か確認します
2. 法務確認 — GPL の場合は製品への影響範囲を社内で確認します
3. 代替選定 — Apache 2.0 や MIT の代替ライブラリを Claude などで探します
4. 採用判断 — ライセンスが許容範囲のライブラリを最終選定します

## 関連用語

- Apache 2.0
- MIT ライセンス
- Creative Commons
- OSS

<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- 派生物にも公開義務が伝染し、知らずに使うと製品全体が縛られます。
- 無料で使えると思って取り込むと、後から制約の強さに気づきます。
- 公開する側ではない人にとって、リスク感度を共有するのが難しいです。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: ただで使えるからいいじゃん、と思って近寄って痛い目を見そうになりました。
- 👍 良い点: OSS の自由を守るという思想が明確で、オープン推進の場面では筋が通ります。
- 👎 ダメな点: クローズで持ちたい秘匿部分まで出てしまい、企業内展開では危険を感じます。
- 👥 誰向けか: オープンで広めたいプロジェクト向けで、使い方の設計は慎重さが要ります。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: GPL コードを取り込むと外側の自社製品全体に GPL が広がる「伝染」のイメージ図。取り込み前は「MIT」「Apache 2.0」「GPL」の 3 択ボックスが並ぶ
- 登場人物: 開発担当者（非エンジニア）がライセンス一覧を見ているシーン
- 吹き出し・心の声: 「GPL を入れると全部公開しないといけないの！？」
- 中央に置くキーワード/ラベル: GPL（伝染）→ 自社製品
- Before / After の場合の対比ポイント: Before = MIT/Apache のみ（安全）、After = GPL を取り込んで全体に波及

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 虫眼鏡（ライセンス調査）
- Step 2 のアイコン/絵柄: 書類・印鑑（法務確認）
- Step 3 のアイコン/絵柄: AI チャット画面（代替検索）
- Step 4 のアイコン/絵柄: チェックボックス（最終採用）
- 矢印で示す流れの意図: 調査 → 判断 → 代替 → 採用の順で進む

## コミュニティ補完メモ

- F-151 Apache 2.0 との住み分け：Apache 2.0 は特許条項付きの「ゆるいライセンス」でコピーレフト義務がない。GPL との対比で選定基準を示す
- F-150 MIT ライセンス との住み分け：MIT はさらにシンプルで制限が少ない。GPL／Apache 2.0／MIT の三択比較は F-150〜F-152 でまとめて参照可能
- F-154 OSS との住み分け：OSS はライセンス全般の上位概念。GPL は OSS の一種だが、OSS エントリはライセンスの種類論ではなくオープンソースの定義・文化を扱う
- AGPLv3（GPLv3 の派生）はネットワーク経由配信にも適用。MongoDB 旧バージョン / Grafana などが採用。本エントリの備考に記載

## 出典メモ

- GNU GPL ライセンス公式 <https://www.gnu.org/licenses/gpl-3.0.html> — checked 2026-04-30
- FSF フリーソフトウェア定義 <https://www.gnu.org/philosophy/free-sw.html> — checked 2026-04-30

## 備考

- GPLv1（1989）/ GPLv2（1991、Linux カーネル採用）/ GPLv3（2007、特許条項追加）/ AGPLv3（2007、ネットワーク配信にも適用）
- 「フリー」は「無料（free of charge）」ではなく「自由（free as in freedom）」を意味する。"Free as in free speech, not free beer" という説明が定番
- AGPLv3 は SaaS など「実行するだけで配布しない」場合でもソース公開義務が生じる。MongoDB（旧）/ Grafana / Elasticsearch（一部）が採用
- GPL の「伝染」は厳密には「GPL コードとリンクして統合された場合」に適用される。ライブラリとして動的リンクする場合の解釈には議論がある（専門家確認推奨）
