---
title: "浮动工资导入模块hr_salary_ext"
source: "http://www.thinkltd.cn/forum/2/hr-salary-ext-3565"
forum: "模块库"
author: "肖相扶"
published: 2024-08-07
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 浮动工资导入模块hr_salary_ext

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-08-07
> <http://www.thinkltd.cn/forum/2/hr-salary-ext-3565>

【20240807升级到17.0】OSCG_Git\17.0\extra-addons\hr_salary_ext

【20221228模块升级到16.0】

1.  升级后模块位置：[https://gitlab.com/oscg-china/extra-addons/-/tree/16.0/hr_salary_ext](https://gitlab.com/oscg-china/extra-addons/-/tree/16.0/hr_salary_ext)
2.  同时修正了一个小缺陷：如果有重名员工，则以员工姓名导入浮动工资，系统不能匹配正确的员工。为了纠正此问题，浮动工资导入时候，员工列可以填写员工姓名，也可以填写员工身份证号（匹配员工上的 identification_id 字段）

模块位置：OSCG_SVN\odoo_ecommerce\15.0SRC\HR\hr_salary_ext

【模块功能】

1.      hr_payroll模块中，有个hr.salary.attachment，该表单用于设置每个月固定从工资中扣除的条目金额。工资单(hr.payslip)计算时候，系统检查此表单，自动将此条目加入到工资单的 Other Inputs中，用于工资计算。参考：[专项扣除/代扣代缴等工资项的配置方法](http://www.thinkltd.cn/forum/1/question/933)

2.      工资单上还有一类条目，如绩效工资，此部分数据每个月都不一样。本模块新增一个表单（hr.salary.extension）用于导入处理此部分工资条目。

3.     每个月工资计算前，通过Excel批量导入每个员工该月份的变动工资到hr.salary.extension，工资单计算时候，系统自动加入变动工资到工资单的 Other Inputs。注意，加入时候，系统检查该工资单上的计算规则的Code，和 hr.salary.extension 上的Other Input Type的Code进行匹配，只导入能匹配上的hr.salary.extension 。

【功能截图】

增加浮动工资 菜单

![[2-hr-salary-ext-3565-8b0b24b0.png]]

工资单上自动导入浮动工资到其他输入项

![[2-hr-salary-ext-3565-55f40bd8.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
