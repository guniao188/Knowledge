---
title: "OCA自动填充完成数量stock_pack_operation_auto_fill"
source: "http://www.thinkltd.cn/forum/2/ocastock-pack-operation-auto-fill-2549"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA自动填充完成数量stock_pack_operation_auto_fill

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocastock-pack-operation-auto-fill-2549>

模块链接：

1.   此模块在Picking上增加按钮“AutoFill”，点击按钮，系统自动填充完成数量，填充规则如下：没启用批次管理的商品，直接拷贝保留数量到完成数量；有批次管理的商品，入库情况不做处理，出库情况，将各批次的保留数量拷贝到完成数量。

2.  Picking Type上增加配置字段"Avoid auto-assignment of lots"，"Auto fill operations"。如果"Avoid auto-assignment of lots"不勾选，则AutoFill时候，批次管理商品也拷贝保留数量到完成数量。勾选则不拷贝。"Auto fill operations"目前未用（不起作用）。

3.  一个应用场景是，一个Picking有50个明细行，其中只有一行缺货，按Odoo现有功能，必须填写49行的完成数量。有了AutoFill则可以自动填写50行，再手工修改缺货的一行。

This module alow auto fill quantities in picking operations and autoassignment lots quantities.

In Odoo, if you schedule to transfer 50 product quantities and only receive 49 quantities, you have to change the quantity directly on the picking. As the quantity by default is 0 for each line, you have to write the received quantity on 49 lines.

In this module we have added a button that helps users to fill automatically the scheduled quantities. Then, the user can just change back the quantities for the product that hasn't been received yet.

##

## Products with lots

When working with lots, it's very uncomfortable to introduce the quantity, lot by lot, when transferring pickings from your warehouse (outgoing or internal).

This module automatically assigns the reserved quantity as the done one, so that you only have to change it in case of divergence, but having the possibility of transferring directly.

Also this module adds a button in backorder confirmation wizard to auto complete to do quantities for products without lots.

**Table of contents**

##

## Configuration

To configure this module, you need to:

1.  Make sure you have selected the proper removal strategy on your product categories.
2.  Configure the product on the page "Inventory", field "Tracking" with one of these values: "By Unique Serial Number" or "By Lots" if you want autoassign lots.
3.  Check in Operation type if you want auto assign quantities, by default if you want assign quantities done to reserved quantities you must push the button "Auto Fill" when the picking is in ready state and has move lines
4.  Check in Operation type if you do not want auto assign lots quantities with "Avoid auto-assignment of lots".

##

## Usage

Set options in operation types, you can set 'Auto fill operation' what make autoassignment button invisible and fill the quantities in operations for lines and 'Avoid Autoassignment Lots' what allow fill manually the lots quantities.

##

## Products without tracking lots

After confirming the picking, click on Auto fill operations button. The Operations matching the following conditions will be filled automatically:

- The operation has not be processed (i.e qty_done == 0).
- The operation has no package set (i.e package_id is empty).

##

## Product with lots

1.  Create an outgoing or an internal picking.
2.  Include one product with lots and with enough stock.
3.  Click on "Mark as Todo" button, and then on "Reserve".
4.  Clicking on the icon with the three items bullet list on the "Operations" tab you will see that the quantities have been auto-assigned on the "Done" column.

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
