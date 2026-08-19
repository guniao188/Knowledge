---
title: "Odoo16生产计划/生产管理详解(MPS功能)"
source: "http://www.thinkltd.cn/forum/1/odoo16-mps-3652"
forum: "求助台"
author: "肖相扶"
published: 2023-03-24
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo16生产计划/生产管理详解(MPS功能)

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2023-03-24
> <http://www.thinkltd.cn/forum/1/odoo16-mps-3652>

生产计划/管理工作：生管的工作是，根据销售部门的销售订单/销售预测，基于BoM计算关键物料的需求，下达关键物料的补货计划（采购或预生产）。非关键物料，制造订单（MO）确认时候，系统自动展开物料需求，发起补货计划（采购、部件生产）。

![[1-odoo16-mps-3652-96108fb6.png]]

- Actual Demand Y-2：前年(今年减2年)同期该产品的需求数量（系统汇总前年同期该产品的出库Stock Move的数量）
- Actual Demand Y-1：去年(今年减1年)同期该产品的需求数量（系统汇总去年同期该产品的出库Stock Move的数量）
- Actual / Forecasted Demand：实际需求(Actula Demand)：该产品该期的实际需求数量（系统汇总该期该产品的出库Stock Move的数量，包括完成状态的Stock Move，也包括待出货的Stock Move）。 Forecasted Demand：预测的需求数量，用户手填的该期预测数量。
- Actual / Suggested Replenishment： Actual Replenishment实际补货数量，该产品该期的实际补货数量（ 系统汇总该期该产品的入库Stock Move的数量，包括完成状态的Stock Move，也包括待入库的Stock Move）。  Suggested Replenishment建议补货数量，系统用该期需求数量(实际需求数量 + 预测需求数量)，减去期初库存，减去实际补货数量，得到该期建议补货数量。用户还可以手动修改建议补货数量。
- ATP / Forecasted Stock：ATP(Available to Promise)可承诺的该期出货数量（等同于该期期末预测库存数量）。 Forecasted Stock该期期初的预测库存数量。
- Indirect Demand Forecast：间接需求预测，系统根据用到该产品的成品/半成品的需求数量，基于BoM自动计算的该产品的需求数量。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
