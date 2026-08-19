---
title: "Odoo17采购、质量改善点一览"
source: "http://www.thinkltd.cn/forum/1/odoo17-3829"
forum: "求助台"
author: "肖相扶"
published: 2024-04-10
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo17采购、质量改善点一览

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-04-10
> <http://www.thinkltd.cn/forum/1/odoo17-3829>

返回  [Odoo17改善点列表](http://www.thinkltd.cn/forum/1/odoo17-3808)

#### 采购折扣

产品上的供应商价格表增加折扣字段，采购明细行上也增加折扣字段。默认将折扣带入明细行，明细行上还可以进一步修改。

![[1-odoo17-3829-8edc447c.png]]

#### 从产品目录快速添加批量添加产品到PO

和销售订单类似，增加了从产品列表快速添加产品到PO的功能。

#### 不良品(质检不通过)库位

a) 质量控制点（QCP单）增加了按数量质检的方式，如果选择该方式，QCP上可以设置不良品库位。b) Picking的质检弹窗上，可以填写质检不通过数量，以及不良品库位。c) 系统自动分拆入库明细，良品数量正常入库，分拆不良品数量入库到不良品库位。不过此功能有个小Bug，Bug现象及修改方法参考： [Odoo17按数量质检不良品库位Bug修复](http://www.thinkltd.cn/forum/1/odoo17bug-3832) 

![[1-odoo17-3829-3e2d6263.png]]

![[1-odoo17-3829-03d6364b.png]]

 

![[1-odoo17-3829-3bed6941.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
