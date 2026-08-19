---
title: "制造单(mrp.production)表单视图，大数据量下 性能下降原因"
source: "http://www.thinkltd.cn/forum/1/mrp-production-730"
forum: "求助台"
author: "施叶寒"
published: 2024-09-27
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 制造单(mrp.production)表单视图，大数据量下 性能下降原因

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:施叶寒 | 2024-09-27
> <http://www.thinkltd.cn/forum/1/mrp-production-730>

现象：

    产品数据过万的情况下，mrp.production表单视图 加载时/产品变更时，页面响应性能急速下降。

原因：

表单视图中存在一个隐藏字段，allowed_product_ids，用于给当前页面的product_id提供过滤条件。

经调查，服务器实际响应时间（提供allowed_product_ids数据的时间）处于毫秒级别；
然而，js依照服务器提供的数据，初始化的时候写入/onchange的时候加载 allowed_product_ids的时间处于秒级别。

因此，当页面不加载allowed_product_ids时，性能恢复正常；此时需要重写product_id的domain条件。

## 补充/答案 1

V17版本，MO明细行到一百多行，再加领料单，从领料单回到MO上，会要大概三分钟左右，特别慢。

解决办法：（施）

改了界面的视图：

mrp.production -- form

![[1-mrp-production-730-988b4019.png]]

mrp.production -- tree

![[1-mrp-production-730-77b6753f.png]]

注释了这些就快了。重点是那个明细组件的预计到货日期，它原本是隐藏的没显示，但就是它速度一下子就提上来了。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
