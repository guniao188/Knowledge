---
title: "重复Email、电话手机的Partner检测（重复客户联系人检测）"
source: "http://www.thinkltd.cn/forum/2/emailpartner-3612"
forum: "模块库"
author: "肖相扶"
published: 2022-12-21
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 重复Email、电话手机的Partner检测（重复客户联系人检测）

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-21
> <http://www.thinkltd.cn/forum/2/emailpartner-3612>

模块链接：[https://gitlab.com/oscg-china/extra-addons/-/tree/16.0/crm_same_partners](https://gitlab.com/oscg-china/extra-addons/-/tree/16.0/crm_same_partners)

【模块功能】

1.  销售在客户开拓过程中，经常出现的问题是，重复创建客户，重复创建联系人，客户公司和其下面的联系人邮箱、电话、手机相同。
2.  正常情况下，客户及联系人的Email、电话、手机不应相同，但某些特殊情况下，允许相同，例如，同一个人，在不同公司担任职务，这种情况，两个客户公司，但它们拥有同一个联系人。
3.  Odoo中如果存在Partner Email重复情况，给该Partner发邮件时候，邮件发不出去。以及接收该重复Email的邮件时候，收到的邮件系统不知道该挂到哪个Partner上。因此Email重复情况，对于和邮件系统集成是极大隐患。
4.  本模块新增功能：普通用户创建、修改客户及联系人（ Partner ）时候，如果存在相同Emai或电话或手机的Partner，系统报错，不予创建/修改。拥有销售管理员权限的用户则不做此检测，特殊情况下的重复联系人，可以由销售管理员负责创建。
5.  对于既存的Partner，本模块提供了两个服务器动作“检测重复Email的Partner”，“检测重复电话手机的Partner”。销售管理员有权限使用此服务器动作筛选重复Partner，而后手动纠正。
6.  本模块还提供了一个“计划动作”，默认每10天自动给Partner按成交情况（销售订单）分级打标签。有三种标签：“从未成交”，“一年前有成交”，“一年内有成交”。

【功能截图】

![[2-emailpartner-3612-72830824.png]]

![[2-emailpartner-3612-c5bd7999.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
