---
title: "生产单MO不自动确认/标记待办mrp_not_confirm"
source: "http://www.thinkltd.cn/forum/2/mo-mrp-not-confirm-3369"
forum: "模块库"
author: "肖相扶"
published: 2023-03-30
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 生产单MO不自动确认/标记待办mrp_not_confirm

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2023-03-30
> <http://www.thinkltd.cn/forum/2/mo-mrp-not-confirm-3369>

模块位置：SVN\odoo_ecommerce\13.0SRC\mrp_not_confirm
【新增15.0版本】OSCG_SVN\odoo_ecommerce\15.0SRC\生产管理\mrp_not_confirm

【2022.5.26BUG修复】原先版本未考虑MO的欠单情况，系统通过backorder_sequence字段判断是否为欠单。backorder_sequence=0为原单据，如果有欠单，原单的backorder_sequence变成1，欠单的backorder_sequence变为2。
14和15版本SVN代码已修复该BUG。13因为没有MO创建欠单逻辑，所以代码不需要跟新。

【业务背景】

1.  深圳五洲行的生产管理，帐篷生产分三个大的步骤：裁床、车缝、包装。裁床步骤是机器批量裁布，车缝是将裁好的布片缝制成帐篷。车缝基本上是手工作业，很慢，是产能瓶颈所在。

2.  生管/PMC计划排产时候，如果自己工厂车缝车间产能紧张，则会将车缝步骤委外给其他工厂。有多家委外商，排产时候会择优安排委外商。

3.  Odoo中，标准的委外功能是，BoM指定是否委外，如果委外，该BoM部件，系统总是按委外处理，参考说明 \\forum/1/question/3355

4.  但这里的需求是，产能足够则不委外，产能不足才委外。

5.  一种处理方法是，1) 设置一个“委外”的作业类型，计划排产时候，如果该MO/子MO需要委外，则修改MO的作业类型（picking_type_id字段）成“委外” 。 2) 对于每个委外的MO，手工创建一个PO采购“委外服务”，用于管理供应商应付账款。

6.  但上述处理方法存在一个问题，Odoo现有功能中，主MO确认/标记待办时候，系统自动confirm 原料消耗的Stock Move，自动产生子MO，子MO也自动标记待办。子MO自动标记为待办后，没法修改作业类型。希望增加一个功能，主MO确认时候，子MO不要自动标记待办，而是让计划员手工修改作业类型后（例如改成委外），手工标记为待办。

【模块设计】

1.  新开发功能模块 mrp_not_confirm， 该模块在BoM上增加了一个Boolen型字段“自动标记待办”，该字段默认值为True。

2.  系统基于制造规则创建的MO，如果该MO的BoM上的“自动标记待办”字段设置为False，则该MO不自动标记待办。

3.  参考实现方法：代码文件 ODOO13\source\odoo\addons\mrp\models\stock_rule.py 中，方法 def _run_manufacture(self, procurements):  ，代码行  productions.action_confirm()，该代码行增加一个BoM上的“自动标记待办”字段值判断，如果为True才调用 action_confirm()

【SVN路径】

    SVN\odoo_ecommerce\13.0SRC\mrp_not_confirm

## 补充/答案 1

16版本插件中，对原生的功能 action_confirm传了上下文，拿到上下文才跑 action_confirm方法

所以如果想通过服务器动作写批量确认功能时，也要传上下文

records.with_context(action_confirm_from_ui=True).action_confirm()

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
