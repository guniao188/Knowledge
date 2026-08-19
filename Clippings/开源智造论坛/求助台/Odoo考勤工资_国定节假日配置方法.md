---
title: "Odoo考勤工资/国定节假日配置方法"
source: "http://www.thinkltd.cn/forum/1/odoo-930"
forum: "求助台"
author: "肖相扶"
published: 2023-06-04
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo考勤工资/国定节假日配置方法

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2023-06-04
> <http://www.thinkltd.cn/forum/1/odoo-930>

【功能概要】功能基于15.0版本

1.  考勤记录（Work Entry）：每个月系统自动产生员工的考勤记录，工资单（Salary Slip）上，工资计算规则引用考勤记录（变量 worked_days），计算考勤工资。

2.  考勤记录的产生，系统根据员工合同上的出勤表（Working Hours），产生正常上班的考勤记录，再根据员工的缺勤记录（Time Off），产生各种没上班的考勤记录。

3.  注意：Odoo的考勤模块（Attendances）对算工资用的考勤记录（Work Entry）没有影响（不自动产生考勤记录）

4.  2023年6月4日，请安装模块： [HR排班/加班申请/加班调休模块hr_overtime](http://www.thinkltd.cn/forum/2/hr-hr-overtime-3563) 处理 加班/调班/倒班等情况。下述代码修改不需要（不能正确解决问题）。【删除】--> 调休的配置，需要修改下述代码：文件 OSCGODOO15\source\addons\hr_work_entry_contract\models\hr_contract.py 方法 def _get_contract_work_entries_values(self, date_start, date_stop)，108行代码  real_leaves = attendances - real_attendances  改成  real_leaves = leaves   < --【删除】

【实施截图】

考勤类型：

![[1-odoo-930-cadb4133.png]]

出勤表：

![[1-odoo-930-26de6de3.png]]

出勤表上配置节假日/调休。注意调休要像出勤表一样分上午、下午时段配置。

![[1-odoo-930-4f1a4514.png]]

休假类型配置。休假类型上可以设置对应的考勤类型，如此，该类型的休假，系统用该考勤类型创建考勤记录。

![[1-odoo-930-3943b24e.png]]

员工合同上设置对应的出勤表、合同工资。

![[1-odoo-930-d545c680.png]]

1.  工资单上，系统自动获取出勤记录（按考勤类型汇总）。工资计算规则上，引用考勤数据计算工资。

2.  工资单上不同类型考勤金额计算逻辑：1) 该类型考勤的小时数，除以工资单上的考勤小时总数，乘以合同上的工资。2) 当期有多个生效合同的情况下，取第一个合同的工资。

3.  工资单上引用考勤记录上的金额的示例代码：result = - sum(worked_days.LEAVE100.mapped('amount'))

![[1-odoo-930-cbc1f4fd.png]]

![[1-odoo-930-100f4f1e.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
