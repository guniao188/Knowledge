---
title: "PG高级功能例解WITH、COALESCE、LATERAL 用法"
source: "http://www.thinkltd.cn/forum/1/pgwithcoalescelateral-877"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# PG高级功能例解WITH、COALESCE、LATERAL 用法

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/pgwithcoalescelateral-877>

【用法说明】

【示例截图】

WITH move_type as (

select sm.id, sm.product_id, sm.date, spt.code from stock_move sm

left join stock_picking sp on (sm.picking_id = sp.id)

left join stock_picking_type spt on (sp.picking_type_id = spt.id)

)

select pp.id as pid, pp.default_code as pcode, COALESCE(smt.date, pp.create_date) as date

from product_product pp

 left join LATERAL (select date from move_type where product_id = pp.id and code = 'incoming' order by date limit 1) smt on true

![[1-pgwithcoalescelateral-877-a0b86db3.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
