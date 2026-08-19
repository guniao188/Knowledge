---
title: "OCA订货规则上增加补货单位字段stock_orderpoint_uom"
source: "http://www.thinkltd.cn/forum/2/ocastock-orderpoint-uom-2862"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA订货规则上增加补货单位字段stock_orderpoint_uom

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocastock-orderpoint-uom-2862>

模块链接：

1.  订货规则上增加补货单位字段

2.  产品上修改单位时候检查是否和订货规则不同类别，不同类别则报错。订货规则及补货单上修改单位时候，检查和产品的单位类别是否同一类别，不同则报错。

This module allows users users to define what unit of measure should be used in procurements created from minimum stock rules.

A typical use case would be a product that is stocked in centimeters, and needs to be restocked in meters from another warehouse. When the picking is created, the quantity to be transferred will be expressed in meters, making it easier for the people responsible for the transfers to understand the requirement.

###

### Configuration

To configure this module, you need to 'Inventory > Configuration > Settings' and enable 'Sell and purchase products in different units of measure' option.

###

### Usage

Go to 'Inventory > Master Data > Reordering Rules' and indicate a Procurement UoM.

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
