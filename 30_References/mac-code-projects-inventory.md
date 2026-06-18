---
title: cuizihao 目录代码项目盘点
tags: [reference, code, inventory]
created: 2026-06-18
source: /Users/cuizihao
related: []
---

# cuizihao 目录代码项目盘点

## 扫描范围

- 根目录：`/Users/cuizihao`
- 实际扫描入口：`/Users/cuizihao/Code`, `/Users/cuizihao/SUTPC`, `/Users/cuizihao/OGE`, `/Users/cuizihao/Documents`, `/Users/cuizihao/Desktop`, `/Users/cuizihao/Downloads`, `/Users/cuizihao/jf`
- 项目信号：`.git`、`package.json`、`pyproject.toml`、`requirements.txt`、`go.mod`、`Cargo.toml`、`pom.xml`、`build.gradle*`、`composer.json`、`Gemfile`、`CMakeLists.txt`、`Makefile`
- 已排除：`Library`、`.cursor`、`.gradle`、`.nvm`、`.cache`、`node_modules`、构建产物、依赖目录、媒体目录等

## 总览

- 识别到代码项目：73 个
- 无权限或无法读取路径：0 个

## 按顶层目录统计

| 顶层目录 | 项目数 |
| --- | ---: |
| `Downloads` | 40 |
| `SUTPC` | 14 |
| `Desktop` | 8 |
| `OGE` | 8 |
| `Code` | 2 |
| `~/jf` | 1 |

## 按技术信号统计

| 类型 | 项目数 |
| --- | ---: |
| `javascript` | 36 |
| `python` | 25 |
| `cmake` | 8 |
| `make` | 5 |
| `java-maven` | 3 |
| `git` | 1 |
| `go` | 1 |
| `java-gradle` | 1 |
| `php` | 1 |

## 项目清单

| 路径 | 类型 | 信号文件 |
| --- | --- | --- |
| `~/Code/cuizihao` | `git` | `.git` |
| `~/Code/cuizihao/openclaw` | `go`, `java-gradle`, `javascript`, `python` | `.git`, `build.gradle.kts`, `go.mod`, `package.json`, `pyproject.toml` |
| `~/Desktop/桌面整理_2026-06-07/文件夹/asdf/桌面 - 崔子豪的MacBook Pro/.du..4JtkUO23xj/test-vue` | `javascript` | `.git`, `package.json` |
| `~/Desktop/桌面整理_2026-06-07/文件夹/asdf/桌面 - 崔子豪的MacBook Pro/cesium-workshop-master` | `javascript` | `package.json` |
| `~/Desktop/桌面整理_2026-06-07/文件夹/asdf/桌面 - 崔子豪的MacBook Pro/draggable-example-master` | `javascript` | `package.json` |
| `~/Desktop/桌面整理_2026-06-07/文件夹/asdf/桌面 - 崔子豪的MacBook Pro/loan-master/loan-admin-api` | `javascript` | `package.json` |
| `~/Desktop/桌面整理_2026-06-07/文件夹/asdf/桌面 - 崔子豪的MacBook Pro/loan-master/loan-app-api` | `javascript` | `package.json` |
| `~/Desktop/桌面整理_2026-06-07/文件夹/asdf/桌面 - 崔子豪的MacBook Pro/loan-master/loan-sub-admin-api` | `javascript` | `package.json` |
| `~/Desktop/桌面整理_2026-06-07/文件夹/asdf/桌面 - 崔子豪的MacBook Pro/tfjs-examples-master` | `javascript`, `python` | `package.json`, `requirements.txt` |
| `~/Desktop/桌面整理_2026-06-07/文件夹/asdf/桌面 - 崔子豪的MacBook Pro/归档` | `javascript` | `package.json` |
| `~/Downloads/Cesium-1.47` | `javascript` | `package.json` |
| `~/Downloads/Cesium-1.48` | `javascript` | `package.json` |
| `~/Downloads/DeepSegmentor-master` | `python` | `requirements.txt` |
| `~/Downloads/DXY-2019-nCoV-Crawler-master` | `python` | `requirements.txt` |
| `~/Downloads/echartsLayer-master` | `javascript` | `package.json` |
| `~/Downloads/examples-master/cpp/autograd` | `cmake` | `CMakeLists.txt` |
| `~/Downloads/examples-master/cpp/custom-dataset` | `cmake` | `CMakeLists.txt` |
| `~/Downloads/examples-master/cpp/dcgan` | `cmake` | `CMakeLists.txt` |
| `~/Downloads/examples-master/cpp/distributed` | `cmake` | `CMakeLists.txt` |
| `~/Downloads/examples-master/cpp/mnist` | `cmake` | `CMakeLists.txt` |
| `~/Downloads/examples-master/cpp/regression` | `cmake` | `CMakeLists.txt` |
| `~/Downloads/examples-master/cpp/transfer-learning` | `cmake` | `CMakeLists.txt` |
| `~/Downloads/examples-master/dcgan` | `python` | `requirements.txt` |
| `~/Downloads/examples-master/distributed/ddp` | `python` | `requirements.txt` |
| `~/Downloads/examples-master/distributed/rpc/batch` | `python` | `requirements.txt` |
| `~/Downloads/examples-master/distributed/rpc/ddp_rpc` | `python` | `requirements.txt` |
| `~/Downloads/examples-master/distributed/rpc/pipeline` | `python` | `requirements.txt` |
| `~/Downloads/examples-master/distributed/rpc/rl` | `python` | `requirements.txt` |
| `~/Downloads/examples-master/distributed/rpc/rnn` | `python` | `requirements.txt` |
| `~/Downloads/examples-master/fx/native_interpreter` | `cmake` | `CMakeLists.txt` |
| `~/Downloads/examples-master/imagenet` | `python` | `requirements.txt` |
| `~/Downloads/examples-master/mnist` | `python` | `requirements.txt` |
| `~/Downloads/examples-master/mnist_hogwild` | `python` | `requirements.txt` |
| `~/Downloads/examples-master/reinforcement_learning` | `python` | `requirements.txt` |
| `~/Downloads/examples-master/snli` | `python` | `requirements.txt` |
| `~/Downloads/examples-master/time_sequence_prediction` | `python` | `requirements.txt` |
| `~/Downloads/examples-master/vae` | `python` | `requirements.txt` |
| `~/Downloads/examples-master/word_language_model` | `python` | `requirements.txt` |
| `~/Downloads/flask-master/docs` | `make`, `python` | `Makefile`, `requirements.txt` |
| `~/Downloads/gdal-3.2.2/doc` | `make`, `python` | `Makefile`, `requirements.txt` |
| `~/Downloads/gdal-3.2.2/frmts/pcidsk/sdk` | `make` | `Makefile` |
| `~/Downloads/gdal-3.2.2/swig/java` | `java-maven` | `pom.xml` |
| `~/Downloads/gdal-3.2.2/swig/perl` | `make` | `Makefile` |
| `~/Downloads/mapbox-gl-js-cgcs2000` | `javascript` | `package.json` |
| `~/Downloads/Object-Recognition-Using-TensorFlow.js-master/server` | `javascript` | `package.json` |
| `~/Downloads/openfoam-OpenFOAM-v2312/wmake/src` | `make` | `Makefile` |
| `~/Downloads/simple-icons-master` | `javascript`, `php` | `composer.json`, `package.json` |
| `~/Downloads/uni-app-master` | `javascript` | `package.json` |
| `~/Downloads/vue-iclient-master` | `javascript` | `package.json` |
| `~/Downloads/yolov7-tfjs-master` | `javascript` | `package.json` |
| `~/jf` | `javascript` | `.git`, `package.json` |
| `~/OGE/oge-computation-ogc` | `java-maven` | `.git`, `pom.xml` |
| `~/OGE/oge-data-import` | `python` | `.git`, `requirements.txt` |
| `~/OGE/oge-server` | `java-maven` | `.git`, `pom.xml` |
| `~/OGE/oge-vector-process` | `python` | `.git`, `requirements.txt` |
| `~/OGE/oge-web` | `javascript` | `.git`, `package.json` |
| `~/OGE/oge-web-edu` | `javascript` | `.git`, `package.json` |
| `~/OGE/oge-web2` | `javascript` | `.git`, `package.json` |
| `~/OGE/split` | `python` | `requirements.txt` |
| `~/SUTPC/Code/cdos-front` | `javascript` | `.git`, `package.json` |
| `~/SUTPC/Code/chaozongWebDist` | `javascript` | `.git`, `package.json` |
| `~/SUTPC/Code/components` | `javascript` | `.git`, `package.json` |
| `~/SUTPC/Code/demo-echarts` | `javascript` | `.git`, `package.json` |
| `~/SUTPC/Code/demo-vue3` | `javascript` | `.git`, `package.json` |
| `~/SUTPC/Code/develop-portal` | `javascript` | `.git`, `package.json` |
| `~/SUTPC/Code/iv-admin-web` | `javascript` | `.git`, `package.json` |
| `~/SUTPC/Code/template-bigscreen-vue3` | `javascript` | `.git`, `package.json` |
| `~/SUTPC/Code/template-bigscreen-vue3/public/static/theme/dark/mars3d-cesium` | `javascript` | `package.json` |
| `~/SUTPC/Code/template-mobile-vue3` | `javascript` | `.git`, `package.json` |
| `~/SUTPC/Code/template-pc-vue3` | `javascript` | `.git`, `package.json` |
| `~/SUTPC/Code/vehicle-inspection-python` | `javascript`, `python` | `.git`, `package.json`, `requirements.txt` |
| `~/SUTPC/test/gaodeZuobiao` | `javascript` | `package.json` |
| `~/SUTPC/test/slope-ui-admin-vue3` | `javascript` | `.git`, `package.json` |
