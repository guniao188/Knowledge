---
title: "OCA发票Invoice上直接修改汇率account_invoice_change_currency"
source: "http://www.thinkltd.cn/forum/2/ocainvoiceaccount-invoice-change-currency-2695"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA发票Invoice上直接修改汇率account_invoice_change_currency

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocainvoiceaccount-invoice-change-currency-2695>

模块链接：https://github.com/OCA/account-invoicing/tree/12.0/account_invoice_change_currency

发票Invoice上增加汇率字段，及按新汇率刷新价格的按钮。测试时候注意开启多币种功能。

This module allows users to update the currency of Invoices (in draft state) by a button Update Currency at the invoice form. After update to new currency, all the unit prices of invoice lines will be recomputed to new currency, thus the Total amounts (tax and without tax) of Invoice will be in the new currency also

Also this module allows user to set a custom rate that will be take to recompute all lines. By default the custom rate proposed is the rate between invoice currency and base currency (company currency), after the first coversion the custom rate will be proposed by default between last currency and invoice currency.

## 补充/答案 1

需要测试知道一下，是否对采购的对账单invoice也能生效？因为供应商账单在创建时就已经自动按本位币换算成明细行的单价了。

那如果另外指定的汇率，原币种的值，是否还能取得到？


## 原帖外链配图

![[2-ocainvoiceaccount-invoice-change-cur-x194038c2.png]]
<small>原始地址: /web/image/1080/snipaste_20190122_142341.png?access_token=d0212c4d-a8a9-4097-a2e2-d53388d9af67</small>

![[2-ocainvoiceaccount-invoice-change-cur-x194038c2.png]]
<small>原始地址: /web/image/1100/snipaste_20190124_160512.png?access_token=d8fa1417-bdeb-470e-875d-589e2cccdc81</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
