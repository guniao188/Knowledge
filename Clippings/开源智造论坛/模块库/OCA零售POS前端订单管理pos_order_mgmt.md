---
title: "OCA零售POS前端订单管理pos_order_mgmt"
source: "http://www.thinkltd.cn/forum/2/ocapospos-order-mgmt-3158"
forum: "模块库"
author: "施叶寒"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA零售POS前端订单管理pos_order_mgmt

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:施叶寒 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocapospos-order-mgmt-3158>

1. 模块存放位置：

2. 使用场景： 无特定场景，对point_of_sale的功能补充。

3. 实现新功能包括：再次打印小票、复制已有零售单、生成退货单。

4. 实现思路：
```python
    1）再次打印小票: action_print,获取指定的pos.order,调用源码ReceiptScreenWidget的print方法（如果存在posbox,打印小票)/show方法（如果不存在，展示小票）
    2）复制已有零售单: action_copy,获取指定的pos.order,在js环境生成一张新的零售单，并设为当前零售单。
    主要关注：_prepare_order_from_order_data()
    3）生成退货单: action_copy,获取指定的pos.order,在js环境生成一张新的零售单（数量为负），并设为当前零售单。
    主要关注：_prepare_order_from_order_data()
```

5. 依赖：
模块：point_of_sale

6.截图：

![[2-ocapospos-order-mgmt-3158-1e9ec79a.png]]

![[2-ocapospos-order-mgmt-3158-d44802e1.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
