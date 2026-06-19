#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from kb_search import DEFAULT_INDEX, compact, search

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    parser = argparse.ArgumentParser(description="Search the local vector index.")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--vector-weight", type=float, default=0.65)
    parser.add_argument("--json", action="store_true", help="Print JSON results")
    args = parser.parse_args()

    results = search(args.query, index=args.index, top_k=args.top_k, vector_weight=args.vector_weight)

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
