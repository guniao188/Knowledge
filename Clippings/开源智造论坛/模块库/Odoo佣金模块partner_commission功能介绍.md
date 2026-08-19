---
title: "Odoo佣金模块partner_commission功能介绍"
source: "http://www.thinkltd.cn/forum/2/odoopartner-commission-3865"
forum: "模块库"
author: "肖相扶"
published: 2024-01-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo佣金模块partner_commission功能介绍

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-01-15
> <http://www.thinkltd.cn/forum/2/odoopartner-commission-3865>

【模块功能】

1.  Odoo14开始，企业版新增加了销售佣金模块partner_commission
2.  该模块中可以设置佣金提成规则(CRM的设置菜单下，Commission Plans)，销售订单上，可以选择提成规则（commission_plan_id字段），以及佣金方(referrer_id)。
3.  Partner上增加佣金计划字段
4.  销售订单对应的客户发票上，新增两个和佣金有关字段：佣金方( Referrer )，以及佣金采购明细(Referrer Purchase Order line)。登记收款时候，系统自动创建一个佣金PO，及佣金采购明细。

【功能截图】

佣金计划:

![[2-odoopartner-commission-3865-88034912.png]]

Purchase Default Product: 系统自动创建佣金采购单时候，佣金采购明细上的产品，默认Commission。

Rules：指定产品类别，产品，销售订单模板，销售价格表，对应的佣金提成比例。如果勾选Capped(封顶)，Max Commission中指定佣金上限。

Partner上增加代理级别、佣金计划等字段：

![[2-odoopartner-commission-3865-7d054605.png]]

销售订单上增加佣金方、佣金计划、佣金金额字段：

![[2-odoopartner-commission-3865-45f0bcdc.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
