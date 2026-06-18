---
title: CETC 重点项目运行手册
tags: [reference, code, cetc, runbook]
created: 2026-06-18
source: /Users/cuizihao/CETC/Project
related: [CETC 项目健康度报告, CETC Project 项目盘点]
---

# CETC 重点项目运行手册

## 说明

本手册优先整理健康度报告里的 D 级项目。当前覆盖：

- `~/CETC/Project/xinfang/xinfang-web-admin`
- `~/CETC/Project/cetc-ui/bi-ui`

只做静态分析，未安装依赖、未实际启动项目。

## xinfang-web-admin

### 基本定位

- 路径：`~/CETC/Project/xinfang/xinfang-web-admin`
- 类型：分析预警系统管理后台
- 来源模板：RuoYi-Vue
- 技术栈：Vue 2.6.10、Vue CLI 4.4、Element UI 2.13、ECharts 4、Axios 0.18
- 健康度问题：缺前端 lockfile、存在环境配置、存在构建产物、旧前端依赖、疑似敏感配置线索

### 关键目录

| 路径 | 作用 |
| --- | --- |
| `src/main.js` | 应用入口 |
| `src/router/index.js` | 路由配置 |
| `src/store/` | Vuex 状态 |
| `src/api/` | API 模块 |
| `src/utils/request.js` | Axios 实例、token 注入、响应拦截 |
| `src/settings.js` | 后台标题和布局配置 |
| `vue.config.js` | Vue CLI、代理、构建配置 |
| `.env.development` | 开发环境变量 |
| `.env.production` | 生产环境变量 |
| `.env.staging` | 测试环境变量 |

### 启动方式

```bash
cd /Users/cuizihao/CETC/Project/xinfang/xinfang-web-admin
npm install
npm run dev
```

README 里说明浏览器访问：

```text
http://localhost:80
```

`vue.config.js` 中端口逻辑：

```text
process.env.port || process.env.npm_config_port || 80
```

如果 80 端口权限或占用有问题，可用：

```bash
npm run dev -- --port 8080
```

### 构建方式

```bash
npm run build:stage
npm run build:prod
```

构建输出：

```text
dist/
```

静态资源目录：

```text
dist/static/
```

部署路径固定为：

```text
/admin
```

### 接口配置

环境变量：

| 环境 | VUE_APP_BASE_API |
| --- | --- |
| development | `/cetc/api` |
| staging | `/stage-api` |
| production | 空字符串 |

开发代理在 `vue.config.js`：

```text
/cetc/api -> http://10.0.13.68:8080
```

Axios 基础地址在 `src/utils/request.js`：

```text
baseURL: process.env.VUE_APP_BASE_API
```

请求 token 头：

```text
Authorization: Bearer <token>
```

### 主要风险

- 依赖较旧：Vue 2、Element UI、Axios 0.18、Vue CLI 4。
- 未发现前端 lockfile，重新安装依赖可能产生不可复现结果。
- 生产环境 `VUE_APP_BASE_API` 为空，依赖部署路径或后端同源配置。
- 开发代理写死内网地址 `10.0.13.68:8080`。
- 项目中有 `.env.*`，需要确认是否包含真实生产配置。

### 建议处理顺序

1. 补齐 lockfile：在可运行 Node 版本下生成 `package-lock.json` 或 `pnpm-lock.yaml`。
2. 明确推荐 Node 版本，建议先从 Node 12/14 试起。
3. 把 `10.0.13.68:8080` 改为通过环境变量配置。
4. 写一份最小启动说明，记录后端依赖、账号、接口路径。
5. 如果继续维护，规划 Vue 2/Element UI 迁移或至少冻结依赖。

## bi-ui

### 基本定位

- 路径：`~/CETC/Project/cetc-ui/bi-ui`
- 类型：CETC BI / COMPASS-UI 组件库和示例工程
- 技术栈：Vue 2、Webpack 4、VuePress 1、Element UI、ECharts、Mapbox GL、ArcGIS JS API 外部资源
- 健康度问题：缺本地启动脚本、缺前端 lockfile、存在环境配置、存在构建产物、旧前端依赖、疑似敏感配置线索

### 关键目录

| 路径 | 作用 |
| --- | --- |
| `src/components/` | 组件库源码 |
| `src/pages/` | 示例/页面 |
| `src/router/` | 示例路由 |
| `src/store/` | 示例状态管理 |
| `src/common/api/` | 通用 API |
| `src/common/request/` | 请求封装 |
| `src/config.js` | 外部静态资源地址 |
| `build/` | Webpack 构建配置 |
| `docs/` | VuePress 文档 |
| `docs/.vuepress/config.js` | 文档站配置 |

### 脚本现状

`package.json` 中存在：

```text
docs:dev
docs:build
demo:dev
demo:build
lint
pack
build:prd
```

README 写的是：

```bash
npm run dev
npm run build
```

但 `package.json` 里没有 `dev` 和 `build` 脚本。这是当前最大启动坑。

### 推荐启动方式

启动文档站：

```bash
cd /Users/cuizihao/CETC/Project/cetc-ui/bi-ui
npm install
npm run docs:dev
```

启动示例工程：

```bash
npm run demo:dev
```

打包组件库：

```bash
npm run pack
```

构建文档：

```bash
npm run docs:build
```

### 外部资源配置

`src/config.js` 写死了资源根地址：

```text
http://10.0.14.49
```

依赖的外部资源包括：

- ArcGIS JS API 4.13
- GIS CSS/JS
- ECharts layer
- Tinymce
- Ace
- HT 相关脚本

如果不在对应内网环境，GIS/编辑器/HT 相关组件大概率加载失败。

### 构建产物

组件库主入口：

```text
lib/compass-ui.common.js
```

发布文件范围包含：

```text
build/
dist/
src/
README.md
```

### 主要风险

- README 启动命令与实际 scripts 不一致。
- 未发现 lockfile，依赖安装不可复现。
- Webpack 4、Vue 2、Element UI、VuePress 1 都偏旧。
- 依赖里有 `emmet` GitHub 源，离线或网络不通时安装可能失败。
- 外部资源地址硬编码为 `10.0.14.49`。
- `src/config.js` 是运行关键配置，迁移环境必须先处理。

### 建议处理顺序

1. 修正 README，把 `npm run dev/build` 改成 `docs:dev`、`demo:dev`、`pack`、`docs:build`。
2. 明确项目到底是“组件库优先”还是“示例工程优先”。
3. 把 `src/config.js` 的 `BaseUrl` 改为环境变量或独立配置文件。
4. 生成 lockfile，并记录可用 Node/npm 版本。
5. 如果要继续维护组件库，先补最小示例和组件清单。

## 共同建议

这两个项目都是典型旧 Vue 2 体系。短期目标不应马上升级，而是先做到：

1. 可复现安装。
2. 可本地启动。
3. 配置外置。
4. README 与真实脚本一致。
5. 明确后端和外部静态资源依赖。
