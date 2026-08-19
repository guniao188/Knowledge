---
title: "OCA采购计划到货日期purchase_date_planned_manual"
source: "http://www.thinkltd.cn/forum/2/ocapurchase-date-planned-manual-2604"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA采购计划到货日期purchase_date_planned_manual

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocapurchase-date-planned-manual-2604>

模块链接：https://github.com/OCA/purchase-workflow/tree/11.0/purchase_date_planned_manual

This module makes the system to always respect the planned (or scheduled) date set by the user when creating a Purchase Order.

Additionally, this module modifies the PO views and sets in red the lines that are predicted to arrive late compared to the scheduled date and vendor lead time.

To use this module you could follow any of the two options below:

1.  Go to 'Purchase' and create a purchase order.
2.  Manually set the scheduled date in the PO lines.
3.  This date will never be modified by the system and the lines that are expected to be late are highlighted in red.

Or:

1.  Create a procurement order for a product that can be bought and have the route 'buy' activated.
2.  Run the procurement.
3.  Now the scheduled date in the procurement is respected even if the line is added to a previously existing PO.

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
