---
title: "OCA打包/捆绑销售sale_product_set及sale_product_set_variant组合商品/套件"
source: "http://www.thinkltd.cn/forum/2/oca-sale-product-setsale-product-set-variant-2501"
forum: "模块库"
author: "肖相扶"
published: 2025-08-26
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA打包/捆绑销售sale_product_set及sale_product_set_variant组合商品/套件

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2025-08-26
> <http://www.thinkltd.cn/forum/2/oca-sale-product-setsale-product-set-variant-2501>

模块链接：

多属性产品打包：

13.0版：

16、17、18的版本[https://apps.odoo.com/apps/modules/16.0/product_set](https://apps.odoo.com/apps/modules/16.0/product_set)

配置Set打包产品，SO上选择Set产品。

![[2-oca-sale-product-setsale-product-set-variant-2501-d98089c3.png]]

![[2-oca-sale-product-setsale-product-set-variant-2501-87e8d1f3.png]]

![[2-oca-sale-product-setsale-product-set-variant-2501-2417eeba.png]]

![[2-oca-sale-product-setsale-product-set-variant-2501-23da4cbb.png]]

![[2-oca-sale-product-setsale-product-set-variant-2501-71bda421.png]]

添加组合套装进来后，变成订单明细行的是打散的。 然后在订单外面可以进行搜索用到这个组合集套装的订单。

## 补充/答案 1

但订单上不能显示这个打包的产品，需要SO明细上显示的是这个打包后的产品，如果SO上需要显示明细，那至少可以在哪里显示一下打包后的产品列表，或者打印能做到显示这个打包后的产品。而仓库扣减库存是按打包的里面的内容扣减。

## 补充/答案 2

打包产品有两种做法，一种是做一个打包的 SKU，该SKU有 Set类型的BoM表，如此，SO上显示的是打包SKU，出货单上显示的是按BoM表展开的内容。 这个是Odoo标准功能。

本模块展示的是另外一种做法，SO和OUT单上都是显示展开的明细，而不需要另外创建SKU。


## 原帖外链配图

![[2-oca-sale-product-setsale-product-set-x194038c2.png]]
<small>原始地址: /web/image/1066/snipaste_20190121_184751.png?access_token=75f24ce6-52e0-4932-8ed4-b8a45f01c749</small>

![[2-oca-sale-product-setsale-product-set-x194038c2.png]]
<small>原始地址: /web/image/1068/snipaste_20190121_185029.png?access_token=f8d5fd7e-dd36-4377-a7fc-aadd1e2eda9c</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
