---
title: "OCA列表视图增加图像显示控件web_tree_image"
source: "http://www.thinkltd.cn/forum/2/ocaweb-tree-image-2840"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA列表视图增加图像显示控件web_tree_image

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaweb-tree-image-2840>

模块链接：

This module defines a tree image widget, to be used with either binary fields or (function) fields of type character. Use `widget='image'` in your view definition. Optionally, set a `width` attribute. Default width is 30px.

If you use the widget with a character field, the content of the field can be any of the following:

- The absolute or relative location of an image. For example, "//static/src/img/youricon.png"
- A standard icon from the web distribution, without path or extension, For example, 'gtk-open'
- A dynamic image in a data url base 64 format. Prefix with 'data:image/png;base64,'

###

### Usage

Set the attribute `widget=image` in a `field` tag in a tree view. You can also set `height=` to set the height the image will have. Note that this just sets the CSS `max-height` attribute, if you want to make the server return a resized, maybe to save data by making it return a smaller one or to have uniform images, use the `resize=","` attribute.

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
