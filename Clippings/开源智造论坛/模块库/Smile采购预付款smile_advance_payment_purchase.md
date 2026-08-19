---
title: "Smile采购预付款smile_advance_payment_purchase"
source: "http://www.thinkltd.cn/forum/2/smilesmile-advance-payment-purchase-3077"
forum: "模块库"
author: "肖相扶"
published: 2022-12-16
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Smile采购预付款smile_advance_payment_purchase

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-16
> <http://www.thinkltd.cn/forum/2/smilesmile-advance-payment-purchase-3077>

模块链接：

Odoo14.0中，该模块不再可用，改用这个：[/forum/2/question/advance-payment-3399](http://www.thinkltd.cn/forum/2/question/advance-payment-3399)

上述链接模块可以直接在12.0上安装

Odoo 13.0版升级好了：OSCG_SVN\odoo_ecommerce\13.0SRC\采购预付款\smile_advance_payment_purchase

Odoo14.0版升级好了：OSCG_SVN\odoo_ecommerce\14.0SRC\采购预付款\smile_advance_payment_purchase

这里还有一个参照Odoo标准的销售预收款原理实现的采购预付款模块：在PO上创建预付款的供应商账单，账单上登记付款后完成预付款。对应的会计凭证有两笔， 一笔借记 预付账款，贷记 应付账款，一笔借记 应付账款，贷记 银行存款：[/forum/2/question/purchase-down-payment-3313](http://www.thinkltd.cn/forum/2/question/purchase-down-payment-3313)

【注意事项】

1.  安装本模块后，如果启用了Saxon功能，客户发票确认的时候，不会生成主营业务成本的会计分录。值得注意的是，卸载本模块，重新安装，又可以生成主营业务分录。但重启Odoo后，又不会生成主营业务分录。

2.  经查，原因是，本模块继承了account.move对象的post()方法，生成Saxon的主营业务成本分录的程序代码在sale_stock模块继承的account.move 的 post()方法中。由于本模块不依赖于sale_stock模块，这会导致，Odoo重启后，本模块的post()方法继承顺序在sale_stock模块的post() 方法之后。因而，sale_stock模块的post()方法不被调用，导致Saxon的主营业务成本分录不被生成。

3.  修正方法：如果安装了stock_cost、sale_stock、purchase_stock、stock_account模块，建议模块smile_advance_payment_base的__manifest__.py 中，依赖于上述模块。

【模块功能】

1.  供应商上设置预付账款科目

2.  设置一个预付款专用日记账（凭证类型）

3.  采购单确认后，会显示一个“Advance Payment”页签，该页签上添加预付款申请记录（实际上是Payment表单）

4.  财务在会计 | 供应商 | Payments 菜单可以看见来自采购单的预付款申请，财务付款，并过账该付款单

5.  仓库采购收货

6.  采购在采购单上创建“供应商账单”

7.  财务确认供应商账单，系统自动关联预付款单，产生一笔“借 应付账款， 贷 预付账款”的会计凭证，并抵扣供应商账单上的应付账款金额。

![[2-smilesmile-advance-payment-purchase-3077-826859fc.png]]

![[2-smilesmile-advance-payment-purchase-3077-293b3b1f.png]]

This module allows to manage supplier advance payment before invoicing the purchase order.

The amount of advance is deducted during the payment of purchase order invoice.

## [Usage](https://github.com/Smile-SA/odoo_addons/tree/11.0/smile_advance_payment_purchase#id1)

**Create purchase order, confirm it, then create advance**

**Advance is deducted once the invoice is paid**

##

## [Requirements](https://github.com/Smile-SA/odoo_addons/tree/11.0/smile_advance_payment_purchase#id2)

This module depends on [smile_advance_payment_base](https://github.com/Smile-SA/odoo_addons/tree/11.0/smile_advance_payment_base) .

## 补充/答案 1

模块在14版本里不通用，安装后，会导致无法确认发票/账单。

## 补充/答案 2

【发现Bug】

1.  Bug现象：1）PO确认；2）PO预付款；3）PO收货；4）PO开一半票，验证，此时，系统自动将预付款核销应付款。5）完成发票的付款；6）PO开另一半票，验证。此时出现Bug，系统会用步骤5中的付款，自动核销此笔发票的应付账款。

【Bug原因及解决】

1.  经调查，程序文件 smile_advance_payment_purchase\models\account_invoice.py 的方法 def _get_advance_payments 中，查找预付款单的搜索条件有Bug，该搜索条件中应该增加“仅搜索预付款”的条件。否则系统将前一个发票的付款也搜索出来，用于核销第二个发票。

2.  OSCG_SVN\odoo_ecommerce\13.0SRC\采购预付款\smile_advance_payment_purchase 的代码已经修复了上述Bug

## 补充/答案 3

经过大量单据测试发现，该模块存在一个BUG。安装该模块后，需要在联系人上设置预收账款和预付账款2个科目。这两个科目设置完之后，服务器不能重启，一旦重启，开启撒克逊会计功能状态下，销售发票就会不结转成本。除非卸载模块，重新安装。

猜测可能的原因是，一旦重启服务器，系统在读取联系人上面的预收账款和预付账款科目时，优先调用，从而与撒克逊会计结转成本功能冲突

## 补充/答案 4

OSCG_SVN\odoo_ecommerce\13.0SRC\采购预付款\smile_advance_payment_purchase
这个功能实际上也为客户的预收开了口子，业务伙伴上是可以配置好预收账款科目，是否也有办法可以用同样的方法，实现客户的预收账款自动核销呢，目前系统自带的客户发票down payment也不太好用，总是会生成一张预收的发票，且也不会在运营端订单上体现收款情况。

当然目前如有需要的客户，目前也可以装后来买的V13，直接登记进应收账款了，但这个流程终归有些涉及跨月的情况下，都统一进了应收，不太好用。

## 补充/答案 5

“借 应付， 贷 预付“的会计分录不要关联 payment_id的话，还能自动核销到正常的账单上吗？V12的目前看是没有问题，这个改动是V13的吗？

## 补充/答案 6

如果希望预付款记录到 “预付账款” 科目，建议用这个采购预付款模块更好，该模块在PO上创建预付款的供应商账单，账单上登记付款后完成预付款。对应的会计凭证有两笔， 一笔借记 预付账款，贷记 应付账款，一笔借记 应付账款，贷记 银行存款：[/forum/2/question/purchase-down-payment-3313](http://www.thinkltd.cn/forum/2/question/purchase-down-payment-3313)

## 补充/答案 7

V12上版本的正确使用：

第一步，需要配置所有供应商上的【预收账款】【预付账款】的会计科目，可以通过【公司属性】的菜单进行默认设置：

![[2-smilesmile-advance-payment-purchase-3077-dd9d0a10.png]]

![[2-smilesmile-advance-payment-purchase-3077-f7cfdd33.png]]

![[2-smilesmile-advance-payment-purchase-3077-cf503246.png]]

第二步，需要创建特殊的【日记账】即凭证类型，并勾选允许预付，且科目配置为默认银行的基本账户科目，不可以直接在原银行日记账凭证上勾选允许预付，否则在invoice那里正常登记款项时，会有报错，所以需要单独创建预付的日记账：

![[2-smilesmile-advance-payment-purchase-3077-fd69b6f3.png]]

故需要设置单独的预付款日记账：

![[2-smilesmile-advance-payment-purchase-3077-9f943d74.png]]

第三步，采购订单上点【编辑】，即可添加预付款申请和验证付款

![[2-smilesmile-advance-payment-purchase-3077-72eb4f7a.png]]

会生成相应的预付款，与款相关的会计凭证

![[2-smilesmile-advance-payment-purchase-3077-4a20639b.png]]

第四步，供应商发货，仓库正常收货入库；

第五步，采购收到供应商票据或对账，创建提交供应商账单；

第六步，会计收到发票账单，验证供应商账单：

![[2-smilesmile-advance-payment-purchase-3077-147f1029.png]]

BILL账单验证，会产生会计凭证，同时会产生可供冲销原预付款项的凭证和可供核销的记录：

![[2-smilesmile-advance-payment-purchase-3077-ea48fda5.png]]

![[2-smilesmile-advance-payment-purchase-3077-c4f242ec.png]]

为何能直接核销了，是因为在创建bill，验证后，系统同时有自动产生了一条预付与应付款转换的凭证

![[2-smilesmile-advance-payment-purchase-3077-fdf02128.png]]

所以能正常冲销原预付款。

这样做的同时，还可以使会计报表上，能正确区分预付和应付的金额。

而V13版本，因account这块改动较大，invoice对象变成了凭证同一个对象，原采购预付款模块功能不足，故有另外买只是订单与款进行绑定的模块。

## 补充/答案 8

已有另外购买V13版本

下载链接参考：

该模块有权限组预收预付

SO有预收款记录与SO有绑定；

PO有预付款记录与PO绑定

说明：这个模块主要解决的问题是销售或采购与财务收款或付款的脱节

该模块将SO或PO与收付款进行了关联，以及默认带入了相应的SO或PO单号，便于再开具账单时可以快速匹配核销账目。

但实际还是都进到了应收应付科目。并没有区分预收预付科目，只是走了预收预付货款。

## 补充/答案 9

该模块的依赖模块 smile_advance_payment_base 有个Bug，会导致供应商账单确认时候，系统报错“You cannot modify a journal entry linked to a posted payment.”。 原因是，系统产生的“借 应付， 贷 预付“的会计分录自动关联了预付款的payment单据（accout.move.line 的 payment_id字段），而系统会检查，分录修改时候，如果该分录关联的payment_id 已经过账了，报错，不允许修改分录。

【Bug修复方法】“借 应付， 贷 预付“的会计分录不要关联 payment_id ，修改代码如下：
文件 smile_advance_payment_base\models\account_payment_recovery.py 方法 def _get_shared_move_line_vals(self)，注释代码行 'payment_id': self.payment_id.id,   换成代码行 'name': self.payment_id.name,  修改完毕，重启Odoo系统即可生效。

![[2-smilesmile-advance-payment-purchase-3077-b9f46e76.png]]


## 原帖外链配图

![[2-smilesmile-advance-payment-purchase--x514878fc.png]]
<small>原始地址: https://github.com/Smile-SA/odoo_addons/raw/11.0/smile_advance_payment_purchase/static/description/purchase.pn</small>

![[2-smilesmile-advance-payment-purchase--x3c6daf47.png]]
<small>原始地址: https://github.com/Smile-SA/odoo_addons/raw/11.0/smile_advance_payment_purchase/static/description/advance.png</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
