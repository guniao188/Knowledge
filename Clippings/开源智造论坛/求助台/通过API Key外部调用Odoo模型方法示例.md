---
title: "通过API Key外部调用Odoo模型方法示例"
source: "http://www.thinkltd.cn/forum/1/api-keyodoo-3906"
forum: "求助台"
author: "肖相扶"
published: 2024-03-27
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 通过API Key外部调用Odoo模型方法示例

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-03-27
> <http://www.thinkltd.cn/forum/1/api-keyodoo-3906>

1.  在用户偏好画面为用户创建API Key。可以创建多个Key，分发给不同的外部用户使用。

![[1-api-keyodoo-3906-359e7fdb.png]]

2.  XMLRPC调用中，用API KEY替换用户密码，调用Odoo各种模型方法，如下面代码示例。

    import xmlrpc.client
    #odoo_server_url = 'https://demo4.odoo.com'
```python
    odoo_server_url = 'http://localhost:8769'
    odoo_db="O17_E01"
    username="admin"
    odoo_api_key="b3a9d279f0095f1583f88d733369c913ef466f2c"

    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(odoo_server_url))
    uid = common.authenticate(odoo_db, username, odoo_api_key, {})
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(odoo_server_url))
    result=models.execute_kw(odoo_db, uid, odoo_api_key, 'res.partner', 'search_read', [[], ['name']])
    print(result)
```

a

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
