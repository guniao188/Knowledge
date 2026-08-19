---
title: "【服务器动作】员工工作条目（Work Entry）批量重新生成"
source: "http://www.thinkltd.cn/forum/1/work-entry-949"
forum: "求助台"
author: "肖相扶"
published: 2023-02-14
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 【服务器动作】员工工作条目（Work Entry）批量重新生成

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2023-02-14
> <http://www.thinkltd.cn/forum/1/work-entry-949>

【业务背景】工资模块中，有一个功能可以逐个员工生成开始日期/结束日期 时间段的工作条目（Work Entry），但缺乏多个员工批量生成工作条目的功能。

【实现代码】

1.  本服务器动作代码，勾选员工，批量生成工作条目（Work Entry）。

2.  注意开始日期/结束日期 时间段在代码中指定。

3.  代码如下

```python
date_start = '2022-07-01'

date_stop = '2022-07-31'
```

date_from = datetime.datetime.strptime(date_start, '%Y-%m-%d').date()

date_to = datetime.datetime.strptime(date_stop, '%Y-%m-%d').date()

```python
for emp in records:

    work_entries = env['hr.work.entry'].search([

            ('employee_id', '=', emp.id),

            ('date_stop', '>=', date_from),

            ('date_start', '<=', date_to),

            ('state', '!=', 'validated')])

    work_entries.write({'active': False})

    emp.generate_work_entries(date_from, date_to, True)
```

action = env["ir.actions.actions"]._for_xml_id('hr_work_entry.hr_work_entry_action')

![[1-work-entry-949-10517a3f.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
