---
title: "OCA供应商费用报销account_invoice_reimbursable"
source: "http://www.thinkltd.cn/forum/2/ocaaccount-invoice-reimbursable-2706"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA供应商费用报销account_invoice_reimbursable

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaaccount-invoice-reimbursable-2706>

模块链接：https://github.com/OCA/account-invoicing/tree/11.0/account_invoice_reimbursable

例如，供应商提供服务，服务费用1000，服务过程中，垫款代买了10000元设备。总共应该支付供应商11000元。收到的发票应该是两张，一种是供应商开的1000元，一种是设备商开的10000元。

This module adds the option to add reimbursables to supplier invoices.

Reimbursables are payments for services that your supplier has made on behalf of your company as part of an agreement. Your company receives two invoices: one from the supplier, that includes the reimbursable, and your company should pay, and one from the third party that has been paid by your supplier on your behalf.

For example, when you set up a company your lawyer might pay for various government fees on your behalf, that the lawyer is then going to pass on to you as a reimbursable in the invoice. You will still receive an invoice for the government fees, but you have no obligation to pay them, because they have already been paid by your lawyer.

###

### Usage

1.  Go to 'Accounting/Invoicing > Purchases > Documents > Vendors Bills'
2.  Create an invoice for a provider and add the reimbursables on the reimbursable page
3.  Validate the invoice


## 原帖外链配图

![[2-ocaaccount-invoice-reimbursable-2706-x194038c2.png]]
<small>原始地址: /web/image/1118/snipaste_20190126_173812.png?access_token=f45507b2-f3c0-4426-8b36-a3b13b218274</small>

![[2-ocaaccount-invoice-reimbursable-2706-x194038c2.png]]
<small>原始地址: /web/image/1120/snipaste_20190126_173937.png?access_token=b0bbcf57-859a-4b4e-ad6d-1f99ca71d0f0</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
