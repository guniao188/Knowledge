---
title: "Odoo企业版主生产计划模块mrp_mps"
source: "http://www.thinkltd.cn/forum/2/odoomrp-mps-3088"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo企业版主生产计划模块mrp_mps

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/odoomrp-mps-3088>

Period: 可以选择按月、按周、按天进行计划

Rows：勾选，计划表上显示哪些行，不显示哪些行

Starting Inventory：期初库存

Demand Forecast：期间预测的销售数量，手工填写

Indirect Demand：根据其他产品的BoM表计算而得的本产品在该期间的生产消耗数量

To Receive / To Supply / Produce：期间需要补货的数量，Launch Green Cell之前，手工填写需求数量。Launch时候，系统根据补货规则产生相应补货单（PO、调拨单、或者生产单）。Launch后，该期间预计入库的未确认的PO单数量、该期间预计入库（但尚未入库）的Stock Move数量，两者相加作为预计补货数量。

Forecasted Inventory：期末数量。

## 补充/答案 1

操作按钮详解

![[2-odoomrp-mps-3088-04186060.png]]


## 原帖外链配图

![[2-odoomrp-mps-3088-x194038c2.png]]
<small>原始地址: /web/image/1682/snipaste_20190610_200422.png?access_token=accac08a-752a-45be-9fbe-b9973049a0e3</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
