---
title: "LGC Work Order功能描述"
client: lgc
type: 项目文档
phase: 实施期
yuque_url: "https://www.yuque.com/xinsuixiaoyao-degek/klxky6/ntekts77xf9n8nwm"
yuque_slug: "ntekts77xf9n8nwm"
tags: [Odoo, 实施期, 客户/lgc, 正在实施]
created_at: "2026-01-23T05:34:55.000Z"
updated_at: "2026-01-26T11:03:10.000Z"
published_at: "2026-01-23T06:51:15.000Z"
---
# LGC Work Order功能描述

1、产品维护optional products及对应的数量，在创建订单保存时，会自动增加明细行

![image](_附件/1769147597820-6aa6fa3d-1280-4be6-b3fa-18-75adbe41bb7a250c.png)

增加wage字段，用于维护service 产品的内部cost,该字段仅在产品类型为service时可见。

![image](_附件/1769147634312-b3b5f9c2-22e9-4082-9670-43-0dd148f4d6584da8.png)

2、订单上可以快速查看订单中的service类型的明细（除price discount）

在订单上可填写Supervisor，此处对应的是employee，需要维护员工之后才能选择

![image](_附件/1769148042095-24aa7956-b832-46b5-a282-13-6de526780ef4b4b1.png)

![image](_附件/1769148996330-c2f91243-4450-4a6b-87bc-40-06922a3e64eab151.png)3、从销售订单处打印工单，样式如下：![image](_附件/1769148111977-37becd99-9fd7-4a20-a35b-a4-e439f563484aadc7.png)![image](_附件/1769148445168-09cdd3b8-a5f6-4964-b5f5-2f-2019d67409fc4026.png)

4、增加work order菜单，此处显示所有的service 产品（除price discount）的销售明细![image](_附件/1769149056374-d48098df-721f-482c-8109-71-260521415e4430e5.png)

5、报工：批量选择需要报工的明细，点击finish，即可写入finished time![image](_附件/1769149932083-9442c556-176d-4bec-a3c4-73-bc1a2112f0740313.png)

6、创建工资单:此界面显示的为已完成报工，但未创建工资单的work order

![image](_附件/1769150099699-6972dd2f-724b-455a-972b-e6-5ab37f3d2627e634.png)

可以批量选择后，点击create wrokorder invoice，即会创建一张bill。只可选择同一个员工的工资单。创建后，则不会再出现在该菜单中。![image](_附件/1769150432170-f830c1e1-2671-41ed-b6df-da-9e69560b71e40f33.png)

点击按钮后，会自动跳转到这张账单上，可以补充工资单的时间和供应商

注：如果该产品有税，则维护在service产品的purchase tax处。如有维护，工资单会填充税及计算总计金额![image](_附件/1769150529408-71b425e1-c6f1-476a-b382-78-76fcc52b4be61bdb.png)

点击打印，生成工资单![image](_附件/1769150579420-968287f4-61b6-44dd-80e1-7d-faf312252b05c4a6.png)![image](_附件/1769150668227-bed34357-7ac0-4f18-86b4-79-9080fad7f7b41f43.png)

员工地址、email等类型方式的维护：![image](_附件/1769150774202-d248effa-c76a-4dcc-a365-bc-318435494932bec5.png)

员工增加了一个work order partner字段，需要增加一个该员工的联系人，然后在此处绑定。用于生成工资invoice的vendor信息。

7、工资单统计

增加菜单：Employee Invoice,汇总所有的工资单![image](_附件/1769150806838-82f76da4-e677-4afd-9aad-7a-b1b0b06aafa551c6.png)

![image](_附件/1769150839697-e35d2c0c-1c0e-400b-82e6-ae-8c1e99baeec5191a.png)
