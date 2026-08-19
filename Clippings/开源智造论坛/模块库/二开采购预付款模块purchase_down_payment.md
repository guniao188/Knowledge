---
title: "二开采购预付款模块purchase_down_payment"
source: "http://www.thinkltd.cn/forum/2/purchase-down-payment-3313"
forum: "模块库"
author: "肖相扶"
published: 2024-05-23
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开采购预付款模块purchase_down_payment

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-05-23
> <http://www.thinkltd.cn/forum/2/purchase-down-payment-3313>

模块链接：OSCG_SVN\odoo_ecommerce\13.0SRC\采购预付款\purchase_down_payment

这里还有一个实现效果更好的采购预付款模块：[/forum/2/question/smilesmile-advance-payment-purchase-3077](http://www.thinkltd.cn/forum/2/question/smilesmile-advance-payment-purchase-3077)

【业务背景】

Odoo中有销售预收款申请功能，但没有采购预付款申请功能；之前的一个做法是，直接做一个付款单，借记 应付账款，贷记 银行存款。 有些场景，希望预付款记入 “预付账款”科目，本模块实现此功能。

本模块参照系统中销售预收款的做法，增加了采购预付款申请功能。

【模块功能】

    * PO表单增加按钮“预付申请”，点击按钮，弹窗填写预付款金额，而后系统自动在PO上增加一个预付款明细行，并自动创建一个预付款账单；
    * PO上点击“创建账单”按钮，系统创建的账单上，自动添加数量为 -1 的预付款明细行，抵扣掉预付款。
    * 预付明细行上的产品，和销售预收款申请的产品相同，使用系统参数表的Key值“sale.default_deposit_product_id”配置的产品
    * 预付款产品的收入科目应该配置“预收账款”，费用科目应该配置“预付账款”

## 补充/答案 1

【功能截图】

![[2-purchase-down-payment-3313-ac79798b.png]]

预付款账单：

![[2-purchase-down-payment-3313-e719a507.png]]

预付款抵扣

![[2-purchase-down-payment-3313-3a185766.png]]

预付款产品科目配置：

![[2-purchase-down-payment-3313-837c3789.png]]

## 补充/答案 2

目前14环境可以从“昊星”这个客户的版本中拉取出来


## 附件

- [[附件/forum/2-purchase-down-payment-3313-purchase_down_paymentV17.rar|purchase_down_paymentV17.rar]] (30 KB)

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
