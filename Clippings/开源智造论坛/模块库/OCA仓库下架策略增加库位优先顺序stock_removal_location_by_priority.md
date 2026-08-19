---
title: "OCA仓库下架策略增加库位优先顺序stock_removal_location_by_priority"
source: "http://www.thinkltd.cn/forum/2/ocastock-removal-location-by-priority-2874"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA仓库下架策略增加库位优先顺序stock_removal_location_by_priority

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocastock-removal-location-by-priority-2874>

模块链接：

This module adds a removal priority field on stock locations. This priority applies when removing a product from different stock locations and the incoming dates are equal in both locations.

## [Configuration](https://github.com/OCA/stock-logistics-warehouse/tree/11.0/stock_removal_location_by_priority#id1)

You can activate the removal priority as follows:

1.  Go to "Inventory > Configuration > Settings"
2.  In 'Operations' section, mark the "Removal Priority" option.
3.  You also need to activate the following settings in the section *Warehouse* if they are not yet:
    1.  Manage several locations using *Storage Locations* option.
    2.  Advanced routing using "Multi-Step Routes" option.

Then, set the *Removal Priority* in the desired locations. Remember that a lower number means more priority:

1.  Go to "Inventory > Configuration > Warehouse Management > Locations"
2.  In each Location form, in the Logistics section, put a Removal Priority.

##

## [Usage](https://github.com/OCA/stock-logistics-warehouse/tree/11.0/stock_removal_location_by_priority#id2)

After configure your locations properly, the system will select the quant at the location with more priority in case of equal date, no matter if you use FIFO or LIFO removal strategy.


## 原帖外链配图

![[2-ocastock-removal-location-by-priorit-x194038c2.png]]
<small>原始地址: /web/image/1367/snipaste_20190215_182018.png?access_token=8cd4126f-e906-4882-897f-6a8af8e81628</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
