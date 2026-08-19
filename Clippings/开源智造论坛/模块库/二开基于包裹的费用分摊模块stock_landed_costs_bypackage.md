---
title: "二开基于包裹的费用分摊模块stock_landed_costs_bypackage"
source: "http://www.thinkltd.cn/forum/2/stock-landed-costs-bypackage-3297"
forum: "模块库"
author: "肖相扶"
published: 2022-12-16
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开基于包裹的费用分摊模块stock_landed_costs_bypackage

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-16
> <http://www.thinkltd.cn/forum/2/stock-landed-costs-bypackage-3297>

模块链接：OSCG_SVN\odoo_ecommerce\13.0SRC\存货核算\stock_landed_costs_bypackage

【模块功能】

1.  成本分摊表单上，增加分摊到包裹的功能。费用明细行上，增加包裹列，费用摊入指定包裹。

2.  如果费用明细行上不指定包裹，系统自动从分摊单上的Picking单据(字段 picking_ids) 获取所有包裹(Stock Move Line的 result_package_id 字段)

3.  本模块依赖模块：[基于包裹的个别计价法模块stock_cost_bypackage](http://www.thinkltd.cn/forum/2/question/stock-cost-bypackage-3294)、[分摊单增强模块stock_landed_costs_improved](http://www.thinkltd.cn/forum/2/question/stock-landed-costs-improved-3295)

## 补充/答案 1

【功能截图】

费用分摊单的费用明细行上增加“包裹列”

![[2-stock-landed-costs-bypackage-3297-f61d156a.png]]

分摊明细上增加包裹字段：

![[2-stock-landed-costs-bypackage-3297-ea01f726.png]]

分摊产生的SVL：

![[2-stock-landed-costs-bypackage-3297-bffb10a0.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
