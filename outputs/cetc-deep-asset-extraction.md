---
title: CETC 高价值项目深度资产报告
tags: [reference, code, cetc, deep-extraction, generated]
created: 2026-06-22
source: /Users/cuizihao/CETC/Project
related: [CETC 自动资产抽取报告, CETC 旧项目业务价值与架构判断]
---

# CETC 高价值项目深度资产报告

> 生成时间：2026-06-21T16:15:11.847693+00:00

## 总览

- 目标项目：10 个
- 实际存在：10 个
- JSON 输出：`outputs/cetc-deep-asset-extraction.json`
- Markdown 输出：`outputs/cetc-deep-asset-extraction.md`

| 类型 | 数量 |
| --- | ---: |
| `frontend` | 5 |
| `java` | 2 |
| `unknown` | 3 |

## 资产矩阵

| 项目 | 类型 | 页面 | 路由 | 组件 | API/接口 | GIS 线索 | 风险线索 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `jun-dd-web` | `frontend` | 160 | 51 | 120 | 0 | 120 | 120 |
| `cetc-ui/bi-ui` | `frontend` | 143 | 11 | 120 | 2 | 120 | 99 |
| `gis/gis-map-sdk` | `frontend` | 0 | 0 | 0 | 0 | 54 | 19 |
| `gis/gis-map-sdk-cesium` | `unknown` | 0 | 0 | 0 | 0 | 120 | 42 |
| `gis/gis-map-develop-platform` | `unknown` | 0 | 0 | 0 | 0 | 120 | 82 |
| `cgpt2.0/city-manage-h5` | `unknown` | 55 | 17 | 24 | 0 | 14 | 49 |
| `cgpt2.0/city-manage-server` | `java` | 0 | 0 | 0 | 160 | 120 | 120 |
| `cgpt2.0/e-city-big` | `frontend` | 58 | 5 | 55 | 0 | 36 | 8 |
| `xinfang/xinfang` | `java` | 64 | 18 | 30 | 160 | 120 | 120 |
| `xinfang/xinfang-web-admin` | `frontend` | 64 | 19 | 30 | 84 | 31 | 36 |

## 项目深挖

### jun-dd-web

- 类型：`frontend`
- 资产价值：BI 大屏、可视化组件、GIS 页面和前端工程经验，可作为组件/页面/样式资产继续复用。
- 依赖样本：`@babel/core, @commitlint/cli, @commitlint/config-conventional, @shopify/draggable, @turf/area, @turf/center-of-mass, @turf/turf, @vue/eslint-config-prettier, acorn, async-validator, axios, babel`
- 脚本/构建入口：`build, build:prd, compress, dev, lint, pack, precommit, prettier, tar`

关键目录：
- `src/common/api`
- `src/components`
- `src/components/Tinymce/components`
- `src/components/TyTable/components`
- `src/components/charts_backup/api`
- `src/components/charts_backup/components`
- `src/components/charts_backup/components/GIS/components`
- `src/components/charts_backup/store`
- `src/components/data-set/components`
- `src/components/photo-booklet/decorateDailog/components`
- ... 另有 16 项

路由入口：
- `/newHome` in `src/router/pages.js`
- `/projectIndex` in `src/router/pages.js`
- `/jxInfoHead` in `src/router/pages.js`
- `/jxWarnPush` in `src/router/pages.js`
- `/elTimeLine` in `src/router/pages.js`
- `/sIndex` in `src/router/pages.js`
- `/loginOther` in `src/router/pages.js`
- `/personalPortrait` in `src/router/pages.js`
- `/makingForm` in `src/router/pages.js`
- `/timeline` in `src/router/pages.js`
- `/` in `src/router/pages.js`
- `/createPhoto` in `src/router/pages.js`
- `/personalCenter` in `src/router/pages.js`
- `/personalCenter/updatePwd` in `src/router/pages.js`
- ... 另有 37 项

页面样本：
- `src/App.vue`
- `src/components/CustomizedComponents/JxGraph/graph.vue`
- `src/components/CustomizedComponents/JxPertition/JxPertition.vue`
- `src/components/CustomizedComponents/JxPertition/com/customMap.vue`
- `src/components/DemoTemplate/demo1.vue`
- `src/components/DemoTemplate/demo2.vue`
- `src/components/DemoTemplate/demo3.vue`
- `src/components/DemoTemplate/demo4.vue`
- `src/components/DemoTemplate/smartcity.vue`
- `src/components/HT-bak/index.vue`
- `src/components/HT/index.vue`
- `src/components/ResizeBox/index.vue`
- `src/components/ResizeBox/pages.vue`
- `src/components/SvgIcon/index.vue`
- `src/components/TimeLine/TimeLine.vue`
- `src/components/TimelineApi-1/Timeline.vue`
- ... 另有 144 项

组件/库样本：
- `src/components/CustomizedComponents/JxGraph/graph.vue`
- `src/components/CustomizedComponents/JxGraph/index.js`
- `src/components/CustomizedComponents/JxGraph/utils/engin.js`
- `src/components/CustomizedComponents/JxPertition/JxPertition.vue`
- `src/components/CustomizedComponents/JxPertition/com/customMap.vue`
- `src/components/CustomizedComponents/JxPertition/index.js`
- `src/components/DemoTemplate/demo1.vue`
- `src/components/DemoTemplate/demo2.vue`
- `src/components/DemoTemplate/demo3.vue`
- `src/components/DemoTemplate/demo4.vue`
- `src/components/DemoTemplate/smartcity.vue`
- `src/components/HT-bak/index.vue`
- `src/components/HT/index.vue`
- `src/components/ResizeBox/index.vue`
- `src/components/ResizeBox/pages.vue`
- `src/components/SvgIcon/index.vue`
- ... 另有 104 项

API/后端接口样本：
- 未发现

GIS/地图/可视化线索：
- `jest.config.js`
- `package.json`
- `src/assets/iconfont/iconfont.css`
- `src/assets/style/common.less`
- `src/common/api/index.js`
- `src/components/CustomizedComponents/JxGraph/utils/engin.js`
- `src/components/CustomizedComponents/JxPertition/JxPertition.vue`
- `src/components/CustomizedComponents/JxPertition/com/customMap.vue`
- `src/components/HT-bak/index.vue`
- `src/components/HT/index.vue`
- `src/components/TimeLine/TimeLine.vue`
- `src/components/TimelineApi-1/Timeline.vue`
- `src/components/TimelineApi/Timeline.vue`
- `src/components/Tinymce/components/EditorImage.vue`
- `src/components/Tinymce/index.vue`
- `src/components/Tinymce/toolbar.js`
- ... 另有 104 项

配置文件线索：
- `.gitlab-ci.yml`
- `commitlint.config.js`
- `jest.config.js`
- `src/components/charts_backup/components/GIS/components/menuConfig.vue`
- `src/components/charts_backup/components/GIS/components/menuConfig_20200401.vue`
- `src/components/charts_backup/config/config-bar.js`
- `src/components/charts_backup/config/config-line.js`
- `src/components/charts_backup/config/config-pie.js`
- `src/components/charts_backup/graph/config/baseConfig.js`
- `src/components/dialog/exportConfig.vue`
- `src/components/dialog/navbarConfig.vue`
- `src/components/dialog/webSocketConfig.vue`
- `src/components/echarts/config/config.js`
- `src/components/echarts/config/pieconfig.js`
- ... 另有 8 项

敏感关键词线索：
- `.postcssrc.js`
- `package.json`
- `src/assets/data/retailData.json`
- `src/assets/iconfont/iconfont.css`
- `src/assets/style/common.less`
- `src/booklet/booklet.js`
- `src/common/api/index.js`
- `src/common/api/other.js`
- `src/components/CustomizedComponents/JxPertition/JxPertition.vue`
- `src/components/CustomizedComponents/JxPertition/com/customMap.vue`
- `src/components/HT-bak/index.vue`
- `src/components/HT/index.vue`
- `src/components/ResizeBox/index.vue`
- `src/components/SvgIcon/index.vue`
- ... 另有 106 项

### cetc-ui/bi-ui

- 类型：`frontend`
- 资产价值：BI 大屏、可视化组件、GIS 页面和前端工程经验，可作为组件/页面/样式资产继续复用。
- 依赖样本：`@babel/core, @commitlint/cli, @commitlint/config-conventional, @shopify/draggable, @turf/turf, @vue/eslint-config-prettier, acorn, async-validator, axios, babel, babel-core, babel-eslint`
- 脚本/构建入口：`build:prd, demo:build, demo:dev, docs:build, docs:dev, lint, pack, plop, precommit, prettier`

关键目录：
- `src/common/api`
- `src/components`
- `src/components/Booklet/BiCanvas/components`
- `src/components/Booklet/ItemSettings/item/components`
- `src/components/Echarts/components`
- `src/components/Gis/components`
- `src/pages`
- `src/router`
- `src/store`

路由入口：
- `/bi-pagelist` in `src/router/pages.js`
- `/bi-booklet` in `src/router/pages.js`
- `/bi-share` in `src/router/pages.js`
- `/test` in `src/router/pages.js`
- `/bi-createPhoto` in `src/router/pages.js`
- `/entrance` in `src/router/pages.js`
- `/404` in `src/router/pages.js`
- `/tab` in `src/router/pages.js`
- `/bi-dialog-making` in `src/router/pages.js`
- `/gis` in `src/router/pages.js`
- `*` in `src/router/pages.js`

页面样本：
- `src/App.vue`
- `src/components/404/404.vue`
- `src/components/BiIcon/BiIcon.vue`
- `src/components/Booklet/BiCanvas/BiCanvas.vue`
- `src/components/Booklet/BiCanvas/components/ResizeChart.vue`
- `src/components/Booklet/BiCanvas/components/ResizeDecorate.vue`
- `src/components/Booklet/BiCanvas/components/ResizeForm.vue`
- `src/components/Booklet/BiCanvas/components/ResizeGeo.vue`
- `src/components/Booklet/ComponentsList/ComponentsList.vue`
- `src/components/Booklet/ComponentsList/Item/Item.vue`
- `src/components/Booklet/ItemSettings/ItemSettings.vue`
- `src/components/Booklet/ItemSettings/item/Arcgis.vue`
- `src/components/Booklet/ItemSettings/item/Bar-3D.vue`
- `src/components/Booklet/ItemSettings/item/Bar-circle.vue`
- `src/components/Booklet/ItemSettings/item/Bar-special.vue`
- `src/components/Booklet/ItemSettings/item/Bar.vue`
- ... 另有 127 项

组件/库样本：
- `src/components/404/404.vue`
- `src/components/404/index.js`
- `src/components/BiIcon/BiIcon.vue`
- `src/components/BiIcon/icons/index.js`
- `src/components/BiIcon/index.js`
- `src/components/Booklet/BiCanvas/BiCanvas.vue`
- `src/components/Booklet/BiCanvas/components/ResizeChart.vue`
- `src/components/Booklet/BiCanvas/components/ResizeDecorate.vue`
- `src/components/Booklet/BiCanvas/components/ResizeForm.vue`
- `src/components/Booklet/BiCanvas/components/ResizeGeo.vue`
- `src/components/Booklet/BiCanvas/components/mixins/index.js`
- `src/components/Booklet/BiCanvas/index.js`
- `src/components/Booklet/BiCanvas/styles/index.js`
- `src/components/Booklet/ComponentsList/ComponentsList.vue`
- `src/components/Booklet/ComponentsList/Item/Item.vue`
- `src/components/Booklet/ComponentsList/Item/index.js`
- ... 另有 104 项

API/后端接口样本：
- `/display/addDisplay` in `src/common/api/index.js`
- `/display/update` in `src/common/api/index.js`

GIS/地图/可视化线索：
- `Plans/plan.md`
- `examples/main.js`
- `guide/DevelopmentGuide.md`
- `guide/heatMap.json`
- `jest.config.js`
- `package.json`
- `src/components/BiIcon/icons/index.js`
- `src/components/Booklet/BiCanvas/BiCanvas.vue`
- `src/components/Booklet/BiCanvas/components/ResizeGeo.vue`
- `src/components/Booklet/BiCanvas/components/mixins/index.js`
- `src/components/Booklet/BiCanvas/styles/index.js`
- `src/components/Booklet/ComponentsList/ComponentsList.vue`
- `src/components/Booklet/ComponentsList/Item/Item.vue`
- `src/components/Booklet/ItemSettings/ItemSettings.vue`
- `src/components/Booklet/ItemSettings/item/Arcgis.vue`
- `src/components/Booklet/ItemSettings/item/Cesium.vue`
- ... 另有 104 项

配置文件线索：
- `.gitlab-ci.yml`
- `commitlint.config.js`
- `jest.config.js`
- `src/components/BiIcon/icons/svgo.yml`
- `src/components/Booklet/ItemSettings/item/components/axisConfig.vue`
- `src/components/Booklet/ItemSettings/item/components/colorConfig.vue`
- `src/components/Booklet/ItemSettings/item/components/dataZoomConfig.vue`
- `src/components/Booklet/ItemSettings/item/components/form/BiTabConfig.vue`
- `src/components/Booklet/ItemSettings/item/components/form/flipper/flipperConfig.vue`
- `src/components/Booklet/ItemSettings/item/components/form/tableSetting/columnsConfig.vue`
- `src/components/Booklet/ItemSettings/item/components/form/tableSetting/paginationConfig.vue`
- `src/components/Booklet/ItemSettings/item/components/form/tableSetting/tableConfig.vue`
- `src/components/Booklet/ItemSettings/item/components/gridConfig.vue`
- `src/components/Booklet/ItemSettings/item/components/layersConfig.vue`
- ... 另有 24 项

敏感关键词线索：
- `.postcssrc.js`
- `examples/main.js`
- `package.json`
- `src/App.vue`
- `src/assets/style/common.less`
- `src/assets/style/index.less`
- `src/components/BiIcon/BiIcon.vue`
- `src/components/Booklet/BiCanvas/BiCanvas.vue`
- `src/components/Booklet/BiCanvas/components/ResizeChart.vue`
- `src/components/Booklet/BiCanvas/components/ResizeDecorate.vue`
- `src/components/Booklet/BiCanvas/components/ResizeForm.vue`
- `src/components/Booklet/BiCanvas/components/ResizeGeo.vue`
- `src/components/Booklet/BiCanvas/components/mixins/index.js`
- `src/components/Booklet/BiCanvas/styles/index.js`
- ... 另有 85 项

### gis/gis-map-sdk

- 类型：`frontend`
- 资产价值：WebGIS SDK 抽象价值高，适合作为地图图层、工具函数和二次开发样板。
- 依赖样本：`@babel/cli, @babel/core, @babel/plugin-transform-runtime, @babel/preset-env, @babel/runtime, @types/arcgis-js-api, babel-eslint, babel-loader, babel-plugin-add-module-exports, babel-plugin-istanbul, babel-preset-env, babel-register`
- 脚本/构建入口：`build, dev, repl, server, test, test:cover, test:watch`

关键目录：
- `src/service`

路由入口：
- 未发现

页面样本：
- 未发现

组件/库样本：
- 未发现

API/后端接口样本：
- 未发现

GIS/地图/可视化线索：
- `README.md`
- `debug/config/layerconfig.json`
- `debug/config/mapconfig.json`
- `debug/css/gismap.css`
- `debug/data/geojson/test.json`
- `debug/data/geojson/test2.json`
- `debug/data/geojson/test3.json`
- `debug/sdk/gismap.css`
- `debug/sdk/gismap.min.js`
- `extension/echarts.min.js`
- `extension/echartsLayer.js`
- `package-lock.json`
- `package.json`
- `src/config/LayerConfig.js`
- `src/config/LayerGroup.js`
- `src/config/LayerNode.js`
- ... 另有 38 项

配置文件线索：
- `.travis.yml`
- `debug/config/layerconfig.json`
- `debug/config/mapconfig.json`
- `src/config/LayerConfig.js`
- `src/config/MapConfig.js`
- `src/map/Config.js`
- `src/util/Config.js`
- `tsconfig.json`
- `webpack.config.js`

敏感关键词线索：
- `debug/config/layerconfig.json`
- `debug/config/mapconfig.json`
- `debug/data/dark_style2.json`
- `debug/data/poi/jiaoyu.json`
- `debug/sdk/gismap.min.js`
- `extension/echarts.min.js`
- `package-lock.json`
- `src/config/LayerNode.js`
- `src/config/MapConfig.js`
- `src/layer/Layer.js`
- `src/layer/TDMapTileLayer.js`
- `src/map/Config.js`
- `src/map/Global.js`
- `src/map/Map.js`
- ... 另有 5 项

### gis/gis-map-sdk-cesium

- 类型：`unknown`
- 资产价值：3D GIS/Cesium 能力沉淀价值高，适合保留相机、图层、实体、场景初始化模式。
- 依赖样本：`未发现`
- 脚本/构建入口：`未发现`

关键目录：
- 未发现

路由入口：
- 未发现

页面样本：
- 未发现

组件/库样本：
- 未发现

API/后端接口样本：
- 未发现

GIS/地图/可视化线索：
- `README.md`
- `src/css/bootstrap/bootstrap.css`
- `src/data/model/guangzhou/tileset.json`
- `src/data/model/guangzhou/tileset_1_1_0.json`
- `src/data/model/guangzhou/tileset_1_1_1.json`
- `src/data/model/guangzhou/tileset_2_0_0.json`
- `src/data/model/guangzhou/tileset_2_0_1.json`
- `src/data/model/guangzhou/tileset_2_0_2.json`
- `src/data/model/guangzhou/tileset_2_0_3.json`
- `src/data/model/guangzhou/tileset_2_1_1.json`
- `src/data/model/guangzhou/tileset_2_1_2.json`
- `src/data/model/guangzhou/tileset_2_2_0.json`
- `src/data/model/guangzhou/tileset_2_2_1.json`
- `src/data/model/guangzhou/tileset_2_2_2.json`
- `src/data/model/guangzhou/tileset_2_3_2.json`
- `src/js/EMap/core/event.js`
- ... 另有 104 项

配置文件线索：
- 未发现

敏感关键词线索：
- `src/css/bootstrap/bootstrap.css`
- `src/js/EMap/core/event.js`
- `src/js/EMap/core/model.js`
- `src/js/EMap/measure.js`
- `src/js/lib/Cesium/Cesium.js`
- `src/js/lib/Cesium/ThirdParty/Workers/deflate.js`
- `src/js/lib/Cesium/ThirdParty/Workers/draco_decoder.js`
- `src/js/lib/Cesium/ThirdParty/Workers/draco_wasm_wrapper.js`
- `src/js/lib/Cesium/ThirdParty/Workers/inflate.js`
- `src/js/lib/Cesium/ThirdParty/google-earth-dbroot-parser.js`
- `src/js/lib/Cesium/Widgets/BaseLayerPicker/BaseLayerPicker.css`
- `src/js/lib/Cesium/Widgets/widgets.css`
- `src/js/lib/Cesium/Workers/Color-92f09d2a.js`
- `src/js/lib/Cesium/Workers/FrustumGeometry-cdde1565.js`
- ... 另有 28 项

### gis/gis-map-develop-platform

- 类型：`unknown`
- 资产价值：地图开发平台样板价值高，但配置风险也较高，适合脱敏后保留。
- 依赖样本：`未发现`
- 脚本/构建入口：`未发现`

关键目录：
- 未发现

路由入口：
- 未发现

页面样本：
- 未发现

组件/库样本：
- 未发现

API/后端接口样本：
- 未发现

GIS/地图/可视化线索：
- `README.md`
- `example2d/css/base.css`
- `example2d/css/codemirror.css`
- `example2d/css/content.css`
- `example2d/gis/config/HKlayerconfig.json`
- `example2d/gis/config/HKmapconfig.json`
- `example2d/gis/config/dark_style2.json`
- `example2d/gis/config/getbyCity.json`
- `example2d/gis/config/gray_style.json`
- `example2d/gis/config/layerconfig.json`
- `example2d/gis/config/mapconfig.json`
- `example2d/gis/config/mapconfig2.json`
- `example2d/gis/data/geojson/company.json`
- `example2d/gis/data/geojson/jiaoyu.json`
- `example2d/gis/data/geojson/p1.json`
- `example2d/gis/data/geojson/p2.json`
- ... 另有 104 项

配置文件线索：
- `example2d/gis/config/HKlayerconfig.json`
- `example2d/gis/config/HKmapconfig.json`
- `example2d/gis/config/layerconfig.json`
- `example2d/gis/config/mapconfig.json`
- `example2d/gis/config/mapconfig2.json`

敏感关键词线索：
- `example2d/css/codemirror.css`
- `example2d/css/content.css`
- `example2d/gis/config/HKlayerconfig.json`
- `example2d/gis/config/HKmapconfig.json`
- `example2d/gis/config/dark_style2.json`
- `example2d/gis/config/getbyCity.json`
- `example2d/gis/config/gray_style.json`
- `example2d/gis/config/layerconfig.json`
- `example2d/gis/config/mapconfig.json`
- `example2d/gis/config/mapconfig2.json`
- `example2d/gis/data/geojson/jiaoyu.json`
- `example2d/gis/data/poi/jiaoyu.json`
- `example2d/gis/sdk/echarts/echarts.min.js`
- `example2d/gis/sdk/gismap.min.js`
- ... 另有 68 项

### cgpt2.0/city-manage-h5

- 类型：`unknown`
- 资产价值：城市治理链路资产，适合抽业务流程、移动端页面、大屏指标和后端接口。
- 依赖样本：`未发现`
- 脚本/构建入口：`未发现`

关键目录：
- `api`
- `common/router`
- `common/router/modules`
- `common/service`
- `components`
- `pages`
- `plugin/colorui/components`
- `store`

路由入口：
- `/preview-image` in `plugin/uni-simple-router/vueRouter/base.js`
- `/choose-location` in `plugin/uni-simple-router/vueRouter/base.js`
- `/open-location` in `plugin/uni-simple-router/vueRouter/base.js`
- `/pages/login/login` in `common/router/index.js`
- `/pages/login/login` in `common/router/modules/routes.js`
- `/pages/index/index` in `common/router/modules/routes.js`
- `/pages/home/home` in `common/router/modules/routes.js`
- `/pages/user/people` in `common/router/modules/routes.js`
- `/pages/user/userdetail` in `common/router/modules/routes.js`
- `/pages/user/about` in `common/router/modules/routes.js`
- `/pages/notice/notice` in `common/router/modules/routes.js`
- `/pages/user/useredit` in `common/router/modules/routes.js`
- `/pages/user/userexit` in `common/router/modules/routes.js`
- `/pages/common/exit` in `common/router/modules/routes.js`
- ... 另有 3 项

页面样本：
- `App.vue`
- `components/my-componets/my-image-upload.vue`
- `components/my-componets/my-page.vue`
- `components/my-componets/my-select.vue`
- `components/uni-popup/uni-popup-dialog.vue`
- `components/uni-popup/uni-popup-message.vue`
- `components/uni-popup/uni-popup-share.vue`
- `components/uni-popup/uni-popup.vue`
- `components/uni-transition/uni-transition.vue`
- `pages/basics/avatar.vue`
- `pages/basics/background.vue`
- `pages/basics/button.vue`
- `pages/basics/design.vue`
- `pages/basics/home.vue`
- `pages/basics/icon.vue`
- `pages/basics/layout.vue`
- ... 另有 39 项

组件/库样本：
- `components/my-componets/my-image-upload.vue`
- `components/my-componets/my-page.vue`
- `components/my-componets/my-select.vue`
- `components/uni-popup/message.js`
- `components/uni-popup/popup.js`
- `components/uni-popup/uni-popup-dialog.vue`
- `components/uni-popup/uni-popup-message.vue`
- `components/uni-popup/uni-popup-share.vue`
- `components/uni-popup/uni-popup.vue`
- `components/uni-transition/uni-transition.vue`
- `pages/component/bar.vue`
- `pages/component/card.vue`
- `pages/component/chat.vue`
- `pages/component/form.vue`
- `pages/component/home.vue`
- `pages/component/list.vue`
- ... 另有 8 项

API/后端接口样本：
- 未发现

GIS/地图/可视化线索：
- `common/util/MinCache.js`
- `manifest.json`
- `package-lock.json`
- `pages/login/login.vue`
- `pages/user/people.vue`
- `pages/user/useredit.vue`
- `plugin/colorui/icon.css`
- `plugin/uni-simple-router/appRouter/init.js`
- `plugin/uni-simple-router/index.js`
- `plugin/uni-simple-router/lifeCycle/hooks.js`
- `plugin/uni-simple-router/patch/h5-patch.js`
- `plugin/uni-simple-router/vueRouter/concat.js`
- `plugin/uni-simple-router/vueRouter/init.js`
- `plugin/uni-simple-router/vueRouter/util.js`

配置文件线索：
- `common/service/config.service.js`
- `plugin/uni-simple-router/helpers/config.js`

敏感关键词线索：
- `.eslintrc.js`
- `README.md`
- `api/api.js`
- `common/luch-request/core/Request.js`
- `common/router/index.js`
- `common/service/service.js`
- `common/util/appUpdate.js`
- `common/util/constants.js`
- `common/util/tip.js`
- `components/uni-popup/message.js`
- `components/uni-popup/uni-popup.vue`
- `components/uni-transition/uni-transition.vue`
- `manifest.json`
- `package-lock.json`
- ... 另有 35 项

### cgpt2.0/city-manage-server

- 类型：`java`
- 资产价值：城市治理链路资产，适合抽业务流程、移动端页面、大屏指标和后端接口。
- 依赖样本：`cetc-boot-parent, spring-boot-starter-parent, javacv-platform, xxl-job-core, spring-boot-starter-web, spring-boot-starter-mail, spring-boot-starter-test, spring-boot-starter-aop, spring-boot-starter-actuator, spring-boot-devtools, commons-io, commons-lang`
- 脚本/构建入口：`未发现`

关键目录：
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/api`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/api`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/base/controller`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/base/service`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/controller`
- `cetc-boot-module-system/src/main/java/com/cetc/city/cmanage/aiexecute/service`
- `cetc-boot-module-system/src/main/java/com/cetc/city/cmanage/bigCenter/controller`
- `cetc-boot-module-system/src/main/java/com/cetc/city/cmanage/deviceCenter/controller`
- `cetc-boot-module-system/src/main/java/com/cetc/city/cmanage/deviceCenter/mapper`
- `cetc-boot-module-system/src/main/java/com/cetc/city/cmanage/deviceCenter/service`
- ... 另有 70 项

路由入口：
- 未发现

页面样本：
- 未发现

组件/库样本：
- 未发现

API/后端接口样本：
- `"/sys/common"` in `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/controller/CommonController.java`
- `"/403"` in `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/controller/CommonController.java`
- `value = "/upload"` in `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/controller/CommonController.java`
- `value = "/upload2"` in `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/controller/CommonController.java`
- `value = "/static/**"` in `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/controller/CommonController.java`
- `value = "/download/**"` in `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/controller/CommonController.java`
- `"/pdf/pdfPreviewIframe"` in `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/controller/CommonController.java`
- `"/transitRESTful"` in `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/controller/CommonController.java`
- `value = "/uploadFile"` in `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/controller/CommonController.java`
- `"/eventCenter/tbEventDetail"` in `cetc-boot-module-system/src/main/java/com/cetc/city/cmanage/eventCenter/controller/TbEventDetailController.java`
- `value = "/add"` in `cetc-boot-module-system/src/main/java/com/cetc/city/cmanage/eventCenter/controller/TbEventDetailController.java`
- `value = "/edit"` in `cetc-boot-module-system/src/main/java/com/cetc/city/cmanage/eventCenter/controller/TbEventDetailController.java`
- `value = "/queryById"` in `cetc-boot-module-system/src/main/java/com/cetc/city/cmanage/eventCenter/controller/TbEventDetailController.java`
- `value = "/queryByEventId"` in `cetc-boot-module-system/src/main/java/com/cetc/city/cmanage/eventCenter/controller/TbEventDetailController.java`
- `value = "/queryEventPic"` in `cetc-boot-module-system/src/main/java/com/cetc/city/cmanage/eventCenter/controller/TbEventDetailController.java`
- `value = "/queryHandlePic"` in `cetc-boot-module-system/src/main/java/com/cetc/city/cmanage/eventCenter/controller/TbEventDetailController.java`
- ... 另有 144 项

GIS/地图/可视化线索：
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/designer/vo/AjaxJson.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/es/JeecgElasticsearchTemplate.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/api/ISysBaseAPI.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/base/controller/JeecgController.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/base/service/impl/JeecgServiceImpl.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/controller/CommonController.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/query/QueryGenerator.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/util/BrowserUtils.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/util/DesUtils.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/util/DySmsEnum.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/util/RedisUtil.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/util/ReflectHelper.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/util/RestUtil.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/util/dynamic/db/DataSourceCachePool.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/util/dynamic/db/DynamicDBUtil.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/util/dynamic/db/FreemarkerParseFactory.java`
- ... 另有 104 项

配置文件线索：
- `cetc-boot-module-system/src/main/java/com/cetc/city/cmanage/deviceCenter/constant/FrameLessXxlJobConfig.java`
- `cetc-boot-module-system/src/main/java/com/cetc/city/cmanage/deviceCenter/constant/RtspTaskThreadPoolConfig.java`
- `cetc-boot-module-system/src/main/java/com/cetc/city/cmanage/xxljob/config/XxlJobAdminConfig.java`
- `cetc-boot-module-system/src/main/java/com/cetc/city/cmanage/xxljob/config/XxlJobConfig.java`
- `cetc-boot-module-system/src/main/java/com/cetc/city/config/AutoPoiConfig.java`
- `cetc-boot-module-system/src/main/java/com/cetc/city/config/MinioConfig.java`
- `cetc-boot-module-system/src/main/java/com/cetc/city/config/MybatisPlusConfig.java`
- `cetc-boot-module-system/src/main/java/com/cetc/city/config/RedisConfig.java`
- `cetc-boot-module-system/src/main/java/com/cetc/city/config/RestTemplateConfig.java`
- `cetc-boot-module-system/src/main/java/com/cetc/city/config/ShiroConfig.java`
- `cetc-boot-module-system/src/main/java/com/cetc/city/config/StaticConfig.java`
- `cetc-boot-module-system/src/main/java/com/cetc/city/config/Swagger2Config.java`
- `cetc-boot-module-system/src/main/java/com/cetc/city/config/WebMvcConfiguration.java`
- `cetc-boot-module-system/src/main/java/com/cetc/city/config/WebSocketConfig.java`
- ... 另有 13 项

敏感关键词线索：
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/constant/CommonConstant.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/constant/DataBaseConstant.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/constant/ProvinceCityArea.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/api/ISysBaseAPI.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/controller/CommonController.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/query/QueryGenerator.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/util/JwtUtil.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/vo/ComboModel.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/vo/DynamicDataSourceModel.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/vo/LoginUser.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/util/BrowserUtils.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/util/DySmsEnum.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/util/DySmsHelper.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/util/MinioUtil.java`
- ... 另有 106 项

### cgpt2.0/e-city-big

- 类型：`frontend`
- 资产价值：城市治理链路资产，适合抽业务流程、移动端页面、大屏指标和后端接口。
- 依赖样本：`@vue/cli-plugin-babel, @vue/cli-plugin-router, @vue/cli-plugin-vuex, @vue/cli-service, ant-design-vue, axios, core-js, echarts, echarts-gl, lodash, lodash.chunk, lodash.clonedeep`
- 脚本/构建入口：`build, lint, serve`

关键目录：
- `src/components`
- `src/router`
- `src/store`
- `src/views`
- `src/views/Home/components`
- `src/views/Home2/components`

路由入口：
- `/` in `src/router/index.js`
- `/home` in `src/router/index.js`
- `/home2` in `src/router/index.js`
- `/test` in `src/router/index.js`
- `/about` in `src/router/index.js`

页面样本：
- `src/App.vue`
- `src/components/AnnualSales/index.vue`
- `src/components/CategorySales/index.vue`
- `src/components/Common/Box.vue`
- `src/components/Common/Frame.vue`
- `src/components/Common/Scroll.vue`
- `src/components/Common/VueEcharts.vue`
- `src/components/Common/baseTemplate.vue`
- `src/components/Common/commonMap.vue`
- `src/components/Completion/index.vue`
- `src/components/DailySales/index.vue`
- `src/components/DisplayHeader/index.vue`
- `src/components/FlowDirection/index copy.vue`
- `src/components/FlowDirection/index.vue`
- `src/components/Overall/index.vue`
- `src/components/StarProduct/index.vue`
- ... 另有 42 项

组件/库样本：
- `src/components/AnnualSales/index.vue`
- `src/components/CategorySales/index.vue`
- `src/components/Common/Box.vue`
- `src/components/Common/Frame.vue`
- `src/components/Common/Scroll.vue`
- `src/components/Common/VueEcharts.vue`
- `src/components/Common/baseTemplate.vue`
- `src/components/Common/commonMap.vue`
- `src/components/Common/createGuid.js`
- `src/components/Completion/index.vue`
- `src/components/DailySales/index.vue`
- `src/components/DisplayHeader/index.vue`
- `src/components/FlowDirection/index copy.vue`
- `src/components/FlowDirection/index.vue`
- `src/components/Overall/index.vue`
- `src/components/StarProduct/index.vue`
- ... 另有 39 项

API/后端接口样本：
- 未发现

GIS/地图/可视化线索：
- `public/map/map-gl.css`
- `public/map/map-gl.js`
- `public/static/data/style.json`
- `public/static/map.css`
- `public/static/map/map-gl.css`
- `public/static/map/map-gl.js`
- `public/static/test.json`
- `src/assets/data/map.js`
- `src/assets/data/style.json`
- `src/components/Common/Scroll.vue`
- `src/components/Common/commonMap.vue`
- `src/components/Common/createGuid.js`
- `src/components/FlowDirection/index copy.vue`
- `src/components/FlowDirection/index.vue`
- `src/components/dialog/mdDialog.vue`
- `src/components/dialog/smDialog.vue`
- ... 另有 20 项

配置文件线索：
- `babel.config.js`
- `vue.config.js`

敏感关键词线索：
- `README.md`
- `public/js/jsmpeg.js`
- `public/map/map-gl.css`
- `public/map/map-gl.js`
- `public/static/map/map-gl.css`
- `public/static/map/map-gl.js`
- `src/assets/css/font.css`
- `src/components/Common/commonMap.vue`

### xinfang/xinfang

- 类型：`java`
- 资产价值：信访业务链路资产，适合抽业务对象、权限结构、工单流转和后台页面。
- 依赖样本：`cetc, spring-boot-dependencies, druid-spring-boot-starter, UserAgentUtils, pagehelper-spring-boot-starter, oshi-core, springfox-swagger2, swagger-annotations, swagger-models, springfox-swagger-ui, commons-io, commons-fileupload`
- 脚本/构建入口：`未发现`

关键目录：
- `cetc-admin/src/main/java/com/cetc/web/controller`
- `cetc-admin/src/main/java/com/cetc/web/jxxf/controller`
- `cetc-admin/src/main/java/com/cetc/web/jxxf/mapper`
- `cetc-admin/src/main/java/com/cetc/web/jxxf/service`
- `cetc-admin/src/main/resources/mapper`
- `cetc-common/src/main/java/com/cetc/common/core/controller`
- `cetc-framework/src/main/java/com/cetc/framework/web/service`
- `cetc-generator/src/main/java/com/ruoyi/generator/controller`
- `cetc-generator/src/main/java/com/ruoyi/generator/mapper`
- `cetc-generator/src/main/java/com/ruoyi/generator/service`
- ... 另有 20 项

路由入口：
- `/` in `cetc-ui/src/permission.js`
- `/` in `cetc-ui/src/permission.js`
- `/401` in `cetc-ui/src/permission.js`
- `*` in `cetc-ui/src/store/modules/permission.js`
- `/redirect` in `cetc-ui/src/router/index.js`
- `/redirect/:path(.*)` in `cetc-ui/src/router/index.js`
- `/login` in `cetc-ui/src/router/index.js`
- `/404` in `cetc-ui/src/router/index.js`
- `/401` in `cetc-ui/src/router/index.js`
- `index` in `cetc-ui/src/router/index.js`
- `/user` in `cetc-ui/src/router/index.js`
- `profile` in `cetc-ui/src/router/index.js`
- `/dict` in `cetc-ui/src/router/index.js`
- `type/data/:dictId(\\d+)` in `cetc-ui/src/router/index.js`
- ... 另有 4 项

页面样本：
- `cetc-ui/src/App.vue`
- `cetc-ui/src/components/Breadcrumb/index.vue`
- `cetc-ui/src/components/Editor/index.vue`
- `cetc-ui/src/components/Hamburger/index.vue`
- `cetc-ui/src/components/HeaderSearch/index.vue`
- `cetc-ui/src/components/IconSelect/index.vue`
- `cetc-ui/src/components/Pagination/index.vue`
- `cetc-ui/src/components/PanThumb/index.vue`
- `cetc-ui/src/components/RightPanel/index.vue`
- `cetc-ui/src/components/RuoYi/Doc/index.vue`
- `cetc-ui/src/components/RuoYi/Git/index.vue`
- `cetc-ui/src/components/Screenfull/index.vue`
- `cetc-ui/src/components/SizeSelect/index.vue`
- `cetc-ui/src/components/SvgIcon/index.vue`
- `cetc-ui/src/components/ThemePicker/index.vue`
- `cetc-ui/src/layout/components/AppMain.vue`
- ... 另有 48 项

组件/库样本：
- `cetc-ui/src/components/Breadcrumb/index.vue`
- `cetc-ui/src/components/Editor/index.vue`
- `cetc-ui/src/components/Hamburger/index.vue`
- `cetc-ui/src/components/HeaderSearch/index.vue`
- `cetc-ui/src/components/IconSelect/index.vue`
- `cetc-ui/src/components/IconSelect/requireIcons.js`
- `cetc-ui/src/components/Pagination/index.vue`
- `cetc-ui/src/components/PanThumb/index.vue`
- `cetc-ui/src/components/RightPanel/index.vue`
- `cetc-ui/src/components/RuoYi/Doc/index.vue`
- `cetc-ui/src/components/RuoYi/Git/index.vue`
- `cetc-ui/src/components/Screenfull/index.vue`
- `cetc-ui/src/components/SizeSelect/index.vue`
- `cetc-ui/src/components/SvgIcon/index.vue`
- `cetc-ui/src/components/ThemePicker/index.vue`
- `cetc-ui/src/layout/components/AppMain.vue`
- ... 另有 14 项

API/后端接口样本：
- `"/tool/gen"` in `cetc-generator/src/main/java/com/ruoyi/generator/controller/GenController.java`
- `"/list"` in `cetc-generator/src/main/java/com/ruoyi/generator/controller/GenController.java`
- `value = "/{talbleId}"` in `cetc-generator/src/main/java/com/ruoyi/generator/controller/GenController.java`
- `"/db/list"` in `cetc-generator/src/main/java/com/ruoyi/generator/controller/GenController.java`
- `value = "/column/{talbleId}"` in `cetc-generator/src/main/java/com/ruoyi/generator/controller/GenController.java`
- `"/importTable"` in `cetc-generator/src/main/java/com/ruoyi/generator/controller/GenController.java`
- `"/{tableIds}"` in `cetc-generator/src/main/java/com/ruoyi/generator/controller/GenController.java`
- `"/preview/{tableId}"` in `cetc-generator/src/main/java/com/ruoyi/generator/controller/GenController.java`
- `"/download/{tableName}"` in `cetc-generator/src/main/java/com/ruoyi/generator/controller/GenController.java`
- `"/genCode/{tableName}"` in `cetc-generator/src/main/java/com/ruoyi/generator/controller/GenController.java`
- `"/batchGenCode"` in `cetc-generator/src/main/java/com/ruoyi/generator/controller/GenController.java`
- `/login` in `cetc-ui/src/api/login.js`
- `/getInfo` in `cetc-ui/src/api/login.js`
- `/logout` in `cetc-ui/src/api/login.js`
- `/captchaImage` in `cetc-ui/src/api/login.js`
- `/getRouters` in `cetc-ui/src/api/menu.js`
- ... 另有 144 项

GIS/地图/可视化线索：
- `cetc-admin/src/main/java/com/cetc/web/controller/common/CaptchaController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/common/CommonController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/monitor/ServerController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/monitor/SysLogininforController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/monitor/SysOperlogController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/monitor/SysUserOnlineController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/system/SysConfigController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/system/SysDeptController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/system/SysDictDataController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/system/SysDictTypeController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/system/SysLoginController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/system/SysMenuController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/system/SysNoticeController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/system/SysPostController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/system/SysProfileController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/system/SysRoleController.java`
- ... 另有 104 项

配置文件线索：
- `cetc-admin/src/main/java/com/cetc/web/controller/system/SysConfigController.java`
- `cetc-admin/src/main/java/com/cetc/web/core/config/SwaggerConfig.java`
- `cetc-admin/src/main/java/com/cetc/web/jxxf/config/AopConfig.java`
- `cetc-admin/src/main/java/com/cetc/web/jxxf/config/MainDataSourceConfigure.java`
- `cetc-admin/src/main/java/com/cetc/web/jxxf/config/PageHelperConfig.java`
- `cetc-admin/src/main/java/com/cetc/web/jxxf/config/RedisConfig.java`
- `cetc-admin/src/main/java/com/cetc/web/jxxf/config/UreportConfig.java`
- `cetc-admin/src/main/resources/META-INF/spring-devtools.properties`
- `cetc-admin/src/main/resources/application-druid.yml`
- `cetc-admin/src/main/resources/application.yml`
- `cetc-admin/src/main/resources/config.properties`
- `cetc-admin/src/main/resources/i18n/messages.properties`
- `cetc-admin/src/main/resources/mybatis/mybatis-config.xml`
- `cetc-common/src/main/java/com/cetc/common/config/CetcConfig.java`
- ... 另有 31 项

敏感关键词线索：
- `cetc-admin/src/main/java/com/cetc/web/controller/monitor/SysUserOnlineController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/system/SysLoginController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/system/SysMenuController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/system/SysProfileController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/system/SysRoleController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/system/SysUserController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/tool/TestController.java`
- `cetc-admin/src/main/java/com/cetc/web/core/config/SwaggerConfig.java`
- `cetc-admin/src/main/java/com/cetc/web/jxxf/aspect/CacheAspect.java`
- `cetc-admin/src/main/java/com/cetc/web/jxxf/constant/ConstantSql.java`
- `cetc-admin/src/main/java/com/cetc/web/jxxf/controller/AlertEventController.java`
- `cetc-admin/src/main/java/com/cetc/web/jxxf/controller/JxxfController.java`
- `cetc-admin/src/main/java/com/cetc/web/jxxf/controller/LetterController.java`
- `cetc-admin/src/main/java/com/cetc/web/jxxf/controller/PersonController.java`
- ... 另有 106 项

### xinfang/xinfang-web-admin

- 类型：`frontend`
- 资产价值：信访业务链路资产，适合抽业务对象、权限结构、工单流转和后台页面。
- 依赖样本：`@riophae/vue-treeselect, @vue/cli-plugin-babel, @vue/cli-plugin-eslint, @vue/cli-plugin-unit-jest, @vue/cli-service, @vue/test-utils, autoprefixer, axios, babel-eslint, babel-jest, babel-plugin-dynamic-import-node, chalk`
- 脚本/构建入口：`build:prod, build:stage, dev, lint, new, preview, svgo, test:ci, test:unit`

关键目录：
- `src/api`
- `src/components`
- `src/layout/components`
- `src/router`
- `src/store`
- `src/store/modules`
- `src/views`
- `src/views/components`

路由入口：
- `/` in `src/permission.js`
- `/adminindex` in `src/permission.js`
- `/` in `src/permission.js`
- `/401` in `src/permission.js`
- `*` in `src/store/modules/permission.js`
- `/redirect` in `src/router/index.js`
- `/redirect/:path(.*)` in `src/router/index.js`
- `/adminlogin` in `src/router/index.js`
- `/404` in `src/router/index.js`
- `/401` in `src/router/index.js`
- `adminindex` in `src/router/index.js`
- `/user` in `src/router/index.js`
- `profile` in `src/router/index.js`
- `/dict` in `src/router/index.js`
- ... 另有 5 项

页面样本：
- `src/App.vue`
- `src/components/Breadcrumb/index.vue`
- `src/components/Editor/index.vue`
- `src/components/Hamburger/index.vue`
- `src/components/HeaderSearch/index.vue`
- `src/components/IconSelect/index.vue`
- `src/components/Pagination/index.vue`
- `src/components/PanThumb/index.vue`
- `src/components/RightPanel/index.vue`
- `src/components/RuoYi/Doc/index.vue`
- `src/components/RuoYi/Git/index.vue`
- `src/components/Screenfull/index.vue`
- `src/components/SizeSelect/index.vue`
- `src/components/SvgIcon/index.vue`
- `src/components/ThemePicker/index.vue`
- `src/layout/components/AppMain.vue`
- ... 另有 48 项

组件/库样本：
- `src/components/Breadcrumb/index.vue`
- `src/components/Editor/index.vue`
- `src/components/Hamburger/index.vue`
- `src/components/HeaderSearch/index.vue`
- `src/components/IconSelect/index.vue`
- `src/components/IconSelect/requireIcons.js`
- `src/components/Pagination/index.vue`
- `src/components/PanThumb/index.vue`
- `src/components/RightPanel/index.vue`
- `src/components/RuoYi/Doc/index.vue`
- `src/components/RuoYi/Git/index.vue`
- `src/components/Screenfull/index.vue`
- `src/components/SizeSelect/index.vue`
- `src/components/SvgIcon/index.vue`
- `src/components/ThemePicker/index.vue`
- `src/layout/components/AppMain.vue`
- ... 另有 14 项

API/后端接口样本：
- `/cetc/api/login` in `src/api/login.js`
- `/cetc/api/getInfo` in `src/api/login.js`
- `/cetc/api/logout` in `src/api/login.js`
- `/cetc/api/captchaImage` in `src/api/login.js`
- `/cetc/api/getRouters` in `src/api/menu.js`
- `/monitor/online/list` in `src/api/monitor/online.js`
- `/monitor/online/` in `src/api/monitor/online.js`
- `/monitor/job/list` in `src/api/monitor/job.js`
- `/monitor/job/` in `src/api/monitor/job.js`
- `/monitor/job` in `src/api/monitor/job.js`
- `/monitor/job/export` in `src/api/monitor/job.js`
- `/monitor/job/changeStatus` in `src/api/monitor/job.js`
- `/monitor/job/run` in `src/api/monitor/job.js`
- `/monitor/server` in `src/api/monitor/server.js`
- `/monitor/operlog/list` in `src/api/monitor/operlog.js`
- `/monitor/operlog/` in `src/api/monitor/operlog.js`
- ... 另有 68 项

GIS/地图/可视化线索：
- `README.md`
- `src/assets/icons/index.js`
- `src/components/IconSelect/requireIcons.js`
- `src/layout/components/Navbar.vue`
- `src/layout/components/Sidebar/index.vue`
- `src/layout/index.vue`
- `src/permission.js`
- `src/store/modules/permission.js`
- `src/utils/generator/html.js`
- `src/utils/generator/icon.json`
- `src/utils/generator/render.js`
- `src/utils/index.js`
- `src/utils/validate.js`
- `src/utils/zipdownload.js`
- `src/views/components/icons/element-icons.js`
- `src/views/components/icons/svg-icons.js`
- ... 另有 15 项

配置文件线索：
- `babel.config.js`
- `src/api/system/config.js`
- `src/assets/icons/svgo.yml`
- `src/utils/generator/config.js`
- `vue.config.js`

敏感关键词线索：
- `.eslintrc.js`
- `package.json`
- `src/api/login.js`
- `src/api/monitor/online.js`
- `src/api/system/user.js`
- `src/assets/styles/ruoyi.scss`
- `src/components/Editor/index.vue`
- `src/components/HeaderSearch/index.vue`
- `src/components/SizeSelect/index.vue`
- `src/components/SvgIcon/index.vue`
- `src/layout/components/Settings/index.vue`
- `src/layout/components/TagsView/index.vue`
- `src/layout/mixin/ResizeHandler.js`
- `src/permission.js`
- ... 另有 22 项

## 下一步动作

- `jun-dd-web` 和 `cetc-ui/bi-ui`：优先抽取通用可视化组件、地图页面、图表封装。
- `gis-map-sdk` 和 `gis-map-sdk-cesium`：沉淀 SDK 能力边界、初始化流程、图层/实体/工具函数清单。
- `cgpt2.0` 链路：按移动端、后端、大屏拆成城市治理业务知识。
- `xinfang` 链路：按业务对象、流程状态、后台权限和页面结构拆成信访业务知识。
- 带敏感关键词线索的项目：只记录风险文件路径和风险类型，不把配置原文进入公开知识库。
