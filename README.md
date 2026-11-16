# Stellaria Link

**为日常连接而设计的 VPN 客户端。**

[下载 Public Beta](https://github.com/Stellaria-Studio/Stellaria-Link-Releases/releases/download/v0.10.8/Stellaria-Link-0.10.8-0J08b-macOS-arm64.dmg) · [发行说明](https://github.com/Stellaria-Studio/Stellaria-Link-Releases/releases/tag/v0.10.8) · [快速开始](#快速开始) · [English](README.en.md)

**0.10.8 · 0J08b**　｜　macOS · Apple Silicon　｜　Public Beta 更新

Stellaria Link 将加密连接、节点选择、规则分流与连接维护整合进一个紧凑的桌面面板。LinkCore 负责数据传输与连接生命周期，LinkGuard 观察信道状态并按需执行恢复策略，让日常连接更容易管理。

## 0J08b 更新

- 修复节点地址解析的冷启动时间预算，在既有超时内并行尝试已配置的解析服务，避免过早失败。
- 复用已验证的 DNS over HTTPS 连接，减少连续测速和连接准备中的重复握手；网络路径更新时清理复用连接。
- 区分通道就绪、节点验证与实际应用响应，并保留测速中的具体失败原因。
- **TUN 模式需要升级网络助手**，才能启用本轮节点解析修复。完成授权并等待助手就绪后再连接。

![Stellaria Link 连接首页](docs/images/connection.png)

## 为什么选择 Link

| 功能 | 使用体验 |
| --- | --- |
| 快速接入 | 粘贴机场订阅、导入节点链接或 YAML 配置，从首页开始连接。 |
| 自主 LinkCore | 以自主的连接调度、资源管理与恢复逻辑，统一承载 Hysteria2、Trojan、VLESS 等协议。 |
| 灵活分流 | 管理节点与策略组，通过图形界面编辑规则，在线切换节点与更新规则。 |
| 看得见的 LinkGuard | 在同一页查看信道状态、防护措施和最近动作，选择高效、自适应或 Privacy 模式。 |
| 低开销设计 | 通过会话复用、缓冲管理和有界采样减少额外工作。 |
| 持续更新 | 定时更新机场订阅；软件和内核从 GitHub 检查签名更新，由你选择立即更新或稍后。 |

## 快速开始

1. 在 [Releases](https://github.com/Stellaria-Studio/Stellaria-Link-Releases/releases/tag/v0.10.8) 下载 macOS Apple Silicon 的 DMG，将 **Stellaria Link** 拖入 **Applications**。
2. 打开 Link，点击 **添加连接**，粘贴机场 HTTPS 订阅、节点链接，或导入已有 YAML 配置。
3. 在 **节点** 页测试并选择节点或策略组，回到首页选择 **代理接入** 与 **规则 / 全局**，点击 **连接**。
4. 在 **订阅** 页管理配置；在 **设置 → 桌面 → 机场自动更新** 开启定时更新。
5. 在 **设置 → 连接 → 检查更新** 获取软件或内核新版。
6. 点击侧栏下方的账户入口，在独立的 Stellaria Pass 窗口中登录、管理账户并展示 Link 支持者身份。

| 代理接入 | 适合的场景 |
| --- | --- |
| 仅本地代理 | 只开启 HTTP / SOCKS 端口，需在应用中填写代理地址；不修改系统代理或路由。 |
| 系统代理 | 让浏览器等遵循系统代理的应用使用 Link。 |
| TUN 模式 | 通过虚拟网卡接收应用流量，再按规则 / 全局模式处理；首次使用按引导安装系统网络组件。 |

首次打开若 macOS 提示无法验证开发者，可在 **系统设置 → 隐私与安全性** 中选择打开本次下载的 Link。TUN 模式的首次组件安装需要管理员授权。在 **设置 → 网络助手** 完成系统 Terminal 授权后，请等待 Link 显示“网络助手已安装并就绪”再连接。本轮 TUN 节点解析修复需要新版网络助手；已安装的旧助手也需升级。

## 节点与连接质量

搜索、排序、手动测试和策略组选择集中在节点页，首页同步显示当前节点、响应、连接质量与内核内存。

![Stellaria Link 节点页](docs/images/nodes.png)

## LinkGuard

高效、自适应与 Privacy 三种模式，共享统一的连接安全要求。连接状态与恢复、隔离、切换等动作都有各自的记录入口。

![Stellaria LinkGuard](docs/images/guard.png)

## 紧凑而清晰的桌面体验

枪灰与琥珀色视觉、圆角控件、玻璃层次和集中的高级工作台，让常用操作与进阶设置各有位置。

![Stellaria Link 高级工作台](docs/images/workbench.png)

## 许可与开源计划

**当前 Public Beta 为闭源公测版本。** 正式发布后，Stellaria Link 将开放源码，采用 **AGPL v3 + Stellaria Commercial License（SCL）** 双重授权。SCL 提供独立的商业授权路径，用于按约定进行专有集成等商业合作。第三方组件继续遵循各自的许可证。

## 反馈

欢迎在 [Issues](https://github.com/Stellaria-Studio/Stellaria-Link-Releases/issues) 提交使用反馈与功能建议，附上版本、平台和复现步骤。
