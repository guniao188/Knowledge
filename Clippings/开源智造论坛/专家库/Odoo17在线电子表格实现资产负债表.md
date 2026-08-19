---
title: "Odoo17在线电子表格实现资产负债表"
source: "http://www.thinkltd.cn/forum/5/odoo17-3867"
forum: "专家库"
author: "钟卫卫"
published: 2024-01-17
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/专家库
---

# Odoo17在线电子表格实现资产负债表

> [!info] 来源
> 开源智造论坛 · 专家库 | 作者:钟卫卫 | 2024-01-17
> <http://www.thinkltd.cn/forum/5/odoo17-3867>

Odoo17在线电子表格，新增了会计科目借方、贷方、余额三个函数，如下例截图。

![[5-odoo17-3867-66c192c4.png]]

函数用法如下截图，如 ODOO.BALANCE(A3,C1,0,"","True")，表示从单元格A3中取得会计科目代码，从C1中取得日期，返回科目余额。

![[5-odoo17-3867-2bd3ea47.png]]

利用此函数，可以做一个工作表，列示所有会计科目的余额，再做一个工作表，引用科目余额，显示资产负债表。科目余额工作表如下面截图。

![[5-odoo17-3867-05bfe781.png]]

---

相关:[[Clippings/开源智造论坛/专家库/00-专家库索引.md|← 专家库索引]]
