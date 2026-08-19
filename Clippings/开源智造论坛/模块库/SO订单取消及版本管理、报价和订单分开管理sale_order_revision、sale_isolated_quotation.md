---
title: "SO订单取消及版本管理、报价和订单分开管理sale_order_revision、sale_isolated_quotation"
source: "http://www.thinkltd.cn/forum/2/sosale-order-revisionsale-isolated-quotation-2674"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# SO订单取消及版本管理、报价和订单分开管理sale_order_revision、sale_isolated_quotation

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/sosale-order-revisionsale-isolated-quotation-2674>

模块链接（报价和订单分开）：[sale-workflow/sale_isolated_quotation at 14.0 · OCA/sale-workflow · GitHub](https://github.com/OCA/sale-workflow/tree/14.0/sale_isolated_quotation)

模块链接（订单版本）Odoo14：[sale-workflow/sale_order_revision at 14.0 · OCA/sale-workflow · GitHub](https://github.com/OCA/sale-workflow/tree/14.0/sale_order_revision)

模块链接（订单版本）Odoo11：

On cancelled orders, you can click on the "New copy of Quotation" button. This will create a new revision of the quotation, with the same base number and a '-revno' suffix appended. A message is added in the chatter saying that a new revision was created.

In the form view, a new tab is added that lists the previous revisions, with the date they were made obsolete and the user who performed the action.

The old revisions of a sale order are flagged as inactive, so they don't clutter up searches.


## 原帖外链配图

![[2-sosale-order-revisionsale-isolated-q-x194038c2.png]]
<small>原始地址: /web/image/1020/snipaste_20190121_105427.png?access_token=7b659b3c-c3cd-4c52-9a8a-043c6fad57c5</small>

![[2-sosale-order-revisionsale-isolated-q-x194038c2.png]]
<small>原始地址: /web/image/1022/snipaste_20190121_105341.png?access_token=3c8d8470-9add-437f-afab-b7ffbe9b5691</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
