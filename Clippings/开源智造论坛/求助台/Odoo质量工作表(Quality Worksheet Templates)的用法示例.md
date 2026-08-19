---
title: "Odoo质量工作表(Quality Worksheet Templates)的用法示例"
source: "http://www.thinkltd.cn/forum/1/odoo-quality-worksheet-templates-3770"
forum: "求助台"
author: "肖相扶"
published: 2025-01-20
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo质量工作表(Quality Worksheet Templates)的用法示例

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2025-01-20
> <http://www.thinkltd.cn/forum/1/odoo-quality-worksheet-templates-3770>

【业务背景】以铝箔纸生产中，粗轧工序为例。

1.  车间领取铝锭，做来料质检，记录质检结果
2.  铝锭上轧机（道次1）轧压，记录生产结果，以及质检结果
3.  道次1轧压出来的铝锭再依次经道次2、道次3、道次4轧压，完成粗轧生产。
4.  参考资料一：铝箔生产工艺：

![[1-odoo-quality-worksheet-templates-3770-382f6fe1.png]]

5.  参考资料二：来料和各道次质检表：

![[1-odoo-quality-worksheet-templates-3770-1f93e79b.png]]

6.  参考资料三：粗轧生产记录表：

![[1-odoo-quality-worksheet-templates-3770-21533f21.png]]

【配置要点】

1.  需要安装模块 quality_mrp_workorder_worksheet 。该模块移植到社区版的方法参考  [Odoo16企业版模块worksheet、quality_control_worksheet移植到社区版](http://www%5C.thinkltd%5C.cn/forum/1/odoo16worksheetquality%5C-control%5C-worksheet%5C-979)
2.  粗轧工序做成BoM，投入铝锭，产出粗铝卷。道次1、道次2、道次3、道次4做成粗轧BoM上的工序。
3.  来料质检、生产记录、完工质检做成道次上的工步（QCP，Quality Control Point）
4.  工步中的记录表格，如来料质检、生产记录、完工质检，做成质检工作表（Quality Worksheet）

【配置截图】

质检记录表模板配置：

![[1-odoo-quality-worksheet-templates-3770-09e8edb6.png]]

系统自动生成的质检记录表模型及视图上，增加需要的字段。如本例中，来料质检，需要记录标识是否合格，卷径、表面质量等，在该模型上增加上述字段，如下面截图。

![[1-odoo-quality-worksheet-templates-3770-8dcd51cd.png]]

配置QCP（质量控制点，或者工步），如下图：

![[1-odoo-quality-worksheet-templates-3770-82875752.png]]

实际生产时候，平板上调出工单（Work Order，如道次2），工步上点击按钮，填写生产记录/质检记录，如下图。

![[1-odoo-quality-worksheet-templates-3770-053b24ab.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
