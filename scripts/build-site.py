#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"

SECTIONS = [
    {"id": "inbox", "title": "Inbox", "dir": "00_Inbox", "description": "临时收集箱"},
    {"id": "notes", "title": "Notes", "dir": "10_Notes", "description": "长期笔记"},
    {"id": "projects", "title": "Projects", "dir": "20_Projects", "description": "项目资料"},
    {"id": "references", "title": "References", "dir": "30_References", "description": "文章、PDF、网页摘要"},
    {"id": "code", "title": "Code", "dir": "40_Code", "description": "技术笔记和代码片段"},
    {"id": "daily", "title": "Daily", "dir": "50_Daily", "description": "每日记录"},
    {"id": "templates", "title": "Templates", "dir": "templates", "description": "常用模板"},
]


def parse_front_matter(raw: str) -> tuple[dict[str, str], str]:
    if not raw.startswith("---"):
        return {}, raw

    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", raw, re.S)
    if not match:
        return {}, raw

    meta: dict[str, str] = {}
    for line in match.group(1).splitlines():
        item = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if item:
            value = item.group(2).strip().strip("\"'")
            meta[item.group(1)] = value

    return meta, match.group(2).strip()


def title_from_body(body: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", body, re.M)
    return match.group(1).strip() if match else fallback


def excerpt(body: str) -> str:
    text = re.sub(r"```.*?```", "", body, flags=re.S)
    text = re.sub(r"^#+\s+", "", text, flags=re.M)
    text = re.sub(r"[*_`>#-]", "", text)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return " ".join(lines)[:180]


def main() -> None:
    notes = []
    for section in SECTIONS:
        section_dir = ROOT / section["dir"]
        if not section_dir.exists():
            continue

        for file_path in sorted(section_dir.rglob("*.md")):
            raw = file_path.read_text(encoding="utf-8")
            meta, body = parse_front_matter(raw)
            relative_path = file_path.relative_to(ROOT).as_posix()
            fallback = file_path.stem
            notes.append(
                {
                    "id": relative_path.replace("/", "--").removesuffix(".md"),
                    "title": meta.get("title") or title_from_body(body, fallback),
                    "section": section["id"],
                    "sectionTitle": section["title"],
                    "path": relative_path,
                    "tags": meta.get("tags", ""),
                    "created": meta.get("created", ""),
                    "source": meta.get("source", ""),
                    "excerpt": excerpt(body),
                    "body": body,
                }
            )

    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    data = {
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "sections": SECTIONS,
        "notes": notes,
    }
    (DOCS_DIR / "data.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Generated docs/data.json with {len(notes)} notes.")


if __name__ == "__main__":
    main()
