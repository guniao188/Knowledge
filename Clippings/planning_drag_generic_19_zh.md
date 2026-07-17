---
title: "planning_drag_generic_19（中文翻译）"
source: "https://apps.odoo.com/apps/modules/19.0/planning_drag_generic_19"
author:
  - "[[Armonia]]"
published:
created: 2026-07-15
translated: 2026-07-15
description: "Odoo 应用商店模块 planning_drag_generic_19 的中文翻译"
tags:
  - "clippings"
  - "翻译"
  - "Odoo/MRP"
  - "生产排程"
---
![](https://apps.odoocdn.com/web/image/loempia.module/309969/icon_image/84x84?unique=791676d)

## 制造排程拖拽（通用版）Manufacturing Planning Drag (Generic)

作者：[Armonia (armonia.odoo@gmail.com)](https://apps.odoo.com/apps/modules/browse?author=Armonia)

Odoo

## $ 145.71

您已购买此模块并需要**技术支持**？[点此进入！](https://apps.odoo.com/apps/support/309969)

Overview（概览）

## 车间生产排程所需的一切

标准 Odoo MRP 告诉你"生产什么"—— 本模块告诉你**按什么顺序、每道工序当前的状态、以及下一步该做什么**。

⠿

### 拖拽排序器（Drag & Drop Sequencer）

通过拖动行来重新排列制造订单。该顺序会驱动整个 MO 树上所有工单的自动排程。

🏭

### 工作中心列（Work Center Columns）

每个工作中心一列，实时展示 WO（工单）状态，配有颜色指示。最多可同时显示 **16 个工作中心**。

⚡

### 加急优先级（Rush Priority）

将一张订单标记为「加急（Rush）」→ 瞬间提升到第 1 位。它的所有工单会在每个工作中心获得最高排程优先级。

🔬

### 按工作中心微排程（Micro Planning by WC）

在单个工作中心内部微调队列 —— 完全按照操作员即将执行的顺序重新排列作业。

📊

### 排程报表（Planning Report）

按工作中心的仪表盘，展示**计划数量 vs 已生产数量、订单数、今日作业**，可按日期筛选。

⚙️

### 自动排程（Auto Scheduling）

切换到自动模式，可配置的定时任务（cron）**每 15 分钟**重新应用排程，并遵守工作中心工作日历。

---

Feature 1（特性一）

## 排程指挥台（The Planning Sequencer）

您的**指挥中心**。每一张打开的制造订单显示为一行 —— 拖拽即可调整优先级，无需打开任何表单即可读出状态。

- ● 待执行（Pending）
- ◐ 进行中（On going）
- ✓ 已完成（Completed）
- × 已取消（Cancelled）
- — 不适用（N/A）

![Planning Sequencer list view showing MOs with work center status columns](https://apps.odoocdn.com/apps/assets/19.0/planning_drag_generic_19/images/screenshot_sequencer.png?1a7a569)

**01. 所有工作中心的实时状态**

每一行是一张制造订单，每一列是一个工作中心。彩色圆点精确显示该作业当前状态 —— 无需钻取表单。左侧的拖拽手柄可用于**即时**调整优先级。

![Drag handles visible on planning rows](https://apps.odoocdn.com/apps/assets/19.0/planning_drag_generic_19/images/screenshot_drag.png?1a7a569)

**02. 拖拽重排序，点击应用即重排程**

拖起任意一行放到新位置，点击「**立即应用排程（Apply schedule now）**」，系统会按您新的顺序把日期与队列号推送到所有待执行的工单。

---

Feature 2（特性二）

## 加急优先级（Rush Priority）

当客户来电要求当天交付，一键即可实现。

⚡ Rush（加急）

### 一张订单，最高优先级，瞬间生效。

将任意打开的排程行标记为 Rush，它会跳到第 1 位。系统**自动清除**其他先前标记为加急的订单 —— **同一时刻仅允许一张加急单**。整个 MO 树（包括多级 BOM 生成的子 MO）中的所有工单均获得最高排程优先级。

![Rush button tooltip visible on planning row](https://apps.odoocdn.com/apps/assets/19.0/planning_drag_generic_19/images/screenshot_rush.png?1a7a569)

**03. 一键一 Rush —— 系统强制唯一**

每一行都有 Rush 按钮。将其设置到一张订单时，系统会自动从其它订单上移除，保证排程明确无二义。⚡ 图标在所有视图中清晰标识加急订单。

---

Feature 3（特性三）

## 按工作中心微排程（Micro Planning by Work Center）

全局顺序告诉每个工作中心其优先级次序；**微排程**允许车间主管在自己工位内部微调队列。

![Micro planning by work center modal dialog](https://apps.odoocdn.com/apps/assets/19.0/planning_drag_generic_19/images/screenshot_micro.png?1a7a569)

**04. 单工作中心队列控制**

打开"微排程向导"，选择一个工作中心，独立地重排其作业。应用微排程后，系统会为每个工单**精确写入开始/结束时间**，并遵守该工作中心的工作日历。

### 日历感知排程（Calendar-aware Scheduling）

工单日期基于每个工作中心的**工作时间**与**休假日历**计算，因此计划时间**符合实际**。

### 多级 MO 支持（Multi-level MO Support）

同时支持根 MO 与所有关联的子 MO（半成品）。**完整的生产树始终纳入考量**。

---

Feature 4（特性四）

## 排程报表（Planning Report）

按工作中心的汇总视图，回答每个班次最关键的问题：**我们计划了多少 vs 实际生产了多少？**

- 每工作中心 —— 计划数量（Planned qty）
- 每工作中心 —— 已生产数量（Produced qty）
- 每工作中心 —— 订单数（Order count）
- 每工作中心 —— 今日作业（Today's jobs）

![Planning Report kanban view with per-workcenter cards](https://apps.odoocdn.com/apps/assets/19.0/planning_drag_generic_19/images/screenshot_report.png?1a7a569)

**05. 工作中心卡片 —— 计划 vs 实际**

每张卡片显示该工作中心的**计划数量、已生产数量、活动订单数**，以及**待执行 vs 已完成工单**的拆分。可按今日、本周或任意日期区间筛选。

---

Configuration（配置）

## 参数设置（Settings）

所有选项均可通过 **制造 > 设置（Manufacturing > Settings）** 访问，**无需任何技术配置**。

| 参数              | 默认值           | 描述                                                              |
| --------------- | ------------- | --------------------------------------------------------------- |
| 排程模式（Scheduling Mode） | 手动（Manual）    | 手动：按需应用；自动：定时任务每 15 分钟运行一次                                     |
| 库存预留按顺序对齐        | 开             | 按排程顺序取消并重新分配组件库存，让靠前的行**优先消耗**可用库存                              |
| 库存预留范围          | 根 MO + 关联 MO  | 预留排序是应用于完整 MO 树，还是仅根订单                                          |
| 第一行标记为 Urgent  | 开             | 将第一张打开的排程行的标准 MO 优先级设为「紧急」，其余为「正常」                              |
| 使用工作中心日历        | 开             | 计算工单日期时**遵守**每个工作中心的考勤与休假日历                                    |
| Cron 始终从当前时间重排  | 关             | 自动模式下，每次定时任务运行时都**从当前时刻**重新锚定所有排程                              |

---

Get in touch（联系我们）

## 有问题或需要现场演示？

我们乐于用**您自己的数据**为您走一遍模块流程。没有推销压力 —— 只是真实地展示它如何运作。

✉️

### 联系方式

有疑问、技术支持或定制开发需求，请联系：

[armonia.odoo@gmail.com](mailto:armonia.odoo@gmail.com)

📅

### 预约演示

现场看模块运行 —— 拖拽排序、Rush 加急、微排程与报表 —— 全部在一个真实的 Odoo 19 实例中演示。

[请求演示 →](mailto:armonia.odoo@gmail.com?subject=Demo%20request%20-%20Manufacturing%20Planning%20Drag&body=Hi%2C%20I%27d%20like%20to%20schedule%20a%20demo%20of%20the%20Manufacturing%20Planning%20Drag%20module.)

---

| **可用环境** | Odoo Online  Odoo.sh  本地部署 |
| --- | --- |
| **依赖 Odoo 应用** | • 制造（mrp）   • 库存（stock）   • 讨论（mail） |
| **代码行数** | 2190 |
| **技术名称** | `planning_drag_generic_19` |
| **许可证** | OPL-1 |
| **官网/联系** | [armonia.odoo@gmail.com](mailto:armonia.odoo@gmail.com) |

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

- 原文：[[Clippings/planning_drag_generic_19.md]]
