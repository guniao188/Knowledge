---
title: "StockMove合并到Picking上的原理"
source: "http://www.thinkltd.cn/forum/1/stockmovepicking-777"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# StockMove合并到Picking上的原理

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/stockmovepicking-777>

系统基于路线规则，MTO自动产生Stock Move，再把Stock Move合并到合适的Stock Picking上去。Picking合并的逻辑参考如下：

Odoo14.0 代码文件 odoo\addons\stock\models\stock_move.py  方法  def _search_picking_for_assignation(self)

![[1-stockmovepicking-777-83bf1ba1.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
