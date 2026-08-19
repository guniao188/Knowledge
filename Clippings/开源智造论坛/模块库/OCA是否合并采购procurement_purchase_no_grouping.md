---
title: "OCA是否合并采购procurement_purchase_no_grouping"
source: "http://www.thinkltd.cn/forum/2/ocaprocurement-purchase-no-grouping-2597"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA是否合并采购procurement_purchase_no_grouping

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaprocurement-purchase-no-grouping-2597>

模块链接：

This module allows to not group generated purchase orders from procurements. The grouping behaviour can be configurable at product category level.

Go to each product category, and select one of these values in the field "Procured purchase grouping":

- *Standard grouping (default)*: With this option, procurements will generate purchase orders as always, grouping lines and orders when possible.
- *No line grouping*: With this value, if there are any open purchase order for the same supplier, it will be reused, but lines won't be merged.
- *No order grouping*: This option will prevent any kind of grouping.

## 补充/答案 1

这个如果跟着路线配置走，也许更合理，在系统原有的功能中，MTO的虽然可以设置【保留】，但如果和安全库存都有草稿状态同一家供应商的，仍会合并，因为安全库存不管【保留】是否为空或传递，总是会去合并PO.

## 补充/答案 2

这个模块用到procurement.rule。可惜12都没有这个这个表了

## 补充/答案 3

Odoo12改成stock.rule 了，应该内容差不多，名字改了一下。

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
