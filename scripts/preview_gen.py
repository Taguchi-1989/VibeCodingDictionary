#!/usr/bin/env python3
"""
開発用プレビュー生成器（dev only）

目的:
- content/entries/**/*.md をブラウザで連続閲覧できる HTML に変換
- iter 22 以降の紙面ルール（右ページ冒頭タイトル削除、関連用語右ページ下段、ポンチ絵拡大）が
  他エントリでも成立するかを著者が確認する
- 各 HTML に prev/next リンクを入れて、entries.csv の順で前後に移動できる
- 右上ハンバーガーから全エントリに飛べる

**本ツールは本番の生成器ではない**。本番は実装担当が Astro + React で作る
（docs/component_spec_v2.md §0 参照）。本スクリプトは iter 中のレイアウト検証専用。

出力先: drafts/prototypes/preview/

Usage:
    python scripts/preview_gen.py
    python scripts/preview_gen.py --open      # 生成後に index.html をブラウザで開く
"""

from __future__ import annotations

import argparse
import csv
import io
import re
import sys
import math
import webbrowser
from html import escape
from pathlib import Path

if sys.platform == "win32" and hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", line_buffering=True)

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "ledgers" / "entries.csv"
ENTRIES_DIR = ROOT / "content" / "entries"
PREVIEW_DIR = ROOT / "drafts" / "prototypes" / "preview"
PONCHI_SVG_DIR = ROOT / "drafts" / "ponchi"
PONCHI_FINAL_DIR = ROOT / "assets" / "ponchi" / "final"
OVERLAY_CSS_REL = "../mockups/design_philosophy_v2/overlay.css"
OVERLAY_TIGHT_CSS_REL = "../mockups/design_philosophy_v2/overlay-tight.css"
BASE_CSS_REL = "../mockups/design_philosophy_v2/base.css"

# ─── 章定義（chapters.yaml の簡易読み込み、PyYAML 非依存） ──────────

CHAPTER_META: dict[str, dict[str, str]] = {
    "A": {"label": "はじめに・読み方", "tilde": "読み方"},
    "B": {"label": "サービス", "tilde": "サービス"},
    "C": {"label": "人・会社", "tilde": "人・会社"},
    "D": {"label": "モデル", "tilde": "モデル"},
    "E": {"label": "ベンチマーク", "tilde": "ベンチマーク"},
    "F": {"label": "ことば・しくみ", "tilde": "技術用語"},
    "G": {"label": "バイブ特有", "tilde": "バイブ特有"},
    "H": {"label": "歴史", "tilde": "歴史"},
    "I": {"label": "MCP", "tilde": "MCP"},
    "J": {"label": "一般語彙", "tilde": "一般語彙"},
}

EXPERIENCE_LABELS = {
    "hands_on": "触った",
    "partial": "少しだけ触った",
    "research_only": "調査ベース",
}

# 物理ページのオフセット。表紙・目次・序章ページの合計をここで決める。
# 例: 表紙(1) + 目次(2-3) があるなら START_PAGE = 4。
START_PAGE = 4

# 各エントリの既定消費ページ数（見開き 1 つ＝ 2 ページ）。
# entries.csv の `pages` 列 または frontmatter の `pages` で個別上書き可能。
DEFAULT_ENTRY_PAGES = 2


def format_entry_id(entry_id: str) -> str:
    """B-2 → B-02 のように先頭の数値部分をゼロ詰め整形（誌面表示用）。

    URL/ファイル名としては使わない。drawer・index・誌面 chrome の表示で揃えるため。
    B-2-a のような派生 ID は数値部分だけ整形して "B-02-a" を返す。
    """
    if "-" not in entry_id:
        return entry_id
    letter, rest = entry_id.split("-", 1)
    parts = rest.split("-")
    if parts[0].isdigit():
        parts[0] = f"{int(parts[0]):02d}"
        return f"{letter}-{'-'.join(parts)}"
    return entry_id


def split_title(title: str) -> tuple[str, str]:
    """`Context（コンテキスト）` → (`Context`, `コンテキスト`) のように主・副に分離。

    主タイトルはデカく太く、副タイトルは小さく細く下に置く想定。
    全角・半角の括弧両方に対応。括弧がなければ副は空文字。
    """
    m = re.match(r"^(.+?)\s*[（(]\s*(.+?)\s*[）)]\s*$", title)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return title, ""


# ─── パーサ ────────────────────────────────────────

def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.DOTALL)
    if not m:
        return {}, text
    raw = m.group(1)
    body = text[m.end():]
    fm: dict = {}
    current_list_key: str | None = None
    for line in raw.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            current_list_key = None
            continue
        if stripped.startswith("- ") and current_list_key:
            fm[current_list_key].append(stripped[2:].strip().strip("'\""))
            continue
        m2 = re.match(r"^(\S[^:]*?):\s*(.*)$", line)
        if m2:
            key = m2.group(1).strip()
            val = m2.group(2).strip()
            if val == "" or val == "[]":
                fm[key] = []
                current_list_key = key
            else:
                fm[key] = val.strip('"').strip("'")
                current_list_key = None
    return fm, body


def extract_section(body: str, heading: str) -> str:
    """## <heading> の本文ブロックを返す（次の ## 直前まで）"""
    m = re.search(re.escape("## " + heading) + r"\s*\n(.*?)(?=\n## |\Z)", body, re.DOTALL)
    return m.group(1).strip() if m else ""


def extract_subsection(body: str, parent_heading: str, child_heading: str) -> str:
    """## parent の中から ### child の本文を返す"""
    section = extract_section(body, parent_heading)
    m = re.search(re.escape("### " + child_heading) + r"\s*\n(.*?)(?=\n### |\Z)", section, re.DOTALL)
    return m.group(1).strip() if m else ""


def _split_into_sentences(text: str) -> list[str]:
    """日本語文を「。」「！」「？」で分割。句点はそのまま末尾に残す。"""
    parts = re.findall(r"[^。！？]+[。！？]?", text)
    return [p.strip() for p in parts if p.strip()]


def _soft_split_long_sentence(sentence: str, limit: int = 70) -> list[str]:
    """1 文が長すぎる場合に「、」で割る。

    全文長が limit 以下ならそのまま。超える場合は、中央寄りの「、」で 2 つに割る。
    両側に最低 15 字以上残らない位置でしか割れない場合はあきらめてそのまま返す。
    """
    if len(sentence) <= limit:
        return [sentence]
    # 「、」候補位置を全部取り、両側 >= 15 字の条件で中央に最も近いものを選ぶ
    n = len(sentence)
    midpoint = n // 2
    candidates: list[int] = []
    for i, ch in enumerate(sentence):
        if ch == "、" and 15 <= i <= n - 16:
            candidates.append(i)
    if not candidates:
        return [sentence]
    best = min(candidates, key=lambda i: abs(i - midpoint))
    head = sentence[:best].rstrip("、").strip()
    tail = sentence[best + 1:].lstrip("、").strip()
    if not head or not tail:
        return [sentence]
    # head の末尾には何も足さない（「、」での分割は連用形の続きが多いため句点を補うと不自然）
    return [head, tail]


def extract_tsumazuki_bullets(body: str) -> list[str]:
    """## 非エンジニアのつまずき の箇条書きを返す。

    1 つの bullet に複数文が詰まっている場合は文単位で分割し、上限 3 文ぶんを返す。
    プレースホルダ行はスキップ。
    """
    section = extract_section(body, "非エンジニアのつまずき")
    bullets: list[str] = []
    for line in section.splitlines():
        m = re.match(r"^\s*-\s+(.+)$", line)
        if not m:
            continue
        text = m.group(1).strip()
        if re.fullmatch(r"[（(]\s*著者記入欄[・·]?空?\s*[）)]", text):
            continue
        # 句点で文分割。さらに 70 字超の長文は「、」でソフト分割する。
        sentences = _split_into_sentences(text) or [text]
        for s in sentences:
            bullets.extend(_soft_split_long_sentence(s))
        if len(bullets) >= 3:
            break
    return bullets[:3]


COMMENT_LABELS = ["第一印象", "良い点", "ダメな点", "誰向けか"]


def extract_comment_items(body: str) -> dict[str, str]:
    """## 私のコメント の 4 ラベル（第一印象/良い点/ダメな点/誰向けか）の値を抽出。

    フォーマット例:
        - 🙂 第一印象: 〜
        - 👍 良い点: 〜
        - 👎 ダメな点: 〜
        - 👥 誰向けか: 〜

    絵文字の有無や `: 〜` の半角全角を吸収。値が空またはプレースホルダの場合は空文字を返す。
    """
    section = extract_section(body, "私のコメント")
    result: dict[str, str] = {label: "" for label in COMMENT_LABELS}
    for line in section.splitlines():
        m = re.match(r"^\s*-\s*(.+)$", line)
        if not m:
            continue
        content = m.group(1).strip()
        for label in COMMENT_LABELS:
            # 行内に「ラベル:」が含まれていれば後続を値として取り出す
            pat = re.compile(rf"{re.escape(label)}\s*[:：]\s*(.*)$")
            mm = pat.search(content)
            if mm:
                value = mm.group(1).strip()
                if re.fullmatch(r"[（(]\s*著者記入欄[・·]?空?\s*[）)]", value):
                    value = ""
                result[label] = value
                break
    return result


def render_tsumazuki_items(bullets: list[str]) -> str:
    """非エンジニアのつまずきの <li> を生成。

    実コンテンツ件数ぶん（1〜3）だけ並べる。空はプレースホルダ 1 行のみ。"""
    if not bullets:
        return '<li class="placeholder">（著者記入欄・空）</li>'
    items = [f"<li>{escape(b)}</li>" for b in bullets[:3]]
    return "\n              ".join(items)


def render_comment_items(values: dict[str, str]) -> str:
    """私のコメント 4 ラベルぶんの <li> を生成。空はプレースホルダ。"""
    items: list[str] = []
    for label in COMMENT_LABELS:
        v = values.get(label, "")
        if v:
            items.append(f'<li><div><span class="cl">{label}:</span>{escape(v)}</div></li>')
        else:
            items.append(f'<li><div><span class="cl">{label}:</span>（著者記入欄・空）</div></li>')
    return "\n              ".join(items)


def strip_md(text: str) -> str:
    """HTML コメント除去・Markdown 装飾除去・空白整理"""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = text.strip()
    return text


def render_body_html(md_text: str) -> str:
    """段落と箇条書き（- 行）を HTML に変換。空行で段落区切り。"""
    if not md_text:
        return ""
    lines = md_text.splitlines()
    parts: list[str] = []
    buf_para: list[str] = []
    buf_list: list[str] = []

    def flush_para() -> None:
        nonlocal buf_para
        if buf_para:
            parts.append(f"<p>{escape(' '.join(buf_para))}</p>")
            buf_para = []

    def flush_list() -> None:
        nonlocal buf_list
        if buf_list:
            items = "".join(f"<li>{escape(li)}</li>" for li in buf_list)
            parts.append(f"<ul>{items}</ul>")
            buf_list = []

    for line in lines:
        stripped = line.strip()
        m = re.match(r"^-\s+(.*)$", stripped)
        if m:
            flush_para()
            buf_list.append(m.group(1).strip())
        elif not stripped:
            flush_list()
            flush_para()
        else:
            flush_list()
            buf_para.append(stripped)
    flush_list()
    flush_para()
    return "\n".join(parts)


def extract_flow_steps(body: str) -> list[tuple[str, str]]:
    """## 開発フローでの位置（必須）の 1. 〜 N. を (label, note) に分解"""
    section = extract_section(body, "開発フローでの位置（必須）")
    steps: list[tuple[str, str]] = []
    for line in section.splitlines():
        m = re.match(r"^\s*(\d+)\.\s+(.*?)\s*$", line)
        if not m:
            continue
        raw = m.group(2).strip()
        if " — " in raw:
            label, note = raw.split(" — ", 1)
        elif " - " in raw:
            label, note = raw.split(" - ", 1)
        else:
            label, note = raw, ""
        steps.append((label.strip(), note.strip()))
    return steps


def extract_related_terms(body: str, yaml_terms: list[str]) -> list[str]:
    """## 関連用語 の本文からピル用の用語名を抽出。なければ YAML の related_terms を使う"""
    section = extract_section(body, "関連用語")
    terms: list[str] = []
    for line in section.splitlines():
        m = re.match(r"^\s*-\s+(.*?)\s*$", line)
        if not m:
            continue
        raw = m.group(1).strip()
        # "用語名 — 隣接メモ" の左側を取る
        if " — " in raw:
            terms.append(raw.split(" — ", 1)[0].strip())
        else:
            terms.append(raw)
    return terms or yaml_terms


def extract_ponchi(body: str, title: str) -> tuple[str, str]:
    """## 誌面ポンチ絵メモ > ### メイン図 の caption を拾う（description 風 1 文を抽出）"""
    memo = extract_section(body, "誌面ポンチ絵メモ")
    # 「描く内容:」「吹き出し:」「中央に置くキーワード:」あたりから 1〜2 文を作る
    lines = memo.splitlines()
    draw = ""
    for line in lines:
        m = re.match(r"^\s*-\s+(?:描く内容|登場人物|シーン[^:]*|吹き出し|中央に置く[^:]*):\s*(.+)$", line)
        if m:
            draw = m.group(1).strip()
            break
    return (f"{title} を使う人", draw or f"{title} を実際に使っている 1 コマ。擬人化ポンチ絵は後日差し込み。")


def extract_reference_url(body: str) -> tuple[str | None, str | None]:
    """## 出典メモ の先頭行から URL と checked 日付を抽出"""
    section = extract_section(body, "出典メモ")
    for line in section.splitlines():
        m = re.match(r"^\s*-\s+(.+?)\s*(?:—|-)\s*checked\s+(\d{4}-\d{2}-\d{2})", line)
        if m:
            return m.group(1), m.group(2)
    return None, None


def extract_bikou(body: str) -> str:
    """## 備考 から誌面に載せる短い補足を 1 つだけ返す。"""
    section = strip_md(extract_section(body, "備考"))
    lines: list[str] = []
    for line in section.splitlines():
        text = re.sub(r"^\s*[-*]\s+", "", line).strip()
        if not text or text.startswith("<!--"):
            continue
        if re.search(r"\b(status|figure_type|experience_level|reader_level|title_reading)\b", text):
            continue
        if re.fullmatch(r"[（(]\s*.*?(なし|未記入|空).*?\s*[）)]", text):
            continue
        lines.append(text)
    if not lines:
        return ""
    text = " ".join(lines)
    parts = _split_into_sentences(text)
    text = parts[0] if parts else text
    return text[:96].rstrip() + ("…" if len(text) > 96 else "")


# ─── HTML 部品 ────────────────────────────────────────

BOOK_ICON_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>'
CODE_ICON_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>'
PIN_ICON_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>'
USER_ICON_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>'
LEVEL_ICON_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="15" width="4" height="6"/><rect x="10" y="10" width="4" height="11"/><rect x="17" y="5" width="4" height="16"/></svg>'
PONCHI_ICON_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/><path d="M9 12l-2 3m8-3l2 3"/></svg>'


def _ponchi_final_asset(entry_id: str) -> tuple[Path, str] | None:
    """final ディレクトリで .webp を優先し、無ければ .png を返す。"""
    for ext in ("webp", "png"):
        p = PONCHI_FINAL_DIR / f"{entry_id}.{ext}"
        if p.exists():
            return p, f"../../../assets/ponchi/final/{entry_id}.{ext}"
    return None


def load_ponchi_asset(entry_id: str) -> tuple[str, bool]:
    """final WebP/PNG -> draft SVG -> placeholder の順でポンチ絵 HTML を返す。"""
    final = _ponchi_final_asset(entry_id)
    if final is not None:
        _, rel = final
        return f'<img src="{rel}" alt="" loading="lazy">', True

    svg_path = PONCHI_SVG_DIR / f"{entry_id}.svg"
    if not svg_path.exists():
        return PONCHI_ICON_SVG, False
    try:
        content = svg_path.read_text(encoding="utf-8")
    except Exception:
        return PONCHI_ICON_SVG, False
    # <?xml ...?> 宣言があれば剥がす（HTML 内に埋めるため）
    content = re.sub(r"^<\?xml[^?]*\?>\s*", "", content)
    return content, True

# 6 視点アイコン
SEEPOINT_ICONS = [
    '<svg class="seepoint-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2" fill="currentColor"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/></svg>',
    '<svg class="seepoint-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>',
    '<svg class="seepoint-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
    '<svg class="seepoint-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6"/><path d="M10 22h4"/><path d="M12 2a7 7 0 0 0-7 7c0 2.4 1.2 4.5 3 5.7V17a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1v-2.3c1.8-1.2 3-3.3 3-5.7a7 7 0 0 0-7-7z"/></svg>',
    '<svg class="seepoint-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M7 20h10"/><path d="M10 20c5.5-2.5.8-6.4 3-10"/><path d="M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5.4-4.8-.3-1.2-.6-2.3-1.9-3-4.2 2.8-.5 4.4 0 5.5.8z"/><path d="M14.1 6a7 7 0 0 0-1.1 4c1.9-.1 3.3-.6 4.3-1.4 1-1 1.6-2.3 1.7-4.6-2.7.1-4 1-4.9 2z"/></svg>',
    '<svg class="seepoint-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h8"/><polyline points="14 2 14 8 20 8"/><circle cx="18" cy="17" r="3"/><line x1="20.5" y1="19.5" x2="23" y2="22"/></svg>',
]

SEEPOINT_LABELS = ["役割", "うれしさ", "注意点", "どこで役立つか", "はじめに", "深掘り先"]
SEEPOINT_KEYS = ["1. 役割", "2. うれしさ", "3. 注意点", "4. どこで役立つか", "5. はじめに", "6. 深掘り先"]

# フロー用ジェネリックアイコン（iter 順に差し替え前提）
FLOW_ICONS = [
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="8" y1="13" x2="16" y2="13"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>',
]


def count_chars(text: str) -> int:
    """空白・HTML コメント・Markdown 装飾を除いた実文字数。validate_entry.py と同じ流儀。"""
    if not text:
        return 0
    t = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    t = re.sub(r"\*\*([^*]+)\*\*", r"\1", t)
    t = re.sub(r"`([^`]+)`", r"\1", t)
    t = re.sub(r"\s+", "", t)
    return len(t)


# v2_rules_summary §2-3 / §2-4 の字数レンジ（許容）
CHAR_RANGES: dict[str, tuple[int, int]] = {
    "tagline": (25, 45),
    "何をしてくれるか": (60, 200),
    "どこで出会うか": (60, 200),
    "見どころ1-5": (15, 40),
    "見どころ6": (15, 50),
    "会話での使い方例": (25, 50),  # 2026-04-26 追加: 左ページ末尾の独立スロット
}


def grade_chars(count: int, lower: int, upper: int) -> tuple[str, str]:
    """(状態記号, CSS クラス名) を返す。✓ / ↓少 / ↑多。"""
    if count == 0:
        return "—", "char-empty"
    if count < lower:
        return f"↓{lower - count}", "char-low"
    if count > upper:
        return f"↑{count - upper}", "char-high"
    return "✓", "char-ok"


def render_char_meta(tagline: str, nani: str, dokode: str, seepoints: list[str], kaiwa: str = "") -> str:
    """preview-meta バー下に出す字数チェック行。範囲超過は赤、不足はオレンジ、OK は緑。"""
    items: list[str] = []

    def cell(label: str, count: int, lower: int, upper: int) -> str:
        mark, klass = grade_chars(count, lower, upper)
        return (
            f'<span class="char-cell {klass}" title="許容 {lower}〜{upper} 字">'
            f'{escape(label)} <b>{count}</b><span class="lim">/{lower}-{upper}</span> {mark}'
            f'</span>'
        )

    items.append(cell("tagline", count_chars(tagline), *CHAR_RANGES["tagline"]))
    items.append(cell("何を", count_chars(nani), *CHAR_RANGES["何をしてくれるか"]))
    items.append(cell("どこで", count_chars(dokode), *CHAR_RANGES["どこで出会うか"]))
    items.append(cell("会話例", count_chars(kaiwa), *CHAR_RANGES["会話での使い方例"]))

    for i, sp in enumerate(seepoints, start=1):
        rng = CHAR_RANGES["見どころ6"] if i == 6 else CHAR_RANGES["見どころ1-5"]
        # 「（未記入）」は字数 0 と同等扱い
        text = "" if sp == "（未記入）" else sp
        items.append(cell(f"見{i}", count_chars(text), *rng))

    return f'<div class="char-meta">{"".join(items)}</div>'


def _scalar(v) -> str:
    """frontmatter 値を str に正規化。空 list（スケルトン未記入の experience_level: 等）は空文字。"""
    if v is None or v == [] or v == "":
        return ""
    if isinstance(v, list):
        return ", ".join(str(x) for x in v)
    return str(v)


def _reader_level_max(fm) -> int:
    """reader_level の上限レベル（数字）を返す。未記入は 0。
    上限で見るのは「6 を含むなら刊行スコープ外シェルフ」と判定するため
    （docs/level_policy.md §2-6）。"""
    nums = [int(x) for x in re.findall(r"\d", _scalar(fm.get("reader_level")))]
    return max(nums) if nums else 0


def _level_palette(lvl: str) -> tuple[str, str]:
    """reader_level（'2' / '2-3' / '1-2' / '4-5' 等）の上限レベル（難しさの天井）を取り、
    A-5 凡例と同じ色帯を返す。戻り値 = (背景色, 文字色)。
    上限基準にするのは、難易度の高いエントリ（専門寄り）を誌面で目立たせるため。"""
    nums = [int(x) for x in re.findall(r"\d", str(lvl))]
    n = max(nums) if nums else 0
    bands = {
        1: ("#F5F9FE", "#123E82"),
        2: ("#EAF1FB", "#123E82"),
        3: ("#DEE9F8", "#123E82"),
        4: ("#C6D9F2", "#123E82"),
        5: ("#A9C5EB", "#0F2E5C"),
        6: ("#8AB0E3", "#FFFFFF"),
    }
    return bands.get(n, ("", ""))


# ─── 難易度＝勲章バッジ（Lv1 若葉マーク＋星1 / Lv2-6 丸メダル）────────────
# 星数＝レベル、素材 銅(2-3)/銀(4)/金(5-6)、リボン色で階級差。range は上限で判定。
_MEDAL_TIERS = {
    "bronze": {"hi": "#F1C492", "mid": "#C77B3B", "lo": "#7A431C", "shi": "#9A5A28", "slo": "#542C12"},
    "silver": {"hi": "#F6F9FC", "mid": "#AAB3BF", "lo": "#69727E", "shi": "#8A94A0", "slo": "#4E565F"},
    "gold":   {"hi": "#FCEBAE", "mid": "#E2BB42", "lo": "#946E10", "shi": "#BE951F", "slo": "#6E5108"},
}
_MEDAL_RIBBON = {
    1: ("#5BB06A", "#2E7D40"), 2: ("#5BB06A", "#2E7D40"), 3: ("#4E9BD6", "#225E96"),
    4: ("#5566B8", "#2C3A86"), 5: ("#9A5FB0", "#5E2E78"), 6: ("#C8505E", "#7E2330"),
}


def _medal_tier(lv: int) -> dict:
    if lv <= 3:
        return _MEDAL_TIERS["bronze"]
    if lv == 4:
        return _MEDAL_TIERS["silver"]
    return _MEDAL_TIERS["gold"]


def _star_d(cx: float, cy: float, r: float) -> str:
    pts = []
    for i in range(10):
        rr = r if i % 2 == 0 else r * 0.4
        a = math.pi * 2 * i / 10 - math.pi / 2
        pts.append(("M" if i == 0 else "L") + f"{cx + rr * math.cos(a):.2f} {cy + rr * math.sin(a):.2f}")
    return " ".join(pts) + " Z"


def _star_positions(n: int, R: float) -> list[tuple[float, float]]:
    if n <= 1:
        return [(0.0, 0.0)]
    if n == 2:
        return [(-R, 0), (R, 0)]
    if n == 3:
        return [(0, -R), (-R * 0.87, R * 0.5), (R * 0.87, R * 0.5)]
    if n == 4:
        return [(-R * 0.72, -R * 0.72), (R * 0.72, -R * 0.72), (-R * 0.72, R * 0.72), (R * 0.72, R * 0.72)]
    out = []
    for i in range(n):
        a = -math.pi / 2 + math.pi * 2 * i / n
        out.append((R * math.cos(a), R * math.sin(a)))
    return out


def _medal_beads(cx: float, cy: float, R: float, n: int, fill: str) -> str:
    s = ""
    for i in range(n):
        a = math.pi * 2 * i / n
        s += f'<circle cx="{cx + R * math.cos(a):.2f}" cy="{cy + R * math.sin(a):.2f}" r="1.5" fill="{fill}"/>'
    return s


def medal_svg(lv: int, w: int = 38, h: int = 41, cls: str = "level-medal") -> str:
    """難易度勲章 SVG。lv は 1〜6（range は呼び出し側で上限に丸める）。"""
    lv = max(1, min(6, lv))
    if lv == 1:
        outer = "M32 15 C28 27 25 35 22 46 C27 66 39 80 48 90 C57 80 69 66 74 46 C71 35 68 27 64 15 C58 24 53 27 48 31 C43 27 38 24 32 15 Z"
        left = "M48 31 C43 27 38 24 32 15 C28 27 25 35 22 46 C27 66 39 80 48 90 Z"
        return (
            f'<svg class="{cls}" width="{w}" height="{h}" viewBox="0 0 96 104" role="img" aria-label="読者レベル1 入門">'
            '<defs>'
            '<linearGradient id="wkY" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFD93A"/><stop offset="1" stop-color="#E0A400"/></linearGradient>'
            '<linearGradient id="wkG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#46BE63"/><stop offset="1" stop-color="#1C7B3C"/></linearGradient>'
            '<filter id="wkS" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="1.5" stdDeviation="1.5" flood-color="#1A2A44" flood-opacity="0.22"/></filter>'
            '</defs>'
            '<g filter="url(#wkS)" transform="translate(48 50) scale(0.8) translate(-48 -50)">'
            f'<path d="{outer}" fill="url(#wkY)"/>'
            f'<path d="{left}" fill="url(#wkG)"/>'
            f'<path d="{outer}" fill="none" stroke="#B8860B" stroke-width="2.2" stroke-linejoin="round"/>'
            f'<path d="{_star_d(48, 58, 8)}" fill="#FFFFFF" stroke="#7A5A12" stroke-width="0.6"/>'
            '</g></svg>'
        )
    t = _medal_tier(lv)
    rib = _MEDAL_RIBBON[lv]
    R = {2: 9, 3: 9.5, 4: 10, 5: 10.6, 6: 11}[lv]
    sz = {2: 6.6, 3: 6.0, 4: 5.3, 5: 4.8, 6: 4.4}[lv]
    s = f'<svg class="{cls}" width="{w}" height="{h}" viewBox="0 0 96 104" role="img" aria-label="読者レベル{lv}">'
    s += (
        '<defs>'
        f'<radialGradient id="disc{lv}" cx="38%" cy="30%" r="78%"><stop offset="0" stop-color="{t["hi"]}"/><stop offset="55%" stop-color="{t["mid"]}"/><stop offset="100%" stop-color="{t["lo"]}"/></radialGradient>'
        f'<linearGradient id="mstar{lv}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{t["shi"]}"/><stop offset="1" stop-color="{t["slo"]}"/></linearGradient>'
        f'<linearGradient id="rib{lv}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{rib[0]}"/><stop offset="1" stop-color="{rib[1]}"/></linearGradient>'
        f'<filter id="sh{lv}" x="-35%" y="-35%" width="170%" height="170%"><feDropShadow dx="0" dy="1.6" stdDeviation="1.7" flood-color="#1A2A44" flood-opacity="0.30"/></filter>'
        '</defs>'
    )
    s += f'<path d="M40 8 L56 8 L52 30 L48 26 L44 30 Z" fill="url(#rib{lv})"/>'
    s += '<line x1="48" y1="9" x2="48" y2="27" stroke="#00000055" stroke-width="0.7"/>'
    s += f'<rect x="38" y="18" width="20" height="6" rx="3" fill="url(#disc{lv})" stroke="{t["lo"]}" stroke-width="0.8"/>'
    s += f'<g filter="url(#sh{lv})"><circle cx="48" cy="48" r="22" fill="{t["lo"]}"/></g>'
    s += _medal_beads(48, 48, 22, 36, t["hi"])
    s += f'<circle cx="48" cy="48" r="19.5" fill="{t["lo"]}"/>'
    s += f'<circle cx="48" cy="48" r="18" fill="url(#disc{lv})"/>'
    s += '<path d="M34 41 A 18 18 0 0 1 59 33" fill="none" stroke="#ffffff" stroke-width="1.5" opacity="0.4" stroke-linecap="round"/>'
    for dx, dy in _star_positions(lv, R):
        x, y = 48 + dx, 48 + dy
        s += f'<path d="{_star_d(x, y, sz)}" fill="url(#mstar{lv})" stroke="{t["slo"]}" stroke-width="0.5"/>'
        s += f'<path d="{_star_d(x, y - sz * 0.18, sz * 0.5)}" fill="#ffffff" opacity="0.28"/>'
    s += '</svg>'
    return s


def render_level_badge(fm: dict) -> str:
    """上チロム右に出す難易度勲章バッジ。reader_level の上限レベルで勲章を選ぶ。"""
    lvl = _scalar(fm.get("reader_level"))
    if not lvl:
        return ""
    nums = [int(x) for x in re.findall(r"\d", str(lvl))]
    if not nums:
        return ""
    return medal_svg(max(nums))


# ─── 体験区分＝関与バー（電波強度方式）────────────────────────────
# hands_on=3本 / partial=2本 / research_only=1本。難易度の勲章とは別系統（青）。
_EXP_BARS = {"hands_on": 3, "partial": 2, "research_only": 1}


def exp_bars_svg(exp_raw: str, w: int = 18, h: int = 16, cls: str = "exp-bars") -> str:
    """体験区分の関与バー SVG。未知/未記入は空文字。"""
    n = _EXP_BARS.get((exp_raw or "").strip(), 0)
    if n == 0:
        return ""
    blue = "#2F7BE6"
    hs = [14, 22, 30]
    xs = [10, 22, 34]
    s = f'<svg class="{cls}" width="{w}" height="{h}" viewBox="0 0 48 44" role="img" aria-label="体験区分 {escape(exp_raw)}">'
    for i in range(3):
        fill = blue if i < n else "#FFFFFF"
        s += f'<rect x="{xs[i]}" y="{38 - hs[i]}" width="9" height="{hs[i]}" rx="2.5" fill="{fill}" stroke="{blue}" stroke-width="2"/>'
    s += "</svg>"
    return s


def render_tagline_tags(fm: dict) -> str:
    exp_raw = _scalar(fm.get("experience_level"))
    exp = EXPERIENCE_LABELS.get(exp_raw, exp_raw) or "（未記入）"
    lvl = _scalar(fm.get("reader_level")) or "（未記入）"
    bg, fg = _level_palette(lvl)
    # 難易度（reader_level の下限）で凡例と同じ色帯に塗る。未記入は既定スタイル。
    lvl_style = f' style="background:{bg};color:{fg};border-color:{bg};"' if bg else ""
    exp_icon = exp_bars_svg(exp_raw) or USER_ICON_SVG  # 体験区分は関与バー（電波方式）
    return f'''
      <div class="tag-row">
        <span class="tag-chip">{exp_icon}体験区分：{escape(exp)}</span>
        <span class="tag-chip"{lvl_style}>{LEVEL_ICON_SVG}推奨読者レベル：Level {escape(lvl)}</span>
      </div>'''


def render_main_figure(fm: dict, entry_id: str) -> str:
    """figure_type ごとのプレースホルダ。最終 PNG があればそれを仮置きする。"""
    ft = fm.get("figure_type", "structure")
    final = _ponchi_final_asset(entry_id)
    if final is not None:
        _, rel = final
        return f'''
      <div class="section-heading"><span class="label">イメージ</span></div>
      <div class="figure figure--image figure--standalone">
        <img src="{rel}" alt="" loading="lazy">
      </div>'''
    label = {
        "before_after": "Before / After",
        "structure": "構造図",
        "comparison": "比較図",
        "workflow": "ワークフロー図",
        "timeline": "タイムライン",
    }.get(ft, "図")
    return f'''
      <div class="section-heading"><span class="label">{label}</span></div>
      <div class="figure" style="min-height:140px;padding:22px;text-align:center;color:var(--ink-2);font-size:14px;">
        図（figure_type: {escape(ft)}）は本番生成器（Astro + React primitive）で描画。<br>
        iter 22 時点ではプレースホルダ。
      </div>'''


def render_seepoint_cell(num: int, label: str, body: str) -> str:
    return f'''
        <div class="seepoint-cell">
          <span class="badge-num">{num}</span>
          {SEEPOINT_ICONS[num - 1]}
          <div class="seepoint-title">{escape(label)}</div>
          <p class="seepoint-body">{escape(body)}</p>
        </div>'''


def render_flow_row(steps: list[tuple[str, str]]) -> str:
    if not steps:
        return '<div class="flow-row"><div style="color:var(--ink-3);font-size:13px;">（フロー未記入）</div></div>'
    out: list[str] = ['<div class="flow-row">']
    for i, (label, _note) in enumerate(steps):
        icon = FLOW_ICONS[i % len(FLOW_ICONS)]
        if i > 0:
            out.append('<span class="flow-arrow">→</span>')
        out.append(f'''
        <div class="flow-step">
          {icon}
          <div class="flow-label">{escape(label)}</div>
        </div>''')
    out.append('</div>')
    return "".join(out)


def render_related_pills(terms: list[str]) -> str:
    pills = "".join(f'<span class="related-pill">{escape(t)}</span>' for t in terms[:5])
    return f'<div class="related-row">{pills}</div>'


def render_drawer(entries: list[dict], current_id: str) -> str:
    """全エントリを A〜J の accordion で並べる（typescript_spread.html と同じ構造）"""
    groups: dict[str, list[dict]] = {letter: [] for letter in "ABCDEFGHIJ"}
    for e in entries:
        letter = e["id"].split("-", 1)[0]
        if letter in groups:
            groups[letter].append(e)

    details: list[str] = []
    for letter, items in groups.items():
        if not items:
            continue
        meta = CHAPTER_META[letter]
        is_open = any(it["id"] == current_id for it in items)
        opened = " open" if is_open else ""
        rows = []
        for it in items:
            link_class = "is-active" if it["id"] == current_id else ""
            rows.append(
                f'<li><a class="entry-item is-available {link_class}" href="{escape(it["id"])}.html">'
                f'<span class="code">{escape(format_entry_id(it["id"]))}</span>{escape(it["title"])}</a></li>'
            )
        details.append(f'''
      <details{opened}>
        <summary><span class="letter">{letter}</span><span class="chapter-name">{escape(meta["label"])}</span><span class="count">{len(items)}</span></summary>
        <ul class="entry-list">
          {"".join(rows)}
        </ul>
      </details>''')

    return f'''
<div class="proto-nav" id="protoNav">
  <button class="proto-nav-toggle" type="button" aria-label="Open navigation" onclick="document.getElementById('protoNav').classList.toggle('open')">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
  </button>
  <div class="proto-nav-overlay" onclick="document.getElementById('protoNav').classList.remove('open')"></div>
  <aside class="proto-nav-drawer">
    <div class="drawer-head">
      <div>
        <div class="drawer-title">バイブコーディング図鑑</div>
        <div class="drawer-sub">PREVIEW · iter 22</div>
      </div>
      <button class="drawer-close" type="button" aria-label="Close" onclick="document.getElementById('protoNav').classList.remove('open')">×</button>
    </div>
    <div class="drawer-body">
      {"".join(details)}
    </div>
  </aside>
</div>'''


def render_prev_next_bar(prev: dict | None, next_: dict | None) -> str:
    prev_html = (
        f'<a class="nav-prev" href="{prev["id"]}.html">← {escape(format_entry_id(prev["id"]))} {escape(prev["title"])}</a>'
        if prev else '<span class="nav-prev disabled">← prev</span>'
    )
    next_html = (
        f'<a class="nav-next" href="{next_["id"]}.html">{escape(format_entry_id(next_["id"]))} {escape(next_["title"])} →</a>'
        if next_ else '<span class="nav-next disabled">next →</span>'
    )
    return f'''
<div class="preview-nav">
  {prev_html}
  <a class="nav-home" href="index.html">目次</a>
  {next_html}
</div>'''


# ─── ページテンプレート ──────────────────────────────

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — バイブコーディング図鑑 preview</title>
<link rel="stylesheet" href="{base_css}">
<link rel="stylesheet" href="{overlay_css}">
<link rel="stylesheet" href="{overlay_tight_css}">
<style>
body {{ margin: 0; padding: 12px 20px 40px; background: #E5EAF0; font-family: var(--font-jp); }}
/* 本文内の箇条書き・段落（preview のみ。本番は Astro primitive 側で制御） */
.body-text p {{ margin: 0 0 6px; }}
.body-text ul {{ margin: 4px 0 6px; padding-left: 20px; }}
.body-text li {{ margin: 2px 0; line-height: 1.7; }}
/* ponchi SVG が実データの時は円いっぱいに広げる（placeholder は 104px のまま） */
.ponchi-icon.ponchi-icon--real {{ padding: 0; overflow: hidden; }}
.ponchi-icon.ponchi-icon--real svg,
.ponchi-icon.ponchi-icon--real img {{ width: 100% !important; height: 100% !important; border-radius: 50%; object-fit: cover; display: block; }}
.preview-nav {{
  max-width: 1500px; margin: 0 auto 16px; padding: 10px 16px;
  background: #fff; border: 1px solid #d0d9e6; border-radius: 8px;
  display: flex; gap: 16px; align-items: center; justify-content: space-between;
  font-size: 13px; font-family: var(--font-jp);
}}
.preview-nav a {{ color: var(--ink-blue); text-decoration: none; font-weight: 500; }}
.preview-nav a:hover {{ text-decoration: underline; }}
.preview-nav .disabled {{ color: #aaa; }}
.preview-nav .nav-home {{ font-weight: 700; }}
.preview-meta {{
  max-width: 1500px; margin: 0 auto 12px; padding: 6px 16px; font-size: 11px; color: #6b7a8e;
  font-family: var(--font-jp);
}}

/* 字数チェック行（preview のみ。本番では出さない） */
.char-meta {{
  max-width: 1500px; margin: 0 auto 12px; padding: 6px 12px;
  font-size: 11px; font-family: var(--font-jp);
  background: #fff; border: 1px solid #d0d9e6; border-radius: 8px;
  display: flex; flex-wrap: wrap; gap: 8px;
}}
.char-cell {{
  display: inline-flex; gap: 4px; align-items: baseline;
  padding: 2px 8px; border-radius: 12px;
  background: #f3f6fb; color: #4a5568;
}}
.char-cell b {{ color: #1A1A1A; font-variant-numeric: tabular-nums; }}
.char-cell .lim {{ color: #99a3b5; font-size: 10px; }}
.char-ok {{ background: #e8f4ec; color: #2a6f3f; }}
.char-ok b {{ color: #1f5b34; }}
.char-low {{ background: #fff3e0; color: #8a5a14; }}
.char-low b {{ color: #6f4408; }}
.char-high {{ background: #fde4e4; color: #9e2a2a; }}
.char-high b {{ color: #7a1f1f; }}
.char-empty {{ background: #eef0f3; color: #99a3b5; }}

/* 主タイトル直下の和文サブタイトル（preview のみの inline 拡張） */
.title-hero-sub {{
  font-family: var(--font-jp);
  font-size: 26px;
  font-weight: 400;
  color: var(--ink-blue-900);
  letter-spacing: 0.04em;
  line-height: 1.2;
  margin: -14px 0 18px;
  opacity: 0.78;
}}

/* 開発フローのステップ幅を文字数に依存せず等幅にする
   （overlay.css の flex 等分が文字数で揺れるケース対策） */
.flow-row {{
  display: flex !important;
  align-items: stretch !important;
}}
.flow-row .flow-step {{
  flex: 1 1 0 !important;
  min-width: 0 !important;
  width: 0 !important;
}}
.flow-row .flow-step .flow-label {{
  word-break: keep-all;
  overflow-wrap: anywhere;
  white-space: normal;
}}
.flow-row .flow-arrow {{ flex: 0 0 auto !important; }}

/* 読者レベル（難易度）＝勲章バッジ：上チロム右、ページ番号の隣。 */
.page-chrome-top .chrome-right {{ display: flex; align-items: center; gap: 8px; }}
.level-medal {{ display: block; margin-top: -6px; margin-bottom: -8px; }}
/* 体験区分の関与バー（チップ内アイコン） */
.tag-chip .exp-bars {{ vertical-align: -3px; margin-right: 2px; }}

/* ─── PDF 出力（Cmd/Ctrl+P → PDF として保存）───
   2026-04-28 W 案: ポンチ絵スロットを iter 22 前の旧サイズに戻し、書籍判型 A 系 √2 に収める方向。
   @page は CSS 設計値 750×1061px の物理換算（≒199×281mm）。
   開発でしか使わない UI（ドロワー・preview メタ・字数バー・前後リンク）は印刷から除外する。 */
@page {{
  size: 199mm 281mm;
  margin: 0;
}}
@media print {{
  html, body {{
    background: #fff !important;
    padding: 0 !important;
    margin: 0 !important;
  }}
  .proto-nav,
  .preview-meta,
  .preview-nav,
  .char-meta {{ display: none !important; }}

  /* 見開き → 縦並びで各ページを 1 物理ページに割り付け */
  .spread {{
    display: block !important;
    margin: 0 !important;
    gap: 0 !important;
    box-shadow: none !important;
    max-width: none !important;
  }}
  .vbcd.page {{
    margin: 0 !important;
    box-shadow: none !important;
    page-break-after: always;
    page-break-inside: avoid;
    /* CSS 設計値 750×1061px（≒198.4×280.7mm）に合わせて 199×281mm 固定。
       はみ出したら overflow: hidden で切る（W 案の検証用に残す） */
    width: 199mm !important;
    height: 281mm !important;
    min-height: 281mm !important;
    max-height: 281mm !important;
    overflow: hidden !important;
  }}
  .vbcd.page:last-of-type {{ page-break-after: auto; }}
}}
</style>
</head>
<body>

{drawer}

<div class="preview-meta">
  id: <b>{entry_id}</b>（誌面表示: <b>{entry_code}</b>） · 物理ページ: <b>{page_left}–{page_right}</b>（pages={pages}） · category: {category} · figure_type: {figure_type} · status: {status} · evaluation_date: {evaluation_date}
</div>
{char_meta}
{nav_bar}

<div class="spread">

  <section class="vbcd page page--left-compact">
    <div class="page-chrome-top">
      <div class="chrome-left">
        {book_icon}<span class="chrome-label">{tilde_top}</span>
      </div>
      <div class="chrome-right">
        {level_badge}
        <span class="chrome-page">{page_left}</span>
      </div>
    </div>

    <div class="page-body">
      <h1 class="title-hero">{title_main}</h1>
      {title_sub_html}
      <div class="{tagline_class}">{tagline}</div>
      {tags}

      <div class="body-section">
        <span class="icon-circle">{code_icon}</span>
        <div class="body-content">
          <h3 class="body-heading">何をしてくれるか</h3>
          <div class="body-text">{nanishiteku}</div>
        </div>
      </div>

      <div class="body-section">
        <span class="icon-circle">{pin_icon}</span>
        <div class="body-content">
          <h3 class="body-heading">どこで出会うか</h3>
          <p class="body-text">{dokode_deau}</p>
        </div>
      </div>

      {main_figure}
      {ponchi_slot_html}
      <div class="section-heading"><span class="label">開発フローでの位置</span></div>
      {flow_row}
    </div>

    <div class="page-chrome-bottom">
      <div class="chrome-left-foot">{evaluation_month}<span class="sep">·</span>{status}</div>
      <div class="chrome-right-foot">{kaiwa_slot}</div>
    </div>
  </section>

  <section class="vbcd page page--right-tight">
    <div class="page-chrome-top">
      <div class="chrome-left">
        {book_icon}<span class="chrome-label">{title}の見方</span>
      </div>
      <span class="chrome-page">{page_right}</span>
    </div>

    <div class="page-body">
      <div class="section-heading"><span class="label">この用語の見どころ</span></div>
      <div class="seepoint-grid">
        {seepoint_cells}
      </div>

      <div class="bottom-row bottom-row--stack">
        <div>
          <div class="section-heading"><span class="label">非エンジニアのつまずき</span></div>
          <div class="list-block">
            <ul>
              {tsumazuki_items}
            </ul>
          </div>
        </div>
        <div>
          <div class="section-heading"><span class="label">私のコメント</span></div>
          <div class="comment-block">
            <ul>
              {comment_items}
            </ul>
          </div>
        </div>
      </div>

      <div class="section-heading"><span class="label">関連用語</span></div>
      {related_pills}
      {bikou_box}

      <div class="references-row">
        <span class="ref-label">参考</span>
        <a class="ref-url">{ref_url}</a>
        <span class="ref-date">checked {ref_date}</span>
      </div>
    </div>

    <div class="page-chrome-bottom">
      <div class="chrome-left-foot"><span class="entry-code">{entry_code}<span class="sep">·</span>{category}</span></div>
      <div class="chrome-inline">
        {book_icon}<span class="book-title">バイブコーディング図鑑</span>
      </div>
    </div>
  </section>

</div>
</body>
</html>
"""

INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>バイブコーディング図鑑 preview 目次</title>
<link rel="stylesheet" href="{base_css}">
<link rel="stylesheet" href="{overlay_css}">
<link rel="stylesheet" href="{overlay_tight_css}">
<style>
body {{ margin: 0; padding: 40px 20px; background: #f3f6fb; font-family: var(--font-jp); color: var(--ink); }}
main {{ max-width: 900px; margin: 0 auto; background: #fff; border-radius: 12px; padding: 40px; border: 1px solid #dfe6ef; }}
h1 {{ font-size: 32px; color: var(--ink-blue-900); margin: 0 0 6px; font-weight: 900; }}
.sub {{ color: var(--ink-2); font-size: 13px; margin-bottom: 28px; }}
h2 {{ font-size: 17px; color: var(--ink-blue-700); margin: 24px 0 8px; padding: 4px 0 4px 10px; border-left: 4px solid var(--ink-blue); }}
ul {{ list-style: none; padding: 0; margin: 0 0 14px; }}
li {{ margin: 4px 0; }}
a {{ color: var(--ink); text-decoration: none; padding: 4px 8px; border-radius: 6px; display: inline-block; }}
a:hover {{ background: var(--ink-blue-50); color: var(--ink-blue-900); }}
.code {{ display: inline-block; width: 52px; font-weight: 700; color: var(--ink-blue-700); font-family: var(--font-mono, monospace); font-size: 13px; }}
.count {{ color: var(--ink-3); font-size: 12px; margin-left: 6px; }}
.meta {{ background: #eef3fb; padding: 12px 16px; border-radius: 8px; margin-bottom: 20px; font-size: 12px; color: var(--ink-2); }}
</style>
</head>
<body>
<main>
  <h1>バイブコーディング図鑑 <span style="color:var(--ink-blue-700);font-size:20px;">preview</span></h1>
  <div class="sub">開発中に iter 22 レイアウトの反映を確認するためのプレビュー目次。本番は Astro + React（component_spec_v2.md §0）。</div>

  <nav style="display:flex;gap:8px;flex-wrap:wrap;margin:0 0 16px;">
    <a href="../../book/index.html" style="font-size:12px;color:white;background:var(--ink-blue);text-decoration:none;border-radius:6px;padding:5px 12px;font-weight:700;">📖 本として読む</a>
    <a href="../../front_section/index.html" style="font-size:12px;color:var(--ink-2);text-decoration:none;border:1px solid var(--rule);border-radius:6px;padding:5px 12px;">📕 前付け一覧</a>
    <a href="../../search/index.html" style="font-size:12px;color:var(--ink-2);text-decoration:none;border:1px solid var(--rule);border-radius:6px;padding:5px 12px;">🔍 検索</a>
    <a href="../../index.html" style="font-size:12px;color:var(--ink-2);text-decoration:none;border:1px solid var(--rule);border-radius:6px;padding:5px 12px;">管理トップ</a>
  </nav>

  <div class="meta">
    <b>集計:</b> 全 {total} エントリ（{active} active / {archived} archived）<br>
    <b>生成日:</b> scripts/preview_gen.py を最後に実行した時点<br>
    <b>更新方法:</b> markdown を書き換えたあと <code>python scripts/preview_gen.py</code>
  </div>

  {chapters}
</main>
</body>
</html>
"""


# ─── 本体 ─────────────────────────────────────────

def load_entries_from_csv() -> list[dict]:
    with CSV_PATH.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def load_md(path: Path) -> dict | None:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return None
    fm, body = parse_frontmatter(text)
    fm["_body"] = body
    return fm


def _resolve_entry_pages(csv_row: dict, fm: dict) -> int:
    """各エントリの物理ページ消費数を算定。CSV 列 > frontmatter > デフォルト の優先順。

    A 章まえがき・A-9 索引のように見開き 1（2 ページ）に収まらないエントリは、
    entries.csv の `pages` 列か markdown の frontmatter `pages:` に整数を入れることで上書きする。
    値は偶数を推奨（左ページ始まり維持のため）だが、奇数も受け付ける。
    """
    csv_pages_raw = (csv_row.get("pages") or "").strip()
    if csv_pages_raw.isdigit():
        return max(int(csv_pages_raw), 1)
    fm_pages_raw = str(fm.get("pages", "")).strip()
    if fm_pages_raw.isdigit():
        return max(int(fm_pages_raw), 1)
    return DEFAULT_ENTRY_PAGES


def make_entry_record(csv_row: dict) -> dict | None:
    """CSV 行 + md の frontmatter/本文を統合した dict"""
    path = csv_row.get("path", "").strip()
    if not path:
        return None
    md_path = ROOT / path
    if not md_path.exists():
        return None
    fm = load_md(md_path)
    if not fm:
        return None
    if fm.get("status") == "archived":
        return None
    return {
        "id": csv_row["new_id"],
        "title": csv_row["title"] or fm.get("title", ""),
        "category": csv_row.get("category", "") or fm.get("category", ""),
        "path": path,
        "fm": fm,
        "pages": _resolve_entry_pages(csv_row, fm),
    }


def render_page(entry: dict, prev: dict | None, next_: dict | None, drawer_html: str, page_left: int, page_right: int) -> str:
    fm = entry["fm"]
    body = fm["_body"]
    entry_id = entry["id"]
    entry_id_padded = format_entry_id(entry_id)
    letter = entry_id.split("-", 1)[0]
    chapter = CHAPTER_META.get(letter, {"label": "", "tilde": ""})

    # 主・副タイトルの解決:
    #   1. frontmatter の title_reading（iter 23 で正式採用）を最優先
    #   2. なければ title 内の `（...）` を分離する後方互換ロジック（split_title）
    title_reading = (fm.get("title_reading") or "").strip()
    if title_reading:
        title_main, title_sub = entry["title"], title_reading
    else:
        title_main, title_sub = split_title(entry["title"])

    tagline = strip_md(extract_section(body, "tagline")) or fm.get("tagline", "")
    tagline_class = "tagline-bar tagline-bar--dense" if len(tagline) > 55 else "tagline-bar"
    nanishiteku_raw = strip_md(extract_section(body, "何をしてくれるか"))
    dokode_deau_raw = strip_md(extract_section(body, "どこで出会うか"))
    nanishiteku_html = render_body_html(nanishiteku_raw) or "<p>（未記入）</p>"
    dokode_deau_html = render_body_html(dokode_deau_raw) or "<p>（未記入）</p>"

    # 2026-04-26 追加: 左ページ末尾の「会話での使い方例」スロット
    # 25-50 字（推奨 30-40）の 1 文。誌面では下チロム右に印字される
    kaiwa_raw = strip_md(extract_section(body, "会話での使い方例"))

    seepoints = [strip_md(extract_subsection(body, "この用語の見どころ", key)) or "（未記入）" for key in SEEPOINT_KEYS]
    seepoint_cells = "\n".join(render_seepoint_cell(i + 1, SEEPOINT_LABELS[i], seepoints[i]) for i in range(6))

    flow_steps = extract_flow_steps(body)
    flow_html = render_flow_row(flow_steps).replace('class="flow-row"', 'class="flow-row flow-row--compact"', 1)

    char_meta_html = render_char_meta(tagline, nanishiteku_raw, dokode_deau_raw, seepoints, kaiwa_raw)

    related = extract_related_terms(body, fm.get("related_terms", []) or [])
    related_html = render_related_pills(related)

    ponchi_title, ponchi_caption = extract_ponchi(body, entry["title"])
    ponchi_asset, ponchi_is_real = load_ponchi_asset(entry_id)

    tsumazuki_items = render_tsumazuki_items(extract_tsumazuki_bullets(body))
    comment_items = render_comment_items(extract_comment_items(body))

    ref_url, ref_date = extract_reference_url(body)
    bikou_raw = extract_bikou(body)
    bikou_box = (
        f'''
      <div class="section-heading section-heading--note"><span class="label">備考</span></div>
      <div class="note-box">
        <p>{escape(bikou_raw)}</p>
      </div>'''
        if bikou_raw else ""
    )

    title_sub_html = (
        f'<div class="title-hero-sub">{escape(title_sub)}</div>'
        if title_sub else ""
    )

    # 会話での使い方例: 本文があれば直接表示、なければプレースホルダ
    kaiwa_slot_html = (
        f'<span class="slot-kaiwa">{escape(kaiwa_raw)}</span>'
        if kaiwa_raw else
        '<span class="slot-placeholder">（会話での使い方例）</span>'
    )

    return PAGE_TEMPLATE.format(
        title=escape(entry["title"]),
        title_main=escape(title_main),
        title_sub_html=title_sub_html,
        kaiwa_slot=kaiwa_slot_html,
        entry_id=escape(entry_id),
        entry_code=escape(entry_id_padded),
        char_meta=char_meta_html,
        category=escape(entry["category"]),
        figure_type=escape(fm.get("figure_type", "")),
        status=escape(fm.get("status", "")),
        evaluation_date=escape(fm.get("evaluation_date", "")),
        evaluation_month=escape((fm.get("evaluation_date", "") or "")[:7].replace("-", ".")),
        tilde_top=escape(chapter["tilde"]),
        level_badge=render_level_badge(fm),
        base_css=BASE_CSS_REL,
        overlay_css=OVERLAY_CSS_REL,
        overlay_tight_css=OVERLAY_TIGHT_CSS_REL,
        book_icon=BOOK_ICON_SVG,
        code_icon=CODE_ICON_SVG,
        pin_icon=PIN_ICON_SVG,
        ponchi_slot_html=(
            '' if _ponchi_final_asset(entry_id) is not None
            else f'''
      <div class="ponchi-slot">
        <div class="ponchi-icon {"ponchi-icon--real" if ponchi_is_real else ""}">{ponchi_asset}</div>
        <div class="ponchi-caption">
          <div class="ponchi-title">{escape(ponchi_title)}</div>
          <p class="ponchi-hint">{escape(ponchi_caption)}</p>
          <span class="ponchi-todo">擬人化ポンチ絵 · 後日差し込み</span>
        </div>
      </div>'''
        ),
        page_left=f"{page_left:02d}",
        page_right=f"{page_right:02d}",
        pages=entry.get("pages", DEFAULT_ENTRY_PAGES),
        tagline=escape(tagline),
        tagline_class=tagline_class,
        tags=render_tagline_tags(fm),
        nanishiteku=nanishiteku_html,
        dokode_deau=dokode_deau_html,
        main_figure=render_main_figure(fm, entry_id),
        seepoint_cells=seepoint_cells,
        flow_row=flow_html,
        related_pills=related_html,
        bikou_box=bikou_box,
        ref_url=escape(ref_url or "（未記入）"),
        ref_date=escape(ref_date or "—"),
        tsumazuki_items=tsumazuki_items,
        comment_items=comment_items,
        drawer=drawer_html,
        nav_bar=render_prev_next_bar(prev, next_),
    )


def render_index(entries: list[dict], archived_count: int) -> str:
    groups: dict[str, list[dict]] = {letter: [] for letter in "ABCDEFGHIJ"}
    for e in entries:
        letter = e["id"].split("-", 1)[0]
        if letter in groups:
            groups[letter].append(e)

    chapter_blocks: list[str] = []
    for letter, items in groups.items():
        if not items:
            continue
        meta = CHAPTER_META[letter]
        rows = "\n".join(
            f'<li><a href="{escape(e["id"])}.html"><span class="code">{escape(format_entry_id(e["id"]))}</span>{escape(e["title"])}</a></li>'
            for e in items
        )
        chapter_blocks.append(
            f'<h2>{letter}. {escape(meta["label"])}<span class="count">（{len(items)} 件）</span></h2>\n<ul>{rows}</ul>'
        )

    return INDEX_TEMPLATE.format(
        total=len(entries) + archived_count,
        active=len(entries),
        archived=archived_count,
        chapters="\n".join(chapter_blocks),
        base_css=BASE_CSS_REL,
        overlay_css=OVERLAY_CSS_REL,
        overlay_tight_css=OVERLAY_TIGHT_CSS_REL,
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--open", action="store_true", help="生成後に index.html をブラウザで開く")
    args = ap.parse_args()

    csv_rows = load_entries_from_csv()
    entries: list[dict] = []
    archived_count = 0
    shelf_count = 0
    for row in csv_rows:
        rec = make_entry_record(row)
        if rec is None:
            if row.get("path"):
                archived_count += 1
            continue
        # reader_level 6 = 著者の自己学習シェルフ（刊行スコープ外）。
        # 原稿・CSV は残すが誌面には出さない（docs/level_policy.md §2-6）。
        if _reader_level_max(rec["fm"]) >= 6:
            shelf_count += 1
            continue
        entries.append(rec)

    if not entries:
        print("対象エントリなし", file=sys.stderr)
        return 2

    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    drawer_html = None  # 各ページの current_id が違うので毎回再生成

    cursor = START_PAGE
    for idx, entry in enumerate(entries):
        prev = entries[idx - 1] if idx > 0 else None
        next_ = entries[idx + 1] if idx + 1 < len(entries) else None
        drawer_html = render_drawer(entries, entry["id"])
        page_left = cursor
        page_right = cursor + 1
        html = render_page(entry, prev, next_, drawer_html, page_left=page_left, page_right=page_right)
        out_path = PREVIEW_DIR / f"{entry['id']}.html"
        out_path.write_text(html, encoding="utf-8")
        print(
            f"  OK  {out_path.relative_to(ROOT)}"
            f"  [{format_entry_id(entry['id'])}]  p.{page_left:02d}-{page_right:02d}"
            f"  pages={entry['pages']}"
        )
        cursor += entry["pages"]

    index_html = render_index(entries, archived_count)
    index_path = PREVIEW_DIR / "index.html"
    index_path.write_text(index_html, encoding="utf-8")
    print(f"  OK  {index_path.relative_to(ROOT)}")

    print(
        f"\n=== 生成 {len(entries)} エントリ + 目次 1、"
        f"archived {archived_count} 件 / 自己学習シェルフ(Lv6) {shelf_count} 件スキップ ==="
    )

    if args.open:
        webbrowser.open(index_path.as_uri())

    return 0


if __name__ == "__main__":
    sys.exit(main())
