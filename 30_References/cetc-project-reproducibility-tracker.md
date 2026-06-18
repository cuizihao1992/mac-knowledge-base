# CETC 重点项目复现记录表

> 更新时间：2026-06-19
> 用途：作为后续 4 个重点项目安装、启动、构建验证的统一记录入口。

## 使用原则

- 先验证“能否安装依赖”，再验证“能否启动开发服务”，最后验证“能否构建产物”。
- 首轮不修改业务仓库，不提交自动生成的锁文件。
- 每次验证前后都检查 `git status --short`，确认是否产生了额外改动。
- 业务接口不可达时，只记录为“接口依赖不可达”，不要误判为前端工程不能启动。

## 总览

| 项目 | 当前分支 | 推荐 Node | 安装命令 | 首个验证命令 | 构建命令 | 初始状态 |
| --- | --- | --- | --- | --- | --- | --- |
| `xinfang/xinfang-web-admin` | `master` | 12.22.12，备选 14.21.3 | `npm install --package-lock=false` | `npm run build:prod` | `npm run build:prod` | 通过 |
| `cetc-ui/bi-ui` | `sdk_0918_dev` | 10.24.1 | `npm install --package-lock=false` | `npm run docs:build` | `npm run docs:build` / `npm run pack` | 部分通过 |
| `jun-dd-web` | `202004_dev` | 10.24.1 | `npm install` | `npm run dev` | `npm run build` | 待验证 |
| `BeijingDaxing/cetc-moniwa-ui` | `MXSSO` | 8.9.4 | `npm install` | `npm run build` | `npm run build` / `mvn package` | 部分通过 |

## 逐项记录

### xinfang / xinfang-web-admin

| 项 | 内容 |
| --- | --- |
| 路径 | `/Users/cuizihao/CETC/Project/xinfang/xinfang-web-admin` |
| package name | `ruoyi` |
| package version | `3.0.0` |
| 当前分支 | `master` |
| 工作区 | 干净 |
| 引擎声明 | `node >=8.9`，`npm >=3.0.0` |
| 锁文件 | 无 |
| 环境文件 | 无 `.nvmrc` / `.node-version` / `.tool-versions` |
| 首选 Node | `v12.22.12` |
| 备选 Node | `v14.21.3`，当前已安装 |

验证步骤：

```bash
source ~/.nvm/nvm.sh
nvm use 12.22.12
node -v
npm -v
npm install --package-lock=false --no-audit --no-fund
npm run dev -- --port 8080
npm run build:prod
git status --short
```

记录栏：

| 检查点 | 结果 | 备注 |
| --- | --- | --- |
| Node 切换 | 通过 | Node 12.22.12，npm 6.14.16 |
| 依赖安装 | 通过 | 安装 2164 个包；使用 `--package-lock=false` 未保留锁文件 |
| 开发服务 | 未执行 | 默认端口 80，建议手动改用 8080 验证 |
| 构建 | 通过 | `npm run build:prod` 成功，输出 `dist` |
| 业务接口 | 待验证 | 代理依赖内网后端 |
| 是否产生文件改动 | 无需恢复 | `node_modules`、`dist`、`package-lock.json` 均被 `.gitignore` 忽略；工作区保持干净 |

构建备注：

- Vue CLI 构建成功，退出码 0。
- 仅有 asset size / entrypoint size warning，未阻断构建。
- `dist` 约 4.2M，`node_modules` 约 420M。

### cetc-ui / bi-ui

| 项 | 内容 |
| --- | --- |
| 路径 | `/Users/cuizihao/CETC/Project/cetc-ui/bi-ui` |
| package name | `compass-ui` |
| package version | `0.0.1` |
| 当前分支 | `sdk_0918_dev` |
| 工作区 | 干净 |
| 引擎声明 | 未声明 |
| 锁文件 | 无 |
| 环境文件 | 无 `.nvmrc` / `.node-version` / `.tool-versions` |
| 首选 Node | `v10.24.1` |
| 备选 Node | `v12.22.12` |

验证步骤：

```bash
source ~/.nvm/nvm.sh
nvm use 10.24.1
node -v
npm -v
npm install --package-lock=false --no-audit --no-fund
npm run docs:dev
npm run docs:build
npm run pack
git status --short
```

记录栏：

| 检查点 | 结果 | 备注 |
| --- | --- | --- |
| Node 切换 | 通过 | Node 10.24.1，npm 6.14.12 |
| 依赖安装 | 通过 | 安装 4108 个包；`node_modules` 约 975M |
| 文档站启动 | 待验证 | `docs:dev` 风险低于 demo |
| 文档站构建 | 失败 | `stylus-loader` 报 `Cannot read property 'stylus' of undefined` |
| 组件打包 | 待验证 | `pack` |
| demo 启动 | 待验证 | 代理依赖内网 `/biapi` |
| 是否产生文件改动 | 无需恢复 | `node_modules`、`package-lock.json` 被 `.gitignore` 忽略；工作区保持干净 |

构建失败摘录：

```text
Module build failed (from ./node_modules/stylus-loader/index.js):
TypeError: Cannot read property 'stylus' of undefined
Error: Failed to compile with errors.
```

实际依赖版本：

| 包 | 实际版本 |
| --- | --- |
| `vuepress` | 1.9.10 |
| `@vuepress/core` | 1.9.10 |
| `stylus-loader` | 3.0.1 |
| `stylus` | 0.54.5 |

判断：

- 安装链路可用，但无锁文件导致依赖解析不可控。
- 安装过程中出现多项 engine mismatch，例如 Cesium 相关依赖要求 Node 22，说明当前依赖树已经被解析到过新的包。
- 文档站失败集中在 VuePress / Stylus loader 链路，优先尝试固定 `stylus-loader`、`stylus` 或恢复历史锁文件。

### jun-dd-web

| 项 | 内容 |
| --- | --- |
| 路径 | `/Users/cuizihao/CETC/Project/jun-dd-web` |
| package name | `jun-dd` |
| package version | `0.0.1` |
| 当前分支 | `202004_dev` |
| 工作区 | 干净 |
| 引擎声明 | 未声明 |
| 锁文件 | 无 |
| 环境文件 | 无 `.nvmrc` / `.node-version` / `.tool-versions` |
| 首选 Node | `v10.24.1` |
| 备选 Node | `v12.22.12` |

验证步骤：

```bash
source ~/.nvm/nvm.sh
nvm use 10.24.1
node -v
npm -v
npm install
npm run dev
npm run build
git status --short
```

记录栏：

| 检查点 | 结果 | 备注 |
| --- | --- | --- |
| Node 切换 | 待验证 |  |
| 依赖安装 | 待验证 | 无锁文件，项目体积约 1.4G |
| 开发服务 | 待验证 | 多个内网代理路径 |
| 构建 | 待验证 | `build` 会继续执行 `tar` |
| GIS 静态资源 | 待验证 | 内置 ArcGIS JS API 4.13 |
| 是否产生文件改动 | 待验证 |  |

### BeijingDaxing / cetc-moniwa-ui

| 项 | 内容 |
| --- | --- |
| 路径 | `/Users/cuizihao/CETC/Project/BeijingDaxing/cetc-moniwa-ui` |
| package name | `warningplatform` |
| package version | `1.0.0` |
| 当前分支 | `MXSSO` |
| 工作区 | 干净 |
| 引擎声明 | `node >=6.0.0`，`npm >=3.0.0` |
| 锁文件 | 有 `package-lock.json` |
| 环境文件 | 无 `.nvmrc` / `.node-version` / `.tool-versions` |
| 首选 Node | `v8.9.4`，当前已安装 |
| 补充 Node | `v8.17.0`，当前已安装 |
| Maven 前端插件 | Node `v8.9.4`，npm `5.6.0` |

验证步骤：

```bash
source ~/.nvm/nvm.sh
nvm use 8.9.4
node -v
npm -v
npm install --no-audit --no-fund
npm run build
git status --short
```

Maven 验证步骤：

```bash
mvn -v
mvn package
```

记录栏：

| 检查点 | 结果 | 备注 |
| --- | --- | --- |
| Node 切换 | 通过 | 使用 8.9.4，与 `pom.xml` 一致 |
| 精确 Node 8.9.4 | 已补齐 | npm 为 5.6.0 |
| npm ci | 不适用 | npm 5.6.0 不支持 `npm ci` |
| npm install | 通过 | 安装 1455 个包；`fsevents` optional dependency 编译失败但被跳过 |
| 开发服务 | 待验证 | 默认端口 10013 |
| npm 构建 | 失败 | 生成了 `target/public`，但 webpack 最终退出 1 |
| Maven 可用性 | 已补齐 | Apache Maven 3.9.9，入口 `/Users/cuizihao/.local/bin/mvn` |
| Maven 仓库可达 | 待验证 | 依赖 CETC 内网仓库 |
| 是否产生文件改动 | 已恢复 | `npm install` 曾改写 `package-lock.json`，已恢复；`node_modules`、`target` 为忽略目录 |

构建失败摘录：

```text
ERROR in ./node_modules/regenerator-runtime/runtime.js
Module parse failed: Unexpected character '�' (1:3)
You may need an appropriate loader to handle this file type.
@ ./node_modules/regenerator-runtime/runtime-module.js
@ ./node_modules/babel-runtime/regenerator/index.js
@ ./src/permission.js
@ ./src/main.js
```

判断：

- 安装链路可用，Node 8.9.4 / npm 5.6.0 能完成依赖安装。
- `fsevents` 失败属于 optional dependency，当前不阻断安装。
- 构建失败更像依赖包文件内容或 npm 缓存/registry 完整性问题，尤其安装阶段出现过 registry integrity 警告。
- 下一次可尝试清理该依赖后重装：删除 `node_modules/regenerator-runtime`，清理 npm 缓存，或切换 registry 后重装。

## 后续 7 步建议

1. 对 `cetc-moniwa-ui` 执行 `npm ci` 初筛。
2. 对 `xinfang-web-admin` 执行 Node 12 下的安装验证。
3. 对 `bi-ui` 执行 Node 10 下的文档站安装/启动验证。
4. 对 `jun-dd-web` 执行 Node 10 下的安装验证。
5. 汇总失败日志，归类为 Node 版本、依赖源、内网服务、构建脚本四类。
6. 根据验证结果提出 `.nvmrc` 和 README 改进建议。
7. 将验证结果同步到知识库网页并推送部署。
