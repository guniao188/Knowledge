---
title: "Odoo超级BoM功能增强模块mrp_super_bom"
source: "http://www.thinkltd.cn/forum/2/odoobommrp-super-bom-4009"
forum: "模块库"
author: "肖相扶"
published: 2024-12-12
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo超级BoM功能增强模块mrp_super_bom

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-12-12
> <http://www.thinkltd.cn/forum/2/odoobommrp-super-bom-4009>

模块链接：OSCG_Git\18.0\extra-addons\mrp_super_bom

【模块开发背景】参考   [Odoo超级BoM模块mrp_super_bom | Odoo技术服务管理平台 - 上海开源智造软件有限公司](http://www.thinkltd.cn/forum/2/odoobommrp-super-bom-4001)

【模块功能】

1.  Odoo BoM表上增加计算数量字段。例如服装款式，大号、中号、小号，或者自定义尺寸，BoM上原料数量是不同的。计算数量字段可以基于产品变体的属性，自定义Python代码计算原料的数量。没有设置计算数量的情况，系统仍取Odoo原有的数量字段。
2.  Odoo销售明细行上增加BoM成本按钮，点击按钮，列示产品的BoM明细，及成本。此功能主要用于定制化的变体的成本查看。
3.  BoM如果带有“套件”类型的下级BoM，BoM成本明细行列示其下级BoM的明细行。非套件的下级BoM，则只列示该下级产品成本，不管其下级。
4.  属性定制的产品且MTO的产品，SO确认时候，系统基于变体的属性，筛选BoM明细行（Odoo标准功能），再根据BoM明细行的“计算数量”字段，计算BoM原料数量（本模块新增功能），生成对应MO。
5.  计算数量字段的代码写法，参考计算字段的帮助提示。

【功能截图】

带计算数量的BoM示例（示例代码 根据尺寸属性计算BoM用量）：

![[2-odoobommrp-super-bom-4009-4dcf29d1.png]]

![[2-odoobommrp-super-bom-4009-1d2e446f.png]]

销售订单SO上按属性定制产品：

![[2-odoobommrp-super-bom-4009-7309807a.png]]

点击销售明细行的“BoM成本”按钮，显示BoM成本：

![[2-odoobommrp-super-bom-4009-856c5993.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
