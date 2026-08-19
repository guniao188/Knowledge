---
title: "OCA销售佣金的模块使用"
source: "http://www.thinkltd.cn/forum/2/oca-3693"
forum: "模块库"
author: "周鸿飞"
published: 2023-04-19
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA销售佣金的模块使用

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:周鸿飞 | 2023-04-19
> <http://www.thinkltd.cn/forum/2/oca-3693>

OCA的模块 commission 提供了销售的佣金方案：

1、新建agent对应的是 res.partner，在partner设置佣金比例

![[2-oca-3693-0c805df6.png]]

2、在销售订单的明细行上设置可以得到佣金的agent，可设置一个或者多个

![[2-oca-3693-abc909d2.png]]

3、当销售单确认开票后，会在结算单上显示

![[2-oca-3693-7ae811d9.png]]

4、看代码，当销售订单明细行上没有设置agent，并且销售员的partner是agent的时候，会添加销售员为明细行的agent，但是操作并没有实现

![[2-oca-3693-4449f89b.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
