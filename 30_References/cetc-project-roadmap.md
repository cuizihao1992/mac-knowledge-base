---
title: CETC 项目整理路线图
tags: [reference, code, cetc, roadmap]
created: 2026-06-19
source: /Users/cuizihao/CETC/Project
related: [CETC 项目健康度报告, CETC 重点项目运行手册, CETC Project 项目盘点]
---

# CETC 项目整理路线图

## 目标

把 `/Users/cuizihao/CETC/Project/` 下的历史项目从“能看到目录”整理到“知道价值、能复现、能交接、能维护”。

当前基础资料：

- `CETC Project 项目盘点`：25 个 git 项目，按用途和技术栈归类。
- `CETC 项目健康度报告`：A/B/C/D 健康度、风险和高频问题。
- `CETC 重点项目运行手册`：已覆盖 4 个 D 级项目。

## 总体判断

- 项目群以 Vue 2、Webpack 3/4、Element UI、ECharts、GIS/地图能力为主。
- 最大维护风险不是代码复杂度，而是环境不可复现：缺 lockfile、旧 Node/npm、内网资源写死、README 与实际脚本不一致。
- 多数风险应先“冻结和记录”，不应马上升级重构。

## 阶段 1：风险止血

优先级：最高

目标：确认有没有真实敏感信息、生产地址、不可公开配置。

范围：

| 项目 | 重点检查 |
| --- | --- |
| `gis/gis-map-develop-platform` | `token.js`、地图配置 JSON、SDK 示例 |
| `BeijingDaxing/cetc-moniwa-ui` | `static/js/config.js` 中 SSO、`client_secret`、API 地址 |
| `smartCity/java` | `application.yml`、`app.properties` |
| `xinfang/xinfang-web-admin` | `.env.*`、登录/API 模块 |
| `cetc-ui/bi-ui` | `src/config.js`、GIS 静态资源地址 |
| `jun-dd-web` | `src/config.js`、外部 `/static` 依赖 |

产出：

- 一份“敏感配置复核清单”。
- 明确哪些值是公开前端配置，哪些需要迁出。
- 对真实密钥或生产凭据做轮换计划。

## 阶段 2：运行环境复现

优先级：高

目标：让重点项目能在本机或指定机器上稳定安装和启动。

首批项目：

| 项目 | 原因 | 推荐动作 |
| --- | --- | --- |
| `xinfang/xinfang-web-admin` | 后台管理项目，脚本清晰但缺 lockfile | 确认 Node 12/14，生成 lockfile，验证 `npm run dev` |
| `cetc-ui/bi-ui` | 组件库/示例工程，README 与 scripts 不一致 | 修 README，验证 `docs:dev` 和 `demo:dev` |
| `jun-dd-web` | BI 前端，构建链路包含 pack/compress/tar | 确认 `/static` 资源，验证 `dev` 和 `build:prd` |
| `BeijingDaxing/cetc-moniwa-ui` | Maven 指定 Node 8.9.4/npm 5.6.0 | 用 Maven 或 nvm 复现 Node 8 构建 |

产出：

- 每个项目补一份最小 README 或运行手册。
- 记录 Node/npm 版本。
- 记录依赖安装命令。
- 记录启动端口、后端/API、外部静态资源。
- 能生成 lockfile 的项目先生成 lockfile。

## 阶段 3：按业务线归档

优先级：中

目标：把项目按业务线串起来，减少“散落项目名”的认知成本。

建议分组：

| 业务线 | 项目 |
| --- | --- |
| 网络安全 | `1.2-project-network-security-java`、`1.2-project-network-security-web` |
| CGPT / E-City | `city-manage-h5`、`city-manage-server`、`city-mange-ui-web`、`e-city-big` |
| GIS 平台 | `gis-map-sdk`、`gis-map-sdk-cesium`、`gis-map-develop-platform`、`gisopenplatform-admin`、`offline-map`、`urban-virtual-reality-fusion-simulation-platform`、`gis-bigdata-etl` |
| 智慧城市 | `smartCity/java`、`smartCity/managerweb`、`smartCity/wepy` |
| 信访系统 | `xinfang`、`xinfang-web`、`xinfang-web-admin` |
| BI / 组件 | `cetc-ui/bi-ui`、`cetc-ui/compass-ui-demo`、`jun-dd-web`、`industry-chain` |
| 大兴监测预警 | `BeijingDaxing/cetc-moniwa-ui` |

产出：

- 一篇“业务线关系图”文档。
- 每条业务线标出前端、后端、大屏、SDK、移动端的关系。
- 明确哪些项目是核心业务，哪些只是示例、组件或历史归档。

## 阶段 4：维护策略

优先级：中低

目标：决定哪些项目保留维护，哪些只归档。

建议策略：

| 类型 | 策略 |
| --- | --- |
| 仍可能运行的生产/演示项目 | 先冻结依赖、补 README、保留可复现启动方式 |
| SDK/组件库 | 补组件清单和最小示例，确认是否还有复用价值 |
| 老 Vue 2 管理后台 | 先记录运行环境，不急着升级 |
| 无后端/无资源无法运行的前端 | 标记为“需环境依赖”，不投入重构 |
| 下载/归档性质项目 | 只保留索引，不做运行手册 |

## 当前已完成

- 已生成全局代码项目盘点。
- 已生成 CETC 项目盘点。
- 已生成 CETC 项目健康度报告。
- 已完成 4 个 D 级项目运行手册：
  - `xinfang/xinfang-web-admin`
  - `cetc-ui/bi-ui`
  - `jun-dd-web`
  - `BeijingDaxing/cetc-moniwa-ui`

## 下一步建议

下一步做“敏感配置复核清单”。

原因：

- 健康度报告里 `疑似敏感配置线索` 命中 19 个项目。
- 其中有些只是变量名或登录模块，但也有 `token.js`、`client_secret`、内网 API、SSO 地址等需要人工确认。
- 在没有复核前，不适合大规模公开或迁移这些配置。

建议优先复核顺序：

1. `gis/gis-map-develop-platform`
2. `BeijingDaxing/cetc-moniwa-ui`
3. `smartCity/java`
4. `xinfang/xinfang-web-admin`
5. `cetc-ui/bi-ui`
6. `jun-dd-web`
