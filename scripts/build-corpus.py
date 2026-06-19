#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

SECTIONS = [
    {"id": "inbox", "title": "Inbox", "dir": "00_Inbox"},
    {"id": "notes", "title": "Notes", "dir": "10_Notes"},
    {"id": "projects", "title": "Projects", "dir": "20_Projects"},
    {"id": "references", "title": "References", "dir": "30_References"},
    {"id": "code", "title": "Code", "dir": "40_Code"},
    {"id": "daily", "title": "Daily", "dir": "50_Daily"},
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
            meta[item.group(1)] = item.group(2).strip().strip("\"'")

    return meta, match.group(2).strip()


def title_from_body(body: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", body, re.M)
    return match.group(1).strip() if match else fallback


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def stable_id(*parts: str) -> str:
    raw = "::".join(parts)
    digest = hashlib.sha1(raw.encode("utf-8")).hexdigest()[:12]
    readable = re.sub(r"[^A-Za-z0-9._/-]+", "-", parts[0]).strip("-")
    return f"{readable}::{digest}"


def parse_tags(meta_tags: str) -> list[str]:
    if not meta_tags:
        return []
    value = meta_tags.strip()
    if value.startswith("[") and value.endswith("]"):
        value = value[1:-1]
    return [item.strip().strip("\"'") for item in value.split(",") if item.strip()]


def heading_chunks(body: str) -> list[tuple[str, str]]:
    lines = body.splitlines()
    chunks: list[tuple[str, list[str]]] = []
    current_heading = "全文"
    current_lines: list[str] = []

    for line in lines:
        match = re.match(r"^(#{1,3})\s+(.+)$", line)
        if match and current_lines:
            chunks.append((current_heading, current_lines))
            current_heading = match.group(2).strip()
            current_lines = [line]
        else:
            if match:
                current_heading = match.group(2).strip()
            current_lines.append(line)

    if current_lines:
        chunks.append((current_heading, current_lines))

    return [(heading, normalize_text("\n".join(chunk_lines))) for heading, chunk_lines in chunks]


def split_long_text(text: str, max_chars: int = 1800, overlap: int = 180) -> list[str]:
    if len(text) <= max_chars:
        return [text]

    parts: list[str] = []
    start = 0
    while start < len(text):
        end = min(start + max_chars, len(text))
        candidate = text[start:end]
        split_at = max(candidate.rfind("\n\n"), candidate.rfind("\n"), candidate.rfind("。"))
        if split_at > max_chars * 0.55:
            end = start + split_at + 1
        parts.append(text[start:end].strip())
        if end >= len(text):
            break
        start = max(0, end - overlap)

    return [part for part in parts if part]


def write_jsonl(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def main() -> None:
    generated_at = datetime.now(timezone.utc).isoformat()
    corpus: list[dict[str, object]] = []
    chunks: list[dict[str, object]] = []

    for section in SECTIONS:
        section_dir = ROOT / section["dir"]
        if not section_dir.exists():
            continue

        for file_path in sorted(section_dir.rglob("*.md")):
            raw = file_path.read_text(encoding="utf-8")
            meta, body = parse_front_matter(raw)
            body = normalize_text(body)
            relative_path = file_path.relative_to(ROOT).as_posix()
            title = meta.get("title") or title_from_body(body, file_path.stem)
            tags = parse_tags(meta.get("tags", ""))
            doc_id = stable_id(relative_path)

            corpus.append(
                {
                    "id": doc_id,
                    "type": "document",
                    "title": title,
                    "section": section["id"],
                    "sectionTitle": section["title"],
                    "path": relative_path,
                    "tags": tags,
                    "created": meta.get("created", ""),
                    "source": meta.get("source", ""),
                    "content": body,
                    "charCount": len(body),
                    "generatedAt": generated_at,
                }
            )

            chunk_index = 0
            for heading, chunk_text in heading_chunks(body):
                for piece in split_long_text(chunk_text):
                    chunks.append(
                        {
                            "id": stable_id(relative_path, heading, str(chunk_index), piece[:80]),
                            "documentId": doc_id,
                            "type": "chunk",
                            "title": title,
                            "heading": heading,
                            "section": section["id"],
                            "sectionTitle": section["title"],
                            "path": relative_path,
                            "tags": tags,
                            "content": piece,
                            "charCount": len(piece),
                            "chunkIndex": chunk_index,
                            "generatedAt": generated_at,
                        }
                    )
                    chunk_index += 1

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    write_jsonl(DATA_DIR / "corpus.jsonl", corpus)
    write_jsonl(DATA_DIR / "chunks.jsonl", chunks)

    manifest = {
        "generatedAt": generated_at,
        "documentCount": len(corpus),
        "chunkCount": len(chunks),
        "outputs": ["data/corpus.jsonl", "data/chunks.jsonl"],
    }
    (DATA_DIR / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    print(f"Generated {len(corpus)} documents and {len(chunks)} chunks.")


if __name__ == "__main__":
    main()
