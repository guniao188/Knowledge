---
title: "成本价格计算时候报candidate.quantity 除零错误"
source: "http://www.thinkltd.cn/forum/1/candidate-quantity-694"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 成本价格计算时候报candidate.quantity 除零错误

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/candidate-quantity-694>

【报错现象】

销售发票发布时候，报下述错误：

![[1-candidate-quantity-694-7ee50f32.png]]

【Bug原因】

发票发布，系统计算平均成本价格时候，按先进先出原则查找成本的Stock Value Layer记录，并计算锁货总价值。计算逻辑上，系统没考虑数量为零的svl的情况。经查，Odoo13,14都存在此Bug。修正策略如下：

代码文件：odoo13\odoo-server\addons\stock_account\models\product.py 方法  def _compute_average_price ，如下修正：

            # Odoo Bug修正（避免数量为0的SVL candidate 记录除0错误）

            #tmp_value += qty_taken_on_candidate * (candidate.value / candidate.quantity)

```python
            if float_is_zero(candidate.quantity, precision_rounding=candidate.uom_id.rounding):

                tmp_value += candidate.value + sum(candidate.stock_valuation_layer_ids.mapped('value'))

            else:

                tmp_value += qty_taken_on_candidate * \

                    ((candidate.value + sum(candidate.stock_valuation_layer_ids.mapped('value'))) / candidate.quantity)
```

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
