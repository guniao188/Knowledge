---
title: "生产单（MO、PO）批量报工结单及工作中心分时段成本设置mrp_production_batch、mrp_workorder_cost"
source: "http://www.thinkltd.cn/forum/2/mopo-mrp-production-batchmrp-workorder-cost-3482"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 生产单（MO、PO）批量报工结单及工作中心分时段成本设置mrp_production_batch、mrp_workorder_cost

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/mopo-mrp-production-batchmrp-workorder-cost-3482>

模块链接：

OSCG_SVN\odoo_ecommerce\14.0SRC\生产制造\mrp_production_batch

OSCG_SVN\odoo_ecommerce\14.0SRC\生产制造\mrp_workorder_cost

【业务背景】

1.  非标设备制造行业、机加工行业，以激光裁切工序为例，一块钢板同时裁切出多个半成品，即多个生产订单（MO）同时完成。此种情况，如果每个MO、WO分别点击完成按钮报工，现实操作上不太可能。

2.  MO批量报工需求：新增一个批量报工单，该报工单上可以添加多个MO，汇总填写每个原料的实际消耗数量，系统自动按计划投料数分摊实际投料数到每个MO，批量完工MO。注意，批量报工不支持部分报工（欠单）。

3.  WO批量报工需求：新增一个批量报工单，该报工单上可以添加多个WO，汇总填写总工时，系统自动按计划工时分摊实际工时到每个WO，批量完工WO。

4.  工时标准成本（模块mrp_workorder_cost）：该模块允许设置分时段的工作中心成本（Odoo本来的功能是，工作中心上设定标准工时成本。但现实是，每个月的标准工时成本可能都不同）。WO批量报工时候，系统自动查找完工时间点的标准工时成本，填写到WO的工时成本字段上，如此，MO报工时候，系统会自动按此成本计算制造费用（参考 [生产工单上增加分析账户(生产成本项目核算) mrp_analytic](http://www.thinkltd.cn/forum/2/question/mrp-analytic-3470)）。

【模块功能】

【功能截图】

![[2-mopo-mrp-production-batchmrp-workorder-cost-3482-047cb9fd.png]]

![[2-mopo-mrp-production-batchmrp-workorder-cost-3482-aaa204a0.png]]

![[2-mopo-mrp-production-batchmrp-workorder-cost-3482-a6b85c09.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
