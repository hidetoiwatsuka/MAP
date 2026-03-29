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
  [[Note Name]]           →  [Note Name](relative/path/Note%20Name.md)
  [[File.pdf]]            →  [File.pdf](relative/path/File.pdf)
  [[Note|表示名]]         →  [表示名](relative/path/Note.md)
  ![[image.png]]          →  ![image.png](relative/path/image.png)
  ![[Note Name]]          →  [Note Name](relative/path/Note%20Name.md)

特記事項
--------
- macOS の HFS+ は NFD でファイル名を保存するが、Obsidian は NFC で
  リンクを書くため、Unicode NFC 正規化でマッチングを行う。
- リンク先が存在しない .md ノートは 00_inbox/ にプレースホルダーを
  自動生成してリンクを解決する。
- リンク先が存在しない PDF は 00_inbox/01_Assets/Attachments/ を
  NFC 正規化で再検索して解決する。
- 解決できなかったリンクはそのまま [[]] で残る。

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

# ── 既知のファイル拡張子（これ以外は .md として扱う） ────────────
KNOWN_EXTENSIONS = {".pdf", ".png", ".jpg", ".jpeg", ".gif",
                    ".svg", ".webp", ".md", ".txt"}


# ── ユーティリティ ────────────────────────────────────────────────
def nfc(s: str) -> str:
    """Unicode NFC 正規化（macOS NFDファイル名対策）"""
    return unicodedata.normalize("NFC", s)


def has_file_extension(name: str) -> bool:
    """既知の拡張子を持つかどうか判定（ノート名中の . は無視）"""
    return Path(nfc(name)).suffix.lower() in KNOWN_EXTENSIONS


def make_relative_url(source_file: Path, target_file: Path) -> str:
    """source_file から target_file への相対URLパスを返す（URLエンコード済み）"""
    rel = os.path.relpath(target_file, source_file.parent)
    parts = Path(rel).parts
    return "/".join(quote(nfc(p), safe="") for p in parts)


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
    """vault全体から解決できないリンクを収集する"""
    unresolved_md: set[str]  = set()
    unresolved_pdf: set[str] = set()
    for md_path in VAULT_ROOT.rglob("*.md"):
        text = md_path.read_text(encoding="utf-8")
        for _, inner in WIKILINK_RE.findall(text):
            note_name = inner.split("|")[0].strip()
            if resolve_target(note_name, index) is None:
                suffix = Path(nfc(note_name)).suffix.lower()
                if suffix == ".pdf":
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
    # ファイル名に使えない文字 (/ \) を - に置換
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

        target = resolve_target(note_name.strip(), index)
        if target is None:
            unresolved += 1
            return m.group(0)

        url = make_relative_url(md_path, target)
        ok += 1

        if bang == "!":
            suffix = target.suffix.lower()
            if suffix in (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".pdf"):
                return f"![{display}]({url})"
            # Markdown embed → plain link (GitHub非対応のため)
            return f"[{display}]({url})"
        return f"[{display}]({url})"

    return WIKILINK_RE.sub(replace, text), ok, unresolved


# ── メイン ───────────────────────────────────────────────────────
def main() -> None:
    print(f"Vault: {VAULT_ROOT}\n")

    # Step 1: インデックス構築
    index = build_index(VAULT_ROOT)
    print(f"Indexed {len(index)} files.\n")

    # Step 2: 未解決リンクの収集
    unresolved_md, unresolved_pdf = collect_unresolved(index)
    print(f"未解決 MD ノート : {len(unresolved_md)} 件")
    print(f"未解決 PDF リンク: {len(unresolved_pdf)} 件\n")

    # Step 3: PDF を Attachments から NFC マッチで解決
    if ATTACHMENTS.exists():
        all_pdfs = [p for p in ATTACHMENTS.rglob("*.pdf")
                    if not p.name.startswith(".")]
        pdf_resolved = 0
        for pdf_name in sorted(unresolved_pdf):
            match = fuzzy_pdf_match(pdf_name, all_pdfs)
            if match:
                key = nfc(match.name)
                if key not in index:
                    index[key] = match
                    pdf_resolved += 1
                    print(f"  PDF resolved : {pdf_name}")
            else:
                print(f"  PDF NOT FOUND: {pdf_name}")
        print(f"  → {pdf_resolved} 件の PDF をインデックスに追加\n")

    # Step 4: 未作成ノートにプレースホルダーを生成
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

    # Step 5: 全 .md を変換
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
        print("✅ 全 [[リンク]] の変換が完了しました。")


if __name__ == "__main__":
    main()
