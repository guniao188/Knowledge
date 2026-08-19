---
title: "OCA MTS+MTO补货规则stock_mts_mto_rule"
source: "http://www.thinkltd.cn/forum/2/oca-mts-mtostock-mts-mto-rule-2868"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA MTS+MTO补货规则stock_mts_mto_rule

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/oca-mts-mtostock-mts-mto-rule-2868>

12.0版链接：

模块链接：

## Stock MTS+MTO Rule

This module add a Make To Stock + Make to Order Route.

If you choose the make to stock + make to order rule instead of the make to order route, the creation of a purchase order will depend on the virtual stock. There are 3 cases :

1.  The virtual stock of the product is 0
    => It will act exactly like the make to order route.

2.  The virtual stock is equal to the quantity ordered
    => It will act exactly like a make to stock route

3.  The virtual stock is more than 0 but less than ordered quantity
    => On part of the products will be taken from stock and a purchase order
    will be created for the rest. So it will act like both make to order and make to stock rule.

Example : We have a virtual stock of : 1 product A A sale Order is made for 3 products A. 2 Procurements will be created :

1.  1 with a make to stock rule and a quantity of 1
2.  1 with a make to order rule and a quantity of 2.

After validation, a purchase order with 2 products will be created.

###

### Configuration

You have to select 'Use MTO+MTS rules' on the company's warehouse form.

###

### Usage

You have to select the mts+mto route on the product form. You should not select both the mts+mto route and the mto route.

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
