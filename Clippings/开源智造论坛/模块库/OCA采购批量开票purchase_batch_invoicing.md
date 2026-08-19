---
title: "OCA采购批量开票purchase_batch_invoicing"
source: "http://www.thinkltd.cn/forum/2/ocapurchase-batch-invoicing-2701"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA采购批量开票purchase_batch_invoicing

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocapurchase-batch-invoicing-2701>

模块链接：

勾选PO，批量创建发票

计划任务，定期自动批量开票

This module extends the functionality of purchases to support batch invoicing purchase orders and to allow you to choose if you want them grouped by purchase order or by vendor.

[Configuration](https://github.com/OCA/account-invoicing/tree/11.0/purchase_batch_invoicing#id1)

An automated task is included to invoice all pending purchase orders every week, but it is disabled by default. To enable it:

1.  Have *Administration / Settings* permissions.
2.  Go to *[Your user menu] > About > Activate the developer mode*.
3.  Go to *Settings > Technical > Automation > Scheduled Actions > Invoice all pending purchase orders > Edit*.
4.  Enable it by clicking on *Active* and set the date accordingly.
5.  Save.

To use this module, you'll need:

1.  Have *Purchase / User* permissions.

##

## [Usage](https://github.com/OCA/account-invoicing/tree/11.0/purchase_batch_invoicing#id2)

To use this module, you need to:

1.  Go to *Purchases > Purchase > Purchase Orders > Create* and fill the form.

2.  Press *Confirm*.

3.  Press *Receive Products*.

4.  Press *Validate > Apply*.

5.  Repeat above steps a couple of times.

6.  Go back to *Purchase Orders*, select those you just created and press *Action > Batch Invoice*. Alternatively, you can use the *Create Invoice* button in the purchase order form.

7.  You get a wizard with a list of ready-to-invoice purchase orders. Choose the *Grouping* method.

8.  Press *Accept*.

9.  You will get to a screen where you can see all the vendor bills you just generated.


## 原帖外链配图

![[2-ocapurchase-batch-invoicing-2701-x194038c2.png]]
<small>原始地址: /web/image/1104/snipaste_20190126_155334.png?access_token=5ea39f28-679b-4d08-8c5c-437b22537b96</small>

![[2-ocapurchase-batch-invoicing-2701-x194038c2.png]]
<small>原始地址: /web/image/1106/snipaste_20190126_155407.png?access_token=d39ddac1-7f77-4d49-810c-6da10ec88b0e</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
