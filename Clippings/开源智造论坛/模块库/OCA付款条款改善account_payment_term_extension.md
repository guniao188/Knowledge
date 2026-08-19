---
title: "OCA付款条款改善account_payment_term_extension"
source: "http://www.thinkltd.cn/forum/2/ocaaccount-payment-term-extension-2703"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA付款条款改善account_payment_term_extension

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaaccount-payment-term-extension-2703>

模块链接：

This module extends the functionality of payment terms to :

- support rounding, months and weeks on payment term lines
- allow to set more than one day of payment in payment terms
- if a payment term date is a holiday, it is postponed to a selected date
- allow to apply a chronological order on lines
  - for example, with a payment term which contains 2 lines
    - on standard, the due date of all lines is calculated from the invoice date
    - with this feature, the due date of the second line is calculated from the due date of the first line

###

### Configuration

To configure the Payment Terms and see the new options on the Payment Term Lines, you need to:

1.  Go to the menu Accounting > Configuration > Management > Payment Terms.

To use multiple payment days, define for each payment term line which payment days apply, separated by spaces, commas or dashes. To use holidays, insert the holiday and the date payment terms will be postponed to.


## 原帖外链配图

![[2-ocaaccount-payment-term-extension-27-x194038c2.png]]
<small>原始地址: /web/image/1112/snipaste_20190126_171026.png?access_token=4edccbb4-6360-4bd5-b62d-ea7025906a13</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
