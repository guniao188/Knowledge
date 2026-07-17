---
title: "machine_scheduling_advanced（中文翻译）"
source: "https://apps.odoo.com/apps/modules/19.0/machine_scheduling_advanced"
author:
  - "[[Micra digital]]"
published:
created: 2026-07-15
translated: 2026-07-15
description: "Odoo 应用商店模块 machine_scheduling_advanced 的中文翻译"
tags:
  - "clippings"
  - "翻译"
  - "Odoo/MRP"
  - "生产排程"
  - "设备管理"
---
![](https://apps.odoocdn.com/web/image/loempia.module/296577/icon_image/84x84?unique=f1b27a0)

## 高级制造排程（Advanced Manufacturing Scheduling）

作者：[Micra digital https://www.micra.digital/](https://apps.odoo.com/apps/modules/browse?author=Micra%20digital)

Odoo

## $ 48.57

| **版本** | [17.0](https://apps.odoo.com/apps/modules/17.0/machine_scheduling_advanced) [18.0](https://apps.odoo.com/apps/modules/18.0/machine_scheduling_advanced) 19.0 |
| --- | --- |

您已购买此模块并需要**技术支持**？[点此进入！](https://apps.odoo.com/apps/support/296577)

| **可用环境** | Odoo Online  Odoo.sh  本地部署 |
| --- | --- |
| **依赖 Odoo 应用** | • 库存（stock）   • 制造（mrp）   • 讨论（mail）   • 员工（hr） |
| **代码行数** | 1026 |
| **技术名称** | `machine_scheduling_advanced` |
| **许可证** | OPL-1 |
| **官网** | [https://www.micra.digital/](https://www.micra.digital/) |

| **版本** | [17.0](https://apps.odoo.com/apps/modules/17.0/machine_scheduling_advanced) [18.0](https://apps.odoo.com/apps/modules/18.0/machine_scheduling_advanced) 19.0 |
| --- | --- |

## 高级设备排程（Advanced Machine Scheduling）

先进的**甘特图排程、设备优化与故障处理**，用于提升生产可视化、降低停机影响、最大化制造效率。

甘特图排程 · 优化 · 故障处理 · 等待与维修时间跟踪

## 快速预览

### 智能故障决策系统（Smart Breakdown Decision System）

![](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/8.png?93dd2a1)

**智能"维修 vs 迁移"分析**  
当一台设备发生故障时，系统**并非仅仅停止生产**，而是自动比较三种方案：**等待维修**、**转移到其他设备**、**将已生产数量推进到下一道工序**。计划员**几秒内**即可看到总延误、预计生产时间、以及节省的时间，从而做出最佳决策。

![](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/12.png?93dd2a1)

**故障自动跟踪与历史**  
每一次设备故障均**自动记录**故障原因、时间、迁移详情。管理层可直接在**工作中心界面**清晰跟踪设备可靠性、维护问题与操作员动作。有助于改进维护计划，防止重复的生产损失。

![](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/15.png?93dd2a1)

**自动生产重排**  
发生迁移或冲突后，排程看板**自动更新**。工序自动转移到可用设备，工作流**继续无需人工重新计划**。确保生产不中断、闲置时间减少、工厂资源利用率最大化。

## 为什么选择本模块？

本模块通过**智能设备排程、实时甘特图视图、优化工具与故障管理**增强制造计划，最小化生产延误。

### 高级甘特图视图（设备排程）

- **设备级别**的排程，时间轴清晰
- 一眼看出重叠与延误
- 按设备计算完工时间

### 手动与自动优化

- 优化设备分配，减少闲置时间
- 基于实时视图做更聪明的排程决策
- 提升工作中心利用率

### 故障管理与迁移

- 处理设备故障时**不丢失可视性**
- 将工序**迁移**到备用设备
- 故障期间**部分数量转移**

### 等待与维修时间跟踪

- 跟踪等待时间与维修时间用于分析
- 改善维护计划
- 用数据降低停机影响

#### 工作中心增强

每个工作中心可显示**上次故障时间、故障原因、当前机器状态**，支持更快的决策。

#### 核心收益

- 提升生产可视化
- 降低停机影响
- 更聪明的资源分配
- 基于实时数据做更好决策
- 更高的制造效率

---

### 配置与操作指南

本节讲解完整工作流：从**选择备用工作中心**，到**故障处理、迁移和使用「设备排程」甘特图视图进行自动排程**。

![Step 1](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/1.png?93dd2a1)

**步骤 1 —— 配置备用工作中心**  
打开 **制造 → 配置 → 工作中心**，选中一个工作中心，定义其**备用工作中心（Alternative Workcenter）**。这样当前设备不可用（故障/繁忙）时，系统可**无阻塞地**平滑迁移工序。

![Step 2](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/2.png?93dd2a1)

**步骤 2 —— 确认制造订单**  
创建并**确认**一张制造订单，以便生成工序。确认后前往 **计划 → 设备排程（Planning → Machine Schedule）** 查看和管理工序的实时时间轴。

![Step 3](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/3.png?93dd2a1)

**步骤 3 —— 查看定制甘特图流程**  
系统为制造订单展示**定制的甘特图视图**，可视化整个工序序列，箭头显示跨设备的**正确工艺流向**，让计划员**立刻理解依赖关系与下一道工序**。

![Step 4](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/4.png?93dd2a1)

**步骤 4 —— 打开设备分配**  
在甘特图中选中设备块（工作中心工序）并点击**编辑**。此处可管理排程决策、上报问题或按需迁移作业。

![Step 5](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/5.png?93dd2a1)

**步骤 5 —— 上报设备问题**  
若所选工作中心（设备）发生故障或需维护，点击**上报问题（Report Problem）**。这会启动**故障流程**，防止在故障设备上错误地开始生产。

![Step 6](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/6.png?93dd2a1)

**步骤 6 —— 在弹窗中填写故障详情**  
弹出向导包含**故障原因、备注、时间**等字段。此举确保故障被规范记录，并对计划员/操作员可见，便于快速处理。

![Step 7](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/7.png?93dd2a1)

**步骤 7 —— 迁移剩余数量**  
向下滚动并启用**"迁移剩余产品（Relocate remaining product）"**。手动选择另一个工作中心（设备），或点击**"寻找最优（Find Optimum）"** 让系统根据可用性与效率**推荐最佳设备**。

![Step 8](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/8.png?93dd2a1)

**步骤 8 —— 理解时间分析**  
系统显示详细对比，包括**等待时间**和**工作中心效率**。若同时把已生产的数量推进到下一道工序，向导还会显示**整条工序链节省的时间**。

![Step 9](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/9.png?93dd2a1)

**步骤 9 —— 确认处理方案**  
点击**"确认处理（Confirm Resolution）"**。系统将剩余工作迁移到所选工作中心，并**更新工序计划**，同时不破坏制造顺序。

![Step 10](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/10.png?93dd2a1)

**步骤 10 —— 在甘特图中验证变更**  
返回甘特图，MO 工序已被迁移（例：转到**设备 D**）；若已启用，已生产的产品会被**推进到下一道工序**（例：**设备 B**）。箭头同步更新，保持正确的工序流向。

![Step 11](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/11.png?93dd2a1)

**步骤 11 —— 在制造订单内验证**  
打开制造订单并检查工序，可以看到**下一道工序已启动**（若已推进）以及**迁移后的工作中心**，生产团队据此按更新后的计划执行。

![Step 12](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/12.png?93dd2a1)

**步骤 12 —— 工作中心上的故障告警**  
打开被上报的工作中心：**告警**确认已发生故障，**故障信息（Breakdown Info）** 存储原因与备注，形成清晰的历史，供维护与计划审计使用。

![Step 13](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/13.png?93dd2a1)

**步骤 13 —— 阻止在故障设备上开工**  
若用户尝试在故障设备上开始制造流程，系统**阻断该操作**并弹出提示。防止错误的生产执行与不准确的报工。

![Step 14](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/14.png?93dd2a1)

**步骤 14 —— 处理分配冲突**  
当一张 MO 已经在某台设备上排程，用户又把另一张 MO 分配到相同时段时，弹窗询问是使用**自动排程（Auto Schedule）** 还是**手动排程（Manually Schedule）** 到其他时间。

![Step 15](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/15.png?93dd2a1)

**步骤 15 —— 自动排程**  
选择**"自动排程"** 后，模块会**自动寻找该设备的下一个可用时段**并据此重排工序，确保无重叠、维持排程精度。

![Step 16](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/images/16.png?93dd2a1)

**步骤 16 —— 设备繁忙时的迁移提示**  
若用户在设备已被占用时尝试开始一道工序，系统弹出**迁移提示**，建议把工序转移到其他工作中心，确保生产连续性并降低延误。

---

## 环境要求与兼容性

#### 兼容对象

- Odoo（制造 / MRP）
- 工作中心（Work Centers）
- 制造订单（工序）

#### 核心能力

- 设备级别排程（甘特图）
- 优化工具（手动 / 自动）
- 故障处理 + 迁移

#### 跟踪与洞察

- 等待与维修时间跟踪
- 工作中心故障信息
- 更优的决策支持

**提示**：可利用截图 Tab 清晰演示您的甘特图视图、优化按钮、故障向导以及迁移流程。

---

## 技术支持与联系

### 邮件支持

需要安装或配置帮助？联系我们的支持团队：

[support@micradigital.com](mailto:support@yourcompany.com?subject=Advanced%20Machine%20Scheduling%20Support)

![Micra Digital Logo](https://apps.odoocdn.com/apps/assets/19.0/machine_scheduling_advanced/screenshots/logoo.png?93dd2a1)

### 官方网站

浏览团队更多的 Odoo 模块、解决方案与服务：

<https://www.micra.digital>

若因 Odoo 应用商店安全策略无法点击链接，请复制 URL 到浏览器。

---

| **可用环境** | Odoo Online  Odoo.sh  本地部署 |
| --- | --- |
| **依赖 Odoo 应用** | • 库存（stock）   • 制造（mrp）   • 讨论（mail）   • 员工（hr） |
| **代码行数** | 1026 |
| **技术名称** | `machine_scheduling_advanced` |
| **许可证** | OPL-1 |
| **官网** | [https://www.micra.digital/](https://www.micra.digital/) |

---

## 许可证原文（Odoo Proprietary License v1.0）

```
Odoo Proprietary License v1.0

This software and associated files (the "Software") may only be used (executed,
modified, executed after modifications) if you have purchased a valid license
from the authors, typically via Odoo Apps, or if you have received a written
agreement from the authors of the Software (see the COPYRIGHT file).

You may develop Odoo modules that use the Software as a library (typically
by depending on it, importing it and using its resources), but without copying
any source code or material from the Software. You may distribute those
modules under the license of your choice, provided that this license is
compatible with the terms of the Odoo Proprietary License (For example:
LGPL, MIT, or proprietary licenses similar to this one).

It is forbidden to publish, distribute, sublicense, or sell copies of the Software
or modified copies of the Software.

The above copyright notice and this permission notice must be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
```

**许可证要点中文摘要**：
- 本软件为 **Odoo 专有许可证 v1.0（OPL-1）**，闭源商用授权。
- 仅在**已从作者处购得合法授权**（通常通过 Odoo Apps 购买）或已获得作者书面协议的前提下，方可使用（运行、修改、修改后运行）。
- 可以开发**依赖并调用**本软件的 Odoo 模块（作为库使用），但**不得复制**本软件的任何源代码或素材；派生模块可采用自选许可证（须与 OPL 兼容，例如 LGPL、MIT 或类似的专有许可证）。
- **禁止**发布、分发、再授权或销售本软件（或其修改版）的副本。
- 软件按"现状"提供，作者不对任何索赔、损害或其他责任承担义务。

---

## 关联笔记

- 原文：[[Clippings/machine_scheduling_advanced.md]]
- 相关：[[Clippings/advanced_mrp_ai_zh.md]]
- 相关：[[Clippings/planning_drag_generic_19_zh.md]]
