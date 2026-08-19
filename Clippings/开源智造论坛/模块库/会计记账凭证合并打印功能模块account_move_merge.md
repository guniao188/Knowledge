---
title: "会计记账凭证合并打印功能模块account_move_merge"
source: "http://www.thinkltd.cn/forum/2/account-move-merge-3607"
forum: "模块库"
author: "肖相扶"
published: 2025-01-12
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 会计记账凭证合并打印功能模块account_move_merge

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2025-01-12
> <http://www.thinkltd.cn/forum/2/account-move-merge-3607>

【20250112升级到18.0】OSCG_Git\18.0\extra-addons\account_move_merge

模块位置：[https://gitlab.com/oscg-china/extra-addons/-/tree/16.0/account_move_merge](https://gitlab.com/oscg-china/extra-addons/-/tree/16.0/account_move_merge)

【模块功能】

1.  按中国财税部门要求，企事业单位的会计凭证必须打印存档。参见  [会计凭证打印/必须全部打印吗/SAP如何打印会计凭证](http://www.thinkltd.cn/forum/1/sap-975)
2.  Odoo中的大部分会计凭证都是系统自动生成，生成的凭证很多、很细，尤其出入库相关的会计凭证。如果将系统自动生成的会计凭证原样打印，则打印量太大，太细，实际工作中行不通
3.  本模块新开发一个“ 打印凭证 ”的表单（account.move.merge），可以按一定的规则将系统原来的会计记账凭证，合并成供打印用的“打印凭证”（原有凭证仍然保留），凭证打印功能在“打印凭证”上完成。增加菜单“会计 --> 会计 --> 打印凭证”显示合并后的打印凭证。
4.  会计凭证模型(account.move)上增加字段account_move_merge_id，记录该凭证被合并到哪个打印凭证。 会计凭证明细模型(account.move.line)上增加字段account_move_merge_line_id记录本明细行被合并到哪个打印凭证的明细行。
5.  本模块新增两个服务器动作，“合并打印凭证”按一定规则将勾选的系统会计凭证，合并成“打印凭证”。“重排凭证字”将勾选的打印凭证的凭证字按日期顺序重排。
6.  系统的总分类账上，科目展开的分录显示，也改成了打印凭证的分录，而不是系统原来的会计凭证分录。即如果该 会计凭证明细行(account.move.line)被合并了，则显示合并后的打印明细行，而不是自身明细行。多条凭证明细行被合并为一条打印明细行的情况，打印明细行只会显示一次。

【功能截图】

![[2-account-move-merge-3607-7d8f9dce.png]]

![[2-account-move-merge-3607-d28f7a12.png]]

![[2-account-move-merge-3607-d329af3a.png]]

![[2-account-move-merge-3607-403ab36f.png]]

## 补充/答案 1

合并打印凭证的服务器动作参考代码，代码中的注释详细讲解了合并逻辑。

    #action = records.action_multi_update_account_merge()

    #会计记账凭证合并打印。合并策略说明：
    #出入库凭证(stock_move_id字段有值, 且对应stock_move的picking_id字段有值)：按picking_id、会计科目合并到一个打印凭证。合并后的凭证name取picking的name
    #生产领料凭证（stock_move_id字段有值, 且对应stock_move的raw_material_production_id字段有值）：按raw_material_production_id、会计科目合并到一个打印凭证。合并后的凭证name取picking的name
    #客户结算单和供应商账单等（move_type != 'entry'的凭证）：同一个记账凭证按会计科目合并到打印凭证。合并后的凭证name取原凭证name
    #银行收付凭证（日记账为现金或银行类型）：同 move_type != 'entry'的凭证
    #生产入库类凭证（stock_move_id字段有值, 且对应stock_move的production_id字段有值）：同 move_type != 'entry'的凭证
    #库存盘点凭证(stock_move_id字段有值，且对应stock_move的picking_id、raw_material_production_id字段都没值)：不同记账凭证按科目合并到一个打印凭证。合并后的凭证name日期最早的凭证的name
    #其他记账凭证(move_type == 'entry', stock_move_id字段无值)：不同记账凭证按科目合并到一个打印凭证。合并后的凭证name日期最早的凭证的name
    #
    #by_key: 'picking', 'production', 'not_entry', 'move', 'other'
```python
    def merge_by_key(account_move_ids, by_key):
      res_merge_ids = env['account.move.merge']
      to_merge = {}
      first_move = account_move_ids and account_move_ids[0]
      if by_key in ['move', 'other']:
        for am in account_move_ids:
          if am.date < first_move.date:
            first_move = am

      for am in account_move_ids:
        if by_key == 'picking':
          merge_key = am.stock_move_id.picking_id
        elif by_key == 'production':
          merge_key = am.stock_move_id.raw_material_production_id
        elif by_key == 'not_entry':
          merge_key = am
        elif by_key in ['move', 'other']:
          merge_key = first_move

        if not to_merge.get(merge_key, False):
          to_merge[merge_key] = {'account_moves': env['account.move']}
        to_merge[merge_key]['account_moves'] |= am

        for line in am.line_ids:
          if not to_merge[merge_key].get(line.account_id, False):
            to_merge[merge_key][line.account_id] = env['account.move.line']
          to_merge[merge_key][line.account_id] |= line

      for merge_key, amls in to_merge.items():
        dt = max(amls['account_moves'].mapped("date"))
        journal_id = amls['account_moves'][0].journal_id
        company_id = amls['account_moves'][0].company_id
        ref = False
        if by_key in ['not_entry', 'move', 'other']:
          ref = merge_key.ref

        origin = False
        if by_key in ['picking','production']:
          origin = "%s%s" % (merge_key.origin and "%s:" % merge_key.origin or '', merge_key.name)
        user_id = env.user
        vals = {
          'name': merge_key.name,
          'journal_id': journal_id.id,
          'date': dt,
          'origin': origin,
          'ref': ref,
          'user_id': user_id.id,
          'company_id': company_id.id,
        }
        merge_id = env['account.move.merge'].create(vals)
        amls['account_moves'].write({'account_move_merge_id': merge_id.id})
        res_merge_ids |= merge_id

        for acc, lines in amls.items():
          if acc == 'account_moves':
            continue
          debit = sum(lines.mapped('debit'))
          credit = sum(lines.mapped('credit'))
          name = merge_key.name
          names = list(set(lines.mapped('name')))
          if len(names) == 1:
            name = names[0]
          line_vals ={
            'account_id': acc.id,
            'name': name,
            'date': dt,
            'debit': debit,
            'credit': credit,
            'balance': debit - credit,
            'journal_id': journal_id.id,
            'merge_id': merge_id.id,
            'company_id': acc.company_id.id,
          }
          merge_line_id = env['account.move.merge.line'].create(line_vals)
          lines.write({'account_move_merge_line_id': merge_line_id.id})

      return res_merge_ids

    def merge_with_stock_move(account_move_ids):
      res_merge_ids = env['account.move.merge']

      return res_merge_ids

    def merge_others(account_move_ids):
      res_merge_ids = env['account.move.merge']

      return res_merge_ids

    def account_move_merge():
      error_moves = records.filtered(lambda s: s.account_move_merge_id)
      if error_moves:
        raise UserError("您勾选了合并过打印凭证的凭证【%s】。" % (error_moves, ) )

      merged_ids = env['account.move.merge']
```

      #出入库凭证
```python
      moves_picking = records.filtered(lambda s: s.stock_move_id and s.stock_move_id.picking_id)
      merged_ids = merged_ids | merge_by_key(moves_picking, 'picking')
      records_left = records - moves_picking
```

      #生产领料凭证
```python
      moves_production = records_left.filtered(lambda s: s.stock_move_id and s.stock_move_id.raw_material_production_id)
      merged_ids = merged_ids | merge_by_key(moves_production,  'production')
      records_left = records_left - moves_production
```

      #Invoice、收付款、成品入库类凭证
```python
      moves_not_entry = records_left.filtered(lambda s: (s.move_type != 'entry') or (s.journal_id.type in ['bank', 'cash']) or (s.stock_move_id and s.stock_move_id.production_id))
      merged_ids = merged_ids | merge_by_key(moves_not_entry,  'not_entry')
      records_left = records_left - moves_not_entry
```

      #库存盘点类凭证
```python
      moves_inventory = records_left.filtered(lambda s: s.stock_move_id)
      merged_ids = merged_ids | merge_by_key(moves_inventory,  'move')
      records_left = records_left - moves_inventory
```

      #其他凭证
```python
      merged_ids = merged_ids | merge_by_key(records_left,  'other')

      res = {
        'name': '合并打印凭证',
        'type': 'ir.actions.act_window',
        'res_model': 'account.move.merge',
      }
      res.update({
          'view_mode': 'list,form',
          'domain': [('id', 'in', merged_ids.ids)],
      })
      return res

    action = account_move_merge()
    a
```

打印凭证字重排的服务器动作，代码注释详细介绍了重排逻辑。

    #打印凭证的name字段（凭证字）重新排序，排序处理如下：
    #1) 勾选的打印凭证，按date日期顺序排序,日期相同按id排序
    #2) 取第一个凭证的name字段（凭证字），提取凭证字中的数字。如果提取不到数字，则报错。
    #3) 其他凭证的name字段，以第一个为基准，自动加1 生成
    #
```python
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    def resequence_name(merge_ids):
      if not merge_ids:
        return
      new_merge_ids = [(m, m.date) for m in merge_ids]
      new_merge_ids.sort(key=lambda m: "%s %10d" % (m[1], m[0].id))

      first_name = new_merge_ids[0][0].name
      size = len(first_name)
      size0 = size-1
      if first_name[size0] not in numbers:
        raise UserError("第一个凭证【%s】的凭证字末尾不是数字！" % first_name)

      while first_name[size0] in numbers:
        size0 = size0 - 1
        if size0 == 0:
          break
      first_pre = first_name[0:size0+1]
      first_seq = first_name[size0+1:size]
      seq_len = len(first_seq)
      first_seq = int(first_seq)

      seq = first_seq
      for m in new_merge_ids[1:]:
        seq = seq + 1
        ss = "%s" % seq
        while len(ss) < seq_len:
          ss = '0' + ss
        new_name = "%s%s" % (first_pre, ss)
        m[0].write({'name': new_name})

    resequence_name(records)
```

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
