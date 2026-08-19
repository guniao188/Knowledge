---
title: "Odoo13企业版主生产计划mrp_mps"
source: "http://www.thinkltd.cn/forum/2/odoo13mrp-mps-3360"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo13企业版主生产计划mrp_mps

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/odoo13mrp-mps-3360>

【模块功能】

Odoo12的主生产计划模块功能参考：\\forum/2/question/odoomrp-mps-3088

![[2-odoo13mrp-mps-3360-2c94914f.png]]

- Starting Inventory: 期初库存。系统自动计算，计算逻辑是：期初时间点的产品库存数量

- Demand Forecast: 预测的期间需求数量，手工填写。

- Actual Demand：实际需求数量。系统自动计算，计算逻辑是：该期间该产品，done和confirm状态的出库Stock Move的数量汇总

- Indirect Demand Forecast: 间接需求预测数量。 计算逻辑：根据上层BoM需求计算得出

- To Replenish: 待补货数量。系统自动计算，也可以手工修改。计算逻辑是：待补货数量 = 期末目标值 - 期初库存 - 预测的期间需求。如果算出的待补货数量，小于或大于最小、最大补货数量，则取最小、最大值。

- Actual Replenishment：实际补货数量，系统自动计算。计算逻辑是：该期间该产品，done和confirm状态的入库Stock Move的数量汇总

- Forecasted Stock：预测的期末库存，系统自动计算，计算逻辑是：期初 + 期间补货 - 期间需求 - 间接需求

- Available to Promise：期末最大可用库存，系统自动计算，计算逻辑是：期初 + 期间补货 - 实际需求

- 按钮Repenish：点击按钮，系统调用该产品、该仓库的补货规则，产生补货单据（采购单/调拨单/生产单）。

【功能截图】

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
