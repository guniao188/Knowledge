---
title: "Odoo超级BoM模块mrp_super_bom"
source: "http://www.thinkltd.cn/forum/2/odoobommrp-super-bom-4001"
forum: "模块库"
author: "肖相扶"
published: 2024-12-12
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo超级BoM模块mrp_super_bom

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-12-12
> <http://www.thinkltd.cn/forum/2/odoobommrp-super-bom-4001>

【模块下载】 [Odoo超级BoM功能增强模块mrp_super_bom | Odoo技术服务管理平台 - 上海开源智造软件有限公司](http://www.thinkltd.cn/forum/2/odoobommrp-super-bom-4009)

【业务背景】

1.  Odoo标准功能中，支持基于产品的变体属性，选择不同的原料，构成变体的BoM。如下图所示（应用于变体列）

![[2-odoobommrp-super-bom-4001-3834b5f1.png]]

2.  但有些情况，Odoo现有功能支持不是很好。例如，以电梯生产为例，电梯有长、宽、层高、层数四个参数，参数不同，钢材的用量不同。但钢材的用量可以通过长宽高层数四个参数计算出来。例如计算公式是：(长 * 层高 + 宽 * 层高) * 层数 * 1.03 。
3.  针对电梯这种情况，一种解决方法是，电梯有四个属性： 长、宽、层高、层数，四个属性的可选值是自定义值，如下图 

![[2-odoobommrp-super-bom-4001-49c43c37.png]]

电梯BoM的明细行上，增加一列“计算数量”，计算数量是一行Python代码。制造订单MO上生成组件用量时候，如果BoM的“计算数量”有值，优先调用计算数量计算得到物料用量。
4.  针对电梯的案例，还有一个需求，销售报价时候，希望系统计算一个BoM成本价格。业务员参考成本价格给客户报价。一种解决办法是，销售明细行上增加一个按钮，点击按钮，系统显示该变体的BoM物料组成，数量，及价格。

【模块功能】

1.  Odoo的BoM明细行上增加字段“计算数量 qty_compute”
2.  MO基于BoM计算组件数量时候，优先通过“计算数量”字段获取BoM数量
3.  产品变体(product.product)上增加展开BoM明细及成本的方法: action_bom_cost，该方法显示产品的BoM物料、数量、单价、总价(数量 * 单价)
4.  销售明细行上增加按钮“BoM成本”，点击按钮，系统调用方法 action_bom_cost，显示BoM明细及成本。

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
