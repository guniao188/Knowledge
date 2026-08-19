---
title: "OCA产品自动编号、料号必填、料号唯一性校验功能product_sequence"
source: "http://www.thinkltd.cn/forum/2/ocaproduct-sequence-2644"
forum: "模块库"
author: "肖相扶"
published: 2024-10-31
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA产品自动编号、料号必填、料号唯一性校验功能product_sequence

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-10-31
> <http://www.thinkltd.cn/forum/2/ocaproduct-sequence-2644>

模块链接：

Odoo17版：[product-attribute/product_sequence at 17.0 · OCA/product-attribute · GitHub](https://github.com/OCA/product-attribute/tree/17.0/product_sequence)

产品料号 (default_code)必填：

Odoo17版： [product-attribute/product_code_mandatory at 17.0 · OCA/product-attribute · GitHub](https://github.com/OCA/product-attribute/tree/17.0/product_code_mandatory)

产品料号必须唯一：

Odoo17版： [product-attribute/product_code_unique at 17.0 · OCA/product-attribute · GitHub](https://github.com/OCA/product-attribute/tree/17.0/product_code_unique) 13.0版本已升级： [/forum/2/question/product-sequence-3280](http://www.thinkltd.cn/forum/2/question/product-sequence-3280)

## Product Sequence

This module allows to associate a sequence to the product reference. The reference (default code) is unique (SQL constraint) and required.

You can optionally specify different sequences for different product categories.

###

### Installation

Prior to installing this module, if you have any existing products you should ensure they already have a unique reference (or no reference) set. Products with a default_code of '/' or empty will automatically be assigned a code of "!!mig!!" followed by the system id for that product.

Otherwise the setting of the unique constraint will fail and the module will fail to install.

###

### Usage

To specify a different sequence for a product category proceed as follows:

1.  Go to the a Product Category form view. (**note:** you will need to install Inventory app to be able to access to the form view, *Inventory > Configuration > Products > Products Categories*; or create a menuitem manually).
2.  Fill the *Prefix for Product Internal Reference* as desired.

## 补充/答案 1

V13版本已有升级，用在了平湖机械客户。

SVN目录：F:\SVN\odoo_ecommerce\06.Customization\平湖机械\V13 addons\product_sequence


## 原帖外链配图

![[2-ocaproduct-sequence-2644-x194038c2.png]]
<small>原始地址: /web/image/970/snipaste_20190120_211226.png?access_token=ca91bf8c-2ec3-4482-9678-b91c7388ccf3</small>

![[2-ocaproduct-sequence-2644-x194038c2.png]]
<small>原始地址: /web/image/972/snipaste_20190120_211345.png?access_token=1f8038be-9a5f-479e-93cd-4ed3b6885a13</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
