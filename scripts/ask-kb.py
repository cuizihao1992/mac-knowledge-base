#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import OrderedDict
from pathlib import Path

from kb_search import DEFAULT_INDEX, compact, search


ACTION_WORDS = [
    "下一步",
    "建议",
    "优先",
    "修复",
    "补",
    "固定",
    "检查",
    "验证",
    "生成",
    "构建",
    "失败",
    "风险",
]

ACTION_QUERY_WORDS = ["下一步", "怎么", "如何", "修", "处理", "解决", "做什么", "怎么办"]


def split_sentences(text: str) -> list[str]:
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"\|.*?\|", "", text)
    lines = []
    for raw_line in text.splitlines():
        line = raw_line.strip().strip("-").strip()
        if not line or line.startswith("#"):
            continue
        line = re.sub(r"^\d+\.\s*", "", line)
        parts = re.split(r"(?<=[。！？])\s*", line)
        lines.extend(part.strip() for part in parts if part.strip())
    return lines


def score_sentence(sentence: str, query: str) -> int:
    score = 0
    query_terms = set(re.findall(r"[A-Za-z0-9_.-]+|[\u4e00-\u9fff]{2,}", query.lower()))
    lowered = sentence.lower()
    for term in query_terms:
        if term and term in lowered:
            score += 3
    for word in ACTION_WORDS:
        if word in sentence:
            score += 2
    if len(sentence) > 180:
        score -= 1
    return score


def best_sentences(results: list[dict[str, object]], query: str, limit: int = 6) -> list[str]:
    candidates = []
    seen = set()
    for result in results:
        content = str(result.get("content", ""))
        if len(re.sub(r"\s+", "", content)) < 40:
            continue
        for sentence in split_sentences(str(result.get("content", ""))):
            normalized = re.sub(r"\s+", "", sentence)
            if normalized in seen:
                continue
            seen.add(normalized)
            score = score_sentence(sentence, query)
            if score > 0:
                candidates.append((score, sentence))
    candidates.sort(key=lambda item: item[0], reverse=True)
    return [sentence for _, sentence in candidates[:limit]]


def query_ascii_terms(query: str) -> set[str]:
    return set(re.findall(r"[A-Za-z0-9_.-]+", query.lower()))


def extract_actions(sentences: list[str], query: str) -> list[str]:
    ascii_terms = query_ascii_terms(query)
    actions = []
    for sentence in sentences:
        if ascii_terms and not any(term in sentence.lower() for term in ascii_terms):
            continue
        if any(word in sentence for word in ACTION_WORDS):
            actions.append(sentence)
    return actions[:5]


def wants_actions(query: str) -> bool:
    return any(word in query for word in ACTION_QUERY_WORDS)


def unique_sources(results: list[dict[str, object]]) -> list[tuple[str, str]]:
    sources: OrderedDict[str, str] = OrderedDict()
    for result in results:
        path = str(result.get("path", ""))
        title = str(result.get("title", ""))
        if path and path not in sources:
            sources[path] = title
    return [(path, title) for path, title in sources.items()]


def print_answer(query: str, results: list[dict[str, object]]) -> None:
    sentences = best_sentences(results, query)
    actions = extract_actions(sentences, query)
    sources = unique_sources(results)

    print(f"# {query}\n")
    print("## 结论")
    if sentences:
        for sentence in sentences[:4]:
            print(f"- {sentence}")
    else:
        print("- 没有从知识库中提取到足够明确的结论。")

    print("\n## 下一步")
    if wants_actions(query) and actions:
        for index, action in enumerate(actions, 1):
            print(f"{index}. {action}")
    elif wants_actions(query):
        print("1. 先查看下方来源片段，确认知识库是否已有足够信息。")
        print("2. 如果信息不足，补充项目验证记录后重新生成语料和索引。")
    else:
        print("- 这是解释型问题，当前不强行生成行动项。")

    print("\n## 依据片段")
    for result in results:
        print(
            f"- [{result['rank']}] score={result['score']:.4f} "
            f"{result['title']} / {result['heading']} ({result['path']})"
        )
        print(f"  {compact(str(result.get('content', '')), 220)}")

    print("\n## 来源")
    for path, title in sources:
        print(f"- {title}: `{path}`")

    print("\n> 当前为无模型版回答：它基于本地检索片段做摘取和排序，不会调用外部 AI。")


def main() -> None:
    parser = argparse.ArgumentParser(description="Ask the local knowledge base without an external model.")
    parser.add_argument("query", help="Question to ask")
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    parser.add_argument("--top-k", type=int, default=8)
    parser.add_argument("--json", action="store_true", help="Print raw retrieved context as JSON")
    args = parser.parse_args()

    results = search(args.query, index=args.index, top_k=args.top_k)
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return
    print_answer(args.query, results)


if __name__ == "__main__":
    main()
