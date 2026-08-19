---
title: "Smile计算型字段api.depends增强依赖变更smile_api_depends_filter"
source: "http://www.thinkltd.cn/forum/2/smileapi-dependssmile-api-depends-filter-3052"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Smile计算型字段api.depends增强依赖变更smile_api_depends_filter

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/smileapi-dependssmile-api-depends-filter-3052>

模块链接：

This module allows to filter records to recompute by specifying a domain for a trigger.

To work, this module must be defined as a wide module.

**Example**

```python
    @api.depends(
        ('product_id.lst_price', [('invoice_id.state', '=', 'draft')]))

    此定义的意思是，本计算型方法，条件 [('invoice_id.state', '=', 'draft')] 时候，product_id.lst_price发生变化时候，重新计算。
    计算型字段的依赖定义中，增加了 domain条件定义功能。
```

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
