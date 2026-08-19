---
title: "OCA业务员佣金、佣金计算公式等hr_commission、sale_commission_formula、sale_commission_pricelist"
source: "http://www.thinkltd.cn/forum/2/ocahr-commissionsale-commission-formulasale-commission-pricelist-2821"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA业务员佣金、佣金计算公式等hr_commission、sale_commission_formula、sale_commission_pricelist

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocahr-commissionsale-commission-formulasale-commission-pricelist-2821>

模块链接：

This module links sale_commission with hr module. For now, it only adds another type of agent whose commissions are not invoiced in the corresponding wizard.

This module extends sale_commission to introduce the use of formulas to compute the agent commissions.

To use this module, you need to:

- Go to Sales, Commission Types and create a commission with type formula

This module extends the functionality of sale_commission to allow you set a commission to pricelist item.

The commission is applied when the pricelist rule is applied, that is after changing product or quantity of sale order line.

To use this module, you need to:

1.  Go to Sales -> Configuration -> Settings -> Pricing -> Sale Price and activate: "Advanced pricing based on formulas (discounts, margins, rounding)"
2.  Go to Sales -> Configuration -> Price-list and edit an existing one or create a new one
3.  In the pricelist -> add a new item or open a new one
4.  You will find the field commission in the pricelist item


## 原帖外链配图

![[2-ocahr-commissionsale-commission-form-x194038c2.png]]
<small>原始地址: /web/image/1313/snipaste_20190206_212640.png?access_token=30f47c06-ce67-40a4-b171-06e560460ccd</small>

![[2-ocahr-commissionsale-commission-form-x194038c2.png]]
<small>原始地址: /web/image/1315/snipaste_20190206_213030.png?access_token=fb7382ee-971a-46fe-90a7-df0cae25f132</small>

![[2-ocahr-commissionsale-commission-form-x194038c2.png]]
<small>原始地址: /web/image/1317/snipaste_20190206_213324.png?access_token=2e4d6712-3d10-4ea6-b03b-e6176bf66e13</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
