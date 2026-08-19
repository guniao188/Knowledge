---
title: "请技术研发调查一下V13的这个【预测】库存的计算逻辑report.stock.quantity"
source: "http://www.thinkltd.cn/forum/1/v13report-stock-quantity-591"
forum: "求助台"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 请技术研发调查一下V13的这个【预测】库存的计算逻辑report.stock.quantity

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/v13report-stock-quantity-591>

请技术研发调查一下V13的这个【预测】库存的计算逻辑，这些数字是如何推算出来的？

![[1-v13report-stock-quantity-591-305548d0.png]]

是哪些地方的数字会影响这里的计算？

## 补充/答案 1

你测试一下，看看是不是就是预测库存：截止到几月几日的预测库存，也就是在手库存 加减 date <= 截止日 的未done的Stock Move数量。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
