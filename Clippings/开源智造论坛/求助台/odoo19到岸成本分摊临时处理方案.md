---
title: "odoo19到岸成本分摊临时处理方案"
source: "http://www.thinkltd.cn/forum/1/odoo19-4091"
forum: "求助台"
author: "姚代娣"
published: 2025-11-19
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# odoo19到岸成本分摊临时处理方案

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:姚代娣 | 2025-11-19
> <http://www.thinkltd.cn/forum/1/odoo19-4091>

背景：odoo19版本的到岸成本的逻辑为仅分摊有剩余库存产品，但未处理已消耗产品，而是直接跳过。虽然在估值调整处有显示但计价凭证不会产生。临时处理方案为参考18版本的代码。

路径：stoc_landed_costs/models/stock_landed_cost.py

注释372、373行：

    #        if not remaining_qty:
    #            return AccountMoveLine

    diff = self.additional_landed_cost * (remaining_qty / self.quantity)

修改成：diff = self.additional_landed_cost

在 return AccountMoveLine 上面增加以下代码：

    #        增加以下代码
            qty_out = self.quantity - remaining_qty
            # Create account move lines for quants already out of stock
```python
            if qty_out > 0:
                name_text = _("%(product)s: %(quantity)s already out", product=self.name, quantity=qty_out)
                already_out_account_id = self.env['account.journal'].search([('type','=','purchase')],limit=1).default_account_id.id
                debit_line = dict(base_line,
                                  name=name_text,
                                  quantity=0,
                                  account_id=already_out_account_id)
                credit_line = dict(base_line,
                                   name=name_text,
                                   quantity=0,
                                   account_id=debit_account_id)
                diff = diff * qty_out / self.quantity
                if diff > 0:
                    debit_line['debit'] = diff
                    credit_line['credit'] = diff
                else:
```

                    # negative cost, reverse the entry
```python
                    debit_line['credit'] = -diff
                    credit_line['debit'] = -diff
                AccountMoveLine.append([0, 0, debit_line])
                AccountMoveLine.append([0, 0, credit_line])
```

![[1-odoo19-4091-db663b49.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
