# 本地知识库问答使用说明

> 更新时间：2026-06-19

## 当前能力

知识库现在已经有第一版本地问答脚本：

```bash
python3 scripts/ask-kb.py "jun-dd-web 为什么构建失败？下一步怎么修？"
```

它会执行：

1. 从 `data/vector-index/` 检索相关片段。
2. 从片段中提取结论、行动项和来源。
3. 输出一个带依据路径的回答。

当前版本不调用外部 AI，不需要 API key。

## 它和 search-vector.py 的区别

| 脚本 | 用途 |
| --- | --- |
| `scripts/search-vector.py` | 返回相似片段列表 |
| `scripts/ask-kb.py` | 基于相似片段整理成回答 |

`search-vector.py` 更像搜索引擎，`ask-kb.py` 更像一个无模型版 RAG 问答助手。

## 示例

```bash
python3 scripts/ask-kb.py "这个知识库有什么意义？"
```

```bash
python3 scripts/ask-kb.py "哪些项目构建失败？"
```

```bash
python3 scripts/ask-kb.py "jun-dd-web 下一步怎么修？"
```

## 输出结构

回答包含：

- `结论`
- `下一步`
- `依据片段`
- `来源`

这样做的重点是可追溯。即使没有大模型，也能知道回答来自哪篇文档。

## 当前限制

- 它不是大模型，不会做复杂推理。
- 它主要做检索、摘取和排序。
- 如果知识库没有记录，它不会自动知道答案。
- 问题越接近文档里的关键词，效果越好。

## 后续升级

下一步可以把 `ask-kb.py` 的检索结果作为上下文，交给模型生成更自然的回答。

可接入：

- OpenAI API
- DeepSeek API
- Ollama 本地模型
- LM Studio 本地模型
- Qwen / DeepSeek / Llama 本地量化模型

推荐顺序：

1. 保留当前无模型版作为 fallback。
2. 增加 `--provider openai` / `--provider ollama` 参数。
3. 让模型只基于检索片段回答，并强制输出来源。
