# winboat 项目深度分析报告

## 1. 项目基本信息
- **名称**: winboat
- **GitHub**: https://github.com/TibixDev/winboat
- **定位**: 基于容器化和 KVM 的 Linux 版 Windows 应用程序管理器。

## 2. 核心架构与实现原理

### 2.1 整体架构
Winboat 采用了“宿主机控制台 + 容器化虚拟化 + 客户机代理”的三层架构。它通过 Electron 提供前端界面，后端利用 Docker/Podman 运行 QEMU/KVM 虚拟化的 Windows 镜像，并配合 FreeRDP 实现应用无缝接入。

### 2.2 技术栈协同
1. **Electron + Vue 3 (宿主机控制与前端界面)**
   - **职责**：作为系统的“大脑”，负责 UI 交互、容器编排以及 RDP 连接调度。
   - **实现**：主进程通过 `child_process` 调用系统层面的 `docker-compose` 指令。
2. **Guest Server (客户机内的 Go 代理)**
   - **职责**：运行在 Windows 内部，监听 7148 端口，暴露监控指标（CPU、内存、磁盘）和系统状态。
   - **协同**：Electron 通过轮询此 API 获取虚拟机的实时性能数据。
3. **Bun (构建与工程化)**
   - **职责**：提供极速的依赖管理和脚本执行环境。
   - **应用**：用于加速 Electron 应用的打包及 Guest Server 的交叉编译。
4. **QMP & USB Manager (硬件直通)**
   - **原理**：利用 QEMU Machine Protocol (QMP) 进行底层热插拔操作。
   - **效果**：支持 USB 设备动态映射，插入 U 盘后可自动被 Windows 虚拟机识别。

## 3. 核心优势与解决的问题
- **解决虚拟机配置难**：屏蔽复杂的 KVM 和网络配置，实现一键式 Windows 环境搭建。
- **无缝化体验**：利用 FreeRDP 的 Seamless Mode，让 Windows 软件像原生 Linux 应用一样在独立窗口运行。
- **高性能虚拟化**：基于容器化的 QEMU/KVM，相比传统虚拟机性能损耗更低。

## 4. 结论
Winboat 巧妙地组合了现代前端工具链 (Electron/Bun) 与经典的虚拟化技术，为 Linux 生态下的 Windows 应用兼容性提供了一个高度自动化的、极低门槛的解决方案。
