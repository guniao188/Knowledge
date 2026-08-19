---
title: "二开包裹类型体积模块stock_package_volume"
source: "http://www.thinkltd.cn/forum/2/stock-package-volume-3157"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开包裹类型体积模块stock_package_volume

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/stock-package-volume-3157>

SVN地址：odoo_ecommerce\12.0SRC\stock_package_volume

【业务背景】

Picking单上增加体积（产品体积、包裹体积）、重量信息。这些信息将用于分配集装箱。

【模块设计】

1） 增加包裹类型表单 stock.package.type, 字段包括 名称(name), 长(length)，宽(width)，高(high)，体积(volum) 字段
2）Picking上增加字段 包裹类型(many2one 到 stock.package.type)
3）包裹（stock.quant.package）上增加字段: 包裹类型(many2one 到 stock.package.type)，长(length)，宽(width)，高(high)，体积(volum)，重量(weight)。填写“包裹类型”时候，自动带出 长，宽，高，体积 四个字段值
4）仓库作业明细(stock.move.line) 上增加计算型字段: 体积(volum)，重量(weight)。体积计算规则是：
```python
    i. 如果“目的包裹result_package_id”字段不空，且目的包裹上的包裹类型字段有值，取目的包裹的体积；
    ii.如果目的包裹没值，取产品(product_id)上的体积(volum)字段，乘以“产品数量”，“产品数量”取值方法是，如果完成数qty_done不为零，取qty_done。如果qty_done为零，取保留数product_uom_qty。
    iii.重量计算规则是，取产品(product_id)上的重量(weight)字段，乘以“产品数量”，“产品数量”取值方法是，如果完成数qty_done不为零，取qty_done。如果qty_done为零，取保留数product_uom_qty。
```

5) Picking上点击“打入包裹”按钮时候，如果Picking上填写了"包裹类型"，将“包裹类型”字段写入包裹（stock.quant.package）

![[2-stock-package-volume-3157-e76caa82.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
