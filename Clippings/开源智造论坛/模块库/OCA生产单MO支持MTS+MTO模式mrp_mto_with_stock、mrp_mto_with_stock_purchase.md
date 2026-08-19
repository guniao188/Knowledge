---
title: "OCA生产单MO支持MTS+MTO模式mrp_mto_with_stock、mrp_mto_with_stock_purchase"
source: "http://www.thinkltd.cn/forum/2/ocamomts-mtomrp-mto-with-stockmrp-mto-with-stock-purchase-3015"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA生产单MO支持MTS+MTO模式mrp_mto_with_stock、mrp_mto_with_stock_purchase

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocamomts-mtomrp-mto-with-stockmrp-mto-with-stock-purchase-3015>

模块链接：

MO确认时候，生产领料功能，系统先锁定有库存的数量，不足库存的数量再按MTO原则发起补货。“不足库存的数量”的计算方法有两种，一种是MO需求数量减去在手数量，一种是MO需求数量减去可用数量。如果安装了模块mrp_mto_with_stock_purchase，可用数量的计算中，会加上Draft状态的PO数量。

This module extends the functionality of Manufacturing to support the creation of procurements only for a part of the raw material. It has 2 modes. The default one allow you to pull from stock until the quantity on hand is zero, and then create a procurement to fulfill the MO requirements. In this mode, the created procurements must be the ones fulfilling the MO that has generated it. The other mode is based on the forecast quantity. It will allow to pull from stock until the forecast quantity is zero and then create a procurement for the missing products. In this mode, there is no link between the procurement created and MO that has generated it. The procurement may be used to fulfill another MO.

###

### Configuration

To configure this module, you need to:

1.  Go to the products you want to follow this behaviour.
2.  In the view form go to the tab *Inventory* and set the *Manufacturing MTO/MTS Locations*. Any other location not specified here will have the standard behavior.

If you want to use the second mode, based on forecast quantity

1.  Go to the warehouse you want to follow this behaviour.
2.  In the view form go to the tab *Warehouse Configuration* and set the *MRP MTO with forecast stock*. You still need to configure the products like described in last step.

###

### Usage

To use this module, you need to:

1.  Go to *Manufacturing* and create a Manufacturing Order.
2.  Click on *Check availability*.
3.

模块链接：

This module make compatible mrp_mto_with_stock and purchase modules. Indeed, there is an option in mto_mto_with_stock to check the forecast stock when checking the availibility of a Manufacture Order. But this forecast stock does not take into account the quantities coming from draft POs. This module adds this behavior.

## [Configuration](https://github.com/OCA/manufacture/tree/11.0/mrp_mto_with_stock_purchase#id1)

- This module is installed automatically when mrp_mto_with_stock and purchase module are installed

##

## [Usage](https://github.com/OCA/manufacture/tree/11.0/mrp_mto_with_stock_purchase#id2)

When a manufacturing order is created out of a procurement evaluation (from an orderpoint, MTO,...) the calendar is considered in the computation of the planned start date of the manufacturing order.

For example, if it takes 1 day to manufacture a product and it is required for Monday, the manufacturing order will be created with planned start date on the previous Friday, if the warehouse operates under a Mo-Fri working calendar.


## 原帖外链配图

![[2-ocamomts-mtomrp-mto-with-stockmrp-mt-x194038c2.png]]
<small>原始地址: /web/image/1463/snipaste_20190310_160042.png?access_token=21cef4d0-ad3c-4cb8-8c6e-555349bd6ac5</small>

![[2-ocamomts-mtomrp-mto-with-stockmrp-mt-x194038c2.png]]
<small>原始地址: /web/image/1465/snipaste_20190310_160155.png?access_token=064bbbbe-a62a-4429-b418-839d6e07ab76</small>

![[2-ocamomts-mtomrp-mto-with-stockmrp-mt-x194038c2.png]]
<small>原始地址: /web/image/1467/snipaste_20190310_160619.png?access_token=1aa4cefc-6d01-49ff-a73d-5bb00674b58c</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
