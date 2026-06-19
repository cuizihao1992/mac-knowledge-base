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
python3 scripts/build-site.py
```

脚本会重新生成 `docs/data.json`，网站会自动展示最新内容。推送到 `main` 后，GitHub Actions 会部署到 GitHub Pages。

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
