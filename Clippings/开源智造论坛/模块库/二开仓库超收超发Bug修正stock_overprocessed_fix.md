---
title: "二开仓库超收超发Bug修正stock_overprocessed_fix"
source: "http://www.thinkltd.cn/forum/2/bugstock-overprocessed-fix-3278"
forum: "模块库"
author: "肖相扶"
published: 2022-12-16
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开仓库超收超发Bug修正stock_overprocessed_fix

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-16
> <http://www.thinkltd.cn/forum/2/bugstock-overprocessed-fix-3278>

SVN路径：OSCG_SVN\proj\odoo_ecommerce\13.0SRC\stock_overprocessed_fix

【问题背景】

1.  Odoo仓库超收超发控制功能参考这里： [/forum/1/question/343](http://www.thinkltd.cn/forum/1/question/343)

2.  [超收超发控制功能实现原理参考这里：](http://www.thinkltd.cn/forum/1/question/343)[/forum/1/question/bugextra-new-move-363]()

3.  [V12.0的Bug修复参考这里：/forum/2/question/odoo12stock-barcode-show-total-3147]()

4.  V13.0中，Stock Picking Type上增加了配置项 Pre-fill Detailed Operations，如果不勾选，则Picking锁货后，不显示锁货的作业明细。当扫码出入库时候，不显示锁货作业明细是非常合适的（按实际扫码结果出入库，而不是按锁货明细出入库）。

5.  但是，如果不勾选 Pre-fill Detailed Operations，扫码或手工添加的作业明细行，锁货数量（字段 product_uom_qty）永远是 0，明细行上的实际收发数量（quantity_done）总是大于product_uom_qty，超收超发判断功能失效了。

【模块设计】

1.  继承 stock\models\stock_picking.py 的方法 def _get_overprocessed_stock_moves(self) ，重写超收超发判断逻辑。
    比较作业明细（move_line_ids）和初始数量明细（move_lines），如果move_line_ids的产品多于move_lines，或者某个产品的完成数**汇总**超出了move_line_ids中该产品的初始数量**汇总**，则判定为超出。

2.  如果Picking没有move_lines（即时调拨的情况），不判定为超出。

![[2-bugstock-overprocessed-fix-3278-920e7f08.png]]

![[2-bugstock-overprocessed-fix-3278-4c6daf3a.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
