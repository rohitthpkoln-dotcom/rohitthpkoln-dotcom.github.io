#!/usr/bin/env python3

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import shutil

import rebuild_posts

ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "posts"
TEMPLATE_INDEX = ROOT / "templates" / "post-index.html"
TEMPLATE_CONTENT = ROOT / "templates" / "post-content.md"


def slugify(value: str) -> str:
    return re.sub(r"-+", "-", re.sub(r"[^\w\s-]", "", value.lower()).strip().replace(" ", "-"))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a new notebook post.")
    parser.add_argument("title", help="The post title.")
    parser.add_argument("--slug", help="Optional custom folder slug.")
    parser.add_argument("--date", default=date.today().isoformat(), help="ISO date, e.g. 2026-05-07.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    slug = args.slug or slugify(args.title)
    target_dir = POSTS_DIR / slug

    if target_dir.exists():
        raise SystemExit(f"Post already exists: {target_dir}")

    target_dir.mkdir(parents=True)
    shutil.copyfile(TEMPLATE_INDEX, target_dir / "index.html")

    content = TEMPLATE_CONTENT.read_text(encoding="utf-8")
    content = content.replace("{{TITLE}}", args.title).replace("{{DATE}}", args.date)
    (target_dir / "content.md").write_text(content, encoding="utf-8")

    manifest = rebuild_posts.build_manifest()
    print(f"Created {target_dir}")
    print(f"Manifest now lists {len(manifest)} posts")


if __name__ == "__main__":
    main()
