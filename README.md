# Mac Knowledge Base

本仓库是一个面向 Mac 本地使用的个人知识库模板，核心格式为 Markdown，适合搭配 Obsidian、VS Code、Logseq 或命令行工具使用。

## 为什么做这个知识库

这个知识库不是资料堆放处，而是本机项目地图、环境复现手册、风险账本和后续行动清单。入口说明见：[知识库入口：它有什么意义](10_Notes/knowledge-base-purpose.md)。

## 目录

```text
.
├── 00_Inbox/          # 临时收集箱
├── 10_Notes/          # 长期笔记
├── 20_Projects/       # 项目资料
├── 30_References/     # 文章、PDF、网页摘要
├── 40_Code/           # 技术笔记和代码片段
├── 50_Daily/          # 每日记录
├── assets/            # 图片和附件
├── templates/         # 常用模板
└── scripts/           # 本地工具脚本
```

## 使用方式

1. 新内容先放进 `00_Inbox/`。
2. 每周整理一次，把内容移动到对应目录。
3. 使用 `tags`、`source` 和 `related` 维护上下文。
4. 用 `scripts/search.sh` 快速搜索知识库内容。

## 搜索

```bash
./scripts/search.sh "关键词"
```

## 网站

本仓库包含一个位于 `docs/` 的静态知识库网站。更新 Markdown 内容后，运行：

```bash
./scripts/update-all.sh
```

脚本会重新扫描项目、生成报告、重建 `docs/data.json`、AI 语料和本地向量索引。推送到 `main` 后，GitHub Pages 会展示最新内容。

## AI 语料

如果要让 AI、RAG 或向量数据库使用知识库内容，先生成 JSONL 语料：

```bash
./scripts/update-all.sh
```

脚本会生成：

- `data/corpus.jsonl`：文档级语料
- `data/chunks.jsonl`：检索级切块
- `data/manifest.json`：生成摘要

后续可以把 `data/chunks.jsonl` 送入 embedding 模型，再导入 Chroma、FAISS 或 LanceDB。

## 本地向量检索

生成第一版离线向量索引：

```bash
python3 scripts/build-vector-index.py
```

检索示例：

```bash
python3 scripts/search-vector.py "jun-dd-web 为什么构建失败"
```

当前实现是零 API key 的本地哈希向量索引，适合先把 RAG 检索流程跑通。说明见：[本地向量索引使用说明](30_References/local-vector-index-guide.md)。

## 本地知识库问答

基于向量检索结果生成无模型版回答：

```bash
python3 scripts/ask-kb.py "jun-dd-web 为什么构建失败？下一步怎么修？"
```

当前版本不调用外部 AI，不需要 API key。它会返回结论、下一步、依据片段和来源路径。说明见：[本地知识库问答使用说明](30_References/local-kb-qa-guide.md)。

也可以使用云端模型生成更自然的回答。8GB Mac 推荐这种方式，因为本机只负责检索，不负责运行大模型：

```bash
export DEEPSEEK_API_KEY=你的_key
python3 scripts/ask-kb.py "jun-dd-web 为什么构建失败？下一步怎么修？" --provider deepseek
```

通用 OpenAI-compatible API：

```bash
export KB_API_KEY=你的_key
python3 scripts/ask-kb.py "知识库现在能做什么？" \
  --provider openai-compatible \
  --base-url https://你的模型服务地址 \
  --model 你的模型名
```

说明见：[云端模型知识库问答使用说明](30_References/cloud-model-kb-qa-guide.md)。

常用命令模板见：[知识库问答命令模板](30_References/kb-qa-command-demos.md)。

## 笔记格式

推荐每篇笔记包含 YAML front matter：

```markdown
---
title:
tags: []
created:
source:
related: []
---

# 标题

## 摘要

## 关键点

## 我的理解

## 后续行动
```

## 维护节奏

- 每天：记录新想法、阅读摘录、任务线索。
- 每周：清理 `00_Inbox/`，合并重复笔记。
- 每月：回顾项目资料，沉淀长期知识。
