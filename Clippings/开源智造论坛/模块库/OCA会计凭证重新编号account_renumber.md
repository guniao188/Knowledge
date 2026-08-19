---
title: "OCA会计凭证重新编号account_renumber"
source: "http://www.thinkltd.cn/forum/2/ocaaccount-renumber-2738"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA会计凭证重新编号account_renumber

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaaccount-renumber-2738>

模块链接：

This module extends the functionality of accounting to allow the accounting manager to renumber account moves by date only for admin.

The wizard, which is accesible from the "End of Period" menuitem, lets you select journals, periods, and a starting number. When launched, it renumbers all posted moves that match selected criteria (after ordering them by date).

It will recreate the sequence number for each account move using its journal sequence, which means that:

- Sequences per journal are supported.
- Sequences with prefixes and suffixes based on the move date are also supported.
-

## [Usage](https://github.com/OCA/account-financial-tools/tree/11.0/account_renumber#id1)

To use this module, you need to:

1.  Be an accounting manager.
2.  Go to *Accounting > Adviser > Renumber journal entries*.
3.  Choose the *First number* of the journal entry that you want. It will be used to start numbering from there on.
4.  Choose the *Starting date* and *Ending date*, to set when you want the process to begin and end.
5.  Choose the journals where you want to perform the renumberings.
6.  Press *Renumber*.

Now, the wizard will locate all journal entries found in those journals and dates, and start numbering them without gaps in a sequential order that starts with the *First number* you chose and matches the entry date order.

If no matches are found, you will be alerted. Otherwise, you will be redirected to a view of all the entries that have been renumbered.


## 原帖外链配图

![[2-ocaaccount-renumber-2738-x194038c2.png]]
<small>原始地址: /web/image/1206/snipaste_20190127_210754.png?access_token=a0541c43-9d35-443b-802e-4017db354ce3</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
