#!/usr/bin/env python3
"""从 yoyo-html 学习路径里抽出配图清单，并检查缺图。

用法:
  python extract_shots.py path/to/journey.html
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ATTRS = ("data-yo-prompt", "data-yo-type", "data-yo-labels")


def attr(tag: str, name: str) -> str:
    m = re.search(rf'{name}="([^"]*)"', tag)
    return m.group(1) if m else ""


def main() -> int:
    if len(sys.argv) < 2:
        print("用法: python extract_shots.py path/to/journey.html", file=sys.stderr)
        return 2
    html_path = Path(sys.argv[1]).resolve()
    if not html_path.exists():
        print(f"找不到文件: {html_path}", file=sys.stderr)
        return 1
    text = html_path.read_text(encoding="utf-8")
    figures = re.findall(r"<figure\b[^>]*class=\"[^\"]*yo-fig[^\"]*\"[^>]*>.*?</figure>", text, re.S)
    if not figures:
        figures = re.findall(r"<figure\b[^>]*class='[^']*yo-fig[^']*'[^>]*>.*?</figure>", text, re.S)

    print(f"# shot list · {html_path.name}\n")
    missing = 0
    for i, fig in enumerate(figures, 1):
        prompt = attr(fig, "data-yo-prompt") or "(无 data-yo-prompt)"
        kind = attr(fig, "data-yo-type") or "?"
        labels = attr(fig, "data-yo-labels") or ""
        img = re.search(r'<img[^>]*src="([^"]+)"', fig)
        src = img.group(1) if img else ""
        slot = "yo-slot" in fig
        exists = False
        if src and not src.startswith(("http://", "https://", "data:")):
            exists = (html_path.parent / src).exists()
        status = "占位" if slot or not src else ("有图" if exists else "缺图")
        if status != "有图":
            missing += 1
        print(f"## {i:02d} · {kind} · {status}")
        print(f"- prompt: {prompt}")
        if labels:
            print(f"- labels: {labels}")
        print(f"- src: {src or '(无 img)'}")
        print()

    print(f"共 {len(figures)} 张插槽，其中 {missing} 张还没有图。")
    return 0 if missing == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
