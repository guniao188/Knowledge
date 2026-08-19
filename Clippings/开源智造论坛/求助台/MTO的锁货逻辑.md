---
title: "MTO的锁货逻辑"
source: "http://www.thinkltd.cn/forum/1/mto-640"
forum: "求助台"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# MTO的锁货逻辑

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/mto-640>

MTO仓库锁货的逻辑，它是通过哪个字段标识去锁到采购入的那一笔入库单的货的，手动创建的PO就是不会被锁到，我想调配一下，能让后来手动入库的，被锁到货，所以想搞清楚这里MTO的锁货逻辑。

我将手动创建的PO上group_id补货组也变成和SO单号一致，但仍然缺失的部分，无法正常锁货，所以很奇怪，究竟是哪个字段有标识或判断

## 补充/答案 1

答案参考：

[/forum/1/question/mto-365](http://www.thinkltd.cn/forum/1/question/mto-365)

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
