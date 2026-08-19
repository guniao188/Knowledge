---
title: "odoo15删除凭证"
source: "http://www.thinkltd.cn/forum/1/odoo15-965"
forum: "求助台"
author: "葛忠彪"
published: 2023-07-17
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# odoo15删除凭证

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:葛忠彪 | 2023-07-17
> <http://www.thinkltd.cn/forum/1/odoo15-965>

即使重置为草稿也无法删除凭证，因为posted_before字段为True的无法删除，用服务器动作批量重置后，可以删除凭证

```python
for i in records:

  a = ''

  if i.state == 'posted':

    i.button_draft()

  i.write({'name':a})

  i.write({'posted_before':False})
```

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
