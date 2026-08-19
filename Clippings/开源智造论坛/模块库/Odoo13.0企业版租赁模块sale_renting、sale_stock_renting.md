---
title: "Odoo13.0企业版租赁模块sale_renting、sale_stock_renting"
source: "http://www.thinkltd.cn/forum/2/odoo13-0sale-rentingsale-stock-renting-3357"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo13.0企业版租赁模块sale_renting、sale_stock_renting

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/odoo13-0sale-rentingsale-stock-renting-3357>

【模块功能】

1.  产品上增加了字段“可租赁Can be Rented”，以及租赁页签“Rental”，该页签有租赁价格、超时价格、两次租赁之间的安全时间（小时）
    扩展了销售订单 sale.order 的功能，使得可以处理租赁类的销售业务。SO明细行上添加可租赁的产品时候，系统自动弹出租期及价格填写的窗口，填写租期和价格。填写好以后，系统自动在SO Line的说明列显示从什么时候出租到什么时候。**注意：要正确设置用户的时区，系统使用用户时区显示时间**。

2.  销售订单行上，系统增加了一些和租赁相关的字段：is_rental：是否出租，pickup_date：出租时间，return_date：收回时间，is_late：是否延期了。

3.  模块sale_stock_renting，增加了仓库相关功能：1）出租时候（Pick Up按钮），系统背后自动创建一条调拨的Stock Move，从主仓库调拨到Rental仓库。2）归还时候（Return），自动创建Rental库位到主仓库的Stock Move。3）增加了出租设备的序列码功能。

4.  本模块可以在社区版安装，但有一个菜单“Schedule”需要依赖企业版模块 web_gantt，需要将模块web_gantt挪移到社区版，安装。

## 补充/答案 1

以甘特图形式，显示每个产品的出租订单

![[2-odoo13-0sale-rentingsale-stock-renting-3357-dcdae53a.png]]

## 补充/答案 2

【功能截图】

增加租赁功能模块：

![[2-odoo13-0sale-rentingsale-stock-renting-3357-e5c796d0.png]]

增加租赁模块，产品上增加租赁页签

![[2-odoo13-0sale-rentingsale-stock-renting-3357-61c418d6.png]]

销售订单添加明细行时候，如果是租赁产品，系统自动弹出填写租赁时间：

![[2-odoo13-0sale-rentingsale-stock-renting-3357-fd64bb19.png]]

![[2-odoo13-0sale-rentingsale-stock-renting-3357-737518ae.png]]

![[2-odoo13-0sale-rentingsale-stock-renting-3357-184eafad.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
