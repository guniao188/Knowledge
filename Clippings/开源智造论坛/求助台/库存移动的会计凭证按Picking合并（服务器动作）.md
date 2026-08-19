---
title: "库存移动的会计凭证按Picking合并（服务器动作）"
source: "http://www.thinkltd.cn/forum/1/picking-886"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 库存移动的会计凭证按Picking合并（服务器动作）

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/picking-886>

【业务背景】

1.  Odoo中，入库、出库时候，每一条库存移动都会生成一个会计凭证。同一个出入库单（Picking），会有多个会计凭证；

2.  大量的会计凭证，给凭证的打印装订带来麻烦；

3.  本服务器动作按Picking合并库存移动的会计凭证

【服务器动作代码】

![[1-picking-886-11b0ba15.png]]

# 合并同一个Picking的会计凭证。合并逻辑如下：

# 1）同一个Picking的所有会计凭证的明细行，搬移到第一个会计凭证上，而后取消被搬空了的会计凭证；

# 2) 搬移到一起的会计凭证，按会计科目合并明细行（有核销匹配号的不合并），删除被合并的明细行。

```python
picking_dict = {}

for r in records:

  if not r.stock_move_id:

    continue

  picking = r.stock_move_id.picking_id #or r.stock_move_id.production_id

  if not picking_dict.get(picking, False):

    picking_dict[picking] = r

  else:

    entry_id = picking_dict[picking].id

    r.line_ids.write({"move_id": entry_id})

    r.stock_valuation_layer_ids.write({"account_move_id": entry_id})

    r.write({"state": 'cancel'})
```

# 同一个会计凭证上的明细行，如果没有核销/部分核销号，则按会计科目合并到一个明细行，被合并的明细行金额设置为0，而后删除之。

for k, move in picking_dict.items():

```python
  acc_dict = {}

  for l in move.line_ids:

    if l.matching_number:

      continue

    if not acc_dict.get(l.account_id, False):

      acc_dict[l.account_id] = l

    else:

      mv_line = acc_dict[l.account_id]

      credit = mv_line.credit + l.credit

      debit = mv_line.debit + l.debit

      amount_currency = mv_line.amount_currency + l.amount_currency
```

      #mv_line.write({"credit": credit, "debit": debit})

      #l.write({"credit":0.0, "debit": 0.0})

```python
      env.cr.execute("update account_move_line set amount_currency=%s, credit=%s, debit=%s where id=%s", [amount_currency, credit, debit, mv_line.id])

      env.cr.execute("update account_move_line set amount_currency=0.0, credit=0.0, debit=0.0 where id=%s", [l.id])

  env.cr.execute("delete from account_move_line where move_id = %s and credit=0.0 and debit=0.0 and amount_currency=0.0", [move.id])
```

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
