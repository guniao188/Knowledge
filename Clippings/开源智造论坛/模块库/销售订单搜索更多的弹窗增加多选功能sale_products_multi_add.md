---
title: "销售订单搜索更多的弹窗增加多选功能sale_products_multi_add"
source: "http://www.thinkltd.cn/forum/2/sale-products-multi-add-3628"
forum: "模块库"
author: "肖相扶"
published: 2023-02-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 销售订单搜索更多的弹窗增加多选功能sale_products_multi_add

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2023-02-15
> <http://www.thinkltd.cn/forum/2/sale-products-multi-add-3628>

模块链接：[https://gitlab.com/oscg-china/extra-addons/-/tree/16.0/sale_products_multi_add](https://gitlab.com/oscg-china/extra-addons/-/tree/16.0/sale_products_multi_add)

【模块功能】

1.  销售订单添加产品时候，搜索更多的弹窗，一次只能点选一个产品，添加一个明细行。
2.  本模块增加功能，搜索更多的弹窗，可以勾选多个产品，一次添加多个明细行
3.  注意事项：本模块不要和系统自带的模块 sale_product_configurator、sale_product_matrix同时安装，会有冲突。
4.  快速修改数量：销售明细行上，光标落到数量列，而后可以通过上下箭头键，在上下行的的同一列（数量列）切换光标
5.  延迟搜索产品：销售明细行上输入产品名称（编码）时候，系统频繁查找产品，当产品很多（几十万个）时候，这种频繁查找严重影响系统性能。本模块在XML的字段定义上，增加了“延迟秒数(delay_seconds)”的配置参数。指定延迟秒数，则在该秒数内，系统只会查找一次产品（而不是频繁查询）。

【功能截图】

![[2-sale-products-multi-add-3628-3d4f502e.png]]

![[2-sale-products-multi-add-3628-f2d60b3d.png]]

![[2-sale-products-multi-add-3628-a3196fbe.png]]

## 补充/答案 1

Odoo V13.0版参见附件文件 sale_products_multi_add_v13.zip ：

20230210新增功能：录入产品名称时候，产品搜索改成了延迟搜索。延迟搜索的意思是，录入产品名称时候，每当改变一个字符，系统不会立即搜索产品，而是延迟一定秒数再搜索。连续快速录入时候，系统不会搜索，而是稍作停顿时候，系统再搜索。视图xml的product_id字段的options中，可以设置延迟秒数，设置参数如 'delay_seconds': 1.5  表示延迟1.5秒。

功能截图

![[2-sale-products-multi-add-3628-1ca7b2f9.png]]


## 附件

- [[附件/forum/2-sale-products-multi-add-3628-sale_products_multi_add_V13.zip|sale_products_multi_add_V13.zip]] (19 KB)

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
