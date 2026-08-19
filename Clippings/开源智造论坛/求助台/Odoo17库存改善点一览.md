---
title: "Odoo17库存改善点一览"
source: "http://www.thinkltd.cn/forum/1/odoo17-3812"
forum: "求助台"
author: "肖相扶"
published: 2024-04-10
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo17库存改善点一览

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-04-10
> <http://www.thinkltd.cn/forum/1/odoo17-3812>

返回  [Odoo17改善点列表](http://www.thinkltd.cn/forum/1/odoo17-3808)

1.  自动划分波次
    作业类型上增加了自动划分波次相关设定。

![[1-odoo17-3812-20e73e21.png]]

2.  先进先出（FIFO）产品成本价格计算方法
    The cost of FIFO products is now set to the average price of the remaining quantities. FIFO出库成本价格的计算方法改成了：本次出库锁货的所有Quants的锁货后的剩余价值/剩余数量，得到出库成本。以前版本的算法是，本次出库所锁到的最后一个Quants的锁货前的剩余价值/剩余数量，得到出库成本。
3.  库存自由保留
    Picking上直接编辑数量、批次等，系统直接保留（锁货）。以前版本是，一个需求数量，一个保留数量，新版本只有一个数量，直接编辑。新版本也去掉了“取消保留”功能，直接编辑，编辑保存时候，系统自动保留符合条件的Quants及数量。 

![[1-odoo17-3812-ccf05628.png]]

4.  库存预测报告上的保留
    库存预测报告上保留、取消保留时候，只保留/取消保留该Picking上的该产品，而不是整个Picking单。
5.  Incoterms
    Incoterm and location are now included on the delivery slip.
6.  批次/序列号显示
    批次/序列号列表视图上，增加了在手数量的显示。 

![[1-odoo17-3812-0ab9c121.png]]

7.  批次/序列码、到期日期、数量批量录入
    入库单上，序列码自动产生，批次、数量、到期日期拷贝粘贴批量录入。

![[1-odoo17-3812-1f9fa861.png]]

8.  MTO/MTS
    'Make to Order' (MTO) 被打断后，自动改成MTS，以使流程可以往下走。实测结果：1) MTO产品，做一个SO，数量10个，确认SO，系统自动产生一个PO，数量也是10个。2) 此时，修改PO的数量为3个，确认PO，系统自动修改SO的发货单的数量为3，此时发货单的状态是“等待另一个操作” 。3) 验证收货单，此时发货单的状态变为“就绪”，验证发货单，创建欠单。4）此时，在17.0中，发货单产生的欠单，自动改成了MTS，状态是“等待”，而在16.0中，欠单还是MTO，状态是“等待另一个操作”，这使得整个发货流程走不下去（必须通过服务器动作之类的改单成MTS才能走下去）。
9.  新增下架策略: least packages
    新增下架策略"Least Packages"：查找数量大于待下架数量的，数量最小的包裹，优先下架。如果待下架数量大于单个包裹的数量，则先下架数量最多的包裹，剩余数量继续按此规则查找包裹。
10. 作业菜单
    改进了作业菜单，老版本的一个菜单“传输”拆成了“收货单”、“发货单”、“调拨单”三个菜单。
11. 产品包装规格显示在单据上
    SO、PO、Picking单据上都显示产品包装规格，及包数。填写包数，自动调整产品数量，填写产品数量，自动调整包数。

![[1-odoo17-3812-dcc4117d.png]]

12. 仓库单据作业时候自动打印
    作业类型上可以定义，该类型的作业单，哪些作业操作自动打印什么标签/单据。

![[1-odoo17-3812-4658a6cc.png]]

13. 产品数量更新
    产品表单页面，更新数量按钮，直接跳转到库存盘点页面，快速更新产品数量。
14. 实时库存计价
    会计设置界面增加了全局库存计价相关设置（企业版模块stock_accountant）。新增了“生产成本”科目配置（企业版模块mrp_accountant），用于生产成本核算。 

![[1-odoo17-3812-78f545d8.png]]

15. Reception report barcodes
    Reception report now includes a barcode for the next step (ex., from pick to pack) to allow quick movements through a workflow with a barcode scanner.
16. 补货功能改善
    补货界面，增加了供应商字段，可以指定供货的供应商。增加了批量操作功能：选择多个产品，一键补货到最大数量。
17. Reserve / unreserve button
    The forecast report reserve / unreserve button now supports multistep routes.
18. Picking改善
    去掉了计划调拨和立即调拨，统一成调拨。
19. Shipping-based routing
    Specify shipping method on routes.
20. 库龄报表
    库存模块增加了库龄报表。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
