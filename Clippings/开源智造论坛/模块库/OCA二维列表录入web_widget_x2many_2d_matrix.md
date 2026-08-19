---
title: "OCA二维列表录入web_widget_x2many_2d_matrix"
source: "http://www.thinkltd.cn/forum/2/ocaweb-widget-x2many-2d-matrix-2835"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA二维列表录入web_widget_x2many_2d_matrix

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocaweb-widget-x2many-2d-matrix-2835>

模块链接：

使用示例模块：

经测试，删除py文件中所有的 @api.multi ，即可在 13.0 中正常安装使用。

This module allows to show an x2many field with 3-tuples ($x_value, $y_value, $value) in a table

|            | $x_value1   | $x_value2   |
|------------|--------------|--------------|
| $y_value1 | $value(1/1) | $value(2/1) |
| $y_value2 | $value(1/2) | $value(2/2) |

where value(n/n) is editable.

An example use case would be: Select some projects and some employees so that a manager can easily fill in the planned_hours for one task per employee. The result could look like this:

The beauty of this is that you have an arbitrary amount of columns with this widget, trying to get this in standard x2many lists involves some quite ugly hacks.

## [Usage](https://github.com/OCA/web/tree/12.0/web_widget_x2many_2d_matrix#id5)

Use this widget by saying:

This assumes that my_field refers to a model with the fields x, y and value. If your fields are named differently, pass the correct names as attributes:

You can pass the following parameters:

field_x_axis
The field that indicates the x value of a point

field_y_axis
The field that indicates the y value of a point

field_label_x_axis
Use another field to display in the table header

field_label_y_axis
Use another field to display in the table header

field_value
Show this field as value

show_row_totals
If field_value is a numeric field, it indicates if you want to calculate row totals. True by default

show_column_totals
If field_value is a numeric field, it indicates if you want to calculate column totals. True by default

###

### [Example](https://github.com/OCA/web/tree/12.0/web_widget_x2many_2d_matrix#id6)

You need a data structure already filled with values. Let's assume we want to use this widget in a wizard that lets the user fill in planned hours for one task per project per user. In this case, we can use `project.task` as our data model and point to it from our wizard. The crucial part is that we fill the field in the default function:

```python
    from odoo import fields, models
    class MyWizard(models.TransientModel):
        _name = 'my.wizard'
        def _default_task_ids(self):
```

            # your list of project should come from the context, some selection
            # in a previous wizard or wherever else
            projects = self.env['project.project'].browse([1, 2, 3])
            # same with users
```python
            users = self.env['res.users'].browse([1, 2, 3])
            return [
                (0, 0, {
                    'name': 'Sample task name',
                    'project_id': p.id,
                    'user_id': u.id,
                    'planned_hours': 0,
                    'message_needaction': False,
                    'date_deadline': fields.Date.today(),
                })
```

                # if the project doesn't have a task for the user,
                # create a new one
                if not p.task_ids.filtered(lambda x: x.user_id == u) else
                # otherwise, return the task
```python
                (4, p.task_ids.filtered(lambda x: x.user_id == u)[0].id)
                for p in projects
                for u in users
            ]
        task_ids = fields.Many2many('project.task', default=_default_task_ids)
```

Now in our wizard, we can use:

## 补充/答案 1

功能效果截图：

![[2-ocaweb-widget-x2many-2d-matrix-2835-937486e7.png]]


## 原帖外链配图

![[2-ocaweb-widget-x2many-2d-matrix-2835-xd2cbbb61.png]]
<small>原始地址: https://raw.githubusercontent.com/OCA/web/12.0/web_widget_x2many_2d_matrix/static/description/screenshot.png</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
