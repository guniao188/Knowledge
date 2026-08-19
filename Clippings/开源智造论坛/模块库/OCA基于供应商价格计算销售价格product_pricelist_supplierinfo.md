---
title: "OCA基于供应商价格计算销售价格product_pricelist_supplierinfo"
source: "http://www.thinkltd.cn/forum/2/ocaproduct-pricelist-supplierinfo-2657"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA基于供应商价格计算销售价格product_pricelist_supplierinfo

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaproduct-pricelist-supplierinfo-2657>

模块链接：

## [Configuration](https://github.com/OCA/product-attribute/tree/11.0/product_pricelist_supplierinfo#id2)

To configure pricelists with the new feature of this module, you need to:

1.  Go to *Sales > Configuration > Settings* and check "Multiple Sales Prices per Product" option and "Prices computed from formulas" after that. You must have correct permissions and you must install **Sales Management** app (sale) to see these settings.
2.  Create or edit a Sales Pricelist at *Sales > Catalog > Pricelists*.
3.  Add or edit a pricelist item and check "Formula" option in "Price Computation" section.
4.  You will see the new option "Prices based on supplier info".
5.  If you want to bypass the "Min.Quantity" field of the supplier info and always select the lowest quantity price, check the option "Ignore Supplier Info Min. Quantity".

##

## [Usage](https://github.com/OCA/product-attribute/tree/11.0/product_pricelist_supplierinfo#id3)

For adding supplier info:

1.  Go to *Sales > Catalog > Products*
2.  Open or create a product.
3.  Go to "Purchase" page.
4.  On "Vendors" section, add the supplier and prices.
5.  You can drag and drop for reordering these lines.

Check the remark in known issues about the supplier info line selection.

For checking pricelists in action, you can (with sale module installed):

1.  Go to *Sales > Orders > Quotations*
2.  Create or edit a quotation.
3.  Add a line.
4.  Select a product with the criteria to match the pricelist from supplier info.
5.  See the proper price appears in the line.


## 原帖外链配图

![[2-ocaproduct-pricelist-supplierinfo-26-x194038c2.png]]
<small>原始地址: /web/image/988/snipaste_20190120_225606.png?access_token=08cd6c3c-aac6-44c2-8e63-812e2c2982ad</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
