---
title: "Odoo标准模块stock_landed_cost功能介绍"
source: "http://www.thinkltd.cn/forum/2/odoostock-landed-cost-2461"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo标准模块stock_landed_cost功能介绍

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/odoostock-landed-cost-2461>

**系统目前的成本分摊（stock_landed_cost）只允许自动库存价值计算、先进先出成本法情况下使用。**

**案例分析：**

1.      采购入库单 WH/IN/00022入库Ham 8个，单价 5元；

2.      而后销售出库了3个，还剩下5个

3.      此时，收到采购入库的运费单10元，将其分摊到采购入库成本中

4.      10元分摊中，八分之五，即6.25元入库存商品，八分之三，即3.75元入销售成本。

**  系统分摊原理：**

1.      待摊总金额10元，系统将该值记入Stock Move的分摊值字段（landed_cost_value）；

2.      Stock Move总值增加 = (余数 / 总数) * 分摊值 = (5 / 8) * 10 = 6.25，总值 = 40 + 6.25

3.      分摊后余值增加 = 总值增加 = 6.25，余值 = 25 + 6.25

4.      分摊后单价 = 余值 / 余数 = (25 + 6.25) / 5 = 6.25

5.      分摊对应的会计分录：库存商品增加10 元，其中10 * (8 – 5) / 8 = 3.75 元已经出库，转为主营业务成本。

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
