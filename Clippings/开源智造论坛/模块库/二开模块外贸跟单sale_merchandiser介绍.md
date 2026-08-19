---
title: "二开模块外贸跟单sale_merchandiser介绍"
source: "http://www.thinkltd.cn/forum/2/sale-merchandiser-2496"
forum: "模块库"
author: "肖相扶"
published: 2023-06-26
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开模块外贸跟单sale_merchandiser介绍

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2023-06-26
> <http://www.thinkltd.cn/forum/2/sale-merchandiser-2496>

模块存放位置：OSCG_SVN\odoo_ecommerce\11.0SRC\进销存\sale_merchandiser

13.0将此模块功能拆分为两个模块：[/forum/2/question/sale-merchandiser-3309](http://www.thinkltd.cn/forum/2/question/sale-merchandiser-3309)

[/forum/2/question/sosale-supplier-3303](http://www.thinkltd.cn/forum/2/question/sosale-supplier-3303)

【MTO订单处理】
    * 应用场景：小型贸易公司，原则上没有库存，都是MTO订单，且经常有新产品销售（第一次销售的产品）。此类产品在给客人SO的同时，需要临时找供应商询价。此种场景，SO上需要有供应商询价功能。
    * 解决方案：SO明细行上增加供应商字段、采购说明字段、采购单价字段，默认值取产品上的第一个供应商，及采购说明。SO确认时候，如果是手填的新供应商，自动更新产品上的供应商及采购说明。如此，系统后续MTO运算产品PO时候，自动应用SO明细行上的供应商、采购说明及采购单价。

【外贸跟单】
    * SO表单右上角增加按钮“采购”，点击显示 源单据 为该SO的PO列表
    * 销售订单SO上增加字段： PO日期(po_date)，PL日期(pl_date)，CI日期(ci_date)，到款日期(payment_date)
```python
      PO日期(po_date)：源单据为该SO的PO的确认日期，取最近的PO日期
      PL日期(pl_date)：源单据为该SO的PO的入库单完成日期，取最近的入库单日期
      CI日期(ci_date)：该SO的Invoice的确认日期，取最近的Invoice日期
      到款日期(payment_date)：该SO的Invoice的收款日期，取最近的收款日期
```

    * 销售模块增加菜单“销售跟单”，显示销售订单SO及其PO的关键节点日期
    * 销售表单增加出发港、到达港字段，销售配置中增加港口表单配置

## 补充/答案 1

sale_supplier模块这里我代码里发现了一个问题，不知道是不是我哪里设置的有问题：

![[2-sale-merchandiser-2496-922657a3.png]]

![[2-sale-merchandiser-2496-8f667260.png]]

![[2-sale-merchandiser-2496-106b4669.png]]

![[2-sale-merchandiser-2496-88e5cb15.png]]

![[2-sale-merchandiser-2496-98cbe5cc.png]]

是不是我哪里配置错了，还是代码有bug呢？需要传入quality这个参数？？

## 补充/答案 2

选择产品时候，数量总是为1，系统只能带出最小数量为0 的供应商。此模块没考虑最小数量，如果设置了最小数量，带不出供应商。如果有需要根据销售数量带出合适的供应商，应该在SO Line的 Quantity字段的onchang 方法里面，根据数量去找供应商，_select_seller 方法有数量参数。

## 补充/答案 3

【功能截图】

- l  销售报价成功，订单成交，进入销售跟单阶段。销售跟单阶段，需要协调供应商备货、发货，协调客户报关、清关、安排付款。期间还可能会发生客户改单情况

- l  销售跟单界面，列示每个SO的关键时间节点：PO是否已经确认，确认日期，供应商是否已经发货，发货日期，是否已经开CI，开CI日期，客户是否已经付款，付款日期

- l  销售订单界面，以SO为中心，一键跳转到关联单据：发货单、CI、采购单

- l  PO Date：采购单确认的时间，如果有多个采购单，取时间最近的那个采购单日期

- l  PL Date：采购发货时间，即PO对应的Picking的验证日期。如果有多个发货单（一个SO可能有多个PO，一个PO可能有多个Picking），取时间最近的那个Picking日期

- l  CI Date：销售订单SO的Invoice （CI，Commercial Invoice）的时间，如果有多个CI，取时间最大的那个日期

- l  Payment Date：收到客户款项的日期，如果该SO有多个CI，对应的多笔回款，取时间最近的那个回款日期

跟单状态更新：

以销售单SO为中心，一键跳转到关联单据。

## 补充/答案 4

港口城市的界面默认值excel导入模板，以及sale_merchandiser这个模块的中文翻译

请参考SVN目录：F:\SVN\odoo_ecommerce\06.Customization\魔数\addons

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
