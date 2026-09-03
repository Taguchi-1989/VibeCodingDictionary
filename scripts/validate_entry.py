#!/usr/bin/env python3
"""
VibeCodingDictionary エントリ検証スクリプト

Usage:
    # 単体実行：ファイルパスを引数に
    python3 scripts/validate_entry.py content/entries/service/B-1_gemini.md

    # Hook 実行：PostToolUse JSON payload を stdin から受け取る
    echo '{"tool_input":{"file_path":"..."}}' | python3 scripts/validate_entry.py

Exit codes:
    0  全パス
    1  警告のみ（☆ 違反なし。transcript に表示される想定）
    2  ☆ 違反あり（PostToolUse で stderr を Claude に見せる）

設計メモ:
    - docs/quality_checklist.md の ☆ 項目を機械的にチェック
    - archived / sample ステータスはチェック対象外
    - 左ページ 700-800 字、右ページ 250-400 字（100 字超過で ☆ 違反）
    - 標準ライブラリのみ（PyYAML なし、手書き frontmatter parser）
"""

import io
import json
import os
import re
import sys
from pathlib import Path

# Windows cp932 でも絵文字を出力できるように stdout/stderr を UTF-8 に統一
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
if sys.stderr.encoding and sys.stderr.encoding.lower() != "utf-8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


# ─── 設定 ─────────────────────────────────────────

REQUIRED_YAML = [
    "id",
    "title",
    "category",
    "figure_type",
    "page_layout",
    "evaluation_date",
    "status",
]

REQUIRED_SECTIONS = [
    "## tagline",
    "## 何をしてくれるか",
    "## どこで出会うか",
    "## メイン図",
    "## 会話での使い方例",   # 2026-04-26 追加: 左ページ末尾、下チロム右スロット印字
    "## 関連用語",
    "## この用語の見どころ",
    "## 開発フローでの位置（必須）",
    "## 非エンジニアのつまずき",
    "## 私のコメント",
]

MIHIDOKORO_SUBS = [
    "### 1. 役割",
    "### 2. うれしさ",
    "### 3. 注意点",
    "### 4. どこで役立つか",
    "### 5. はじめに",
    "### 6. 深掘り先",
]

# メイン図の型。docs/entry_schema.yaml の figure_type enum と同期させること
FIGURE_TYPES = ("before_after", "structure", "comparison", "workflow", "timeline")

# 前付け（A 章）レイアウト群。詳細は docs/front_section_layout.md §4
# spread_v1 用の必須節・字数合計判定はスキップし、軽い YAML / トーンチェックだけ走らせる
FRONT_LAYOUTS = {
    "front_concept_spread",
    "front_essay",
    "front_anatomy",
    "front_map_index",
    "front_legend_marks",
    "front_swatch",
    "front_log_glossary",
}

# layout 別の related_terms 必須個数（3〜5）。掲載外は任意（空でも警告しない）
FRONT_REQUIRES_RELATED_TERMS = {
    "front_map_index",
    "front_legend_marks",
}

# 旧テンプレで書かれた箇所を検出して移行を促す（警告のみ）
DEPRECATED_HEADINGS = [
    ("どこで効くか", "「どこで効くか」→「どこで役立つか」（AI 臭回避、2026-04-24 決定）"),
    ("## ひとことで", "「ひとことで」は v2 で廃止。内容は tagline に合流してください"),
    ("## バイブコーディングでの位置づけ", "「バイブコーディングでの位置づけ」→「どこで出会うか」（v2 改名）"),
    ("### 5. 最初に理解する範囲", "「最初に理解する範囲」→「はじめに」（v2 改名）"),
    ("🎯 誰向けか", "「🎯 誰向けか」→「👥 誰向けか」（v2 絵文字変更）"),
]

# 強い断定語（本文に入ると減点）
STRONG_ASSERTION_WORDS = ["最新", "最強", "完全に", "絶対に", "必ず"]

# です・ます調から外れるパターン（語尾検出）
# だ調・である調の検出。2026-08-24: 判定を「文末」に限定した。
# 以前は `だ[。\s]` としていたため、連体形の直後に半角スペースが来るだけの
# 「選んだ Transport」「読んだ 本」を、だ調と誤検出していた（日本語の本文では
# 欧文の前に半角スペースを置くのが本書の表記なので、頻繁に踏む）。
# 文末（`。` または行末）に限れば、だ調・である調だけを拾える。
NON_DESU_MASU_PATTERNS = [
    re.compile(r"である(?:。|$)", re.M),
    re.compile(r"(?<![すまりぞ])だ(?:。|$)", re.M),  # "です"や"ます"に続く「だ」は除外
]


# ─── 字数目安（quality_checklist.md §H と一致、v2 誌面ベース） ─────────────────

# セクションごとの [key, display_name, min, max, page]
# 個別セクションは超過/下回りとも「⚠️ 警告」のみ。
# ☆（ブロッキング）は左右ページ合計が 100 字超過したときのみ。
# v2_rules_summary.md §2 の決定版ルールを写したもの。数値変更時は v2_rules_summary を先に動かす。
# min/max の「推奨範囲」。超過は ⚠️ 警告（☆ は左右合計 + 100 字超でのみ）
# (key, display, min, max, page, in_total) — in_total=False は左右合計から除外（独立スロット）
SECTION_TARGETS = [
    # tagline 許容上限 45→60（2026-04-28）：略称・ヌメロニム（MCP / a11y / LLM 等）の
    # tagline 冒頭に正式名称を入れるルール追加に追随。詳細は docs/v2_rules_summary.md §2-3。
    ("tagline",        "tagline",            25,  60, "left",  True),   # 許容 25-60, 推奨 30-38（略称展開含む場合 35-50）
    ("nanishiteku",    "何をしてくれるか",   60, 200, "left",  True),   # 許容 60-200, 推奨 80-150
    ("dokode_deau",    "どこで出会うか",     60, 200, "left",  True),   # 許容 60-200, 推奨 80-150
    # 2026-04-26 追加: 左ページ末尾の独立スロット、下チロム右に印字。左合計には含めない
    ("kaiwa",          "会話での使い方例",   25,  50, "left",  False),
    ("mihidokoro",     "見どころ 6 視点",   120, 240, "right", True),   # 6 視点合計（各 15-40、深掘り 15-50）
    ("kaihatsu_flow",  "開発フローでの位置", 80, 180, "right", True),
    # iter 22（2026-04-25）: 関連用語を左ページから右ページ下段（開発フロー直下）へ移動
    ("related_terms",  "関連用語",           20,  50, "right", True),
]

# 著者記入欄は誌面に出るが、著者本人が後で書く領域。文字数は情報表示のみ（判定しない）。
AUTHOR_INFO_SECTIONS = [
    ("tsumazuki",         "非エンジニアのつまずき"),
    ("watashino_comment", "私のコメント"),
]

# 左右ページ合計の目安と ☆ 閾値（著者欄は合計に含めない）
# iter 22（2026-04-25）: 関連用語（20-50 字）が左→右へ移動したため、左は -20/-50、右は +20/+50 シフト
LEFT_TOTAL_MIN, LEFT_TOTAL_MAX = 155, 250
RIGHT_TOTAL_MIN, RIGHT_TOTAL_MAX = 220, 430
TOTAL_STARS_OVER = 100   # 合計がこの字数を超えて超過すると ☆


# ─── 結果ラッパ ─────────────────────────────────────────

class Report:
    def __init__(self, path: Path):
        self.path = path
        self.star_fails: list[str] = []  # ☆ 違反（exit 2）
        self.warnings: list[str] = []    # 警告（exit 1）
        self.char_table: list[tuple[str, int, int, int, str, str]] = []
        # 各行: (セクション名, min, max, actual, page, judgement)

    def star(self, msg: str):
        self.star_fails.append(msg)

    def warn(self, msg: str):
        self.warnings.append(msg)

    def add_char_row(self, display: str, mn: int, mx: int, actual: int, page: str, judge: str):
        self.char_table.append((display, mn, mx, actual, page, judge))

    @property
    def exit_code(self) -> int:
        if self.star_fails:
            return 2
        if self.warnings:
            return 1
        return 0

    def render_char_table(self) -> str:
        if not self.char_table:
            return ""
        out = [
            "### 文字数チェック\n",
            "| セクション | 目安 | 実測 | 差分 | 判定 |",
            "| :-- | --: | --: | --: | :-- |",
        ]
        for display, mn, mx, actual, page, judge in self.char_table:
            # 著者記入欄は target なし（min=max=0 で表現）
            if mn == 0 and mx == 0:
                target_str = "—"
                diff = "—"
            else:
                target_str = f"{mn}-{mx}"
                if actual < mn:
                    diff = f"-{mn - actual}"
                elif actual > mx:
                    diff = f"+{actual - mx}"
                else:
                    diff = "—"
            row = f"| {display} | {target_str} | {actual} | {diff} | {judge} |"
            out.append(row)
        out.append("")
        return "\n".join(out)

    def render(self) -> str:
        lines = [f"## Validator: {self.path.as_posix()}\n"]
        table = self.render_char_table()
        if table:
            lines.append(table)
        if self.star_fails:
            lines.append("### ❌ ☆ 違反（修正必須）\n")
            for m in self.star_fails:
                lines.append(f"- {m}")
            lines.append("")
        if self.warnings:
            lines.append("### ⚠️ 警告\n")
            for m in self.warnings:
                lines.append(f"- {m}")
            lines.append("")
        if not self.star_fails and not self.warnings:
            lines.append("### ✅ 全チェックパス\n")
        return "\n".join(lines)


# ─── Parser（YAML frontmatter の最小実装） ─────────────────

def parse_frontmatter(content: str) -> tuple[dict, str]:
    """YAML frontmatter と本文を分離する。必要最小限の key:value パーサ。"""
    if not content.startswith("---\n"):
        return {}, content
    end = content.find("\n---\n", 4)
    if end == -1:
        return {}, content
    fm_text = content[4:end]
    body = content[end + 5:]
    data: dict = {}
    current_list_key: str | None = None
    for raw in fm_text.split("\n"):
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        if raw.startswith("  - "):
            if current_list_key:
                data.setdefault(current_list_key, []).append(raw[4:].strip())
            continue
        m = re.match(r"^([A-Za-z_]\w*):\s*(.*)$", raw)
        if m:
            k, v = m.group(1), m.group(2).strip()
            # インラインコメント ` #...` を除去（簡易 YAML 対応、2026-04-28）
            # 値の途中にスペース＋# が現れたらそこ以降をコメントとみなす
            if " #" in v:
                v = v.split(" #", 1)[0].strip()
            if v == "":
                data[k] = []
                current_list_key = k
            else:
                data[k] = v
                current_list_key = None
    return data, body


# ─── 文字数カウント ─────────────────────────────────

def count_chars(text: str) -> int:
    """見出し・HTML コメント・Markdown 装飾・空白を除いた実文字数。"""
    t = re.sub(r"^#+\s.*$", "", text, flags=re.MULTILINE)
    t = re.sub(r"<!--.*?-->", "", t, flags=re.DOTALL)
    t = re.sub(r"\*\*([^*]+)\*\*", r"\1", t)
    t = re.sub(r"^\s*(\d+\.|-)\s*", "", t, flags=re.MULTILINE)
    t = re.sub(r"[\s\n]+", "", t)
    return len(t)


# ─── チェック関数群 ─────────────────────────────────

def check_yaml(fm: dict, r: Report) -> None:
    for key in REQUIRED_YAML:
        if key not in fm or not str(fm[key]).strip():
            r.star(f"A. YAML: 必須キー `{key}` が欠落")
    layout = str(fm.get("page_layout", "")).strip()
    if layout and layout != "spread_v1" and layout not in FRONT_LAYOUTS:
        r.warn(f"A. YAML: `page_layout` が enum 外（{layout}）")

    # evaluation_date の書式
    eval_date = str(fm.get("evaluation_date", "")).strip()
    if eval_date and not re.match(r"^\d{4}-\d{2}-\d{2}$", eval_date):
        r.warn(f"A. YAML: `evaluation_date` が YYYY-MM-DD 形式でない（{eval_date}）")

    # 2026-04-28: title 末尾の括弧書き読み・展開を禁止
    # タイトルは純粋名のみ。読み・日本語訳は title_reading スロットに分離する
    title = str(fm.get("title", "")).strip()
    if re.search(r"[（(][^)）]+[)）]\s*$", title):
        r.warn(
            "A. YAML: `title` 末尾に括弧書きが含まれます — 読み・展開は "
            "`title_reading` フィールドへ移動してください"
            f"（現在: {title}）"
        )

    # title_reading（任意）の字数目安
    reading = str(fm.get("title_reading", "")).strip()
    if reading:
        n = len(reading)
        if n < 2 or n > 30:
            r.warn(
                f"A. YAML: `title_reading` が {n} 字（目安 2〜30、推奨 3〜15）"
            )

    # 2026-08-23: figure_type の enum チェック
    # docs/entry_schema.yaml §figure_type の 5 値。CSS class の割当先なので
    # enum 外だと誌面側でスタイルが当たらない（component_spec_v2.md §2-6）
    figure_type = str(fm.get("figure_type", "")).strip()
    if figure_type and figure_type not in FIGURE_TYPES:
        r.warn(
            f"A. YAML: `figure_type` が enum 外（{figure_type}） — "
            + " / ".join(FIGURE_TYPES)
            + " のいずれかを指定してください"
        )

    # 2026-04-30: importance（任意）の enum チェック A〜E
    # A=必須 / B=一般 / C=中級 / D=上級 / E=開発者向け
    importance = str(fm.get("importance", "")).strip()
    if importance and importance not in ("A", "B", "C", "D", "E"):
        r.warn(
            f"A. YAML: `importance` が `{importance}` — A/B/C/D/E のいずれかを指定してください "
            "(A=必須 / B=一般 / C=中級 / D=上級 / E=開発者向け)"
        )

    # 2026-06-22: reader_level（任意）の書式チェック
    #   - 1〜5 = 刊行スコープ / 6 = 著者の自己学習シェルフ（刊行外）
    #   - 範囲表記は幅 1 段まで（"2-3" / "4-5"）。幅 2 以上は禁止
    #   - 6 は単一値のみ。6 を含む範囲（"5-6" 等）は禁止
    #   詳細: docs/level_policy.md §2-4, §2-6
    rl = str(fm.get("reader_level", "")).strip()
    if rl:
        if not re.match(r"^(\d|\d-\d)$", rl):
            r.warn(
                f"A. YAML: `reader_level` が `{rl}` — `1`〜`6` の単一値か "
                "`2-3` 形式の範囲で指定してください"
            )
        else:
            nums = [int(x) for x in re.findall(r"\d", rl)]
            if any(n < 1 or n > 6 for n in nums):
                r.warn(f"A. YAML: `reader_level` の値が範囲外（{rl}） — 1〜6 で指定してください")
            if "-" in rl:
                lo, hi = min(nums), max(nums)
                if hi - lo >= 2:
                    r.warn(
                        f"A. YAML: `reader_level` の範囲幅が 2 段以上（{rl}） — "
                        "幅は最大 1 段（例 `2-3`）にし、迷ったら単一値に寄せてください"
                    )
                if 6 in nums:
                    r.warn(
                        f"A. YAML: `reader_level` に 6 を含む範囲（{rl}） — "
                        "6 は刊行スコープ外シェルフなので単一値 `6` で指定してください"
                        "（docs/level_policy.md §2-6）"
                    )


def check_structure(body: str, r: Report) -> None:
    for sec in REQUIRED_SECTIONS:
        if sec not in body:
            r.star(f"B/C 構造: 必須セクション `{sec}` が無い")
    found_subs = [s for s in MIHIDOKORO_SUBS if s in body]
    if len(found_subs) < 6:
        missing = [s for s in MIHIDOKORO_SUBS if s not in body]
        r.star(f"C. 見どころ 6 視点: {', '.join(missing)} が無い")


# ─── 前付け（front_*）用の検証関数 ─────────────────────────────────

def check_yaml_front(fm: dict, r: Report) -> None:
    """前付けレイアウト用 YAML チェック（spread_v1 より緩い）。

    - id は `^[A-J]-\\d{1,2}$` または `^front_[a-z_]+$` を許容
    - figure_type は任意（あっても無視）
    - related_terms は layout 別（FRONT_REQUIRES_RELATED_TERMS に載る layout のみ 3〜5 個必須）
    - title / category / page_layout / evaluation_date / status は必須
    """
    entry_id = str(fm.get("id", "")).strip()
    if not entry_id:
        r.star("A. YAML: 必須キー `id` が欠落")
    elif not re.match(r"^([A-J]-\d{1,2}|front_[a-z_]+)$", entry_id):
        r.warn(
            f"A. YAML: `id` が letter ID でも `^front_` 接頭辞でもない（{entry_id}）"
        )

    for key in ("title", "category", "page_layout", "evaluation_date", "status"):
        if key not in fm or not str(fm[key]).strip():
            r.star(f"A. YAML: 必須キー `{key}` が欠落")

    layout = str(fm.get("page_layout", "")).strip()
    if layout and layout not in FRONT_LAYOUTS:
        r.warn(
            f"A. YAML: `page_layout` が front_* enum 外（{layout}） — "
            "docs/front_section_layout.md §4-1 の 7 値から選んでください"
        )

    # evaluation_date 書式
    eval_date = str(fm.get("evaluation_date", "")).strip()
    if eval_date and not re.match(r"^\d{4}-\d{2}-\d{2}$", eval_date):
        r.warn(f"A. YAML: `evaluation_date` が YYYY-MM-DD 形式でない（{eval_date}）")

    # related_terms: layout が要求するときだけ個数を見る
    if layout in FRONT_REQUIRES_RELATED_TERMS:
        related = fm.get("related_terms")
        if not isinstance(related, list) or not (3 <= len(related) <= 5):
            n = len(related) if isinstance(related, list) else 0
            r.warn(
                f"A. YAML: `related_terms` が {layout} では 3〜5 個必要（現在 {n} 件）"
            )

    # spread_position: 同居 layout（A-3+A-9 / A-4+A-5+A-6 / A-7+A-8 / A-10+A-11）で
    # 左右どちらの面を担当するかを明示する任意キー
    sp = str(fm.get("spread_position", "")).strip()
    if sp and sp not in ("left", "right", "full"):
        r.warn(
            f"A. YAML: `spread_position` が `left` / `right` / `full` 以外（{sp}）"
        )

    # title_reading（任意）
    reading = str(fm.get("title_reading", "")).strip()
    if reading:
        n = len(reading)
        if n < 2 or n > 30:
            r.warn(f"A. YAML: `title_reading` が {n} 字（目安 2〜30）")


AUTHOR_FIELD_KEYS = {
    "非エンジニアのつまずき": "stumble",
    "私のコメント": "my_comment",
}


def author_field_block(body: str, heading: str) -> str:
    """著者記入欄の中身を切り出す。

    全エントリには `<!-- user-input:start key="..." -->` 〜 `<!-- user-input:end ... -->`
    のマーカーが埋め込まれている（scripts/add_user_input_markers.py）。RepoEdit が
    スマホから編集する範囲もこのマーカーで、著者の記入は必ずこの内側に入る。

    マーカーを優先して読み、無いファイル（旧形式・前付けなど）だけ見出し起点の
    切り出しにフォールバックする。

    注意: 以前は見出し起点の切り出しだけを使っていたが、終端の先読みが
    `\\n<!--` を含むため **user-input マーカーそのもの**で止まり、切り出し結果が
    常に空になっていた。マーカー導入以降、著者欄の判定が全件 False に倒れていた
    （2026-09-02 修正）。
    """
    key = AUTHOR_FIELD_KEYS.get(heading)
    if key:
        m = re.search(
            r'<!-- user-input:start key="%s" -->(.*?)<!-- user-input:end' % key,
            body,
            re.DOTALL,
        )
        if m:
            return m.group(1)
    m = re.search(rf"## {re.escape(heading)}\n(.*?)(?=\n## |\Z)", body, re.DOTALL)
    return m.group(1) if m else ""


def check_author_fields_empty(body: str, status: str, r: Report) -> None:
    """著者欄が空スケルトンのままか。

    - status が `drafting` のときは ☆ 違反（AI がまだ書いている段階なので空が正）
    - status が `needs_review` 以降は**何も言わない**。著者が記入済みなのが正常な姿で、
      そこに警告を出すと「正しく仕事が終わっている状態」がノイズになる
      （2026-09-02: 記入検出のバグを直したところ 326 件が警告に化けたため整理）
    """
    is_strict = status in ("drafting", "candidate", "", None)
    if not is_strict:
        return

    # 非エンジニアのつまずき：`-` のみで、語句なしか
    block = author_field_block(body, "非エンジニアのつまずき")
    if block:
        for line in block.split("\n"):
            line = line.strip()
            if line.startswith("-") and len(line) > 1 and line[1:].strip():
                r.star(
                    f"D. 著者欄: 「非エンジニアのつまずき」に記入あり（{line[:40]}…）"
                    " — drafting 中は空スケルトンのままに"
                )
                break

    # 私のコメント：4 ラベル（🎯 / 👥 どちらも許容）
    label_keys = ["第一印象", "良い点", "ダメな点", "誰向けか"]
    block = author_field_block(body, "私のコメント")
    if block:
        for lbl in label_keys:
            for line in block.split("\n"):
                if lbl in line and ":" in line:
                    after = line.split(":", 1)[-1].strip()
                    if after:
                        r.star(
                            f"D. 著者欄: 「私のコメント」の {lbl} に記入あり（{after[:40]}）"
                            " — drafting 中は空ラベルのままに"
                        )
                        break


def check_author_line_limits(body: str, r: Report) -> None:
    """著者記入欄の 1 行ごとの上限を警告。

    - 私のコメント: ラベル後の本文 45 字以内（推奨 25〜40）
    - 非エンジニアのつまずき: 1 項目 60 字以内（推奨 30〜50）
    上限超過は ⚠️。著者の最終判断で残してもよいが、誌面枠を割る可能性が高い。
    """
    MY_COMMENT_LIMIT = 45
    TSUMAZUKI_LIMIT = 60
    LABEL_RE = re.compile(r"^([^\w]*[^\s:：]+)\s*[:：]\s*(.*)$")

    # 私のコメント
    m = re.search(r"## 私のコメント\n(.*?)(?=\n## |\n<!--)", body, re.DOTALL)
    if m:
        for line in m.group(1).split("\n"):
            line = line.strip()
            if not line.startswith("- "):
                continue
            body_text = line[2:].strip()
            mm = LABEL_RE.match(body_text)
            content = mm.group(2).strip() if mm else body_text
            if not content:
                continue
            if len(content) > MY_COMMENT_LIMIT:
                head = (mm.group(1) + ": ") if mm else ""
                r.warn(
                    f"H. 私のコメント: {head}{len(content)} 字（上限 {MY_COMMENT_LIMIT}） — "
                    f"「{content[:30]}…」"
                )

    # 非エンジニアのつまずき
    m = re.search(r"## 非エンジニアのつまずき\n(.*?)(?=\n## |\n<!--)", body, re.DOTALL)
    if m:
        for line in m.group(1).split("\n"):
            line = line.strip()
            if not line.startswith("- "):
                continue
            content = line[2:].strip()
            if not content:
                continue
            if len(content) > TSUMAZUKI_LIMIT:
                r.warn(
                    f"H. 非エンジニアのつまずき: {len(content)} 字（上限 {TSUMAZUKI_LIMIT}） — "
                    f"「{content[:30]}…」"
                )


def extract_section(body: str, heading: str) -> str:
    """`## <heading>` の本文を取り出す。次の `## ` またはファイル終端まで。"""
    m = re.search(re.escape("## " + heading) + r"\n(.*?)(?=\n## |\Z)", body, re.DOTALL)
    return m.group(1) if m else ""


def extract_mihidokoro_body(body: str) -> str:
    """見どころセクション（### 1〜6 の合計）を取り出す。"""
    section = extract_section(body, "この用語の見どころ")
    return section


def extract_kaihatsu_flow_body(body: str) -> str:
    """開発フローセクションを取り出す。"""
    section = extract_section(body, "開発フローでの位置（必須）")
    return section


def judge_section(actual: int, mn: int, mx: int) -> tuple[str, str]:
    """個別セクション判定（✅ / ⚠️ のみ）。"""
    if mn <= actual <= mx:
        return "✅", ""
    if actual > mx:
        return "⚠️", f"+{actual - mx} 字超過"
    return "⚠️", f"-{mn - actual} 字不足"


def judge_total(actual: int, mn: int, mx: int) -> tuple[str, str]:
    """合計判定（☆ 違反あり）。100 字超過で ❌ ☆。"""
    if mn <= actual <= mx:
        return "✅", ""
    if actual > mx:
        over = actual - mx
        if over > TOTAL_STARS_OVER:
            return "❌ ☆", f"+{over} 字超過（{TOTAL_STARS_OVER} 字超で ☆）"
        return "⚠️", f"+{over} 字超過"
    return "⚠️", f"-{mn - actual} 字不足"


def check_char_counts(body: str, r: Report) -> None:
    """各セクションと左右ページ合計を個別に判定。著者欄は情報表示のみ。"""

    heading_map = {
        "tagline": "tagline",
        "nanishiteku": "何をしてくれるか",
        "dokode_deau": "どこで出会うか",
        "kaiwa": "会話での使い方例",   # 2026-04-26 追加
        "related_terms": "関連用語",
    }
    author_heading_map = {
        "tsumazuki": "非エンジニアのつまずき",
        "watashino_comment": "私のコメント",
    }

    left_total = 0
    right_total = 0

    # 採点対象セクション
    for key, display, mn, mx, page, in_total in SECTION_TARGETS:
        if key in heading_map:
            text = extract_section(body, heading_map[key])
        elif key == "mihidokoro":
            text = extract_mihidokoro_body(body)
        elif key == "kaihatsu_flow":
            text = extract_kaihatsu_flow_body(body)
        else:
            text = ""

        actual = count_chars(text)
        # in_total=False のセクション（会話での使い方例など独立スロット）は左右合計に含めない
        if in_total:
            if page == "left":
                left_total += actual
            else:
                right_total += actual

        mark, reason = judge_section(actual, mn, mx)
        judgement = mark + ((" " + reason) if reason else "")
        r.add_char_row(display, mn, mx, actual, page, judgement)

        if mark.startswith("⚠️"):
            r.warn(f"H. {display}: {actual} 字（目安 {mn}-{mx}、{reason}）")

    # 著者記入欄は情報表示のみ（著者が書く領域なので判定しない）
    for key, display in AUTHOR_INFO_SECTIONS:
        heading = author_heading_map.get(key)
        if not heading:
            continue
        text = extract_section(body, heading)
        actual = count_chars(text)
        r.add_char_row(display, 0, 0, actual, "right", "ℹ️ 著者記入欄")

    # 著者欄の 1 行ごとの上限チェック（2026-05-02 追加：誌面はみ出し防止）
    check_author_line_limits(body, r)

    # 左右ページ合計（著者欄は含めない）
    left_mark, left_reason = judge_total(left_total, LEFT_TOTAL_MIN, LEFT_TOTAL_MAX)
    left_judge = left_mark + ((" " + left_reason) if left_reason else "")
    r.add_char_row("**左ページ合計**", LEFT_TOTAL_MIN, LEFT_TOTAL_MAX, left_total, "left", left_judge)
    if left_mark.startswith("❌"):
        r.star(f"H. 左ページ合計: {left_total} 字（目安 {LEFT_TOTAL_MIN}-{LEFT_TOTAL_MAX}、{left_reason}）")
    elif left_mark.startswith("⚠️"):
        r.warn(f"H. 左ページ合計: {left_total} 字（目安 {LEFT_TOTAL_MIN}-{LEFT_TOTAL_MAX}、{left_reason}）")

    right_mark, right_reason = judge_total(right_total, RIGHT_TOTAL_MIN, RIGHT_TOTAL_MAX)
    right_judge = right_mark + ((" " + right_reason) if right_reason else "")
    r.add_char_row("**右ページ合計**", RIGHT_TOTAL_MIN, RIGHT_TOTAL_MAX, right_total, "right", right_judge)
    if right_mark.startswith("❌"):
        r.star(f"H. 右ページ合計: {right_total} 字（目安 {RIGHT_TOTAL_MIN}-{RIGHT_TOTAL_MAX}、{right_reason}）")
    elif right_mark.startswith("⚠️"):
        r.warn(f"H. 右ページ合計: {right_total} 字（目安 {RIGHT_TOTAL_MIN}-{RIGHT_TOTAL_MAX}、{right_reason}）")


def extract_printed_body(body: str) -> str:
    """誌面に刷られる本文だけを返す（2026-08-24 追加）。

    `## 非エンジニアのつまずき` 以降は「著者記入欄」と「裏台帳メモ」で、
    - 著者記入欄（非エンジニアのつまずき／私のコメント）は**著者本人の一人称の声**。
      AI は触らない決まりなので（CLAUDE.md §3）、トーン警告を出しても直せない
    - 裏台帳メモ（誌面ポンチ絵メモ／コミュニティ補完メモ／出典メモ／備考）は
      デザイン担当・次セッション向けの申し送りで、誌面には出ない
    どちらもトーン規則（です・ます／強い断定語）の対象外とする。
    """
    m = re.search(r"\n## 非エンジニアのつまずき", body)
    return body[: m.start()] if m else body


def check_tone(body: str, r: Report) -> None:
    # 旧テンプレの残骸（v1 → v2 移行ヘルパ）。警告のみ（☆ にはしない）
    # ここは構造の話なので全文を見る
    for pat, msg in DEPRECATED_HEADINGS:
        if pat in body:
            r.warn(f"F. v1 テンプレの名残: `{pat}` — {msg}")

    # トーン規則は誌面本文にだけ適用する
    printed = extract_printed_body(body)

    # である調／だ調の検出
    for rx in NON_DESU_MASU_PATTERNS:
        matches = rx.findall(printed)
        if matches:
            # 誤検出しやすいのでサンプルだけ警告
            sample = str(rx.pattern)
            r.warn(f"F. トーン: です・ます外れの疑いあり（{sample} のパターン、要目視確認）")
            break

    # 強い断定語
    for w in STRONG_ASSERTION_WORDS:
        if re.search(rf"(?<![「『\w]){re.escape(w)}", printed):
            r.warn(f"F. トーン: 強い断定語「{w}」が入っている可能性（要確認）")


def check_sources_date(body: str, fm: dict, r: Report) -> None:
    """出典メモの `checked YYYY-MM-DD` 形式を確認。time-varying entry のみ。"""
    pricing = str(fm.get("pricing_note", "")).strip()
    version = str(fm.get("version_status", "")).strip()
    time_varying = bool(pricing or version)
    if not time_varying:
        return

    m = re.search(r"## 出典メモ\n(.*?)(?=\n## |\Z)", body, re.DOTALL)
    if not m:
        r.star("E. 出典メモ: 時変情報を扱うのに `## 出典メモ` セクションが無い")
        return
    sources = m.group(1)
    if not re.search(r"checked\s+\d{4}-\d{2}-\d{2}", sources):
        r.star("E. 出典メモ: `checked YYYY-MM-DD` 形式の記載が無い（時変情報を扱っているのに）")


# ─── メイン ─────────────────────────────────────────

def resolve_path_from_stdin_or_argv() -> Path | None:
    """Hook (JSON on stdin) か CLI 引数 か。"""
    # 引数優先
    if len(sys.argv) > 1:
        return Path(sys.argv[1])

    # stdin JSON
    if not sys.stdin.isatty():
        try:
            data = sys.stdin.read()
            if not data.strip():
                return None
            payload = json.loads(data)
            tool_input = payload.get("tool_input", {})
            file_path = tool_input.get("file_path") or payload.get("tool_response", {}).get("filePath")
            if file_path:
                return Path(file_path)
        except Exception:
            return None
    return None


def should_validate(path: Path) -> bool:
    """content/entries/**/*.md または content/frontmatter/*.md を対象に。

    common/（A 章）と frontmatter/（扉）の分岐は main() 側で page_layout を見て決める:
      - page_layout が front_* → 前付け用ルールセット（軽い YAML / トーンのみ）
      - それ以外で common/ → 当面スキップ（spread_v1 から front_* への移行中）
      - それ以外 → 既存の spread_v1 検証
    """
    posix = path.as_posix()
    if "/content/frontmatter/" in posix or posix.startswith("content/frontmatter/"):
        return True
    return bool(re.search(r"(^|/)content/entries/[^/]+/[^/]+\.md$", posix))


def promote_to_needs_review(path: Path) -> bool:
    """drafting → needs_review に YAML を直接書き換える。

    - validator の全チェックがパスしたエントリのみで呼ばれる
    - YAML frontmatter 内の `status: drafting` だけを置換（本文・コメントは触らない）
    - Python の直接書き込みなので Edit/Write フックは再発火しない（ループしない）
    """
    return _replace_status(path, "drafting", "needs_review")


def ready_autopromote_enabled() -> bool:
    """needs_review → ready の自動昇格を有効にするか。

    既定は **無効**。CLAUDE.md の運用（「自動昇格は drafting → needs_review のみ。
    著者レビューが終わったら手で ready に上げる」）に合わせている。

    経緯: 実装側にはもともと自動昇格が書かれていたが、著者欄の検出
    （is_author_fields_filled）が user-input マーカー導入以降ずっと False に
    倒れていたため一度も発火していなかった。2026-09-02 に検出を直したところ、
    そのままだと 82 件が一斉に ready へ書き換わる状態だったので、
    文書側の仕様に合わせて既定オフのフラグにした。

    自動昇格させたいときは環境変数で明示的に有効化する:
        VCD_AUTOPROMOTE_READY=1 python3 scripts/update_review_queue.py
    """
    return os.environ.get("VCD_AUTOPROMOTE_READY", "").strip() in ("1", "true", "yes")


def promote_to_ready(path: Path) -> bool:
    """needs_review → ready に YAML を直接書き換える。

    - 著者欄が全項目埋まったエントリのみで呼ばれる
    - YAML frontmatter 内の `status: needs_review` だけを置換
    - ready_autopromote_enabled() が False のときは何もしない
    """
    if not ready_autopromote_enabled():
        return False
    return _replace_status(path, "needs_review", "ready")


def _replace_status(path: Path, old: str, new: str) -> bool:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return False
    if not text.startswith("---\n"):
        return False
    end = text.find("\n---\n", 4)
    if end == -1:
        return False
    fm_text = text[4:end]
    rest = text[end:]
    new_fm = re.sub(
        rf"^status:\s*{re.escape(old)}\s*$",
        f"status: {new}",
        fm_text,
        flags=re.MULTILINE,
    )
    if new_fm == fm_text:
        return False
    try:
        path.write_text("---\n" + new_fm + rest, encoding="utf-8")
    except Exception:
        return False
    return True


def is_author_fields_filled(body: str) -> bool:
    """A 案（厳しめ）: 著者欄が完全に埋まっているか判定する。

    needs_review → ready の自動昇格条件として使う。

    - 「## 非エンジニアのつまずき」: ハイフン箇条書きで語句が入った行が 1 つ以上
    - 「## 私のコメント」: 4 ラベル（第一印象 / 良い点 / ダメな点 / 誰向けか）
      すべてのラベル後に語句が入っている

    どちらか欠けていたら False。
    """
    tsumazuki_filled = False
    for line in author_field_block(body, "非エンジニアのつまずき").split("\n"):
        line = line.strip()
        if line.startswith("-") and len(line) > 1 and line[1:].strip():
            tsumazuki_filled = True
            break
    if not tsumazuki_filled:
        return False

    block = author_field_block(body, "私のコメント")
    if not block:
        return False
    label_keys = ["第一印象", "良い点", "ダメな点", "誰向けか"]
    for lbl in label_keys:
        found = False
        for line in block.split("\n"):
            if lbl in line and ":" in line:
                after = line.split(":", 1)[-1].strip()
                if after:
                    found = True
                    break
        if not found:
            return False
    return True


def reader_level_max(fm: dict) -> int:
    """reader_level の上限レベル（数字）を返す。未記入は 0。
    6 を含むなら刊行スコープ外シェルフ（docs/level_policy.md §2-6）。"""
    nums = [int(x) for x in re.findall(r"\d", str(fm.get("reader_level", "")))]
    return max(nums) if nums else 0


def main() -> int:
    path = resolve_path_from_stdin_or_argv()
    if path is None:
        # ファイルが特定できなければ静かに終了（他の Edit/Write には干渉しない）
        return 0

    if not should_validate(path):
        return 0

    if not path.exists():
        print(f"validator: file not found: {path}", file=sys.stderr)
        return 0

    try:
        content = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"validator: read error: {e}", file=sys.stderr)
        return 0

    fm, body = parse_frontmatter(content)

    # archived / sample / skeleton はチェック対象外
    # skeleton は本文未着手の枠だけが置かれた状態（2026-04-28 追加）
    status = str(fm.get("status", "")).strip()
    if status in ("archived", "sample", "skeleton"):
        return 0

    # 前付けレイアウト（front_*）: 軽い検証ルートに分岐
    # 必須節・字数合計の検査はスキップ。自動昇格も無効（著者本人レビュー必須）
    # 未知の front_xxx も同じ経路に流す（check_yaml_front が enum 外 warn を出す）
    layout = str(fm.get("page_layout", "")).strip()
    if layout.startswith("front_"):
        r = Report(path)
        check_yaml_front(fm, r)
        check_tone(body, r)
        rendered = r.render()
        if r.star_fails:
            print(rendered, file=sys.stderr)
        else:
            print(rendered)
        return r.exit_code

    # spread_v1 で common/ にあるエントリは移行中のため当面スキップ
    # （A-1〜A-11 が front_* に移行し終えるとこの除外は不要になる）
    posix = path.as_posix()
    if "/content/entries/common/" in posix or posix.startswith("content/entries/common/"):
        return 0

    # reader_level 6 = 著者の自己学習シェルフ（刊行スコープ外・docs/level_policy.md §2-6）。
    # 誌面レイアウト前提の制約（字数・ですます・著者欄）は外し、
    # YAML と構造の最小サニティ＋出典日だけ見る。深掘り・数式・長文・常体 OK。
    # 自動昇格もしない（著者本人が status を管理する学習ノートのため）。
    if reader_level_max(fm) >= 6:
        r = Report(path)
        check_yaml(fm, r)
        check_structure(body, r)
        check_sources_date(body, fm, r)
        rendered = r.render()
        if r.star_fails:
            print(rendered, file=sys.stderr)
        else:
            print(rendered)
        return r.exit_code

    r = Report(path)
    check_yaml(fm, r)
    check_structure(body, r)
    check_author_fields_empty(body, status, r)
    check_char_counts(body, r)
    check_tone(body, r)
    check_sources_date(body, fm, r)

    # 自動昇格ゲート
    # 1) drafting + ☆違反0 + 警告0   → needs_review
    # 2) needs_review + ☆違反0 + 著者欄が全項目埋まっている → ready
    #    （著者欄を埋めると check_author_fields_empty が「警告」を出すが、これは
    #     情報通知の警告なので昇格判定では除外する。判定は ☆ 違反のみで見る）
    promoted_msg = ""
    if status == "drafting" and not r.star_fails and not r.warnings:
        if promote_to_needs_review(path):
            promoted_msg = "- status: `drafting` → `needs_review`（全チェックパスのため）"
    elif status == "needs_review" and not r.star_fails and is_author_fields_filled(body):
        if promote_to_ready(path):
            promoted_msg = "- status: `needs_review` → `ready`（著者欄が全項目埋まったため）"

    # 出力：☆ 違反は stderr（Claude に見せる）、警告は stdout
    rendered = r.render()
    if promoted_msg:
        rendered += "\n### 🆙 自動昇格\n\n" + promoted_msg + "\n"
    if r.star_fails:
        print(rendered, file=sys.stderr)
    else:
        print(rendered)
    return r.exit_code


if __name__ == "__main__":
    sys.exit(main())
