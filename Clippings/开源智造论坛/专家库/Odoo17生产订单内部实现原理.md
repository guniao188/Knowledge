---
title: "Odoo17生产订单内部实现原理"
source: "http://www.thinkltd.cn/forum/5/odoo17-3854"
forum: "专家库"
author: "施叶寒"
published: 2024-03-18
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/专家库
---

# Odoo17生产订单内部实现原理

> [!info] 来源
> 开源智造论坛 · 专家库 | 作者:施叶寒 | 2024-03-18
> <http://www.thinkltd.cn/forum/5/odoo17-3854>

【问题列表】

1.  生产订单（mrp.production）BoM(bom_id字段)改变时候，系统自动创建组件明细行(move_raw_ids字段)、产成品明细行(move_finished_ids)。请解释说明创建组件明细、产成品明细的内部逻辑。注意包括套件BoM情况的内部逻辑。
2.  生产订单确认时候，系统自动创建子生产订单(有子BoM且MTO的情况下)，组件领料单(两步领料的情况下)。请解释说明系统内部实现的逻辑原理。
3.  请说明下面截图中，Status、Receipt、MO Cost、Real Cost三列的含义

![[5-odoo17-3854-22bb2889.png]]

【业务实现示例】

1.  升级二开生产订单拆单功能模块，参考 [生产订单MO分拆模块mrp_production_split](http://www.thinkltd.cn/forum/2/momrp-production-split-3480)
2.  请说明主MO和子MO的计划日期(date_start字段)，原料采购PO单明细行的计划日期(date_planned字段)，三者之间的逻辑关系，及内部计算原理。

---

相关:[[Clippings/开源智造论坛/专家库/00-专家库索引.md|← 专家库索引]]
