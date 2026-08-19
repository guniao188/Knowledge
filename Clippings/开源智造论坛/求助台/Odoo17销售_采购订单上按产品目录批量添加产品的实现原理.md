---
title: "Odoo17销售/采购订单上按产品目录批量添加产品的实现原理"
source: "http://www.thinkltd.cn/forum/1/odoo17-3933"
forum: "求助台"
author: "肖相扶"
published: 2024-05-24
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo17销售/采购订单上按产品目录批量添加产品的实现原理

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-05-24
> <http://www.thinkltd.cn/forum/1/odoo17-3933>

【关键技术点】

1.  设置看板视图的属性 js_class="product_kanban_catalog"，参见代码文件 OSCGODOO17\source\addons\product\views\product_views.xml中视图product_view_kanban_catalog 的定义
2.  product_kanban_catalog的实现中，定义鼠标Click事件（添加订单明细行），代码参见  OSCGODOO17\source\addons\product\static\src\product_catalog\kanban_record.js
3.  添加订单明细行的视图界面，调用组件orderLineComponent，参见代码文件OSCGODOO17\source\addons\product\static\src\product_catalog\kanban_record.xml
4.  组件orderLineComponent的实现代码，视图参见代码文件 OSCGODOO17\source\addons\product\static\src\product_catalog\order_line\order_line.xml，视图数据来源调用后端方法 /product/catalog/update_order_line_info ，参见代码文件OSCGODOO17\source\addons\product\static\src\product_catalog\kanban_record.js
5.   方法 /product/catalog/update_order_line_info的实现中，对应代码文件 OSCGODOO17\source\addons\product\controllers\catalog.py中的方法 product_catalog_update_order_line_info。该方法再调用订单的方法 _update_order_line_info ，参见代码文件  OSCGODOO17\source\addons\sale\models\sale_order.py
6.  如果需要输入产品数量之外，再增加产品批次输入，需要两处修改，一是组件 orderLineComponent的视图上添加批次输入框（下拉选择框），二是组件数据源方法（ _update_order_line_info ）中，增加该产品的所有批次供下拉选择。

![[1-odoo17-3933-ce70a37c.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
