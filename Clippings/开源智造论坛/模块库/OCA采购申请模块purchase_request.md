---
title: "OCA采购申请模块purchase_request"
source: "http://www.thinkltd.cn/forum/2/ocapurchase-request-2639"
forum: "模块库"
author: "肖相扶"
published: 2024-10-30
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA采购申请模块purchase_request

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-10-30
> <http://www.thinkltd.cn/forum/2/ocapurchase-request-2639>

【2024/01/19】升级到Odoo17： OSCG_Git\17.0\extra-addons\purchase_request

模块链接：

改善版：OSCG_SVN\odoo_ecommerce\14.0SRC\库存请求\purchase_request

【20220910功能增加】从补货菜单发起采购请求后，补货菜单不再显示该产品缺货。即，补货菜单中，缺货计算时候把采购请求中的数量考虑进去。目前系统考虑的是采购请求单状态为 'draft', 'to_approve'的数量，'approved'状态的采购请求单的数量不考虑（该状态可能已经发起了采购，操作上的注意事项是，采购请求单审批通过后，应该马上发起采购，否则，补货菜单中不会考此状态的采购请求，可能导致再次补货。如果已经发起了采购，则采购单上的数量会被系统纳入补货计算，因而不会重复订货）。

1.  当MO、SO需要物料时候，Odoo原本功能是Procurement直接生成RFQ，本模块则可以生成采购请求单。此模块实现的功能比Odoo自带的 purchase_requisition模块更好。

2.  同一个补货组的采购需求，自动合并到同一个采购请求单。且，每个采购请求行上，系统默认自动填写该产品的第一个供应商

3.  其他部门需要采购产品时，需求部门和采购部门直接缺乏沟通单据（采购请求单），本模块提供采购请求单功能

4.  SVN上改善的模块，采购请求行上可以填写供应商，可以批量创建采购单/RFQ，创建时候可以指定PO（所有采购请求行都合并到指定的PO上），指定供应商（所有采购请求行都从该供应商采购，和Odoo自带的 purchase_requisition功能一致），也可以不指定供应商（按每个采购请求行上的供应商分别采购）。

You use this module if you wish to give notification of requirements of materials and/or external services and keep track of such requirements.

Requests can be created either directly or indirectly. "Directly" means that someone from the requesting department enters a purchase request manually.

The person creating the requisition determines what and how much to order, and the requested date.

"Indirectly" means that the purchase request initiated by the application automatically, for example, from procurement orders (MO, SO).

A purchase request is an instruction to Purchasing to procure a certain quantity of materials services, so that they are available at a certain point in time.

A line of a requisition contains the quantity and requested date of the material to be supplied or the quantity of the service to be performed. You can indicate the service specifications if needed.

Once request is approved go to the Purchase Request Lines from the menu entry 'Purchase Requests', and also from the 'Purchase' menu.

Select the lines that you wish to initiate the RFQ for, then go to 'More' and press 'Create RFQ'.

You can choose to select an existing RFQ or create a new one. In the later, you have to choose a supplier.

In case that you chose to select an existing RFQ, the application will search for existing lines matching the request line, and will add the extra quantity to them, recalculating the minimum order quantity, if it exists for the supplier of that RFQ.

In case that you create a new RFQ, the request lines will also be consolidated into as few as possible lines in the RFQ.

## [Configuration](https://github.com/OCA/purchase-workflow/tree/11.0/purchase_request#id1)

To configure the product follow this steps:

1.  Go to a product form.
2.  Go to *Inventory* tab.
3.  Check the box *Purchase Request* along with the route *Buy*.

With this configuration, whenever a procurement order is created and the supply rule selected is 'Buy' the application will create a Purchase Request instead of a Purchase Order.

##

## [Usage](https://github.com/OCA/purchase-workflow/tree/11.0/purchase_request#id2)

Purchase requests are accessible though a new menu entry 'Purchase Requests', and also from the 'Purchase' menu.

Users can access to the list of Purchase Requests or Purchase Request Lines.

It is possible to filter requests by its approval status.

## 补充/答案 1

此模块有几个问题

1.如果同一个请购明细行分多次采购时，取的是第一张采购单的状态

2.如果启用了Odoo原生的采购单确认后锁定功能，那么只要其中任意一个明细行的采购状态是锁定，则这张请购单不能继续创建询价单，会报错，事实上同第一点，如果只采购了一部分数量，此时采购状态也是锁定

GIT上已经修复，改成了判断请购单数量是否小于已采购数作为判断条件，但是写得不好，直接用了比较符号没用float比较方法。

3.点创建询价单时，弹窗里每行的请购数目前就等于请购单明细行的数量，可能等于 请购数减去已采购数更好

[4.purchase.request.line](https://4.purchase.request.line) 的排序是ID DESC，如果用户是excel导入请购单，就会发现excel上的内容在请购单里是倒序的，解决方案1是在PY的order里把desc去掉，解决方案2是在tree视图上重写排序方法

## 补充/答案 2

模块：

在采购请求单上添加 部门 字段，从而可以按部门汇总查看。

模块：[https://github.com/OCA/purchase-workflow/tree/11.0/purchase_request_order_approved
](https://github.com/OCA/purchase-workflow/tree/11.0/purchase_request_order_approved)

依赖模块 purchase_order_approved，在Purchase Request Line上显示该PR对应的PO是否已经Approved了。

【功能截图】

![[2-ocapurchase-request-2639-6646eaca.png]]

![[2-ocapurchase-request-2639-cebd9282.png]]

This module computes the new PO state 'Approved' related to a Purchase Request Line to display it in the Purchase Request Line tree view and adds a 'Purchase Approved' filter.

## 补充/答案 3

这个审批层是固定一层吗？有自定义多层审批的功能吗？业务场景：要在采购请购单上加字段关联到“项目”，对应的项目负责人要有审批请购单的权限。

![[2-ocapurchase-request-2639-bf0b401f.png]]

![[2-ocapurchase-request-2639-bf0b401f.png]]

## 补充/答案 4

多层审批模块  [purchase-workflow/purchase_request_tier_validation at 14.0 · OCA/purchase-workflow · GitHub
](https://github.com/OCA/purchase-workflow/tree/14.0/purchase_request_tier_validation)

多层审批用法参考：[OCA审批工作流base_tier_validation、purchase_tier_validation、sale_tier_validation](http://www.thinkltd.cn/forum/2/question/ocabase-tier-validationpurchase-tier-validationsale-tier-validation-2588)


## 原帖外链配图

![[2-ocapurchase-request-2639-x194038c2.png]]
<small>原始地址: /web/image/962/snipaste_20190120_203645.png?access_token=dc5572ad-df5d-454c-9995-b07fbfb13113</small>

![[2-ocapurchase-request-2639-x194038c2.png]]
<small>原始地址: /web/image/964/snipaste_20190120_204323.png?access_token=de699ef0-5265-4a8e-aa74-427d593da06d</small>

![[2-ocapurchase-request-2639-x194038c2.png]]
<small>原始地址: /web/image/966/snipaste_20190120_204526.png?access_token=27069399-d5ba-48f0-8117-e503018d9f33</small>

![[2-ocapurchase-request-2639-x194038c2.png]]
<small>原始地址: /web/image/968/snipaste_20190120_204533.png?access_token=9768f968-0eca-4895-9ab0-3329d556fec6</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
