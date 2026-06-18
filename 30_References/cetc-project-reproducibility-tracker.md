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
| `xinfang/xinfang-web-admin` | `master` | 12.22.12 | `npm install` | `npm run dev -- --port 8080` | `npm run build:prod` | 待验证 |
| `cetc-ui/bi-ui` | `sdk_0918_dev` | 10.24.1 | `npm install` | `npm run docs:dev` | `npm run docs:build` / `npm run pack` | 待验证 |
| `jun-dd-web` | `202004_dev` | 10.24.1 | `npm install` | `npm run dev` | `npm run build` | 待验证 |
| `BeijingDaxing/cetc-moniwa-ui` | `MXSSO` | 8.17.0 初筛，8.9.4 精确复现 | `npm ci` | `npm run dev` | `npm run build` / `mvn package` | 待验证 |

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
| 备选 Node | `v14.21.3`，当前未安装 |

验证步骤：

```bash
source ~/.nvm/nvm.sh
nvm use 12.22.12
node -v
npm -v
npm install
npm run dev -- --port 8080
npm run build:prod
git status --short
```

记录栏：

| 检查点 | 结果 | 备注 |
| --- | --- | --- |
| Node 切换 | 待验证 |  |
| 依赖安装 | 待验证 | 无锁文件，可能生成 `package-lock.json` |
| 开发服务 | 待验证 | 默认端口 80，建议改用 8080 |
| 构建 | 待验证 |  |
| 业务接口 | 待验证 | 代理依赖内网后端 |
| 是否产生文件改动 | 待验证 |  |

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
npm install
npm run docs:dev
npm run docs:build
npm run pack
git status --short
```

记录栏：

| 检查点 | 结果 | 备注 |
| --- | --- | --- |
| Node 切换 | 待验证 |  |
| 依赖安装 | 待验证 | 无锁文件，依赖体量大 |
| 文档站启动 | 待验证 | `docs:dev` 风险低于 demo |
| 文档站构建 | 待验证 | `docs:build` |
| 组件打包 | 待验证 | `pack` |
| demo 启动 | 待验证 | 代理依赖内网 `/biapi` |
| 是否产生文件改动 | 待验证 |  |

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
| 首选 Node | `v8.9.4`，当前未安装 |
| 初筛 Node | `v8.17.0`，当前已安装 |
| Maven 前端插件 | Node `v8.9.4`，npm `5.6.0` |

验证步骤：

```bash
source ~/.nvm/nvm.sh
nvm use 8.17.0
node -v
npm -v
npm ci
npm run dev
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
| Node 切换 | 待验证 | 先用 8.17.0 初筛 |
| 精确 Node 8.9.4 | 待补齐 | 与 `pom.xml` 一致 |
| npm ci | 待验证 | 有锁文件，优先 `npm ci` |
| 开发服务 | 待验证 | 默认端口 10013 |
| npm 构建 | 待验证 | 输出到 `target/public` |
| Maven 可用性 | 待补齐 | 当前 `mvn` 不在 PATH |
| Maven 仓库可达 | 待验证 | 依赖 CETC 内网仓库 |
| 是否产生文件改动 | 待验证 |  |

## 后续 9 步建议

1. 检查并补齐 Node 8.9.4、14.21.3。
2. 检查 Maven 安装和 PATH。
3. 对 `cetc-moniwa-ui` 执行 `npm ci` 初筛。
4. 对 `xinfang-web-admin` 执行 Node 12 下的安装验证。
5. 对 `bi-ui` 执行 Node 10 下的文档站安装/启动验证。
6. 对 `jun-dd-web` 执行 Node 10 下的安装验证。
7. 汇总失败日志，归类为 Node 版本、依赖源、内网服务、构建脚本四类。
8. 根据验证结果提出 `.nvmrc` 和 README 改进建议。
9. 将验证结果同步到知识库网页并推送部署。
