---
title: "二开生产领料及线边库库存管理mrp_mto_with_stock"
source: "http://www.thinkltd.cn/forum/2/mrp-mto-with-stock-3135"
forum: "模块库"
author: "肖相扶"
published: 2022-12-16
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开生产领料及线边库库存管理mrp_mto_with_stock

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-16
> <http://www.thinkltd.cn/forum/2/mrp-mto-with-stock-3135>

模块链接：OSCG_SVN\odoo_ecommerce\12.0SRC\mrp_mto_with_stock

本模块从此模块改造而来：[/forum/2/question/ocamomts-mtomrp-mto-with-stockmrp-mto-with-stock-purchase-3015](http://www.thinkltd.cn/forum/2/question/ocamomts-mtomrp-mto-with-stockmrp-mto-with-stock-purchase-3015)

【业务背景】

车间的线边库，原则上是零库存的，但因为整包装领料的原因，上次未用完的原料还会留在线边库。本次领料的时候，希望扣除线边库余料再领料。

如果用MTO处理总仓到线边库的领料，可以实现零库存管理，也可以实现领料单和生产单间的关联关系（通过源单据关联）。但无法实现先扣除余料再领料的需求。

如果用零安全库存（设定线边库最大、最小数量都为0的再订货规则），可以实现零库存管理，也可以实现先扣除余料再领料的需求，但领料单和MO单失去了关联关系，其次，每个物料都要设定再订货规则，设置工作也很麻烦。

本模块实现上述需求：1) 物料上可以设置该物料是否在线边库先按MTO扣除余料，不足料时候，再按MTO领料；2) 修改MO生产数量时候，将MO的原料Stock Move统一修改成MTS方式。如果不修改，MO生产数量调大的时候，会导致原料Stock Move无法锁货（因为上游总仓到线边库的领料Picking数量没有同步调大，参考此贴说明 [/forum/1/question/mto-365](http://www.thinkltd.cn/forum/1/question/mto-365)）。

![[2-mrp-mto-with-stock-3135-fe01a756.png]]

## 补充/答案 1

![[2-mrp-mto-with-stock-3135-5aaa70df.png]]

是否启用生产线边库的设定

![[2-mrp-mto-with-stock-3135-0ce26e32.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
