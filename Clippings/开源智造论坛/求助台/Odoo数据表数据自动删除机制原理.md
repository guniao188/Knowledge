---
title: "Odoo数据表数据自动删除机制原理"
source: "http://www.thinkltd.cn/forum/1/odoo-696"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo数据表数据自动删除机制原理

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo-696>

Odoo模型中，有垃圾数据（过期数据）删除方法：def _gc_messages(self) 。每个模型可以重载该方法，定义自己的过期数据删除机制。例如模型“bus.bus” （代码文件 Odoo\addons\bus\models\bus.py ）中，自动删除创建时间超过100秒的通知消息。

```python
    @api.autovacuum

    def _gc_messages(self):

        timeout_ago = datetime.datetime.utcnow()-datetime.timedelta(seconds=TIMEOUT*2)

        domain = [('create_date', '<', timeout_ago.strftime(DEFAULT_SERVER_DATETIME_FORMAT))]

        return self.sudo().search(domain).unlink()
```

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
