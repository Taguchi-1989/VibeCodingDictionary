---
id: J-93
title: Ubuntu
title_reading: ウブントゥ
category: term_general
subtype: ui_os
experience_level: hands_on
reader_level: 2-3
importance: D
figure_type: structure
page_layout: spread_v1
start_date: 2004-10-20
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - Linux
  - WSL
  - bash
  - GPL
status: ready
---

<!-- バイブコーディング図鑑 エントリー v2（spread_v1） -->

## tagline

Canonical 社が開発する Debian（デビアン）系 Linux（リナックス）ディストリビューションです。


<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

無償で使える Linux OS の一つです。Canonical 社が 2 年ごとに LTS（長期サポート）版を出し、安定運用なら LTS、新機能優先なら通常版と選べます。

## どこで出会うか

WSL（Windows Subsystem for Linux）を入れたときの初期ディストリビューションとして登場します。AWS・GCP・Azure 仮想マシンの既定 OS にもよく選ばれます。

## メイン図

### 図の狙い

Ubuntu が「手元 PC・クラウド・WSL」という 3 つの場面でどう顔を出すかを示します。

### B. 登場シーン（figure_type: structure）

- シーン1: 開発者の手元 PC に直接インストールして Linux 環境として利用する
- シーン2: WSL 経由で Windows 上に Linux 環境を立ち上げる際の初期ディストリビューションとして登場する
- シーン3: AWS / GCP / Azure でクラウド仮想マシンを作成する際のデフォルト OS として選ばれる
- 並べる基準: 読者が Ubuntu の名を見かける場所（エディタ・ターミナル・クラウドコンソール）を入口に並列


## 会話での使い方例

「WSL の Ubuntu に Claude Code を入れれば bash 手順がそのまま動きます。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

Debian 系 Linux をエンドユーザーにも使いやすい形で提供する OS です。

### 2. うれしさ

クラウド・WSL・手元 PC で同じ操作体験が得られます。

### 3. 注意点

LTS 版と通常版で EOL（サポート終了）時期が大きく異なります。

### 4. どこで役立つか

AI ツールのサーバサイドや WSL 開発環境の基盤として使われます。

### 5. はじめに

LTS 版と通常版の違いとバージョン番号（YY.MM）の読み方が入口です。

### 6. 深掘り先

Linux、WSL、bash

## 開発フローでの位置（必須）

1. 環境選定 — Windows なら WSL、クラウドなら仮想マシン OS として選ぶ
2. インストール — LTS 版か通常版かをバージョン番号（例: 24.04 LTS）で確認
3. 初期設定 — apt でパッケージを更新し開発ツールを揃える
4. ツール導入 — Claude Code などを Linux 向け手順で入れる
5. 動作確認 — bash でチュートリアルを流し動作を確かめる


## 関連用語

- Linux
- WSL
- bash
- GPL
- Debian


<!-- ━━━━━━━━ 著者記入欄（右ページ下段に印刷される／AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- まず何と読むのかわからないし、聞いたこともない、というところから始まる。
- Linux の中の一部が Ubuntu、というその位置づけが分かりづらい。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 読めない。
- 👍 良い点: Windows なしでもパソコンの OS として機能できるところ。
- 👎 ダメな点: 使っていくにはやっぱり多少の知識が必要。
- 👥 誰向けか: サーバー・AI エージェント・ロボット OS を使う人向けです。
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: structure）

- 描く内容: 中央に Ubuntu ロゴ／名前を置き、三方向の矢印で「手元 PC」「WSL（Windows）」「クラウド仮想マシン」の 3 シーンを配置する
- 登場人物（いれば）: 開発者 1 名がノート PC と向き合う姿（右下隅）
- 吹き出し・心の声: 「どこでも同じ apt コマンドで揃う」
- 中央に置くキーワード/ラベル: Ubuntu
- Before / After の場合の対比ポイント: なし（登場シーン型）

### 6視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 選択肢カード（Windows / Cloud / PC）
- Step 2 のアイコン/絵柄: ダウンロード矢印＋バージョン番号ラベル
- Step 3 のアイコン/絵柄: ターミナル画面＋ apt コマンド
- Step 4 のアイコン/絵柄: AI ツールのアイコン群
- 矢印で示す流れの意図: 環境選定から動作確認まで一直線に進む様子

## コミュニティ補完メモ

- J-92 Linux との住み分け：Linux はカーネル／OS ファミリー全体の概念エントリ。Ubuntu は Linux の具体ディストリビューションとして、実際に使う場面での顔を担う。重複説明は避け、Ubuntu 側では「なぜ Ubuntu が選ばれるか」「LTS 版と通常版の選び方」に絞る。
- F-82 WSL との住み分け：WSL は Windows 上で Linux を動かす仕組みのエントリ。Ubuntu 側では「WSL の初期ディストリビューションとして登場する」という一言にとどめ、仕組みの説明は WSL エントリに譲る。
- バリエーション（Kubuntu / Xubuntu / Pop!_OS）は本文に入れると字数が膨れるため、備考に記載。

## 出典メモ

- Ubuntu 公式サイト <https://ubuntu.com/about> — checked 2026-04-30
- Canonical 社公式リリースノート <https://wiki.ubuntu.com/Releases> — checked 2026-04-30

## 備考

- Ubuntu のバージョン番号は「YY.MM」形式（例: 24.04 = 2024 年 4 月リリース）。末尾が「.04」の年の LTS が安定版の目印。
- バリエーション：Kubuntu（KDE デスクトップ）/ Xubuntu（軽量 XFCE）/ Pop!_OS（Ubuntu 派生、ゲーム・GPU 寄り）など派生ディストリビューションが存在する。これらは本文のスコープ外として備考に記録。
- Canonical 社（カノニカル）はイギリス企業。創業者 Mark Shuttleworth（マーク・シャトルワース）は南アフリカ出身の実業家で、「人類のための OS」を掲げて Ubuntu を公開した（2004 年 10 月）。
