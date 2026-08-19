---
title: "OCA添加支付方式account_payment"
source: "http://www.thinkltd.cn/forum/2/ocaaccount-payment-2683"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA添加支付方式account_payment

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaaccount-payment-2683>

新增支付方式表单：

This module adds a new object *account.payment.mode*, that is used to better classify and route incoming/outgoing payment orders with the banks.

Partner、Invoice、Account Move Line、InvoicePDF打印上增加支付方式字段：

This module adds severals fields:

- the *Supplier Payment Mode* and *Customer Payment Mode* on Partners,
- the *Payment Mode* on Invoices.
- the *Show bank account* on Payment Mode.
- the *# of digits for customer bank account* on Payment Mode.
- the *Bank account from journals* on Payment Mode.

On a Payment Order, in the wizard *Select Invoices to Pay*, the invoices will be filtered per Payment Mode.

Allows to print in the invoice to which account number the payment (via SEPA direct debit) is going to be charged so the customer knows that information, but there are some customers that don't want that everyone looking at the invoice sees the full account number (and even GDPR can say a word about that), so that's the reason behind the several options.

SO上增加支付方式字段，并从Partner上自动带入SO，并自动带到Invoice，SO PDF打印上增加支付方式：

This modules adds one field on sale orders: *Payment Mode*. This field is copied from customer to sale order and then from sale order to customer invoice.

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
