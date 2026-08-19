---
title: "二开销售采购仓库包装规格模块sale_purchase_stock_packaging"
source: "http://www.thinkltd.cn/forum/2/sale-purchase-stock-packaging-3165"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开销售采购仓库包装规格模块sale_purchase_stock_packaging

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/sale-purchase-stock-packaging-3165>

V12 SVN存放位置：odoo_ecommerce/12.0SRC/sale_purchase_stock_packaging

V13.0位置：OSCG_SVN\odoo_ecommerce\13.0SRC\sale_purchase_stock_packaging

【20220324新增15.0版本】位置： OSCG_SVN\odoo_ecommerce\15.0SRC\包装称重

【模块设计】

1) 销售订单明细行上增加字段“箱数(package_qty)”, Tree视图上显示字段“箱规product_packaging”(该字段系统中已经有，只需要显示出来)。此两字段的显示加上权限组 product.group_stock_packaging 。
2）销售订单明细行上选择产品时候，默认带出“箱规product_packaging”。默认取产品上的第一个箱规（产品上的字段 packaging_ids）。
3) 箱数是计算型字段，计算规则是：如果字段“product_packaging”没值，箱数为0，如果有值，取值为订购数量(product_uom_qty) / 箱规产品数（qty）

4）采购明细行上增加字段“箱规product_packaging”、“箱数(package_qty)”,加上权限组 product.group_stock_packaging 。
5）采购订单明细行上选择产品时候，默认带出“箱规product_packaging”。默认取产品上的第一个箱规（产品上的字段 packaging_ids）。
6）箱数是计算型字段，计算规则是：如果字段“product_packaging”没值，箱数为0，如果有值，取值为订单数量(product_qty) / 箱规产品数（qty）

7) stock.move和stock.move.line上增加字段“箱规product_packaging”、“箱数(package_qty)”,加上权限组 product.group_stock_packaging 。
8）stock.move箱规取数规则是：如果 sale_line_id有值，取销售明细行上的箱规，如果purchase_line_id有值，取采购明细行上的箱规，**如果都取不到，则默认取产品的第一个包装规格，因为也会存在内部调拔或是其他领用等情况**。箱数计算规则和销售明细行上的一样，用初始需求（product_uom_qty）除以箱规产品数（qty）。
9）stock.move.line的箱规则从对应的Stock Move (move_id) 取，箱数计算规则和销售明细行上的一样，用保留数（product_uom_qty）除以箱规产品数（qty）。

10) **库存调整明细行（stock.inventory.line）上，“实际数量”的左边增加“箱规”、“箱数”字段，权限组 product.group_stock_packaging 。修改箱数时候，自动填写实际数量，修改实际数量时候，也自动填写箱数。**

**【功能截图】**

采购表单

![[2-sale-purchase-stock-packaging-3165-b9c9dd2f.png]]

Picking表单

![[2-sale-purchase-stock-packaging-3165-434fec0f.png]]

销售表单

![[2-sale-purchase-stock-packaging-3165-ec19a2d1.png]]

## 补充/答案 1

仍有些问题，SO和PO上，如果某个产品没有配置包装规格，则应当默认【箱数】为1，按基础计量单位来显示，否则总是填写的数量会被互相计算而变成0，需要用户反复录入【数量】才能保存。

![[2-sale-purchase-stock-packaging-3165-87c25402.png]]

一点【保存】，数量一列又变成0了。

好几个客户都有用到这个模块，敬请修改升级。

## 补充/答案 2

@小施，有个bug，因为订单上的箱数和数量是有相互计算，当订单上某个产品是服务类型的，不存在包装的配置的情况下，会自动将订购数量变成0，导致需要带金额的服务类的产品行，数量会变掉。

是否可以增加一个判断，如果是产品没有包装规格，可否以基础计量单位来计算，或者这种情况下单据上就不要互相计算了。

## 补充/答案 3

12,13代码已更新。

产品 增加新字段：默认包装（default_product_packaging）

销售、采购、出库明细、出库详细明细、库存调拨 增加新字段：包装(product_packaging)、包装规格(package_qty)。

即时库存 增加新字段：包装数量(package_uom_qty)、包装规格(package_qty)。包装数量 优先取产品的默认包装的数量，其次取基本单位的比值（factor）。

如果 包装未填，不会影响原来的 数量取值方式。

## 补充/答案 4

请模块优化一下仓库这里的视图，加个过滤，更新一下，实际上销售，采购明细行上的包装规格，也需要加一下过滤，避免出来所有产品的包装规格，而是只要出来该产品的包装规格，包数的计算需要依据包装规格来算，这样就可以适用于当某个产品有多个不同的包装规格时的使用场景了，比如香烟，做零售是单包销售也可以一条销售，做采购或是批发则是整箱销售，这里就有二个包装规格可供用户订单上选择。

![[2-sale-purchase-stock-packaging-3165-9276ef62.png]]

## 补充/答案 5

SO订单上的包装规格无法默认带出的原因是，SO明细行添加产品时默认数量是0，如果改为默认是1，就能带出规格来了。

## 补充/答案 6

V13啥时候出来？

可以【库存计价】表上面也能按这个包装显示包装规格以及包装后的箱数吗

## 补充/答案 7

V13升级好了。OSCG_SVN\odoo_ecommerce\13.0SRC\sale_purchase_stock_packaging

V13中，在Stock Quant上增加了 箱规和箱数 字段。不过，考虑性能问题，此二字段不会自动计算，而是要点击菜单“刷新在手箱数”，系统刷新所有内部位置的Quant的箱规和箱数。参考下面功能截图。

![[2-sale-purchase-stock-packaging-3165-8209ccc8.png]]

## 补充/答案 8

测试的问题三个改的点：

1、在仓库move上可以填写【完成箱数】自动计算【完成】数量吗？

2、另外move.line上没有【箱数】，包括是否也能填写【完成箱数】自动互算【完成】数量，或者算数量能自动计算箱数呢？

这个功能就象销售和采购一样的操作，请优化一下。

![[2-sale-purchase-stock-packaging-3165-3800732e.png]]

![[2-sale-purchase-stock-packaging-3165-3800732e.png]]

包括move.line上也是如此，方便操作。

3、另外，模块请更新代码xml写入：

stock.view_stock_move_line_operation_tree 将这张视图move.line里面补上【保留箱数】这个值目前测试是在【验证】完成后会变成0，因为取的是保留数量，所以名字也改成保留箱数。

![[2-sale-purchase-stock-packaging-3165-25cde15d.png]]

## 补充/答案 9

优化完善一下：

填写箱数，能自动算出基础计量单位数量；

填写基础计量单位数量，能算出箱数。

另外，在仓库单据上，写代码时需要注意，开启批次的情况和不开批次的情况，计算走的逻辑有不同。

里面套了一层line。

做采购订单时需要留意，采购订单会手动创建和自动创建的情况，MTO时自动生成的采购订单，需要注意这个代码的写法，不要有这种bug。

同时，在多公司情况下，销售订单也有可能自动创建，所以创建的SO的箱数的写法上，需要留意避免出现这种bug.

另外，第8点，8）stock.move箱规取数规则是：如果 sale_line_id有值，取销售明细行上的箱规，如果purchase_line_id有值，取采购明细行上的箱规。箱数计算规则和销售明细行上的一样，用初始需求（product_uom_qty）除以箱规产品数（qty）-----------------------补充，如果都取不到，则默认取产品的第一个包装规格，因为也会存在内部调拔或是其他领用等情况。

是否还能再增加一个：库存盘点上的包装规格呢？

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
