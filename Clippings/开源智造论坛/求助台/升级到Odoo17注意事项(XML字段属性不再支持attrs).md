---
title: "升级到Odoo17注意事项(XML字段属性不再支持attrs)"
source: "http://www.thinkltd.cn/forum/1/odoo17-xmlattrs-3819"
forum: "求助台"
author: "肖相扶"
published: 2023-12-09
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 升级到Odoo17注意事项(XML字段属性不再支持attrs)

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2023-12-09
> <http://www.thinkltd.cn/forum/1/odoo17-xmlattrs-3819>

XML的字段属性不再支持attrs，invisible, readonly等属性支持复杂的关系表达式。

例如下述 attrs的写法，在Odoo17.0中直接将条件表达式写在invisible上即可。

以前版本的写法(attrs属性)：

attrs="{'invisible': ['|', '|', ('validated', '=', True), ('rejected', '=', True), ('review_ids', '=', [])]}"

Odoo17.0的写法如下：

invisible ="validated == True or rejected == True or not review_ids"

也可以写成如下：

invisible ="validated or rejected or not review_ids"

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
