---
title: "Odoo17加班单及节假日调班模块hr_holidays_legal_ot"
source: "http://www.thinkltd.cn/forum/2/odoo17hr-holidays-legal-ot-3879"
forum: "模块库"
author: "肖相扶"
published: 2025-07-07
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo17加班单及节假日调班模块hr_holidays_legal_ot

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2025-07-07
> <http://www.thinkltd.cn/forum/2/odoo17hr-holidays-legal-ot-3879>

模块链接：OSCG_Git\17.0\extra-addons\hr_holidays_legal_ot

【模块功能】

1.  Odoo假期管理模块（hr_holidays），现有的“公共假期”功能，可以设置国定节假日，但无法设置国定节假日的调班。
2.  Odoo现有的HR功能中，有请休假管理功能，也有年假分配功能，但缺乏加班申请功能。
3.  本模块增加模型“国定节假日及调班(hr.leaves.legal)”、“加班申请(hr.ot.request)”。增加菜单“休假 --> 配置 --> 国定节假日及调班”、“休假 --> 我的时间 --> 我的加班”、“休假 --> 管理 --> 加班申请”。增加工作记录类型“国定节假日”、“节假日调班”、“平日加班”、“周末加班”、“节假日加班“，增加假期类型“加班调休”。
4.  国定节假日及调班确认后，国定节假日系统自动创建休假日历(resource.calendar.leaves)，调班系统自动创建出勤日历(resource.calendar.attendance)。此二记录参见菜单“设置 --> 技术 --> 资源 --> 休息时间”。 出勤日历没有菜单，可以在模型中找到此模块，创建菜单。
5.  加班申请批准后，系统自动创建加班时间段的 出勤日历(resource.calendar.attendance)，如果勾选了加班转调休，系统自动创建假期分配(hr.leave.allocation)，在加班调休类型的假期分配上增加加班时数对应的假期。
6.  加班申请菜单中，一个加班申请上，可以有多名员工（主管要求集体加班的情况）。系统也会自动添加多名员工的 出勤日历(resource.calendar.attendance)，及 假期分配(hr.leave.allocation)。

【功能截图】

![[2-odoo17hr-holidays-legal-ot-3879-f0e7c4fd.png]]

![[2-odoo17hr-holidays-legal-ot-3879-5e80a70a.png]]

## 补充/答案 1

【模块开发原理】

1.  Odoo的工作出勤、休假管理，基于基础模型出勤记录(resource.calendar.attendance)、休假记录(resource.calendar.leaves)。
2.  出勤记录(resource.calendar.attendance)，记录应出勤的工作时间段。有两种记录，一种是记录特定人（resource_id，员工也是resource），特定日期（date_from, date_to），几点到几点（hour_from, hour_to）出勤。如员工加班申请后，记录员工的加班时间段。另一种是不指定员工（也就是使用于所有人），记录一个时间段内(date_from, date_to)，周日到周六的上班时间。如公司的上下班时刻表，节假日调班表。
3.  休假记录(resource.calendar.leaves)，记录在出勤记录(resource.calendar.attendance)的时间段内，应休假的时间段(date_from, date_to)。不在出勤记录(resource.calendar.attendance)时间段的时间，如每日上班前、下班后，或者周末时间，天然属于休假，无需记录在 休假记录(resource.calendar.leaves)。落在周一到周五的节假日、员工请假时间段，此种休假需要记录到 休假记录(resource.calendar.leaves)。
4.  工作时刻表模型(resource.calendar)，该模型基于工作时刻表包含的 出勤记录(resource.calendar.attendance)、休假记录(resource.calendar.leaves)，计算员工的上班时间、非上班时间、休假时间，等等。
5.  1.  def _attendance_intervals_batch：返回时刻表上，指定时间段内、指定员工的上班时间段。本方法只基于出勤记录(resource.calendar.attendance)计算上班时间段，未基于休假记录(resource.calendar.leaves)排除休假时间段。
```python
    2.  def _leave_intervals_batch: 基于 休假记录(resource.calendar.leaves) ，返回指定时间段内、指定员工的休假时间段。
    3.  def _work_intervals_batch:   _attendance_intervals_batch返回的基础上，减去休假的时间段，得到真正的工作时间段
    4.  def _unavailable_intervals_batch: 指定时间段内、指定员工，非工作时间段（ _work_intervals_batch 返回值以外的时间段）
    5.  def get_work_hours_count: 指定时间段内，应工作的小时数。计算方法是， _work_intervals_batch返回的工作时间段，每个时间段的小时数加起来。
```

6.  节假日及调班、加班申请单，确认后，系统自动生成相应的 出勤记录(resource.calendar.attendance)、 休假记录(resource.calendar.leaves)，用于系统正确管理工作时间和休假时间。
7.  工作记录（hr.work.entry），基于出勤记录(resource.calendar.attendance)、 休假记录(resource.calendar.leaves)，生成每个员工，每个时间段的工作/休假小时数（作为工资计算的考勤数据）。计算逻辑是：先基于出勤记录(resource.calendar.attendance)计算出勤时间段，再基于休假记录(resource.calendar.leaves)，和出勤记录重叠的那部分时间段，标记为休假。工作记录的每个时间段，都有工作记录类型(hr.work.entry.type)，用于标记工作/休假类型，如正常上班、调班、加班、年假、事假，等等。计算方法参见文件OSCGODOO17\source\addons\hr_work_entry_contract\models\hr_contract.py 方法 def _get_contract_work_entries_values 。

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
