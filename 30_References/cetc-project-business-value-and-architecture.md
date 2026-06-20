---
title: CETC 旧项目业务价值与架构判断
tags: [reference, code, cetc, architecture, archive]
created: 2026-06-20
source: /Users/cuizihao/CETC/Project
related: [CETC Project 项目盘点, CETC 项目健康度报告]
---

# CETC 旧项目业务价值与架构判断

## 结论

这些项目大多数技术栈已经过时，不建议继续当作新项目底座投入。

但它们不等于“没用”。真正价值主要在：

- 业务流程：城管、信访、GIS、监测预警、综合信息资源、网络安全等业务模块。
- 页面和功能清单：路由、菜单、页面、表单、图表、大屏、移动端页面。
- 接口和数据模型：`api/`、`controller/`、`service/`、`mapper/`、Swagger/接口说明。
- GIS 和可视化资产：地图 SDK、图层配置、ArcGIS/Mapbox/Cesium 接入方式。
- 风险证据：内网地址、部署说明、疑似账号口令、旧依赖和不可复现环境。

我的判断：

```text
不要继续精修大多数旧项目。
先把业务结构、页面清单、接口线索、敏感配置线索归档。
归档完成后，再删除源码目录会更稳。
```

## 总体架构分组

| 架构组 | 包含项目 | 业务价值 | 技术状态 | 建议 |
| --- | --- | --- | --- | --- |
| 城市治理 / CGPT 2.0 | `cgpt2.0/city-manage-server`, `city-mange-ui-web`, `city-manage-h5`, `e-city-big` | 高 | Java + Vue 2 + UniApp + 大屏 | 保留业务说明和接口/页面清单，源码可归档 |
| 信访系统 | `xinfang/xinfang`, `xinfang-web`, `xinfang-web-admin` | 高 | RuoYi/Java + Vue 2 + Element UI | 保留业务模型和后台/H5/管理端结构，源码归档前脱敏 |
| GIS 平台 | `gis/*`, `cetc-ui/bi-ui`, `jun-dd-web` | 高 | Mapbox/ArcGIS/Cesium + Vue 2 + SDK | 保留 SDK、图层配置、地图接入方式；业务应用按价值归档 |
| 智慧城市 / SmartCity | `smartCity/java`, `managerweb`, `wepy` | 中 | Spring Boot + Vue Element Admin + 小程序 | 保留接口和模板改造痕迹，源码可低优先归档 |
| 监测预警 | `BeijingDaxing/cetc-moniwa-ui`, `brain` | 中 | Vue 2 + ECharts + GIS + 旧 Webpack | 保留数据字典、监测分类、页面结构 |
| 网络安全 | `1.2-project-network-security-java`, `1.2-project-network-security-web` | 中 | JEECG/cityIE + Ant Design Vue | 保留后端模块结构和安全业务页面 |
| 组件/示例 | `cetc-ui/compass-ui-demo`, `industry-chain` | 低到中 | Vue 2 组件/示例 | 只保留可复用组件清单和截图/说明 |

## 删除前必须保留什么

删除源码前，至少保留这些信息：

1. 每个项目的 README、`package.json`、`pom.xml`。
2. 前端 `router/`、`views/`、`pages/`、`modules/` 目录清单。
3. 后端 `controller/`、`service/`、`mapper/`、`entity/domain` 目录清单。
4. `api/` 目录和接口封装文件名。
5. `.env*`、`config*`、`application.yml/properties` 的脱敏摘要。
6. 有价值页面截图或设计稿链接。
7. 部署路径、二级目录、代理路径、内网服务依赖的脱敏摘要。

不要直接把包含账号、密码、token、client_secret 的原文复制到知识库。只记录“哪里有、是什么类型、是否需要轮换/删除”。

## 项目级判断

| 项目 | 业务价值 | 架构/技术 | 保留价值 | 删除建议 |
| --- | --- | --- | --- | --- |
| `cgpt2.0/city-manage-server` | 高 | Java/Maven，疑似 JEECG/Boot 后端 | 城市治理后端接口、模块、权限、数据模型 | 先抽取后端模块和接口摘要，再归档源码 |
| `cgpt2.0/city-mange-ui-web` | 高 | Vue + JEECG Boot + Ant Design Vue/Element UI | 管理端页面、权限、菜单、部署路径说明 | 保留页面/菜单清单，源码可归档 |
| `cgpt2.0/city-manage-h5` | 高 | UniApp/HBuilderX，移动端/H5/小程序 | 移动端业务流程、多端发布方式 | 保留页面清单和发布说明，源码可归档 |
| `cgpt2.0/e-city-big` | 中高 | Vue 2 + ECharts 5 大屏 | 城管大屏指标、图表方案、可视化参考 | 保留截图/指标/图表链接，源码可归档 |
| `xinfang/xinfang` | 高 | RuoYi 风格 Java 多模块 + 前端 | 信访业务后端、生成器、系统/权限/定时任务 | 保留模块、表、接口摘要后归档 |
| `xinfang/xinfang-web-admin` | 高 | Vue 2 + Element UI 管理后台 | 分析预警系统管理端页面和接口 | 保留路由/API/页面清单，源码可归档 |
| `xinfang/xinfang-web` | 中高 | Vue/H5 | 信访移动端/门户流程、设计稿链接 | 保留页面和设计链接，清理敏感说明后归档 |
| `gis/gis-map-sdk` | 高 | WebGIS SDK，Webpack，地图服务层 | 可复用地图 SDK、图层/服务抽象 | 不建议直接删，先单独归档为 GIS 资产 |
| `gis/gis-map-sdk-cesium` | 高 | 3D GIS/Cesium SDK | 三维地图接入参考 | 不建议直接删，先归档 README 和源码结构 |
| `gis/gis-map-develop-platform` | 高 | GIS 开发平台/示例 | 平台示例、图层配置、地图能力展示 | 脱敏后保留配置摘要，源码可归档 |
| `gis/gis-bigdata-etl` | 中高 | GIS 空间大数据 ETL | 空间数据处理流程线索 | 保留说明和脚本/配置目录，再判断删除 |
| `gis/gisopenplatform-admin` | 中高 | Spring Boot + 多模块 | GIS 开放平台后台、坐标转换、高德/腾讯 API 适配 | 保留模块说明，源码可归档 |
| `gis/offline-map` | 中 | Vue 2 离线地图 | 离线地图部署和资源组织方式 | 保留离线地图资源说明，源码可归档 |
| `gis/urban-virtual-reality-fusion-simulation-platform` | 中 | Vue 2 GIS/仿真平台 | 城市虚拟现实融合仿真页面参考 | 保留页面结构，源码可归档 |
| `jun-dd-web` | 高 | CETC BI，可视化/GIS/拖拽组件 | BI 可视化页面、组件组合、GIS 静态资源组织 | 不建议直接删，先抽页面/组件/API 清单 |
| `cetc-ui/bi-ui` | 中高 | 组件库 + VuePress 文档 + GIS/BI 组件 | 组件库、示例、文档站结构 | 保留组件清单和文档，源码可归档 |
| `cetc-ui/compass-ui-demo` | 低中 | Vue CLI demo | 组件 demo、Codemirror/GIS 示例 | 保留 demo 说明即可 |
| `smartCity/java` | 中 | Spring Boot 后端 | 统一平台接口、Swagger、MyBatis 结构 | 保留接口/配置摘要，源码可归档 |
| `smartCity/managerweb` | 低中 | vue-element-admin 模板改造 | 后台模板改造痕迹、菜单/页面 | 若业务改造少，保留摘要后可删 |
| `smartCity/wepy` | 中 | 小程序/移动端 | 移动端页面和接口 | 保留页面/API 清单，源码可归档 |
| `BeijingDaxing/cetc-moniwa-ui` | 中高 | Vue 2 + ECharts + GIS + Maven 包装构建 | 大兴监测预警页面、SSO/地图/API 运行结构 | 保留运行配置摘要和页面结构后归档 |
| `brain` | 中 | Vue 2 + ECharts + 农业/监测数据字典 | 数据字典、监测地图分类、大屏页面 | 保留数据字典和页面清单，源码可归档 |
| `industry-chain` | 低中 | Vue 2 综合信息资源中心 | 可视化组件和页面参考 | 保留页面/组件清单即可 |
| `1.2-project-network-security-java` | 中 | Spring Boot/JEECG 风格后端 | 网络安全后端模块、安全/权限/生成器结构 | 保留模块和接口摘要，源码可归档 |
| `1.2-project-network-security-web` | 中 | Ant Design Vue/cityIE 前端 | 网络安全管理端页面 | 保留页面/路由清单，源码可归档 |

## 删除优先级

### 第一批：可以先删但建议保留摘要

这些更像模板、demo 或重复实现，业务独特性较弱：

- `cetc-ui/compass-ui-demo`
- `smartCity/managerweb`
- `industry-chain`
- `gis/offline-map`

删除前保留 README、依赖、路由/页面清单即可。

### 第二批：可归档，不建议直接删

这些有业务或架构线索，但旧技术维护价值不高：

- `brain`
- `BeijingDaxing/cetc-moniwa-ui`
- `smartCity/java`
- `smartCity/wepy`
- `1.2-project-network-security-java`
- `1.2-project-network-security-web`
- `gis/urban-virtual-reality-fusion-simulation-platform`
- `gis/gisopenplatform-admin`
- `gis/gis-bigdata-etl`

建议压缩归档或迁到外置硬盘/云盘，再从工作目录删除。

### 第三批：先不要删，先做资产抽取

这些最可能有复用价值：

- `cgpt2.0/*`
- `xinfang/*`
- `jun-dd-web`
- `cetc-ui/bi-ui`
- `gis/gis-map-sdk`
- `gis/gis-map-sdk-cesium`
- `gis/gis-map-develop-platform`

它们的价值不是旧代码，而是业务、页面、接口、GIS 能力和可视化组件。

## 资产抽取建议

下一步如果要为删除做准备，建议先生成这些清单：

```text
项目 -> README 摘要
项目 -> 路由/页面清单
项目 -> API 文件清单
项目 -> 后端 Controller/Service/Mapper 清单
项目 -> 配置/敏感线索清单
项目 -> 可删除/需归档/需保留判断
```

抽取完成后，可以把源码目录分成：

```text
keep/
archive/
delete-after-archive/
```

我的建议是：先不要直接删 `cgpt2.0`、`xinfang`、`gis-map-sdk`、`jun-dd-web`、`bi-ui`。它们是业务和 GIS/BI 能力最集中的部分。
