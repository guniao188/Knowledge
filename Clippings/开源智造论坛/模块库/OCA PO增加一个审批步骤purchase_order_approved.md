---
title: "OCA PO增加一个审批步骤purchase_order_approved"
source: "http://www.thinkltd.cn/forum/2/oca-popurchase-order-approved-2611"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA PO增加一个审批步骤purchase_order_approved

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/oca-popurchase-order-approved-2611>

模块链接：

This module extends the functionality of purchases adding a new state *Approved* in purchase orders before the *Purchase Order* state. Additionally add the possibility to set back to draft a purchase order in all the states previous to *Purchase Order*.

In this new *Approved* state:

- You cannot modify the purchase order.
- However, you can go back to draft and pass through the workflow again.
- The incoming shipments are not created. You can create them by clicking the *Convert to Purchase Order* button, also moving to state *Purchase Order*.

The new state diagram is depicted below:

To configure this module:

1.  Go to 'Purchases > Configuration > Settings'.
2.  In the *Orders* section you can set the *State 'Approved' in Purchase Orders*.

##

## [Usage](https://github.com/OCA/purchase-workflow/tree/11.0/purchase_order_approved#id3)

To use this module, you need to:

1.  Go to a Request for Quotation.
2.  Click *Confirm Order*. The state is now *Approved* (if no order approval is not set).
3.  To move forward to the state *Purchase Order* and release the creation of the deliveries, click on *Convert to Purchase Order*.

## 补充/答案 1

【Odoo自带PO两步审批逻辑】

1.  开启两步审批，并设定门槛金额（高于该金额才两步审批）

2.  采购员填写PO，点击“Confirm”按钮，如果PO金额高于门槛金额，且当前操作者没有采购经理权限，则PO状态到'to approve'，待采购经理审批。如果低于门槛金额，或当前操作者有采购经理权限则PO状态直接到'purchase'，即一步完成审批

3.  采购经理点击按钮“Approve”，PO状态变为'purchase'

【本模块逻辑】

1.  在'to approve'状态后面增加了一个状态'approved'，采购经理审批后，进入'approved'

2.  采购业务员点击“Convert to Purchase”按钮后转为PO

3.  增加了配置项目“是否启用”状态'approved'


## 原帖外链配图

![[2-oca-popurchase-order-approved-2611-xc3b1797e.png]]
<small>原始地址: https://raw.githubusercontent.com/OCA/purchase-workflow/11.0/purchase_order_approved/static/description/schema</small>

![[2-oca-popurchase-order-approved-2611-x194038c2.png]]
<small>原始地址: /web/image/902/snipaste_20190120_143533.png?access_token=d01dae59-0633-433c-b4ca-85a552406553</small>

![[2-oca-popurchase-order-approved-2611-x194038c2.png]]
<small>原始地址: /web/image/904/snipaste_20190120_143642.png?access_token=00ceed4f-5528-4cf6-b019-635239bbcadb</small>

![[2-oca-popurchase-order-approved-2611-x194038c2.png]]
<small>原始地址: /web/image/906/snipaste_20190120_143044.png?access_token=73daa980-2e52-4f2e-816f-bb450e5ddfdd</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
