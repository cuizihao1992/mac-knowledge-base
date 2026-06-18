# CETC 本机开发环境基线

> 更新时间：2026-06-19
> 用途：记录当前 Mac 上用于复现 CETC 重点项目的基础环境，作为后续安装、启动、构建验证的参照。

## 机器与系统

| 项 | 当前值 |
| --- | --- |
| 系统 | macOS 13.7.8 |
| 内核 | Darwin 22.6.0 |
| 架构 | x86_64 |
| Shell | `/bin/zsh` |
| Git | 2.23.0 |

## Node / npm / 包管理器

| 工具 | 当前默认版本 | 路径 / 说明 |
| --- | --- | --- |
| Node | v20.10.0 | `/Users/cuizihao/.nvm/versions/node/v20.10.0/bin/node` |
| npm | 10.2.3 | 跟随 Node v20.10.0 |
| yarn | 1.22.21 | 已安装 |
| pnpm | 10.5.2 | 已安装 |
| nvm | 0.39.4 | 已安装，需在 shell 中加载 `~/.nvm/nvm.sh` |

已安装的 nvm Node 版本：

| 版本 | 状态 | 对 CETC 项目的意义 |
| --- | --- | --- |
| v8.17.0 | 已安装 | 可初步验证 `cetc-moniwa-ui`，但不是 `pom.xml` 精确声明的 v8.9.4 |
| v10.24.1 | 已安装 | 适合初步验证 `bi-ui`、`jun-dd-web` |
| v12.22.12 | 已安装 | 适合初步验证 `xinfang-web-admin`、`bi-ui`、`jun-dd-web` |
| v18.18.0 | 已安装 | 可用于新项目，不建议作为老 Vue 项目的首选 |
| v20.10.0 | 当前默认 | 对老 Vue/Webpack 项目风险较高 |
| v22.14.0 / v22.22.0 | 已安装 | 不建议用于首轮复现老项目 |

建议补齐：

- `v8.9.4`：匹配 `BeijingDaxing/cetc-moniwa-ui/pom.xml` 中的 frontend-maven-plugin 配置。
- `v14.21.3`：作为 `xinfang-web-admin` 的备选现代 LTS 验证环境。

## Java / Maven

| 工具 | 当前状态 | 说明 |
| --- | --- | --- |
| Java | 1.8.0_241 | 老 Maven 项目通常可接受 |
| Maven | 未在 PATH 中发现 | `mvn package` 类流程暂时不可直接验证 |

影响：

- `cetc-moniwa-ui` 的 Maven 打包流程暂时不能直接跑，需要先补齐 Maven。
- 纯前端 npm 流程不受 Maven 缺失影响。

## 重点项目当前状态

| 项目 | Git 分支 | 工作区状态 | 体积 | 锁文件 / 环境文件 |
| --- | --- | --- | ---: | --- |
| `xinfang/xinfang-web-admin` | `master` | 干净 | 3.2M | 无锁文件，无 `.nvmrc` |
| `cetc-ui/bi-ui` | `sdk_0918_dev` | 干净 | 464M | 无锁文件，无 `.nvmrc` |
| `jun-dd-web` | `202004_dev` | 干净 | 1.4G | 无锁文件，无 `.nvmrc` |
| `BeijingDaxing/cetc-moniwa-ui` | `MXSSO` | 干净 | 214M | 有 `package-lock.json`，无 `.nvmrc` |

## 复现策略

### 优先级 1：不改业务仓库的验证

先用 nvm 切换 Node 版本，在各项目目录内只执行读操作和必要的安装验证。若安装会生成锁文件或改动文件，先记录结果，不直接提交业务仓库。

建议顺序：

1. `cetc-moniwa-ui`：使用 Node 8.17.0 初筛，后续补 Node 8.9.4 做精确复现。
2. `xinfang-web-admin`：使用 Node 12.22.12。
3. `bi-ui`：使用 Node 10.24.1。
4. `jun-dd-web`：使用 Node 10.24.1。

### 优先级 2：补齐缺口

- 安装或启用 Maven。
- 安装 Node 8.9.4。
- 安装 Node 14.21.3。
- 为每个项目准备本地复现日志，不污染业务仓库。

### 优先级 3：形成项目内改进建议

等确认每个项目可以安装、启动、构建后，再考虑是否给原业务项目补：

- `.nvmrc`
- README 运行说明
- 锁文件
- 环境变量样例

## 当前判断

这台 Mac 已经具备复现老前端项目的大部分基础条件，尤其是 Node 8/10/12 已经通过 nvm 安装。最大缺口是 Maven 不在 PATH，以及 `cetc-moniwa-ui` 精确声明的 Node 8.9.4 尚未安装。下一步可以开始给 4 个重点项目建立逐项复现记录表。
