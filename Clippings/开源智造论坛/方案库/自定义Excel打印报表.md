---
title: "自定义Excel打印报表"
source: "http://www.thinkltd.cn/forum/3/excel-3601"
forum: "方案库"
author: "肖相扶"
published: 2022-12-17
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/方案库
---

# 自定义Excel打印报表

> [!info] 来源
> 开源智造论坛 · 方案库 | 作者:肖相扶 | 2022-12-17
> <http://www.thinkltd.cn/forum/3/excel-3601>

模块excel_import_export 可以在Odoo页面上设置，打印模型的哪个字段，输出到Excel模板的哪个格子。其功能特点是：

1.  上传Excel输出模板，定义业务模型的哪个字段输出到模板Excel的哪个格子。
2.  可以定义循环输出，如单据上的多个明细行的输出。
3.  可以定义一些简单的输出条件，例如，单据上的某个字段等于1时候输出A值，等于2时候输出B值。
4.  不能操作Excel格式，模板文件是什么样，输出格式就是什么样。例如，无法实现： 单据上的某个字段等于1时候以红色字体显示，等于2时候以蓝色字体显示。
5.  不能做数据处理，例如，明细行的输出，不能自动添加序号。只能在业务单据的明细行的序号字段上，预先填写好序号值，再输出到Excel中。不能在Excel模板上添加序号。

excel_import_export打印报表的优缺点是：

1.  和Qweb技术，report_xlsx技术相比，本模块优点：格式模板简单，取数逻辑的设置简单。
2.  本模块缺点是，输出能力太弱，不能调整Excel格式，也不能处理数据逻辑。基本上只能按模板格式直接输出单据字段值。
3.  如果客户不愿意花工时做QWeb或 report_xlsx打印报表，可以向客户推荐此模块。培训客户模块使用方法，而后让客户自己制作打印单据。我们自己做打印报表的时候，不要采用此方案，因为基本上无法满足客户的各种打印需求。
4.  注意：采用此方案时候，一定要事先向客户申明，只能输出简单格式，复杂格式处理不了。实际情况，很可能客户自己试验之后，发现不行，不得不求助我们制作Qweb或 report_xlsx打印报表。

excel_import_export模块参考： [Excel订单数据导入/导出/Excel报表工具excel_import_export](http://www.thinkltd.cn/forum/2/excel-excelexcel-import-export-3486)

---

相关:[[Clippings/开源智造论坛/方案库/00-方案库索引.md|← 方案库索引]]
