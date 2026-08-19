---
title: "OCA 自动合并在一个指定时间段内MTO产生的MO  mrp_production_grouped_by_product"
source: "http://www.thinkltd.cn/forum/2/oca-mtomo-mrp-production-grouped-by-product-3092"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA 自动合并在一个指定时间段内MTO产生的MO  mrp_production_grouped_by_product

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/oca-mtomo-mrp-production-grouped-by-product-3092>

模块链接：

When you have several sales orders with make to order (MTO) products that require to be manufactured, you end up with one manufacturing order for each of these sales orders, which is very bad for the management.

With this module, each time an MTO manufacturing order is required to be created, it first checks that there's no other existing order not yet started for the same product and bill of materials inside the specied time frame , and if there's one, then the quantity of that order is increased instead of creating a new one.

## [Configuration](https://github.com/OCA/manufacture/tree/12.0/mrp_production_grouped_by_product#id1)

To configure the time frame for grouping manufacturing order:

1.  Go to *Inventory > Configuration > Warehouse Management > Operation Types*

2.  Locate the manufacturing type you are using (default one is called "Manufacturing").

3.  Open it and change these 2 values:

    - MO grouping max. hour (UTC): The maximum hour (between 0 and 23) for considering new manufacturing orders inside the same interval period, and thus being grouped on the same MO. IMPORTANT: The hour should be expressed in UTC.
    - MO grouping interval (days): The number of days for grouping together on the same manufacturing order.

    Example: If you leave the default values 19 and 1, all the planned orders between 19:00:01 of the previous day and 20:00:00 of the target date will be grouped together.

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
