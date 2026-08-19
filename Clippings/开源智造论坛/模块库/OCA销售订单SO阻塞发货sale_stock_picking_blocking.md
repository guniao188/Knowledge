---
title: "OCA销售订单SO阻塞发货sale_stock_picking_blocking"
source: "http://www.thinkltd.cn/forum/2/ocasosale-stock-picking-blocking-2670"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA销售订单SO阻塞发货sale_stock_picking_blocking

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocasosale-stock-picking-blocking-2670>

模块链接：

SO上增加阻塞字段，如果有阻塞，SO确认时候不生成发货单，阻塞解除后再生成发货单。

## [Configuration](https://github.com/OCA/sale-workflow/tree/11.0/sale_stock_picking_blocking#id1)

To configure this module, you need to:

1.  Go to 'Sales > Configuration > Sales > Delivery Block Reason'.
2.  Create the different reasons that can lead to block the deliveries of a sales order.
3.  Add some users to the group 'Release Delivery Block in Sales Orders'.

Additionally, you can set a customer with a 'Default Delivery Block Reason' policy to add that delivery block to his sales by default:

1.  Go to 'Sales > Sales > Customers'.
2.  In the 'Sales & Purchases' add a 'Default Delivery Block Reason'.
3.  The 'Default Delivery Block Reason' will be added automatically when creating a new sales order for the customer.

##

## [Usage](https://github.com/OCA/sale-workflow/tree/11.0/sale_stock_picking_blocking#id2)

To use this module, you need to:

1.  Create a new sales order and provide a 'Delivery Block Reason'.
2.  Confirm Sale (No delivery would be created).
3.  Release Delivery Block when it is time to create the deliveries for the sales order.

## 补充/答案 1

应用安装后，需要设置权限，销售单开票之后才能显示release delivery block（释放解锁出库）

## 补充/答案 2

V12版本：

V13链接：svn\odoo_ecommerce\13.0SRC\sale_stock_picking_blocking
本地测试没有问题

![[2-ocasosale-stock-picking-blocking-2670-b8c3764d.png]]

![[2-ocasosale-stock-picking-blocking-2670-7a75e6d1.png]]

![[2-ocasosale-stock-picking-blocking-2670-7218ef2e.png]]


## 原帖外链配图

![[2-ocasosale-stock-picking-blocking-267-x194038c2.png]]
<small>原始地址: /web/image/1012/snipaste_20190121_102834.png?access_token=50b77917-db93-4a1f-a2f0-271340ee1235</small>

![[2-ocasosale-stock-picking-blocking-267-x194038c2.png]]
<small>原始地址: /web/image/1014/snipaste_20190121_102639.png?access_token=42dfb2a8-a764-4707-b105-8a8cde475445</small>

![[2-ocasosale-stock-picking-blocking-267-x194038c2.png]]
<small>原始地址: /web/image/1016/snipaste_20190121_102756.png?access_token=c26dbb57-89c7-4a8b-aefb-cc8b63c854ed</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
