---
title: "Excel汇总报表示例模块report_xlsx_msr"
source: "http://www.thinkltd.cn/forum/2/excelreport-xlsx-msr-3550"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Excel汇总报表示例模块report_xlsx_msr

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/excelreport-xlsx-msr-3550>

模块链接：OSCG_SVN\odoo_ecommerce\15.0SRC\报表工具\report_xlsx_msr

【模块功能】

1.  汇总销售出库的Stock Move的数据，按 客户、产品、月度显示出库数量、出库金额（以售价计）

2.  该模块依赖模块 report_xlsx ，利用该模块的Excel 打印报表的功能，输出 Excel汇总报表

3.  模块安装后，新增了一个打印报表 “Monthly Summary Report”，该打印报表中，需要手工上传一个 Excel的模板文件。模板文件参见 模块中的文件 report_xlsx_msr\static\description\Monthly Summary Report.xlsx

4.  模块安装后，新增了一个URL类型的动作（模型 ir.actions.act_url）“Monthly Summary Report”。动作中的url字段默认值“/report/xlsx/mmc.msr/1?year=2022”，其中 year=2022 表示抽取2022年的数据。如果需要抽取其他年份的数据，建议为每年创建一个URL动作，以及对应的菜单。或者，直接在浏览器地址栏输入报表打印的URL：/report/xlsx/mmc.msr/1?year=打印年份

5.  参照后面截图的代码，了解如何设置Excel的格式，包括 背景色、字体加粗、居中等。

【功能截图】

![[2-excelreport-xlsx-msr-3550-edbdbe3c.png]]

![[2-excelreport-xlsx-msr-3550-f569ed07.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
