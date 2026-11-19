# Stellaria Link

**为日常连接而设计的 VPN 客户端。**

[下载 Public Beta](https://github.com/Stellaria-Studio/Stellaria-Link-Releases/releases/download/v0.10.15/Stellaria-Link-0.10.15-0J15b-macOS-arm64.dmg) · [发行说明](https://github.com/Stellaria-Studio/Stellaria-Link-Releases/releases/tag/v0.10.15) · [快速开始](#快速开始) · [English](README.en.md)

**0.10.15 · 0J15b**　｜　macOS · Apple Silicon　｜　Public Beta 更新

Stellaria Link 将加密连接、节点选择、规则分流与连接维护整合进一个紧凑的桌面面板。LinkCore 负责数据传输与连接生命周期，LinkGuard 观察信道状态并按需执行恢复策略，让日常连接更容易管理。

## Windows x64 预览版

[下载 Windows x64 ZIP](https://github.com/Stellaria-Studio/Stellaria-Link-Releases/releases/download/v0.10.11-windows.1/Stellaria-Link-0.10.11-0J11b-Windows-x64.zip) · [Windows 发行说明与 SHA-256](https://github.com/Stellaria-Studio/Stellaria-Link-Releases/releases/tag/v0.10.11-windows.1)

支持本地代理、Windows 系统代理及整机 TUN。完整解压后运行 `Start-Link.cmd`；缺少运行库时可运行随包的微软 `VC_redist.x64.exe`。可选运行 `Install-ForUser.ps1` 安装到当前用户并创建快捷方式。

首次使用整机 TUN，请在高级工作台安装网络助手并允许 UAC；日常界面可用普通用户启动。安排独立切换窗口并退出其他 VPN 后连接，断开或使用恢复操作会清理 Link 自己的网络配置。服务故障时防护继续保留，需显式恢复。不要同时开启两个整机 VPN。

整机 IPv4/IPv6 TCP、UDP、DNS、暂停恢复、服务崩溃保护及清理已在一次性 Windows 虚拟机验证。当前为未签名预览版，Windows 按进程分流、真实硬件休眠跨网及长期稳定性尚未验收；Windows 更新通过发行页手动下载。下方原有 macOS 说明保持适用于 macOS。

## 0J15b 更新

- 节点握手后没有应用响应时，Link 会核验当前出口，必要时切到已授权候选。全部候选不可用时继续退避重试。
- 系统网络恢复期间可以手动切换节点。断开立即显示进度，完成后确认系统网络已恢复。
- 去掉重复预检，减少网络通知和连接验证的刷新开销。整机模式的恢复修复需同步更新原生网络助手。

## 0J14b 更新

- 减少背景采集和状态刷新开销，保留实时毛玻璃、页面切换与弹窗动效。
- LinkCore、Qt 界面、网络助手和控制进程分别显示内存占用，修正 macOS TUN 的 CPU 时间计量。
- 提高 DNS 突发准入容量，并缩短完成查询后对 UDP 槽位的占用。

## 0J13b 更新

- 节点页的「管理」菜单从按钮下方展开，菜单文字清晰可读。
- Link 连接期间可下载并校验更新包。下载完成后，正常断开 Link，再从本机「重启并安装」。
- 从旧版升级时可在 VPN 在线期间下载本次 DMG，然后退出 Link 安装。

## 0J12b 更新

- 在节点页勾选允许自动切换的范围。选择「连接时评分 · 故障才切换」后，启动时从候选节点评分选路，健康出口持续使用。
- 单节点或全部候选暂未响应时，Link 持续低开销重试。连接页提示切换节点或更新订阅。
- macOS 安装包提供新版 App 与 LinkCore。可在整机连接空闲后更新 App 和网络助手。

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

1. 在 [Releases](https://github.com/Stellaria-Studio/Stellaria-Link-Releases/releases/tag/v0.10.15) 下载 macOS Apple Silicon 的 DMG，将 **Stellaria Link** 拖入 **Applications**。
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

首次打开若 macOS 提示无法验证开发者，可在 **系统设置 → 隐私与安全性** 中选择打开本次下载的 Link。TUN 模式的首次组件安装需要管理员授权。在 **高级工作台 → 系统组件** 完成系统 Terminal 授权后，请等待 Link 显示“网络助手已安装并就绪”再连接。本轮 TUN 连接修复需要新版网络助手；已安装的旧助手也需升级。

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
