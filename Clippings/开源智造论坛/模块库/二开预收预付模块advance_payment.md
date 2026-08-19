---
title: "二开预收预付模块advance_payment"
source: "http://www.thinkltd.cn/forum/2/advance-payment-3399"
forum: "模块库"
author: "肖相扶"
published: 2024-12-05
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开预收预付模块advance_payment

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-12-05
> <http://www.thinkltd.cn/forum/2/advance-payment-3399>

2024/01/19升级到了Odoo17.0：OSCG_Git\17.0\extra-addons\account_advance_payment、sale_advance_payment、purchase_advance_payment

2023/10/12 多公司Bug修正，Bug参考这里： [多公司property属性值问题](http://www.thinkltd.cn/forum/1/property-3783)

**2022/1/6升级到了Odoo15.0**：OSCG_SVN\odoo_ecommerce\15.0SRC\预收预付

200220819Bug修正：在Odoo15如果预收预付科目不是Recievable, Payable类型，销售单或采购单上的预收预付明细保存不了（报错）。修正了此Bug，不必要求Recievable, Payable类型。

模块位置：OSCG_SVN\odoo_ecommerce\14.0SRC\预收预付\account_advance_payment

OSCG_SVN\odoo_ecommerce\14.0SRC\预收预付\purchase_advance_payment

OSCG_SVN\odoo_ecommerce\14.0SRC\预收预付\sale_advance_payment

【模块功能】

1.  Partner上增加预收/预付会计科目配置

2.  payment.order上增加字段“预收预付”，如果勾选该字段，表示预收预付款，目标会计科目自动取自供应商的预收预付科目

3.  预收预付的情况，payment.order确认时候，系统自动创建一笔 预收/预付  和  应收应付的会计凭证。发票/账单上可以添加此笔凭证，用于核销发票金额

4.  purchase_advance_payment：采购订单上增加采购预付款页签

5.  sale_advance_payment：销售订单上增加销售预收款页签

6.  注意事项：预收预付科目不必是 Recievable, Payable类型，但必须勾选 reconcile ；其次Partner上的应收应付科目和预收预付科目不可以配置成相同科目。

【功能截图】

![[2-advance-payment-3399-065c26be.png]]

![[2-advance-payment-3399-8b5437f6.png]]

![[2-advance-payment-3399-5198da05.png]]

![[2-advance-payment-3399-62ab11a9.png]]

![[2-advance-payment-3399-649132fa.png]]

## 补充/答案 1

基于2024年12月5日17分支的版本升级至18版本

注意要把预付款科目设置成可核销

如果销售预收款不使用原生功能而使用此模块，要把预收款的类型设置成应收账款

不然payment不会进入客户支付菜单的默认过滤条件里，因为源码里会把重置partner_type的值

```python
    def _synchronize_from_moves(self, changed_fields):

    if counterpart_lines.account_id.account_type == 'asset_receivable':
        partner_type = 'customer'
    else:
        partner_type = 'supplier'
```

## 补充/答案 2

【功能改善】

添加到发票上核销应收/应付，之前的实现方法是，付款单（account.payment）过账时候，系统判断如果是预收预付，则自动创建一笔 预收预付 和  应收应付 的会计凭证。此方法的问题在于，付款单过账后，预收预付账款没有余额（转入了应收应付）。

改善后的实现方法是，发票上“添加”区域，不仅可以添加应收应付类分录，也可以添加预收预付类分录，添加后，如果是预收预付类分录，系统自动创建一笔 预收预付 和  应收应付 的会计凭证。如此，直到核销发票时候，才会冲减预收预付科目金额。

![[2-advance-payment-3399-df8de92d.png]]

【注意事项】

银行日记账，系统默认未收账款、未付账款科目设置不是银行，而是需要通过银行对账单收付款后，再核销。但系统有个问题，银行对账单核销时候，系统只匹配 应收/应付 科目，预收/预付科目不起作用。这导致银行对账单核销不了预收/预付的付款单。

一个解决办法是，用于预收预付的银行日记账，未收账款、未付账款科目直接设置成银行，如此，不需要通过银行对账单再核销。

![[2-advance-payment-3399-40b212f0.png]]

## 补充/答案 3

advance payment 功能里还有个bug，即没有考虑多公司的情况下预付账款的核销问题，多公司会无法核销
故有修改这个文件，示例客户：艾利特有应用

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
