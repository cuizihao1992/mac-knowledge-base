# 云端模型知识库问答使用说明

> 更新时间：2026-06-20

## 当前选择

这台 Mac 是 8GB 内存，更适合“本地检索 + 云端模型回答”。

实际流程：

```text
Markdown 知识库
-> 本地语料和向量索引
-> 检索相关片段
-> 调用云端模型总结回答
-> 返回来源路径
```

这样做的好处是：

- 本机不用运行 7B、14B 大模型。
- 知识库内容仍然保存在本地仓库。
- 每次回答都带来源，方便回到原始文档核对。
- DeepSeek、OpenAI 和 OpenAI-compatible 服务都可以接入。

## DeepSeek API

设置 API key：

```bash
export DEEPSEEK_API_KEY=你的_key
```

提问：

```bash
python3 scripts/ask-kb.py "jun-dd-web 为什么构建失败？下一步怎么修？" --provider deepseek
```

也可以使用快捷入口。先复制配置模板：

```bash
cp .env.example .env
```

在 `.env` 中填写：

```text
DEEPSEEK_API_KEY=你的_key
KB_PROVIDER=deepseek
```

之后直接提问：

```bash
./scripts/ask.sh "jun-dd-web 为什么构建失败？下一步怎么修？"
```

默认模型：

```text
deepseek-chat
```

也可以显式指定模型：

```bash
python3 scripts/ask-kb.py "CETC 项目下一步优先做什么？" \
  --provider deepseek \
  --model deepseek-chat
```

## OpenAI-compatible API

很多模型服务都兼容 `/v1/chat/completions` 形态。可以用通用模式：

```bash
export KB_API_KEY=你的_key
python3 scripts/ask-kb.py "知识库整体目标是什么？" \
  --provider openai-compatible \
  --base-url https://你的模型服务地址 \
  --model 你的模型名
```

快捷入口需要在 `.env` 中填写：

```text
KB_PROVIDER=openai-compatible
KB_API_KEY=你的_key
KB_BASE_URL=https://你的模型服务地址
KB_MODEL=你的模型名
```

然后运行：

```bash
./scripts/ask.sh "知识库整体目标是什么？"
```

如果 key 放在别的环境变量里：

```bash
export MY_MODEL_KEY=你的_key
python3 scripts/ask-kb.py "哪些项目构建失败？" \
  --provider openai-compatible \
  --base-url https://你的模型服务地址 \
  --model 你的模型名 \
  --api-key-env MY_MODEL_KEY
```

## OpenAI API

设置 API key：

```bash
export OPENAI_API_KEY=你的_key
```

提问：

```bash
python3 scripts/ask-kb.py "知识库现在能帮我做什么？" --provider openai
```

如需固定模型：

```bash
python3 scripts/ask-kb.py "CETC 项目风险有哪些？" \
  --provider openai \
  --model gpt-4o-mini
```

## 无模型 fallback

不传 `--provider` 时仍然使用无模型版：

```bash
python3 scripts/ask-kb.py "知识库价值是什么？"
```

快捷入口也可以临时指定无模型：

```bash
./scripts/ask.sh "知识库价值是什么？" none
```

这个模式不需要 API key，适合离线查看、排查检索结果、或者模型服务不可用时兜底。

## 参数说明

| 参数 | 作用 |
| --- | --- |
| `--provider none` | 默认，无模型摘取式回答 |
| `--provider deepseek` | 使用 DeepSeek API |
| `--provider openai` | 使用 OpenAI API |
| `--provider openai-compatible` | 使用兼容 OpenAI Chat Completions 的服务 |
| `--model` | 指定模型名 |
| `--base-url` | 指定 API 服务地址 |
| `--api-key-env` | 指定读取哪个环境变量作为 key |
| `--top-k` | 控制送给模型的知识库片段数量 |
| `--temperature` | 控制回答发散程度，默认 0.2 |

## 快捷入口

`scripts/ask.sh` 会自动读取仓库根目录的 `.env`。

如果不配置 `.env`，默认使用无模型版本地检索，不需要 API key：

```bash
./scripts/ask.sh "知识库价值是什么？"
```

如果要使用 DeepSeek，推荐配置：

```text
DEEPSEEK_API_KEY=你的_key
KB_PROVIDER=deepseek
```

常用命令：

```bash
./scripts/ask.sh "我的知识库整体目标是什么？下一步应该做什么？"
```

临时切换 provider：

```bash
./scripts/ask.sh "哪些 CETC 项目构建失败？" none
```

## 注意事项

- 不要把 API key 写进 Markdown、脚本或 Git 提交。
- `.env` 已加入 `.gitignore`，真实 key 放在 `.env`，模板放在 `.env.example`。
- 如果问题涉及敏感项目资料，先确认能否发送到云端模型。
- 模型只会看到检索出来的片段，不会自动读取整个电脑。
- 回答里如果说“信息不足”，通常说明知识库文档还需要补充。

## 推荐下一步

1. 先用 DeepSeek API 跑通知识库问答。
2. 对常问问题建立固定问题清单。
3. 把高价值回答沉淀回 Markdown 文档。
4. 后续再把哈希向量索引升级成真正 embedding 向量。
