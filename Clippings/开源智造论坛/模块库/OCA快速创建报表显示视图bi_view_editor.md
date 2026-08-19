---
title: "OCA快速创建报表显示视图bi_view_editor"
source: "http://www.thinkltd.cn/forum/2/ocabi-view-editor-3005"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA快速创建报表显示视图bi_view_editor

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocabi-view-editor-3005>

模块链接：

BI View Editor is a tool integrated in Odoo that allows users define and execute their own reports without the need to code.

Purpose:

- The BI View Editor is used to create reports not already contained in the standard Odoo, combining data from existing sources.
- It has been designed to be used by users with little or no knowledge of the technical architecture of Odoo. Users visually link business objects and select the fields to visualize.
- The BI View Editor offers users different types of representations, including tree, graph, pivot views.
-

## [Usage](https://github.com/OCA/reporting-engine/tree/11.0/bi_view_editor#id1)

To graphically design your analysis data-set:

- From the Dashboards menu, select "Custom BI Views"
- Browse trough the business objects in the Query tab
- Pick the interesting fields (Drag & Drop)
- For each selected field, right-click on the Options column and select whether it's a row, column or measure; if you want to remove the field from the list view, unflag the checkbox ´List´ in the Options column
- Save and click "Generate BI View"
- Click "Open BI View" to view the result
- If module Dashboard (board) is installed, the standard "Add to My Dashboard" functionality would be available
- Click "Create a menu" to create a new menu item directly linked to your new BI view (this feature is available in developer mode); when the BI view is reset back to draft this menu will be removed, and you will need to re-create the menu entry.


## 原帖外链配图

![[2-ocabi-view-editor-3005-x194038c2.png]]
<small>原始地址: /web/image/1431/snipaste_20190303_171337.png?access_token=11fda5ad-f9d3-48c5-a2f3-078924ab6853</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
