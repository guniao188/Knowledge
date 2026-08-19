---
title: "Odoo17入库出库中move line、quant的关系及性能优化"
source: "http://www.thinkltd.cn/forum/1/odoo17move-linequant-3886"
forum: "求助台"
author: "肖相扶"
published: 2024-02-22
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo17入库出库中move line、quant的关系及性能优化

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-02-22
> <http://www.thinkltd.cn/forum/1/odoo17move-linequant-3886>

【入库出库的内部逻辑】

1.  Picking上的按钮操作“标记待办”逻辑
2.  1.  对应Picking方法 action_confirm，以及stock.move的方法 _action_confirm，参见代码文件 OSCGODOO17\source\addons\stock\models\stock_move.py
    2.  stock.move的方法 _action_confirm，最重要的一件事情是，自动查找合适的补货路线，按补货规则自动创建上游或下游的stock move。例如，mto类型的stock move，系统自动创建补货的stock move，或者补货的PO（PO确认时候生成的入库stock move再关联到当前 stock move。
    3.  mto类型（stock.move的procure_method字段）的stock move，上下游的stock move通过字段 move_orig_ids 和 move_dest_ids 关联。例如销售出库stock move MTO自动生成PO，PO确认后生成的入库stock move。二者关联关系是：入库stock move作为出库stock move的move_orig_ids，出库stock move作为入库stock move的move_dest_ids
3.  Picking上的按钮操作“保留”逻辑：
4.  1.  对应Picking方法 action_assign，以及stock move的方法 _action_assign
```python
    2.  stock move的方法 _action_assign，最重要的事情是，应用上架规则（入库），或下架规则（出库），创建stock.move.line
    3.  如果是“ 可消耗 ”产品，系统不创建stock.quant， _action_assign方法中直接创建stock.move.line
    4.  如果是“可库存产品”， _action_assign方法中调用stock move的方法 _update_reserved_quantity 。该方法中， 系统应用下架规则，自动从stock.quant上锁货，如果锁到货，系统创建一条stock.move.line，如果从多个quant锁货，创建多条 stock.move.line 。
    5.  下架规则及锁货逻辑，代码参见 OSCGODOO17\source\addons\stock\models\stock_quant.py 方法 def _gather 。该方法中， 按库位、产品、包裹、批次/序列号查找quant，按下架规则排序quant。stock move的方法 _update_reserved_quantity 中，逐个quant检查其可用数量（quant的在手数量减去quant的预留数量），创建stock.move.line，同时将保留数量增加到quant的预留数量字段。保留一个quant，创建一个stock.move.line。
```

5.  Picking上的按钮操作“验证”逻辑：
6.  1.  对应Picking方法_action_done，以及stock move方法 _action_done，以及stock move line的方法_action_done。参考代码OSCGODOO17\source\addons\stock\models\stock_move_line.py 方法 def _action_done
    2.  stock move line的方法  _action_done中，按保留时候的相同逻辑(quant的 _gather方法)，查找到第一条quant，扣减quant上的在收数量字段（ quantity ）和预留数量（ reserved_quantity ）字段。
    3.  例如，stock.move要出库3个产品， _action_assign方法中，找到锁货的quant，该quant数量为10，预留数量为0。 _action_assign方法中，将quant的预留数量加3，同时创建数量为3的一条stock.move.line。验证时候（stock move line的方法_action_done，以及 _synchronize_quant， stock.quant的方法 _update_available_quantity），quant的在手数量字段减3，预留数量字段也减3。如此，验证后，quant的在手数量为7，预留数量为0 。

【大数量序列号产品入库出库性能问题】

1.  一万个序列号产品的入库、出库时候，系统要处理一万个stock move line, 对应的要创建/更新1万个stock quant。实测下来，此处入库或出库特别慢，要10分钟以上。
2.  主要的性能卡点在于代码文件OSCGODOO17\source\addons\stock\models\stock_move_line.py 的方法 def _action_done 中，代码段 for ml in mls_todo: ，该代码段逐条move line反复查找/更新/创建 stock quant，处理特别耗时。
3.  针对序列号产品，不必考虑下架规则、上架规则，也不必考虑从多个stock quant上扣减数量，因为每个stock quant的数量都是1，每个move line的数量也是1，且move line和quant可以根据lot_id一一对应起来。如此，可以简化move line 的  _action_done，直接批量创建stock quant即可。
4.  创建规则：如果是入库（location_id.usage != 'internal'）的move line，创建两个 stock.quant, 一个location是ml 的location_id，数量为 -1，一个是ml的location_dest_id, 数量是 1
5.  创建规则：如果是出库(location_dest_id.usage != 'internal')的move line, 直接按ml 的product_id, 及 lot_id搜索stock.quant，而后stock.quant 的location_id 改成 ml的location_dest_id即可
6.  入库出库的stock quant截图参考 

![[1-odoo17move-linequant-3886-7dca8ca1.png]]


## 附件

- [[附件/forum/1-odoo17move-linequant-3886-性能分析.rar|性能分析.rar]] (5.8 MB)

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
