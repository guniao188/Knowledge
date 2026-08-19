---
title: "仓库超收超发Bug修正及Extra/New Move原因分析"
source: "http://www.thinkltd.cn/forum/1/bugextra-new-move-363"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 仓库超收超发Bug修正及Extra/New Move原因分析

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/bugextra-new-move-363>

正常情况下，Odoo12中，收货单或发货单上，实际发货数量多于初始数量，验证时候，系统会提示超发了。但如果数量没有多，而是发了一个不在初始需求中的产品，系统不会提示超发了。在扫码出入库操作的情况下，这个问题尤为严重，例如，如果误扫了一个不在初始需求中的产品，系统自动添加该产品到Stock Picking，验证时候也不提示超发。另外一种情况，如果多扫了一个数量（扫描数量多余初始需求数量），系统自动将多扫的数量按添加新产品处理（另起添加一个产品行），这使得扫描数量多余初始数量的情况，系统也不会提示超发。这些原因，导致扫描出入库的情况，很容易超收超发。

【问题原因】

问题出在stock模块中，判断是否超发时候，系统只判断了实际数量多于初始数量的情况，没有判断超发了初始需求中不存在的产品的情况。问题代码 stock\models\stock_picking.py 的方法 def _get_overprocessed_stock_moves(self):

```python
     def _get_overprocessed_stock_moves(self):
        self.ensure_one()
        return self.move_lines.filtered(
            lambda move: move.product_uom_qty != 0 and float_compare(move.quantity_done, move.product_uom_qty,
                                                                     precision_rounding=move.product_uom.rounding) == 1
        )
```

安装这个模块修正该Bug：[/forum/2/question/stock-barcode-show-total-3147](http://www.thinkltd.cn/forum/2/question/stock-barcode-show-total-3147)

Bug修正后，扫码超收超发提示画面：

![[1-bugextra-new-move-363-e68adf0a.png]]

## 补充/答案 1

另外，如果是扫描了一个初始需求中不存在的产品，或者手工添加了一个初始需求中不存在的产品，验证时候，系统会在该Picking上自动添加一个新的Stock Move，该Stock Move的name 字段含有 Extra字样(V10.0)，或者New 字样(V12.0)

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
