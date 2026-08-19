---
title: "HR工资单导出到Excel功能"
source: "http://www.thinkltd.cn/forum/2/hrexcel-3564"
forum: "模块库"
author: "肖相扶"
published: 2025-08-29
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# HR工资单导出到Excel功能

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2025-08-29
> <http://www.thinkltd.cn/forum/2/hrexcel-3564>

模块位置：OSCG_SVN\odoo_ecommerce\15.0SRC\HR\report_xlsx_payslip

依赖模块：OSCG_SVN\odoo_ecommerce\15.0SRC\报表工具\report_xlsx

【功能截图】

1.  添加菜单“工资单（Excel导出）”，点击菜单，弹窗，选择导出年月，点击确定，导出所选月份的所有完成或支付状态的工资单到Excel文件

2.  模块配置：1）Excel模板文件上传。该模块下的目录 static\description，带有示例模板文件 payslip_template.xlsx；2）找到报表“工资条导出到Excel”，3）报表上配置Excel数据填写规则的python代码。

3.  python代码写法。line.get(code) or 0.0，此处code为工资计算规则上的 代码

![[2-hrexcel-3564-2c1665be.png]]

![[2-hrexcel-3564-0db741ac.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
