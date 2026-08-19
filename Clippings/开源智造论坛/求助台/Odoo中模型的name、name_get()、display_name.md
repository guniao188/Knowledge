---
title: "Odoo中模型的name、name_get()、display_name"
source: "http://www.thinkltd.cn/forum/1/odoonamename-get-display-name-702"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo中模型的name、name_get()、display_name

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoonamename-get-display-name-702>

Odoo模型的 name_get()  及 display_name  字段参考代码： ODOO13\source\odoo\models.py

默认情况，模型的 display_name 字段取值 name_get() 方法，name_get()方法取值 name 字段。但每个模型可以继承 def _compute_display_name() 返回别的显示名称

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
