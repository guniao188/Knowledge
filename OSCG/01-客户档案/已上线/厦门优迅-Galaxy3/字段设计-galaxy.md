---
title: galaxy
client: 厦门优迅-Galaxy3
type: 字段设计
module: 库存
status: 已完成
phase: 上线期
created: 2025-02-14
updated: 2025-02-14
yuque_url: "https://www.yuque.com/xinsuixiaoyao-degek/klxky6/vg7n330yyzlgc768"
tags: [Odoo, 上线期, 字段设计, 客户/厦门优迅-Galaxy3, 已完成, 库存, 报表, 采购, 销售]
---

# galaxy

1、销售订单remark和打印保持一致，remark靠左；

数量不要小数点；字段与excel一致；preview加item；

2、收货时不知道序列号，安装的时候才知道序列号。开发调整。

3、采购订单增加订单行之后销售订单不允许增加产品明细行，采购订单不允许增加修改采购订单。只能点确认。

4、采购订单的项目自动关联project，不允许手动创建purchase

销售订单、销售订单明细只能读、写，不允许改

5、待定供应商不能确定供应商，需要重新创建po，且关联到之前的销售订单
