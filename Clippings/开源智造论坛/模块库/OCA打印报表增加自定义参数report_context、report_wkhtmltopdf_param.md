---
title: "OCA打印报表增加自定义参数report_context、report_wkhtmltopdf_param"
source: "http://www.thinkltd.cn/forum/2/ocareport-contextreport-wkhtmltopdf-param-3007"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA打印报表增加自定义参数report_context、report_wkhtmltopdf_param

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocareport-contextreport-wkhtmltopdf-param-3007>

模块链接：

This module adds a context variable to reports. A possible use for this context could be hiding some fields or many other configuration options.

To configure this module, you need to:

- Enter Odoo in debug mode.
- To add a specific context to a report, you should go to Settings -> Reporting -> Reporting and look for the report you want to edit on the list. You will see that now they contain a new field called Context Value , where you will be able to add all the desired context parameters.
- Go to Settings -> Parameters -> System Parameters. On the system parameters list, look for report.default.context, which is a Python dictionary variable where you can add a context that will be common for all reports.

It can also be added on the developer side using:

        YOUR CONTEXT HERE

命令行参数参考：

This module allows you to add new parameters for a paper format which are then forwarded to wkhtmltopdf command as arguments. To display the arguments that wkhtmltopdf accepts go to your command line and type 'wkhtmltopdf -H'.

A commonly used parameter in Odoo is *--disable-smart-shrinking*, that will disable the automatic resizing of the PDF when converting. This is important when you intend to have a layout that conforms to certain alignment. It is very common whenever you need to conform the PDF to a predefined layoyut (e.g. checks, official forms,...).

###

### Usage

1.  Go to *Settings* and press 'Activate the developer mode (with assets)'
2.  Go to *Settings - Technical - Reports - Paper Format*
3.  Add additional parameters indicating the command argument name (remember to add prefix -- or -) and value.


## 原帖外链配图

![[2-ocareport-contextreport-wkhtmltopdf--x194038c2.png]]
<small>原始地址: /web/image/1433/snipaste_20190303_173556.png?access_token=49e15278-8df8-424b-970b-9de73e85c9f4</small>

![[2-ocareport-contextreport-wkhtmltopdf--x194038c2.png]]
<small>原始地址: /web/image/1435/snipaste_20190303_173429.png?access_token=85441c13-4f99-4170-b157-f554774d37c4</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
