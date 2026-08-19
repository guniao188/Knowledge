---
title: "生产工单Work Order操作按钮详解"
source: "http://www.thinkltd.cn/forum/1/work-order-345"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 生产工单Work Order操作按钮详解

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/work-order-345>

Work Order操作按钮功能详解：

1.  Done: 点击该按钮，系统将Current Qty 的数量累加到 Quantity Produced。Current Qty数量必须大于0，允许很大，大于MO上的应生产数量。如果累加后Quantity Produced数量大于等于MO上的应生产数量，则系统自动Finish这个WO（状态变为Finished）。如果BoM表上指定了在本工序上消耗哪些原料，则Current Qty 的数量累加到 Quantity Produced的同时，系统自动填写MO上的原料消耗行的 Consumed 列数量（但不会自动Done原料消耗的Stock Move）。如果该WO是MO上的最后一个工单，系统同时将Quantity Produced数量写入MO的Finished Products 。

2.  Scrap: 点击按钮，系统弹窗，填写原料及数量，报废该原料（系统自动创建一个Stock Move，从MO上的原料库位移动到报废库位）。如果MO已经完成(状态为 done)，点击报废按钮，系统弹窗选择成品，报废成品（系统自动创建一个Stock Move，从MO上的成品库位移动到报废库位）。

3.  Finish Order: 点击该按钮，系统自动填写 Time Track明细（mrp.workcenter.productivity）中的结束时间，并将该WO状态变为Finished 。Odoo默认情况下不显示该按钮，Invisible条件如下面语句所示，其中 is_produced 字段值是，当Quantity Produced 的数量大于等于MO的数量时候，is_produced才为True 。

为了允许手工结束WO单，建议该按钮如下修改：

![[1-work-order-345-d9c81301.png]]

## 补充/答案 1

![[1-work-order-345-b85388d1.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
