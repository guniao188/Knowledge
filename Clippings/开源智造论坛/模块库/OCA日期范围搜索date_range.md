---
title: "OCA日期范围搜索date_range"
source: "http://www.thinkltd.cn/forum/2/ocadate-range-2568"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA日期范围搜索date_range

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocadate-range-2568>

模块链接：

技术设置里面定义好日期范围，而后在任和一个列表视图上都可以按该日期范围搜索日期。

This module lets you define global date ranges that can be used to filter your values in tree views.

The addon use the daterange method from postgres. This method is supported as of postgresql 9.2

## 补充/答案 1

To configure this module, you need to:

- Go to Settings > Technical > Date ranges > Date Range Types where you can create types of date ranges.

- Go to Settings > Technical > Date ranges > Date Ranges where you can create date ranges.

```python
  It's also possible to launch a wizard from the 'Generate Date Ranges' menu.

  The wizard is useful to generate recurring periods.
```

- Your date ranges are now available in the search filter for any date or datetime fields

```python
  Date range types are proposed as a filter operator

  Once a type is selected, date ranges of this type are porposed as a filter value

  And the dates specified into the date range are used to filter your result.
```

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
