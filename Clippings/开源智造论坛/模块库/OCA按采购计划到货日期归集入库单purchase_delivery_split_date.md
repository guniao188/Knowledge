---
title: "OCA按采购计划到货日期归集入库单purchase_delivery_split_date"
source: "http://www.thinkltd.cn/forum/2/ocapurchase-delivery-split-date-2606"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA按采购计划到货日期归集入库单purchase_delivery_split_date

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocapurchase-delivery-split-date-2606>

模块链接：

When this module is installed, each Purchase Order you confirm will generate one Incoming Shipment for each schedule date indicated in the Purchase Order Lines.

Once the Purchase Order has been confirmed, subsequent changes made to the scheduled dates in the PO lines will produce a reorganization of the corresponding stock moves in the Incoming Shipments, creating/deleting new Incoming Shipments when needed, to ensure that each Incoming Shipment contains moves to be received in the same date.

This module is also designed for extensibility, so that you can define in other modules new criteria to split deliveries.


## 原帖外链配图

![[2-ocapurchase-delivery-split-date-2606-xbe6f5358.png]]
<small>原始地址: https://raw.githubusercontent.com/OCA/purchase-workflow/11.0/purchase_delivery_split_date/static/description/s</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
