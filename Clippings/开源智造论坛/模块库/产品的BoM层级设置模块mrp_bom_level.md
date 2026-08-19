---
title: "产品的BoM层级设置模块mrp_bom_level"
source: "http://www.thinkltd.cn/forum/2/bommrp-bom-level-4021"
forum: "模块库"
author: "肖相扶"
published: 2025-01-06
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 产品的BoM层级设置模块mrp_bom_level

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2025-01-06
> <http://www.thinkltd.cn/forum/2/bommrp-bom-level-4021>

模块链接：OSCG_Git\18.0\extra-addons\mrp_bom_level

【模块功能】

1.  产品上增加BoM层级字段。
2.  增加菜单“会计 --> 存货 --> 配置 --> BoM层级设置”，自动计算并设置产品的BoM层级。 本模块依赖 模块stock_account_category ： [库存计价上增加业务分类功能模块stock_account_category](http://www.thinkltd.cn/forum/2/stock-account-category-4022)。“会计 --> 存货“菜单由模块 stock_account_category添加。
3.  产品BoM层级计算逻辑：基于制造BoM表，从最底层到最上层，重新计算产品的BoM层级。原材料层数为1，直接由原材料构成的产品层数为2，BoM中含有层数2的产品则该产品的层数为3，如此类推。
4.  BoM层级主要应用于月末一次加权平均的生产成本计算，以及生产成本的料工费分析。

【功能截图】

![[2-bommrp-bom-level-4021-0f508e88.png]]

![[2-bommrp-bom-level-4021-2b985f68.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
