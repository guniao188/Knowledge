---
title: "OCA甘特图(Gantt)显示web_timeline"
source: "http://www.thinkltd.cn/forum/2/oca-gantt-web-timeline-2692"
forum: "模块库"
author: "杨浔波"
published: 2025-02-08
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA甘特图(Gantt)显示web_timeline

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:杨浔波 | 2025-02-08
> <http://www.thinkltd.cn/forum/2/oca-gantt-web-timeline-2692>

模块下载：[https://github.com/OCA/web/tree/11.0/web_timeline](https://github%5C.com/OCA/web/tree/11%5C.0/web_timeline)

要在 Project中实现以上效果，需要对该 addon 进行一些修改：

addons/project/views/project_views.xml

```python
            project.task

            timeline

                            Assigned to:
```

....

            kanban,tree,form,calendar,pivot,graph,timeline

###### ....

以上分别使用了date_start和date_deadline字段作为 Timeline 中的开始和结束时间，考虑编辑的便利性，还应同时在 form 视图中添加date_start的编辑功能（由于 date_start 的数据类型是 datetime，所以这里添加了一个widget=”date”）：

...

###### ...

######

效果如下：

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
