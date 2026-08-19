---
title: "Odoo14、15补货规则功能增强stock_procurement_fix、mrp_procurement_fix"
source: "http://www.thinkltd.cn/forum/2/odoo1415stock-procurement-fixmrp-procurement-fix-3394"
forum: "模块库"
author: "肖相扶"
published: 2024-10-08
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo14、15补货规则功能增强stock_procurement_fix、mrp_procurement_fix

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-10-08
> <http://www.thinkltd.cn/forum/2/odoo1415stock-procurement-fixmrp-procurement-fix-3394>

模块位置：OSCG_SVN\odoo_ecommerce\14.0SRC\补货规则改善\stock_procurement_fix  以及  OSCG_SVN\odoo_ecommerce\14.0SRC\补货规则改善\mrp_procurement_fix

【20220309升级到15.0版】15.0版位置：OSCG_SVN\odoo_ecommerce\15.0SRC\路线规则

此二个模块源于Odoo13.0的Bug修正：[/forum/2/question/odoo13-mts-mto-bugstock-mts-mto-fix-3258](http://www.thinkltd.cn/forum/2/question/odoo13-mts-mto-bugstock-mts-mto-fix-3258)

【20240510周鸿飞升级到17.0版】17.0版位置：OSCG_GIT\extra-addons\17.0\mrp_procurement_fix

【stock_procurement_fix增强的问题】

2023年3月14日：

升级到16.0：OSCG_Git\extra-addons\stock_procurement_fix

同时增加功能：子孙MO的源单据上，增加最上层MO的源单据（通常是SO单号），如此便于按SO查找该SO相关的所有MO单据，如下截图。

![[2-odoo1415stock-procurement-fixmrp-procurement-fix-3394-4d96e478.png]]

1.  【20241008 Odoo18不需要】Odoo18自带此功能，因而不再需要！MTS+MTO的补货规则，Odoo自带逻辑是：如果库存数量小于待补货数量，则按MTO补货，否则按MTS补货；本模块将MTS+MTO的补货规则改成：如果库存数量小于待补货数量（有部分库存），则按MTS先消耗库存部分，不足部分再按MTO补货。

2.  【**不需要**】如果从另外一个仓库调拨补货（rule上配置的源库位、目标库位不在同一个仓库），此种情况，系统创建补货单procurement时候，传递过去的warehouse_id字段，是规则上设置的Warehouse（目标库位所在的仓库）。但是，系统为源库位继续补货（查找源库位的补货规则），查找条件中指定仓库为目标库位的仓库，这导致查找不到补货规则，系统报该源库位没有合适的补货规则的异常。本模块修复此Bug：创建补货单procurement时候，传递过去的warehouse_id字段，取自补货规则的源库位的Warehouse，而不是补货规则的Warehouse。**此条其实不需要，Odoo自带解决方法（路线规则上传导的仓库字段），参考下图截图说明。15.0版本中去掉了此项目修改。**

![[2-odoo1415stock-procurement-fixmrp-procurement-fix-3394-df9fee18.png]]

3.   产品上增加“最低补货数量”、“补货倍数”两个字段，系统创建补货单时候，如果需求数量低于“最低补货数量”，自动上抛到最低补货数量；而后，系统自动上抛补货数量到“补货倍数”。“最低补货数量”通常对应到最低采购数量，“补货倍数”通常对应到整包装数，或者经济生产批量。

4.  MO（表单 mrp.production）上修改BoM时候，系统自动创建原料消耗的Stock Move，此时Stock Move的补货方法(procure_method)全是MTS。MO确认时候（ 表单mrp.production的 confirm方法），系统调用Stock Move方法 def _adjust_procure_method(self):  调整Stock Move上的补货方法设置。系统查找该Stock Move适用的补货规则，根据补货规则设置Stock Move的补货规则。但系统原来有个问题，针对 mts_else_mto 类型的规则，如果源库位库存充足，系统设置该Stock Move的补货方法为MTS，如果库存不足，系统设置该Stock Move的补货方法为MTO。此处即使部分有货，系统也是简单按MTO处理。本模块修改Stock Move的方法 def _adjust_procure_method(self)，如果部分有货，则将Stock Move拆分为两条Stock Move，一条为MTS，消耗掉源库位的库存，另一条为MTO 。

![[2-odoo1415stock-procurement-fixmrp-procurement-fix-3394-5dd35c44.png]]

【mrp_procurement_fix修复的问题】

1.   基于“制造”规则产生MO时候（_run_manufacture），系统没有处理规则的“补货组的传播”字段（group_propagation_option）。该字段设置是否应该传播 group_id 到 MO。代码文件 odoo\addons\mrp\models\stock_rule.py   方法 def _prepare_mo_vals 中，应该增加字段 group_propagation_option 的处理，将前一级的补货组(group_id) 带入MO的补货组（procurement_group_id）。

2.   外协生产时候，系统基于外协采购入库单，自动创建外协MO，外协MO的补货组（字段 procurement_group_id）是外协采购入库单的单号。当外协采购入库单有多个明细行，每个明细行创建一个补货组，一个MO，如此，系统创建了多个同名（都是外协采购入库单的单号）的补货组。参考代码 odoo\addons\mrp_subcontracting\models\stock_picking.py  方法 def _prepare_subcontract_mo_vals 。这样导致了一个问题，那就是，如果MO缺料，系统自动生成PO采购时候，这些不同MO的即使是同一个原料，系统也会创建不同的PO（不同补货组的缺料需求会分成不同PO）。本模块修改此Bug：外协采购入库单在创建MO的补货组的时候，应该先查一下同名补货组是否存在，存在则不要创建新补货组。

3.  实践中发现，用户导入的BoM表，经常出现父子循环，导致BoM结构显示时候报错，错误现象：[/forum/1/question/bom-595](http://www.thinkltd.cn/forum/1/question/bom-595)。本模块在显示BoM结构之前先检查BoM是否存在循环产品，存在则报错提示。

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
