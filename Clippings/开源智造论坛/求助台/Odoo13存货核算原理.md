---
title: "Odoo13存货核算原理"
source: "http://www.thinkltd.cn/forum/1/odoo13-440"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo13存货核算原理

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo13-440>

Odoo 12的存货核算原理参考这里：[/forum/2/question/odoostock-account-2450](http://www.thinkltd.cn/forum/2/question/odoostock-account-2450)

Odoo 13的存货核算和之前版本有很大改变：

1.  其一是，引入了新模型 stock.valuation.layer ，Odoo 12中，Stock Move上的 总数量、总价值、剩余数量、剩余价值 几个字段，转移到了该新模型上；Stock Move的每个Move Line，系统对应创建一条SVL记录。入库的SVL，数量为正数，出库的SVL数量为负数，DropShip的情况，系统同时创建一条入库SVL以及一条出库SVL。

2.  其二是，Stock Quant上新增了“价值( value )”字段，该字段的计算方法是：1) 如果是 FIFO 成本计算方法，系统用该产品的库存总价值除以库存总数量（汇总该产品的所有stock.valuation.layer 而得），得到单价，乘以Quant的数量，得到该Quant的价值。2) 移动平均、标准价 的成本计算方法，系统用Quant的数量乘以产品上的成本价格，作为该Quant的价值。

3.  其三是，anglo_saxon 相关的处理方法，从Invoice转移到了 Account Move模型上。

4.  采购入库的情况，Stock Move的price_unit字段总是从purchase_line_id 取值，SVL上的单价（unit_cost）的取值则和成本计算方法相关。标准法，unit_cost取自产品上的成本价格，移动加权平均、FIFO的情况，unit_cost取自Stock Move的price_unit，也就是采购单价（去税）。

5.  出库的情况（销售出库、采购退货等），Stock Move的price_unit总是0.0。SVL上的单价（unit_cost）的取值，标准法、移动加权平均法，unit_cost取自产品上的成本价格。FIFO法，系统按时间顺序从数量大于零的SVL上锁货，unit_cost取自所锁货的SVL的unit_cost （注意不是所锁Quant的成本价格）。

6.  非采购入库的情况，包括销售出库、采购退货、其他出入库等情况，Stock Move的price_unit都是0.0 。

![[1-odoo13-440-7e4dcbae.png]]

![[1-odoo13-440-14456fe1.png]]

## 补充/答案 1

V13先进先出，不会按实际出货的那条move当时的入库成本来计算凭证了吗？奇怪啊

如果实际出的并不是先进来的这批货，虽然总成本是无差异的，但对于销售订单来说，会有不同订单不同团队的成本问题，有什么办法可以按实际出货的成本来吗？

示例：

如图PO进来是12元未税，批次000012，000013二个产品

![[1-odoo13-440-3ea15a3c.png]]

因原来有进来过10元成本的产品，

而SO原本锁货是锁的之前尚未出完的10元成本的批次，但实际出货时，有优先出掉了这个000012的批次：

如图所示SO订单，

![[1-odoo13-440-7f99e8c5.png]]

但实际生成的凭证，仍按之前的成本来的，而非实际入库时该批次的成本，

![[1-odoo13-440-c317900d.png]]

新版本，总是按先进先出入库的来计算了么？而非实际发货的那笔产品，还是新改版后根本没有再考虑不同批次的问题了？

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
