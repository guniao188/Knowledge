---
title: "OCA发票折上折account_invoice_triple_discount"
source: "http://www.thinkltd.cn/forum/2/ocaaccount-invoice-triple-discount-2704"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA发票折上折account_invoice_triple_discount

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaaccount-invoice-triple-discount-2704>

模块链接：

This module allows to have three successive discounts on each invoice line.

###

### Usage

Create a new invoice and add discounts in any of the three discount fields given. They go in order of precedence so discount 2 will be calculated over discount 1 and discount 3 over the result of discount 2. For example, let's divide by two on every discount:

Unit price: 600.00 ->

> - Disc. 1 = 50% -> Amount = 300.00
> - Disc. 2 = 50% -> Amount = 150.00
> - Disc. 3 = 50% -> Amount = 75.00

You can also use negative values to charge instead of discount:

Unit price: 600.00 ->

> - Disc. 1 = 50% -> Amount = 300.00
> - Disc. 2 = -5% -> Amount = 315.00


## 原帖外链配图

![[2-ocaaccount-invoice-triple-discount-2-x194038c2.png]]
<small>原始地址: /web/image/1114/snipaste_20190126_171744.png?access_token=4d1586c2-8353-4d26-bf2e-bf70b5133bb6</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
