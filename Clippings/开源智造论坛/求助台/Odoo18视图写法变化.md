---
title: "Odoo18视图写法变化"
source: "http://www.thinkltd.cn/forum/1/odoo18-4003"
forum: "求助台"
author: "葛忠彪"
published: 2024-12-09
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo18视图写法变化

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:葛忠彪 | 2024-12-09
> <http://www.thinkltd.cn/forum/1/odoo18-4003>

1.tree视图叫法改变，统一改成list，例如动作里的视图类型，tree视图本身，form中的one2many调取的tree视图部分

2.消息附件部分代码简化，如下图

![[1-odoo18-4003-30067aea.png]]

3.many2many字段增加了一个属性，可以点击标签后弹窗编辑此标签
options="{'edit_tags': True}"
4.选项型selection字段 黑名单机制 ，在视图里机上 widget="filterable_selection" options="{'blacklisted_values': ['键','键','键']}"  ，即此视图中这个选项型字段中，不出现键对应的选项

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
