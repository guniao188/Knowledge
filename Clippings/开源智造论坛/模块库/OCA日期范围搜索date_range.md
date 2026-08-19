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


## 原帖外链配图

![[2-ocadate-range-2568-x83b28f41.png]]
<small>原始地址: https://raw.githubusercontent.com/OCA/server-tools/10.0/date_range/static/description/date_range_type_create.p</small>

![[2-ocadate-range-2568-x62e05893.png]]
<small>原始地址: https://raw.githubusercontent.com/OCA/server-tools/10.0/date_range/static/description/date_range_create.png</small>

![[2-ocadate-range-2568-x5ba3baa6.png]]
<small>原始地址: https://raw.githubusercontent.com/OCA/server-tools/10.0/date_range/static/description/date_range_wizard.png</small>

![[2-ocadate-range-2568-xb3f011fc.png]]
<small>原始地址: https://raw.githubusercontent.com/OCA/server-tools/10.0/date_range/static/description/date_range_wizard_result</small>

![[2-ocadate-range-2568-x93732aa1.png]]
<small>原始地址: https://raw.githubusercontent.com/OCA/server-tools/10.0/date_range/static/description/date_range_type_as_filte</small>

![[2-ocadate-range-2568-xf1c49df5.png]]
<small>原始地址: https://raw.githubusercontent.com/OCA/server-tools/10.0/date_range/static/description/date_range_as_filter.png</small>

![[2-ocadate-range-2568-xb2209c38.png]]
<small>原始地址: https://raw.githubusercontent.com/OCA/server-tools/10.0/date_range/static/description/date_range_as_filter_res</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
