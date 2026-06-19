from __future__ import annotations

import hashlib
import re

import numpy as np


def tokenize(text: str) -> list[str]:
    ascii_terms = re.findall(r"[A-Za-z0-9_./:-]+", text.lower())
    cjk_terms = re.findall(r"[\u4e00-\u9fff]{1,4}", text)
    cjk_bigrams: list[str] = []
    for term in cjk_terms:
        if len(term) == 1:
            cjk_bigrams.append(term)
        else:
            cjk_bigrams.extend(term[i : i + 2] for i in range(len(term) - 1))
    return ascii_terms + cjk_bigrams


def token_hash(token: str, dims: int) -> tuple[int, float]:
    digest = hashlib.blake2b(token.encode("utf-8"), digest_size=8).digest()
    value = int.from_bytes(digest, "big")
    index = value % dims
    sign = -1.0 if (value >> 63) else 1.0
    return index, sign


def embed(text: str, dims: int) -> np.ndarray:
    vector = np.zeros(dims, dtype=np.float32)
    for token in tokenize(text):
        index, sign = token_hash(token, dims)
        vector[index] += sign
    norm = float(np.linalg.norm(vector))
    if norm:
        vector /= norm
    return vector


def token_set(text: str) -> set[str]:
    return set(tokenize(text))
