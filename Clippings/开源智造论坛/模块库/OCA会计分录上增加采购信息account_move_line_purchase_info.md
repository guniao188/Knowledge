---
title: "OCA会计分录上增加采购信息account_move_line_purchase_info"
source: "http://www.thinkltd.cn/forum/2/ocaaccount-move-line-purchase-info-2725"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA会计分录上增加采购信息account_move_line_purchase_info

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaaccount-move-line-purchase-info-2725>

模块链接：

在Account Move Line上增加PO Line字段，目的是结合另一个模块（参考 [account_mass_reconcile_by_purchase_line](http://www.thinkltd.cn/forum/2/question/ocaaccount-mass-reconcile-by-purchase-line-2724)），完成应付暂估的核销。

This module will add the purchase order line to journal items.

The ultimate goal is to establish the purchase order line as one of the key fields to reconcile the Goods Received Not Invoiced accrual account.

###

### Usage

The purchase order line will be automatically copied to the journal items.

- When a supplier invoice is created referencing purchase orders, the purchase order line will be copied to the corresponding journal item.
- When a stock move is validated and generates a journal entry, the purchase order line is copied to the account move line.

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
