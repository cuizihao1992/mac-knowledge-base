---
title: CETC 自动资产抽取报告
tags: [reference, code, cetc, archive, generated]
created: 2026-06-23
source: /Users/cuizihao/CETC/Project
related: [CETC 删除前资产抽取清单, CETC 旧项目业务价值与架构判断]
---

# CETC 自动资产抽取报告

> 生成时间：2026-06-23T03:49:25.361681+00:00

## 总览

- 扫描项目：21 个
- JSON 输出：`outputs/cetc-asset-extraction.json`
- Markdown 输出：`outputs/cetc-asset-extraction.md`

| 建议动作 | 数量 |
| --- | ---: |
| `保留` | 4 |
| `保留到抽取完成` | 5 |
| `先脱敏后保留` | 1 |
| `先脱敏后归档` | 3 |
| `归档` | 8 |

## 清理优先级

| 项目 | 业务价值 | 建议动作 | 配置线索 | 敏感线索 |
| --- | --- | --- | ---: | ---: |
| `1.2-project-network-security-java` | 网络安全业务 | `归档` | 1 | 30 |
| `1.2-project-network-security-web` | 网络安全业务 | `归档` | 5 | 30 |
| `BeijingDaxing/cetc-moniwa-ui` | 监测预警 / 大屏 | `先脱敏后归档` | 0 | 25 |
| `brain` | 监测预警 / 大屏 | `归档` | 4 | 9 |
| `cetc-ui/bi-ui` | GIS / BI / 地图资产 | `保留` | 4 | 9 |
| `cgpt2.0/city-manage-h5` | 城市治理业务链 | `保留到抽取完成` | 2 | 9 |
| `cgpt2.0/city-manage-server` | 城市治理业务链 | `保留到抽取完成` | 1 | 30 |
| `cgpt2.0/city-mange-ui-web` | 城市治理业务链 | `先脱敏后归档` | 7 | 30 |
| `cgpt2.0/e-city-big` | 城市治理业务链 | `保留到抽取完成` | 2 | 0 |
| `gis/gis-bigdata-etl` | GIS / BI / 地图资产 | `归档` | 0 | 0 |
| `gis/gis-map-develop-platform` | GIS / BI / 地图资产 | `先脱敏后保留` | 5 | 17 |
| `gis/gis-map-sdk` | GIS / BI / 地图资产 | `保留` | 8 | 13 |
| `gis/gis-map-sdk-cesium` | GIS / BI / 地图资产 | `保留` | 0 | 3 |
| `gis/gisopenplatform-admin` | GIS / BI / 地图资产 | `归档` | 1 | 30 |
| `gis/urban-virtual-reality-fusion-simulation-platform` | GIS / BI / 地图资产 | `归档` | 4 | 0 |
| `jun-dd-web` | GIS / BI / 地图资产 | `保留` | 12 | 30 |
| `smartCity/java` | 智慧城市业务 | `归档` | 2 | 9 |
| `smartCity/wepy` | 智慧城市业务 | `归档` | 2 | 0 |
| `xinfang/xinfang` | 信访业务链 | `保留到抽取完成` | 10 | 30 |
| `xinfang/xinfang-web` | 信访业务链 | `先脱敏后归档` | 11 | 14 |
| `xinfang/xinfang-web-admin` | 信访业务链 | `保留到抽取完成` | 7 | 17 |

## 项目明细

### 1.2-project-network-security-java

- 业务价值：网络安全业务
- 建议动作：`归档`
- README：`未发现`
- 前端页/组件样本数：0
- API 文件样本数：0
- 后端 Controller/Service/Mapper 样本数：35
- 配置文件线索数：1
- 敏感关键词线索数：30


关键目录：
- `cetc-security-master/cetc-boot-base-common/src/main/java/com/cetc/city/common/api`
- `cetc-security-master/cetc-boot-base-common/src/main/java/com/cetc/city/common/system/api`
- `cetc-security-master/cetc-boot-base-common/src/main/java/com/cetc/city/common/system/base/controller`
- `cetc-security-master/cetc-boot-base-common/src/main/java/com/cetc/city/common/system/base/service`
- `cetc-security-master/cetc-boot-base-common/src/main/java/com/cetc/city/common/system/controller`
- `cetc-security-master/cetc-boot-module-system/src/main/java/com/cetc/city/allNet/controller`
- `cetc-security-master/cetc-boot-module-system/src/main/java/com/cetc/city/allNet/mapper`
- `cetc-security-master/cetc-boot-module-system/src/main/java/com/cetc/city/allNet/service`
- ... 另有 27 项

API 样本：
- 未发现

后端样本：
- `cetc-security-master/cetc-boot-base-common/src/main/java/com/cetc/city/common/system/base/controller/JeecgController.java`
- `cetc-security-master/cetc-boot-base-common/src/main/java/com/cetc/city/common/system/base/service/JeecgService.java`
- `cetc-security-master/cetc-boot-base-common/src/main/java/com/cetc/city/common/system/controller/CommonController.java`
- `cetc-security-master/cetc-boot-module-system/src/main/java/com/cetc/city/allNet/controller/KtLoopholeController.java`
- `cetc-security-master/cetc-boot-module-system/src/main/java/com/cetc/city/allNet/controller/KtThreatenController.java`
- `cetc-security-master/cetc-boot-module-system/src/main/java/com/cetc/city/allNet/mapper/KtLoopholeMapper.java`
- `cetc-security-master/cetc-boot-module-system/src/main/java/com/cetc/city/allNet/mapper/KtThreatenMapper.java`
- `cetc-security-master/cetc-boot-module-system/src/main/java/com/cetc/city/allNet/service/IKtLoopholeService.java`
- ... 另有 27 项

配置线索：
- `cetc-security-master/cetc-boot-module-system/src/main/resources/application.yml`

敏感关键词线索：
- `cetc-security-master/cetc-boot-base-common/src/main/java/com/cetc/city/common/constant/CommonConstant.java`
- `cetc-security-master/cetc-boot-base-common/src/main/java/com/cetc/city/common/constant/DataBaseConstant.java`
- `cetc-security-master/cetc-boot-base-common/src/main/java/com/cetc/city/common/system/api/ISysBaseAPI.java`
- `cetc-security-master/cetc-boot-base-common/src/main/java/com/cetc/city/common/system/controller/CommonController.java`
- `cetc-security-master/cetc-boot-base-common/src/main/java/com/cetc/city/common/system/util/JwtUtil.java`
- `cetc-security-master/cetc-boot-base-common/src/main/java/com/cetc/city/common/system/vo/ComboModel.java`
- `cetc-security-master/cetc-boot-base-common/src/main/java/com/cetc/city/common/system/vo/DynamicDataSourceModel.java`
- `cetc-security-master/cetc-boot-base-common/src/main/java/com/cetc/city/common/system/vo/LoginUser.java`
- ... 另有 22 项

### 1.2-project-network-security-web

- 业务价值：网络安全业务
- 建议动作：`归档`
- README：`README.md`
- 前端页/组件样本数：25
- API 文件样本数：5
- 后端 Controller/Service/Mapper 样本数：0
- 配置文件线索数：5
- 敏感关键词线索数：30

- package：`vue-antd-jeecg`，脚本：`build, lint, pre, serve`

README 摘要：

> # Ant Design cityIE Vue 当前最新版本： 2.0.2（发布日期：20190708） ## Overview 基于 [Ant Design of Vue](https://vuecomponent.github.io/ant-design-vue/docs/vue/introduce-cn/) 实现的 Ant Design Pro Vue 版 cityIE-boot 的前段 UI 框架，采用前后端分离方案，提供强大代码生成器的快速开发平台。 前端页面代码和后端功能代码一键生成，不需要写任何代码，保持 cityIE 一贯的强大！！ #### 前端技术 - 基础框架：[ant-design-vue](https://github.com/vueComponent/ant-design-vue) - Ant Design Of Vue 实现 - JavaScript 框架：Vue - Webpack - node - yarn - eslint - @vue/cli 3.2

关键目录：
- `src/api`
- `src/components`
- `src/router`
- `src/store`
- `src/store/modules`
- `src/views`
- `src/views/big/allNet/components`
- `src/views/big/preventionStatus/components`
- ... 另有 24 项

API 样本：
- `src/api/GroupRequest.js`
- `src/api/api.js`
- `src/api/index.js`
- `src/api/login.js`
- `src/api/manage.js`

后端样本：
- 未发现

配置线索：
- `babel.config.js`
- `idea.config.js`
- `src/config/router.config.js`
- `src/jsconfig.json`
- `vue.config.js`

敏感关键词线索：
- `src/api/api.js`
- `src/api/index.js`
- `src/api/login.js`
- `src/cas/sso.js`
- `src/components/bpm/ProcessInstPicModal.vue`
- `src/components/jeecg/JImageUpload.vue`
- `src/components/jeecg/JUpload.vue`
- `src/components/jeecgbiz/JSelectMultiUser.vue`
- ... 另有 22 项

### BeijingDaxing/cetc-moniwa-ui

- 业务价值：监测预警 / 大屏
- 建议动作：`先脱敏后归档`
- README：`未发现`
- 前端页/组件样本数：25
- API 文件样本数：22
- 后端 Controller/Service/Mapper 样本数：0
- 配置文件线索数：0
- 敏感关键词线索数：25

- package：`warningplatform`，脚本：`build, dev, lint, start`
- Maven：`cect-moniwa-ui`

关键目录：
- `src/api`
- `src/components`
- `src/pages`
- `src/pages/ecological-environment/components`
- `src/pages/layout/components`
- `src/pages/monitoring/components`
- `src/router`
- `src/store`
- ... 另有 1 项

API 样本：
- `src/api/callback.js`
- `src/api/ecologicalRelevance.js`
- `src/api/economic.js`
- `src/api/general.js`
- `src/api/login.js`
- `src/api/popDetail.js`
- `src/api/system/LogManagement.js`
- `src/api/system/access.js`
- ... 另有 14 项

后端样本：
- 未发现

配置线索：
- 未发现

敏感关键词线索：
- `package-lock.json`
- `src/App.vue`
- `src/api/callback.js`
- `src/api/economic.js`
- `src/api/login.js`
- `src/api/system/subsystem.js`
- `src/api/system/user.js`
- `src/components/map/showImgAndCheckOutEvent.js`
- ... 另有 17 项

### brain

- 业务价值：监测预警 / 大屏
- 建议动作：`归档`
- README：`README.md`
- 前端页/组件样本数：25
- API 文件样本数：25
- 后端 Controller/Service/Mapper 样本数：0
- 配置文件线索数：4
- 敏感关键词线索数：9

- package：`integrated-info-rc`，脚本：`build, dev, lint, precommit, prettier`

README 摘要：

> # R16E R16E ## [蓝狐](https://lanhuapp.com/web/#/item/project/product?pid=9b5087f9-f1f2-49e5-8255-394e7edc819c&versionId=0a3abe7d-983b-47cd-acb6-3de30cd2e57c&docId=92cf074a-6781-4f31-99e1-c474f458ae82&docType=axure&pageId=895e99314a094a39b3de72bb08f4c552&image_id=92cf074a-6781-4f31-99e1-c474f458ae82&parentId=0c139630-2363-44ce-af1f-ceccea76f3c3) ## [接口文档,注意切换 ip](http://10.0.17.114:8080/swagger-ui/index.html#/) ## Install ```js npm install ``` ## Q

关键目录：
- `src/common/api`
- `src/components`
- `src/components/GisMap/api`
- `src/components/GisMap/components`
- `src/pages`
- `src/router`
- `src/store`
- `src/store/modules`

API 样本：
- `src/common/api/chartApi.js`
- `src/common/api/index.js`
- `src/common/api/login.js`
- `src/common/api/system/alarm.js`
- `src/common/api/system/app.js`
- `src/common/api/system/child.js`
- `src/common/api/system/config.js`
- `src/common/api/system/course.js`
- ... 另有 17 项

后端样本：
- 未发现

配置线索：
- `commitlint.config.js`
- `jest.config.js`
- `src/common/api/system/config.js`
- `src/utils/gisConfig.js`

敏感关键词线索：
- `src/common/api/login.js`
- `src/common/api/system/user.js`
- `src/components/GisMap/api/api.js`
- `src/components/GisMap/index_test.vue`
- `src/lang/en-US.js`
- `src/lang/zh-CN.js`
- `src/pages/login.vue`
- `src/store/modules/user.js`
- ... 另有 1 项

### cetc-ui/bi-ui

- 业务价值：GIS / BI / 地图资产
- 建议动作：`保留`
- README：`README.md`
- 前端页/组件样本数：25
- API 文件样本数：1
- 后端 Controller/Service/Mapper 样本数：0
- 配置文件线索数：4
- 敏感关键词线索数：9

- package：`compass-ui`，脚本：`build:prd, demo:build, demo:dev, docs:build, docs:dev, lint, pack, plop, precommit, prettier`

README 摘要：

> # jun-dd CETC BI ## Install ```js npm install ``` ## Quick Start ```js npm run dev npm run build ``` ## Commit 提交规范 ### 说明 - commit 信息应符合下方规范，不符合规范的不允许提交 - commit 时会进行 tslint 校验，lint 不通过的不允许提交 ### 规范 ```js <type>: <subject> ``` 注意冒号后面有空格 ### type 用于说明 commit 的类别，只允许使用下面 7 个标识。 - feat：新功能（feature） - fix：修补 bug - docs：文档（documentation） - style： 格式（不影响代码运行的变动） - refactor：重构（即不是新增功能，也不是修改 bug 的代码变动） - test：增加测试 - chore：构建过程或辅助工具的变动 如果 type 为 feat 和 f

关键目录：
- `src/common/api`
- `src/components`
- `src/components/Booklet/BiCanvas/components`
- `src/components/Booklet/ItemSettings/item/components`
- `src/components/Echarts/components`
- `src/components/Gis/components`
- `src/pages`
- `src/router`
- ... 另有 1 项

API 样本：
- `src/common/api/index.js`

后端样本：
- 未发现

配置线索：
- `commitlint.config.js`
- `jest.config.js`
- `src/config.js`
- `src/utils/gisConfig.js`

敏感关键词线索：
- `src/components/Booklet/BiCanvas/components/mixins/index.js`
- `src/components/Gis/Gis.vue`
- `src/components/Gis/components/Arcgis.js`
- `src/components/Gis/components/Cesium.js`
- `src/components/Gis/components/extensions/CesiumUtils/index.js`
- `src/components/Gis/components/testData.js`
- `src/components/Gis/index.vue`
- `src/lang/en-US.js`
- ... 另有 1 项

### cgpt2.0/city-manage-h5

- 业务价值：城市治理业务链
- 建议动作：`保留到抽取完成`
- README：`README.md`
- 前端页/组件样本数：25
- API 文件样本数：1
- 后端 Controller/Service/Mapper 样本数：0
- 配置文件线索数：2
- 敏感关键词线索数：9


README 摘要：

> # E-CITY-H5 需要使用 hbuildx 这个款 IDE 打开项目 如果需要发布到线上环境,请先修改配置文件 config.service.js ,然后点击编辑器的发布 ## Jeecg-Boot-Uniapp（APP开发框架） JEECG BOOT APP 移动解决方案，采用uniapp框架，一份代码解决多终端适配（APP、小程序、H5）。 [![AUR](https://img.shields.io/badge/license-Apache%20License%202.0-blue.svg)](https://github.com/zhangdaiscott/jeecg-boot/blob/master/LICENSE) [![](https://img.shields.io/badge/Author-JEECG团队-orange.svg)](http://www.jeecg.com) [![](https://img.shields.io/badge/version-1.0

关键目录：
- `api`
- `common/router`
- `common/router/modules`
- `common/service`
- `components`
- `pages`
- `plugin/colorui/components`
- `store`

API 样本：
- `api/api.js`

后端样本：
- 未发现

配置线索：
- `common/service/config.service.js`
- `plugin/uni-simple-router/helpers/config.js`

敏感关键词线索：
- `README.md`
- `common/router/index.js`
- `common/service/service.js`
- `common/util/constants.js`
- `pages/login/login.vue`
- `pages/user/about.vue`
- `pages/user/people.vue`
- `setting.json`
- ... 另有 1 项

### cgpt2.0/city-manage-server

- 业务价值：城市治理业务链
- 建议动作：`保留到抽取完成`
- README：`未发现`
- 前端页/组件样本数：0
- API 文件样本数：0
- 后端 Controller/Service/Mapper 样本数：35
- 配置文件线索数：1
- 敏感关键词线索数：30

- Maven：`aliyun Repository`

关键目录：
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/api`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/api`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/base/controller`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/base/service`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/controller`
- `cetc-boot-module-system/src/main/java/com/cetc/city/cmanage/aiexecute/service`
- `cetc-boot-module-system/src/main/java/com/cetc/city/cmanage/bigCenter/controller`
- `cetc-boot-module-system/src/main/java/com/cetc/city/cmanage/deviceCenter/controller`
- ... 另有 27 项

API 样本：
- 未发现

后端样本：
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/base/controller/JeecgController.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/base/service/JeecgService.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/controller/CommonController.java`
- `cetc-boot-module-system/src/main/java/com/cetc/city/cmanage/aiexecute/service/AIExecuteService.java`
- `cetc-boot-module-system/src/main/java/com/cetc/city/cmanage/bigCenter/controller/BigCenterController.java`
- `cetc-boot-module-system/src/main/java/com/cetc/city/cmanage/deviceCenter/controller/RTSPController.java`
- `cetc-boot-module-system/src/main/java/com/cetc/city/cmanage/deviceCenter/controller/TbAiDefaultParamController.java`
- `cetc-boot-module-system/src/main/java/com/cetc/city/cmanage/deviceCenter/controller/TbDeviceController.java`
- ... 另有 27 项

配置线索：
- `cetc-boot-module-system/src/main/resources/application.yml`

敏感关键词线索：
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/constant/CommonConstant.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/constant/DataBaseConstant.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/api/ISysBaseAPI.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/controller/CommonController.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/util/JwtUtil.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/vo/ComboModel.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/vo/DynamicDataSourceModel.java`
- `cetc-boot-base-common/src/main/java/com/cetc/city/common/system/vo/LoginUser.java`
- ... 另有 22 项

### cgpt2.0/city-mange-ui-web

- 业务价值：城市治理业务链
- 建议动作：`先脱敏后归档`
- README：`README.md`
- 前端页/组件样本数：25
- API 文件样本数：10
- 后端 Controller/Service/Mapper 样本数：0
- 配置文件线索数：7
- 敏感关键词线索数：30

- package：`cetc`，脚本：`build, lint, lint-fix, pre, serve`
- Maven：`cetc-cgpt-ui`

README 摘要：

> # e-city 说明文档 **[代码仓库](http://gt.cetccity.com:8090/cgpt2.0)** ### e-city-big **大屏** - 使用 2k 构建,所有 px 需要按照高保真比例缩放,例如 高保真 1920*1080,一个容器的 width:400px;height:200px,项目中需要 * 2 - 开发环境: vscode **编辑器** + node + npm/cnpm/yarn **推荐使用: cnpm / yarn** + git + chrome - 技术栈: vue + ant-design-vue + lodash + axios + mapbox **子豪构建的 gis 地图** - master 为 思超版本高保真构建 - dev 为 玉兰版本高保真构建 - master 部署时需要注意: vue.config.js 中 `publicPath: process.env.NODE_ENV === "production" ?

关键目录：
- `src/api`
- `src/components`
- `src/router`
- `src/store`
- `src/store/modules`
- `src/views`
- `src/views/cetc-dev/rule-engine/components`
- `src/views/cgpt/components`
- ... 另有 8 项

API 样本：
- `src/api/GroupRequest.js`
- `src/api/action.js`
- `src/api/alertCenter.js`
- `src/api/api.js`
- `src/api/developer.js`
- `src/api/dict.js`
- `src/api/index.js`
- `src/api/login.js`
- ... 另有 2 项

后端样本：
- 未发现

配置线索：
- `babel.config.js`
- `idea.config.js`
- `jsconfig.json`
- `src/config/router.config.js`
- `src/mixins/DeviceAiConfigMixin.js`
- `src/views/cetc-dev/rule-engine/js/config.js`
- `vue.config.js`

敏感关键词线索：
- `README.md`
- `src/api/api.js`
- `src/api/index.js`
- `src/api/login.js`
- `src/cas/sso.js`
- `src/components/Editor/index.vue`
- `src/components/jeecg/JImageUpload.vue`
- `src/components/jeecg/JUpload.vue`
- ... 另有 22 项

### cgpt2.0/e-city-big

- 业务价值：城市治理业务链
- 建议动作：`保留到抽取完成`
- README：`README.md`
- 前端页/组件样本数：25
- API 文件样本数：0
- 后端 Controller/Service/Mapper 样本数：0
- 配置文件线索数：2
- 敏感关键词线索数：0

- package：`e-city`，脚本：`build, lint, serve`

README 摘要：

> # 智慧城管 大屏数据可视化 基于vue2和echarts5的数据大屏案例 ## Project setup ``` npm install ``` ### Compiles and hot-reloads for development ``` npm run serve ``` ### Compiles and minifies for production ``` npm run build ``` ## Echarts 相关图标参考 ### [水平柱状图 - 高发事件类型TOP 5](https://www.makeapie.com/editor.html?c=xtb1sE6zH) ### [3D环饼图 - 处置情况](https://www.makeapie.com/editor.html?c=xX9xcKXRjq) ### [曲顶柱状图 - 事件的时间分布](https://www.makeapie.com/editor.html?c=xpE5FVGymy) ### [雷达图

关键目录：
- `src/components`
- `src/router`
- `src/store`
- `src/views`
- `src/views/Home/components`
- `src/views/Home2/components`

API 样本：
- 未发现

后端样本：
- 未发现

配置线索：
- `babel.config.js`
- `vue.config.js`

敏感关键词线索：
- 未发现

### gis/gis-bigdata-etl

- 业务价值：GIS / BI / 地图资产
- 建议动作：`归档`
- README：`README.md`
- 前端页/组件样本数：0
- API 文件样本数：0
- 后端 Controller/Service/Mapper 样本数：0
- 配置文件线索数：0
- 敏感关键词线索数：0


README 摘要：

> GIS空间大数据ETL项目

关键目录：
- 未发现

API 样本：
- 未发现

后端样本：
- 未发现

配置线索：
- 未发现

敏感关键词线索：
- 未发现

### gis/gis-map-develop-platform

- 业务价值：GIS / BI / 地图资产
- 建议动作：`先脱敏后保留`
- README：`README.md`
- 前端页/组件样本数：0
- API 文件样本数：0
- 后端 Controller/Service/Mapper 样本数：0
- 配置文件线索数：5
- 敏感关键词线索数：17


README 摘要：

> GIS开发平台

关键目录：
- 未发现

API 样本：
- 未发现

后端样本：
- 未发现

配置线索：
- `example2d/gis/config/HKlayerconfig.json`
- `example2d/gis/config/HKmapconfig.json`
- `example2d/gis/config/layerconfig.json`
- `example2d/gis/config/mapconfig.json`
- `example2d/gis/config/mapconfig2.json`

敏感关键词线索：
- `example2d/gis/config/HKlayerconfig.json`
- `example2d/gis/config/HKmapconfig.json`
- `example2d/gis/config/layerconfig.json`
- `example2d/gis/config/mapconfig.json`
- `example2d/gis/config/mapconfig2.json`
- `example2d/gis/sdk/token.js`
- `example2d/js/jquery.js`
- `example2d/test/ArcGIS-with-Echarts/jquery.js`
- ... 另有 9 项

### gis/gis-map-sdk

- 业务价值：GIS / BI / 地图资产
- 建议动作：`保留`
- README：`README.md`
- 前端页/组件样本数：0
- API 文件样本数：0
- 后端 Controller/Service/Mapper 样本数：0
- 配置文件线索数：8
- 敏感关键词线索数：13

- package：`gismap-sdk`，脚本：`build, dev, repl, server, test, test:cover, test:watch`

README 摘要：

> # gis-map-sdk gis快速开发框架

关键目录：
- `src/service`

API 样本：
- 未发现

后端样本：
- 未发现

配置线索：
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
- `debug/sdk/gismap.min.js`
- `src/config/LayerNode.js`
- `src/config/MapConfig.js`
- `src/layer/Layer.js`
- `src/layer/TDMapTileLayer.js`
- `src/map/Global.js`
- ... 另有 5 项

### gis/gis-map-sdk-cesium

- 业务价值：GIS / BI / 地图资产
- 建议动作：`保留`
- README：`README.md`
- 前端页/组件样本数：0
- API 文件样本数：0
- 后端 Controller/Service/Mapper 样本数：0
- 配置文件线索数：0
- 敏感关键词线索数：3


README 摘要：

> gis-map-sdk-3d

关键目录：
- 未发现

API 样本：
- 未发现

后端样本：
- 未发现

配置线索：
- 未发现

敏感关键词线索：
- `src/js/EMap/core/model.js`
- `src/js/main/main.js`
- `src/js/main/measure.js`

### gis/gisopenplatform-admin

- 业务价值：GIS / BI / 地图资产
- 建议动作：`归档`
- README：`README.md`
- 前端页/组件样本数：0
- API 文件样本数：0
- 后端 Controller/Service/Mapper 样本数：35
- 配置文件线索数：1
- 敏感关键词线索数：30

- Maven：`aliyun nexus`

README 摘要：

> # GISOpenPlatform-Admin GIS开放平台后台

关键目录：
- `coordinateTransformApi/src/main/java/com/cetc/city/controller`
- `demo/src/main/java/com/cetc/city/controller`
- `demo/src/main/java/com/cetc/city/mapper`
- `demo/src/main/java/com/cetc/city/service`
- `gaodeApi/src/main/java/com/cetc/city/controller`
- `portalPage/src/main/java/com/cetc/city/controller`
- `portalPage/src/main/java/com/cetc/city/mapper`
- `portalPage/src/main/java/com/cetc/city/service`
- ... 另有 12 项

API 样本：
- 未发现

后端样本：
- `coordinateTransformApi/src/main/java/com/cetc/city/controller/coordinateController.java`
- `demo/src/main/java/com/cetc/city/controller/DemoController.java`
- `demo/src/main/java/com/cetc/city/mapper/DemoMapper.java`
- `demo/src/main/java/com/cetc/city/service/DemoService.java`
- `gaodeApi/src/main/java/com/cetc/city/controller/gaodeController.java`
- `portalPage/src/main/java/com/cetc/city/controller/GisMenuController.java`
- `portalPage/src/main/java/com/cetc/city/mapper/GisMenuMapper.java`
- `portalPage/src/main/java/com/cetc/city/service/GisMenuService.java`
- ... 另有 27 项

配置线索：
- `app/src/main/resources/application.yml`

敏感关键词线索：
- `app/src/main/java/com/cetc/city/ConvergedCommunicationApplication.java`
- `app/src/main/resources/application-druid.yml`
- `app/src/main/resources/application.yml`
- `system/src/main/java/com/cetc/city/common/constant/Constants.java`
- `system/src/main/java/com/cetc/city/common/exception/user/UserPasswordNotMatchException.java`
- `system/src/main/java/com/cetc/city/common/utils/SecurityUtils.java`
- `system/src/main/java/com/cetc/city/common/utils/Sms.java`
- `system/src/main/java/com/cetc/city/common/utils/security/Md5Utils.java`
- ... 另有 22 项

### gis/urban-virtual-reality-fusion-simulation-platform

- 业务价值：GIS / BI / 地图资产
- 建议动作：`归档`
- README：`README.md`
- 前端页/组件样本数：7
- API 文件样本数：0
- 后端 Controller/Service/Mapper 样本数：0
- 配置文件线索数：4
- 敏感关键词线索数：0

- package：`gis`，脚本：`build, lint, serve`

关键目录：
- `src/components`
- `src/router`
- `src/store`
- `src/views`

API 样本：
- 未发现

后端样本：
- 未发现

配置线索：
- `.env.development`
- `.env.production`
- `babel.config.js`
- `vue.config.js`

敏感关键词线索：
- 未发现

### jun-dd-web

- 业务价值：GIS / BI / 地图资产
- 建议动作：`保留`
- README：`README.md`
- 前端页/组件样本数：25
- API 文件样本数：5
- 后端 Controller/Service/Mapper 样本数：0
- 配置文件线索数：12
- 敏感关键词线索数：30

- package：`jun-dd`，脚本：`build, build:prd, compress, dev, lint, pack, precommit, prettier, tar`

README 摘要：

> # jun-dd CETC BI ## Install ```js npm install ``` ## Quick Start ```js npm run dev npm run build ``` ## Commit 提交规范 ### 说明 - commit 信息应符合下方规范，不符合规范的不允许提交 - commit 时会进行 tslint 校验，lint 不通过的不允许提交 ### 规范 ```js <type>: <subject> ``` 注意冒号后面有空格 ### type 用于说明 commit 的类别，只允许使用下面 7 个标识。 - feat：新功能（feature） - fix：修补 bug - docs：文档（documentation） - style： 格式（不影响代码运行的变动） - refactor：重构（即不是新增功能，也不是修改 bug 的代码变动） - test：增加测试 - chore：构建过程或辅助工具的变动 如果 type 为 feat 和 f

关键目录：
- `src/common/api`
- `src/components`
- `src/components/Tinymce/components`
- `src/components/TyTable/components`
- `src/components/charts_backup/api`
- `src/components/charts_backup/components`
- `src/components/charts_backup/components/GIS/components`
- `src/components/charts_backup/store`
- ... 另有 16 项

API 样本：
- `src/common/api/Veteran.js`
- `src/common/api/index.js`
- `src/common/api/newIndex.js`
- `src/common/api/other.js`
- `src/components/charts_backup/api/index.js`

后端样本：
- 未发现

配置线索：
- `commitlint.config.js`
- `jest.config.js`
- `src/components/charts_backup/config/config-bar.js`
- `src/components/charts_backup/config/config-line.js`
- `src/components/charts_backup/config/config-pie.js`
- `src/components/charts_backup/graph/config/baseConfig.js`
- `src/components/echarts/config/config.js`
- `src/components/echarts/config/pieconfig.js`
- ... 另有 4 项

敏感关键词线索：
- `src/common/api/index.js`
- `src/common/api/other.js`
- `src/components/Tinymce/components/EditorImage.vue`
- `src/components/chart-build/baiduMapCustomization.vue`
- `src/components/chart-build/giscustomization.vue`
- `src/components/charts_backup/components/GIS/minxJS/BMapMethod.js`
- `src/components/charts_backup/components/table/table.vue`
- `src/components/charts_backup/readme.md`
- ... 另有 22 项

### smartCity/java

- 业务价值：智慧城市业务
- 建议动作：`归档`
- README：`未发现`
- 前端页/组件样本数：0
- API 文件样本数：0
- 后端 Controller/Service/Mapper 样本数：14
- 配置文件线索数：2
- 敏感关键词线索数：9

- Maven：`unifiedplatform`

关键目录：
- `src/main/java/com/cetc/unifiedplatform/controller`
- `src/main/java/com/cetc/unifiedplatform/service`
- `src/main/resources/mapper`

API 样本：
- 未发现

后端样本：
- `src/main/java/com/cetc/unifiedplatform/controller/AppController.java`
- `src/main/java/com/cetc/unifiedplatform/controller/BannerController.java`
- `src/main/java/com/cetc/unifiedplatform/controller/BkdAppController.java`
- `src/main/java/com/cetc/unifiedplatform/controller/BkdCompanyController.java`
- `src/main/java/com/cetc/unifiedplatform/controller/CategoryController.java`
- `src/main/java/com/cetc/unifiedplatform/controller/CompanyController.java`
- `src/main/java/com/cetc/unifiedplatform/controller/FileController.java`
- `src/main/java/com/cetc/unifiedplatform/controller/IdxController.java`
- ... 另有 6 项

配置线索：
- `src/main/resources/app.properties`
- `src/main/resources/application.yml`

敏感关键词线索：
- `src/main/java/com/cetc/unifiedplatform/constant/Const.java`
- `src/main/java/com/cetc/unifiedplatform/controller/AppController.java`
- `src/main/java/com/cetc/unifiedplatform/controller/BkdAppController.java`
- `src/main/java/com/cetc/unifiedplatform/controller/UserController.java`
- `src/main/java/com/cetc/unifiedplatform/dto/PicToken.java`
- `src/main/java/com/cetc/unifiedplatform/entity/gen/UserGen.java`
- `src/main/java/com/cetc/unifiedplatform/util/FileUploadUtils.java`
- `src/main/resources/app.properties`
- ... 另有 1 项

### smartCity/wepy

- 业务价值：智慧城市业务
- 建议动作：`归档`
- README：`未发现`
- 前端页/组件样本数：0
- API 文件样本数：2
- 后端 Controller/Service/Mapper 样本数：0
- 配置文件线索数：2
- 敏感关键词线索数：0

- package：`dkznh`，脚本：`build, dev, test`

关键目录：
- `src/api`
- `src/pages`

API 样本：
- `src/api/api.js`
- `src/api/promise.js`

后端样本：
- 未发现

配置线索：
- `jsconfig.json`
- `wepy.config.js`

敏感关键词线索：
- 未发现

### xinfang/xinfang

- 业务价值：信访业务链
- 建议动作：`保留到抽取完成`
- README：`README.md`
- 前端页/组件样本数：25
- API 文件样本数：18
- 后端 Controller/Service/Mapper 样本数：35
- 配置文件线索数：10
- 敏感关键词线索数：30

- Maven：`cetc`

README 摘要：

> ## 平台简介 * 前端采用Vue、Element UI。 * 后端采用Spring Boot、Spring Security、Redis & Jwt。 * 权限认证使用Jwt，支持多终端认证系统。 * 支持加载动态权限菜单，多方式轻松权限控制。 * 高效率开发，使用代码生成器可以一键生成前后端代码。 * 提供了一个Oracle版本[cetc-Vue-Oracle](https://github.com/yangzongzhuan/cetc-Vue-Oracle)，保持同步更新。 * 不分离版本，请移步[cetc](https://gitee.com/y_project/cetc)，微服务版本，请移步[cetc-Cloud](https://gitee.com/y_project/cetc-Cloud) * 感谢[Vue-Element-Admin](https://github.com/PanJiaChen/vue-element-admin)，[eladmin-web](https:

关键目录：
- `cetc-admin/src/main/java/com/cetc/web/controller`
- `cetc-admin/src/main/java/com/cetc/web/jxxf/controller`
- `cetc-admin/src/main/java/com/cetc/web/jxxf/mapper`
- `cetc-admin/src/main/java/com/cetc/web/jxxf/service`
- `cetc-admin/src/main/resources/mapper`
- `cetc-common/src/main/java/com/cetc/common/core/controller`
- `cetc-framework/src/main/java/com/cetc/framework/web/service`
- `cetc-generator/src/main/java/com/ruoyi/generator/controller`
- ... 另有 22 项

API 样本：
- `cetc-ui/src/api/login.js`
- `cetc-ui/src/api/menu.js`
- `cetc-ui/src/api/monitor/job.js`
- `cetc-ui/src/api/monitor/jobLog.js`
- `cetc-ui/src/api/monitor/logininfor.js`
- `cetc-ui/src/api/monitor/online.js`
- `cetc-ui/src/api/monitor/operlog.js`
- `cetc-ui/src/api/monitor/server.js`
- ... 另有 10 项

后端样本：
- `cetc-admin/src/main/java/com/cetc/web/controller/common/CaptchaController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/common/CommonController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/monitor/ServerController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/monitor/SysLogininforController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/monitor/SysOperlogController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/monitor/SysUserOnlineController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/system/SysConfigController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/system/SysDeptController.java`
- ... 另有 27 项

配置线索：
- `cetc-admin/src/main/resources/application.yml`
- `cetc-jxxf/src/main/resources/application.properties`
- `cetc-jxxf/src/main/resources/application.yml`
- `cetc-ui/.env.development`
- `cetc-ui/.env.production`
- `cetc-ui/.env.staging`
- `cetc-ui/babel.config.js`
- `cetc-ui/src/api/system/config.js`
- ... 另有 2 项

敏感关键词线索：
- `cetc-admin/src/main/java/com/cetc/web/controller/monitor/SysUserOnlineController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/system/SysLoginController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/system/SysMenuController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/system/SysProfileController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/system/SysRoleController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/system/SysUserController.java`
- `cetc-admin/src/main/java/com/cetc/web/controller/tool/TestController.java`
- `cetc-admin/src/main/java/com/cetc/web/core/config/SwaggerConfig.java`
- ... 另有 22 项

### xinfang/xinfang-web

- 业务价值：信访业务链
- 建议动作：`先脱敏后归档`
- README：`README.md`
- 前端页/组件样本数：25
- API 文件样本数：25
- 后端 Controller/Service/Mapper 样本数：0
- 配置文件线索数：11
- 敏感关键词线索数：14

- package：`micro_home_h5`，脚本：`build, build:stage, dev, lint`

README 摘要：

> # micro_home_h5 ## Project setup ``` yarn install ``` ### Compiles and hot-reloads for development ``` yarn serve ``` ### Compiles and minifies for production ``` yarn build ``` ### Lints and fixes files ``` yarn lint ``` ### Customize configuration See [Configuration Reference](https://cli.vuejs.org/config/). [设计稿地址](https://lanhuapp.com/url/5JzD7-kcjEa) [原型](https://lanhuapp.com/web/#/item/project/product?pid=6afea715-cdab-4bfc-b951-d13fb5aa501

关键目录：
- `src/api`
- `src/common/api`
- `src/components`
- `src/components/searchListModule/components`
- `src/modules`
- `src/modules/api`
- `src/pages`
- `src/pages/components`
- ... 另有 27 项

API 样本：
- `src/api/SpecialPersonnel/importantPeople.js`
- `src/api/common.js`
- `src/api/monitoringPush/oneToFivePush.js`
- `src/api/monitoringPush/overdueWarning.js`
- `src/api/monitoringPush/petitionPush.js`
- `src/api/oneToFive/forecastAndJudgment.js`
- `src/api/oneToFive/overviewSituation.js`
- `src/api/oneToFive/specificAnalysis.js`
- ... 另有 17 项

后端样本：
- 未发现

配置线索：
- `.env.development`
- `.env.production`
- `.env.staging`
- `babel.config.js`
- `src/config.js`
- `src/pages/jxxfPages/overviewSituation/gisJson/letterMapConfig.json`
- `src/pages/jxxfPages/overviewSituation/gisJson/oneToFiveMapConfig.json`
- `src/pages/jxxfPages/overviewSituation/gisJson/oneToFiveMapConfig备份.json`
- ... 另有 3 项

敏感关键词线索：
- `src/api/common.js`
- `src/common/api/other.js`
- `src/components/gis/minxJS/BMapMethod.js`
- `src/main.js`
- `src/pages/login.vue`
- `src/pages/newLogin.vue`
- `src/store/getters.js`
- `src/store/other.js`
- ... 另有 6 项

### xinfang/xinfang-web-admin

- 业务价值：信访业务链
- 建议动作：`保留到抽取完成`
- README：`README.md`
- 前端页/组件样本数：25
- API 文件样本数：18
- 后端 Controller/Service/Mapper 样本数：0
- 配置文件线索数：7
- 敏感关键词线索数：17

- package：`ruoyi`，脚本：`build:prod, build:stage, dev, lint, new, preview, svgo, test:ci, test:unit`

README 摘要：

> ## 开发 ```bash # 克隆项目 git clone https://gitee.com/y_project/RuoYi-Vue # 进入项目目录 cd ruoyi-ui # 安装依赖 npm install # 建议不要直接使用 cnpm 安装依赖，会有各种诡异的 bug。可以通过如下操作解决 npm 下载速度慢的问题 npm install --registry=https://registry.npm.taobao.org # 启动服务 npm run dev ``` 浏览器访问 http://localhost:80 ## 发布 ```bash # 构建测试环境 npm run build:stage # 构建生产环境 npm run build:prod ```

关键目录：
- `src/api`
- `src/components`
- `src/layout/components`
- `src/router`
- `src/store`
- `src/store/modules`
- `src/views`
- `src/views/components`

API 样本：
- `src/api/login.js`
- `src/api/menu.js`
- `src/api/monitor/job.js`
- `src/api/monitor/jobLog.js`
- `src/api/monitor/logininfor.js`
- `src/api/monitor/online.js`
- `src/api/monitor/operlog.js`
- `src/api/monitor/server.js`
- ... 另有 10 项

后端样本：
- 未发现

配置线索：
- `.env.development`
- `.env.production`
- `.env.staging`
- `babel.config.js`
- `src/api/system/config.js`
- `src/utils/generator/config.js`
- `vue.config.js`

敏感关键词线索：
- `src/api/login.js`
- `src/api/monitor/online.js`
- `src/api/system/user.js`
- `src/components/Editor/index.vue`
- `src/permission.js`
- `src/store/getters.js`
- `src/store/modules/user.js`
- `src/utils/auth.js`
- ... 另有 9 项
