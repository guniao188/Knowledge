---
title: "OCA新增周期性盘点计划表单stock_cycle_count、stock_inventory_discrepancy、stock_inventory_exclude_sublocation"
source: "http://www.thinkltd.cn/forum/2/ocastock-cycle-countstock-inventory-discrepancystock-inventory-exclude-sublocation-2886"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA新增周期性盘点计划表单stock_cycle_count、stock_inventory_discrepancy、stock_inventory_exclude_sublocation

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocastock-cycle-countstock-inventory-discrepancystock-inventory-exclude-sublocation-2886>

周期性盘点计划表单：

库存盘点规则：

1.  定期盘点

2.  库存周转率超过一定阀值盘点

3.  库存准确性低于一点阀值盘点

4.  出现零库存或负库存盘点

盘点单（Inventory Adjust）上增加库存偏差数字段：

库位上增加“是否排除在周期性盘点计划之外”的标志字段：

This module provides the capability to execute a cycle count strategy in a warehouse through different rules defined by the user. Cycle count is an alternative to full wall-to-wall physical inventories in which little portions (stock locations) of the stock are selected to count on a regular basis.

The system propose locations in which to perform a inventory adjustment every day based on a set of rules defined for the warehouse. In addition the system can propose Zero-Confirmations which are simple and opportunistic counts to check whether a locations has actually became empty or not.

With this strategy it is possible to:

- Remove the need to perform full physical inventories and to stop the production in the warehouse.
- Measure the accuracy of the inventory records and improve it.
- Correct inventory errors earlier and prevent them to become bigger.
-

## [Configuration](https://github.com/OCA/stock-logistics-warehouse/tree/11.0/stock_cycle_count#id4)

You can configure the rules to compute the cycle count, acting as follow:

1.  Go to *Inventory > Configuration > Cycle Count Rules*.
2.  Create as much cycle count rules as you want.
3.  Assign the rules to the Warehouse or zones where you want to apply the rules in.
4.  Go to *Inventory > Configuration > Warehouse Management > Warehouses* and set a *Cycle Count Planning Horizon* for each warehouse.

##

## [Usage](https://github.com/OCA/stock-logistics-warehouse/tree/11.0/stock_cycle_count#id5)

Once you have some rules configured for your warehouses, you can proceed as is described below.

1.  Go to *Inventory > Configuration > Warehouse Management > Warehouses*.
2.  Select all the warehouses you want to compute the rules in.
3.  Click on "Action" and then in "Compute Cycle Count Rules". (**note**: A cron job will do this for every warehouse daily.)
4.  Go to *Operations > Cycle Counts*.
5.  Select a planned Cycle Count and confirm it, this will create a draft Inventory Adjustment.
6.  In the right top corner of the form view you can access to the generated Inventory Adjustment.
7.  Proceed with the Inventory Adjustment as usual.


## 原帖外链配图

![[2-ocastock-cycle-countstock-inventory--x194038c2.png]]
<small>原始地址: /web/image/1389/snipaste_20190217_224044.png?access_token=64b1a720-9a80-4371-a1d7-2b85b525c1df</small>

![[2-ocastock-cycle-countstock-inventory--x194038c2.png]]
<small>原始地址: /web/image/1391/snipaste_20190217_224205.png?access_token=c21ac51c-74c6-4a5d-9d97-e7b781b77c71</small>

![[2-ocastock-cycle-countstock-inventory--x194038c2.png]]
<small>原始地址: /web/image/1393/snipaste_20190217_224355.png?access_token=456cfa3f-d0a5-490e-be45-92ad42902540</small>

![[2-ocastock-cycle-countstock-inventory--x194038c2.png]]
<small>原始地址: /web/image/1395/snipaste_20190217_224438.png?access_token=e08bff4e-0bc4-44e6-9c7f-9f24852ffa82</small>

![[2-ocastock-cycle-countstock-inventory--x194038c2.png]]
<small>原始地址: /web/image/1399/snipaste_20190217_225355.png?access_token=ce2335ac-a00a-4375-97ba-a5ffe7fd13ec</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
