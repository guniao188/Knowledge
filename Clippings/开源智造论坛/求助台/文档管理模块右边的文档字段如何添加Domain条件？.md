---
title: "文档管理模块右边的文档字段如何添加Domain条件？"
source: "http://www.thinkltd.cn/forum/1/domain-795"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 文档管理模块右边的文档字段如何添加Domain条件？

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/domain-795>

【问题】

如下图，文档模块右边的文档相关字段，如 Contact 字段，可以选择所有的Partner，可否添加Domain条件限制只能选择符合条件的Partner ？

![[1-domain-795-ce22c64a.png]]

【答案】

文档模块右边的文档信息区域不是通常的 XML 格式的视图，是 js 实现的界面，实现代码参见 documents\static\src\js\documents_inspector.js   中的方法 _renderField: function (fieldName, options)

因为是JS实现的，无法在界面XML上添加Domain条件。一种变通的方法是，写一个小模块，在后台py文件中，字段定义上增加 domain 条件。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
