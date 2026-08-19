---
title: "华霆电器Picking入库单验证特别慢的解决办法"
source: "http://www.thinkltd.cn/forum/1/picking-665"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 华霆电器Picking入库单验证特别慢的解决办法

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/picking-665>

【问题现象】

Odoo 13企业版，大的Picking入库单（超过100行），实际只入库一行，点击验证时候，系统特别慢，要等一两分钟。网上搜索，发现其他人也碰到这个问题：[https://www.odoo.com/zh_CN/forum/help-1/question/how-to-improve-the-stock-picking-validate-performance-126475 ](https://www.odoo.com/zh_CN/forum/help-1/question/how-to-improve-the-stock-picking-validate-performance-126475)

## 补充/答案 1

【问题调查】

参照这里的调查工具 [/forum/3/question/odoo-36](http://www.thinkltd.cn/forum/3/question/odoo-36)

使用工具pyFrame调查，发现主要耗时在于文件 stock_account\models\stock_move.py，方法 _run_fifo_vacuum ，下面是pyFrame生成的燃烧图：

进一步深入调查发现

1）_action_done中，每个Stock Move都会调用 product_price_update_before_done、_create_%s_svl、_run_fifo_vacuum。尤其是方法 _run_fifo_vacuum 很耗时。 如果Picking上有100个items，product_price_update_before_done、_create_%s_svl、_run_fifo_vacuum 三个方法会被调用100次。考虑到back_order的情况，即使只入库 1个产品，系统也会调用100次上述三个方法。应该修改成只调用一次，如此则 Validate 的速度提升100倍。参照下述修改代码：

```python
    def _action_done(self, cancel_backorder=False):

        todo = self.env['stock.move']

        for move in self:

            qty_done = sum(move.move_line_ids.mapped('qty_done'))

            if float_is_zero(qty_done, precision_rounding=move.product_id.uom_id.rounding):

                continue

            else:

                todo |= move

        return super(StockMove, todo)._action_done(cancel_backorder=cancel_backorder)
```

2）方法 _run_fifo_vacuum （代码文件 stock_account\models\product.py）性能改善。

     该方法不应该  ensure_one，下面代码：

svls_to_vacuum = self.env['stock.valuation.layer'].sudo().search([

```python
            ('product_id', '=', self.id),

            ('remaining_qty', '
```

从燃烧图看，同样的操作，方法 _run_fifo_vacuum 在修改前被调用了 178次，修改后只调用了 54次，性能提升了 3倍多。

## 补充/答案 2

实际发现有一点问题：

系统方法：_run_fifo_vacuum

![[1-picking-665-92589b6b.png]]

![[1-picking-665-04564dbe.png]]

如果要处理，那就还需要循环一下，但是循环之后会不会和系统的一样了？？？？

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
