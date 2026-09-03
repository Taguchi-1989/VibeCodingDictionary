---
id: F-87
title: sudo
title_reading: スードゥー
category: term_tool
subtype: shell
experience_level: hands_on
reader_level: 2-3
importance: D
figure_type: before_after
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - bash
  - WSL
  - Linux
  - git
status: ready
---

# sudo

## tagline

Substitute User do の略。root（管理者）権限を一時的に借りて 1 コマンドだけ実行するシェルコマンドです。

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## 何をしてくれるか

`sudo <コマンド>` と打つと、root（ルート）と呼ばれる最高権限ユーザーとして実行できます。実行前にパスワードを求めて確認するため、誤操作を防ぐ安全弁にもなっています。

## どこで出会うか

パッケージ導入（`sudo apt install ...`）やシステム設定変更など、通常権限では弾かれる操作で登場します。Claude Code が裏でシェルコマンドを走らせる際にも sudo を求める場面があります。

## メイン図

### 図の狙い

sudo を使う前と後で、コマンドの「通り道」がどう変わるかを示す。

### A. Before / After（figure_type: before_after）

- Before
  - 状況: 一般ユーザーが root 専用コマンドを実行しようとする
  - 視覚要素（コード or 概念）: `apt install nginx` → Permission denied
  - つまずき: 権限がなくてエラーになる
- After
  - 状況: sudo を付けて再実行する
  - 視覚要素: `sudo apt install nginx` → パスワード入力 → 実行完了
  - うれしさ: root の権限を借りて操作が通る


## 会話での使い方例

「sudo を要求するコマンドは Claude に確認させてから手動で実行する運用にしました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

一般ユーザーが root 権限を一時的に借りるコマンドです。

### 2. うれしさ

常時 root 運用より安全に管理者操作を行えます。

### 3. 注意点

AI に sudo 権限を渡す際は操作内容の確認が必要です。

### 4. どこで役立つか

パッケージ導入やシステム設定など管理者操作全般に使います。

### 5. はじめに

root（全権限ユーザー）の権限を一時借用するコマンドです。

### 6. 深掘り先

bash、Linux、WSL


## 開発フローでの位置（必須）

1. 環境構築 — WSL や Linux サーバーのセットアップ時に登場します
2. パッケージ導入 — `sudo apt install` でライブラリやツールを追加します
3. 設定変更 — `/etc/` 配下の設定ファイルを書き換える際に sudo が要ります
4. AI との協働 — Claude Code が sudo 付きコマンドを提案したら、人間が内容を確認してから実行します


## 関連用語

- bash（シェル）
- WSL
- Linux
- git


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- Linux 系で玄人が使うのを見たことはありますが、何の略か分かりません。
- ターミナルでパッケージを入れる時に求められて、「なんじゃこりゃ」となります。
- パスワードを打っても画面に表示されないなど、癖のある挙動に戸惑います。
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: Claude が裏で実行したり、管理者権限が要る場面で初めて目にしました。
- 👍 良い点: スーパーユーザー権限を一時的に借りられ、設定変更で頼りになります。
- 👎 ダメな点: 権限が強い分、誤操作の影響が大きく失敗から学ぶことが多いです。
- 👥 誰向けか: Linux や WSL で初期設定や環境構築をする人に必要になります。
<!-- user-input:end key="my_comment" -->

<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: before_after）

- 描く内容: 一般ユーザーがコマンドを叩こうとして弾かれる場面（Before）と、sudo を付けて鍵が開く場面（After）の対比
- 登場人物: 一般ユーザー（困り顔の人物）と「root の扉」を守る門番のアイコン
- 吹き出し・心の声: Before「Permission denied...」／After「パスワード確認、OK！」
- 中央に置くキーワード/ラベル: sudo
- Before / After の対比ポイント: 権限の壁を sudo が一時的に突破するイメージ

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用（個別演出が要るときだけ書き足す）

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: サーバー・PC のセットアップアイコン
- Step 2 のアイコン/絵柄: パッケージ箱のアイコン
- Step 3 のアイコン/絵柄: 設定ファイル・歯車アイコン
- Step 4 のアイコン/絵柄: AI と人間が並ぶ確認シーンのアイコン
- 矢印で示す流れの意図: 環境を作って → 必要なものを入れて → 設定して → AI と安全に使う流れ

## コミュニティ補完メモ

- bash（F-81）との住み分け：bash はシェル全体の話、sudo は権限昇格という 1 つの機能に絞った用語。bash エントリで「権限が必要なときは sudo」と触れ、詳細はここへ誘導する
- WSL（F-82）との住み分け：WSL は Windows 上で Linux 環境を動かす仕組み、sudo は Linux 環境内で使う権限コマンド。WSL を使い始めると sudo にも必ず遭遇するので、「WSL の次に知る用語」として位置づける
- Linux（F-92）との住み分け：Linux エントリは OS 全体の概説、sudo は Linux 上の具体的なコマンドの 1 つ

## 出典メモ

- sudo 公式サイト <https://www.sudo.ws/> — checked 2026-04-30
- man sudo（Linux マニュアルページ）— checked 2026-04-30


## 備考

- root の概念が初学者の壁になりやすい。tagline と「何をしてくれるか」で root を一言補足している
- AI（Claude Code など）への sudo 権限付与は慎重に判断すべき点として、「どこで出会うか」と開発フロー Step 4 に反映した
- 時変情報は特になし（sudo はバージョン変更が仕組みの根本に影響しない安定コマンド）
