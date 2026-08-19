---
title: "OCA补货规则Rule上添加自动创建补货组的字段procurement_auto_create_group"
source: "http://www.thinkltd.cn/forum/2/ocaruleprocurement-auto-create-group-2851"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA补货规则Rule上添加自动创建补货组的字段procurement_auto_create_group

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaruleprocurement-auto-create-group-2851>

模块链接：

This module allows the system to propose automatically new procurement groups when procuring.

This capability is important when you want to make sure that all the stock moves resulting from this procurement will never be mixed with moves from other groups in stock transfers.

The stock transfers resulting from the execution of these procurements will only contain stock moves created from that procurement.

## [Configuration](https://github.com/OCA/stock-logistics-warehouse/tree/11.0/procurement_auto_create_group#id1)

1.  Go to *Inventory / Configuration / Settings* and check the option 'Multi-Step Routes' and press the 'Save' button.
2.  Activate the developer mode.
3.  Go to *Inventory / Configuration / Warehouse Management / Routes* and select the route you want to change. Select the pull rule you wish to change and Select 'Propagation of Procurement Group': 'Propagage'. The checkbox 'Auto-create Procurement Group' will then appear and you can set it if you want to procurement group to be automatically created.

##

## [Usage](https://github.com/OCA/stock-logistics-warehouse/tree/11.0/procurement_auto_create_group#id2)

1.  Create a new procurement and make sure that it determines a pull rule with the option 'Auto-create Procurement Group' set.
2.  When the procurement rule is executed, a procurement group with format 'PG/000001' will be created.

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
