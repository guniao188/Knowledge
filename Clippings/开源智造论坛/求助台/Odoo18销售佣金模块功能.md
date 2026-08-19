---
title: "Odoo18销售佣金模块功能"
source: "http://www.thinkltd.cn/forum/1/odoo18-3982"
forum: "求助台"
author: "肖相扶"
published: 2024-10-09
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo18销售佣金模块功能

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-10-09
> <http://www.thinkltd.cn/forum/1/odoo18-3982>

【模块功能】

1.  佣金模式：提成模式(Achievement) 或者目标达成模式(Targets)。提成模式即按销售额的一定比例提成，目标达成模式是，设定月度、季度或者年度销售目标，达成目标的百分之多少，对应奖励多少钱。
2.  佣金对象：销售业务员，或者销售团队。
3.  销售额计算基准：销售金额（SO确认即计算佣金），开票金额（SO对应的结算单确认时候计算佣金），销售数量，开票数量，销售利润。
4.  佣金计划(Commission Plans)：设定佣金计算规则
5.  销售业绩(Achievements)：销售业绩达成时候，系统自动产生的佣金业绩明细(sale.commission.achievement.report)
6.  佣金明细(Commissions)：销售业绩达成时候，系统基于佣金计划中设定的佣金计算规则，自动产生的佣金明细( sale.commission.report) 。
7.  佣金调整(Adjustments)：有些单子，如果没有在系统做SO，或者没有在系统做结算单，可以手工录入销售业绩( sale.commission.achievement)，系统也会自动产生佣金明细。

【功能截图】

下面截图的佣金计划，按目标达成率计算佣金，按季度计算佣金，按业务员计算佣金。目标100%达成佣金(On Target Commission，OTC)是1500元。目标达成150%，佣金是2个OTC，即3000元。

![[1-odoo18-3982-92725ea4.png]]

下面截图，设定销售达成基准是发票确认时候，按金额计算目标达成率。系统中可以针对不同的产品，不同的产品分类，设定不同的销售提成（按提成计算佣金的模式）。

![[1-odoo18-3982-c3c0af65.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
