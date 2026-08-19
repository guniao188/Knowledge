---
title: "OCA自动批量生成订货规则stock_orderpoint_generator"
source: "http://www.thinkltd.cn/forum/2/ocastock-orderpoint-generator-2856"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA自动批量生成订货规则stock_orderpoint_generator

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocastock-orderpoint-generator-2856>

模块链接：

Add a wizard to configure reordering rules for multiple products in one go, and allow to automatically update reordering rules from rule templates.

## [Configuration](https://github.com/OCA/stock-logistics-warehouse/tree/11.0/stock_orderpoint_generator#id1)

Reordering rule templates can be configured in "Inventory > Configuration > Products > Reordering Rule Templates".

The frequency of the cron that updates the Reordering Rules can be configured in "Settings > Technical > Automation > Scheduled Actions". The name of the scheduled action is "Reordering Rule Templates Generator".

##

## [Usage](https://github.com/OCA/stock-logistics-warehouse/tree/11.0/stock_orderpoint_generator#id2)

By activating the "Create Rules Automatically" on a reordering rule template, you are able to select a list of products. Any change on the template will then be replicated on the products Reordering Rules. The change is not immediate as it is processed by a scheduled action.

Lastly, you can promptly create Reordering Rules for a product or a product template using the "Reordering Rules Generator". Note that it will replace all the existing rules for the product. You will usually not want to use this feature on products that have Automatic Reordering Rules Templates.


## 原帖外链配图

![[2-ocastock-orderpoint-generator-2856-x194038c2.png]]
<small>原始地址: /web/image/1353/snipaste_20190215_122308.png?access_token=0cbc0a4b-db44-4c4e-900d-cfe22f96751a</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
