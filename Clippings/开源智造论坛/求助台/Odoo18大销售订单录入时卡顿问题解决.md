---
title: "Odoo18大销售订单录入时卡顿问题解决"
source: "http://www.thinkltd.cn/forum/1/odoo18-4011"
forum: "求助台"
author: "肖相扶"
published: 2024-12-14
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo18大销售订单录入时卡顿问题解决

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-12-14
> <http://www.thinkltd.cn/forum/1/odoo18-4011>

【问题】客户伊酷环保碰到的问题。Odoo18大的销售订单（超过80个明细行），明细行录入时候明显卡顿。随着明细行的增多，卡顿越明显。

【原因】

1.  Odoo18新增组合产品处理功能，订单明细行变化时候，系统处理组合产品的明细行。参见文件 OSCGODOO18\source\addons\sale\models\sale_order.py 方法 def _onchange_order_line(self)
2.  该方法总是要轮询一遍订单明细行，当明细行很多以后，轮询速度变慢（经测试，80个明细行，差不多要500毫秒），因而出现卡顿。

【解决方法】

1.  销售订单模型上增加一个Boolean字段"含组合产品"，默认值为False。销售订单模型的方法 def _onchange_order_line中，如果 含组合产品为False则直接返回，不轮询明细行。
2.  明细行上产品录入时候，如果录入的是组合产品，自动将“ 含组合产品 ”字段置为True，实现代码参考 文件OSCGODOO18\source\addons\sale\models\sale_order_line.py，方法 def _onchange_product_id_warning(self)

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
