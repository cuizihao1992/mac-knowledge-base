---
title: CETC 项目健康度报告
tags: [reference, code, inventory, cetc, health]
created: 2026-06-18
source: /Users/cuizihao/CETC/Project
related: [CETC Project 项目盘点]
---

# CETC 项目健康度报告

## 评分口径

- 基准分 100。
- 扣分项：缺 README、缺启动/构建脚本、缺 lockfile、存在环境配置、存在构建产物、旧前端依赖、疑似敏感配置线索。
- 只做静态检查，未安装依赖、未运行项目。
- `疑似敏感配置线索` 仅表示文件中出现 `token`、`secret`、`password`、`accessKey` 等关键字，需要人工复核；不等同于确认泄露。

## 总览

- 检查 git 项目：25 个

| 等级 | 数量 |
| --- | ---: |
| `A` | 7 |
| `B` | 8 |
| `C` | 6 |
| `D` | 4 |

## 高频问题

| 问题 | 项目数 |
| --- | ---: |
| `疑似敏感配置线索` | 19 |
| `旧前端依赖` | 16 |
| `存在环境配置文件` | 8 |
| `存在构建产物目录` | 8 |
| `缺前端 lockfile` | 6 |
| `缺 README` | 5 |
| `缺本地启动脚本` | 1 |

## 项目健康度清单

| 项目 | 等级 | 分数 | 主要问题 | 启动/构建脚本 |
| --- | --- | ---: | --- | --- |
| `~/CETC/Project/gis/urban-virtual-reality-fusion-simulation-platform` | `A` | 80 | `存在环境配置文件`, `旧前端依赖` | `build`, `serve` |
| `~/CETC/Project/gis/gis-map-develop-platform` | `A` | 82 | `疑似敏感配置线索` | - |
| `~/CETC/Project/gis/gis-map-sdk-cesium` | `A` | 82 | `疑似敏感配置线索` | - |
| `~/CETC/Project/1.2-project-network-security-java` | `A` | 85 | `缺 README` | - |
| `~/CETC/Project/cgpt2.0/city-manage-server` | `A` | 85 | `缺 README` | - |
| `~/CETC/Project/gis/gis-bigdata-etl` | `A` | 100 | - | - |
| `~/CETC/Project/gis/gisopenplatform-admin` | `A` | 100 | - | - |
| `~/CETC/Project/smartCity/java` | `B` | 67 | `缺 README`, `疑似敏感配置线索` | - |
| `~/CETC/Project/smartCity/wepy` | `B` | 67 | `缺 README`, `疑似敏感配置线索` | `build`, `dev` |
| `~/CETC/Project/1.2-project-network-security-web` | `B` | 70 | `旧前端依赖`, `疑似敏感配置线索` | `build`, `serve` |
| `~/CETC/Project/cetc-ui/compass-ui-demo` | `B` | 70 | `旧前端依赖`, `疑似敏感配置线索` | `build`, `serve` |
| `~/CETC/Project/cgpt2.0/city-mange-ui-web` | `B` | 70 | `旧前端依赖`, `疑似敏感配置线索` | `build`, `serve` |
| `~/CETC/Project/gis/gis-map-sdk` | `B` | 70 | `旧前端依赖`, `疑似敏感配置线索` | `build`, `dev` |
| `~/CETC/Project/cgpt2.0/city-manage-h5` | `B` | 74 | `存在环境配置文件`, `疑似敏感配置线索` | - |
| `~/CETC/Project/cgpt2.0/e-city-big` | `B` | 76 | `缺前端 lockfile`, `旧前端依赖` | `build`, `serve` |
| `~/CETC/Project/industry-chain` | `C` | 50 | `缺前端 lockfile`, `存在构建产物目录`, `旧前端依赖`, `疑似敏感配置线索` | `build`, `dev` |
| `~/CETC/Project/xinfang/xinfang` | `C` | 50 | `缺前端 lockfile`, `存在环境配置文件`, `旧前端依赖`, `疑似敏感配置线索` | `build:prod`, `build:stage`, `dev` |
| `~/CETC/Project/brain` | `C` | 62 | `存在构建产物目录`, `旧前端依赖`, `疑似敏感配置线索` | `build`, `dev` |
| `~/CETC/Project/gis/offline-map` | `C` | 62 | `存在构建产物目录`, `旧前端依赖`, `疑似敏感配置线索` | `build`, `dev`, `start` |
| `~/CETC/Project/smartCity/managerweb` | `C` | 62 | `存在构建产物目录`, `旧前端依赖`, `疑似敏感配置线索` | `build:prod`, `build:sit`, `dev` |
| `~/CETC/Project/xinfang/xinfang-web` | `C` | 62 | `存在环境配置文件`, `旧前端依赖`, `疑似敏感配置线索` | `build`, `build:stage`, `dev` |
| `~/CETC/Project/cetc-ui/bi-ui` | `D` | 27 | `缺本地启动脚本`, `缺前端 lockfile`, `存在环境配置文件`, `存在构建产物目录`, `旧前端依赖`, `疑似敏感配置线索` | `build:prd` |
| `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `D` | 39 | `缺 README`, `存在环境配置文件`, `存在构建产物目录`, `旧前端依赖`, `疑似敏感配置线索` | `build`, `dev`, `start` |
| `~/CETC/Project/jun-dd-web` | `D` | 42 | `缺前端 lockfile`, `存在环境配置文件`, `存在构建产物目录`, `旧前端依赖`, `疑似敏感配置线索` | `build`, `build:prd`, `dev` |
| `~/CETC/Project/xinfang/xinfang-web-admin` | `D` | 42 | `缺前端 lockfile`, `存在环境配置文件`, `存在构建产物目录`, `旧前端依赖`, `疑似敏感配置线索` | `build:prod`, `build:stage`, `dev` |

## 重点风险明细

### ~/CETC/Project/gis/gis-map-develop-platform

- 等级/分数：`A` / 82
- 问题：`疑似敏感配置线索`
- 疑似敏感配置线索文件：`example2d/gis/sdk/gismap.min.js`, `example2d/gis/sdk/token.js`, `example2d/gis/config/mapconfig2.json`, `example2d/gis/config/layerconfig.json`, `example2d/gis/config/mapconfig.json`

### ~/CETC/Project/gis/gis-map-sdk-cesium

- 等级/分数：`A` / 82
- 问题：`疑似敏感配置线索`
- 疑似敏感配置线索文件：`src/js/main/measure.js`, `src/js/main/main.js`

### ~/CETC/Project/smartCity/java

- 等级/分数：`B` / 67
- 问题：`缺 README`, `疑似敏感配置线索`
- 疑似敏感配置线索文件：`src/main/resources/app.properties`, `src/main/resources/application.yml`

### ~/CETC/Project/smartCity/wepy

- 等级/分数：`B` / 67
- 问题：`缺 README`, `疑似敏感配置线索`
- 疑似敏感配置线索文件：`package-lock.json`

### ~/CETC/Project/1.2-project-network-security-web

- 等级/分数：`B` / 70
- 问题：`旧前端依赖`, `疑似敏感配置线索`
- 旧依赖：`Vue 2`, `Webpack <= 4`
- 疑似敏感配置线索文件：`src/permission.js`, `src/main.js`, `src/store/getters.js`, `src/store/mutation-types.js`, `src/store/modules/user.js`

### ~/CETC/Project/cetc-ui/compass-ui-demo

- 等级/分数：`B` / 70
- 问题：`旧前端依赖`, `疑似敏感配置线索`
- 旧依赖：`Vue 2`
- 疑似敏感配置线索文件：`src/components/CodemirrorTemp.vue`, `public/static/GIS/layerConfig.json`

### ~/CETC/Project/cgpt2.0/city-mange-ui-web

- 等级/分数：`B` / 70
- 问题：`旧前端依赖`, `疑似敏感配置线索`
- 旧依赖：`Vue 2`, `Element UI`
- 疑似敏感配置线索文件：`src/permission.js`, `src/main.js`, `src/store/getters.js`, `src/store/mutation-types.js`, `src/store/modules/user.js`

### ~/CETC/Project/gis/gis-map-sdk

- 等级/分数：`B` / 70
- 问题：`旧前端依赖`, `疑似敏感配置线索`
- 旧依赖：`Webpack <= 4`
- 疑似敏感配置线索文件：`webpack.config.js`, `src/layer/TDMapTileLayer.js`, `src/layer/Layer.js`, `src/map/Global.js`, `src/map/index.js`

### ~/CETC/Project/cgpt2.0/city-manage-h5

- 等级/分数：`B` / 74
- 问题：`存在环境配置文件`, `疑似敏感配置线索`
- 环境配置：`plugin/uni-simple-router/helpers/config.js`
- 疑似敏感配置线索文件：`setting.json`, `README.md`, `store/index.js`, `pages/login/login.vue`, `pages/user/people.vue`

### ~/CETC/Project/industry-chain

- 等级/分数：`C` / 50
- 问题：`缺前端 lockfile`, `存在构建产物目录`, `旧前端依赖`, `疑似敏感配置线索`
- 旧依赖：`Vue 2`, `Webpack <= 4`, `Element UI`
- 构建产物目录：`build`
- 疑似敏感配置线索文件：`src/lang/en-US.js`, `src/lang/zh-CN.js`

### ~/CETC/Project/xinfang/xinfang

- 等级/分数：`C` / 50
- 问题：`缺前端 lockfile`, `存在环境配置文件`, `旧前端依赖`, `疑似敏感配置线索`
- 旧依赖：`Vue 2`, `Element UI`
- 环境配置：`cetc-ui/.env.development`, `cetc-ui/.env.production`, `cetc-ui/.env.staging`
- 疑似敏感配置线索文件：`cetc-ui/src/permission.js`, `cetc-ui/src/store/getters.js`, `cetc-ui/src/views/login.vue`, `cetc-ui/src/api/login.js`, `cetc-ui/src/utils/request.js`

### ~/CETC/Project/brain

- 等级/分数：`C` / 62
- 问题：`存在构建产物目录`, `旧前端依赖`, `疑似敏感配置线索`
- 旧依赖：`Vue 2`, `Webpack <= 4`, `Element UI`
- 构建产物目录：`build`
- 疑似敏感配置线索文件：`src/store/modules/user.js`, `src/pages/login.vue`, `src/common/api/login.js`, `src/components/GisMap/index_test.vue`, `src/lang/en-US.js`

### ~/CETC/Project/gis/offline-map

- 等级/分数：`C` / 62
- 问题：`存在构建产物目录`, `旧前端依赖`, `疑似敏感配置线索`
- 旧依赖：`Vue 2`, `Webpack <= 4`, `Element UI`, `node-sass`
- 构建产物目录：`build`
- 疑似敏感配置线索文件：`package-lock.json`, `src/main.js`, `src/store/index.js`, `src/views/login/index.vue`, `src/utils/core.js`

### ~/CETC/Project/smartCity/managerweb

- 等级/分数：`C` / 62
- 问题：`存在构建产物目录`, `旧前端依赖`, `疑似敏感配置线索`
- 旧依赖：`Vue 2`, `Webpack <= 4`, `Element UI`, `node-sass`
- 构建产物目录：`build`
- 疑似敏感配置线索文件：`package-lock.json`, `src/permission.js`, `src/store/getters.js`, `src/store/modules/user.js`, `src/views/login/index.vue`

### ~/CETC/Project/xinfang/xinfang-web

- 等级/分数：`C` / 62
- 问题：`存在环境配置文件`, `旧前端依赖`, `疑似敏感配置线索`
- 旧依赖：`Vue 2`, `Element UI`
- 环境配置：`.env.development`, `.env.production`, `.env.staging`, `src/config.js`
- 疑似敏感配置线索文件：`src/main.js`, `src/store/other.js`, `src/store/getters.js`, `src/pages/login.vue`, `src/pages/newLogin.vue`

### ~/CETC/Project/cetc-ui/bi-ui

- 等级/分数：`D` / 27
- 问题：`缺本地启动脚本`, `缺前端 lockfile`, `存在环境配置文件`, `存在构建产物目录`, `旧前端依赖`, `疑似敏感配置线索`
- 旧依赖：`Vue 2`, `Webpack <= 4`, `Element UI`
- 环境配置：`docs/.vuepress/config.js`, `src/config.js`
- 构建产物目录：`build`
- 疑似敏感配置线索文件：`src/static/GIS/gismap.min.js`, `src/static/GIS/layerConfig.json`, `src/components/Gis/index.vue`, `src/components/Gis/Gis.vue`, `src/lang/en-US.js`

### ~/CETC/Project/BeijingDaxing/cetc-moniwa-ui

- 等级/分数：`D` / 39
- 问题：`缺 README`, `存在环境配置文件`, `存在构建产物目录`, `旧前端依赖`, `疑似敏感配置线索`
- 旧依赖：`Vue 2`, `Webpack <= 4`, `Element UI`
- 环境配置：`static/js/config.js`
- 构建产物目录：`build`
- 疑似敏感配置线索文件：`package-lock.json`, `src/App.vue`, `src/permission.js`, `src/router/index.js`, `src/store/getters.js`

### ~/CETC/Project/jun-dd-web

- 等级/分数：`D` / 42
- 问题：`缺前端 lockfile`, `存在环境配置文件`, `存在构建产物目录`, `旧前端依赖`, `疑似敏感配置线索`
- 旧依赖：`Vue 2`, `Webpack <= 4`, `Element UI`
- 环境配置：`src/config.js`
- 构建产物目录：`build`
- 疑似敏感配置线索文件：`src/store/other.js`, `src/pages/share/swiper.vue`, `src/pages/share/chart.vue`, `src/pages/login/index-old.vue`, `src/pages/personalCenter/updatePwd.vue`

### ~/CETC/Project/xinfang/xinfang-web-admin

- 等级/分数：`D` / 42
- 问题：`缺前端 lockfile`, `存在环境配置文件`, `存在构建产物目录`, `旧前端依赖`, `疑似敏感配置线索`
- 旧依赖：`Vue 2`, `Element UI`
- 环境配置：`.env.development`, `.env.production`, `.env.staging`, `src/api/system/config.js`, `src/utils/generator/config.js`
- 构建产物目录：`build`
- 疑似敏感配置线索文件：`src/permission.js`, `src/store/getters.js`, `src/store/modules/user.js`, `src/views/login.vue`, `src/api/login.js`

## 建议下一步

1. 优先处理 `D` 和带 `疑似敏感配置线索` 的项目，确认是否有真实密钥或生产地址泄露。
2. 对仍要维护的前端项目补齐 lockfile 和启动说明。
3. 从业务价值最高的 3-5 个项目开始写运行手册。
