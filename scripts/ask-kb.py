#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
from collections import OrderedDict
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from kb_search import DEFAULT_INDEX, compact, search


PROVIDER_CONFIG = {
    "deepseek": {
        "base_url": "https://api.deepseek.com",
        "api_key_env": "DEEPSEEK_API_KEY",
        "model": "deepseek-chat",
    },
    "openai": {
        "base_url": "https://api.openai.com",
        "api_key_env": "OPENAI_API_KEY",
        "model": "gpt-4o-mini",
    },
}

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


def retrieved_context(results: list[dict[str, object]], max_chars: int = 9000) -> str:
    blocks = []
    total = 0
    for result in results:
        block = (
            f"[{result['rank']}] {result['title']} / {result['heading']}\n"
            f"path: {result['path']}\n"
            f"score: {result['score']:.4f}\n"
            f"{str(result.get('content', '')).strip()}"
        )
        if total + len(block) > max_chars:
            break
        blocks.append(block)
        total += len(block)
    return "\n\n---\n\n".join(blocks)


def build_messages(query: str, results: list[dict[str, object]]) -> list[dict[str, str]]:
    context = retrieved_context(results)
    system = (
        "你是一个个人知识库问答助手。只能基于用户提供的知识库片段回答；"
        "如果片段不足以回答，要明确说信息不足。回答使用中文，务必给出来源路径。"
    )
    user = f"""问题：
{query}

知识库片段：
{context}

请按这个结构回答：
1. 结论
2. 依据
3. 下一步
4. 来源
"""
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def provider_defaults(provider: str) -> dict[str, str]:
    return PROVIDER_CONFIG.get(provider, {})


def resolve_api_key(provider: str, explicit_env: str | None) -> str:
    env_name = explicit_env or provider_defaults(provider).get("api_key_env") or "KB_API_KEY"
    api_key = os.environ.get(env_name)
    if not api_key:
        raise SystemExit(f"缺少 API key。请先设置环境变量：export {env_name}=你的_key")
    return api_key


def chat_completion(
    provider: str,
    query: str,
    results: list[dict[str, object]],
    model: str | None,
    base_url: str | None,
    api_key_env: str | None,
    temperature: float,
) -> str:
    defaults = provider_defaults(provider)
    resolved_model = model or defaults.get("model")
    if not resolved_model:
        raise SystemExit("缺少模型名。请通过 --model 指定，例如 --model deepseek-chat")

    resolved_base_url = (base_url or defaults.get("base_url") or "").rstrip("/")
    if not resolved_base_url:
        raise SystemExit("缺少 API 地址。请通过 --base-url 指定，例如 https://api.deepseek.com")

    api_key = resolve_api_key(provider, api_key_env)
    payload = {
        "model": resolved_model,
        "messages": build_messages(query, results),
        "temperature": temperature,
    }
    request = Request(
        f"{resolved_base_url}/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urlopen(request, timeout=90) as response:
            data = json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"API 请求失败：HTTP {exc.code}\n{detail}") from exc
    except URLError as exc:
        raise SystemExit(f"API 请求失败：{exc.reason}") from exc

    try:
        return str(data["choices"][0]["message"]["content"]).strip()
    except (KeyError, IndexError, TypeError) as exc:
        raise SystemExit(f"API 返回格式无法解析：{json.dumps(data, ensure_ascii=False)[:1000]}") from exc


def print_model_answer(query: str, answer: str, results: list[dict[str, object]], provider: str, model: str) -> None:
    print(f"# {query}\n")
    print(answer.strip())
    print("\n## 检索来源")
    for path, title in unique_sources(results):
        print(f"- {title}: `{path}`")
    print(f"\n> 当前回答由 `{provider}` / `{model}` 基于本地检索片段生成。")


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
    parser = argparse.ArgumentParser(description="Ask the local knowledge base.")
    parser.add_argument("query", help="Question to ask")
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    parser.add_argument("--top-k", type=int, default=8)
    parser.add_argument(
        "--provider",
        choices=["none", "deepseek", "openai", "openai-compatible"],
        default="none",
        help="Answer provider. 'none' uses extractive local fallback.",
    )
    parser.add_argument("--model", help="Chat model name")
    parser.add_argument("--base-url", help="OpenAI-compatible API base URL")
    parser.add_argument("--api-key-env", help="Environment variable that stores the API key")
    parser.add_argument("--temperature", type=float, default=0.2)
    parser.add_argument("--json", action="store_true", help="Print raw retrieved context as JSON")
    args = parser.parse_args()

    results = search(args.query, index=args.index, top_k=args.top_k)
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return
    if args.provider != "none":
        defaults = provider_defaults(args.provider)
        model = args.model or defaults.get("model")
        answer = chat_completion(
            args.provider,
            args.query,
            results,
            args.model,
            args.base_url,
            args.api_key_env,
            args.temperature,
        )
        print_model_answer(args.query, answer, results, args.provider, model or "unknown")
        return
    print_answer(args.query, results)


if __name__ == "__main__":
    main()
