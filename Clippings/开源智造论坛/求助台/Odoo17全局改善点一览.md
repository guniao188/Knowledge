---
title: "Odoo17全局改善点一览"
source: "http://www.thinkltd.cn/forum/1/odoo17-3809"
forum: "求助台"
author: "肖相扶"
published: 2024-04-10
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo17全局改善点一览

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-04-10
> <http://www.thinkltd.cn/forum/1/odoo17-3809>

返回 [Odoo17改善点列表](http://www.thinkltd.cn/forum/1/odoo17-3808)

1.  全新用户操作界面（UI）设计
    []()全新设计了用户操作界面，着重提升了界面易用性和界面美观性。主要目标是增强整体用户体验，提供可视化的操作界面，尽量做到用户一看就知道怎么使用。
2.  “搜索更多”改成了“查看所有”
    Users can now click 'View all' in dropdown menus, which opens a list in a dialog, facilitating differentiation between potentially identical records.
3.  高级搜索界面改善
    搜索框中的高级搜索框，改成了弹窗输入，输入界面更大，更容易 。 

![[1-odoo17-3809-3972ae09.png]]

4.  增加头像名片预览功能
    点击用户或员工的头像，显示联系信息，以前的版本是点击头像，自动弹出消息发送消息的

![[1-odoo17-3809-86bea6b9.png]]

5.  地图视图的Sidebar
    和Odoo中其他视图一样，地图视图的Sidebar放到了左边（以前版本在右边）。

![[1-odoo17-3809-07e8bb3a.png]]

6.  Chatter: message and note translations
    Enable translations for messages and notes in the chatter.
7.  单据确认和取消按钮增加快捷键
    单据确认按钮增加快捷键 (ALT/CMD+Q)，单据取消按钮增加快捷键(ALT/CMD+X)。
8.  数据导入时候日期格式
    数据导入时候，日期和时间格式支持客户化格式（待确认：是不是技术设置中配置的时间日期格式？）。
9.  弹窗消息确认窗口支持快捷键操作
    弹窗消息确认窗口，快捷键（ CTRL+Enter ）等同于点击确认按钮。
10. 禁止打开表单视图
    点击只读的Many2One的字段，不再打开Form表单视图。
11. 去掉了拼写检查
    文本输入框（Text类型字段），去掉了浏览器的自动拼写检查功能。
12. 筛选域编辑界面改善
    T筛选条件域的编辑界面改善了，更易于理解怎么用。

![[1-odoo17-3809-53304c81.png]]

13. 表单状态栏上显示停留时长
    表单视图（Form）上，状态条上显示单据在每个状态上停留的时长。目前该功能已应用于在项目任务、销售线索、售后问题。

![[1-odoo17-3809-59503d33.png]]

14. Odoo文本编辑器集成了ChatGPT
    Odoo文本编辑器集成了ChatGPT，辅助自动生成文本内容。/ChatGPT即可调出ChatGPT

![[1-odoo17-3809-9a6ba5c6.png]]

15. 别名邮箱设置上增加状态显示

![[1-odoo17-3809-f6c3c66d.png]]

16. Email bounce feedback
    Get feedback on why your email bounced.
17. 邮件模板管理
    邮件模板增加用户字段，以及权限规则，普通员工只能创建、修改自己的邮件模板。
18. 固定列表视图表头行
    列表视图（Tree视图）上，上下滚动时候，标题行不滚动，固定显示标题行。不过，表单上One2many字段，明细行很多，上下滚动时候标题行不固定。
19. Gamification: track karma
    Track where karma points come from in a dedicated menu.
20. 属性( property )类型字段也支持分组操作
    可以按属性( property )类型字段进行分组操作
21. 按易于人理解的方式显示数字字段值
    数字类型字段值可以按缩略格式显示 (如显示 500k，而不是显示 500,000)
22. 增强了看板视图上的新建功能
    看板视图上，按 Many2Many类型字段 (如 标签tags字段, 负责人assignees字段, 等等) 分组显示时候，也可以支持快递新建记录。以前的版本，按 Many2Many类型字段分组时候不支持新建。
23. 列表视图：支持多选批量复制功能
    以前版本只能支持Form视图上单条记录复制
24. Mixed stacked bar / line chart
    Analyze trends more easily on stacked bar charts by adding a line graph displaying group totals.
25. Mobile app shortcuts
    Access useful Odoo apps with shortcuts on the mobile application.
26. Wizard弹窗位置可以拖动
    Wizard弹窗可以拖动到不同位置显示（但还不支持改变窗口大小）。以前的版本，弹窗不能拖动，只能固定显示在一个位置
27. Email别名功能支持多域名邮箱

![[1-odoo17-3809-107932bf.png]]

28. Odoo渐进式WebApp（PWA）
    参看  [Odoo17支持WebApp安装](http://www.thinkltd.cn/forum/1/odoo17webapp-3807)
29. OWLGrid视图
    Grid视图换成了OWL技术实现，提升了性能，还增加了新特性，如显示样例数据。
30. 属性(Property)类型字段也支持Domain筛选
    高级搜索中，可以按 属性(Property)类型字段 筛选
31. 属性（ Property ）类型字段
    Property fields have been added to additional models.
32. Property fields in list views
    Display property fields in list view by adding optional columns.
33. 快速用户指派
    看板视图上，点击用户头像，快速指派用户

![[1-odoo17-3809-c8f67d74.png]]

34. 列表视图shit快捷键连选记录
    列表视图上，Shift键+上下光标键，或鼠标点击，批量连选/去选记录。
35. Ratings on email templates
    Ask customers for their opinion by adding ratings to your email templates.
36. Re-order apps
    Each user can re-order their app icons on the dashboard by dragging-and-dropping them.
37. 用户字段
    指定用户的字段，用户选择时候，当前用户总是排在下拉框的第一位

![[1-odoo17-3809-32fa43e2.png]]

38. 支持属性property类型字段筛选
    搜索框中输入搜索字符筛选时候，支持 属性property类型字段
39. Separator field type
    Group property fields into categories by using collapsible separator fields.
40. SMS短信状态
    增加了“发送中的”短信发送状态
41. Stacked bar charts
    Stacked bar charts now include a line graph displaying the groups' totals for easier trend analysis.
42. 文本编辑框可以任意输入字体大小
    以前的版本只能选择字体大小，不能任意输入

![[1-odoo17-3809-6925f5e2.png]]

43. 从收件箱中去关注
    邮件或Odoo的收件箱中增加“去关注”功能。

![[1-odoo17-3809-3526328f.png]]

44. 列表视图上增加了“去选所有”功能

![[1-odoo17-3809-fe58bbbe.png]]

1.  新增了一个“ToDo待办事项”的功能模块

![[1-odoo17-3809-b708c490.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
