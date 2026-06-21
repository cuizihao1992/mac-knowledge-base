---
title: CETC 清理命令计划
tags: [reference, code, cetc, cleanup, generated]
created: 2026-06-21
source: /Users/cuizihao/CETC/Project
related: [CETC 清理执行计划, CETC 自动资产抽取报告]
---

# CETC 清理命令计划

> 生成时间：2026-06-21T15:59:19.965140+00:00

## 说明

这是 dry-run 命令计划，默认不移动、不删除任何项目。

- 包含动作：摘要后可删
- 命令数量：4
- JSON 输出：`outputs/cetc-cleanup-commands.json`

## 目标目录

- `摘要后可删` -> `/Users/cuizihao/CETC/Archive/delete-after-review`

## 待执行命令

### cetc-ui/compass-ui-demo

- 业务价值：低到中，需按目录确认
- 建议动作：`摘要后可删`
- 源目录：`/Users/cuizihao/CETC/Project/cetc-ui/compass-ui-demo`
- 目标目录：`/Users/cuizihao/CETC/Archive/delete-after-review`

```bash
mkdir -p /Users/cuizihao/CETC/Archive/delete-after-review
mv /Users/cuizihao/CETC/Project/cetc-ui/compass-ui-demo /Users/cuizihao/CETC/Archive/delete-after-review/
```

### gis/offline-map

- 业务价值：GIS / BI / 地图资产
- 建议动作：`摘要后可删`
- 源目录：`/Users/cuizihao/CETC/Project/gis/offline-map`
- 目标目录：`/Users/cuizihao/CETC/Archive/delete-after-review`

```bash
mkdir -p /Users/cuizihao/CETC/Archive/delete-after-review
mv /Users/cuizihao/CETC/Project/gis/offline-map /Users/cuizihao/CETC/Archive/delete-after-review/
```

### industry-chain

- 业务价值：低到中，需按目录确认
- 建议动作：`摘要后可删`
- 源目录：`/Users/cuizihao/CETC/Project/industry-chain`
- 目标目录：`/Users/cuizihao/CETC/Archive/delete-after-review`

```bash
mkdir -p /Users/cuizihao/CETC/Archive/delete-after-review
mv /Users/cuizihao/CETC/Project/industry-chain /Users/cuizihao/CETC/Archive/delete-after-review/
```

### smartCity/managerweb

- 业务价值：智慧城市业务
- 建议动作：`摘要后可删`
- 源目录：`/Users/cuizihao/CETC/Project/smartCity/managerweb`
- 目标目录：`/Users/cuizihao/CETC/Archive/delete-after-review`

```bash
mkdir -p /Users/cuizihao/CETC/Archive/delete-after-review
mv /Users/cuizihao/CETC/Project/smartCity/managerweb /Users/cuizihao/CETC/Archive/delete-after-review/
```

## 执行后复核

真正移动后，重新运行：

```bash
python3 scripts/extract-cetc-assets.py
python3 scripts/build-site.py
python3 scripts/build-corpus.py
python3 scripts/build-vector-index.py
```
