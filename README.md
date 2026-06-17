# Mac Knowledge Base

本仓库是一个面向 Mac 本地使用的个人知识库模板，核心格式为 Markdown，适合搭配 Obsidian、VS Code、Logseq 或命令行工具使用。

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
