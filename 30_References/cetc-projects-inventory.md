---
title: CETC Project 项目盘点
tags: [reference, code, inventory, cetc]
created: 2026-06-18
source: /Users/cuizihao/CETC/Project
related: [cuizihao 目录代码项目盘点]
---

# CETC Project 项目盘点

## 扫描说明

- 根目录：`/Users/cuizihao/CETC/Project/`
- 识别方式：以 `.git` 目录作为项目边界，读取 `package.json`、`pom.xml`、`build.gradle*`、`requirements.txt`、`README`、`vite/vue/next` 配置等信号。
- 用途判断：根据目录名、依赖、脚本、README 文本推断；未运行项目。

## 总览

- 识别到 git 项目：25 个

## 按用途统计

| 用途 | 数量 |
| --- | ---: |
| `GIS/地图平台` | 7 |
| `移动端/小程序前端` | 6 |
| `后端服务` | 5 |
| `可视化大屏` | 3 |
| `后台管理前端` | 3 |
| `组件/SDK/示例` | 1 |

## 按技术栈统计

| 技术栈 | 数量 |
| --- | ---: |
| `JavaScript/Node` | 17 |
| `Vue` | 15 |
| `Element UI` | 12 |
| `ECharts` | 11 |
| `Webpack` | 9 |
| `Java/Maven` | 7 |
| `未知` | 4 |
| `GIS/Map` | 3 |

## 项目清单

| 项目 | 推断用途 | 技术栈 | 说明 | 常见脚本 |
| --- | --- | --- | --- | --- |
| `~/CETC/Project/1.2-project-network-security-java` | 后端服务 | `Java/Maven` | - | - |
| `~/CETC/Project/1.2-project-network-security-web` | 后端服务 | `JavaScript/Node`, `Vue`, `Webpack` | Ant Design cityIE Vue | `build`, `lint`, `pre`, `serve` |
| `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | 后端服务 | `ECharts`, `Element UI`, `Java/Maven`, `JavaScript/Node`, `Vue`, `Webpack` | daxing early warning platform | `build`, `dev`, `lint`, `start` |
| `~/CETC/Project/brain` | 可视化大屏 | `ECharts`, `Element UI`, `JavaScript/Node`, `Vue`, `Webpack` | 综合信息资源中心 | `build`, `dev`, `lint`, `precommit`, `prettier` |
| `~/CETC/Project/cetc-ui/bi-ui` | GIS/地图平台 | `ECharts`, `Element UI`, `GIS/Map`, `JavaScript/Node`, `Vue`, `Webpack` | jun-dd | `build:prd`, `demo:build`, `demo:dev`, `docs:build`, `docs:dev`, `lint`, `pack`, `plop` |
| `~/CETC/Project/cetc-ui/compass-ui-demo` | 移动端/小程序前端 | `JavaScript/Node`, `Vue` | demo-ui | `build`, `docs:build`, `docs:dev`, `lint`, `serve` |
| `~/CETC/Project/cgpt2.0/city-manage-h5` | 移动端/小程序前端 | `未知` | E-CITY-H5 | - |
| `~/CETC/Project/cgpt2.0/city-manage-server` | 后端服务 | `Java/Maven` | - | - |
| `~/CETC/Project/cgpt2.0/city-mange-ui-web` | 可视化大屏 | `Element UI`, `Java/Maven`, `JavaScript/Node`, `Vue` | e-city 说明文档 | `build`, `lint`, `lint-fix`, `pre`, `serve` |
| `~/CETC/Project/cgpt2.0/e-city-big` | 可视化大屏 | `ECharts`, `JavaScript/Node`, `Vue` | 大屏数据可视化 | `build`, `lint`, `serve` |
| `~/CETC/Project/gis/gis-bigdata-etl` | GIS/地图平台 | `未知` | GIS空间大数据ETL项目 | - |
| `~/CETC/Project/gis/gis-map-develop-platform` | GIS/地图平台 | `未知` | GIS开发平台 | - |
| `~/CETC/Project/gis/gis-map-sdk` | GIS/地图平台 | `JavaScript/Node`, `Webpack` | WebGIS快速开发SDK | `build`, `dev`, `repl`, `server`, `test`, `test:cover`, `test:watch` |
| `~/CETC/Project/gis/gis-map-sdk-cesium` | GIS/地图平台 | `未知` | gis-map-sdk-3d | - |
| `~/CETC/Project/gis/gisopenplatform-admin` | 后台管理前端 | `Java/Maven` | GISOpenPlatform-Admin | - |
| `~/CETC/Project/gis/offline-map` | 移动端/小程序前端 | `ECharts`, `Element UI`, `GIS/Map`, `JavaScript/Node`, `Vue`, `Webpack` | A Vue.js project | `build`, `dev`, `start`, `test`, `unit` |
| `~/CETC/Project/gis/urban-virtual-reality-fusion-simulation-platform` | GIS/地图平台 | `Element UI`, `JavaScript/Node`, `Vue` | gis | `build`, `lint`, `serve` |
| `~/CETC/Project/industry-chain` | 组件/SDK/示例 | `ECharts`, `Element UI`, `JavaScript/Node`, `Vue`, `Webpack` | 综合信息资源中心 | `build`, `dev`, `lint`, `precommit`, `prettier` |
| `~/CETC/Project/jun-dd-web` | GIS/地图平台 | `ECharts`, `Element UI`, `GIS/Map`, `JavaScript/Node`, `Vue`, `Webpack` | CETC BI | `build`, `build:prd`, `compress`, `dev`, `lint`, `pack`, `precommit`, `prettier` |
| `~/CETC/Project/smartCity/java` | 后端服务 | `Java/Maven` | - | - |
| `~/CETC/Project/smartCity/managerweb` | 后台管理前端 | `ECharts`, `Element UI`, `JavaScript/Node`, `Vue`, `Webpack` | A magical vue admin. Typical templates for enterprise applications. Newest development stack of vue. Lots of awesome features | `build:prod`, `build:sit`, `dev`, `lint`, `test` |
| `~/CETC/Project/smartCity/wepy` | 移动端/小程序前端 | `JavaScript/Node` | dkznh | `build`, `dev`, `test` |
| `~/CETC/Project/xinfang/xinfang` | 移动端/小程序前端 | `ECharts`, `Element UI`, `Java/Maven`, `JavaScript/Node`, `Vue` | cetc管理系统 | `build:prod`, `build:stage`, `dev`, `lint`, `new`, `preview`, `svgo`, `test:ci` |
| `~/CETC/Project/xinfang/xinfang-web` | 移动端/小程序前端 | `ECharts`, `Element UI`, `JavaScript/Node`, `Vue` | micro_home_h5 | `build`, `build:stage`, `dev`, `lint` |
| `~/CETC/Project/xinfang/xinfang-web-admin` | 后台管理前端 | `ECharts`, `Element UI`, `JavaScript/Node`, `Vue` | 分析预警系统管理后台 | `build:prod`, `build:stage`, `dev`, `lint`, `new`, `preview`, `svgo`, `test:ci` |

## 详细信号

| 项目 | 配置/信号文件 |
| --- | --- |
| `~/CETC/Project/1.2-project-network-security-java` | `cetc-security-master/pom.xml` |
| `~/CETC/Project/1.2-project-network-security-web` | `README.md`, `package.json`, `vue.config.js` |
| `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `package.json`, `pom.xml` |
| `~/CETC/Project/brain` | `README.md`, `package.json` |
| `~/CETC/Project/cetc-ui/bi-ui` | `README.md`, `package.json` |
| `~/CETC/Project/cetc-ui/compass-ui-demo` | `README.md`, `package.json`, `vue.config.js` |
| `~/CETC/Project/cgpt2.0/city-manage-h5` | `README.md` |
| `~/CETC/Project/cgpt2.0/city-manage-server` | `cetc-boot-module-system/README.md`, `pom.xml` |
| `~/CETC/Project/cgpt2.0/city-mange-ui-web` | `README.md`, `package.json`, `pom.xml`, `vue.config.js` |
| `~/CETC/Project/cgpt2.0/e-city-big` | `README.md`, `package.json`, `vue.config.js` |
| `~/CETC/Project/gis/gis-bigdata-etl` | `README.md` |
| `~/CETC/Project/gis/gis-map-develop-platform` | `README.md` |
| `~/CETC/Project/gis/gis-map-sdk` | `README.md`, `package.json` |
| `~/CETC/Project/gis/gis-map-sdk-cesium` | `README.md` |
| `~/CETC/Project/gis/gisopenplatform-admin` | `README.md`, `pom.xml` |
| `~/CETC/Project/gis/offline-map` | `README.md`, `package.json` |
| `~/CETC/Project/gis/urban-virtual-reality-fusion-simulation-platform` | `README.md`, `package.json`, `vue.config.js` |
| `~/CETC/Project/industry-chain` | `README.md`, `package.json` |
| `~/CETC/Project/jun-dd-web` | `README.md`, `package.json` |
| `~/CETC/Project/smartCity/java` | `pom.xml` |
| `~/CETC/Project/smartCity/managerweb` | `README.md`, `README.zh-CN.md`, `package.json` |
| `~/CETC/Project/smartCity/wepy` | `package.json` |
| `~/CETC/Project/xinfang/xinfang` | `README.md`, `cetc-ui/package.json`, `cetc-ui/vue.config.js`, `pom.xml` |
| `~/CETC/Project/xinfang/xinfang-web` | `README.md`, `package.json`, `vue.config.js` |
| `~/CETC/Project/xinfang/xinfang-web-admin` | `README.md`, `package.json`, `vue.config.js` |
