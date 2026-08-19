---
title: "OCA采购订单PO异常检测purchase_exception"
source: "http://www.thinkltd.cn/forum/2/ocapopurchase-exception-2609"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA采购订单PO异常检测purchase_exception

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocapopurchase-exception-2609>

模块链接：

 依赖模块：[/forum/2/question/ocabase-exception-2607](http://www.thinkltd.cn/forum/2/question/ocabase-exception-2607)

purchase.order继承异常基类base.exception，PO confirm，PO明细行修改等情况，调用异常检测方法。检测到异常，系统报错，中断操作。

This module allows you attach several customizable exceptions to your purchase order in a way that you can filter orders by exceptions type and fix them.

This is especially useful in an scenario for mass purchases order import, because it's likely some orders have errors when you import them (like product not found in Odoo, wrong line format etc.)


## 原帖外链配图

![[2-ocapopurchase-exception-2609-x194038c2.png]]
<small>原始地址: /web/image/898/snipaste_20190120_130448.png?access_token=d61a1b33-4767-4351-9dda-c9e287240293</small>

![[2-ocapopurchase-exception-2609-x194038c2.png]]
<small>原始地址: /web/image/900/snipaste_20190120_130817.png?access_token=1fd7a79b-71c0-4dd4-aff7-928c90eeb9b7</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
