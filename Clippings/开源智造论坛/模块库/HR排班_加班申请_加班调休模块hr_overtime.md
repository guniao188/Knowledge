---
title: "HR排班/加班申请/加班调休模块hr_overtime"
source: "http://www.thinkltd.cn/forum/2/hr-hr-overtime-3563"
forum: "模块库"
author: "肖相扶"
published: 2024-02-06
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# HR排班/加班申请/加班调休模块hr_overtime

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-02-06
> <http://www.thinkltd.cn/forum/2/hr-hr-overtime-3563>

【废弃】注意，此模块设计不太合理，Odoo17以后，新开发了加班功能模块，此模块不再需要。参见  [Odoo17加班单及节假日调班模块hr_holidays_legal_ot](http://www.thinkltd.cn/forum/2/odoo17hr-holidays-legal-ot-3879)

模块位置：OSCG_SVN\odoo_ecommerce\15.0SRC\HR\hr_overtime

【模块功能】

1.  20230604功能优化：a. 加班/调班按出勤处理(_attendance_intervals_batch); b. 时间段(Intervals)加减时候，不同模型(resource.calendar.attendances 或 resource.calendar.leaves)时间段不合并（原来的代码因为不同模型合并导致报错）。

2.  **20220717增加排班功能**：员工可能上早班、晚班、夜班。增加员工排班表，可以按时间段指定员工上哪个班次。系统自动产生工作条目（Work Entry）时候，自动查找该时间段的排班，从排班上取工作日历表。没有配置排班的时间段，系统用合同或员工上的工作日历（resource_calendar_id字段）。

3.  增加 加班申请(平日)、加班申请(周末)、加班申请(节假)、加班调休 四种加班相关假期类型

4.      假期管理模块增加菜单“加班”，请假模型（hr.leave）上增加加班申请标记字段“is_overtime”

5.      如果是加班申请，加班时长字段的计算逻辑是：date_from, date_to 之间的时间，减去上班时间段，剩余（非上班时间）的小时数。上班时间段包括周一到周五的上午下午时间段（去除设置的公共节假日），也包括公共节假日里设置的周末调班时间段。

6.      加班申请审批通过时候，系统自动将加班时数 累加到 加班调休 的假期分配上，用于加班调休的请假

7.      加班拒绝时候，系统自动从 加班调休 的假期分配上，减去加班时数

8.      加班，以及 公共节假日上设置的周末调班（time_type必须设置为 other，而不是 leave），系统自动创建相应工作记录(Work Entry)

【功能截图】

![[2-hr-hr-overtime-3563-1dcc6e6d.png]]

![[2-hr-hr-overtime-3563-20716eea.png]]

![[2-hr-hr-overtime-3563-83f54a85.png]]

![[2-hr-hr-overtime-3563-7dc48fe9.png]]

![[2-hr-hr-overtime-3563-1cff7cb9.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
