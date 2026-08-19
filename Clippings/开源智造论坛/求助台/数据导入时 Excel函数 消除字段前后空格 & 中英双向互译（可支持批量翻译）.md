---
title: "数据导入时 Excel函数 消除字段前后空格 &amp; 中英双向互译（可支持批量翻译）"
source: "http://www.thinkltd.cn/forum/1/excel-855"
forum: "求助台"
author: "赵晨"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 数据导入时 Excel函数 消除字段前后空格 &amp; 中英双向互译（可支持批量翻译）

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:赵晨 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/excel-855>

业务场景：帮助客户数据导入，公司名前后常用空格，可用函数去除保证数据整洁性。国家与地区字段可能为英文，系统导入需要中文，使用函数可快速批量翻译。

一.消除字段前后空格函数

=TRIM(A1)               A1可指向任意单元格

二.英汉双向互译函数（汉译英，英译汉）

=FILTERXML(WEBSERVICE("http://fanyi.youdao.com/translate?&i="&A1&"&doctype=xml&version"),"//translation")

A1可指向任意单元格

三.函数生效后取值覆盖方法

圈中后右键-选择性黏贴-值 （如下图）

![[1-excel-855-5533570d.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
