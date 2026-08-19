---
title: "Odoo17 POS订单离线处理机制"
source: "http://www.thinkltd.cn/forum/1/odoo17-pos-3910"
forum: "求助台"
author: "肖相扶"
published: 2024-03-29
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo17 POS订单离线处理机制

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-03-29
> <http://www.thinkltd.cn/forum/1/odoo17-pos-3910>

Odoo17 POS订单离线处理机制：

1.  POS界面上添加零售单时候，系统先把订单添加到浏览器的本地存储(localStorage, 参考 [Window localStorage 属性 | 菜鸟教程 (runoob.com)](https://www.runoob.com/jsref/prop-win-localstorage.html))，再试图将localStorage中的订单都上传到服务器。代码参考 文件 OSCGODOO17\source\addons\point_of_sale\static\src\app\store\pos_store.js，方法 push_single_order
2.  localStorage订单上传到服务器的逻辑，调用pos.order模型的方法 create_from_ui 将本地存储的订单上传服务器，而后将订单的服务器端id更新到本地订单。如果上传成功，从 localStorage 删除本地订单。代码参考 OSCGODOO17\source\addons\point_of_sale\static\src\app\store\pos_store.js 方法 _save_to_server 和 _flush_orders 。
3.  POS界面关闭时候，POS界面打开时候，每次订单付款后，系统都会试图将本地订单上传到服务器。或者鼠标点击POS界面右上角的同步图标时候，系统也会试图同步本地订单到服务器。同步成功后，从本地删除该订单。如果网络不好，同步失败，订单会一直存储在本地localStorage，下次再次打开POS界面时候，系统会试图再同步。
4.  从代码逻辑上看，系统的离线机制很安全，几乎不存在订单丢失的可能。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
