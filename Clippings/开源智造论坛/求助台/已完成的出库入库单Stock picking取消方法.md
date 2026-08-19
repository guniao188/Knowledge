---
title: "已完成的出库入库单Stock picking取消方法"
source: "http://www.thinkltd.cn/forum/1/stock-picking-382"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 已完成的出库入库单Stock picking取消方法

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/stock-picking-382>

有时候由于错误操作，把不该验证的出库单、入库单、Stock Picking验证掉了，希望取消掉该单子。常规做法是做退货处理，但因为是误操作，实际并没有收发货，做退货操作，虽然账面库存数据对了，但仓库单据和实际出入库操作不符。

经测试验证，还可以有一个操作方法，写一个Server Action，将该Picking的Stock Move Line的完成数量修改为 0 即可。如此，系统会自动恢复背后的Quants和Stock Move：Stock Move的完成数量（字段product_uom_qty）变为0，目标库的quants数量变为0，源库位的Quant数量恢复之前数量。

服务器动作一行代码：record.move_line_ids.write({'qty_done':0})

如果该Picking关联了SO或者PO，会自动触发系统重新计算一下已发货/已收货数量。触发逻辑说明如下：

SO、PO的已发货/已收货数量是计算型字段，计算逻辑是，Order Line关联的，已经完成的 Stock Move 的product_uom_qty 字段值汇总，作为已发货/已收货数量。当Stock Move的字段值 product_uom_qty 发生变化时候，会自动触发SO、PO的已发货/已收货数量重新计算。

![[1-stock-picking-382-fed8b403.png]]

![[1-stock-picking-382-d28205ca.png]]

## 补充/答案 1

如果能同时让picking单及move都变为取消状态就更好了。

服务器动作：

record.move_line_ids.write({'qty_done':0})
record.write({'state':'cancel'})
record.move_lines.write({'state':'cancel'})

## 补充/答案 2

应用市场有一个模块干类似的活，买的人挺多的：

看来大家都被这个问题折磨了

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
