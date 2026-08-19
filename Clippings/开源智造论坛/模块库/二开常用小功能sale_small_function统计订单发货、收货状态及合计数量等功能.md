---
title: "二开常用小功能sale_small_function统计订单发货、收货状态及合计数量等功能"
source: "http://www.thinkltd.cn/forum/2/sale-small-function-3557"
forum: "模块库"
author: "符赛红"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开常用小功能sale_small_function统计订单发货、收货状态及合计数量等功能

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:符赛红 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/sale-small-function-3557>

销售及会计上、采购收货状态、bom备注等细节调整：
========================================================
客户发票上的【发票号】去除唯一性校验及字符长度修改;
销售订单上计算合计数量及交货数量合计，以及交货状态的判断计算，比较；（有排除服务类的产品）
采购订单上计算合计数量及收货数量合计，以及收货状态的计算，比较;（有排除服务类的产品）
改写picking上的联系人可索引，用于group by分组；
bom上增加备注，并带入到生产订单物料明细行上。

功能存储在：

D:\svn\SVN\odoo_ecommerce\15.0SRC\销售\sale_small_function

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
