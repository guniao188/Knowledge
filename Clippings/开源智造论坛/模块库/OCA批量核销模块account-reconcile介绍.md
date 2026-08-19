---
title: "OCA批量核销模块account-reconcile介绍"
source: "http://www.thinkltd.cn/forum/2/ocaaccount-reconcile-2491"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA批量核销模块account-reconcile介绍

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaaccount-reconcile-2491>

模块链接：

- **l  ****类型：**实收账款和应收账款的核销方式，系统支持多种自动核销方式

1.  1)     Simple. Amount and Name：Match one debit line vs one credit line. Do not allow partial reconciliation. The lines should have the same amount (with the write-off) and the same name to be reconciled.

2.  2)     Simple. Amount and Partner：Match one debit line vs one credit line. Do not allow partial reconciliation. The lines should have the same amount (with the write-off) and the same partner to be reconciled.

3.  3)     Simple. Amount and Reference：Match one debit line vs one credit line. Do not allow partial reconciliation. The lines should have the same amount (with the write-off) and the same reference to be reconciled.

4.  4)     Advanced. Partner and Ref：Match multiple debit vs multiple credit entries. Allow partial reconciliation. The lines should have the same partner, and the credit entry ref. is matched with the debit entry ref. or name.

- **l  Account：**待核销科目，应收账款，或应付账款科目

- **l  Write off allowed：**实收账款和应收账款之间允许的差额大小，如本例中0.1元，表示不收分数（1角以下部分不收）。即差异额在0.1毛以内允许核销。

- **l  Account Lost：**允许差异核销，此处指定差异金额的会计科目。如果实际收款少于应收账款，差异部分记入此科目，一般是 财务费用，或银行手续费之类科目。

- **l  Account Profit：**差异金额的会计科目。如果实际收款高于应收账款，差异部分记入此科目，一般是 财务费用，或银行手续费之类科目。

- **l  Journal：**指定差异分录记哪个分类账

- **l  Date of reconciliation：**取哪个日期作为核销日期

- **l  Go to unreconciled item：**显示该科目的所有待核销分录明细

- **l  Start Auto Reconciliation****：**按本表单指定的规则，自动核销分录明细

 本例中，核销前，应收账款四笔，实收账款3笔，共7笔待核销分录，unreconciled item显示如下图：

运行自动核销后，三笔应收账款被核销，一笔应收账款部分核销（应收10000元，核销8000元，剩余金额 2000元）

## 补充/答案 1

是否可以增加一种自动核销规则：依据业务伙伴的银行账号来判断？如果是同一个业务伙伴，银行账户号属于同一个业务伙伴的银行应收应付凭证，与发票的同一个银行账号业务伙伴相匹配，则自动核销。

## 补充/答案 2

疑问：1）发票上有银行账号吗？ 2） Payment或银行对账单上有银行账号吗？
如果都有银行账号，发票和Payment的银行账号都利用自动动作，自动写入“参考字段( ref )” ，即可利用现成功能实现此需求。

## 补充/答案 3

银行账号都维护在业务伙伴上。有专门的银行账号表单，上面有绑定业务伙伴。

如果通过参考去记录银行账号的话，有点不太适合，因为一个业务伙伴有可能会有多个银行账号。实际要做的就是查询，收付款登记时，记一下对方的账号到【参考】字段，然后依这个值去银行账户中查。

## 补充/答案 4

【自动核销原理】 以 Simple. Amount and Reference 为例说明：

- l  系统查找该科目的、所有未核销的会计分录

- l  金额相同（方向相反）、且参考字段( ref ) 相同(完全匹配，不是模糊匹配)的分录，互相核销。注意，即使客户不同，也可以核销，如下图：

- l  客户发票确认，形成应收账款会计分录时候，分录上的“标签(name)”字段值取自发票的 name 字段，“参考(ref)”字段值取自发票的 reference 字段

- l  到款单确认时候，应收账款会计分录上的“标签(name)”字段值总是“客户付款”、“供应商付款”，“参考(ref)”字段值取自到款单的“备注( communication )”字段

- l  利用系统的“自动动作”功能，客户发票确认时候，自动将业务员姓名写入会计分录的 ref 字段，到款认领时候，业务员将自己的名字写入到款单的备注字段。如此，系统可以按 金额及ref 核销。

- l  Advanced. Partner and Ref  则是，客户一致，ref一致的多笔分录互相核销。此种方式允许多笔分录核销，允许部分核销。

多条核销示例：


## 原帖外链配图

![[2-ocaaccount-reconcile-2491-x194038c2.png]]
<small>原始地址: /web/image/694/reconcile1.png?access_token=d66674f8-0f23-40d0-baf0-668293b859b9</small>

![[2-ocaaccount-reconcile-2491-x194038c2.png]]
<small>原始地址: /web/image/696/reconcile2.png?access_token=d057e1fb-8cf7-4f17-b04a-18f433b9ad3b</small>

![[2-ocaaccount-reconcile-2491-x194038c2.png]]
<small>原始地址: /web/image/698/reconcile3.png?access_token=02c2e396-efd7-4d15-81b5-9289cbf73936</small>

![[2-ocaaccount-reconcile-2491-x194038c2.png]]
<small>原始地址: /web/image/700/reconcile4.png?access_token=b531b9e1-6be5-4a9d-8fc9-59ee1660e78b</small>

![[2-ocaaccount-reconcile-2491-x194038c2.png]]
<small>原始地址: /web/image/702/reconcile5.png?access_token=87ff4579-1031-4be2-bd92-7b62d734757e</small>

![[2-ocaaccount-reconcile-2491-x194038c2.png]]
<small>原始地址: /web/image/704/reconcile6.png?access_token=21193325-67c7-4c5c-ab11-66ce331ce757</small>

![[2-ocaaccount-reconcile-2491-x194038c2.png]]
<small>原始地址: /web/image/706/reconcile7.png?access_token=63648bec-0073-44ec-9a48-142570c81487</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
