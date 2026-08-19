---
title: "BI报表解决方案（待完善）"
source: "http://www.thinkltd.cn/forum/3/bi-3604"
forum: "方案库"
author: "杨浔波"
published: 2022-12-22
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/方案库
---

# BI报表解决方案（待完善）

> [!info] 来源
> 开源智造论坛 · 方案库 | 作者:杨浔波 | 2022-12-22
> <http://www.thinkltd.cn/forum/3/bi-3604>

### 引言

Odoo针对BI报表解决方案有以下解决方案：

- documents_spreadsheet (odoo13-15企业版)的标准功能应用
- ks_dashboard_ninja：[https://apps.odoo.com/apps/modules/16.0/ks_dashboard_ninja/](https://apps.odoo.com/apps/modules/16.0/ks_dashboard_ninja/)
- Odoo16+ dashboard的标准功能应用
- bi_sql_editor：[https://apps.odoo.com/apps/modules/15.0/bi_sql_editor/](https://apps.odoo.com/apps/modules/15.0/bi_sql_editor/)
- 二次定制开发

### documents_spreadsheet(13-15)使用指南：

首先明确一点，不能作为自定义图表展示，无法修改参数透视标题。可以通过图表插入已有的报表样式进入。能用的是取值，做公式，这里可以以销售提成这样的场景为例，以后类似这样的需求可以通过这种方案实现。要求未来开发在视图层面，多开发一个透视图视图。因为Odoo spreadsheet功能应用必须先从透视图数据插入才可以有效的成为数据源，切记切记！

第一步，先切换透视图视图

![[3-bi-3604-bccc9543.png]]

第二步插入spreadsheet，进入spreadsheet编辑界面。增加sheet2，设置提成参数

![[3-bi-3604-40fde4d4.png]]

第三步，增加字段设置公示。

![[3-bi-3604-e639f413.png]]

第四步增加筛选器，设置条件。

![[3-bi-3604-f260e91a.png]]

之后每次打开报表，都可以通过筛选器进行日期过滤，看到每月的动态销售提成数据。

![[3-bi-3604-a6f1c832.png]]

---

相关:[[Clippings/开源智造论坛/方案库/00-方案库索引.md|← 方案库索引]]
