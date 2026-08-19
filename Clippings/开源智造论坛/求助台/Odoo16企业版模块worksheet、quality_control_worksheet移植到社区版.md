---
title: "Odoo16企业版模块worksheet、quality_control_worksheet移植到社区版"
source: "http://www.thinkltd.cn/forum/1/odoo16worksheetquality-control-worksheet-979"
forum: "求助台"
author: "肖相扶"
published: 2023-06-13
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo16企业版模块worksheet、quality_control_worksheet移植到社区版

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2023-06-13
> <http://www.thinkltd.cn/forum/1/odoo16worksheetquality-control-worksheet-979>

【worksheet移植方法】

1.  文件 OSCGODOO16\myaddons2\worksheet\\_manifest__.py中，'depends': ['web_studio'], 改成     'depends': ['base_automation', 'base_import_module', 'mail', 'web', 'web_editor', 'sms',  ], 

![[1-odoo16worksheetquality-control-worksheet-979-84b74782.png]]

2.  文件 OSCGODOO16\myaddons2\worksheet\static\src\open_studio_button_widget\open_studio_button_widget.js中注释下面三行：

![[1-odoo16worksheetquality-control-worksheet-979-56beb30a.png]]

3.  文件OSCGODOO16\myaddons2\worksheet\\_init__.py 中，注释行 from . import controllers 

![[1-odoo16worksheetquality-control-worksheet-979-a56d5d4f.png]]

【quality_control_worksheet移植方法】

文件 OSCGODOO16\myaddons2\quality_control_worksheet\static\src\views\quality_worksheet_fromview.js 中，ormService 改成 orm 

![[1-odoo16worksheetquality-control-worksheet-979-61425b36.png]]

## 补充/答案 1

【worksheet模板制作方法】
worksheet模板worksheet.template，应用场景是，例如质检环节，不同情况质检的内容不同，是否可以制作一个质检表单，包含所有质检内容的字段呢？worksheet.template就是用于协助制作新表单的。
worksheet.template上的 res_model字段指定新表单关联的模型，如quality.check , 而后新表单的模型名称必须是 x_quality_check 开头，且新表单必须包含字段 x_quality_check_id （many2one关联到quality.check模型），x_comment字段（html类型），x_name字段

![[1-odoo16worksheetquality-control-worksheet-979-a0bcb267.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
