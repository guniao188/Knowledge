---
title: "操作Stock Picking时候&#34;不能取消保留超过库存数量&#34;的错误解析"
source: "http://www.thinkltd.cn/forum/1/stock-picking-871"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 操作Stock Picking时候&#34;不能取消保留超过库存数量&#34;的错误解析

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/stock-picking-871>

【Bug现象】

如下图，Stock Picking上做任何操作（验证、取消保留、取消等等），系统总是提示下述错误：不能取消保留超过库存数量的 [FURN_8888] 办公台灯 产品 (It is not possible to unreserve more products of [FURN_8888] Office Lamp than you have in stock.) 导致该单据操作不了，无法进行下去。

![[1-stock-picking-871-919fc584.png]]

【Bug原因】

1.  如这个帖子  所说，原因是，1) Stock Move保留时候，系统根据下架规则，选择合适的stock.quant，从该Stock Quant上保留数量（记录在Stock Quant上的reserved_quantity字段上）；2) 系统同时创建Stock Move Line，保留数量记录在Stock Move Line的字段 product_qty上；3) Stock Move完成时候，系统从Stock Quant上扣除出库数量（可能大于保留数量），同时释放Stock Quant上的保留数量（字段reserved_quantity设为0）。4) 但是，释放保留数量时候，系统比较Stock Move Line上的保留数量product_qty，和Stock Quant上的保留数量reserved_quantity，如果product_qty大于reserved_quantity，则报此错误（正常情况下此二数量应该一致，但某些错误原因，可能导致不一致），从而完成不了Stock Move。

2.  再现此错误的一个方法是，直接数据库修改stock.quant上的reserved_quantity，使其低于stock move line的保留数量product_qty，即可产生此错误现象。

3.  错误解决方法：从数据库修改stock.move.line 的保留数 product_qty，使其和对应的stock.quant上的reserved_quantity 一致（或更小）即可。操作语句：env.cr.execute("update stock_move_line set product_qty=XX where id in (3332,3493)")   XX为正确的保留值，3332, 3493 为需要修改的Stock Move Line的id

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
