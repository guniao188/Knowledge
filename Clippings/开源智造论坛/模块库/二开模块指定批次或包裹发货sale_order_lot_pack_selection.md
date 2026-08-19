---
title: "二开模块指定批次或包裹发货sale_order_lot_pack_selection"
source: "http://www.thinkltd.cn/forum/2/sale-order-lot-pack-selection-2789"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开模块指定批次或包裹发货sale_order_lot_pack_selection

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/sale-order-lot-pack-selection-2789>

模块位置：OSCG_SVN\odoo_ecommerce\12.0SRC\sale_order_lot_pack_selection

销售订单上指定批次或包裹发货，应用场景及主要功能：
    * 不锈钢钢卷贸易：销售时候需要选定钢卷号码，仓库按选定钢卷号发货
    * 牛排贸易：销售时候不指定箱号，发货时候拣货完毕，根据所拣箱号确定实际发货重量（每箱的重量皆有差异），按发货重量结算
    * 本模块实现：1. SO Line上添加批次和包裹两个字段；2. SO选择产品，批次和包裹字段自动添加Domain：只显示该产品且数量大于0的批次、包裹；3. SO选择包裹，自动带出包裹数量到数量字段；4. SO对应的发货单锁货（检查可用）时候，自动按SO的批次及包裹锁货；5.Picking上的Stock Move Line上源包裹字段添加Domain只显示所选产品且数量大于0的包裹，选择源包裹时候，自动填写目标包裹及完成数量。

上述SO生成的发货单，检查可用时候，系统自动取SO的批次及包裹完成锁货：

如果不是SO生成的发货单（手工创建的发货单），按下述方法指定包裹出货：

## 补充/答案 1

注意，本模块测试中可能存在下述Odoo Bug

[/forum/1/question/you-cannot-move-the-same-package-content-more-than-once-in-the-same-transfer-or-split-the-same-package-into-two-location-252](http://www.thinkltd.cn/forum/1/question/you-cannot-move-the-same-package-content-more-than-once-in-the-same-transfer-or-split-the-same-package-into-two-location-252)

## 补充/答案 2

当销售订单上的数量超出了指定的批次号数量，在发货单上对超出指定批次的这部分产品按先进先出法锁定后，手动修改锁定的批次，例如将原锁定批次A003*1件改为A001，产品A001库存没有从期初的8件变为7件，而是新增一条“-1”的A001库存移动明细。查询在手库存如下，这样会影响对多产品批次库存的查询，还需要将负数明细自己算下。(后来新建了几个产品测试，发现没有出现类似问题，可能是因为操作导致的)

![[2-sale-order-lot-pack-selection-2789-68603ee2.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
