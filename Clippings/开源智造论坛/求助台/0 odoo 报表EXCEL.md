---
title: "0 odoo 报表EXCEL"
source: "http://www.thinkltd.cn/forum/1/0-odoo-excel-652"
forum: "求助台"
author: "沙正武"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 0 odoo 报表EXCEL

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:沙正武 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/0-odoo-excel-652>

### 准备工作

###

# 导入包

from openpyxl import load_workbook, Workbook

# 导入字体、边框、颜色以及对齐方式相关库

from openpyxl.styles import Font, Border, Side, PatternFill, colors, Alignment

# 设置初始行行高 水平和垂直对齐方式 边框样式 字体加粗

align_center = Alignment(horizontal='center', vertical='center',wrapText=True)

font_bold = Font(name='Arial', size=9, bold=True, color='ffffff')

# # 设置填充青色

cyan_fill = PatternFill("solid", fgColor="004269")

###

###

### 取值

**在发票中找关联的销售订单号**

so = self.env['sale.order'].search([('name', '=', obj.invoice_origin)], limit=1)

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
