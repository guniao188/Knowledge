---
title: "OCA生产申请单mrp_production_request"
source: "http://www.thinkltd.cn/forum/2/ocamrp-production-request-3014"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA生产申请单mrp_production_request

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocamrp-production-request-3014>

模块链接：

该模块增加了生产申请单MR，一个MR可以创建多个MO。

This module extends the functionality of Manufacturing to allow you to use Manufacturing Request (MR) as a previous step to Manufacturing Orders (MO).

Some of the benefits you can obtain are:

- Allow managers to review what is going to be manufactured.
- Better control of manufacturing calendar.
- Manage big requirements splitting them in batches.
- Know your bottleneck component in advance and only schedule what you really can build.
-

## [Usage](https://github.com/OCA/manufacture/tree/11.0/mrp_production_request#id3)

To use this module, you need to:

1.  Go to *Manufacturing > Manufacturing Requests*.
2.  Create a manufacturing request or open a existing one (assigned to you or created from a procurement).
3.  If you click on *Request approval* button the user assigned as approver will be added to the thread.
4.  If you are the approver you can either click on *Approve* or *Reject* buttons.
5.  Rejecting a MR will cancel it and propagate this cancellation to destination moves.
6.  Approving a MR will allow you to create manufacturing orders.
7.  You can manually set to done a request by clicking in the button *Done*.

To create MOs from MRs you have to:

1.  Go to approved manufacturing request.
2.  Click on the button *Create Manufacturing Order*.
3.  In the opened wizard, click on *Compute lines* so you will have a quantity proposed for creating a MO. This quantity is the maximum quantity you can produce with the current stock available for the components needed in the source location.
4.  Use the proposed quantity or change it and click on *Create MO* at the bottom of the wizard.

**NOTE:** This module does not restrict the quantity that can be converted from a MR to MOs. It is in hands of the user to decide when a MR is ended and to set it to *Done* state.


## 原帖外链配图

![[2-ocamrp-production-request-3014-x194038c2.png]]
<small>原始地址: /web/image/1457/snipaste_20190310_133620.png?access_token=2691b97b-f116-4251-a4bd-0ad310bda99a</small>

![[2-ocamrp-production-request-3014-x194038c2.png]]
<small>原始地址: /web/image/1459/snipaste_20190310_133443.png?access_token=ea5ab780-49b6-4286-bda7-3457753a4d90</small>

![[2-ocamrp-production-request-3014-x194038c2.png]]
<small>原始地址: /web/image/1461/snipaste_20190310_134010.png?access_token=2e79222b-c89c-4517-a054-49bcae50d7f6</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
