---
title: "MPS筛选条件"
source: "http://www.thinkltd.cn/forum/1/mps-913"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# MPS筛选条件

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/mps-913>

【业务背景】

主生产计划（MPS）画面，批量添加了几千个产品。希望有个筛选功能，例如只显示负数库存的产品的MPS。

【实现方法】

1.  MPS画面显示的是模型mrp.production.schedule 的数据。创建一个服务器动作，筛选负库存的产品的mps，而后跳转到MPS显示画面

2.  MPS菜单下面添加一个子菜单，该子菜单关联上述服务器动作

3.  服务器动作示例代码：

mps_ids = model.search([('product_id.virtual_available', '<', 0)])

domain = [('id', 'in', mps_ids.ids)]

action = env.ref('mrp_mps.action_mrp_mps').read()[0]

action['domain'] = domain

【配置示例】

![[1-mps-913-57e35bc2.png]]

![[1-mps-913-d041d6c7.png]]

![[1-mps-913-cb3c0599.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
