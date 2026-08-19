---
title: "Odoo14电子表格应用原理documents_spreadsheet"
source: "http://www.thinkltd.cn/forum/1/odoo14documents-spreadsheet-754"
forum: "求助台"
author: "肖相扶"
published: 2024-04-09
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo14电子表格应用原理documents_spreadsheet

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-04-09
> <http://www.thinkltd.cn/forum/1/odoo14documents-spreadsheet-754>

【原理解析】

1) Odoo14.0中，安装documents_spreadsheet模块后，所有透视表视图(Pivot)，都可以“Insert in spreadsheet”, Insert in spreadsheet时候，系统根据Pivot视图上的筛选和分组条件，在js中创建一个 pivot data cach数据，spreadsheet在线表格显示的数据，来自该cach数据
2) spreadsheet上，还可以增加筛选条件，系统按筛选条件过滤数据，刷新pivot data cach数据
3) spreadsheet上，可以使用 pivot() 函数，从pivot data cach中提取数据显示在表格上
4) spreadsheet上，可以设置格式条件，符合条件的数据格，按指定的格式（颜色、字体等）显示

![[1-odoo14documents-spreadsheet-754-2208ac24.png]]

【功能截图】

![[1-odoo14documents-spreadsheet-754-305a6e12.png]]

![[1-odoo14documents-spreadsheet-754-41569683.png]]

![[1-odoo14documents-spreadsheet-754-de63d776.png]]

![[1-odoo14documents-spreadsheet-754-fd59b7d6.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
