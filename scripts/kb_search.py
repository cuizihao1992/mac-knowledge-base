from __future__ import annotations

import json
import re
from pathlib import Path

try:
    import numpy as np
except ModuleNotFoundError:
    np = None

try:
    from vector_utils import embed, token_set
except ModuleNotFoundError:
    embed = None

    def token_set(text: str) -> set[str]:
        ascii_terms = re.findall(r"[A-Za-z0-9_./:-]+", text.lower())
        cjk_terms = re.findall(r"[\u4e00-\u9fff]{1,4}", text)
        cjk_bigrams: list[str] = []
        for term in cjk_terms:
            if len(term) == 1:
                cjk_bigrams.append(term)
            else:
                cjk_bigrams.extend(term[index : index + 2] for index in range(len(term) - 1))
        return set(ascii_terms + cjk_bigrams)

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INDEX = ROOT / "data" / "vector-index"
MIN_SCORE = 0.05


def load_jsonl(path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def search(
    query: str,
    index: Path = DEFAULT_INDEX,
    top_k: int = 5,
    vector_weight: float = 0.65,
) -> list[dict[str, object]]:
    manifest = json.loads((index / "manifest.json").read_text(encoding="utf-8"))
    chunks = load_jsonl(index / "chunks.jsonl")
    query_terms = token_set(query)
    query_ascii_terms = {term for term in query_terms if re.search(r"[A-Za-z0-9]", term)}
    has_vector_backend = np is not None and embed is not None and (index / "vectors.npy").exists()

    if has_vector_backend:
        vectors = np.load(index / "vectors.npy")
        query_vector = embed(query, int(manifest["dims"]))
        vector_scores = vectors @ query_vector
    else:
        vector_scores = [0.0] * len(chunks)

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

    if np is not None:
        lexical_scores_array = np.array(lexical_scores, dtype=np.float32)
        penalties_array = np.array(penalties, dtype=np.float32)
        scores = (vector_weight * vector_scores + (1.0 - vector_weight) * lexical_scores_array) * penalties_array
        order = np.argsort(-scores)[:top_k]
    else:
        lexical_scores_array = lexical_scores
        penalties_array = penalties
        scores = [score * penalty for score, penalty in zip(lexical_scores, penalties)]
        order = sorted(range(len(scores)), key=lambda index: scores[index], reverse=True)[:top_k]

    if len(scores) == 0 or max(float(score) for score in scores) < MIN_SCORE:
        return []

    results = []
    for rank, row_index in enumerate(order, 1):
        chunk = chunks[int(row_index)]
        results.append(
            {
                "rank": rank,
                "score": float(scores[int(row_index)]),
                "vectorScore": float(vector_scores[int(row_index)]),
                "lexicalScore": float(lexical_scores_array[int(row_index)]),
                "penalty": float(penalties_array[int(row_index)]),
                "backend": "local-hashing" if has_vector_backend else "lexical-fallback",
                "title": chunk.get("title"),
                "heading": chunk.get("heading"),
                "path": chunk.get("path"),
                "content": chunk.get("content"),
            }
        )
    return results


def compact(text: str, limit: int = 260) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[: limit - 1] + "…"
