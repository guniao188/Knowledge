---
title: "如何在客户发票上添加字段取值于so上的值"
source: "http://www.thinkltd.cn/forum/1/so-764"
forum: "求助台"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 如何在客户发票上添加字段取值于so上的值

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/so-764>

比如想在客户发票上或发票打印上要打印出so上的字段值，可以在客户发票account.move上新加字段，然后显示到打印qweb中即可。

添加字段的写法：

so是什么字段类型，在发票上新加的字段就要求是什么字段类型

如果是选择类型，需要在客户发票上也要加上选择值的范围

同时加上计算方法，代码如下：

```python
for record in self:
  record['x_sale_x_res_term_three'] = False
  sale_orders = record.invoice_line_ids.mapped('sale_line_ids.order_id')
  if sale_orders:
    record['x_sale_x_res_term_three'] = sale_orders[0].x_res_term_three
```

![[1-so-764-d94d3e6c.png]]

![[1-so-764-d8bd5d7d.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
