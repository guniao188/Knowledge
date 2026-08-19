---
title: "OCA StockPicking增加补货规则触发补货stock_picking_procure_method"
source: "http://www.thinkltd.cn/forum/2/oca-stockpickingstock-picking-procure-method-2865"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA StockPicking增加补货规则触发补货stock_picking_procure_method

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/oca-stockpickingstock-picking-procure-method-2865>

模块链接：

StockPicking上增加补货规则字段，填写该字段自动覆写到StockMove，从而触发补货。一个应用场景是，手工创建MO，产生领料单，领料单触发原料采购。

This module adds the possibility to set the supply method to *Apply Procurement Rules* in the pickings, which is normally set to *Take From Stock* by default.

This way, you can configure MTO flows triggered from the picking itself.

## [Installation](https://github.com/OCA/stock-logistics-warehouse/tree/11.0/stock_picking_procure_method#id1)

This module is useless without either Odoo's mrp or purchase modules (or both). Depending on your needs you should install them in advance.

##

## [Configuration](https://github.com/OCA/stock-logistics-warehouse/tree/11.0/stock_picking_procure_method#id2)

This is an example scenario with two warehouses. WH2 will be allways supplied through WH1.

Common steps to mrp and purchase procurements:

1.  Go to *Inventory > Configuration > Settings > Warehouse* and set *Multi-Step Routes* on.
2.  Go to *Inventory > Configuration > Warehouse Management > Warehouses*
3.  Create **WH1** with either *Manufacture in this Warehouse* or *Purchase to resupply this warehouse* or both set.
4.  Create **WH2** setting off *Manufacture in this Warehouse* and *Purchase to resupply this warehouse*. Set **WH1** as the *Resupply Warehouse*.
5.  Go to *Inventory > Configuration > Warehouse Management > Routes* and click on the *Make To Order* one.
6.  Add a new *Procurement Rule* with these settings and save:
    - Name: *WH1 -> WH2-MTO*
    - Action: *Move From Another Location*
    - Procurement Location: *WH2/Stock*
    - Served Warehouse: *WH2*
    - Source Location: *WH1/Stock*
    - Move Supply Method: *Create Procurement*
    - Operation Type: *WH1: Internal Transfers*
    - Propagation of Procurement Group: *Propagate*
    - Propagate cancel and split: True
    - Warehouse to Propagate: *WH1*

Now if you want to trigger a manufacture:

> - Create a stockable product product with a BoM list.
> - In the product's *Inventory > Routes section* set *Make To Order* and *Manufacture* on.

Or if you want to trigger a purchase:

> - Create a stockable product product with a supplier.
> - In the product's *Inventory > Routes section* set *Make To Order* and *Purchase* on.

##

## [Usage](https://github.com/OCA/stock-logistics-warehouse/tree/11.0/stock_picking_procure_method#id3)

After configuring you procurement rules and your product routes:

1.  Go to *Inventory > Dashboard* and click on the *more options* icon (☰).
2.  Choose *New > Planned Transfer*.
3.  Set an origin and destination that is considered in the routes procurement rules.
4.  Set *Supply Method* to *Apply Procurement Rules*.
5.  Set the products and quantities you want to supply.
6.  Save and click on *Mark as To Do*.
7.  Depending on the product's supply type a new MO or a new PO should be created.


## 原帖外链配图

![[2-oca-stockpickingstock-picking-procur-x194038c2.png]]
<small>原始地址: /web/image/1363/snipaste_20190215_134650.png?access_token=f48cd26b-2c3a-46d4-bbcf-c79af0e5a49d</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
