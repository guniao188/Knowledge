---
title: "OCA禁止等待其他入库的Picking取消stock_picking_restrict_cancel_with_orig_move"
source: "http://www.thinkltd.cn/forum/2/ocapickingstock-picking-restrict-cancel-with-orig-move-2546"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA禁止等待其他入库的Picking取消stock_picking_restrict_cancel_with_orig_move

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocapickingstock-picking-restrict-cancel-with-orig-move-2546>

模块链接：

Picking取消时候，此模块检查一下该Picking的Stock Move是否存在前置Stock Move，如果有，则提示必须先取消前置Stock Move才可以取消本Picking。

前置Stock Move：处于“等待其他入库” 状态的Stock Move，其他入库就是该Stock Move的前置Stock Move。如MTO时候，采购入库的Stock Move是销售出库Stock Move的前置Stock Move。

This module restricts the cancelation of stock picking, if any move is linked to a previous move, which is not canceled or done yet.

###

### Usage

Odoo allows to cancel any picking in a chain of moves between locations, and will automatically cancel the ensuing moves but leaves the previous ones in their actual state.

This module restricts this possibility and displays an error to the user, listing all the stock pickings containing stock moves linked to the picking the user is trying to cancel, so he can delete the original, ensuring all the following pickings will be canceled as well.

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
