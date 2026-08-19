---
title: "越库发货(为SO分配专用库位) stock_reserve_location"
source: "http://www.thinkltd.cn/forum/2/so-stock-reserve-location-3451"
forum: "模块库"
author: "肖相扶"
published: 2024-05-10
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 越库发货(为SO分配专用库位) stock_reserve_location

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2024-05-10
> <http://www.thinkltd.cn/forum/2/so-stock-reserve-location-3451>

模块位置：OSCG_SVN\odoo_ecommerce\14.0SRC\仓库物流\stock_reserve_location

【20240510周鸿飞升级到17.0版】17.0版位置：OSCG_GIT\extra-addons\17.0\stock_reserve_location

【业务背景】

1.  杭州迅得电子，PCB小批量定制化生产，接到订单后，订单需要的原料有两个来源：大部分（80%）需要按单采购，少量常规品种会备库存。有些芯片类物料，采购周期较长。订单从接单到备齐物料，周期大概30天。

2.  生产备料方法是，为每个SO订单分配一个库位，常规类料号，从备货区拣货到订单专用库位，采购类料号，采购入库时候，直接上架到订单专用库位。生产领料时候，直接从订单专用库位领料。

【模块功能】

1.      补货组上增加库位字段(location_id)

2.      Stock Move入库时候，如果Stock Move的补货组上有库位，则按此库位上架入库

3.      Stock Move锁货时候，如果Stock Move的补货组上有库位，则按此库位下架锁货

【模块应用】

为MTO类SO分配专用库位，该SO引发的物料采购，入库到该专用库位，该SO从该专用库位发货。实现方法是，安装本模块，且1）SO确认时候，系统会自动创建一个以SO单位为名的补货组，写一个自动动作，为该补货组分配一个专用库位；2）系统自带的购买规则，补货组传播设置为“传播”。3）SO引发生产MO，MO再引发采购的情况，分两步采购入库，第一步入库到收货区，第二步入库到订单库位区，上架到订单专用库位。4) 参考：[/forum/1/question/somo-picking-po-picking-757](http://www.thinkltd.cn/forum/1/question/somo-picking-po-picking-757)

## 补充/答案 1

【应用实例】

1.  先安装自动动作模块，再安装模块 stock_reserve_location、\stock_mrp_tracking_so\\ \\\以\及\\nbsp\\\\\[stock_procurement_fix]()

2.  仓库分为备货区、订单区

3.  SO订单确认时候，从订单区查找一个空的子库位分配给订单

4.  配置规则：销售发货时候从订单区发货，订单区缺货时候从备货区调拨，备货区缺货时候购买

5.  采购收货的作业类型，默认目标库位改成 备货区

6.  实现效果：SO订单确认后，系统自动为SO分配一个库位；系统自动产生一个备货区到订单库位的调拨单，缺料的产品，系统自动产生采购询价单，采购入库到备货区。

【操作截图】

![[2-so-stock-reserve-location-3451-f4efdc3f.png]]

![[2-so-stock-reserve-location-3451-467f1567.png]]

![[2-so-stock-reserve-location-3451-22436836.png]]

销售确认引发的Picking单

![[2-so-stock-reserve-location-3451-4ef07674.png]]

备货区调拨到订单分配的库位

![[2-so-stock-reserve-location-3451-42c4207c.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
