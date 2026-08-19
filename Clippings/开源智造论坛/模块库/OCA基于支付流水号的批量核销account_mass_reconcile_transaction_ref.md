---
title: "OCA基于支付流水号的批量核销account_mass_reconcile_transaction_ref"
source: "http://www.thinkltd.cn/forum/2/ocaaccount-mass-reconcile-transaction-ref-2720"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA基于支付流水号的批量核销account_mass_reconcile_transaction_ref

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaaccount-mass-reconcile-transaction-ref-2720>

模块链接：

Account Move Line的字段 'transaction_ref' 相同的核销，或者字段 'transaction_ref' 和 字段 'ref' 相同的核销。收付款单模型account.payment 的Memo字段记录的银行流水号，系统会写入Account Move Line的字段 ref .

This module extends the functionality of account_mass_reconcile to use the 'transaction_ref' field defined in base_transaction_id.

## 补充/答案 1

【注意】

文件 account_mass_reconcile_transaction_ref\models\mass_reconcile.py中，需要增加下述方法：

```python
    def _selection_name(self):
        methods = super()._selection_name()
        methods += [
            ('mass.reconcile.advanced.transaction_ref',
             'Advanced. Partner and Transaction Ref.'),
            ('mass.reconcile.advanced.trans_ref_vs_ref',
             'Advanced. Partner and Transaction Ref. vs Ref.'),
        ]
        return methods
```


## 原帖外链配图

![[2-ocaaccount-mass-reconcile-transactio-x194038c2.png]]
<small>原始地址: /web/image/1160/snipaste_20190127_132907.png?access_token=25fa7016-f4df-41a4-be97-cb07500ca739</small>

![[2-ocaaccount-mass-reconcile-transactio-x194038c2.png]]
<small>原始地址: /web/image/1162/snipaste_20190127_132718.png?access_token=14bf90d1-9570-4c67-9e3e-e8a4aa456c98</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
