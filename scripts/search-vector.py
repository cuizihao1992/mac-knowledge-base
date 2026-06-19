#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import numpy as np

from vector_utils import embed, token_set

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INDEX = ROOT / "data" / "vector-index"


def load_jsonl(path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def compact(text: str, limit: int = 260) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[: limit - 1] + "…"


def main() -> None:
    parser = argparse.ArgumentParser(description="Search the local vector index.")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--vector-weight", type=float, default=0.65)
    parser.add_argument("--json", action="store_true", help="Print JSON results")
    args = parser.parse_args()

    manifest = json.loads((args.index / "manifest.json").read_text(encoding="utf-8"))
    vectors = np.load(args.index / "vectors.npy")
    chunks = load_jsonl(args.index / "chunks.jsonl")
    query_vector = embed(args.query, int(manifest["dims"]))
    vector_scores = vectors @ query_vector
    query_terms = token_set(args.query)
    query_ascii_terms = {term for term in query_terms if re.search(r"[A-Za-z0-9]", term)}
    lexical_scores = []
    penalties = []
    for chunk in chunks:
        searchable_text = " ".join(str(chunk.get(key, "")) for key in ["title", "heading", "path", "content"])
        chunk_terms = token_set(searchable_text)
        if not query_terms or not chunk_terms:
            lexical_scores.append(0.0)
            penalties.append(1.0)
            continue
        overlap = len(query_terms & chunk_terms)
        lexical_scores.append(overlap / len(query_terms))
        missing_ascii_terms = query_ascii_terms - chunk_terms
        penalties.append(0.45 if missing_ascii_terms else 1.0)
    lexical_scores_array = np.array(lexical_scores, dtype=np.float32)
    penalties_array = np.array(penalties, dtype=np.float32)
    scores = (args.vector_weight * vector_scores + (1.0 - args.vector_weight) * lexical_scores_array) * penalties_array
    order = np.argsort(-scores)[: args.top_k]

    results = []
    for rank, row_index in enumerate(order, 1):
        chunk = chunks[int(row_index)]
        result = {
            "rank": rank,
            "score": float(scores[int(row_index)]),
            "vectorScore": float(vector_scores[int(row_index)]),
            "lexicalScore": float(lexical_scores_array[int(row_index)]),
            "penalty": float(penalties_array[int(row_index)]),
            "title": chunk.get("title"),
            "heading": chunk.get("heading"),
            "path": chunk.get("path"),
            "content": chunk.get("content"),
        }
        results.append(result)

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return

    for result in results:
        print(
            f"{result['rank']}. score={result['score']:.4f} "
            f"vector={result['vectorScore']:.4f} lexical={result['lexicalScore']:.4f} "
            f"penalty={result['penalty']:.2f} "
            f"{result['title']} / {result['heading']}"
        )
        print(f"   {result['path']}")
        print(f"   {compact(str(result['content']))}")
        print()


if __name__ == "__main__":
    main()
