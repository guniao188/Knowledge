---
title: "OCA到期日/保质期管理product_expiry_simple"
source: "http://www.thinkltd.cn/forum/2/oca-product-expiry-simple-2530"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA到期日/保质期管理product_expiry_simple

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/oca-product-expiry-simple-2530>

模块链接：

本模块升级到了Odoo 13.0，模块连接： OSCG_SVN\odoo_ecommerce\13.0SRC\product_expiry_simple

升级模块中还增加了到期日期报表，可以显示Stock Quant的到期日期、剩余天数、剩余天数占保质天数的比例。参见后面功能截图。

此模块功能类似于Odoo标准模块product_expiry，但比product_expiry简单实用。

1.  只在产品批次上增加一个到期日期，而不是像product_expiry那样增加4个日期

2.  入库时候，不自动计算到期日期，而是Stock Move Line上输入到期日期。product_expiry计算到期日期完全不实用，因为工厂的话，到期日计算逻辑远比product_expiry复杂，零售公司的话，到期日期是根据商品包装上的到期日期录入系统而不是那么简单地计算出来

3.  Quant上增加到期日期字段，Quant和批次列表视图上按到期日期分颜色显示

This module is similar to the official [product_expiry](https://www.odoo.com/apps/modules/11.0/product_expiry/) module that adds support for *Expiry Dates* on products, but it is both simpler and better:

- Only one *Expiry Date* field instead of 4 fields (End of Life Date, Best before Date, Removal Date, Alert Date)!
- Use date field instead of datetime field for *Expiry Date*
- No automatic computing of Expiry Date based on a delay configured on product because it is not used most of the time (for manufacturing companies, the rules that control expiry dates are usually more complex than that ; for reseller companies, they have to copy the expiry date written on the good when they receive it in their warehouse)
- List views of production lots and quants have a color depending on expiry date: green if expiry date is in the future, red if it is in the past.
- Ability to show stats about expiry dates on quants pivot table (because, with this module, the *Expiry Date* is a related stored field on stock.quant).

This modules keeps the main feature of the official *product_expiry* module: the support of FEFO (First Expiry First Out).

I decided to develop this module because, after implementing *product_expiry* at several companies, I noticed that I spent more time inheriting the official *product_expiry* module to make always the same kind of changes that re-developping a simpler and better alternative.

## 补充/答案 1

13.0版本新增到期日期报表：

![[2-oca-product-expiry-simple-2530-56dcadbd.png]]


## 原帖外链配图

![[2-oca-product-expiry-simple-2530-x194038c2.png]]
<small>原始地址: /web/image/795/snipaste_20190119_133822.png?access_token=bb2b0a89-6c26-4f16-ae65-d84dad09ffdf</small>

![[2-oca-product-expiry-simple-2530-x194038c2.png]]
<small>原始地址: /web/image/797/snipaste_20190119_133921.png?access_token=649b59db-a57a-47b7-9144-21e79ef0dc55</small>

![[2-oca-product-expiry-simple-2530-x194038c2.png]]
<small>原始地址: /web/image/799/snipaste_20190119_134046.png?access_token=a9a39ae1-7f4c-4dc2-836e-22efa65831f1</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
