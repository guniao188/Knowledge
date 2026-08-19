---
title: "odoo16补货解析"
source: "http://www.thinkltd.cn/forum/3/odoo16-3715"
forum: "方案库"
author: "施叶寒"
published: 2023-06-05
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/方案库
---

# odoo16补货解析

> [!info] 来源
> 开源智造论坛 · 方案库 | 作者:施叶寒 | 2023-06-05
> <http://www.thinkltd.cn/forum/3/odoo16-3715>

拉式规则的应用

1.1 触发时机
stock_move 的 _action_confirm 方法

1.2 应用条件
stock_move.move_orig_ids == False
stock_move.procure_method == 'make_to_order'
env['stock.rule']._get_rule 找到对应的 规则

1.3 上游明细 的 数据源
stock_move._prepare_procurement_values => 上下游关系、捕获组、日期等
stock_move._prepare_procurement_origin => 原单据
stock_move 本身 => 产品、数量 等
stock_rule => 源位置、目的位置

1.4 上游明细 的数据构成
stock_rule._get_stock_move_values 返回创建上有明细的 键值对
其中,可以在 stock_rule._get_custom_move_fields 里登记待传递的新字段,例如 sale_line_id

1.5 规则
1. env['stock.rule']._get_rule_domain => 公司为空/当前(子)公司 + 位置匹配 + 规则!=推
2. env['stock.rule']._search_rule =>
在当前位置中,去找匹配 业务单据中指定>包裹绑定的>产品绑定的>仓库绑定的的路线 的规则;如果没有找到,向上级位置循环去找。

1.6 关键代码
1. 业务单据(sale_order, mrp_production)构建 ['stock.rule'].Procurement 对象
2. 调用 env['procurement.group']的 run 方法,通过 _get_rule 方法找到对应的 stock_rule
3. 根据 stock_rule 的动作,产生相应的单据：
拉/拉并推 => stock.picking
制造 => mrp.production
购买 => purchase.order
4. 如果执行动作 拉,产生的上游单据 stock_move ,将自动确认。在 stock_move 的_action_confirm 方法将再度尝试触发 拉式规则,形成递归。

1.7 自动/手动触发
能否产生上游单据的核心在于 stock_move.procure_method 的值,默认为make_to_stock,copy=False。
如果 stock_move 由其他单据产生,比如 sale_order ,系统将根据Procurement及对应的 stock_rule,自动调整为make_to_order;
如果 stock_move 在界面直接产生,比如 mrp_production ,或者直接产生的一个 stock_picking ,那么在 _aciton_confirm 之前,需要调用_adjust_procure_method 方法,重新调整 procure_method

---

相关:[[Clippings/开源智造论坛/方案库/00-方案库索引.md|← 方案库索引]]
