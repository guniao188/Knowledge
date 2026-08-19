---
title: "Odoo负数出库冲平机制及Bug"
source: "http://www.thinkltd.cn/forum/1/odoobug-288"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo负数出库冲平机制及Bug

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoobug-288>

Odoo 11.0及12.0中，负数出库的冲平机制：

1.  如果负数出库，该出库Stock Move的剩余数量字段及剩余价值字段为负数（有库存情况，即正常出库的话，其值为 0）。

2.  “运行调度”的时候，系统会检查所有的 剩余数量字段及剩余价值字段为负数 的Stock Move，用其后面的入库Stock Move（剩余数量字段及剩余价值字段为正数），抵冲该负数。抵冲后，负数变0，正数（入库）剩余价值和剩余数量变少。

3.  负数冲平的代码参考 addons\stock_account\models\stock.py  方法  _run_scheduler_tasks  ，该方法在“运行调度”时候被调用。

但系统负数冲平有个Bug，参见：  该Bug 2018年8月份提出，Odoo却迟迟未修复。该Bug导致负数冲平不生效。

## 补充/答案 1

模块 OSCG_SVN\odoo_ecommerce\12.0SRC\存货核算\stock_cost 修复了负数冲平的Bug 。

负数冲平图示：

## 补充/答案 2

那么历史的错误数据修复仍然还是需要用工具才能处理，对吧？

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
