---
title: "Odoo中配置实现电子报关单(Excel文件)的导出"
source: "http://www.thinkltd.cn/forum/3/odoo-excel-3705"
forum: "方案库"
author: "穆宇涵"
published: 2023-04-25
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/方案库
---

# Odoo中配置实现电子报关单(Excel文件)的导出

> [!info] 来源
> 开源智造论坛 · 方案库 | 作者:穆宇涵 | 2023-04-25
> <http://www.thinkltd.cn/forum/3/odoo-excel-3705>

模块链接：[server-tools/sql_export at 14.0 · OCA/server-tools (github.com)](https://github.com/OCA/server-tools)

模块包括 excel_import_export，excel_import_export_demo

注意，SVN有改善后的模块（增加带格式插入行） OSCG_SVN\odoo_ecommerce\14.0SRC\Excel报表\excel_import_export
【**20220507 15.0升级版**】OSCG_SVN\odoo_ecommerce\15.0SRC\报表工具\excel_import_export

【**20220806 Bug修正**】明细行存在合并列的情况，报错 TypeError: 的问题修正。

【模块功能】

1.  Excel导入：指定Excel的单元格 和 Odoo模型(订单)的字段对应关系，而后自动数据导入

2.  Excel导出：指定Excel的单元格 和 Odoo模型(订单)的字段对应关系，而后自动数据导出。可以导出为Excel打印格式报表

3.  注意，该模块导出Excel时候，需要创建一个临时Excel文件，需要指定临时文件目录，Odoo系统参数中指定键值 path_temp_file 设置临时文件目录。如果不设置，系统默认用 /tmp 。在Windows上，必须设置，因为Windows没有 /tmp 文件目录

![[3-odoo-excel-3705-b8d99575.png]]

【功能截图】

![[3-odoo-excel-3705-5f841849.png]]

![[3-odoo-excel-3705-8380d2d6.png]]

![[3-odoo-excel-3705-42ffc807.png]]

![[3-odoo-excel-3705-1d288989.png]]

---

相关:[[Clippings/开源智造论坛/方案库/00-方案库索引.md|← 方案库索引]]
