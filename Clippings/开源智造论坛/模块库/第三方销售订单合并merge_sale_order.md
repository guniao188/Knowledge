---
title: "第三方销售订单合并merge_sale_order"
source: "http://www.thinkltd.cn/forum/2/merge-sale-order-3103"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 第三方销售订单合并merge_sale_order

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/merge-sale-order-3103>

模块链接：

#### ** Merge Sale Orders**

The primary purpose of this module is to merge sale orders be it two or more than two which are in the Quotation/Draft state. User can now forget the hassles of creating new quotation on their every sale order. If the same customer is ordering from the partner’s store then only they will be able to avail the feature of merging multiple orders. If user is trying to merge sale order purchased for different customers then a pop up with a warning message will be displayed and this functionality will be disabled at that time.

Below listed are features of “Merge Sale Order” module:

- User can merge two or more than two Quotations of the same Customer.
- Various options are provided when user selects the order and proceeds for merging.
- User can create a new order of merged sale orders and previous order will be cancelled.
- Second option is user can create new merged sale order and previous orders will be deleted.
- With the third option user can select an existing order and add other orders by clicking on “Merge Sale Order” button and the existing order products will be added on the order selected. And rest of the orders will be cancelled.
- The fourth option will work as the 3rd one but when user clicks on merge sale order selected orders will be combined with the order selected and rest of the orders will be deleted.

#### ** Prerequisites before Installation**

There are no prerequisites required before the Installation

#### ** Configurations**

For merging orders, you will have to select multiple orders displayed in the quotation stage and go to the “Action” tab and select “Merge Quotations” from the dropdown menu.

As shown in the image when user selects two/more orders from the quotation tab and taps on the “Action” tab they will be able to merge order by clicking on “Merge Sale Order”.

When you click on the “Merge Sale Order” you will be asked to choose from four different options before merging the orders.

As shown in the below image you can:

- Create order by merging orders and cancel the selected orders.
- Create new order by merging orders and deleting the selected orders.
- Select existing order and add other orders to the existing order and cancel others.
- Select existing order and add other orders to the existing order and delete others.

You can merge order only if they belong to the same store. If in case you will try to merge orders from different stores you will be provided with a warning message. Moreover, your order should be in draft/quotation stage otherwise you will not be able to merge orders.

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
