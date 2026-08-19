---
title: "OCA添加库存变更原因字段stock_change_qty_reason"
source: "http://www.thinkltd.cn/forum/2/ocastock-change-qty-reason-2854"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA添加库存变更原因字段stock_change_qty_reason

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocastock-change-qty-reason-2854>

模块链接：

1.  产品上数量变更时候，变更Wizard上添加原因字段

2.  库存调整明细行上添加原因字段

3.  增加是否预设原因的配置项

This module extends the product stock management and allows to set a reason in the wizard when changing the product quantity or in inventory adjustments per line.

It also can manage preset reasons optionally.

## [Configuration](https://github.com/OCA/stock-logistics-warehouse/tree/11.0/stock_change_qty_reason#id1)

To enable preset reason feature, you must:

- Go to: Inventory > Settings > Inventory Adjustment
- Enable: Preset Change Qty Reason
- Enable: Technical Settings > Manage Stock Change Qty Preset Reasons

Once is activate you will require te add a Preset reason to validate stock products change quantity.

To allow an Stock Manager configure preset reasons easily, you should:

- Select Stock Manager user on: Settings > Users
- Enable: Technical Settings > Manage Stock Change Qty Preset Reasons
- Go to Inventory > Configuration > Inventory Adjustment > Change Qty Reasons

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
