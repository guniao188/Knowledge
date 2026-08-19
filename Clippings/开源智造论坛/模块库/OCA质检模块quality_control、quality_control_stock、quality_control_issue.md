---
title: "OCA质检模块quality_control、quality_control_stock、quality_control_issue"
source: "http://www.thinkltd.cn/forum/2/ocaquality-controlquality-control-stockquality-control-issue-3240"
forum: "模块库"
author: "肖相扶"
published: 2022-12-16
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA质检模块quality_control、quality_control_stock、quality_control_issue

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-16
> <http://www.thinkltd.cn/forum/2/ocaquality-controlquality-control-stockquality-control-issue-3240>

模块链接：

Odoo 13.0升级方法：参照此贴通用升级方法处理后，即可在Odoo13中安装使用 [/forum/1/question/odoo12odoo13-461](http://www.thinkltd.cn/forum/1/question/odoo12odoo13-461)

Odoo 13汉化版模块链接：OSCG_SVN\odoo_ecommerce\13.0SRC\质检

参照此贴详细功能说明 [/forum/2/question/quality-control-mrp-3242](http://www.thinkltd.cn/forum/2/question/quality-control-mrp-3242)

【模块功能】

1.  该模块可以设置质检要求（qc.test），一个质检要求可以有多个质检明细（质量控制点），明细有两种，一种是测量型，设置质检合格范围（最小值、最大值、正常值）；一种是选择型，设置若干可选项（如优、良、不良等三个选项，或者白、灰白、亮白等选项），并指定哪些选项是合格的。【模块 quality_control】

2.  质检触发器（qc.trigger），模块自动为每中作业类型（Picking Type）创建一个触发器。每个触发器可以设置若干各触发条件。模块定义了三种触发条件：指定的产品、指定的变体、指定的产品分类。触发器上定义，哪个产品/变体/产品分类，需要做什么样的质检（qc.test）。【模块 quality_control_stock】

3.  Picking验证时候（action_done），系统检查适用于该作业类型的质检触发条件，如果找到了，则为找到的每一个触发条件创建一个质检单(qc.inspection)。

4.  如果qc.inspection 上各个质检控制点都合格，则确认时候，qc.inspection 状态变为完成。如果存在不合格的质检点，则要求更高权限的人审批。

【功能截图】

质量要求定义

![[2-ocaquality-controlquality-control-stockquality-control-issue-3240-468fc715.png]]

质检单触发条件设置

![[2-ocaquality-controlquality-control-stockquality-control-issue-3240-0a849190.png]]

质检单

![[2-ocaquality-controlquality-control-stockquality-control-issue-3240-bc9bd813.png]]

## 补充/答案 1

该质检存在一个问题，还会生成系统的质检单号，需要注释掉系统这两处：（1）、enterprise/mrp_workorder/models/mrp_workorder.py的def record_production部分代码
（2）、enterprise/mrp_workorder/models/mrp_production.py的button_plan()方法；

![[2-ocaquality-controlquality-control-stockquality-control-issue-3240-a65a9dea.png]]

![[2-ocaquality-controlquality-control-stockquality-control-issue-3240-00ae3260.png]]

![[2-ocaquality-controlquality-control-stockquality-control-issue-3240-cb816e8d.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
