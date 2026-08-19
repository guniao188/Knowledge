---
title: "OCA应收应付冲抵account_netting"
source: "http://www.thinkltd.cn/forum/2/ocaaccount-netting-2736"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA应收应付冲抵account_netting

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaaccount-netting-2736>

模块链接：

快速创建凭证，同一Partner应收账款和应付账款冲抵。

## AR/AP netting

This module allows to compensate the balance of a receivable account with the balance of a payable account for the same partner, creating a journal item that reflects this operation.

**WARNING**: This operation can be forbidden in your country by the accounting regulations, so you should check current laws before using it. For example, in Spain, this is not allowed at first instance, unless you document well the operation from both parties.

###

### Usage

From any account journal entries view:

- Accounting/Journal Entries/Journal Items

select all the lines that corresponds to both AR/AP operations from the same partner. Click on "More > Compensate". If the items don't correspond to the same partner or they aren't AR/AP accounts, you will get an error.

On contrary, a dialog box will be presented with the result of the operation and a selection of the journal to register the operation. When you click on the "Compensate" button, a journal entry is created with the corresponding counterparts of the AR/AP operations.


## 原帖外链配图

![[2-ocaaccount-netting-2736-x194038c2.png]]
<small>原始地址: /web/image/1200/snipaste_20190127_205409.png?access_token=5a466471-6c8a-4eca-babf-87dc59a32892</small>

![[2-ocaaccount-netting-2736-x194038c2.png]]
<small>原始地址: /web/image/1202/snipaste_20190127_205443.png?access_token=11b1b7c8-ce21-4518-b4c2-d317d672245a</small>

![[2-ocaaccount-netting-2736-x194038c2.png]]
<small>原始地址: /web/image/1204/snipaste_20190127_205657.png?access_token=119903da-2a31-41e9-a222-2b099232a095</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
