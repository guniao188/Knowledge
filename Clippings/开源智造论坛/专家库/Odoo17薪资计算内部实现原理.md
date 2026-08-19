---
title: "Odoo17薪资计算内部实现原理"
source: "http://www.thinkltd.cn/forum/5/odoo17-3853"
forum: "专家库"
author: "刘祥海"
published: 2024-01-03
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/专家库
---

# Odoo17薪资计算内部实现原理

> [!info] 来源
> 开源智造论坛 · 专家库 | 作者:刘祥海 | 2024-01-03
> <http://www.thinkltd.cn/forum/5/odoo17-3853>

【问题列表】

1.  工资计算规则（hr.salary.rule）界面各个字段含义解释。
2.  工资计算变量含义及用法解说：payslip、employee、contract、rules、categories、worked_days、inputs
3.  工资附件hr.salary.attachment各个字段含义解说
4.  工资单（hr.payslip）各个字段含义解说，尤其WORKED DAYS、OTHER INPUTS、hr.payslip.line各个字段含义说明
5.  参考  [Odoo14薪资模块hr_payroll](http://www.thinkltd.cn/forum/2/odoo14hr-payroll-3412)

【业务实现示例】

1.  升级开发中国标准工资结构示例模块。
2.  参考  [中国薪资计算规则模块hr_payroll_cn](http://www.thinkltd.cn/forum/2/hr-payroll-cn-3617)

---

相关:[[Clippings/开源智造论坛/专家库/00-专家库索引.md|← 专家库索引]]
