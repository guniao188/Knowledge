---
title: "OCA客制化异常基类base_exception"
source: "http://www.thinkltd.cn/forum/2/ocabase-exception-2607"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA客制化异常基类base_exception

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocabase-exception-2607>

客制化异常基类。其他模型继承此基类，调用该基类的异常检测方法，如果检测到异常，异常类型写入被检测对象的exception_ids字段，并修改对象状态。示例继承代码：

```python
class PurchaseOrder(models.Model):
    _inherit = ['purchase.order', 'base.exception']
    _name = 'purchase.order'
    _order = 'main_exception_id asc, date_order desc, name desc'

    rule_group = fields.Selection(
        selection_add=[('purchase', 'Purchase')],
        default='purchase',
    )
```

This module provide an abstract model to manage customizable exceptions to be applied on different models (sale order, invoice, ...).

It is not useful for itself. You can see an example of implementation in the 'sale_exception' module. (sale-workflow repository) or 'purchase_exception' module (purchase-workflow repository).


## 原帖外链配图

![[2-ocabase-exception-2607-x194038c2.png]]
<small>原始地址: /web/image/894/snipaste_20190120_122332.png?access_token=47e4fbba-801e-4259-8e67-53d7e0b8cad8</small>

![[2-ocabase-exception-2607-x194038c2.png]]
<small>原始地址: /web/image/896/snipaste_20190120_122320.png?access_token=669673b7-8998-45c6-8346-39a93796f153</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
