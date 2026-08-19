---
title: "Odoo18新特性--销售改善点"
source: "http://www.thinkltd.cn/forum/1/odoo18-3980"
forum: "求助台"
author: "肖相扶"
published: 2024-12-24
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo18新特性--销售改善点

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-12-24
> <http://www.thinkltd.cn/forum/1/odoo18-3980>

#### [Odoo18新特性列表](http://www.thinkltd.cn/forum/1/odoo18-4016)

#### 亚马逊连接器

A free order is now created when a product is replaced by Amazon.

#### 删除产品属性

新版本可以删除不再需要的产品模板上的属性值，当然，前提是需要先删除用到过该属性值的产品变体（或者从产品变体上移除该属性值）。

#### 组合产品

新版本中，组合产品(Combo Products)可以应用在电商模块，以及销售模块，而不仅仅是零售模块。组合产品相当于是套餐产品，套餐中的每一个组成都有多个选项（如主菜、点心、饮料）。

#### 佣金计划

管理销售团队的佣金计划。详细功能参看  [Odoo18销售佣金模块功能](http://www.thinkltd.cn/forum/1/odoo18-3982)

#### 报价PDF构建器

PDF构建器详细介绍参见 [Odoo18的PDF Builder（PDF构建器）](http://www.thinkltd.cn/forum/1/odoo18pdf-builder-pdf-3981)。

#### 客户查看报价单后自动通知

业务员可以决定，客户查看报价单后，是否自动给业务员发送通知。

#### Dynamic sale description from quotation template

Provide product descriptions in the quotation template to use them in quotations created from that template.

#### EDI订单

上传或拖拽客户的采购PO文件，系统自动创建SO。如果客户的PO来自Odoo系统，或者PO包含订单XML数据，系统自动提取信息预填写SO。

#### Gelato

Connect Odoo with Gelato, a print-on-demand service.

#### 管理父分类

按产品分类搜索产品时候，分类及其下级分类的产品都可以搜索出来。

#### 门户：积分和电子钱包(储值)

客户门户网站上增加了积分和电子钱包余额查看。

#### 改善了报价PDF构建器

模型上的任何字段（包括自己添加的字段）都可以应用于PDF构建器的域字段。

#### 重构了价格表，增加了价格表打印

价格表简化了，价格表可以按PDF, CSV, or XLSX格式导出。

#### 对应产品字段变化修改了邮件模板

修改了SO的报价发送邮件模板，以及订单确认邮件模板。

#### 产品表单视图改善

产品表单及模型重构了，可库存产品及可消耗产品合并成了商品(Goods)，批次/序列号跟踪改成了按数量、按批次、还是按序列号管理。

#### 产品价格

SO明细行修改数量时候，产品价格不自动变化。

#### 属性变化时自动更新产品

属性修改，或属性额外成本修改时候，自动更新所有受影响的产品。

#### 产品说明

编辑销售明细行时候，产品及产品说明两列合并为一列进行编辑。

#### Quotation templates sequence

Sort quotation templates by order of importance.

#### 移除了模块

eBay连接器模块移除了。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
