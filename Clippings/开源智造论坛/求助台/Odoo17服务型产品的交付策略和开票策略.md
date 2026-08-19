---
title: "Odoo17服务型产品的交付策略和开票策略"
source: "http://www.thinkltd.cn/forum/1/odoo17-3986"
forum: "求助台"
author: "肖相扶"
published: 2024-10-16
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo17服务型产品的交付策略和开票策略

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-10-16
> <http://www.thinkltd.cn/forum/1/odoo17-3986>

老版本参考： [Odoo 13服务型产品的开票策略和交付策略](http://www.thinkltd.cn/forum/1/odoo-13-476)

【功能解说】

1.  开票策略Prepaid/Fixed Price：SO确认后即可创建发票，数量为订单数量
2.  开票策略Based on Timesheets：SO确认后，如果存在关联了该SO明细行的timesheet(模型account.analytic.line的so_line字段)，交付数量取那些timesheet上的数量，可以按此数量创建发票。
3.  开票策略Based on Milestones： SO确认后，系统自动创建一个项目里程牌(模型 project.milestone)，项目任务可以关联此里程碑。当此里程碑标记为完成时候，系统会把该SO明细行写入关联了此里程碑的Task对应的Timesheet的so_line字段，SO明细行的交付数量计算逻辑是，SO明细行数量乘以里程碑上填写的完成百分比(模型project.milestone的字段quantity_percentage)。
4.  开票策略Based on Delivered Quantity(Manual)：SO确认后，交付数量一列，系统不从Timesheet取值，而是用户手工填写。系统按此数量创建发票。
5.  交付策略 Task：此选项的话，产品上要指定关联Project。SO确认时候，系统为该明细行自动创建一个关联Project的Task，该Task自动关联本明细行。Task上填写Timesheet时候，此明细行业自动带入到Timesheet上。本明细行的交付数量取自关联的Timesheet的工时数量。
6.  交付策略 Project & Task：SO确认时候，系统自动为SO创建一个Project，同时为明细行创建一个Task。
7.  交付策略 Project：SO确认时候，系统自动为SO创建一个Project。
8.  如果安装了应用Plan，服务型产品上多出一个配置项“Plan Services”。勾选它，设置计划角色(plan.role)，如此，SO确认后，系统显示该SO有XX小时待计划。在Plan模块中安排计划(planning.slot)，计划关联该SO Line，SO上显示计划了多少小时，剩下多少小时待计划。

【功能截图】

![[1-odoo17-3986-8ee7f7b0.png]]

![[1-odoo17-3986-d5dfdd2e.png]]

![[1-odoo17-3986-9326a053.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
