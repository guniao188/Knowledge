---
title: "Odoo17库存成本内部实现原理"
source: "http://www.thinkltd.cn/forum/5/odoo17-3851"
forum: "专家库"
author: "周鸿飞"
published: 2024-01-02
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/专家库
---

# Odoo17库存成本内部实现原理

> [!info] 来源
> 开源智造论坛 · 专家库 | 作者:周鸿飞 | 2024-01-02
> <http://www.thinkltd.cn/forum/5/odoo17-3851>

【问题列表】
说明stock.valuation.layer库存计价界面上，各个字段的含义。不同计价方法（标准法、移动加权平均法、先进先出法）情况下，分别说明单价(unit_cost)、剩余价值(remaining_value)的计算逻辑

【业务实现示例】
Odoo不支持个别计价法。个别计价法的一种实现方式是：结合批次管理，出库时候指定批次，系统计算出库成本时候，取该批次的成本（而不是按先进先出或移动平均取成本）。如何在Odoo上二开实现此功能。参考  [基于批次的个别计价方法](http://www.thinkltd.cn/forum/2/3569)

---

相关:[[Clippings/开源智造论坛/专家库/00-专家库索引.md|← 专家库索引]]
