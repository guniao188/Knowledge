---
title: "OCA前置StockMove数量变化自动修改后续StockMove数量stock_picking_purchase_propagate"
source: "http://www.thinkltd.cn/forum/2/ocastockmovestockmovestock-picking-purchase-propagate-2566"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA前置StockMove数量变化自动修改后续StockMove数量stock_picking_purchase_propagate

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocastockmovestockmovestock-picking-purchase-propagate-2566>

模块链接：

1.  以MTO订单采购为例。SO上客人要货11件，MTO采购商品，SO确认系统自动产生PO；

2.  采购询价过程中，只找到10件商品，下PO采购10件

3.  10件商品采购入库，但SO对应的出库Stock Move上还是11件。

4.  本模块增加功能，PO数量修改时候，系统自动将PO数量传导到之前产生PO的一系列Stock Move上。

This module allows to propagate the procurement group and the quantity of the purchase order at its confirmation to the ensuing picking and stock moves and their destination moves and pickings.

###

### Usage

This module can help you if your warehouse uses two- or three- steps reception.

In such a case, odoo's scheduler will generate internal transfers pickings with the procurement group defined on each orderpoint of the products in need.

So, if no procurement group is defined on the orderpoints, Odoo will generate only one internal transfer picking for all the products having needs, even if suppliers and delays could be totally different.

If the product is to be purchased, the scheduler will also generate a purchase order. However when confirming this purchase order, the generated receipt picking and its move will get the procurement group from the sale order, which doesn't match the procurement group of the ensuing internal transfers, what could be baffling for the stock operator who has to find the ensuing internal transfer.

Moreover, if the quantity is changed before confirming the purchase order, the receipt picking will be generated with the PO's quantity, whereas the ensuing moves and picking will still have the original quantity from the orderpoint. Therefore, if the quantity was reduced on the purchase order, the stock operator won't be able to close the move line in waiting state, although it's not expected to receive more quantity until the next purchase order.

Instead of provoking such headaches to stock operators, this module will propagate the procurement group and the quantity of the purchase order to the whole chain of moves and reassign them to new pickings.

This allows to have a clear match through the procurement group between purchase order, receipts and internal transfers, and allows as well stock operators not to worry about missing quantities which weren't ordered in the first place.


## 原帖外链配图

![[2-ocastockmovestockmovestock-picking-p-x194038c2.png]]
<small>原始地址: /web/image/845/snipaste_20190119_212604.png?access_token=d95f0756-10d9-4d48-939b-57d6a666fb2c</small>

![[2-ocastockmovestockmovestock-picking-p-x194038c2.png]]
<small>原始地址: /web/image/847/snipaste_20190119_212753.png?access_token=9878ecd7-9201-47ab-8a09-f65142be2b2a</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
