---
title: "OCA颜色选择控件web_widget_color"
source: "http://www.thinkltd.cn/forum/2/ocaweb-widget-color-2834"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA颜色选择控件web_widget_color

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaweb-widget-color-2834>

模块链接：

This module aims to add a color picker to Odoo.

It's a [jsColor](http://jscolor.com/) lib integration.

## Features

- The picker allow the user to quickly select a color on edit mode

```python
  Note

  Notice how html code and the background color is updating when selecting a color.
```

- Display the color on form view when you are not editing it

- Display the color on list view to quickly find what's wrong!

## Usage

You need to declare a char field:

```python
    color = fields.Char(
        string="Color",
        help="Choose your color"
    )
```

In the view declaration, put widget='color' attribute in the field tag:

```python
    ...

            ...

            ...

    ...

            ...

            ...

    ...
```

Widget Options:

    - readonly_mode
        - 'default' > Color Box + text
        - 'color' > Only Color Box
        - 'text' > Only Text
```python
    ...

            ...

            ...

    ...
```

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
