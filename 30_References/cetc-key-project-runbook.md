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
- `~/CETC/Project/jun-dd-web`
- `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui`

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

## jun-dd-web

### 基本定位

- 路径：`~/CETC/Project/jun-dd-web`
- 类型：CETC BI 可视化/组件化前端
- 技术栈：Vue 2、Webpack 4、Element UI、ECharts、Mapbox GL、ArcGIS 外部资源、视频/图表/拖拽组件
- 健康度问题：缺前端 lockfile、存在环境配置、存在构建产物、旧前端依赖、疑似敏感配置线索

### 关键目录

| 路径 | 作用 |
| --- | --- |
| `src/main.js` | 应用入口 |
| `src/router/` | 页面和模块路由 |
| `src/store/` | GIS、页面、数据集等状态模块 |
| `src/common/api/` | 通用 API 模块 |
| `src/components/` | 图表、弹窗、时间轴等组件 |
| `src/modules/` | 业务/表单设计模块 |
| `src/config.js` | GIS、Tinymce、Ace、HT 等外部资源映射 |
| `build/webpack.config.js` | Webpack 构建配置 |
| `build/tar.js` | 构建后打包脚本 |
| `build/compressing.js` | 压缩脚本 |

### 启动方式

```bash
cd /Users/cuizihao/CETC/Project/jun-dd-web
npm install
npm run dev
```

### 构建方式

普通构建：

```bash
npm run build
```

完整生产构建：

```bash
npm run build:prd
```

`build:prd` 会依次执行：

```text
pack -> compress -> build
```

其中 `build` 会清理 `src/dist`，执行 Webpack 构建，然后运行 `build/tar.js`。

### 外部资源配置

`src/config.js` 当前使用：

```text
BaseUrl = /static
```

历史注释里有内网地址：

```text
http://10.0.14.49
```

依赖的外部资源包括：

- GIS CSS/JS
- ArcGIS JS API 4.13
- ECharts layer
- Tinymce
- Ace
- HT 相关脚本

部署时必须保证 `/static/js/...` 下这些资源存在，否则 GIS、编辑器、HT 组件会加载失败。

### 主要风险

- 未发现 lockfile，依赖安装不可复现。
- Vue 2、Webpack 4、Element UI、ECharts 4 体系偏旧。
- `emmet` 依赖来自 GitHub，离线或网络受限时安装可能失败。
- 构建链路包含自定义压缩和 tar 打包，不能只看 Webpack 输出。
- 外部静态资源依赖强，迁移环境需要先确认 `/static` 资源目录。

### 建议处理顺序

1. 先确认当前线上/测试环境的 `/static` 资源来源。
2. 记录可用 Node/npm 版本，并生成 lockfile。
3. 明确 `build` 和 `build:prd` 的产物差异。
4. 把 `src/config.js` 改为环境配置，而不是代码内写死。
5. 补一份“部署目录结构”，重点记录 `src/dist`、压缩包和 `/static` 的关系。

## cetc-moniwa-ui

### 基本定位

- 路径：`~/CETC/Project/BeijingDaxing/cetc-moniwa-ui`
- 类型：大兴监测预警平台 UI
- 技术栈：Vue 2.5、Webpack 3、Element UI、ECharts、ArcGIS/GIS、Maven frontend-maven-plugin
- 健康度问题：缺 README、存在环境配置、存在构建产物、旧前端依赖、疑似敏感配置线索

### 关键目录

| 路径 | 作用 |
| --- | --- |
| `src/main.js` | 应用入口 |
| `src/router/` | 路由配置 |
| `src/store/` | Vuex 状态，包含 ArcGIS 相关模块 |
| `src/api/` | 业务 API |
| `src/utils/request.js` | 请求封装 |
| `static/js/config.js` | SSO、侧边导航、全局运行配置 |
| `config/index.js` | dev/build 端口、代理、输出目录 |
| `config/dev.env.js` | 开发环境 API |
| `config/prod.env.js` | 生产环境 API |
| `pom.xml` | Maven 包装构建，安装指定 Node/npm 并运行 npm build |

### 启动方式

```bash
cd /Users/cuizihao/CETC/Project/BeijingDaxing/cetc-moniwa-ui
npm install
npm run dev
```

开发端口：

```text
10013
```

开发服务 host：

```text
localhost
```

### 构建方式

前端构建：

```bash
npm run build
```

Maven 包装构建：

```bash
mvn package
```

`pom.xml` 使用 `frontend-maven-plugin`：

```text
Node v8.9.4
npm 5.6.0
npm install
npm run build
```

这说明该项目最好使用 Node 8/npm 5 复现构建环境。

### 输出目录

`config/index.js` 中生产构建输出到：

```text
target/public/
```

HTML 入口：

```text
target/public/index.html
```

静态资源目录：

```text
target/public/static/
```

### 接口和运行配置

开发代理：

```text
/moniwa/v1 -> http://10.173.134.167
```

环境 API：

```text
BASE_API = http://10.217.17.75:10012/moniwa
MAP_API = http://10.217.17.75:10012
```

SSO 配置在 `static/js/config.js`：

```text
sso = http://10.217.17.81:30009/api/sso/authentication/sso
client_id = moniwa
client_secret = moniwa
```

这里的 `client_secret` 需要人工确认是否只是公开前端占位值，还是实际敏感信息。

### 主要风险

- 无 README，项目恢复成本高。
- Webpack 3、Vue 2.5、Node 8 生态很旧。
- `static/js/config.js` 包含 SSO 地址、client 信息和大量导航配置。
- API、地图、SSO 都写死内网地址。
- Maven 构建依赖内网 Maven 仓库：`maven.cetccity.com:10001`。
- 构建产物在 `target/public`，容易和 Java/Maven 产物混在一起。

### 建议处理顺序

1. 固化 Node 8.9.4/npm 5.6.0 环境，优先保证能复现 Maven 构建。
2. 人工复核 `static/js/config.js` 中的 `client_secret`。
3. 补 README，至少写明端口、API、SSO、构建产物。
4. 将 API/SSO/地图地址抽成环境配置。
5. 记录 `target/public` 如何被后端或部署系统消费。

## 共同建议

这些项目都是典型旧 Vue 2 体系。短期目标不应马上升级，而是先做到：

1. 可复现安装。
2. 可本地启动。
3. 配置外置。
4. README 与真实脚本一致。
5. 明确后端和外部静态资源依赖。
