---
title: "Odoo18月末一次加权平均生产成本计价mrp_cost_month_end"
source: "http://www.thinkltd.cn/forum/2/odoo18mrp-cost-month-end-4026"
forum: "模块库"
author: "肖相扶"
published: 2025-04-12
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo18月末一次加权平均生产成本计价mrp_cost_month_end

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2025-04-12
> <http://www.thinkltd.cn/forum/2/odoo18mrp-cost-month-end-4026>

模块链接：OSCG_Git\18.0\extra-addons\mrp_cost_month_end

【模块功能】

1.  半成品/产成品月末一次加权平均成本价格计算逻辑：
```python
    a) 先做制造费用分摊（参见 [全月制造费用分摊模块mrp_landed_costs_cn](http://www.thinkltd.cn/forum/2/mrp-landed-costs-cn-4019)），而后再做月末一次加权平均成本价格计算。
    b) 成本价格计算时候，先计算BoM层级为1的产品（原材料）的成本价格。BoM层级参考 [产品的BoM层级设置模块mrp_bom_level](http://www.thinkltd.cn/forum/2/bommrp-bom-level-4021)
    c) 再计算BoM层级为2的产品（半成品）的成本价格
    d) 依次类推，再计算BoM层级为3的成本价格
```

2.  本模块新增菜单“会计 --> 存货 --> 月末一次加权平均 --> 生产成本”，点击菜单，弹窗Wizard，为每个层级创建一个月末一次加权平均的计算表单。
3.  本模在月末一次加权平均计算表单上增加字段“BoM层级”，参考 [Odoo18月末一次加权平均成本计价方法stock_costs_month_end](http://www.thinkltd.cn/forum/2/odoo18stock-costs-month-end-4025)

【功能截图】

![[2-odoo18mrp-cost-month-end-4026-88af0bb5.png]]

## 补充/答案 1

新版本的方案会带来另一个问题，因为库存计价分摊的费用是独立的记录，而全月加权核算的时候没有再管到费用，所以只是原有价值的平均，从而如果实物都已经出完了，就会在库存计价里还留有余额无法带走

![[2-odoo18mrp-cost-month-end-4026-e822e4c8.png]]

这张示例是先做了费用分摊，然后再做的全月加权平均之后的库存计价，实物已经全部用完出完，但账上却挂着余额。

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
