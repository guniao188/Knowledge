---
title: "二开基于包裹的个别计价法stock_cost_bypackage"
source: "http://www.thinkltd.cn/forum/2/stock-cost-bypackage-3294"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开基于包裹的个别计价法stock_cost_bypackage

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/stock-cost-bypackage-3294>

模块链接： OSCG_SVN\odoo_ecommerce\13.0SRC\存货核算\stock_cost_bypackage

【模块功能】

 1) 产品、产品分类上，增加“个别计价法”的成本核算方法勾选项
 2) 入库时候，如果产品是个别计价法，则包裹是必输字段。Odoo标准功能是为每个Stock Move生成一条计价记录（Stock Valuation Level）。如果勾选了个别计价法，本模块为每个包裹（Stock Move Line）生成一条计价记录(SVL)
3) 出库时候，Odoo标准功能是，按先进先出规则，匹配SVL，获得出库成本。如果勾选了个别计价法，本模块按包裹号码匹配SVL，取得包裹出库成本。

【功能截图】

产品和分类上增加“个别计价法”的勾选项

![[2-stock-cost-bypackage-3294-1c759ab4.png]]

按包裹生成存货价值（SVL），SVL上增加“包裹字段”：

![[2-stock-cost-bypackage-3294-7ed3340e.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
