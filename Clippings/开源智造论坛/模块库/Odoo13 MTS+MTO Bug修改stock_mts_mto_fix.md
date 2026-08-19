---
title: "Odoo13 MTS+MTO Bug修改stock_mts_mto_fix"
source: "http://www.thinkltd.cn/forum/2/odoo13-mts-mto-bugstock-mts-mto-fix-3258"
forum: "模块库"
author: "肖相扶"
published: 2022-12-16
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo13 MTS+MTO Bug修改stock_mts_mto_fix

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-16
> <http://www.thinkltd.cn/forum/2/odoo13-mts-mto-bugstock-mts-mto-fix-3258>

模块链接 OSCG_SVN\odoo_ecommerce\13.0SRC\stock_mts_mto_fix

【问题背景】

Odoo14中下述问题的修复参考：[Odoo14补货规则功能增强](http://www.thinkltd.cn/forum/2/question/odoo14-3394)

1.  问题1：Odoo13 在MTO、MTS两种模式之外，新增加了MTS + MTO的模式，但存在问题。其中一个问题是：系统检查库存数量及需求数量，如果库存数量（预测数量）大于等于需求数量，按MTS逻辑补货，否则按MTO逻辑补货。更期望的逻辑应该是：库存数量（预测数量）小于需求数量，有库存部分按MTS逻辑，不足部分按MTO逻辑。具体参照这个帖子说明 [/forum/1/question/odoo13mts-mto-428](http://www.thinkltd.cn/forum/1/question/odoo13mts-mto-428)

2.  问题2：经测试，生产领料时候，例如希望车间有料优先用完车间物料，不足部分再产生领料单。如果设置成MTS + MTO，系统实际是按MTS运作，车间物料不足部分，并不会产生领料单。

3.  问题3：Stock Move确认时候，如果是MTO规则，系统进一步查找补货rule，但系统是用Stock Move上的 Warehouse查找规则，应该优先用Stock Move的源库位所属的Warehouse查找规则。否则跨仓库 pull 时候，pull链条连不起来了。

4.  问题4：MO确认时候，原料Stock Move MTO pull 产生的子MO的最迟开始时间（date_deadline），系统减了该子MO的生产提前期。但计划时间（date_planned_start），系统未减去生产提前期，这使得无法倒排子MO，以及孙子MO的计划生产时间。经查，在2020年2月3日，Odoo修复了此Bug，参见

5.  问题5：基于“制造”规则产生MO时候（_run_manufacture），系统没有处理规则的“补货组的传播”字段（group_propagation_option）。该字段设置是否应该传播 group_id 到 MO。代码文件 Odoo13\source\odoo\addons\mrp\models\stock_rule.py   方法 def _prepare_mo_vals 中，应该增加字段 group_propagation_option 的处理，将前一级的补货组(group_id) 带入MO的补货组（procurement_group_id）。

6.  问题6：实践中发现，用户导入的BoM表，经常出现父子循环，导致BoM结构显示时候报错，错误现象：[/forum/1/question/bom-595](http://www.thinkltd.cn/forum/1/question/bom-595)。本模块在显示BoM结构之前先检查BoM是否存在循环产品，存在则报错提示。

7.   外协生产时候，系统基于外协采购入库单，自动创建外协MO，外协MO的补货组（字段 procurement_group_id）是外协采购入库单的单号。当外协采购入库单有多个明细行，每个明细行创建一个补货组，一个MO，如此，系统创建了多个同名（都是外协采购入库单的单号）的补货组（代码参考 odoo\addons\mrp_subcontracting\models\stock_picking.py  方法 def _prepare_subcontract_mo_vals ）。这样导致了一个问题，那就是，如果MO缺料，系统自动生成PO采购时候，这些不同MO的即使是同一个原料，系统也会创建不同的PO（不同补货组的缺料需求会分成不同PO）。因此，此种情况下，外协采购入库单在创建MO的补货组的时候，应该先查一下同名补货组是否存在，存在则不要创建新补货组。

本模块修复系统的上述六个问题，安装本模块后，上述几个问题自动解决。

## 补充/答案 1

【Bug修复】

1.  主MO确认时候，系统自动产生子MO。默认情况下，系统以MO单号作为MO的补货组。安装本模块后，如果制造规则上补货组传播设置成“传播”，则主MO的补货组传播到所有子MO，所有MO的补货组都一样。如果制造规则上补货组传播设置成“留空”，则所有子MO的补货组都是False。不管哪种情况，子MO的补货组总是一样（或者为主MO的单号，或者为False）。这导致了子MO的领料单（如果配置成两步生产）都合并到了一起（因为补货组相同，系统自动合并领料）。

2.  如果制造规则上补货组传播设置成“留空”，应该保留系统原本的功能，以子MO的单号作为子MO的补货组，如此，则不同子MO的领料单不会自动合并。经查，本模块在处理制造规则的“留空”时候，存在Bug，导致了问题。今天修复了此Bug，提交到了SVN。

## 补充/答案 2

V12 的版本模块名叫什么，有下载链接吗？

## 补充/答案 3

本模块是修正V13原生MTS+MTO功能的缺陷，不适用于V12，V12原生没有MTS+MTO功能 。

V12版本MTS+MTO模式，需要第三方模块支持，参考 [/forum/2/question/mrp-mto-with-stock-3135](http://www.thinkltd.cn/forum/2/question/mrp-mto-with-stock-3135)

## 补充/答案 4

BoM循环检查报错：

![[2-odoo13-mts-mto-bugstock-mts-mto-fix-3258-c48cf4c4.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
