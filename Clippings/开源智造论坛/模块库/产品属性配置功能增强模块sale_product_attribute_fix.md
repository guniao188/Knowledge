---
title: "产品属性配置功能增强模块sale_product_attribute_fix"
source: "http://www.thinkltd.cn/forum/2/sale-product-attribute-fix-3588"
forum: "模块库"
author: "肖相扶"
published: 2023-08-11
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 产品属性配置功能增强模块sale_product_attribute_fix

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2023-08-11
> <http://www.thinkltd.cn/forum/2/sale-product-attribute-fix-3588>

模块链接：OSCG_Git\extra-addons\sale_product_attribute_fix

【模块功能】

1.  Odoo标准功能中，产品变体的名称显示时候，有两个问题，其一是，只显示属性值，不显示属性。其二是，如果某属性只有一个可选的属性值，则变体名称显示时候，不显示该属性值。

2.  Odoo标准功能中，自定义（custom）的属性值，系统总是当成相同属性值处理。即，产品配置时候，每次填写不同的属性值，系统却总是当成同一个产品变体处理

3.  本模块解决上述几个问题。变体名称显示的两个问题，通过继承修改模型product.attribute.value的方法def _get_combination_name()  实现

4.  自定义属性的问题，在属性值上增加配置字段“自动新增属性值”，如果勾选，则产品配置时候，每次填写自定义值时候，系统自动新增一个该自定义值的属性值。如此，当每次填写不同的属性值时，系统总是会创建不同的产品变体。

【功能截图】

![[2-sale-product-attribute-fix-3588-66727166.png]]

![[2-sale-product-attribute-fix-3588-08cf25a9.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
