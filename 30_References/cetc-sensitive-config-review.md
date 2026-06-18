---
title: CETC 敏感配置复核清单
tags: [reference, code, cetc, security, review]
created: 2026-06-19
source: /Users/cuizihao/CETC/Project
related: [CETC 项目整理路线图, CETC 项目健康度报告]
---

# CETC 敏感配置复核清单

## 说明

- 本清单只记录命中文件、关键词类型和处理建议。
- 不记录疑似密钥、token、密码、内网配置的原始值；证据片段已脱敏。
- `高/中/低` 是静态扫描优先级，不等同于确认泄露。

## 扫描范围

- `/Users/cuizihao/CETC/Project/gis/gis-map-develop-platform`
- `/Users/cuizihao/CETC/Project/BeijingDaxing/cetc-moniwa-ui`
- `/Users/cuizihao/CETC/Project/smartCity/java`
- `/Users/cuizihao/CETC/Project/xinfang/xinfang-web-admin`
- `/Users/cuizihao/CETC/Project/cetc-ui/bi-ui`
- `/Users/cuizihao/CETC/Project/jun-dd-web`

## 总览

- 原始命中文件：235 个
- 进入复核清单：106 个

| 风险级别 | 文件数 |
| --- | ---: |
| `高` | 15 |
| `中` | 147 |
| `低` | 73 |

## 关键词类型统计

| 类型 | 文件数 |
| --- | ---: |
| `token` | 143 |
| `internal_ip` | 93 |
| `password` | 58 |
| `secret` | 10 |
| `access_key` | 8 |
| `client_secret` | 6 |
| `private_key` | 1 |

## 按项目统计

| 项目 | 命中文件数 |
| --- | ---: |
| `~/CETC/Project/jun-dd-web` | 97 |
| `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | 68 |
| `~/CETC/Project/gis/gis-map-develop-platform` | 20 |
| `~/CETC/Project/xinfang/xinfang-web-admin` | 20 |
| `~/CETC/Project/cetc-ui/bi-ui` | 17 |
| `~/CETC/Project/smartCity/java` | 13 |

## 复核清单

| 风险 | 项目 | 文件 | 命中类型 | 建议 |
| --- | --- | --- | --- | --- |
| `高` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `src/pages/system/SubSystem.vue` | `client_secret`, `password`, `secret` | 出现密钥类字段名，需要确认是否为真实凭据；公开仓库中应避免保留真实值。 |
| `高` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `src/permission.js` | `client_secret`, `secret`, `token` | 出现密钥类字段名，需要确认是否为真实凭据；公开仓库中应避免保留真实值。 |
| `高` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `static/debug/config/mapconfig.json` | `access_key`, `internal_ip`, `token` | 出现密钥类字段名，需要确认是否为真实凭据；公开仓库中应避免保留真实值。 |
| `高` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `static/debug/config/mapconfig2.json` | `access_key`, `internal_ip`, `token` | 出现密钥类字段名，需要确认是否为真实凭据；公开仓库中应避免保留真实值。 |
| `高` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `static/debug/config/mapconfig_decision.json` | `access_key`, `internal_ip`, `token` | 出现密钥类字段名，需要确认是否为真实凭据；公开仓库中应避免保留真实值。 |
| `高` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `static/js/config.js` | `client_secret`, `internal_ip`, `secret` | 出现密钥类字段名，需要确认是否为真实凭据；公开仓库中应避免保留真实值。 |
| `高` | `~/CETC/Project/gis/gis-map-develop-platform` | `example2d/gis/config/HKmapconfig.json` | `access_key`, `internal_ip` | 出现密钥类字段名，需要确认是否为真实凭据；公开仓库中应避免保留真实值。 |
| `高` | `~/CETC/Project/gis/gis-map-develop-platform` | `example2d/gis/config/mapconfig.json` | `access_key`, `token` | 出现密钥类字段名，需要确认是否为真实凭据；公开仓库中应避免保留真实值。 |
| `高` | `~/CETC/Project/gis/gis-map-develop-platform` | `example2d/gis/config/mapconfig2.json` | `access_key`, `internal_ip`, `token` | 出现密钥类字段名，需要确认是否为真实凭据；公开仓库中应避免保留真实值。 |
| `高` | `~/CETC/Project/gis/gis-map-develop-platform` | `home/doc2d/content/地图.md` | `access_key`, `token` | 出现密钥类字段名，需要确认是否为真实凭据；公开仓库中应避免保留真实值。 |
| `高` | `~/CETC/Project/jun-dd-web` | `src/components/dialog/thirdForm.vue` | `client_secret`, `password`, `secret`, `token` | 出现密钥类字段名，需要确认是否为真实凭据；公开仓库中应避免保留真实值。 |
| `高` | `~/CETC/Project/jun-dd-web` | `src/pages/projects/DBTypes.vue` | `client_secret`, `password`, `secret`, `token` | 出现密钥类字段名，需要确认是否为真实凭据；公开仓库中应避免保留真实值。 |
| `高` | `~/CETC/Project/jun-dd-web` | `src/pages/projects/createData.vue` | `client_secret`, `password`, `secret`, `token` | 出现密钥类字段名，需要确认是否为真实凭据；公开仓库中应避免保留真实值。 |
| `高` | `~/CETC/Project/xinfang/xinfang-web-admin` | `src/utils/generator/render.js` | `access_key`, `password` | 出现密钥类字段名，需要确认是否为真实凭据；公开仓库中应避免保留真实值。 |
| `高` | `~/CETC/Project/xinfang/xinfang-web-admin` | `src/utils/jsencrypt.js` | `private_key` | 出现密钥类字段名，需要确认是否为真实凭据；公开仓库中应避免保留真实值。 |
| `中` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `config/dev.env.js` | `internal_ip` | 配置文件中出现敏感关键词或内网地址，需要确认是否可公开。 |
| `中` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `config/index.js` | `internal_ip` | 配置文件中出现敏感关键词或内网地址，需要确认是否可公开。 |
| `中` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `config/prod.env.js` | `internal_ip` | 配置文件中出现敏感关键词或内网地址，需要确认是否可公开。 |
| `中` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `src/api/ecologicalRelevance.js` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `src/api/popDetail.js` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `src/components/map/popUp/PopCom.vue` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `src/components/map/showImgAndCheckOutEvent.js` | `internal_ip`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `src/components/mapConfig/initMap.vue` | `internal_ip`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `src/components/mapConfig/initMap_decision.vue` | `internal_ip`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `src/pages/layout/components/Navbar.vue` | `internal_ip`, `password`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `src/utils/request.js` | `internal_ip`, `password`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `static/debug/config/layerconfig.json` | `internal_ip`, `token` | 配置文件中出现敏感关键词或内网地址，需要确认是否可公开。 |
| `中` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `static/debug/config/videomapconfig.json` | `internal_ip`, `token` | 配置文件中出现敏感关键词或内网地址，需要确认是否可公开。 |
| `中` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `static/gis/config/mapconfig.xml` | `internal_ip` | 配置文件中出现敏感关键词或内网地址，需要确认是否可公开。 |
| `中` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `static/gis/config/mapconfig_.xml` | `internal_ip` | 配置文件中出现敏感关键词或内网地址，需要确认是否可公开。 |
| `中` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `static/gis/js/main/config/mapConfig.js` | `internal_ip` | 配置文件中出现敏感关键词或内网地址，需要确认是否可公开。 |
| `中` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `static/gis/js/main/main.js` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `static/gis/js/main/main1.js` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `static/gis/js/main/test.js` | `internal_ip`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `static/gis/js/module/layerControl/basegeoLayer/boundary.js` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `static/gis/js/module/layerControl/common/loadUtil.js` | `internal_ip`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `static/gis/js/module/layerControl/futianLayer/dataVisual.js` | `internal_ip`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `static/gis/js/module/layerQuery/featureNearbyQuery.js` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/BeijingDaxing/cetc-moniwa-ui` | `static/gis/js/module/layerQuery/featureNearbyQuery_bak.js` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/cetc-ui/bi-ui` | `examples/main.js` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/cetc-ui/bi-ui` | `src/components/Booklet/ItemSettings/item/components/map/point _temp.vue` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/cetc-ui/bi-ui` | `src/components/Booklet/ItemSettings/item/components/mapConfig.vue` | `internal_ip`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/cetc-ui/bi-ui` | `src/config.js` | `internal_ip` | 配置文件中出现敏感关键词或内网地址，需要确认是否可公开。 |
| `中` | `~/CETC/Project/cetc-ui/bi-ui` | `src/static/GIS/data/jx_all.json` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/cetc-ui/bi-ui` | `src/static/GIS/data/shenshan.json` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/cetc-ui/bi-ui` | `src/static/GIS/layerConfig.json` | `internal_ip`, `token` | 配置文件中出现敏感关键词或内网地址，需要确认是否可公开。 |
| `中` | `~/CETC/Project/cetc-ui/bi-ui` | `src/static/GIS/map_style.json` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/gis/gis-map-develop-platform` | `example2d/gis/config/HKlayerconfig.json` | `internal_ip`, `token` | 配置文件中出现敏感关键词或内网地址，需要确认是否可公开。 |
| `中` | `~/CETC/Project/gis/gis-map-develop-platform` | `example2d/gis/config/dark_style2.json` | `internal_ip` | 配置文件中出现敏感关键词或内网地址，需要确认是否可公开。 |
| `中` | `~/CETC/Project/gis/gis-map-develop-platform` | `example2d/gis/config/getbyCity.json` | `internal_ip` | 配置文件中出现敏感关键词或内网地址，需要确认是否可公开。 |
| `中` | `~/CETC/Project/gis/gis-map-develop-platform` | `example2d/gis/config/gray_style.json` | `internal_ip` | 配置文件中出现敏感关键词或内网地址，需要确认是否可公开。 |
| `中` | `~/CETC/Project/gis/gis-map-develop-platform` | `example2d/gis/config/layerconfig.json` | `internal_ip`, `token` | 配置文件中出现敏感关键词或内网地址，需要确认是否可公开。 |
| `中` | `~/CETC/Project/gis/gis-map-develop-platform` | `home/doc2d/content/Vue.js支持.md` | `internal_ip`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/gis/gis-map-develop-platform` | `home/doc2d/content/图层.md` | `internal_ip`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/gis/gis-map-develop-platform` | `home/doc2d/content/快速入门.md` | `internal_ip`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/gis/gis-map-develop-platform` | `home/doc2d/content/配置ArcGIS开发包.md` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/common/api/index.js` | `internal_ip`, `password`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/CustomizedComponents/JxGraph/graph.vue` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/CustomizedComponents/JxPertition/JxPertition.vue` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/CustomizedComponents/JxPertition/com/customMap.vue` | `internal_ip`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/DemoTemplate/demo1.vue` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/DemoTemplate/demo2.vue` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/DemoTemplate/demo3.vue` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/DemoTemplate/demo4.vue` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/DemoTemplate/smartcity.vue` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/chart-build/baiduMapCustomization.vue` | `internal_ip`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/chart-build/giscustomization.vue` | `internal_ip`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/charts_backup/components/GIS/BDMap.vue` | `internal_ip`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/charts_backup/components/GIS/GDMap.vue` | `internal_ip`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/charts_backup/components/GIS/gis.vue` | `internal_ip`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/charts_backup/components/GIS/gis1.vue` | `internal_ip`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/charts_backup/components/GIS/gis_20200515.vue` | `internal_ip`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/dialog/uploadFile.vue` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/jxInfoHeader/index.vue` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/jxWarnSpeculate/index.vue` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/jxWarnSpeculate/speculateList.vue` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/jxWarnSpeculate/warnInfoList.vue` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/personalPortrait/dialogComponents/tableList.vue` | `internal_ip`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/personalPortrait/graph/processing/controller.js` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/personalPortrait/graph/processing/controller_temp.js` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/photo-booklet/dialog/index.vue` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/photo-booklet/drag-resize-swiperPic/dailog.vue` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/photo-booklet/drag-resize-swiperPic/dailogList.vue` | `internal_ip`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/components/photo-booklet/searchListModule/index.vue` | `internal_ip`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/config.js` | `internal_ip` | 配置文件中出现敏感关键词或内网地址，需要确认是否可公开。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/mixins/html2canvas.js` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/modules/FormDesign/components/componentsConfig.js` | `token` | 配置文件中出现敏感关键词或内网地址，需要确认是否可公开。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/pages/isDelete-isTrue/index.vue` | `internal_ip`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/pages/login/controller/controller.js` | `internal_ip`, `password` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/pages/login/index-old.vue` | `internal_ip`, `password` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/pages/personalCenter/personCenter.vue` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/pages/photo-booklet/_blank-index.vue` | `internal_ip`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/pages/projects/index.vue` | `internal_ip`, `password`, `token` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/static/GIS/data/jx_all.json` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/static/GIS/data/shenshan-cdn.json` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/static/GIS/data/shenshan.json` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/static/GIS/layerConfig.json` | `internal_ip`, `token` | 配置文件中出现敏感关键词或内网地址，需要确认是否可公开。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/static/GIS/map_style.json` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/static/common/js/baseUrl.js` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/static/common/js/baseUrlGis.js` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/jun-dd-web` | `src/store/gis.js` | `internal_ip` | 出现内网 IP 或内网服务地址，迁移环境时需要外置配置。 |
| `中` | `~/CETC/Project/smartCity/java` | `src/main/resources/app.properties` | `internal_ip`, `secret` | 配置文件中出现敏感关键词或内网地址，需要确认是否可公开。 |
| `中` | `~/CETC/Project/smartCity/java` | `src/main/resources/application.yml` | `password` | 配置文件中出现敏感关键词或内网地址，需要确认是否可公开。 |
| `中` | `~/CETC/Project/xinfang/xinfang-web-admin` | `src/utils/generator/config.js` | `password` | 配置文件中出现敏感关键词或内网地址，需要确认是否可公开。 |
| `中` | `~/CETC/Project/xinfang/xinfang-web-admin` | `vue.config.js` | `internal_ip` | 配置文件中出现敏感关键词或内网地址，需要确认是否可公开。 |
| `低` | `~/CETC/Project/jun-dd-web` | `src/modules/FormDesign/components/WidgetConfig.vue` | `token` | 登录、权限、页面或组件里的 token/password 多半是业务字段名，抽查即可。 |

## 高优先级证据片段

### ~/CETC/Project/BeijingDaxing/cetc-moniwa-ui / src/pages/system/SubSystem.vue

- 命中类型：`client_secret`, `password`, `secret`
- 脱敏片段：
  - `perms= ***REDACTED***`
  - `<el-form-item label= ***REDACTED***`
  - `<el-input v-model= ***REDACTED*** />`

### ~/CETC/Project/BeijingDaxing/cetc-moniwa-ui / src/permission.js

- 命中类型：`client_secret`, `secret`, `token`
- 脱敏片段：
  - `getToken,`
  - `} from '***REDACTED***' // get token from cookie`
  - `// const hasToken = ***REDACTED***`

### ~/CETC/Project/BeijingDaxing/cetc-moniwa-ui / static/debug/config/mapconfig.json

- 命中类型：`access_key`, `internal_ip`, `token`
- 脱敏片段：
  - `"***REDACTED***": ***REDACTED***,`
  - `"url": ***REDACTED***,`
  - `"url": ***REDACTED***,`

### ~/CETC/Project/BeijingDaxing/cetc-moniwa-ui / static/debug/config/mapconfig2.json

- 命中类型：`access_key`, `internal_ip`, `token`
- 脱敏片段：
  - `"***REDACTED***": ***REDACTED***,`
  - `"url": ***REDACTED***,`
  - `"url": ***REDACTED***,`

### ~/CETC/Project/BeijingDaxing/cetc-moniwa-ui / static/debug/config/mapconfig_decision.json

- 命中类型：`access_key`, `internal_ip`, `token`
- 脱敏片段：
  - `"***REDACTED***": ***REDACTED***,`
  - `"url": ***REDACTED***,`
  - `"url": ***REDACTED***,`

### ~/CETC/Project/BeijingDaxing/cetc-moniwa-ui / static/js/config.js

- 命中类型：`client_secret`, `internal_ip`, `secret`
- 脱敏片段：
  - `'***REDACTED***'`
  - `env.client_secret = ***REDACTED***`

### ~/CETC/Project/gis/gis-map-develop-platform / example2d/gis/config/HKmapconfig.json

- 命中类型：`access_key`, `internal_ip`
- 脱敏片段：
  - `"url": ***REDACTED***,`
  - `"url": ***REDACTED***,`
  - `"url": ***REDACTED***,`

### ~/CETC/Project/gis/gis-map-develop-platform / example2d/gis/config/mapconfig.json

- 命中类型：`access_key`, `token`
- 脱敏片段：
  - `"url": ***REDACTED***,`
  - `"***REDACTED***": {`

### ~/CETC/Project/gis/gis-map-develop-platform / example2d/gis/config/mapconfig2.json

- 命中类型：`access_key`, `internal_ip`, `token`
- 脱敏片段：
  - `"url": ***REDACTED***,`
  - `"url": ***REDACTED***,`
  - `"url": ***REDACTED***,`

### ~/CETC/Project/gis/gis-map-develop-platform / home/doc2d/content/地图.md

- 命中类型：`access_key`, `token`
- 脱敏片段：
  - `"***REDACTED***": {`
  - `GMap.Global.accessToken = ***REDACTED***;`
  - `GMap.Global.accessToken = ***REDACTED***;`

### ~/CETC/Project/jun-dd-web / src/components/dialog/thirdForm.vue

- 命中类型：`client_secret`, `password`, `secret`, `token`
- 脱敏片段：
  - `<el-option label= ***REDACTED*** value= ***REDACTED***`
  - `<el-option label= ***REDACTED***`
  - `v-if= ***REDACTED***`

### ~/CETC/Project/jun-dd-web / src/pages/projects/DBTypes.vue

- 命中类型：`client_secret`, `password`, `secret`, `token`
- 脱敏片段：
  - `const { username, password, url, databaseType, databaseIp, databasePort, databaseName } = ***REDACTED***;`
  - `password,`
  - `password,`

### ~/CETC/Project/jun-dd-web / src/pages/projects/createData.vue

- 命中类型：`client_secret`, `password`, `secret`, `token`
- 脱敏片段：
  - `const { username, password, databaseType, databaseIp, databasePort, databaseName } = ***REDACTED***;`
  - `password,`
  - `tokenRequestType = ***REDACTED***,`

### ~/CETC/Project/xinfang/xinfang-web-admin / src/utils/generator/render.js

- 命中类型：`access_key`, `password`
- 脱敏片段：
  - `'***REDACTED***'`
  - `+ '***REDACTED***'`

### ~/CETC/Project/xinfang/xinfang-web-admin / src/utils/jsencrypt.js

- 命中类型：`private_key`
- 脱敏片段：
  - `const privateKey = ***REDACTED*** +`
  - `encryptor.setPrivateKey(privateKey)`

## 建议处理

1. 先人工复核高优先级项，确认是否为真实凭据。
2. 对真实凭据进行轮换，并从仓库历史中评估是否需要清理。
3. 对内网地址、SSO、地图服务地址做环境变量或部署配置外置。
4. 对低优先级登录/权限模块命中，确认是业务字段后标记为已复核。
