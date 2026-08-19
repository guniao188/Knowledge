---
title: "生产订单MO分拆模块mrp_production_split"
source: "http://www.thinkltd.cn/forum/2/momrp-production-split-3480"
forum: "模块库"
author: "肖相扶"
published: 2023-03-30
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 生产订单MO分拆模块mrp_production_split

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2023-03-30
> <http://www.thinkltd.cn/forum/2/momrp-production-split-3480>

模块链接：OSCG_SVN\odoo_ecommerce\14.0SRC\生产制造\mrp_production_split

【业务背景】

1.  业务场景1：大生产订单分拆为若干小生产订单。MTO类型制造产品，SO确认时候，系统自动创建对应的MO，有时候，SO数量极大，需要将对应MO分拆为若干个小MO，小MO安排到不同时间段生产，或者安排到不同车间产线生产。此场景参考深圳五洲行案例 [生产单MO排产优化mrp_production_plan](http://www.thinkltd.cn/forum/2/question/momrp-production-plan-3374)

2.  业务场景2：化工类生产，同样的原料投入，计划生产A，实际可能产出若干A、若干B、若干C。一种解决办法是，将原来计划生产A的MO分拆为三个小MO，分别生产A、B、C 。此场景有实际案例 杭州诺瓦特伦、绍兴亿德新材料。

3.  机加行业按下料后的框数分拆MO（功能待开发），方案参考  [机械加工行业生产管理参考方案](http://www.thinkltd.cn/forum/1/3659)

【模块功能】

1.  生产订单MO上增加按钮“拆单”，点击按钮弹窗，填写分拆MO的作业类型、产成品、分拆数量

2.  如果不填作业类型、产品，则默认取原生产订单的作业类型和产品。即只拆数量，不改变作业类型和产品

3.  分拆出的新MO，   其单号是原MO单号加后缀 "-Sn"，n是流水号，取值 1, 2, 3 ... 。分拆后，自动取消原MO

4.  分拆出的MO，投料Stock Move的源库位取填写的作业类型的默认源库位，成品入库的Stock Move的目标库位取作业类型的默认目标库位

5.  如果填写了分拆产品，则分拆出的新MO的产品不同于原MO，包括成品入库的Stock Move的产品也会改成新的产品

6.  分拆后的MO，系统仍会维持新MO的投料Stock Move，成品入库Stock Move的MTO上下游关系。MTO上下游关系说明参考：[MTO产生的上下游StockMove间的内部关系原理](http://www.thinkltd.cn/forum/1/question/mtostockmove-782)

7.   分拆出的MO，投料Stock Move、入库Stock Move的数量，系统按分拆数量与分拆前MO数量比例调整。

【功能截图】

![[2-momrp-production-split-3480-4afd231a.png]]

![[2-momrp-production-split-3480-24989455.png]]

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
