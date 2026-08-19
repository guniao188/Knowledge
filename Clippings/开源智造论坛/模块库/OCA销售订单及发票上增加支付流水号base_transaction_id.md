---
title: "OCA销售订单及发票上增加支付流水号base_transaction_id"
source: "http://www.thinkltd.cn/forum/2/ocabase-transaction-id-2718"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA销售订单及发票上增加支付流水号base_transaction_id

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocabase-transaction-id-2718>

模块链接：

1.  销售订单及发票上增加支付流水号字段transaction_ref，支付流水号从SO带入发票。实收应收核销时候，按支付流水号核销。

2.  会计分录Account Move Line上也增加字段transaction_ref， 银行对账单核销时候，增加按transaction_ref的核销条件。

3.  此功能应用于电商行业。

Adds transaction ID to invoice and sale models and views.

On Sales order, you can specify the transaction ID used for the payment and it will be propagated to the invoice (even if made from packing). This is mostly used for e-commerce handling.

You can then add a mapping on that SO field to save the e-commerce financial Transaction ID into the Odoo sale order field.

The main purpose is to ease the reconciliation process and be able to find the partner when importing the bank statement.


## 原帖外链配图

![[2-ocabase-transaction-id-2718-x194038c2.png]]
<small>原始地址: /web/image/1154/snipaste_20190127_114654.png?access_token=c5108d68-ea7c-47b3-9980-7c0dba5bb860</small>

![[2-ocabase-transaction-id-2718-x194038c2.png]]
<small>原始地址: /web/image/1156/snipaste_20190127_114800.png?access_token=363dc316-fe31-4844-addd-5c1f4e763349</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
