---
title: "质量检查点上增加在线电子表格(SpreadSheet)质检表单功能"
source: "http://www.thinkltd.cn/forum/2/spreadsheet-3999"
forum: "模块库"
author: "肖相扶"
published: 2024-10-31
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 质量检查点上增加在线电子表格(SpreadSheet)质检表单功能

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-10-31
> <http://www.thinkltd.cn/forum/2/spreadsheet-3999>

【业务背景】

1.  企业实际在用的质检表单往往比较复杂，用Odoo现有质量检查点（模型quality.point），自带的几种质检类型都比较简单。唯一复杂一点的是Worksheet类型，但此类型也难以处理如下图那样的质检单。
2.  一种解决办法是，在Odoo质量检查点模型上增加一个在线电子表格(SpreadSheet)模板，系统基于质检检查点创建质检单时候，从模板复制一个在线电子表格。质检员从平板电脑上打开表格，填写质检结果。
3.  技术实现方法， 质量检查点（模型quality.point）上增加质检类型SpreadSheet，及many2one字段关联到 SpreadSheet  Template，选择该类型时候，要求填写电子表格模板。基于 质量检查点生成质检单的时候，字段从模板创建电子表格（质量检查单上增加电子表格字段）。

![[2-spreadsheet-3999-29e07bd5.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
