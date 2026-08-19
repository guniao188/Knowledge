---
title: "Odoo14发票/账单上添加预付/预收账款的技术实现原理"
source: "http://www.thinkltd.cn/forum/1/odoo14-737"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo14发票/账单上添加预付/预收账款的技术实现原理

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo14-737>

如下图，添加预付账款的小控件的实现原理？

![[1-odoo14-737-07895292.png]]

【实现原理】

1.  整个预收预付的添加的区域是一个计算型字段，该字段是一个定制的Widget “payment”

2.  payment 的实现代码参考：ODOO14\source\addons\account\static\src\js\account_payment_field.js ， ODOO14\source\addons\account\static\src\xml\account_payment.xml

3.  XML视图上的实现代码：ODOO14\source\addons\account\views\account_move_views.xml ：

![[1-odoo14-737-55576e17.png]]

    4. py中计算方法参考ODOO14\source\addons\account\models\account_move.py   def _compute_payments_widget_to_reconcile_info(self):

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
