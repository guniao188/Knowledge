---
title: "OCA快速创建反向凭证（红冲分录）account_reversal"
source: "http://www.thinkltd.cn/forum/2/oca-account-reversal-2734"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA快速创建反向凭证（红冲分录）account_reversal

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/oca-account-reversal-2734>

模块链接：

This module adds an action "Reversal" on account moves, to allow the accountant to create reversal account moves in 2 clicks. Also add on account entries:

- a checkbox and filter "to be reversed"
- a link between an entry and its reversal entry

Odoo v11c include a similar action (overwritten by this addon), but with less features, for instance:

- Allowing inheritance
- Options like prefix (for journal entry and journal item), post and reconcile.
- Create a link between the entry and its reversal
- Mark entries to be reversed in the future.

##

## Usage

If you select an entry from Invoicing > Adviser > Accounting Entries > Journal Entries, then an action menu 'Reverse Entries' is available. If clicked, then a wizard allows user to select Reversal Date, Reversal Journal, Prefix, Post and Reconcile.

- If no Reversal Journal is selected, then the same journal is used
- If Post is True, then reversal entry will be posted else it will be leaved as a draft entry.
- If Post and Reconcile are True, then all entry lines with reconciled accounts of the entry will be reconciled with the reserval entry ones.

There is also a new menu Invoicing > Adviser > Accounting Entries > Journal Entries to be Reversed in order to allow tracking entries that must be reserved for any reason.


## 原帖外链配图

![[2-oca-account-reversal-2734-x194038c2.png]]
<small>原始地址: /web/image/1196/snipaste_20190127_204307.png?access_token=3b4bf024-60e0-4cc3-8c0d-8b63a6ef8340</small>

![[2-oca-account-reversal-2734-x194038c2.png]]
<small>原始地址: /web/image/1198/snipaste_20190127_204321.png?access_token=79427cc2-63fd-408f-8555-d6067bf37f9d</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
