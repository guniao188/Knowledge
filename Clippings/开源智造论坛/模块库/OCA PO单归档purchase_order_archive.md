---
title: "OCA PO单归档purchase_order_archive"
source: "http://www.thinkltd.cn/forum/2/oca-popurchase-order-archive-2626"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA PO单归档purchase_order_archive

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/oca-popurchase-order-archive-2626>

模块链接：

On a system with a high volume of purchases, the number of purchase orders displayed in the list view can become huge. This module allows to archive Purchase Orders that are in status Locked or Cancelled.

If a purchase order is archived, it will be hidden from the purchase orders list view.

This module only depends on module purchase, but it could be used in combination with OCA module 'record_archiver' in order to automatically archive old purchase orders.

## [Usage](https://github.com/OCA/purchase-workflow/tree/11.0/purchase_order_archive#id1)

To archive purchase orders, you need to:

1.  Open the tree view of purchase orders.
2.  Select a purchase order (in status Locked or Cancelled) you want to archive.
3.  Click on the Archive (Active) smart button.
4.  The purchase order is now archived.

To unarchive purchase orders, you need to:

1.  Open the tree view of purchase orders.
2.  In the filter box select the Archived filter. The list of archived purchase orders will be displayed.
3.  Select the purchase order (in status Locked or Cancelled) you want to restore to Active.
4.  Click on the Restore (Archived) smart button.
5.  The purchase order is now active.


## 原帖外链配图

![[2-oca-popurchase-order-archive-2626-x194038c2.png]]
<small>原始地址: /web/image/936/snipaste_20190120_172643.png?access_token=48a941ba-85e5-404a-a7fb-e8dbcefb0223</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
