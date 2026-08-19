---
title: "二开生产替代料功能模块mrp_substitions、purchase_split_substitions"
source: "http://www.thinkltd.cn/forum/2/mrp-substitionspurchase-split-substitions-3396"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开生产替代料功能模块mrp_substitions、purchase_split_substitions

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/mrp-substitionspurchase-split-substitions-3396>

模块位置：OSCG_SVN\odoo_ecommerce\14.0SRC\替代料\mrp_substitions

OSCG_SVN\odoo_ecommerce\14.0SRC\替代料\purchase_split_substitions

【模块mrp_substitions功能】

1.  生产模块中，增加替代料配置功能，即某物料A，如果是可替代料，可以配置它的替代料 A1，A2，A3

2.  BoM使用替代料A，MO确认时候，系统自动查找原料中的替代料，将其替换为A1，A2，A3，替换规则是，先将A1，A2，A3的库存消耗掉，如果还不够，则不够的数量都增加到A1上。

【模块purchase_split_substitions功能】

1.  如果待采购物料A1有替代组，则采购明细分拆时候（参考：[/forum/2/question/purchase-split-3395](http://www.thinkltd.cn/forum/2/question/purchase-split-3395) ），不按供应商分拆，而是按替代料组分拆。即可以将A1的采购，拆分为A1，A2，A3的采购。

2.  被拆分出来的采购明细行，如A2，PO确认时候，如果当初A1的采购明细是由某Stock Move通过MTO方式产生的，则系统会自动找到该Stock Move，复制出一条来，产品换成A2，将A2的采购入库Stock Move MTO关联到复制出来的Stock Move上。

【功能截图】

![[2-mrp-substitionspurchase-split-substitions-3396-034c3915.png]]

![[2-mrp-substitionspurchase-split-substitions-3396-41e5baa8.png]]

![[2-mrp-substitionspurchase-split-substitions-3396-a9491157.png]]

![[2-mrp-substitionspurchase-split-substitions-3396-226b88dd.png]]

## 补充/答案 1

【已知问题】

注意：替代产品和替代料不能是同一个产品，如下图。否则MO创建欠单时候，系统报错。

![[2-mrp-substitionspurchase-split-substitions-3396-121db96d.png]]

![[2-mrp-substitionspurchase-split-substitions-3396-f19c4289.png]]

## 补充/答案 2

替代料另一个bug问题反馈：

会在MO完工，生成一条没有使用替代料的情况下，也会让明细行变成二行。

![[2-mrp-substitionspurchase-split-substitions-3396-b271463e.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
