---
title: "OCA生产单MO产成品入库应用上架策略mrp_production_putaway_strategy"
source: "http://www.thinkltd.cn/forum/2/ocamomrp-production-putaway-strategy-3022"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA生产单MO产成品入库应用上架策略mrp_production_putaway_strategy

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocamomrp-production-putaway-strategy-3022>

模块链接：

12.0版的模块链接：

MO创建时候，系统检查成品入库库位，如果该库位有上架策略，自动应用上架策略得到上架库位，MO的成品入库库位自动修改为上架库位。

This module allows to apply putaway strategies to the products resulting from the manufacturing orders.

The finished products will be placed in the location designated by the putaway strategy (if they do not have another destination move), based on the finished products location that was defined in the manufacturing order.

## [Configuration](https://github.com/OCA/manufacture/tree/11.0/mrp_production_putaway_strategy#id1)

To configure a putaway strategy follow the next steps:

1.  Go to 'Inventory / Settings'. Activate the option 'Multi-Step Routes' and save.
2.  Go again to 'Inventory / Settings' and press 'Set Putaway Strategies on Locations'. Then define a putaway strategy in the location zone where the finished products are supposed to be placed, and indicate the specific sub-location/bin where the products should be placed.

##

## [Usage](https://github.com/OCA/manufacture/tree/11.0/mrp_production_putaway_strategy#id2)

To use this module proceed as follows:

1.  Create a manufacturing order and indicate the product and the finished products location zone.
2.  Confirm the manufacturing order.
3.  You will notice that the finished products location has changed to the putaway location, and the chatter shows a message indicating that the putaway strategy was applied.

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
