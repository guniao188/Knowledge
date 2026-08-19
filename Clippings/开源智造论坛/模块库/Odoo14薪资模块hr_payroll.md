---
title: "Odoo14薪资模块hr_payroll"
source: "http://www.thinkltd.cn/forum/2/odoo14hr-payroll-3412"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo14薪资模块hr_payroll

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/odoo14hr-payroll-3412>

【Bug修正】

1.  经测试，工资条上手工录入销售提成、考勤扣款等浮动工资时候，系统的工资计算规则上，处理这部分工资有三处Bug。

2.  文件 ODOO14\source\enterprise\hr_payroll\models\hr_payslip.py，对象 hr.payslip.input 的字段 code的定义上，需要加上 store=True ，否则该模型对应的数据表中没有该字段，后面工资计算（inputs变量）时候会报错

3.  文件ODOO14\source\enterprise\hr_payroll\views\hr_payslip_views.xml ， Other Inputs 中， 的后面增加字段code：

4.  文件 OSCGODOO14\source\enterprise\hr_payroll\models\browsable_object.py， class InputLine 的SQL语句中，hp.state = 'done'  改成 hp.state = 'verify' 。否则系统找不到当前计算的工资条，也就找不到工资条的输入项( inputs )

【工资计算规则】

                    # Available variables:

                    #----------------------

                    # payslip: object containing the payslips

                    # employee: hr.employee object

                    # contract: hr.contract object

                    # rules: object containing the rules code (previously computed)

                    # categories: object containing the computed salary rule categories (sum of amount of all rules belonging to that category).

                    # worked_days: object containing the computed worked days.

                    # inputs: object containing the computed inputs.

- **payslip**：当前计算的工资单上的工资项目，可以直接用payslip.JXGZ1 获取绩效工资金额（JXGZ1 是绩效工资项目的工资规则的Code，注意不是工资规则的Categories的Code）。方法 payslip.sum('JXGZ1', payslip.date_from, to_date = payslip.date_to ) 返回date_from 到 date_to 时间段的， 规则代码为 'JXGZ1' 的所有工资项目的总金额，注意返回的总金额不包括本工资单的金额（即，只能返回以前的工资单的金额）。方法  payslip.sum_category('ALW', payslip.date_from, to_date=payslip.date_to) 返回 date_from 到 date_to 时间段的，类别(Categories) 代码为 'ALW' 的所有工资项目的总金额。此二个方法可用于计算个税（计算当年1月1日至算工资当月的工资、扣除）

- **categories**:  当前计算的工资单上的工资项目的工资规则的Categories，可以用 categories.GRJJ 获取当前工资单上的个人交金金额汇总（GRJJ 是工资规则上Categories的Code，个人承担的养老保险、公积金等可以设置为同一个Code，即GRJJ）

- **result_rules**：result_rules.JXGZ1 获取绩效工资数据，返回值是一个字典，包含值：{'total': tot_rule, 'amount': amount, 'quantity': qty}。即 result_rules.JXGZ1['total'] 获取该工资单上的绩效工资的金额。

- **worked_days**: 当前计算的工资单上的考勤数据

- **inputs**:  当前计算的工资单上的其他输入项，可以用  inputs.sum('JXGZ', payslip.date_from, to_date=payslip.date_to) 汇总计算当员工当月工资单的绩效工资总额

【功能介绍】

![[2-odoo14hr-payroll-3412-f5530a44.png]]

![[2-odoo14hr-payroll-3412-4f543923.png]]

![[2-odoo14hr-payroll-3412-81add1d7.png]]

![[2-odoo14hr-payroll-3412-69295ae6.png]]

![[2-odoo14hr-payroll-3412-b53829f1.png]]

【功能截屏】

## 补充/答案 1

【考勤工资】

Odoo 15.0 考勤工资/国定节假日配置方法参考 [Odoo考勤工资/国定节假日配置方法](http://www.thinkltd.cn/forum/1/question/odoo-930)

1.  工作表设置，设置菜单 Working Times，以周为单位，设置每天（周日到周六）的工作时间，如上午几点到几点，下午几点到几点，晚上几点到几点。不同班次，如白班、晚班，可以设置不同的工作表。工作表上还可以设置特殊日期（Global Time Off），如国定节假日。**注意，工作表上要正确设定时区**。

2.  员工适用工作表及时区设置，员工表单上，设置员工适用哪个工作表（如白班？夜班？），以及员工的时区。

3.  考勤类型设置，设置菜单 Work Entry Types，如正常上班、国定休假、事假、病假、迟到、旷工等考勤类型

4.  考勤打卡记录，hr_attendance模块，Attendances菜单，即几点签到、几点签出的打卡记录

5.  考勤明细数据，Work Entries菜单，含有员工、考勤类型、开始时间、结束时间、时长的考勤数据。系统提供了自动填充考勤明细数据功能，该功能根据员工的工作表，自动填写员工每天的考勤明细。可以写个服务器动作，基于考勤打卡记录自动生成考勤明细数据。

6.  考勤汇总数据，工资表上，系统自动抓取员工该月的考勤明细数据，按考勤类型汇总工作时间（天数、小时数），并用合同工资计算每小时单价，及该考勤类型的金额（每小时单价 X 该类型的时长）

7.  考勤工资计算，基于考勤汇总数据，编写工资计算规则，计算考勤工资。计算时候，可以获取“考勤汇总数据”中的每种考勤类型、时长、金额，而后计算考勤工资（如请假扣多少钱、迟到扣多少钱）。

## 补充/答案 2

![[2-odoo14hr-payroll-3412-46a46716.png]]

![[2-odoo14hr-payroll-3412-c2a7f7f6.png]]

【注意】

上面截图的个税算法是2018年前的算法，2019年开始，新的个税算法（）参考下述代码：

![[2-odoo14hr-payroll-3412-026b546a.png]]

#获取工资单所在年的1月1日开始，各项累计金额

date_year_1st = payslip.date_from

date_year_1st = date_year_1st.replace(month=1, day=1)

#累计合同工资、绩效工资

total_gz = payslip.sum("HTGZ", date_year_1st, payslip.date_to) + result_rules.HTGZ['total'] + payslip.sum("JXGZ", date_year_1st) + result_rules.JXGZ['total']

#累计减除费用（个税基数 5000）

total_kc = payslip.sum("GSJS", date_year_1st, payslip.date_to) + result_rules.GSJS['total']

#累计专项扣除（社保）

total_sbgr = payslip.sum("SBGR", date_year_1st, payslip.date_to) + result_rules.SBGR['total']

#累计已缴税额

total_gs = payslip.sum("GSKC", date_year_1st, payslip.date_to)

nsgz = total_gz - total_kc - total_sbgr

```python
if nsgz <=0:

    result = 0.0

elif nsgz < 36000:

    result = nsgz * 0.03 - total_gs

elif nsgz < 144000:

    result = nsgz * 0.1 - 2520 - total_gs

elif nsgz < 300000:

    result = nsgz * 0.2 - 16920 - total_gs

elif nsgz < 420000:

    result = nsgz * 0.25 - 31920 - total_gs

elif nsgz < 660000:

    result = nsgz * 0.3 - 52920 - total_gs

elif nsgz < 960000:

    result = nsgz * 0.35 - 85920 - total_gs

else:

    result = nsgz * 0.45 - 181920 - total_gs
```

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
