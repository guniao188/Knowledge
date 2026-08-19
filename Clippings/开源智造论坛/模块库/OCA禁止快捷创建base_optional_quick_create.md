---
title: "OCA禁止快捷创建base_optional_quick_create"
source: "http://www.thinkltd.cn/forum/2/ocabase-optional-quick-create-2580"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA禁止快捷创建base_optional_quick_create

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocabase-optional-quick-create-2580>

模块链接：

ir.model表单上增加字段“Avoid Quick Create”，勾选则在Many2One的下拉框里面，不允许Create对象。

This module allows to avoid to *quick create* new records, through many2one fields, for a specific model. You can configure which models should allow *quick create*. When specified, the *quick create* option will always open the standard create form.

Got the idea from [https://twitter.com/nbessi/status/337869826028605441](https://twitter.com/nbessi/status/337869826028605441)

###

### Usage

To use this module, you need to:

> - go into the menu of *ir_model*,
> - select the model for which you want to disable the quick create option,
> - enable the option *Avoid quick create*.


## 原帖外链配图

![[2-ocabase-optional-quick-create-2580-x194038c2.png]]
<small>原始地址: /web/image/869/snipaste_20190119_235511.png?access_token=ad995d17-a19a-40d3-bb9a-d8a20c81e313</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
