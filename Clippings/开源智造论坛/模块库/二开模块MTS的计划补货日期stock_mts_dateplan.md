---
title: "二开模块MTS的计划补货日期stock_mts_dateplan"
source: "http://www.thinkltd.cn/forum/2/mtsstock-mts-dateplan-3098"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开模块MTS的计划补货日期stock_mts_dateplan

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/mtsstock-mts-dateplan-3098>

模块链接：OSCG_SVN\odoo_ecommerce\12.0SRC\stock_mts_dateplan

【问题背景】

生产型企业，原则上半成品都是需要的时候再生产，但半成品生产有个经济批量，例如，生产A产品120件需要半成品B 120件，但B的经济生产批量是100，B实际会下单生产200件（经济批量的倍数）。

这个经济批量的问题，用Odoo系统的MTO处理半成品生产，可以满足“需要时再生产”的需求，但满足不了“经济批量”问题。如果用MTS，设置最小最大数量都为 0 的订货规则，订货规则上有“倍数”字段，可以满足经济批量问题，又一定程度上满足需要时候再生产的需求。但又有新问题，订货规则发起补货时候，它总是以当天日期计算需货日期。例如，今天是6月1日，安排了A产品的生产单MO，计划开始日期是6月10日，那么，A产品的原料的需求日期应该是6月10日，而不是今天（运行调度的日期）。

本模块修改stock.warehouse.orderpoint的方法_get_date_planned，首先判断最小最大数量都为0的话，取最近的要货的Stock Move的date日期作为计划要货日期。如果最小最大数量不为0的话，按系统原有逻辑计算计划补货日期。

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
