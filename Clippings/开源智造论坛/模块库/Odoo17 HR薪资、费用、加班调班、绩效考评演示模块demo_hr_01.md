---
title: "Odoo17 HR薪资、费用、加班调班、绩效考评演示模块demo_hr_01"
source: "http://www.thinkltd.cn/forum/2/odoo17-hrdemo-hr-01-3968"
forum: "模块库"
author: "肖相扶"
published: 2024-08-12
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo17 HR薪资、费用、加班调班、绩效考评演示模块demo_hr_01

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-08-12
> <http://www.thinkltd.cn/forum/2/odoo17-hrdemo-hr-01-3968>

模块链接：OSCG_Git\17.0\extra-addons\demo_hr_01

【功能说明】

1.  本模块依赖：[中国薪资计算规则模块hr_payroll_cn](http://www.thinkltd.cn/forum/2/hr-payroll-cn-3617)，[浮动工资导入模块hr_salary_ext](http://www.thinkltd.cn/forum/2/hr-salary-ext-3565)，[在线python代码下载Excel报表模块report_xlsx](http://www.thinkltd.cn/forum/2/pythonexcelreport-xlsx-3615)， [Odoo费用报销模块完善hr_expense_cn](http://www.thinkltd.cn/forum/2/odoohr-expense-cn-3415)， [Odoo17加班单及节假日调班模块hr_holidays_legal_ot](http://www.thinkltd.cn/forum/2/odoo17hr-holidays-legal-ot-3879)、 [Odoo17绩效考评模块hr_appraisal_cn](http://www.thinkltd.cn/forum/2/odoo17hr-appraisal-cn-3970)
2.  本模块增加“工资表导出到Excel”功能。

![[2-odoo17-hrdemo-hr-01-3968-047d6cf9.png]]

3.  安装本模块，自动导入一名员工“张开源”及对应劳动合同。
4.  安装本模块后，执行服务器动作“演示：费用报销演示数据”，自动设置费用类产品类别及员工工作地址（address_id）的会计科目，自动创建管理、销售、制造、请款类的费用产品。
5.  安装本模块后，执行服务器动作“演示：绩效考评演示数据”，自动创建一个“通用绩效考评”问卷表。

![[2-odoo17-hrdemo-hr-01-3968-010af3ab.png]]

6.  HR薪资制单参考SOP：
7.  1.  检查岗位津贴、个税专项附加扣除有无变更。如有变更，菜单“工资 --> 合同 --> 工资附件”中对应修改
```python
    2.  导入浮动工资(如销售提成、绩效工资、考勤工资等)。菜单“工资 --> 合同 --> 浮动工资”
    3.  创建“工资批”。菜单“工资 --> 工资单 --> 工资批量”
    4.  工资审核
    5.  工资单邮件发给员工
    6.  导出Excel工资表，工资表交财务
```

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
