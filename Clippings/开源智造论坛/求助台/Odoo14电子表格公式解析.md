---
title: "Odoo14电子表格公式解析"
source: "http://www.thinkltd.cn/forum/1/odoo14-715"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo14电子表格公式解析

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo14-715>

如下图，=PIVOT("1","expected_revenue","create_date:month","11/2020","stage_id","4")   表示，汇总透视表 1 中，create_date月份 = 11/2020, 且 stage_id阶段 = 4 的数据的expected_revenue字段的和 。即，该公式的第二个参数是 需要汇总的字段，后面各个参数则是数据筛选条件。

![[1-odoo14-715-94406ba8.png]]

【】

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
