---
title: "OCA供应商最低采购金额检查purchase_minimum_amount"
source: "http://www.thinkltd.cn/forum/2/ocapurchase-minimum-amount-2615"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA供应商最低采购金额检查purchase_minimum_amount

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocapurchase-minimum-amount-2615>

模块链接：

参考：[/forum/2/question/ocapurchase-order-approval-block-2613](http://www.thinkltd.cn/forum/2/question/ocapurchase-order-approval-block-2613)

This module allows you to establish and automate a specific Purchase Order Approval Block Reason in the system: the 'Minimum Purchase Order Amount per Vendor'.

### Configuration

- Go to 'Purchases / Purchase / Vendors'
- Click on a Vendor and inside the 'Sales & Purchases' page specify the non-required field 'Minimum Purchase Amount'.
- Assign the security group 'Release blocked RFQ' to users that should be able to release the block. Users in group 'Purchase / Managers' are by default assigned to this group.

###

### Usage

####

#### Set the Purchase Approval Block

1.  Go to 'Purchases / Purchase / Requests for Quotation'
2.  Create a new RFQ and upon saving if the Untaxed Amount is below the Purchase Minimum Amount specified in that vendor, then the Approval Block Reason is automatically set and the Approval Block Reason is not editable anymore.

####

#### Search existing RFQ

There is a filter 'Blocked' to search for orders that are blocked. It is also possible to search RFQ’s with the Approval Block Reason 'Minimum Purchase Order Amount per Vendor'.

####

#### Confirm the RFQ

1.  Press the button ‘Confirm’. If there’s an approval block, the order will be set to status 'To Approve'. You will then need to request a Purchase Manager to approve it.

####

#### Release the purchase approval block

1.  All the RFQ’s with a total amount surpassing the specified Minimum Purchase Order Amount for that vendor (excluding taxes) are automatically released.
2.  If a blocked RFQ without surpassing the minimum amount wants to be released, a user member of the security group 'Release RFQ with approval block' can see a button 'Release Approval Block'. When pressing it, anyone seeing that RFQ is able to validate it.

####

#### Notifications to followers

1.  Followers of the RFQ receive notifications when an approval block has been set or released.


## 原帖外链配图

![[2-ocapurchase-minimum-amount-2615-x194038c2.png]]
<small>原始地址: /web/image/920/snipaste_20190120_152123.png?access_token=7d32fa8d-e7c1-409a-86d3-054b26e06be7</small>

![[2-ocapurchase-minimum-amount-2615-x194038c2.png]]
<small>原始地址: /web/image/918/snipaste_20190120_152224.png?access_token=b97bc009-a02b-4587-8c87-dd144684b0e0</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
