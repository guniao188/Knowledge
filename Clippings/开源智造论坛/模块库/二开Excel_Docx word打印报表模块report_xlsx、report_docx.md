---
title: "二开Excel/Docx word打印报表模块report_xlsx、report_docx"
source: "http://www.thinkltd.cn/forum/2/excel-docx-wordreport-xlsxreport-docx-2987"
forum: "模块库"
author: "肖相扶"
published: 2022-12-23
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开Excel/Docx word打印报表模块report_xlsx、report_docx

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-23
> <http://www.thinkltd.cn/forum/2/excel-docx-wordreport-xlsxreport-docx-2987>

Odoo 16.0版本参考  [在线python代码下载Excel报表模块report_xlsx](http://www.thinkltd.cn/forum/2/pythonexcelreport-xlsx-3615)

模块链接：OSCG_SVN\odoo_ecommerce\12.0SRC\report_xlsx    示例：百赛

OSCG_SVN\odoo_ecommerce\13.0SRC\report_xlsx

示例客户代码：魔数、优源环保、拓博脉

**2022年1月23日新增Odoo15.0版本，同时改善Odoo14.0版本：**

OSCG_SVN\odoo_ecommerce\14.0SRC\Excel报表\\report_xlsx    示例客户：泰特，百赛

OSCG_SVN\odoo_ecommerce\14.0SRC\Excel报表\\report_docx

OSCG_SVN\odoo_ecommerce\15.0SRC\报表工具\report_xlsx

OSCG_SVN\odoo_ecommerce\15.0SRC\报表工具\report_docx

1.  report_docx使用Word模板，输出Word格式。Word上以jinja2 为取数据的模板语法，[Jinja语法入门参考这里](https://www.cnblogs.com/dachenzi/p/8242713.html)：https://www.cnblogs.com/dachenzi/p/8242713.html

2.  report_docx的使用案例参考这里：合同管理模块中合同打印模板示例：[合同管理相关模块agreement、agreement_legal](http://www.thinkltd.cn/forum/2/question/agreementagreement-legal-3539)

【**升级到14.0的修改**】

文件OSCG_SVN\odoo_ecommerce\13.0SRC\report_xlsx\models\ir_report.py，修改下述代码行：

report_type = fields.Selection(selection_add=[("xlsx", "XLSX")])  改成  report_type = fields.Selection(selection_add=[("xlsx", "XLSX")], ondelete={'xlsx': lambda recs: recs.write({'report_type': 'txt'})})

![[2-excel-docx-wordreport-xlsxreport-docx-2987-207fbfcb.png]]

原始OCA模块：

OCA模块增加了Excle的打印报表类型，该模块使用python库xlsxwriter及xlrd操作Excel输出。

1.  改造后的模块使用python库 openpyxl，该模块功能如下：

2.  报表定义界面增加Excel模板文件上传(模板文件必须是 .xlsx 为后缀的Excel文件)，增加Excel报表文件取值填充的的python代码字段

3.  报表打印时候，系统加载Excel模板，调用界面写的填值python code，形成报表输出。

4.  如果勾选多个对象打印，系统以第一个WorkSheet为模板，为每一个对象复制一个WorkSheet，WorkSheet的标题取对象的name （如果待打印对象没有name可能会报错）

5.  如果报表定义上填写了 print_report_name ，系统按print_report_name 计算下载的Excel文件名（文件名表达式可用变量 object 和 time 两个），如果没有填写，系统以 report_file 字段作为文件名。如果 report_file 也没填写则下载文件名为 "Odoo.xlsx"

6.

    报表report_name的填写方法

预定义好的可以使用的report_name 有： report_xlsx.sale_order1_xlsx, report_xlsx.sale_order2_xlsx,  report_xlsx.purchase_order1_xlsx, report_xlsx.purchase_order2_xlsx,  report_xlsx.picking1_xlsx, report_xlsx.picking2_xlsx,  report_xlsx.account_invoice1_xlsx, report_xlsx.account_invoice2_xlsx

需要更多报表，可以自己写个模块，定义报表Class，只要写个name，不需要写任何方法，如下例：
```python
class AccountInvoice1Xlsx(models.AbstractModel):
    _name = 'report.report_xlsx.account_invoice1_xlsx'
    _inherit = 'report.report_xlsx.abstract'
```

Python Code中补货异常的代码写法示例：
```python
try:
    a = 1
    c = a/0
```

 except Exception as e:
    log.error(traceback.format_exc())

Odoo日志文件中打印出的Log如下（界面填充的代码的第三行异常）：
2019-03-12 11:27:38,932 7028 ERROR O12_ent01 odoo.addons.report_xlsx.report.report_xlsx: Traceback (most recent call last):
  File "", line 3, in
ZeroDivisionError: division by zero

#### 合并单元格

    ws.merge_cells('A2:D2')
    ws.unmerge_cells('A2:D2')  #合并后的单元格，脚本单独执行拆分操作会报错，需要重新执行合并操作再拆分
    # 或对应具体的行列，与上面两条结果相同
    ws.merge_cells(start_row=2,start_column=1,end_row=2,end_column=4)
    ws.unmerge_cells(start_row=2,start_column=1,end_row=2,end_column=4)

#### 使用公式求和

    ws["A5"] = "SUM(A1,A3)"
    ws["A5]" = "=SUM(A1:A%d)"%(i)

## 补充/答案 1

不能安装模块“report_xlsx”，因为一个外部依赖没有满足:No module named openpyxl

请问依赖于什么，SVN上有吗？安装不了。

安装一个python依赖:pip3 install openpyxl

## 补充/答案 2

备注一下，今天用了一个XLS后缀的文件报错，必须要xlsx后缀的文件 --！

## 补充/答案 3

Excel报表效果图（新增图片缩放及插入到Excel示例）

## 补充/答案 4

odoo13 打印报错TypeError: got invalid input value of type , expected string or Element

错误原因1： 版本过高，自动安装的版本为 openpyxl 3.0.2

解决办法：使用openpyxl 3.0.1 版本

    pip3 uninstall openpyxl
    pip3 install openpyxl==3.0.1

查看版本号的方法：

import openpyxl

openpyxl.__version__

## 补充/答案 5

##### **该模块相关参考链接**

\https\\\\\\www\\cnblogs\\com\\zeke\\python\\road\\p\\8986318\\html\\\

[https://blog.csdn.net/forever_wen/article/details/82555545]()

[https://xlsxwriter.readthedocs.io/format.html]()

## 补充/答案 6

塬数的excel报表中有图片，在打印时报错，看日志提示唱过了PIL包能处理的最大像素

![[2-excel-docx-wordreport-xlsxreport-docx-2987-38e0ea31.png]]

google后修改最大显示为不限制报错 MemoryError

![[2-excel-docx-wordreport-xlsxreport-docx-2987-86771164.png]]

![[2-excel-docx-wordreport-xlsxreport-docx-2987-6db05e20.png]]

要使用的图片大小是5.4M  像素大小时25813 * 7646

![[2-excel-docx-wordreport-xlsxreport-docx-2987-b72af298.png]]

![[2-excel-docx-wordreport-xlsxreport-docx-2987-b72af298.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
