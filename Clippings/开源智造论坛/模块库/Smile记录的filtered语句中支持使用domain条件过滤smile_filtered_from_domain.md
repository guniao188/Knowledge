---
title: "Smile记录的filtered语句中支持使用domain条件过滤smile_filtered_from_domain"
source: "http://www.thinkltd.cn/forum/2/smilefiltereddomainsmile-filtered-from-domain-3087"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Smile记录的filtered语句中支持使用domain条件过滤smile_filtered_from_domain

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/smilefiltereddomainsmile-filtered-from-domain-3087>

模块链接：

This module allows to filter records from a search domain.

**Example with filtered_from_domain:**

```python
    records.filtered_from_domain([
        ('state', '=', 'draft'),
        ('line_ids.product_id.name', '=', 'My product'),
    ])
```

**Example with filtered:**

    records.filtered(lambda r: r.state == 'draft' and line_ids.product_id.name == 'My product')

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
