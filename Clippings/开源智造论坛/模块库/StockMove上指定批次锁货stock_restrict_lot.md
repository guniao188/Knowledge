---
title: "StockMove上指定批次锁货stock_restrict_lot"
source: "http://www.thinkltd.cn/forum/2/stockmovestock-restrict-lot-3476"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# StockMove上指定批次锁货stock_restrict_lot

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/stockmovestock-restrict-lot-3476>

模块链接：[stock-logistics-workflow/stock_move.py at 14.0 · OCA/stock-logistics-workflow (github.com)](https://github.com/OCA/stock-logistics-workflow/tree/14.0/stock_restrict_lot)

【业务背景】

1.  化工厂，同一个料号，不同供应商，性能有差异，即使同一供应商的同一款原料，也有不同等级。针对这种情况，在Odoo中的一种处理方法是，在原料的批次上标注性能等级。

2.  给超市供货的食品企业，超市有剩余保质期的要求。例如，剩余保质期不低于2/3，意思是，如果该食品的保质期是180天，则剩余的保质期要求不低于 180 * 2/3 = 120天。不同超市对剩余保质期要求不同，如沃尔玛要求不低于1/2，家乐福要求不低于2/3，华润不低于4/5，等等。不同批次剩余保质期不同，针对这种情况，Odoo中的一种处理方法是，不同超市的订单，指定批次（符合保质期要求的批次）发货

3.  上面两种情况都有一个共同的需求，就是指定批次发货。

【模块功能】

1.  本模块在Stock Move上增加批次字段“restrict_lot_id”。

2.  当指定批次后，Stock Move锁货时候，只会锁该批次的库存。MTO产生补货需求时候，指定的批次可以传播到补货的Stock Move上。

3.  字段“restrict_lot_id”默认没有显示到XML视图上，实施时候需要添加到XML中显示。

【功能截图】

![[2-stockmovestock-restrict-lot-3476-fb178b1c.png]]

## 补充/答案 1

经过测试发现一个小问题：
2步领料下，如果我线边仓有批次B，并且可用。这时候我指定批次A（线边仓无货），那么就不会产生领料单；
如果我把线边仓的B占住，再指定批次A，是可以产生A的领料单的。

## 补充/答案 2

【Bug原因】

MO上配置成先消耗车间物料，不足部分再领料时候（mts_else_mto规则），MO确认时候，系统会检查车间库存，而后自动拆分组件消耗的Stock Move，其中一条为MTS，消耗车间库存，不足部分为MTO，发起领料。系统检查车间库存时候，没有考虑批次号，因而产生Bug

【Bug修正】

模块文件 stock_procurement_fix\models\stock_move.py 方法 def _adjust_procure_method(self):   增加下述红框的四行代码，重启Odoo即可。

```python
            if move._fields.get("restrict_lot_id", False) and move.restrict_lot_id:

                forecasted_qty = move.product_id.with_context(location=location.id, lot_id=move.restrict_lot_id.id).free_qty

                    if move._fields.get("restrict_lot_id", False) and move.restrict_lot_id:

                        def_vals["restrict_lot_id"] = move.restrict_lot_id.id
```

![[2-stockmovestock-restrict-lot-3476-115a09bb.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
