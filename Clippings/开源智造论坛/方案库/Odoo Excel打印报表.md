---
title: "Odoo Excel打印报表"
source: "http://www.thinkltd.cn/forum/3/odoo-excel-3600"
forum: "方案库"
author: "肖相扶"
published: 2022-12-17
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/方案库
---

# Odoo Excel打印报表

> [!info] 来源
> 开源智造论坛 · 方案库 | 作者:肖相扶 | 2022-12-17
> <http://www.thinkltd.cn/forum/3/odoo-excel-3600>

report_xlsx模块在Odoo的打印报表上，增加了一种新的输出格式（SLSX，即Excel文件）。其打印处理逻辑是：

报表定义上，上传Excel格式的打印报表模板文件

1.  报表定义上，在线编写python代码，获取数据，并写入Excel文件对应格子里
2.  当用户点击打印时候，系统复制Excel报表模板文件，调用在线的Python代码，输出Excel文件
3.  该模块基于Python库openpyxl 操作Excel文件。在线编写报表python代码时候，内置了 openpyxl 的 workbook, worksheet, style 对象，可以灵活操作Excel格式。

report_xlsx Excel打印报表的优劣势：

1.  优点是，和QWeb报表相比，直接用Excel模板作为输出格式，打印格式简单
2.  缺点是，数据的获取，Excel数据填充，Excel格式调整等，需要在线python编程实现，需要一定的python程序基础。
3.  另外一个缺点是，不能自动分页。分页输出的情况，系统输出Excel打印报表，自己手动调整Excel的分页输出。
4.  销售订单、采购订单之类单据，一般一次只会打印一个，可以用此报表打印技术。拣货单之类的，往往一次要打印多张拣货单，不适合用此技术（而应该用QWeb打印报表技术）。
5.  一些带格式的统计报表，如月报或年报，也可以用此技术（qweb-text报表虽然也可以输出数据，但不能带格式）。如下面链接的示例 report_xlsx_msr 即为年报报表。

report_xlsx模块参考：

1.  [二开Excel/Docx word打印报表模块report_xlsx、report_docx](http://www.thinkltd.cn/forum/2/excel-docx-wordreport-xlsxreport-docx-2987)
2.  [Excel汇总报表示例模块report_xlsx_msr](http://www.thinkltd.cn/forum/2/excelreport-xlsx-msr-3550)

openpyxl技术资料参考：

1.  [python之openpyxl模块（最全总结 足够初次使用） - 火星小编 - 博客园 (cnblogs.com)](https://www.cnblogs.com/programmer-tlh/p/10461353.html)
2.  [openpyxl - A Python library to read/write Excel 2010 xlsx/xlsm files — openpyxl 3.0.10 documentation](https://openpyxl.readthedocs.io/en/stable/)

---

相关:[[Clippings/开源智造论坛/方案库/00-方案库索引.md|← 方案库索引]]
