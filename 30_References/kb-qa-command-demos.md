---
title: 知识库问答命令模板
tags: [reference, ai, qa, deepseek, command]
created: 2026-07-11
source: scripts/ask.sh
related: [本地知识库问答使用说明, 云端模型知识库问答使用说明]
---

# 知识库问答命令模板

## 进入项目目录

所有命令先进入知识库目录：

```bash
cd /Users/cuizihao/Documents/Codex/2026-06-18/mac
```

## 本地无 Key 问答

不调用外部模型，只做本地检索和摘录：

```bash
./scripts/ask.sh "知识库现在能做什么？"
```

```bash
./scripts/ask.sh "哪些 CETC 项目最值得保留？"
```

```bash
./scripts/ask.sh "哪些文件建议删除？直接告诉我结论，简短回答"
```

适合：

- 快速查资料。
- 不想把内容发给云端模型。
- 检查知识库里有没有相关记录。

## DeepSeek 临时 Key 模式

只在当前终端临时使用，不写入文件：

```bash
export DEEPSEEK_API_KEY="你的_deepseek_key"
./scripts/ask.sh "哪些 CETC 项目最值得保留？请直接给结论和原因" deepseek
```

```bash
export DEEPSEEK_API_KEY="你的_deepseek_key"
./scripts/ask.sh "哪些 CETC 项目可以归档？哪些不要删？用表格回答" deepseek
```

```bash
export DEEPSEEK_API_KEY="你的_deepseek_key"
./scripts/ask.sh "jun-dd-web 有哪些可复用资产？按组件、页面、GIS、风险分组" deepseek
```

## DeepSeek 长期配置模式

复制配置模板：

```bash
cp .env.example .env
```

编辑 `.env`：

```bash
nano .env
```

填写：

```text
KB_PROVIDER=deepseek
DEEPSEEK_API_KEY=你的_deepseek_key
```

之后可以直接运行：

```bash
./scripts/ask.sh "我的知识库整体目标是什么？下一步应该做什么？"
```

## 常用 Demo 问题

### 项目清理

```bash
./scripts/ask.sh "哪些 CETC 项目建议删除或归档？请只输出结论列表" deepseek
```

```bash
./scripts/ask.sh "第一批已经移动了哪些项目？现在还能恢复吗？" deepseek
```

```bash
./scripts/ask.sh "第二批普通归档应该处理哪些项目？给出风险提醒" deepseek
```

### 高价值资产

```bash
./scripts/ask.sh "高价值 CETC 项目有哪些？分别有什么业务价值？" deepseek
```

```bash
./scripts/ask.sh "gis-map-sdk 和 gis-map-sdk-cesium 的价值区别是什么？" deepseek
```

```bash
./scripts/ask.sh "xinfang 项目有哪些可沉淀的业务知识？" deepseek
```

### 架构和复用

```bash
./scripts/ask.sh "这个知识库最终架构是什么？目前还缺什么？" deepseek
```

```bash
./scripts/ask.sh "如果我要把这些旧项目经验复用到新项目，优先看哪些文档？" deepseek
```

```bash
./scripts/ask.sh "当前本地问答、向量索引、DeepSeek 三者的关系是什么？" deepseek
```

### 风险检查

```bash
./scripts/ask.sh "哪些项目有敏感配置风险？只列项目名和原因" deepseek
```

```bash
./scripts/ask.sh "哪些内容不应该直接推到公开仓库？" deepseek
```

```bash
./scripts/ask.sh "删除旧项目之前必须确认哪些事情？" deepseek
```

## 指定模型

默认模型是 `deepseek-chat`。需要显式指定时：

```bash
./scripts/ask.sh "知识库现在最值得优化什么？" deepseek --model deepseek-chat
```

## 控制检索片段数量

默认会取前 8 个相关片段。想多给模型一些上下文：

```bash
./scripts/ask.sh "请综合判断 CETC 项目的删除、归档、保留策略" deepseek --top-k 12
```

想更简短：

```bash
./scripts/ask.sh "哪些项目可以归档？只给结论" deepseek --top-k 5
```

## 输出 JSON 检索结果

只看检索命中的原始片段，不调用模型：

```bash
python3 scripts/ask-kb.py "哪些项目可以归档？" --json
```

这适合排查为什么回答不准。

## 安全提醒

- 不要把 DeepSeek Key 写进 Markdown。
- 不要把 `.env` 提交到 GitHub。
- 涉及真实账号、密码、token、client_secret 的问题，先确认是否可以发给云端模型。
- DeepSeek 只能看到检索出来的片段，不会自动读取整台电脑。
