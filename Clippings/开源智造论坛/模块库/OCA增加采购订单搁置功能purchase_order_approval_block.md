---
title: "OCA增加采购订单搁置功能purchase_order_approval_block"
source: "http://www.thinkltd.cn/forum/2/ocapurchase-order-approval-block-2613"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA增加采购订单搁置功能purchase_order_approval_block

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocapurchase-order-approval-block-2613>

模块链接：

依赖模块： [/forum/2/question/ocapopurchase-exception-2609](http://www.thinkltd.cn/forum/2/question/ocapopurchase-exception-2609)

1.  采购经理审批PO时候，如果某些原因不想立即审批（暂时搁置），本模块在PO上增加了字段approval_block_id (采购订单搁置原因)

2.  采购订单列表视图增加了“搁置订单”的筛选项

3.  搁置订单Confirm时候，报异常（参见 [/forum/2/question/ocapopurchase-exception-2609](http://www.thinkltd.cn/forum/2/question/ocapopurchase-exception-2609)）

## Purchase Order Approval Block

This module allows you to block the approval of an RFQ when an Approval Block Reason has been provided. Upon confirmation of an RFQ the orders will be waiting for approval by a Manager.

###

### Configuration

- Go to ‘Purchases / Configuration / Purchase Approval Block Reasons’ and create the blocking reasons as needed, providing a name and a description. A field ‘Active’ allows you to deactivate the reason if you do not plan to use it any more.
- Assign the security group 'Release blocked RFQ' to users that should be able to release the block. Users in group 'Purchase / Managers' are by default assigned to this group.

###

### Usage

####

#### Set the Purchase Approval Block

1.  Go to ‘Purchases / Purchase / Requests for Quotation’
2.  Create a new RFQ and indicate the approval block reason (found in the right hand side of the screen, below the order date).

####

#### Search existing RFQ

There is a filter ‘Blocked’ to search for orders that are blocked for approval. It is also possible to search RFQ’s with a specific block reason.

####

#### Confirm the RFQ

1.  Press the button ‘Confirm’. If there’s an approval block, the order will be set to status 'To Approve'. You will then need to request a Purchase Manager to approve it.

####

#### Release the purchase approval block

While the RFQ is in draft, members of security group ‘Release blocked RFQ’, can see a button ‘Release Approval Block’. From this point and on, anyone seeing that RFQ will be able to validate it.

####

#### Notifications to followers

Followers of the RFQ receive notifications when an approval block has been set or released.


## 原帖外链配图

![[2-ocapurchase-order-approval-block-261-x194038c2.png]]
<small>原始地址: /web/image/908/snipaste_20190120_150249.png?access_token=76cdf75a-c697-41f3-a484-f6ce819fafd8</small>

![[2-ocapurchase-order-approval-block-261-x194038c2.png]]
<small>原始地址: /web/image/910/snipaste_20190120_150331.png?access_token=0efc23ea-f54d-458c-bd10-c50f7095caca</small>

![[2-ocapurchase-order-approval-block-261-x194038c2.png]]
<small>原始地址: /web/image/912/snipaste_20190120_150827.png?access_token=d834b953-f446-4674-bbc3-9ac7a2e45a3a</small>

![[2-ocapurchase-order-approval-block-261-x194038c2.png]]
<small>原始地址: /web/image/914/snipaste_20190120_151028.png?access_token=f6cc17e7-b13a-42d4-b1fc-0fcbc7f0de61</small>

![[2-ocapurchase-order-approval-block-261-x194038c2.png]]
<small>原始地址: /web/image/916/snipaste_20190120_151257.png?access_token=10b6f6dd-5c7b-48d3-bf5c-1b0dd3ee6abb</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
