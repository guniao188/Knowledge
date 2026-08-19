---
title: "Odoo14销售订单明细行上库存预测的权限报错Bug"
source: "http://www.thinkltd.cn/forum/1/odoo14bug-718"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo14销售订单明细行上库存预测的权限报错Bug

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo14bug-718>

【问题背景】

记录规则限定当前用户只能看见自己的订单，此种情况，打开销售订单时候，销售订单明细行上的库存预测按钮。系统计算库存预测时候，需要汇总所有的入库、出库Stock Move的数量。在计算过程中，系统会read所有 Stock Move上的订单明细行(sale_line_id)，包括不属于当前用户的订单，此时因为权限问题报错。

![[1-odoo14bug-718-08c5a390.png]]

![[1-odoo14bug-718-3e3b2b42.png]]

【修复方法】

方法一：根据报错提示，文件 odoo14\odoo-server\addons\sale_stock\models\stock.py ，方法 def _get_source_document(self) 代码行 return self.sale_line_id.order_id or res  增加 sudo() 权限，改成：return self.sudo().sale_line_id.order_id or res

方法二：修改XML，去掉销售订单明细行上的库存预测功能

![[1-odoo14bug-718-882d218b.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
