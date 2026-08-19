---
title: "OCA设定科目标志让银行对账单不自动调节account_skip_bank_reconciliation"
source: "http://www.thinkltd.cn/forum/2/ocaaccount-skip-bank-reconciliation-2726"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA设定科目标志让银行对账单不自动调节account_skip_bank_reconciliation

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaaccount-skip-bank-reconciliation-2726>

模块链接：

This module allows to exclude from bank statement reconciliation all journal items of a specific reconcilable account.

Usually, you would want to that in accounts like the Goods Received Not Invoiced, which are required to be reconcilable to be able to have proper traceability in stock received but their reconciliation is done using the account_mass_reconcile module.

## [Usage](https://github.com/OCA/account-reconcile/tree/11.0/account_skip_bank_reconciliation#id1)

To use this module, you need to:

1.  Go to Invoicing / Configuration / Accounting / Charts of Accounts and open a reconcilable account.
2.  In that account, select or not the Exclude from Bank Reconciliation option.


## 原帖外链配图

![[2-ocaaccount-skip-bank-reconciliation--x194038c2.png]]
<small>原始地址: /web/image/1170/snipaste_20190127_144229.png?access_token=0467fe9a-877a-4e60-9a49-7e61c5fad354</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
