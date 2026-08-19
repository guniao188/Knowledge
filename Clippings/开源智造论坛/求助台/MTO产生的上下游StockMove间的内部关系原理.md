---
title: "MTO产生的上下游StockMove间的内部关系原理"
source: "http://www.thinkltd.cn/forum/1/mtostockmove-782"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# MTO产生的上下游StockMove间的内部关系原理

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/mtostockmove-782>

1.  MTO类产品，销售发货的Stock Move，会自动触发采购入库的Stock Move，采购入库的Stock Move和销售发货的Stock Move之间存在MTO上下游关系。即采购入库的Stock Move完成时候，销售发货的Stock Move立即自动锁货，且只锁采购入库的Stock Move的货（即使仓库有别的货，系统也不会锁）

2.  同理，生产单MO物料消耗的Stock Move，如果是MTO类的，也会自动触发领料的Stock Move，物料消耗的Stock Move和领料的Stock Move之间也存在MTO上下游关系。

3.  MTO上下游关系的内部原理是，上游Stock Move（采购入库、生产领料）的move_dest_ids字段指向下游Stock Move（销售发货、生产消耗），下游Stock Move的move_orig_ids字段指向上游Stock Move 。另外下游的Stock Move的procure_method字段设置为“make_to_order”。如此即建立了stock move的上下游的关系。

![[1-mtostockmove-782-fd7d3868.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
