---
title: "OCA Picking单拆分stock_split_picking"
source: "http://www.thinkltd.cn/forum/2/oca-pickingstock-split-picking-2527"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA Picking单拆分stock_split_picking

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/oca-pickingstock-split-picking-2527>

模块链接：[https://github.com/OCA/stock-logistics-workflow/tree/12.0/stock_split_picking
](https://github.com/OCA/stock-logistics-workflow/tree/12.0/stock_split_picking)

Odoo13.0版本：[https://github.com/OCA/stock-logistics-workflow/tree/13.0/stock_split_picking
](https://github.com/OCA/stock-logistics-workflow/tree/13.0/stock_split_picking)

Odoo 14.0版本：OSCG_SVN\odoo_ecommerce\14.0SRC\仓库物流\stock_split_picking

1.  可用状态的Stock Picking上增加按钮“Split”，Picking的完成列填写完成数量，点击“Split”，系统按完成列数量拆分Picking，形成两个Picking，两个Picking都为可用状态，且互为Back Order
2.  Go to **Inventory** dashboard and open any picking.
3.  If picking state is **available** you can see an split button.
4.  On the "Operations" tab, fill the field "Done" to the quantity you want to split for each line.
5.  If you click on **Split** button, wizard will split current picking into two different pickings depends on quantity done you entered above.
6.  Both pickings remain confirmed.

 【功能截图】

![[2-oca-pickingstock-split-picking-2527-f9bc226f.png]]

## 补充/答案 1

官方已经升级最新的Odoo14版本支持，详见网址：https://apps.odoo.com/apps/modules/14.0/stock_split_picking/


## 原帖外链配图

![[2-oca-pickingstock-split-picking-2527-x194038c2.png]]
<small>原始地址: /web/image/789/snipaste_20190119_101141.png?access_token=331dc314-9c1d-4cc0-839d-201a245ed016</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
