---
title: "研究一下库存这块：如何在move或move line那里下拉选择有库存的批次"
source: "http://www.thinkltd.cn/forum/1/movemove-line-361"
forum: "求助台"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 研究一下库存这块：如何在move或move line那里下拉选择有库存的批次

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/movemove-line-361>

有插件可以在move line下拉选择中只出现有库存的批次号，但是操作过程中仍然需要再去查询库存才能知道这个批次到底该出多少合适

V12版本批次

是否有办法可以在下拉的批次中显示该批次对应的内部库存数量，或者下拉搜索更多中窗口列表中可以显示库存数量？

或者是在选择产品时，能过滤查看产品的库存及库存所在的位置及批次？

V10版本

## 补充/答案 1

操作方案改变一下，不要直接选择批次，而是改成选择Quant，按Quant锁货，参考这个模块 [/forum/2/question/ocaquantstock-quant-manual-assign-2870](http://www.thinkltd.cn/forum/2/question/ocaquantstock-quant-manual-assign-2870)  。该模块的Quant选择视图上，只要XML改一下，显示Quant上的批次，即可满足需求。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
