---
title: "基于report_xlsx模块的数据导出方法"
source: "http://www.thinkltd.cn/forum/1/report-xlsx-3614"
forum: "求助台"
author: "肖相扶"
published: 2022-12-22
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 基于report_xlsx模块的数据导出方法

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-22
> <http://www.thinkltd.cn/forum/1/report-xlsx-3614>

Odoo系统自带的导出功能，一次导出数据最多2万条，如果要大量导出数据（几十万），或者希望先对数据做一定处理后再导出，这里介绍一种新方法：

1.  安装模块report_xlsx （[二开Excel/Docx word打印报表模块report_xlsx、report_docx](http://www.thinkltd.cn/forum/2/excel-docx-wordreport-xlsxreport-docx-2987)）
2.  增加一个XLSX类型报表
3.  编写python代码，获取希望导出的数据，填写到Excel工作表导出
4.  实测此数据导出方法速度非常快，10万条产品数据10多秒就导出了
5.  此方法不仅可以用于导出数据，也可以用于导出任意数据报表：
6.  1.  上传报表模板Excel
    2.  python代码抽取报表数据，输出到Excel下载

【配置截图】以产品数据导出为例

![[1-report-xlsx-3614-f964efb9.png]]

![[1-report-xlsx-3614-08d9c5e6.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
