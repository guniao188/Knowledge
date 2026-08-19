---
title: "Odoo18 仓库单据欠单时，系统触发补货规则的问题解析"
source: "http://www.thinkltd.cn/forum/1/odoo18-4046"
forum: "求助台"
author: "葛忠彪"
published: 2025-04-25
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo18 仓库单据欠单时，系统触发补货规则的问题解析

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:葛忠彪 | 2025-04-25
> <http://www.thinkltd.cn/forum/1/odoo18-4046>

【问题现象】

1.  Odoo18测试发现，mts+mto(mts_else_mto)规则时候，例如SO按 mts+mto触发PO，PO正常或部分入库，SO部分发货（产生欠单），此时，欠单部分，系统又产生了补货的PO。如果是半成品的情况，同理，系统也会重复产生半成品补货的MO

【原因分析】

1.  欠单情况，欠单的stock move确认时候，该move的rule_id是mts_else_mto，系统会按此rule_id跑补货单，参见下述代码截图。
2.  系统跑补货单时候，是根据可用库存(free_qty)判断是否有库存，没有则生成补货单。此处有问题，因为之所以欠单，多数情况都是之前的补货部分完成（部分入库），库存不足，所以欠单出库。欠单的move，可用库存肯定是不足的（之前的补货库存尚在途，不计算在可用库存里面），因而系统又会跑出补货单。
3.  如果不是可追踪的产品，系统没有该产品的库存数据，也就是说，系统里永远没有库存，因此总是会跑出新补货单。

【解决办法】

1.  按rule规则跑补货单的代码，改成按预测库存virtual_available（而不是可用库存free_qty）来决定是否有库存。
2.  对应代码参考：OSCGODOO18\source\addons\stock\models\stock_move.py，方法 def _prepare_procurement_qty(self)，代码行 forecasted_qties_by_loc[location] = {product.id: product.free_qty for product in products} 中， product.free_qty改成  product. virtual_available即可。

注：第一张截图备注错了，是V18

V17前还是和第二张图V16的代码一致

![[1-odoo18-4046-c3790b5d.png]]

![[1-odoo18-4046-6cc78c46.png]]

首先看2张图，图2是V16版本，stock move 只有通过 _adjust_procure_method方法调整move的补货规则为MTO时才会去触发补货规则，而图1里，增加了一种可能性，即move上有rule_id 且rule_id（规则）上的补给方式是MTS+MTO时也会触发下一步补货

那么就会出现以下场景

生产a用到b，触发b的领料单，b的领料单的move上有补货规则，一旦此补货规则上的补给方式是mto+mts，且配置了能为这条规则继续提供补货的规则，则b领料单缺货时，跑欠单picking，欠单picking自动确认，触发上述逻辑跑补货

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
