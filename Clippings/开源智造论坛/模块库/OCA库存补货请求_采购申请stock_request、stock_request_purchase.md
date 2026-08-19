---
title: "OCA库存补货请求/采购申请stock_request、stock_request_purchase"
source: "http://www.thinkltd.cn/forum/2/oca-stock-requeststock-request-purchase-2876"
forum: "模块库"
author: "肖相扶"
published: 2024-05-20
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA库存补货请求/采购申请stock_request、stock_request_purchase

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-05-20
> <http://www.thinkltd.cn/forum/2/oca-stock-requeststock-request-purchase-2876>

模块链接：

OCA已经有12.0升级版本：
13.0版物料申请系列模块参见：  OSCG_SVN\odoo_ecommerce\13.0SRC\物料申请   ，包含模块下述模块：

![[2-oca-stock-requeststock-request-purchase-2876-3d4a5b77.png]]

【模块功能】

1.  销售出库有SO单，确认后系统生成出库Picking单，操作出库。采购入库有PO单，确认后系统生成入库Picking单。其他情况的出入库，系统没有提供物料申请单。常见其他出入库场景有：门店补货申请、研发领料申请、项目采购申请，等等。Stock Request就是解决此类问题的。

2.  stock_request系列模块功能是，指定目标库位进行补货申请。补货申请单确认时候，系统根据物料的补货路线（调拨、采购、制造），自动发起补货单据；

3.  补货申请单上可以指定补货组（group_id）、指定分析科目（analytic account，安装模块stock_request_analytic），指定补货组，促发的PO或者Picking可以按补货组分开单据。分析科目可以实现按项目核算领料成本；

4.  补货申请单可以关联PO（模块stock_request_purchase），申请单和PO单互相跳转。

5.  补货申请单上可以两步审批（模块stock_request_submit）：提交 + 确认，也可以自定义多步审批（模块stock_request_tier_validation）：审批模块 [stock_request_tier_validation](http://www.thinkltd.cn/forum/2/question/ocabase-tier-validationpurchase-tier-validationsale-tier-validation-2588)。

6.  应用场景：分店或分仓申请补货。配置总仓到分仓的补货规则，填写补货单，对分仓补货。系统自动触发总仓到分仓的调拨Picking，根据配置的路线规则，该调拨又可能触发总仓补货（采购 or 制造）。

7.  应用场景：项目领料。创建一个名为“项目”的虚拟库位，项目设计或安装人员填写申请单，补货到虚拟库位“项目”，申请单上填写以项目号为名的分析科目。申请单确认后，系统自动产生项目领料出库的Picking，以及总仓采购/外协/制造的补货单。领料出库的Stock Move上，系统自动记录项目分析科目，便于归集项目领料成本。

【功能截图】
补货申请单

![[2-oca-stock-requeststock-request-purchase-2876-ba48c824.png]]

补货申请审批及领料：

![[2-oca-stock-requeststock-request-purchase-2876-75f66222.png]]

采购申请：

![[2-oca-stock-requeststock-request-purchase-2876-04140050.png]]

模块功能配置：

![[2-oca-stock-requeststock-request-purchase-2876-8e51516d.png]]

## 补充/答案 1

采购集成：

12.0升级修改点：

1.  .py文件中，product.uom 模型名称改为 uom.uom，有下面一处修改：stock_request_purchase\tests\test_stock_request_purchase.py(45):         self.uom_dozen = self.env['product.uom'].create({

2.   .py文件中，procurement.rule 模型名称改为 stock.rule，有下面一处修改：stock_request_purchase\models\procurement_rule.py(8):     _inherit = 'procurement.rule'

## 补充/答案 2

该模块再优化处理：

仓库申请单上，增加【批量选择产品】按钮，弹窗跳到产品列表，可以筛选过滤,实施里面会做一个过滤器【显示预测数量为负数】，方便用户拉取这些产品列表，然后可以批量勾选过滤出来的产品，并加载到申请单的明细行上。

在仓库申请单明细行，增加列显示产品上的【预测数量】作为申请数量填写的参考。

-----------------这个改造的适应业务场景是：缺货的统一走这个库存请购单的功能，这是原来V13版本因没有【补货需求池】才有的需求。

## 补充/答案 3

已优化，相关模块已上传至\oscg_svn\13.0SRC\物料申请\最新版本

## 补充/答案 4

![[2-oca-stock-requeststock-request-purchase-2876-5e8290b8.png]]

V14版的stock_analytic发现svn没有。是不是该这模块V14版改动不再适用呢？


## 原帖外链配图

![[2-oca-stock-requeststock-request-purch-x194038c2.png]]
<small>原始地址: /web/image/1375/snipaste_20190215_190031.png?access_token=79e63da3-cf70-4519-a552-04f5e32c1ae1</small>

![[2-oca-stock-requeststock-request-purch-x194038c2.png]]
<small>原始地址: /web/image/1377/snipaste_20190215_190100.png?access_token=17a2ed4b-0347-4915-ba69-d99ae1719720</small>

![[2-oca-stock-requeststock-request-purch-x194038c2.png]]
<small>原始地址: /web/image/1379/snipaste_20190215_190140.png?access_token=0b49dca6-6a15-4f4d-9346-5d41fa44d1a7</small>

![[2-oca-stock-requeststock-request-purch-x194038c2.png]]
<small>原始地址: /web/image/1369/snipaste_20190215_184602.png?access_token=bf7dcec8-10ef-4ddc-a408-3e0136bd1956</small>

![[2-oca-stock-requeststock-request-purch-x194038c2.png]]
<small>原始地址: /web/image/1371/snipaste_20190215_184705.png?access_token=1d850dac-6f9d-4913-b955-391e02caf132</small>

![[2-oca-stock-requeststock-request-purch-x194038c2.png]]
<small>原始地址: /web/image/1373/snipaste_20190215_185333.png?access_token=22dc2071-9b4f-4ed2-a6e1-dec5d5100af6</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
