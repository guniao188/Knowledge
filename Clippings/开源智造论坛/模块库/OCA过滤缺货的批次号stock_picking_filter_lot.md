---
title: "OCA过滤缺货的批次号stock_picking_filter_lot"
source: "http://www.thinkltd.cn/forum/2/ocastock-picking-filter-lot-2556"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA过滤缺货的批次号stock_picking_filter_lot

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocastock-picking-filter-lot-2556>

模块链接：

Odoo 12.0版本（V13应该可以直接安装）：

此模块在Picking上选择批次时候，下拉框仅显示有货的批次号码。

【功能原理】

批次上增加了一个库位的计算型字段

视图上批次字段增加Domain，只显示库位属于源库位儿子的批次。

## 补充/答案 1

这个模块有个问题，会限制住采购入库时，无法再入之前入过的批次，因为之前的批次很有可能无库存。即这模块只考虑了销售，但因为视图是共用的，没有考虑采购。

需要在采购时，将作业类型上勾选，显示出详细作业来临时解决这个限制问题。

而销售出库单作业类型不要显示详细作业。


## 原帖外链配图

![[2-ocastock-picking-filter-lot-2556-x194038c2.png]]
<small>原始地址: /web/image/829/snipaste_20190119_181007.png?access_token=32eb2e7d-83d9-42ad-88bd-d6555e8c0c96</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
