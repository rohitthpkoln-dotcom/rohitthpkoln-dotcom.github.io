#!/usr/bin/env python3

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "posts"
OUTPUT_PATH = ROOT / "content" / "posts.json"
FRONTMATTER_PATTERN = re.compile(r"^---\s*\n(?P<meta>[\s\S]*?)\n---\s*\n?(?P<body>[\s\S]*)$")


def parse_frontmatter(text: str) -> tuple[dict[str, str | list[str]], str]:
    match = FRONTMATTER_PATTERN.match(text)
    if not match:
        return {}, text

    metadata: dict[str, str | list[str]] = {}
    for line in match.group("meta").splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        cleaned = value.strip().strip('"')
        if key.strip() == "tags":
            metadata["tags"] = [item.strip() for item in cleaned.split(",") if item.strip()]
        else:
            metadata[key.strip()] = cleaned

    return metadata, match.group("body")


def infer_excerpt(body: str) -> str:
    paragraphs = [chunk.strip() for chunk in body.split("\n\n") if chunk.strip()]
    if not paragraphs:
        return "Technical note."

    paragraph = paragraphs[0]
    paragraph = re.sub(r"`([^`]+)`", r"\1", paragraph)
    paragraph = re.sub(r"[*_>#-]", "", paragraph)
    paragraph = re.sub(r"\s+", " ", paragraph).strip()
    return paragraph[:180].rstrip() + ("..." if len(paragraph) > 180 else "")


def build_manifest() -> list[dict[str, object]]:
    posts: list[dict[str, object]] = []

    for content_file in sorted(POSTS_DIR.glob("*/content.md")):
        metadata, body = parse_frontmatter(content_file.read_text(encoding="utf-8"))
        slug = content_file.parent.name
        post = {
            "title": metadata.get("title", slug.replace("-", " ").title()),
            "date": metadata.get("date", ""),
            "excerpt": metadata.get("excerpt", infer_excerpt(body)),
            "tags": metadata.get("tags", []),
            "href": f"./posts/{slug}/",
            "slug": slug,
        }
        posts.append(post)

    posts.sort(key=lambda item: str(item["date"]), reverse=True)
    OUTPUT_PATH.write_text(json.dumps(posts, indent=2), encoding="utf-8")
    return posts


if __name__ == "__main__":
    manifest = build_manifest()
    print(f"Wrote {len(manifest)} posts to {OUTPUT_PATH}")
