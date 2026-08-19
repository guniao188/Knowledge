---
title: "OCA可承诺库存潜在库存计算stock_available、stock_available_unreserved、stock_available_mrp"
source: "http://www.thinkltd.cn/forum/2/ocastock-availablestock-available-unreservedstock-available-mrp-2883"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA可承诺库存潜在库存计算stock_available、stock_available_unreserved、stock_available_mrp

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocastock-availablestock-available-unreservedstock-available-mrp-2883>

模块链接：

产品上增加可承诺库存（Available to promise）和潜在库存（Potential）两个字段：

- 可承诺库存是立即可以发货的库存数量，默认情况下等于可用库存，但可以配置其他计算方法

- 潜在库存是，基于库存原料可以立即生产出来的库存数量

新增未被锁定的在手库存字段（qty_available_not_res）：

12.0版本：

-

-

-

This module allows users to check the quantity of a stocked product that is available on-hand, and that has not yet been reserved for use anywhere else.

This key figure is very important during the monitoring of the warehouse execution, because it assists users to ensure that the flow of products will not be stuck due to a sudden unavailability of stock.

If the warehouse personnel ensures that the unreserved quantity on hand > 0, then nobody will be stuck in pickings or manufacturing orders waiting for the availability of unreserved stock.

用在手原料基于BoM表计算可以立即生产的数量作为潜在库存（Potential）：

This module takes the potential quantities available for Products into account in the quantity available to promise, where the "Potential quantity" is the quantity that can be manufactured with the components immediately at hand. By configuration, the "Potential quantity" can be computed based on other product field. For example, "Potential quantity" can be the quantity that can be manufactured with the components available to promise.

## 补充/答案 1

## Stock available to promise

This module proposes several options to compute the quantity available to promise for each product. This quantity is based on the projected stock and, depending on the configuration, it can account for various data such as sales quotations or immediate production capacity. In case of immediate production capacity, it is possible to configure on which field the potential is computed, by default Quantity On Hand is used. This can be configured in Inventory > Configuration > Settings.

###

### Configuration

By default, this module computes the stock available to promise as the virtual stock. To take advantage of the additional features, you must define on which information you want to base the computation, by checking one or more boxes in the settings: Inventory > Configuration > Settings > Stock available to promise. In case of "Include the production potential", it is also possible to configure which field of product to use to compute the production potential.

###

### Usage

This module adds a field named Available for sale on the Product form. Various additional fields may be added, depending on which information you chose to base the computation on.


## 原帖外链配图

![[2-ocastock-availablestock-available-un-x194038c2.png]]
<small>原始地址: /web/image/1383/snipaste_20190217_141232.png?access_token=eacbc02f-cb2b-413c-84a0-77430fb0580d</small>

![[2-ocastock-availablestock-available-un-x194038c2.png]]
<small>原始地址: /web/image/1385/snipaste_20190217_141030.png?access_token=b1b22fdc-e8bd-4679-af61-450782ac2410</small>

![[2-ocastock-availablestock-available-un-x194038c2.png]]
<small>原始地址: /web/image/1387/snipaste_20190217_141435.png?access_token=85971ef4-b517-45c9-9b73-54a6b0b32b16</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
