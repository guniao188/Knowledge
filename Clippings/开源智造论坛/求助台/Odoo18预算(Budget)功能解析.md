---
title: "Odoo18预算(Budget)功能解析"
source: "http://www.thinkltd.cn/forum/1/odoo18-budget-3985"
forum: "求助台"
author: "肖相扶"
published: 2025-07-08
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo18预算(Budget)功能解析

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2025-07-08
> <http://www.thinkltd.cn/forum/1/odoo18-budget-3985>

【预算功能】

1.  Odoo18的预算管理功能，核心有两个模型，一个是预算计划(budget.analytic)，一个是预算明细(budget.line)。
2.  预算明细上的几个核心字段，一个是Project(account_id, many2one到分析科目account.analytic.account)，一个是预算金额(budget_amount), 一个是提交的预算(commited_amount), 一个是达成的预算(achieved_amount)。预算金额是预算计划时候填写的金额。提交的预算是达成的预算 加上 已确认的PO及SO明细，但未开票(未生成分析项目)的金额。达成的预算从分析项目(account.analytic.line)提取金额。
3.  预算分析(budget.analytic)有三种类型(budget_type字段)，一种是费用(Expense)，只提取PO及供应商账单明细的金额，金额显示为正数。一种是收入(Revenue)，只提取SO及客户结算单明细金额，金额显示为正数。一种是收入和费用（Both），同时提取SO、PO、客户结算单及供应商账单的明细金额。PO及供应商结算单金额显示为负数，SO及客户结算单金额显示为正数。因此Both实际上是利润预算，即计划要达成的毛利。
4.  和以前版本相比，预算明细上去掉了会计科目，去掉了期间，因而预算功能简化了很多。

【功能截图】

预算计划：

![[1-odoo18-budget-3985-420cb1e7.png]]

预算明细画面，实施中建议增加预收明细的菜单，显示预算明细列表。

![[1-odoo18-budget-3985-a411f046.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
