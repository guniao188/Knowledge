---
title: "OCA回款滞纳金计算account_credit_control_dunning_fees"
source: "http://www.thinkltd.cn/forum/2/ocaaccount-credit-control-dunning-fees-2733"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA回款滞纳金计算account_credit_control_dunning_fees

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaaccount-credit-control-dunning-fees-2733>

模块链接：

This module extends the functionality of account_credit_control to add the notion of dunning fees on credit control lines.

###

### Configuration

You can specifiy a fixed fees amount, a product and a currency on the credit control level form.

The amount will be used as fees values the currency will determine the currency of the fee. If the credit control line has not the same currency as the fees currency, fees will be converted to the credit control line currency.

The product is used to compute taxes in reconciliation process.

###

### Usage

Fees are automatically computed on credit run and saved on the generated credit lines.

Fees can be manually edited as long credit line is draft

Credit control Summary report includes a new fees column: Support of fees price list


## 原帖外链配图

![[2-ocaaccount-credit-control-dunning-fe-x194038c2.png]]
<small>原始地址: /web/image/1184/snipaste_20190127_181501.png?access_token=fe01b693-0787-497b-8985-4b23129d3950</small>

![[2-ocaaccount-credit-control-dunning-fe-x194038c2.png]]
<small>原始地址: /web/image/1186/snipaste_20190127_181554.png?access_token=90c5be1a-88e2-4fd6-baf2-ec276d3d4e2f</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
