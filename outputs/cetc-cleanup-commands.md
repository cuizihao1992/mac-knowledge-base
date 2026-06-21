---
title: CETC 清理命令计划
tags: [reference, code, cetc, cleanup, generated]
created: 2026-06-22
source: /Users/cuizihao/CETC/Project
related: [CETC 清理执行计划, CETC 自动资产抽取报告]
---

# CETC 清理命令计划

> 生成时间：2026-06-21T16:04:02.924238+00:00

## 说明

这是 dry-run 命令计划，默认不移动、不删除任何项目。

- 包含动作：摘要后可删
- 命令数量：0
- JSON 输出：`outputs/cetc-cleanup-commands.json`

## 目标目录

- `摘要后可删` -> `/Users/cuizihao/CETC/Archive/delete-after-review`

## 待执行命令

## 执行后复核

真正移动后，重新运行：

```bash
python3 scripts/extract-cetc-assets.py
python3 scripts/build-site.py
python3 scripts/build-corpus.py
python3 scripts/build-vector-index.py
```
