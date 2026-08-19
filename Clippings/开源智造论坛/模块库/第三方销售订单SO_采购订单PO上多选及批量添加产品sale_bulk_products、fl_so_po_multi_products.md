---
title: "第三方销售订单SO/采购订单PO上多选及批量添加产品sale_bulk_products、fl_so_po_multi_products"
source: "http://www.thinkltd.cn/forum/2/so-posale-bulk-productsfl-so-po-multi-products-3255"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 第三方销售订单SO/采购订单PO上多选及批量添加产品sale_bulk_products、fl_so_po_multi_products

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/so-posale-bulk-productsfl-so-po-multi-products-3255>

模块链接：

该模块需要和这个模块一起使用：[web_widget_many2many_tags_multi_selection](http://www.thinkltd.cn/forum/2/question/ocaweb-widget-many2many-tags-multi-selection-2837)

【注意事项】

该模块的 sale_bulk_products\\_manifest__.py 文件里面需要添加 模块依赖 web_widget_many2many_tags_multi_selection：

    'depends': ['base', 'sale','product','stock', 'web_widget_many2many_tags_multi_selection'],

模块使用效果截图：

![[2-so-posale-bulk-productsfl-so-po-multi-products-3255-ca86f94d.png]]

## 补充/答案 1

模块连接：https://www.odoo.com/apps/modules/13.0/fl_so_po_multi_products/

该模块为销售和采购的批量添加产品，不需要依赖任何安装包

![[2-so-posale-bulk-productsfl-so-po-multi-products-3255-a2b9a173.png]]

![[2-so-posale-bulk-productsfl-so-po-multi-products-3255-cbd3e233.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
