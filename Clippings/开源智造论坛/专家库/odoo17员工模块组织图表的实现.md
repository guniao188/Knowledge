---
title: "odoo17员工模块组织图表的实现"
source: "http://www.thinkltd.cn/forum/5/odoo17-3857"
forum: "专家库"
author: "王澧鑫"
published: 2024-01-08
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/专家库
---

# odoo17员工模块组织图表的实现

> [!info] 来源
> 开源智造论坛 · 专家库 | 作者:王澧鑫 | 2024-01-08
> <http://www.thinkltd.cn/forum/5/odoo17-3857>

在odoo17的员工模块中，我们可以看到这样一个图表，主要用来显示此员工是谁的直接下属：

![[5-odoo17-3857-1e0b8a23.png]]

他的实现主要分为两部分，第一部分为：

![[5-odoo17-3857-b52ff7b9.png]]

主要是定义该板块的显示名称。

第二部分为：

![[5-odoo17-3857-6af0aeb3.png]]

主要是使用了一个one2many字段以及一个widget小部件，来实现组织图表的功能。

其内部js文件为addons/hr_org_chart/static/src/fields/hr_org_chart.js，代码逻辑如下：

**setup 方法：**

- 初始化组件。
- 获取并设置所需的服务，如 rpc、orm等。
- 使用 useState 来定义组件的状态。
- 使用 onWillStart 和 onWillRender 钩子，在组件启动和渲染之前触发，用于处理组件的更新。

**handleComponentUpdate 方法：**

- 获取当前员工的数据，并根据上一个记录和其上级的值判断是否需要强制重新加载数据。
- 调用 fetchEmployeeData 方法获取员工数据。

**fetchEmployeeData 方法：**

- 根据传入的 employee_id，通过 rpc调用 /hr/get_org_chart 后端接口获取组织架构数据。
- 更新组件的状态，包括上级管理者、下级员工、更多的上级管理者等信息。
- 如果没有有效的 employee_id，则清空相关数据。

**_onOpenPopover 方法：**

- 点击组织架构图中的员工时，打开弹出框显示员工的详细信息。
- 通过 popover.open 方法打开弹出框，并传递当前点击的员工信息。
- 用于重定向到员工表单视图。
- 根据传入的 employee_id，调用 hr.employee 模型的 get_formview_action 方法获取相应员工的操作（action）。
- 通过 actionService.doAction(action) 执行该操作，从而实现重定向。

**_onEmployeeMoreManager 方法：**

- 用于处理点击更多上级管理者时的事件。
- 调用 fetchEmployeeData 方法获取更多上级管理者的数据，并更新组件的状态，以显示更多的上级管理者信息。

其xml模板逻辑如下：

![[5-odoo17-3857-47c0d125.png]]

![[5-odoo17-3857-34d0363f.png]]

![[5-odoo17-3857-7d61b298.png]]

---

相关:[[Clippings/开源智造论坛/专家库/00-专家库索引.md|← 专家库索引]]
