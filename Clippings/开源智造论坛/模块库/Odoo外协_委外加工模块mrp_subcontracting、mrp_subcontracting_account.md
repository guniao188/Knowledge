---
title: "Odoo外协/委外加工模块mrp_subcontracting、mrp_subcontracting_account"
source: "http://www.thinkltd.cn/forum/2/odoo-mrp-subcontractingmrp-subcontracting-account-3183"
forum: "模块库"
author: "肖相扶"
published: 2024-06-18
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo外协/委外加工模块mrp_subcontracting、mrp_subcontracting_account

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-06-18
> <http://www.thinkltd.cn/forum/2/odoo-mrp-subcontractingmrp-subcontracting-account-3183>

【模块功能】

1.  增加一种新的采购形式：外协采购，其原理是，例如，部件A是外协产品，则需要为“部件A”配置外协供应商，配置补货方式为“Buy”，配置“外协库位”，配置外协BoM。如此，部件A的采购入库Stock Move，Confirm时候，系统判断是外协采购，且有外协BoM，系统自动将“源库位”设置为外协供应商的“外协库位”（而不是供应商库位），并且自动创建外协的生产单MO。采购入库“验证时候”，系统自动完成关联的外协MO。

2.  Odoo16, 17中，外协逻辑原理：外协PO确认，生成采购入库单，采购入库的Stock Move Confirm时候，系统判断是外协的入库，调用Picking的方法 _subcontracted_produce （文件 mrp_subcontracting\models\stock_picking.py），该方法中创建外协MO，并将外协MO的完工入库Stock Move的目标move_ids(字段 move_dest_ids)设置为外协采购入库的Stock Move。

3.  模块mrp_subcontracting_account 将外协采购的成本价格自动设置到外协MO的 extra_cost ，计算成品成本价格时候（模块mrp_account），系统基于 原料成本（MO上的原料Stock Move）、加工成本（MO上的工作中心和工艺路线计算得到）、额外成本（extra_cost ），累加三个成本作为产成品成本。

【模块配置】

![[2-odoo-mrp-subcontractingmrp-subcontracting-account-3183-ca8c89f8.png]]

![[2-odoo-mrp-subcontractingmrp-subcontracting-account-3183-004d80e6.png]]

注意：系统默认是归档了外协作业类型，需要激活该作业类型，才能显示外协生产单。

![[2-odoo-mrp-subcontractingmrp-subcontracting-account-3183-1d429588.png]]

![[2-odoo-mrp-subcontractingmrp-subcontracting-account-3183-f3eb7b31.png]]

## 补充/答案 1

V13的委外加工，这个值是用于什么情况下呢？临时替换成委外么?

![[2-odoo-mrp-subcontractingmrp-subcontracting-account-3183-1b53e1e9.png]]

## 补充/答案 2

Odoo 13的工作中心上，新增了可选工作中心 字段。该字段目前系统的用法如下：

1.  MO上点击“计划” 按钮，系统基于工艺路线上的工序生成工单（Work Order）时候，系统比较该工序上的工作中心、及可选工作中心，看看用哪个工作中心可以最快完成工单任务，哪个最快就选择哪个工作中心。

2.  一个应用场景是，例如，一样的机台有三个，把其中一个设置为工作中心，另外两个设置为可选工作中心。如果第一个工作中心不可用（处于维修中），或被占用了，系统自动给工单安排另外两个工作中心。

3.  在工单WO上，还可以手工修改工作中心

## 补充/答案 3

测试发现有个小bug

stock move的单价不对，但会计凭证是对的

![[2-odoo-mrp-subcontractingmrp-subcontracting-account-3183-f48f8cbe.png]]

![[2-odoo-mrp-subcontractingmrp-subcontracting-account-3183-c5313fb5.png]]

凭证是按正确的计算的，6元。

## 补充/答案 4

官方学习资料：https://www.odoo.com/documentation/user/13.0/manufacturing/management/subcontracting.html

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
