---
title: "OCA销售订单SO归档sale_order_archive"
source: "http://www.thinkltd.cn/forum/2/ocasosale-order-archive-2673"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA销售订单SO归档sale_order_archive

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocasosale-order-archive-2673>

模块链接：

On a system with a high volume of sales, the number of sale orders displayed in the list view can become huge. This module allows to archive Sale Orders that are in status Locked or Cancelled.

If a sale order is archived, it will be hidden from the sale orders list view.

This module only depends on module sale, but it could be used in combination with OCA module 'record_archiver' in order to automatically archive old sale orders.

## [Usage](https://github.com/OCA/sale-workflow/tree/11.0/sale_order_archive#id1)

To archive sale orders, you need to:

1.  Open the tree view of sale orders.
2.  Select a sale order (in status Locked or Cancelled) you want to archive.
3.  Click on the Archive (Active) smart button.
4.  The sale order is now archived.

To unarchive sale orders, you need to:

1.  Open the tree view of sale orders.
2.  In the filter box select the Archived filter. The list of archived sale orders will be displayed.
3.  Select the sale order (in status Locked or Cancelled) you want to restore to Active.
4.  Click on the Restore (Archived) smart button.
5.  The sale order is now active.


## 原帖外链配图

![[2-ocasosale-order-archive-2673-x194038c2.png]]
<small>原始地址: /web/image/1018/snipaste_20190121_103754.png?access_token=cbea48f6-5147-43d3-899e-4a8e39582a44</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
