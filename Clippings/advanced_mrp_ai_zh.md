---
title: "advanced_mrp_ai（中文翻译）"
source: "https://apps.odoo.com/apps/modules/19.0/advanced_mrp_ai"
author:
  - "[[Pokutsoft]]"
published:
created: 2026-07-15
translated: 2026-07-15
description: "Odoo 应用商店模块 advanced_mrp_ai 的中文翻译"
tags:
  - "clippings"
  - "翻译"
  - "Odoo/MRP"
  - "AI"
---
![](https://apps.odoocdn.com/web/image/loempia.module/317356/icon_image/84x84?unique=ceb80ac)

## MRP AI：排程、预测、OEE 与 IoT

作者：[Pokutsoft https://pokutsoft.com/](https://apps.odoo.com/apps/modules/browse?author=Pokutsoft)

Odoo

## $ 159.12

| **版本** | [18.0](https://apps.odoo.com/apps/modules/18.0/advanced_mrp_ai) 19.0 |
| --- | --- |

您已购买此模块并需要**技术支持**？[点此进入！](https://apps.odoo.com/apps/support/317356)

| **可用环境** | Odoo Online  Odoo.sh  本地部署 |
| --- | --- |
| **依赖 Odoo 应用** | • 库存（stock）   • 制造（mrp）   • 讨论（mail） |
| **代码行数** | 1258 |
| **技术名称** | `advanced_mrp_ai` |
| **许可证** | OPL-1 |
| **官网** | [https://pokutsoft.com/](https://pokutsoft.com/) |

| **版本** | [18.0](https://apps.odoo.com/apps/modules/18.0/advanced_mrp_ai) 19.0 |
| --- | --- |

![MRP AI for Odoo banner](https://apps.odoocdn.com/apps/assets/19.0/advanced_mrp_ai/banner.png?a4830c0)

## MRP AI for Odoo（Odoo 智能制造）

规划、预测并测量您的车间：**有限产能排程器**、真正的**统计学需求预测**引擎、**OEE / MTBF / MTTR** 分析，以及一个可运行的**车间 IoT** 遥测接入端点 —— 全部构建于标准 **mrp** 应用之上，支持多工厂管理。

有限产能排程 · 需求预测 · OEE / MTBF / MTTR · 车间 IoT · Odoo 18 & 19

## 功能概述

MRP AI 为 Odoo 增加了四项高级制造能力，且每一项都是真正可运行的软件实现。**有限产能排程器**基于每个工作中心的工作时间日历与并行产能，采用「关键比率」或「优先级」派工规则对工单进行前向排程，因此计划开始/完成日期永远不会超过实际产能。**预测引擎**为每个产品的销售或生产历史训练真实的统计学模型。**分析层**直接基于工单工时与停机日志计算 OEE 与可靠性指标。**IoT 端点**端到端地接入并处理设备遥测数据。

## 有限产能排程器（Finite-Capacity Scheduler）

前向有限产能加载会把工序装入每个工作中心真实可用的时间窗口，并遵守其并行通道数。内置两种派工规则：**关键比率（Critical Ratio）**（剩余时间 / 加工时间，逾期风险高的作业优先）和**优先级（Priority）**。每次运行会把计划开始/完成时间写回工单，并生成分工作中心的负荷与瓶颈报表。排程运行范围可限定在单工厂内，也可跨全部工厂执行。

## 统计学需求预测（Statistical Demand Forecasting）

一个无外部依赖的预测引擎，含三种真实模型：**线性趋势回归**（普通最小二乘法 OLS）、**简单指数平滑**（自动选择平滑系数），以及**加法型 Holt-Winters** 三次指数平滑（用于季节性需求）。系统按产品将您的 `sale.order.line`（销售订单行）或 `mrp.production`（制造订单）历史数据聚合为月度桶；引擎会为数据自动选取合适的模型、进行训练、给出预测区间，并输出 MAE / RMSE / MAPE 精度指标。

## OEE / MTBF / MTTR 分析

**整体设备效率（OEE）**= 可用率 × 性能 × 良品率，按每个工作中心从工单工时与 `mrp.workcenter.productivity`（工作中心生产率）日志中计算得出。**可靠性指标 MTBF**（平均无故障时间）与 **MTTR**（平均修复时间）由故障/维修间隔推导；若已安装维护（Maintenance）应用，还会同时基于 `maintenance.request`（维护请求）数据进行计算。

## 车间 IoT 集成（Shop-floor IoT Integration）

一个真实可用的 HTTP JSON 端点 —— `POST /mrp_iot/telemetry` —— 将机器遥测数据接入 `mrp.iot.reading` 日志，并端到端处理：**故障（fault）**读数会锁定工作中心并打开一条停机记录；**恢复（recovery）**读数会解锁工作中心并关闭该记录。端点通过可选的共享密钥头进行安全校验，并可通过一个轻量桥接程序由 MQTT Broker 转发消息。物理硬件不在本模块范围内；但软件层的接入与处理管线是完整的，可用模拟负载进行测试。

## 主要特性

- 有限产能前向加载排程器（关键比率 / 优先级 派工规则）
- 每工作中心的并行产能与理想节拍时间
- 每次排程运行的工作中心负荷与瓶颈报表
- Holt-Winters、线性回归、指数平滑需求预测
- 预测精度指标（MAE / RMSE / MAPE）
- 基于真实日志计算 OEE = 可用率 × 性能 × 良品率
- MTBF / MTTR 可靠性指标
- 支持故障/恢复处理的车间 IoT HTTP JSON 遥测端点
- 多工厂 / 多仓库范围管理，以及跨工厂产能视图
- 纯 Python、经完整单元测试的计算引擎（无需 scikit-learn 依赖）

## 环境要求与说明

基于标准 Odoo **mrp** 与 **stock** 应用构建；不依赖企业版。若已安装维护（Maintenance）应用，维护相关集成会自动启用。预测数学计算只使用 Python 标准库。兼容 Odoo 18 与 19。

## 截图

**有限产能排程运行结果** —— 每工作中心的可用工时 vs 已加载工时、利用率及瓶颈标记。

![MRP AI for Odoo — finite-capacity scheduling run with work-centre load and utilisation](https://apps.odoocdn.com/apps/assets/19.0/advanced_mrp_ai/screenshot_1.png?a4830c0)

**统计学需求预测** —— 所选模型、MAPE / RMSE 精度指标以及月度预测区间。

![MRP AI for Odoo — demand forecast with model, MAPE, RMSE and forecast lines](https://apps.odoocdn.com/apps/assets/19.0/advanced_mrp_ai/screenshot_2.png?a4830c0)

**OEE / MTBF / MTTR 分析** —— 每工作中心的可用率 × 性能 × 良品率及可靠性指标。

![MRP AI for Odoo — OEE, availability, performance, quality, MTBF and MTTR per work centre](https://apps.odoocdn.com/apps/assets/19.0/advanced_mrp_ai/screenshot_3.png?a4830c0)

**车间 IoT 读数** —— 已接入的遥测数据，包含 故障 / 恢复 / 心跳 / 度量 四类，全部完成处理。

![MRP AI for Odoo — shop-floor IoT telemetry readings with fault and recovery processing](https://apps.odoocdn.com/apps/assets/19.0/advanced_mrp_ai/screenshot_4.png?a4830c0)

**MRP AI 菜单** —— 在标准制造（Manufacturing）应用内，将排程、预测、OEE 分析与 IoT 集中于一处。

![MRP AI for Odoo — MRP AI menu inside the Manufacturing app](https://apps.odoocdn.com/apps/assets/19.0/advanced_mrp_ai/screenshot_5.png?a4830c0)

更新日期：2026-07-02

| **可用环境** | Odoo Online  Odoo.sh  本地部署 |
| --- | --- |
| **依赖 Odoo 应用** | • 库存（stock）   • 制造（mrp）   • 讨论（mail） |
| **代码行数** | 1258 |
| **技术名称** | `advanced_mrp_ai` |
| **许可证** | OPL-1 |
| **官网** | [https://pokutsoft.com/](https://pokutsoft.com/) |

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

- 原文：[[Clippings/advanced_mrp_ai.md]]
