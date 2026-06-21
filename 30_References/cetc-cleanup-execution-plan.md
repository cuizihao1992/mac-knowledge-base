---
title: CETC 清理执行计划
tags: [reference, code, cetc, cleanup, archive]
created: 2026-06-21
source: /Users/cuizihao/CETC/Project
related: [CETC 自动资产抽取报告, CETC 删除前资产抽取清单]
---

# CETC 清理执行计划

## 当前阶段

现在已经从“分析阶段”进入“清理准备完成，可以开始执行”的阶段。

已经完成：

- 25 个 CETC 项目自动资产抽取。
- 每个项目已有 README、页面/API/后端样本、配置线索、敏感关键词线索。
- 自动报告已同步到网站、AI 语料和向量索引。
- 现在可以按批次执行移动、压缩归档或后续脱敏。

还没有做：

- 没有删除任何源项目目录。
- 没有移动任何 CETC 项目。
- 没有压缩归档实际源码。

## 总体策略

清理顺序不要从高价值项目开始，而是从“摘要后可删”的低风险项目开始。

推荐顺序：

```text
第一批：摘要后可删
第二批：普通归档
第三批：先脱敏后归档
第四批：继续保留和深抽取
```

## 第一批：摘要后可删

这些项目业务独特性较弱，自动报告已经保留了 README、依赖、页面/API/配置线索。

| 项目 | 建议动作 | 删除前确认 |
| --- | --- | --- |
| `cetc-ui/compass-ui-demo` | 摘要后可删 | README、`package.json`、demo 结构已在报告中 |
| `smartCity/managerweb` | 摘要后可删 | 模板成分较重，保留页面/路由摘要即可 |
| `industry-chain` | 摘要后可删 | 保留页面/组件清单即可 |
| `gis/offline-map` | 摘要后可删 | 保留离线地图资源组织说明即可 |

建议执行方式：

```text
先移动到归档目录，而不是直接 rm 删除。
观察 1-2 周确认没有再用，再删除归档副本。
```

建议目标目录：

```text
/Users/cuizihao/CETC/Archive/delete-after-review/
```

验收条件：

- 这 4 个项目不再出现在 `/Users/cuizihao/CETC/Project/` 工作区。
- 知识库仍可查询这些项目的摘要。
- 如果要恢复，可以从归档目录找回。

## 第二批：普通归档

这些项目还有业务或架构价值，但不建议继续放在主工作区里日常维护。

| 项目 | 业务价值 | 建议动作 |
| --- | --- | --- |
| `1.2-project-network-security-java` | 网络安全后端 | 归档 |
| `1.2-project-network-security-web` | 网络安全前端/大屏 | 归档 |
| `brain` | 监测/农业数据字典和大屏 | 归档 |
| `gis/gis-bigdata-etl` | GIS 空间大数据 ETL | 归档 |
| `gis/gisopenplatform-admin` | GIS 开放平台后台 | 归档 |
| `gis/urban-virtual-reality-fusion-simulation-platform` | 城市仿真/GIS 前端 | 归档 |
| `smartCity/java` | 智慧城市后端 | 归档 |
| `smartCity/wepy` | 小程序/移动端 | 归档 |

建议目标目录：

```text
/Users/cuizihao/CETC/Archive/source-archive/
```

验收条件：

- 源码仍在归档目录。
- 知识库里保留项目快照。
- 主工作区减少噪音。

## 第三批：先脱敏后归档

这些项目不能直接公开或轻易移动，因为报告里有较多配置/敏感关键词线索。

| 项目 | 原因 | 建议动作 |
| --- | --- | --- |
| `BeijingDaxing/cetc-moniwa-ui` | SSO、地图配置、系统配置线索较多 | 先脱敏后归档 |
| `cgpt2.0/city-mange-ui-web` | README 部署说明、规则引擎配置、敏感线索较多 | 先脱敏后归档 |
| `xinfang/xinfang-web` | README、`.env*`、配置和账号线索 | 先脱敏后归档 |

脱敏前不要做：

- 不要推到公开仓库。
- 不要直接分享压缩包。
- 不要把配置原文复制到知识库。

脱敏时只记录：

```text
哪个文件有风险
风险类型是什么
是否需要轮换或删除
```

## 第四批：继续保留和深抽取

这些项目是最有资产价值的部分，先不要删。

| 项目 | 保留原因 | 下一步 |
| --- | --- | --- |
| `jun-dd-web` | BI/GIS/可视化组件和静态 GIS 资源集中 | 抽取组件、页面、API、GIS 静态资源结构 |
| `cetc-ui/bi-ui` | BI/GIS 组件库和 VuePress 文档站 | 抽取组件清单和文档结构 |
| `gis/gis-map-sdk` | WebGIS SDK 和图层抽象 | 单独整理成 GIS SDK 资产 |
| `gis/gis-map-sdk-cesium` | 3D GIS/Cesium 能力 | 保留 3D 地图能力说明 |
| `gis/gis-map-develop-platform` | GIS 开发平台和地图配置示例 | 先脱敏后保留 |
| `cgpt2.0/city-manage-h5` | 城管移动端/H5/小程序 | 抽取页面和发布流程 |
| `cgpt2.0/city-manage-server` | 城管后端 | 抽取后端模块和接口 |
| `cgpt2.0/e-city-big` | 城管大屏 | 抽取指标和图表方案 |
| `xinfang/xinfang` | 完整信访后端和前端 | 抽取业务模型和模块结构 |
| `xinfang/xinfang-web-admin` | 信访管理端 | 抽取页面、API、权限结构 |

这批不是永远不能删，而是要等下一轮更细资产抽取完成后再决定。

## 建议执行命令形态

为了安全，下一步不建议直接执行 `rm -rf`。

推荐先做移动归档：

```bash
mkdir -p /Users/cuizihao/CETC/Archive/delete-after-review
mkdir -p /Users/cuizihao/CETC/Archive/source-archive
```

第一批移动示例：

```bash
mv /Users/cuizihao/CETC/Project/cetc-ui/compass-ui-demo /Users/cuizihao/CETC/Archive/delete-after-review/
mv /Users/cuizihao/CETC/Project/smartCity/managerweb /Users/cuizihao/CETC/Archive/delete-after-review/
mv /Users/cuizihao/CETC/Project/industry-chain /Users/cuizihao/CETC/Archive/delete-after-review/
mv /Users/cuizihao/CETC/Project/gis/offline-map /Users/cuizihao/CETC/Archive/delete-after-review/
```

移动后重新运行：

```bash
python3 scripts/extract-cetc-assets.py
python3 scripts/build-site.py
python3 scripts/build-corpus.py
python3 scripts/build-vector-index.py
```

## 是否已经接近完成

第一阶段还剩 3 步：

1. 执行第一批低价值项目移动归档。
2. 重新扫描并更新知识库，确认项目数量变化。
3. 对高价值项目做一轮更细抽取。

完成这 3 步后，第一阶段就可以算完成。

长期系统还剩 6-8 步，主要是接 DeepSeek 真问答、做定期更新脚本、把高价值项目拆成更细知识资产。

## 下一步建议

下一步建议执行“第一批移动归档”，但需要你明确同意，因为这会改变 `/Users/cuizihao/CETC/Project/` 里的目录位置。

如果暂时不想动文件，就先做一个只输出命令、不执行的脚本：

```text
scripts/plan-cetc-cleanup.py
```

它负责生成待执行命令，等你确认后再真正移动。
