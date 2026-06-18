# CETC 重点项目运行环境复现计划

> 更新时间：2026-06-19
> 范围：优先覆盖健康评分最低、后续最可能需要接手或修复的 4 个前端项目。

## 结论摘要

这 4 个项目都属于较老的 Vue / Webpack 技术栈。当前最影响复现的不是业务代码本身，而是运行时版本、锁文件缺失、内网接口依赖和私有仓库依赖。

| 项目 | 技术栈判断 | 锁文件 | 建议首选运行时 | 主要风险 |
| --- | --- | --- | --- | --- |
| `xinfang/xinfang-web-admin` | Vue CLI 4 / RuoYi 管理后台 | 无 | Node 12 或 14 | 端口默认 80，代理依赖内网后端 |
| `cetc-ui/bi-ui` | Vue 2 + Webpack 4 + VuePress 组件库 | 无 | Node 10 或 12 | 依赖体量大，含 GitHub 依赖和内网代理 |
| `jun-dd-web` | Vue 2 + Webpack 4 业务大屏 | 无 | Node 10 或 12 | 内置 ArcGIS 静态包很重，代理点多 |
| `BeijingDaxing/cetc-moniwa-ui` | Vue 2 + vue-template webpack + Maven 前端打包 | 有 `package-lock.json` | Node 8.9.4 / npm 5.6.0 | Maven 依赖内网仓库，Node 版本很老 |

## 推荐复现顺序

1. 先建立隔离运行环境，不直接使用系统默认 Node。
2. 先跑 `npm install` / `npm ci` 的依赖安装验证，再跑开发服务。
3. 对无锁文件项目优先记录一次成功安装后的锁文件，但不要直接提交到业务仓库，先确认团队是否允许。
4. 对所有内网代理地址做可达性记录，区分“前端能启动”和“业务接口可用”。
5. 每个项目跑通后补一份最小 README：Node 版本、安装命令、启动命令、构建命令、依赖后端。

## 项目复现卡片

### xinfang / xinfang-web-admin

- 路径：`/Users/cuizihao/CETC/Project/xinfang/xinfang-web-admin`
- 项目名：`ruoyi`
- 版本：`3.0.0`
- 引擎声明：`node >=8.9`，`npm >=3.0.0`
- 技术栈：Vue CLI 4、Element UI、Vuex、Vue Router、Axios、ECharts、Jest。
- 锁文件：未发现 `package-lock.json`、`yarn.lock`、`pnpm-lock.yaml`。

常用命令：

```bash
npm install
npm run dev
npm run build:stage
npm run build:prod
npm run test:ci
```

运行注意：

- `vue.config.js` 默认端口是 `80`，普通用户启动可能因为权限失败；建议复现时临时使用 `npm run dev -- --port 8080` 或设置 npm port。
- 开发代理入口来自 `process.env.VUE_APP_BASE_API`，目标为内网后端 `10.0.13.68:8080`。
- 生产 `publicPath` 固定为 `/admin`，部署到其它子路径时需要单独确认。

建议运行时：

- 首选：Node 12.x / npm 6.x。
- 备选：Node 14.x / npm 6.x。
- 不建议直接用 Node 18/20 首次复现，老版 `sass-loader`、`node-sass` 生态容易安装失败。

### cetc-ui / bi-ui

- 路径：`/Users/cuizihao/CETC/Project/cetc-ui/bi-ui`
- 项目名：`compass-ui`
- 版本：`0.0.1`
- 技术栈：Vue 2、Webpack 4、VuePress、Element UI、ECharts、Mapbox、esri-loader、Cesium。
- 锁文件：未发现 `package-lock.json`、`yarn.lock`、`pnpm-lock.yaml`。

常用命令：

```bash
npm install
npm run docs:dev
npm run docs:build
npm run demo:dev
npm run demo:build
npm run pack
```

运行注意：

- `demo:dev` 通过 `build/webpack.config.js` 启动，开发服务 host 为 `localhost`，未显式设置端口。
- 代理 `/biapi` 当前指向内网 `10.0.13.20:9991`。
- `package.json` 依赖中存在 `emmet`，老项目里常见 GitHub 依赖或历史包解析问题，离线或网络受限时容易失败。
- 依赖体量很大，首次安装建议保留完整日志，便于定位 native 模块、镜像源或 peer dependency 问题。

建议运行时：

- 首选：Node 10.x / npm 6.x。
- 备选：Node 12.x / npm 6.x。
- 文档站 VuePress 1 可以单独验证，组件 demo 和打包再分开验证。

### jun-dd-web

- 路径：`/Users/cuizihao/CETC/Project/jun-dd-web`
- 项目名：`jun-dd`
- 版本：`0.0.1`
- 技术栈：Vue 2、Webpack 4、Element UI、ECharts、ArcGIS JS API 静态资源、Mapbox、esri-loader。
- 锁文件：未发现 `package-lock.json`、`yarn.lock`、`pnpm-lock.yaml`。

常用命令：

```bash
npm install
npm run dev
npm run build
npm run pack
npm run build:prd
```

运行注意：

- `build/webpack.config.js` 开发服务 host 为 `0.0.0.0`，未显式设置端口。
- 代理路径较多，包括 `/api`、`/data`、`/alertEvent`、`/gis`、`/group1`、`/source`、`/image`、`/file`。
- 多数代理目标为 `10.0.13.20`、`10.0.13.20:8080`、`10.0.13.20:8091`、`10.0.11.81:8800` 等内网服务。
- `src/static/js/GIS/arcgis_js_api/library/4.13` 内置大量第三方静态资源，仓库体积和扫描噪音都会偏高。
- `build` 会继续执行 `npm run tar`，需要确认本地是否具备压缩产物所需目录和权限。

建议运行时：

- 首选：Node 10.x / npm 6.x。
- 备选：Node 12.x / npm 6.x。
- 首次复现建议只跑 `npm run dev`；业务接口不可达不等于前端构建失败。

### BeijingDaxing / cetc-moniwa-ui

- 路径：`/Users/cuizihao/CETC/Project/BeijingDaxing/cetc-moniwa-ui`
- 项目名：`warningplatform`
- 版本：`1.0.0`
- 引擎声明：`node >=6.0.0`，`npm >=3.0.0`
- 技术栈：Vue 2、Webpack 3/4 时代模板、Element UI、ECharts、esri-loader、Maven 前端插件。
- 锁文件：存在 `package-lock.json`。

常用命令：

```bash
npm ci
npm run dev
npm run build
mvn package
```

运行注意：

- `pom.xml` 使用 `frontend-maven-plugin`，声明安装 Node `v8.9.4` 和 npm `5.6.0`。
- Maven 仓库指向内网 `maven.cetccity.com:10001`，离开内网时 `mvn package` 大概率失败。
- 开发服务默认端口为 `10013`，代理 `/moniwa/v1` 指向内网服务。
- 构建输出目录为 `target/public`，与普通 Vue CLI 项目的 `dist` 不同。

建议运行时：

- 首选：Node 8.9.4 / npm 5.6.0，与 `pom.xml` 保持一致。
- 若只验证 npm 构建，可先用 `npm ci` 保持锁文件一致。
- 若验证 Maven 流程，先确认内网 Maven 仓库可访问。

## 建议的本机工具矩阵

| 工具 | 用途 | 建议 |
| --- | --- | --- |
| `nvm` | 切换 Node 版本 | 至少准备 Node 8.9.4、10.x、12.x、14.x |
| npm 镜像源 | 降低老依赖安装失败概率 | 保留默认源和可用镜像源两套记录 |
| Maven | 验证 `cetc-moniwa-ui` 后端式前端打包 | 需能访问 CETC 内网 Maven 仓库 |
| Java | Maven 运行 | 先记录本机版本，失败时再按项目要求降级 |

## 不建议立即做的事

- 不建议直接在这些业务仓库提交自动生成的锁文件。
- 不建议直接升级依赖或 Node 版本，这会把“复现问题”变成“迁移问题”。
- 不建议先修 lint，老项目 lint 输出可能很多，容易偏离“能跑起来”的目标。
- 不建议把内网地址、密钥、账号类信息同步到公开仓库；知识库只记录脱敏后的结构化信息。

## 下一步动作

1. 为 4 个项目逐个建立本地复现记录表：安装结果、启动结果、构建结果、失败日志摘要。
2. 如果本机已有 `nvm`，优先按建议版本只验证安装和启动，不修改业务仓库。
3. 跑通一个项目后，再决定是否给原项目增加 `.nvmrc`、README 或锁文件。
4. 对 `cetc-moniwa-ui` 单独验证 Maven 仓库可达性，因为它的复现路径和其它纯前端项目不同。
