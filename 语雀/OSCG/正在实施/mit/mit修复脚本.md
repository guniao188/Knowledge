---
title: "mit修复脚本"
client: mit
type: 项目文档
phase: 实施期
yuque_url: "https://www.yuque.com/xinsuixiaoyao-degek/klxky6/gmvuii2rcg8lanfo"
yuque_slug: "gmvuii2rcg8lanfo"
tags: [Odoo, 实施期, 客户/mit, 技术, 正在实施]
created_at: "2026-06-04T02:37:25.000Z"
updated_at: "2026-06-08T07:35:19.000Z"
published_at: "2026-06-07T09:01:20.000Z"
---
# mit修复脚本

收货

```
for record in records:
    record.write({'picking_type_id':9})
```

发货

```
for record in records:
    record.write({'picking_type_id':10})
```

制造

```
for record in records:
    record.write({'picking_type_id':17})
```

stock move

```
for record in records:
    record.write({'location_id':record.picking_type_id.default_location_src_id.id})
    record.write({'location_dest_id':record.picking_type_id.default_location_dest_id.id})
```
