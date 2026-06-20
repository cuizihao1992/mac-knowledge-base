---
title: CETC 删除前资产抽取清单
tags: [reference, code, cetc, archive, cleanup]
created: 2026-06-20
source: /Users/cuizihao/CETC/Project
related: [CETC 旧项目业务价值与架构判断, CETC Project 项目盘点]
---

# CETC 删除前资产抽取清单

## 目的

这份清单用于决定哪些旧项目可以删除、哪些应该归档、哪些要先保留。

原则：

- 不直接删除仍含业务线索的源码。
- 不把真实账号、密码、token、client_secret 原文复制到知识库。
- 先保留 README、依赖、页面/API/后端模块、配置风险位置。
- 如果一个项目只是模板或 demo，保留摘要后可以优先清理。

## 建议动作分级

| 动作 | 含义 |
| --- | --- |
| `保留` | 暂时不要删，先继续抽取页面、接口、组件或 GIS 能力 |
| `归档` | 可以从工作目录移走，但建议压缩备份或迁到外置盘 |
| `摘要后可删` | 保留 README/依赖/目录清单后，可以优先删除源码 |
| `先脱敏` | 发现配置、部署、账号口令或内网地址线索，归档前先人工复核 |

## 删除前通用检查

每个项目删除前至少确认：

1. README、`package.json`、`pom.xml` 已记录。
2. 前端 `router/`、`views/`、`pages/`、`modules/` 已抽取目录清单。
3. 前端 `api/` 已抽取文件清单。
4. 后端 `controller/`、`service/`、`mapper/` 已抽取模块清单。
5. `.env*`、`vue.config.js`、`config*.js/json`、`application.yml/properties` 已做脱敏记录。
6. 有设计稿、原型、Swagger、部署路径、二级目录说明时，已记录链接或脱敏摘要。

## 项目清单

| 项目 | 当前判断 | 删除前必须抽取 | 风险提示 | 建议动作 |
| --- | --- | --- | --- | --- |
| `cgpt2.0/city-manage-server` | 城管后端，业务价值高 | `pom.xml`、后端模块、Controller/Service/Mapper、配置摘要 | `application.yml` 需脱敏复核 | 保留到抽取完成，再归档 |
| `cgpt2.0/city-mange-ui-web` | 城管管理端，业务价值高 | README、路由、`src/api/`、`src/views/`、部署二级目录说明 | README 中出现部署环境和账号口令类信息，需先脱敏 | 先脱敏，归档 |
| `cgpt2.0/city-manage-h5` | 城管移动端/H5/小程序 | README、`pages/`、`api/`、HBuilderX 发布说明 | `config.service.js` 需脱敏复核 | 归档 |
| `cgpt2.0/e-city-big` | 城管大屏 | README、指标/图表链接、`views/`、路由 | 价值主要在指标和图表，不在旧 Vue 代码 | 摘要后可归档 |
| `xinfang/xinfang` | 信访完整后端 + 前端 | README、Java 多模块、`cetc-ui` 页面/API、配置摘要 | `.env*`、`application.yml/properties` 需脱敏 | 保留到抽取完成，再归档 |
| `xinfang/xinfang-web-admin` | 信访管理后台 | README、路由、`src/api/`、`src/views/`、权限/登录流程 | `.env*`、代理和内网 API 需脱敏 | 归档 |
| `xinfang/xinfang-web` | 信访移动/门户 | README、设计稿/原型链接、`pages/`、`modules/`、API | README 中有部署/账号线索，需脱敏 | 先脱敏，归档 |
| `gis/gis-map-sdk` | WebGIS SDK，复用价值高 | README、`src/layer`、`src/map`、`src/service`、debug 配置摘要 | 图层配置、token/内网服务需复核 | 保留 |
| `gis/gis-map-sdk-cesium` | 3D GIS SDK | README、`src/` 目录、Cesium 相关封装 | 配置线索较少，但需确认资源依赖 | 保留 |
| `gis/gis-map-develop-platform` | GIS 开发平台/示例 | README、`example2d/gis/config` 脱敏摘要、示例结构 | 多个 map/layer config 需脱敏 | 先脱敏，保留或归档 |
| `gis/gis-bigdata-etl` | GIS 空间大数据 ETL | README、脚本/配置目录、数据处理流程 | 需要确认是否有真实数据路径 | 归档 |
| `gis/gisopenplatform-admin` | GIS 开放平台后台 | README、`pom.xml`、多模块服务、坐标转换/地图 API 模块 | 后端配置和第三方 API 适配需复核 | 归档 |
| `gis/offline-map` | 离线地图示例/应用 | README、离线资源组织、路由/页面 | 旧 Vue 模板，业务独特性较弱 | 摘要后可删 |
| `gis/urban-virtual-reality-fusion-simulation-platform` | 城市仿真/GIS 前端 | README、路由、`views/`、环境变量 | `.env*` 需脱敏 | 归档 |
| `jun-dd-web` | CETC BI/GIS/可视化资产 | README、`src/components`、`src/modules`、`src/pages`、`src/common/api`、GIS 静态资源结构 | 内置 ArcGIS/Mapbox/GIS 资源和配置较多，直接删会丢资产 | 保留到抽取完成 |
| `cetc-ui/bi-ui` | BI/GIS 组件库 + VuePress 文档 | README、组件清单、`docs/`、`src/components`、GIS 配置 | 文档站和组件清单比旧构建更有价值 | 保留到抽取完成 |
| `cetc-ui/compass-ui-demo` | 组件 demo | README、`package.json`、demo 页面 | 业务独特性弱 | 摘要后可删 |
| `smartCity/java` | 智慧城市后端 | `pom.xml`、Controller/Service/Mapper、配置摘要 | `app.properties`、`application.yml` 需脱敏 | 归档 |
| `smartCity/managerweb` | vue-element-admin 改造后台 | README、路由、页面清单 | 模板成分重，业务价值偏低 | 摘要后可删 |
| `smartCity/wepy` | 小程序/移动端 | `package.json`、`src/pages`、`src/api` | 需确认是否有真实接口配置 | 归档 |
| `BeijingDaxing/cetc-moniwa-ui` | 大兴监测预警 UI | `package.json`、`pom.xml`、`src/pages`、`src/api`、SSO/GIS 配置摘要 | `static/js/config.js`、地图配置需脱敏 | 先脱敏，归档 |
| `brain` | 监测/农业数据字典和大屏 | README、数据字典、`src/pages`、`src/common/api` | 有内网接口文档链接，需脱敏 | 归档 |
| `industry-chain` | 综合信息资源中心/可视化 | README、组件/页面清单 | 业务线索较少，旧 Vue 资产 | 摘要后可删 |
| `1.2-project-network-security-java` | 网络安全后端 | `pom.xml`、网络安全模块 Controller/Service/Mapper | 后端模块多，价值在模块名和数据模型 | 归档 |
| `1.2-project-network-security-web` | 网络安全前端/大屏 | README、`src/views/big`、`src/api`、路由 | 大屏页面包含安全态势、威胁、处置等业务 | 归档 |

## 第一批可清理候选

这些项目业务独特性较弱，适合作为第一批清理对象。建议先保留摘要，然后移动或删除：

| 项目 | 保留内容 |
| --- | --- |
| `cetc-ui/compass-ui-demo` | README、`package.json`、demo 目录清单 |
| `smartCity/managerweb` | README、路由/页面清单、模板改造说明 |
| `industry-chain` | README、页面/组件清单 |
| `gis/offline-map` | README、离线地图资源组织说明 |

## 先不要删的目录

这些目录建议先留着，直到完成更细资产抽取：

- `cgpt2.0/`
- `xinfang/`
- `jun-dd-web`
- `cetc-ui/bi-ui`
- `gis/gis-map-sdk`
- `gis/gis-map-sdk-cesium`
- `gis/gis-map-develop-platform`

原因：它们分别承载城市治理、信访、BI/GIS/SDK 这些最有复用价值的信息。

## 脱敏优先项

删除或归档前，优先人工复核这些配置：

| 项目 | 配置线索 |
| --- | --- |
| `cgpt2.0/city-mange-ui-web` | README 部署说明、`vue.config.js`、规则引擎配置 |
| `xinfang/xinfang-web` | README、`.env*`、`src/config.js` |
| `xinfang/xinfang-web-admin` | `.env*`、`vue.config.js`、系统配置 API |
| `xinfang/xinfang` | Java `application.yml/properties`、前端 `.env*` |
| `BeijingDaxing/cetc-moniwa-ui` | `static/js/config.js`、debug 地图配置 |
| `gis/gis-map-develop-platform` | `example2d/gis/config/*.json` |
| `gis/gis-map-sdk` | `debug/config/*.json` |
| `smartCity/java` | `app.properties`、`application.yml` |

## 已观察到的架构资产

### 网络安全

`1.2-project-network-security-java` 和 `1.2-project-network-security-web` 包含网络安全业务模块：

- 全网漏洞/威胁：`allNet`
- 公共安全：`publicSafety`
- 安全处置：`safeDisposal`
- 安全底图：`securityBasemap`
- 安全策略：`securityStrategy`
- 威胁态势：`threaten`

这些模块值得保留为业务名词和页面/接口参考。

### 城市治理

`cgpt2.0` 是一套比较完整的城管业务链：

- Java 后端：`city-manage-server`
- 管理端：`city-mange-ui-web`
- 移动端/H5/小程序：`city-manage-h5`
- 数据大屏：`e-city-big`

删除前应至少保留管理端页面、移动端页面、后端模块和大屏指标。

### 信访

`xinfang` 目录是一套完整系统：

- Java/RuoYi 风格后端
- 管理后台
- 移动/门户前端
- 生成器、系统模块、定时任务模块

这类项目不建议直接删，除非已经抽取业务流程、接口和页面结构。

### GIS / BI

GIS 和 BI 是这批项目里最容易复用的技术资产：

- `gis-map-sdk`：地图 SDK 和图层抽象。
- `gis-map-sdk-cesium`：3D 地图能力。
- `gis-map-develop-platform`：地图开发平台和配置示例。
- `jun-dd-web`：BI/GIS 可视化应用和组件组合。
- `cetc-ui/bi-ui`：组件库和文档站。

这些建议先归为 `keep`，等抽完组件和 SDK 能力后再决定是否移走源码。

## 推荐下一步

下一步可以做一个自动脚本，把这些项目的目录清单输出为机器可读文件：

```text
outputs/cetc-asset-extraction.json
outputs/cetc-asset-extraction.md
```

这样后面真正清理目录时，可以按 `摘要后可删`、`归档`、`保留` 三类执行。
