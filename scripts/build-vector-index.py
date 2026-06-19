#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from vector_utils import embed

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INPUT = ROOT / "data" / "chunks.jsonl"
DEFAULT_OUTPUT = ROOT / "data" / "vector-index"


def load_chunks(path: Path) -> list[dict[str, object]]:
    chunks: list[dict[str, object]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                chunks.append(json.loads(line))
    return chunks


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a local vector index from JSONL chunks.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--dims", type=int, default=768)
    args = parser.parse_args()

    chunks = load_chunks(args.input)
    if not chunks:
        raise SystemExit(f"No chunks found in {args.input}")

    vectors = np.vstack([embed(str(chunk.get("content", "")), args.dims) for chunk in chunks])
    args.output.mkdir(parents=True, exist_ok=True)

    np.save(args.output / "vectors.npy", vectors)
    (args.output / "chunks.jsonl").write_text(
        "".join(json.dumps(chunk, ensure_ascii=False, sort_keys=True) + "\n" for chunk in chunks),
        encoding="utf-8",
    )

    try:
        source = args.input.relative_to(ROOT).as_posix()
    except ValueError:
        source = str(args.input)

    manifest = {
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "source": source,
        "backend": "local-hashing",
        "dims": args.dims,
        "chunkCount": len(chunks),
        "vectorShape": list(vectors.shape),
        "outputs": [
            "data/vector-index/vectors.npy",
            "data/vector-index/chunks.jsonl",
            "data/vector-index/manifest.json",
        ],
        "note": "This is a lightweight local index. Replace with embedding-model vectors when needed.",
    }
    (args.output / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    print(f"Generated vector index with {len(chunks)} chunks, dims={args.dims}.")


if __name__ == "__main__":
    main()
