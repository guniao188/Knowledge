---
title: "OCA Invoice上增加Picking信息stock_picking_invoice_link"
source: "http://www.thinkltd.cn/forum/2/oca-invoicepickingstock-picking-invoice-link-2539"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA Invoice上增加Picking信息stock_picking_invoice_link

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/oca-invoicepickingstock-picking-invoice-link-2539>

模块链接：

客户发票上增加Tab页，显示关联的Picking信息。供应商账单上不显示。

This module adds a link between pickings and invoices as well as on the lines. Invoices are generated from sales orders. With this module, you can find back which deliveries an invoice relates to.

In standard, if you make a partial delivery and invoice it, then make remaining delivery and invoice it, it is impossible to known to what delivery the invoices relate to. You only have the quantity.

This module is also useful if you want to present data on the invoice report grouped by deliveries.

Note that the links are only for products with an invoicing policy set on delivery.

## 补充/答案 1

V14版本：

https://github.com/OCA/stock-logistics-workflow/tree/14.0/stock_picking_invoice_link


## 原帖外链配图

![[2-oca-invoicepickingstock-picking-invo-x194038c2.png]]
<small>原始地址: /web/image/803/snipaste_20190119_135856.png?access_token=44c3e1cd-5c68-450d-a1dd-15fc2c462c90</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
