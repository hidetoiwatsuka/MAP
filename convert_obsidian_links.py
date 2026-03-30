#!/usr/bin/env python3
"""
convert_obsidian_links.py
=========================
Obsidian の [[wikilinks]] / ![[embeds]] を Git/GitHub で動作する
標準 Markdown リンクに一括変換するスクリプト。

使い方
------
    # このスクリプトをvaultのルートに置いて実行するだけ
    python3 convert_obsidian_links.py

変換ルール
----------
  [[Note Name]]       →  [Note Name](relative/path/Note%20Name.md)
  [[Note|表示名]]     →  [表示名](relative/path/Note.md)
  ![[Note Name]]      →  ![Note Name](relative/path/Note%20Name.md)
  ![[image.png]]      →  ![image.png](relative/path/image.png)

  [[File.pdf]]        →  変換しない（そのまま）
  ![[File.pdf]]       →  変換しない（そのまま）

特記事項
--------
- PDF リンクは変換せずそのまま残す（ローカルの Obsidian で動作、
  GitHub では表示されないことを許容する設計）
- macOS の HFS+ は NFD でファイル名を保存するが、Obsidian は NFC で
  リンクを書くため、Unicode NFC 正規化でマッチングを行う
- リンク先が存在しない .md ノートは 00_inbox/ にプレースホルダーを
  自動生成してリンクを解決する
- 解決できなかったリンクはそのまま [[]] で残る

対応 Python バージョン
----------------------
Python 3.10 以上（Path | None の型ヒント使用）
"""

import os
import re
import unicodedata
from urllib.parse import quote
from pathlib import Path

# ── パス設定（このスクリプトをvaultルートに置いて使う） ──────────
VAULT_ROOT  = Path(__file__).parent.resolve()
INBOX       = VAULT_ROOT / "00_inbox"
ATTACHMENTS = INBOX / "01_Assets" / "Attachments"

# ── 変換しないファイル拡張子 ──────────────────────────────────────
PDF_EXTENSIONS = {".pdf"}

# ── URL で安全にエンコードしない文字（ファイル名に頻出するもの） ──
# カンマ、括弧、アンパサンドなど一般的な記号はそのまま残す
URL_SAFE_CHARS = ",()&+'"

# ── 既知のファイル拡張子（これ以外は .md として扱う） ────────────
KNOWN_EXTENSIONS = {".pdf", ".png", ".jpg", ".jpeg", ".gif",
                    ".svg", ".webp", ".md", ".txt", ".canvas"}


# ── ユーティリティ ────────────────────────────────────────────────
def nfc(s: str) -> str:
    """Unicode NFC 正規化（macOS NFDファイル名対策）"""
    return unicodedata.normalize("NFC", s)


def has_file_extension(name: str) -> bool:
    """既知の拡張子を持つかどうか判定（ノート名中の . は無視）"""
    return Path(nfc(name)).suffix.lower() in KNOWN_EXTENSIONS


def is_pdf(name: str) -> bool:
    return Path(nfc(name)).suffix.lower() in PDF_EXTENSIONS


def make_relative_url(source_file: Path, target_file: Path) -> str:
    """source_file から target_file への相対URLパスを返す（URLエンコード済み）"""
    rel = os.path.relpath(target_file, source_file.parent)
    parts = Path(rel).parts
    return "/".join(quote(nfc(p), safe=URL_SAFE_CHARS) for p in parts)


# ── ファイルインデックス ──────────────────────────────────────────
def build_index(root: Path) -> dict[str, Path]:
    """ファイル名(NFC) → 絶対パス のインデックスを構築する"""
    index: dict[str, Path] = {}
    for path in sorted(root.rglob("*")):
        if path.is_file() and not path.name.startswith("."):
            key = nfc(path.name)
            if key not in index:
                index[key] = path
    return index


def resolve_target(link_name: str, index: dict[str, Path]) -> Path | None:
    """Obsidianリンク名からファイルパスを解決する"""
    name = nfc(link_name)
    if has_file_extension(name):
        result = index.get(name)
        if result:
            return result
        if not name.endswith(".md"):
            return index.get(name + ".md")
        return None
    return index.get(name + ".md")


# ── 未解決リンクの収集 ───────────────────────────────────────────
WIKILINK_RE = re.compile(r"(!?)\[\[([^\[\]]+?)\]\]")


def collect_unresolved(index: dict[str, Path]) -> tuple[set, set]:
    """vault全体から解決できないリンクを収集する（PDFは除く）"""
    unresolved_md: set[str]  = set()
    unresolved_pdf: set[str] = set()
    for md_path in VAULT_ROOT.rglob("*.md"):
        text = md_path.read_text(encoding="utf-8")
        for _, inner in WIKILINK_RE.findall(text):
            note_name = inner.split("|")[0].strip()
            if is_pdf(note_name):
                continue  # PDFは変換しないのでスキップ
            if resolve_target(note_name, index) is None:
                suffix = Path(nfc(note_name)).suffix.lower()
                if suffix in PDF_EXTENSIONS:
                    unresolved_pdf.add(note_name)
                elif not suffix:
                    unresolved_md.add(note_name)
    return unresolved_md, unresolved_pdf


# ── PDF の fuzzy マッチ ──────────────────────────────────────────
def fuzzy_pdf_match(pdf_name: str, all_pdfs: list[Path]) -> Path | None:
    """NFD/NFC の差異を吸収してPDFを検索する"""
    target = nfc(pdf_name)
    for p in all_pdfs:
        if nfc(p.name) == target:
            return p
    return None


# ── プレースホルダー MD の生成 ───────────────────────────────────
def create_placeholder(note_name: str) -> Path:
    """00_inbox/ にプレースホルダーノートを作成して返す"""
    safe_name = note_name.replace("/", "-").replace("\\", "-")
    path = INBOX / f"{safe_name}.md"
    if not path.exists():
        path.write_text(
            f"# {note_name}\n\n"
            f"> [!note] This note is a placeholder. Content to be added.\n",
            encoding="utf-8",
        )
    return path


# ── 1ファイルの変換 ──────────────────────────────────────────────
def convert_file(md_path: Path, index: dict[str, Path]) -> tuple[str, int, int]:
    """ファイルを読み込み [[links]] を変換して返す"""
    text = md_path.read_text(encoding="utf-8")
    ok = 0
    unresolved = 0

    def replace(m: re.Match) -> str:
        nonlocal ok, unresolved
        bang  = m.group(1)   # "!" or ""
        inner = m.group(2)

        if "|" in inner:
            note_name, display = inner.split("|", 1)
        else:
            note_name = inner
            display = note_name if not has_file_extension(nfc(note_name)) \
                      else Path(nfc(note_name)).name

        # PDF はそのまま残す
        if is_pdf(note_name.strip()):
            return m.group(0)

        target = resolve_target(note_name.strip(), index)
        if target is None:
            unresolved += 1
            return m.group(0)

        url = make_relative_url(md_path, target)
        ok += 1

        # ![[]] は画像・ノートともに ! を維持
        if bang == "!":
            return f"![{display}]({url})"
        return f"[{display}]({url})"

    return WIKILINK_RE.sub(replace, text), ok, unresolved


# ── メイン ───────────────────────────────────────────────────────
def main() -> None:
    print(f"Vault: {VAULT_ROOT}\n")

    # Step 1: インデックス構築
    index = build_index(VAULT_ROOT)
    print(f"Indexed {len(index)} files.\n")

    # Step 2: 未解決リンクの収集（PDF除く）
    unresolved_md, _ = collect_unresolved(index)
    print(f"未解決 MD ノート: {len(unresolved_md)} 件\n")

    # Step 3: 未作成ノートにプレースホルダーを生成
    placeholder_created = 0
    for note_name in sorted(unresolved_md):
        p = create_placeholder(note_name)
        key = nfc(p.name)
        if key not in index:
            index[key] = p
            placeholder_created += 1
            print(f"  Created placeholder: {p.name}")
    if placeholder_created:
        print(f"  → {placeholder_created} 件のプレースホルダーを生成\n")

    # Step 4: 全 .md を変換
    total_ok = 0
    total_unresolved = 0
    changed_files = 0

    for md_path in sorted(VAULT_ROOT.rglob("*.md")):
        original = md_path.read_text(encoding="utf-8")
        if "[[" not in original:
            continue
        new_text, ok, unresolved = convert_file(md_path, index)
        if new_text != original:
            md_path.write_text(new_text, encoding="utf-8")
            changed_files += 1
            print(f"  ✓ {md_path.relative_to(VAULT_ROOT)}"
                  f"  ({ok} converted, {unresolved} unresolved)")
        total_ok += ok
        total_unresolved += unresolved

    print(f"\n{'=' * 60}")
    print(f"Changed files    : {changed_files}")
    print(f"Links converted  : {total_ok}")
    print(f"Unresolved links : {total_unresolved}")
    if total_unresolved == 0:
        print("✅ 全 [[リンク]] の変換が完了しました（PDFは除く）。")


if __name__ == "__main__":
    main()
