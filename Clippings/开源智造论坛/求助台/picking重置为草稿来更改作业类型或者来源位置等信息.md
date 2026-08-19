---
title: "picking重置为草稿来更改作业类型或者来源位置等信息"
source: "http://www.thinkltd.cn/forum/1/picking-809"
forum: "求助台"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# picking重置为草稿来更改作业类型或者来源位置等信息

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/picking-809>

服务器动作代码示例：

for record in records:
 if record.state not in ['done', 'cancel']:
```python
    record.do_unreserve()
    record.write({'state': 'draft'})
    if record.move_ids_without_package:
     for move in record.move_ids_without_package:
      move.write({'state': 'draft'})
    if record.move_line_ids_without_package:
     for move_line in record.move_line_ids_without_package:
      move_line.write({'state': 'cancel'})
```

-----------------------如果对方重置为草稿，还需要解除move的上下游单据强绑定关系，可以增加代码，重置示例：

for record in records:
 if record.state not in ['done']:
```python
    record.do_unreserve()
    record.write({'state': 'draft'})
    if record.move_ids_without_package:
     for move in record.move_ids_without_package:
      move.write({'state': 'draft'})
      del_ids = []
      for mv in move.move_orig_ids:
        del_ids.append( (3,mv.id) )
      move.write({'move_orig_ids': del_ids})
      dest_ids = []
      for de in move.move_dest_ids:
        dest_ids.append( (3,de.id) )
      move.write({'move_dest_ids': dest_ids})
    if record.move_line_ids_without_package:
     for move_line in record.move_line_ids_without_package:
      move_line.write({'state': 'cancel'})
```

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
