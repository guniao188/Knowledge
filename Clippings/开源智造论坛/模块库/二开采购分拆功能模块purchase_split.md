---
title: "二开采购分拆功能模块purchase_split"
source: "http://www.thinkltd.cn/forum/2/purchase-split-3395"
forum: "模块库"
author: "肖相扶"
published: 2024-08-06
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开采购分拆功能模块purchase_split

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-08-06
> <http://www.thinkltd.cn/forum/2/purchase-split-3395>

模块位置：OSCG_SVN\odoo_ecommerce\14.0SRC\替代料\purchase_split

【模块功能】

1.  系统根据路线生成采购单（草稿）时候，总是取产品的第一个供应商。有时候希望平衡各个供应商，要改成向每个供应商都采购一定数量。针对此种需求，本模块提供了一个采购明细行拆分功能。

2.  拆分时候，系统自动取出产品的所有供应商，修改数量，而后系统自动拆出多个明细行。拆分时候，如果供应商有草稿状态的PO，则自动将新拆出的明细行合并到该PO，如果没有，则自动创建一个新PO。

3.  拆分时候，如果原采购明细是由某个Stock Move通过MTO规则产生的，拆出来的采购明细行会自动指向该Stock Move

【功能截屏】

![[2-purchase-split-3395-1c40a246.png]]

![[2-purchase-split-3395-6e183991.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
