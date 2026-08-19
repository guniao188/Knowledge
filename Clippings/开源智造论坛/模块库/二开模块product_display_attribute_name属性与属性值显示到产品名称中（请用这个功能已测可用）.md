---
title: "二开模块product_display_attribute_name属性与属性值显示到产品名称中（请用这个功能已测可用）"
source: "http://www.thinkltd.cn/forum/2/product-display-attribute-name-3176"
forum: "模块库"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开模块product_display_attribute_name属性与属性值显示到产品名称中（请用这个功能已测可用）

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/product-display-attribute-name-3176>

##             产品显示属性加属性值（全局）

Odoo源码功能中，当产品开启变体即SKU的情况，当SKU有多个属性和属性值时，在SO，PO,以及仓库，产品列表等各个地方均展示的格式是：【内部ID号】+【产品模板名称】+圆括号里面属性值中间是小逗号隔开（xx,yy,zz）

当SKU产品变体的属性值都是数值类型时，无法准确区分这个值对应的属性是什么。

故技术上处理，全局变更，将属性的名称也展示到产品名称里面，即圆括号里面的值变更为：（属性:属性值,属性:属性值）的形式。

效果示例：

产品变体列表显示：

![[2-product-display-attribute-name-3176-a5ac64c7.png]]

Excel导出效果展示：

![[2-product-display-attribute-name-3176-b2864f33.png]]

销售订单界面效果展示：

![[2-product-display-attribute-name-3176-e5a8de3e.png]]

MO的option效果展示：

![[2-product-display-attribute-name-3176-bf9b6231.png]]

原料产品列表展示。

![[2-product-display-attribute-name-3176-9988f1f5.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
