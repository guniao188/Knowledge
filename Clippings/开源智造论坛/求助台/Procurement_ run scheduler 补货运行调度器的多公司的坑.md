---
title: "Procurement: run scheduler 补货运行调度器的多公司的坑"
source: "http://www.thinkltd.cn/forum/1/procurement-run-scheduler-639"
forum: "求助台"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Procurement: run scheduler 补货运行调度器的多公司的坑

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/procurement-run-scheduler-639>

Procurement: run scheduler 补货运行调度器的多公司的坑

当遇到多公司时，同时不同的产品在不同的抬头下会创建不同的安全库存规则，同时采购订单的编码序号也有按多公司进行不同的序号编码，会出现一种情况，系统自动跑出的单据，会生成的PO的单号会串号到其他抬头，不知道为什么？

请调查一下是不是源码有定死固定抬头么？应当不可能啊。

当时测试时，有将运行调度器的【计划任务】，上绑定的user更改成受多公司限制的具体的用户账号，而非默认的admin账号，当时测试看起来用用户账号，运行调度器跑出来的单据是正常的。但也仍会出现时不时串号，不知道为何？

![[1-procurement-run-scheduler-639-31a2575d.png]]

![[1-procurement-run-scheduler-639-a2674e20.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
