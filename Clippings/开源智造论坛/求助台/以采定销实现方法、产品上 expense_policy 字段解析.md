---
title: "以采定销实现方法、产品上 expense_policy 字段解析"
source: "http://www.thinkltd.cn/forum/1/expense-policy-386"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 以采定销实现方法、产品上 expense_policy 字段解析

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/expense-policy-386>

当开启分析会计功能后，产品表单上有一个字段 Re-Invoice Policy ( expense_pilicy ) ，经调查，该字段用法如下：

1.  字段选项有：no、cost、sales_price 三个选项，如果是后面两个选项，且产品上勾选了 "can_be_expensed" 字段，则SO上含有该产品时候，系统自动以 SO单号为名创建 分析科目。

2.  创建SO单号的分析科目的分析分录( account.analytic.line )时候，系统自动将分析分录上的产品、数量、单价添加到SO上，分析分录的数量对应到SO明细行的“已交货数量”（订货数量为0）。添加到SO时候，如果 expense_pilicy 配置的是cost，则销售单价直接取分析分录的价格，如果配置的是 sales_price ，则取自产品的销售价格。

3.  一个应用场景是，为某客户代采购一批货物。先创建一个空的SO （明细行只有一个勾选了 "can_be_expensed" ，填写了  expense_pilicy 的 服务产品，订购数量为 0），确认SO自动创建SO单号为名的分析科目。之后手工创建采购订单（可以有多个，供应商可以不同），采购订单明细行上的分析科目填写 SO对应的分析科目。如此，采购订单确认、收货、创建供应商账单、确认账单。系统自动创建分析分录，同时将采购产品、数量、价格自动追加到SO上。

4.  另外一个应用场景是，为某客户提供服务，一开始并不知道有多少服务量。创建一个空SO，之后服务人员提供服务，并填写Timesheet，或者提交费用报销单。Timesheet及报销单上都填写 SO对应的分析科目。如此，系统自动将服务量和报销费用追加到SO明细行上。

![[1-expense-policy-386-669862d7.png]]

![[1-expense-policy-386-b0002837.png]]

![[1-expense-policy-386-2cc9b4fb.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
