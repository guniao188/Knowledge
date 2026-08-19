---
title: "Odoo13的路线规则上新增了Scheduling功能"
source: "http://www.thinkltd.cn/forum/1/odoo13scheduling-630"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo13的路线规则上新增了Scheduling功能

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo13scheduling-630>

【问题】

如下截图，Odoo 13的路线规则上，新增的Scheduling字段有何功能？

![[1-odoo13scheduling-630-8e066076.png]]

经调查，Schdduling设置，应用于MTO情况，前后串联的Stock Move的Expected Date的传播。

- Alert if Delay：如果勾选，则MTO的前一个Stock Move如果实际完成日期延迟（迟于计划日期），则前一个Stock Move Done的时候，系统自动在MTO的下游Stock Move上产生一个异常提醒（提醒前一个StockMove延迟了，本Stock Move也要延迟）。

- Propagate Rescheduling：如果勾选，则MTO的前一个Stock Move如果实际完成日期延迟（迟于计划日期），则前一个Stock Move Done的时候，系统自动修改MTO的下游Stock Move的计划日期（Expected Date）。而不是像“Alert if Delay“那样仅仅是提醒。

  截图说明：

## 补充/答案 1

Alert if Delay：

![[1-odoo13scheduling-630-92abae4c.png]]

Propagate Rescheduling：

![[1-odoo13scheduling-630-74c5a2a2.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
