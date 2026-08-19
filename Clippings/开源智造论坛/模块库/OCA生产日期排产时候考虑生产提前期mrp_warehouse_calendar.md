---
title: "OCA生产日期排产时候考虑生产提前期mrp_warehouse_calendar"
source: "http://www.thinkltd.cn/forum/2/ocamrp-warehouse-calendar-3093"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA生产日期排产时候考虑生产提前期mrp_warehouse_calendar

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocamrp-warehouse-calendar-3093>

模块链接：

With this module the manufacturing orders created from procurements consider the calendar assigned to the warehouse of the picking type of the manufacturing order to determine, based on the product's manufacturing lead time, the planned start date of the manufacturing order.

Further manual replannings of start/end date of the manufacturing order also consider the lead time using the warehouse calendar days.

## [Configuration](https://github.com/OCA/manufacture/tree/12.0/mrp_warehouse_calendar#id1)

- This module depends on [stock_warehouse_calendar](https://github.com/OCA/stock-logistics-warehouse)
- Go to *Settings* and activate the developer mode.
- Go to *Settings > Technical > Resource > Working Time* and define your resource calendar.
- Go to *Inventory > Configuration > Warehouse Management > Warehouses* and assign the Resource Calendar.

##

## [Usage](https://github.com/OCA/manufacture/tree/12.0/mrp_warehouse_calendar#id2)

When a manufacturing order is created out of a procurement evaluation (from an orderpoint, MTO,...) the calendar is considered in the computation of the planned start date of the manufacturing order.

For example, if it takes 1 day to manufacture a product and it is required for Monday, the manufacturing order will be created with planned start date on the previous Friday, if the warehouse operates under a Mo-Fri working calendar.

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
