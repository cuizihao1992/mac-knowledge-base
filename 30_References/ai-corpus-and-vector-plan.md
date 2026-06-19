# AI 语料与向量库建设计划

> 更新时间：2026-06-19

## 当前选择

下一步先做语料层，不直接训练模型，也不直接绑定某个向量数据库。

当前产物：

- `data/corpus.jsonl`：文档级语料，一篇 Markdown 对应一行。
- `data/chunks.jsonl`：检索级语料，按标题层级和长度切分。
- `data/manifest.json`：生成时间、文档数量、切块数量。

## 为什么先做 JSONL

JSONL 的价值不是让模型“更认识 JSON”，而是让程序和 AI 都能稳定读取。

每一行都是一个独立对象，适合：

- 批量生成 embedding
- 导入 Chroma / FAISS / LanceDB
- 做关键词检索
- 做 RAG 问答
- 回溯来源文件

## 字段解释

| 字段 | 用途 |
| --- | --- |
| `id` | 稳定唯一编号，便于引用和更新 |
| `documentId` | chunk 对应的原始文档 |
| `type` | 区分 document / chunk |
| `title` | 原始文档标题 |
| `heading` | chunk 所在标题段落 |
| `section` | 知识库分类 |
| `path` | 来源文件路径 |
| `tags` | 标签，后续可用于过滤 |
| `content` | 真正送去 embedding 或检索的正文 |
| `charCount` | 内容长度，便于排查切块质量 |

## 为什么不先训练模型

当前知识库更适合 RAG，不适合优先微调模型。

原因：

- 文档会持续变化，向量库更新更快。
- 项目状态是事实型知识，RAG 更容易追溯来源。
- 微调成本高，且更新一篇文档不能立刻反映到模型里。
- 本地消费级设备更适合运行模型和向量检索，不适合从头训练。

推荐路径：

```text
Markdown 知识库
→ corpus.jsonl
→ chunks.jsonl
→ embeddings
→ 向量库
→ RAG 问答
```

## 后续可选方案

### 轻量本地版

- 使用 `chunks.jsonl`
- 调本地 embedding 模型
- 存 FAISS 或 Chroma
- 用本地 DeepSeek / Qwen / Llama 做回答

### OpenAI API 版

- 使用 `text-embedding-3-small` 或更新的 embedding 模型
- 存 Chroma / LanceDB
- 用 OpenAI 模型做问答和总结

### 纯脚本检索版

- 不生成向量
- 只用关键词和 BM25
- 成本最低，但语义搜索弱一些

## 文件格式处理原则

向量库最终处理的是文本。不同格式需要先抽取文本：

| 格式 | 处理方式 |
| --- | --- |
| Markdown / txt | 直接读取 |
| JSON / YAML | 提取字段后转文本 |
| PDF | 提取文字；扫描件需要 OCR |
| Word / docx | 用解析库抽取正文 |
| Excel / CSV | 表格转文本或记录级 JSON |
| PPTX | 按页面抽取标题和正文 |
| 图片 | OCR 或视觉模型描述 |
| 代码 | 按文件、函数、类切分 |

当前第一版只处理 Markdown，因为知识库主体就是 Markdown。

## 使用命令

```bash
python3 scripts/build-corpus.py
```

生成后可以用：

```bash
head -n 1 data/chunks.jsonl
```

查看单条语料。
