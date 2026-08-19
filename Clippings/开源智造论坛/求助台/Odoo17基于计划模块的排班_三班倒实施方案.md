---
title: "Odoo17基于计划模块的排班/三班倒实施方案"
source: "http://www.thinkltd.cn/forum/1/odoo17-3882"
forum: "求助台"
author: "肖相扶"
published: 2024-02-19
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo17基于计划模块的排班/三班倒实施方案

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-02-19
> <http://www.thinkltd.cn/forum/1/odoo17-3882>

【业务背景】

1.  工厂三班倒生产，早班0点至8点，白班8点至16点，夜班16点至24点
2.  工人以月为单位排班，如张三2月份当白班，3月份当夜班
3.  月末，系统应该按排班表生成每个人的出勤及请休假的工作记录（hr.work.entry）

【实施方案】

1.  安装Odoo17企业版计划相关模块 planning、planning_contract、planning_holidays
2.  配置三班倒的“工作时间表”，起始时间00:00，结束时间24:00
3.  员工及员工合同上选择三班倒工作时间表，合同上工作记录来源选择“计划”
4.  计划模块中，创建早班、白班、夜班的三个角色，为员工安排早班、白班或夜班的计划。如果员工数较多，此处可以开发一个排班的Wizard，批量自动创建排班计划。
5.  员工合同状态改为进行中、排班计划发布。如此，系统可以自动按排班计划生成工作记录。计划的列表视图中，可以多选计划，批量发布。
6.  注意一，夜班中的24点，要填写23:59:59
7.  注意二，此处可能是一个Bug。三班倒员工，如果某天请假了，系统请假的工作记录的时长计算，是按工作时间表来计算，即一天24小时，而不是按排班时间来计算（一天8小时）。即出勤时间按计划来计算，但请假时间未按计划计算。
8.  注意三，计划模块的班次模板(planning.slot.template)，时长计算时候，用的是公司的默认工资时间表。此处应该在此模型上增加一个工作时间表的字段，用该字段的工作时间表计算时长。否则三班倒的情况，时长计算不正确。

【方案截图】

![[1-odoo17-3882-718cbb9b.png]]

![[1-odoo17-3882-34a91ee7.png]]

![[1-odoo17-3882-19140549.png]]

![[1-odoo17-3882-271dc801.png]]

请假时长未按计划计算：

![[1-odoo17-3882-5bebb39c.png]]

## 补充/答案 1

【内部实现逻辑】

1.  系统生成工作记录的方法：OSCGODOO17\source\addons\hr_work_entry_contract\models\hr_contract.py 方法 def _get_contract_work_entries_values 。该方法先调用方法 _get_attendance_intervals  获取出勤时间段。
2.  文件 OSCGODOO17\source\enterprise\hr_work_entry_contract_planning\models\[hr_contract.py](https://hr_contract.py)中，继承了方法_get_attendance_intervals，针对工作记录来源为计划的合同，获取该员工的计划安排(planning.slot)，再计算出勤时间段。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
