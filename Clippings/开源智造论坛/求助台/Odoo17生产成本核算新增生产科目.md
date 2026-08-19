---
title: "Odoo17生产成本核算新增生产科目"
source: "http://www.thinkltd.cn/forum/1/odoo17-3929"
forum: "求助台"
author: "肖相扶"
published: 2024-07-20
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo17生产成本核算新增生产科目

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-07-20
> <http://www.thinkltd.cn/forum/1/odoo17-3929>

【Odoo17新增生产科目】

1.  Odoo17安装生产会计模块(mrp_account)后，产品分类上增加了生产科目配置字段property_stock_account_production_cost_id。

![[1-odoo17-3929-c5060fd2.png]]

2.  生产领料(目标库位是Production类型库位)时候，借方科目，系统科目查找顺序是：先取生产库位（虚拟库位）上的入库科目，如果没有则取产品分类上的 生产科目，如果没有最后取产品分类上的出库科目配置。
3.  生产入库(源库位是Production类型库位)时候，贷方科目，系统科目查找顺序是：先取生产库位（虚拟库位）上的出库科目，如果没有则取产品分类上的 生产科目，如果没有最后取产品分类上的入库科目配置。
4.  实际配置时候，原材料的生产科目应配置“制造费用”，出库科目可以配“其他业务成本”（对应原材料销售出库业务）， 产成品的生产科目应配置“生产成本”，入库科目可以配置“主营业务成本”（对应销售退库业务）。期末应该根据制造费用科目的余额，手工做一笔会计凭证借记 生产成本，贷记 制造费用，清空制造费用科目。如此，期末生产成本科目的余额应为在产品，或者原料以外的制造费用的差异调整。

【Odoo17生产成本计算逻辑】

1.  产成品的成本计算逻辑（平均成本计价或先进先出成本计价时候）：MO上的原料成本 + MO的额外成本（字段extra_cost） + 工单WO的制造费用。计算代码参见 OSCGODOO17\source\addons\mrp_account\models\mrp_production.py 方法 _cal_price
2.  WO的制造费用的计算逻辑是：工时消耗 * 工作中心的成本价格(costs_hour字段)，如果安装了模块enterprise\mrp_workorder，WO的制造费用还会加上员工费用，员工费用计算逻辑是：工时消耗 * 员工上的成本价格(员工上的字段hourly_cost)。计算代码参见 OSCGODOO17\source\enterprise\mrp_workorder\models\mrp_workorder.py  方法 _cal_cost


## 附件

- [[附件/forum/1-odoo17-3929-工作中心中成本算法说明.doc|工作中心中成本算法说明.doc]] (606 KB)

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
