---
title: "OCA多选列表/总是显示搜索更多web_widget_many2many_tags_multi_selection"
source: "http://www.thinkltd.cn/forum/2/oca-web-widget-many2many-tags-multi-selection-2837"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA多选列表/总是显示搜索更多web_widget_many2many_tags_multi_selection

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/oca-web-widget-many2many-tags-multi-selection-2837>

模块链接：

经测试，该模块在Odoo 13.0可以正常安装使用。

13.0增强版SVN位置：OSCG_SVN\odoo_ecommerce\13.0SRC\流程型制造\web_widget_many2many_tags_multi_selection

经测试，该增强版在Odoo14.0可以正常使用。

【功能增强】

Many2one字段下拉框中，Odoo原本的设计是，搜索结果超过7条时候，显示“搜索更多”链接。有时候希望哪怕一条结果也可以点开搜索更多，查看更多字段信息。增强后的模块，字段定义的 options 里面可以增加 'always_search_more':True 让系统始终显示“搜索更多” 。示例：

In a many2many_tags widget when a lot of entries should be selected it's fastidious to select 80% of them. Then you may click on 'search more', but impossible to select several attributes at once.

This module adds a checkbox to this list so multiple entries can be selected at once.

本模块实现 many2many 字段多选列表效果。

使用方法：XML视图定义时候，many2many 的字段定义中，加上 widget="many2many_tags" ，如下例

![[2-oca-web-widget-many2many-tags-multi-selection-2837-a2129e51.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
