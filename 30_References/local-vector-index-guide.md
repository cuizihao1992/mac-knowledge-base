# 本地向量索引使用说明

> 更新时间：2026-06-19

## 当前实现

当前已经有第一版离线可用的本地向量索引。

产物位置：

- `data/vector-index/vectors.npy`
- `data/vector-index/chunks.jsonl`
- `data/vector-index/manifest.json`

脚本：

- `scripts/build-vector-index.py`
- `scripts/search-vector.py`
- `scripts/vector_utils.py`

## 它是什么

这不是最终形态的高精度 embedding 向量库，而是一个轻量本地索引：

- 不需要 API key
- 不需要安装 Chroma / FAISS
- 使用本地哈希词向量
- 支持中文和英文关键词
- 用 cosine 相似度 + 关键词重合做混合排序

它的价值是先把知识库跑通成“AI 可检索”的状态。后续可以把同样的 `data/chunks.jsonl` 换成 OpenAI、DeepSeek、Qwen 或本地 embedding 模型生成的向量。

## 生成索引

先生成语料：

```bash
python3 scripts/build-corpus.py
```

再生成向量索引：

```bash
python3 scripts/build-vector-index.py
```

当前索引摘要：

```json
{
  "backend": "local-hashing",
  "chunkCount": 183,
  "dims": 768,
  "vectorShape": [183, 768]
}
```

## 搜索示例

```bash
python3 scripts/search-vector.py "jun-dd-web 为什么构建失败"
```

输出会包含：

- 相似度分数
- 来源标题
- 所属章节
- 来源文件路径
- 内容摘要

也可以输出 JSON：

```bash
python3 scripts/search-vector.py "jun-dd-web 为什么构建失败" --json
```

## 适合问什么

适合：

- `jun-dd-web 为什么构建失败`
- `哪些项目可以构建成功`
- `CETC 项目有什么风险`
- `Maven 环境怎么配置`
- `知识库有什么意义`
- `敏感配置在哪里`

不适合：

- 需要强推理的问题
- 需要最新网络信息的问题
- 语义非常绕、但没有关键词的问题

## 下一步升级方向

### 方案 A：OpenAI embedding

用 `data/chunks.jsonl` 调 embedding API，替换 `vectors.npy`。

优点：

- 语义检索质量更好
- 中文、英文、代码混合检索更稳

### 方案 B：本地 embedding 模型

用本地模型生成向量，例如 bge、Qwen embedding、nomic embedding 等。

优点：

- 离线
- 隐私更好

限制：

- 需要额外安装模型和依赖
- 首次配置成本更高

### 方案 C：接 Chroma / FAISS / LanceDB

当前 `vectors.npy + chunks.jsonl` 可以继续升级成标准向量数据库。

建议顺序：

1. 保留当前本地哈希索引作为零依赖 fallback。
2. 增加真正 embedding 模型。
3. 再接 Chroma / FAISS / LanceDB。

这样系统不会因为某个模型或数据库不可用而完全失效。
