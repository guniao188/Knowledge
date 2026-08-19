---
title: "Odoo17生产制造改善点一览"
source: "http://www.thinkltd.cn/forum/1/odoo17-3814"
forum: "求助台"
author: "肖相扶"
published: 2024-04-10
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo17生产制造改善点一览

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-04-10
> <http://www.thinkltd.cn/forum/1/odoo17-3814>

返回  [Odoo17改善点列表](http://www.thinkltd.cn/forum/1/odoo17-3808)

1.  BOM更新
    a) MO上增加自动生成BoM的功能。b) BoM有修改时候，MO上增加更新按钮，点击按钮自动将BoM修改反映到MO上。c) MO上增加动作自动创建ECO。

![[1-odoo17-3814-4915b374.png]]

  

![[1-odoo17-3814-13c58531.png]]

 

![[1-odoo17-3814-de29f08b.png]]

2.  生产组件需求传导
    两步生产时候，MO的需求数量，自动传导到领料单上（两步生产的Pre-Production(车间库位)配置了MTO路线）。
3.  新增MO概览功能
    新增MO概览功能，在一个报表上显示缺货数量、补货单据、实际成本、理论成本、计划到货日期/实际到货日期。

![[1-odoo17-3814-c8e123a6.png]]

4.  用户操作界面改善
    制造提前期移到了BoM上（而不是产品上）；MO列表上增加了“检查可用”按钮；MO Form视图上增加了 预计结束日期 字段，以及标签打印Print Label按钮。
5.  生产计划
    基于预计的到料日期排定MO生产计划。MO搜索视图中，新增'Late Components' 过滤器，筛选有到料延迟的MO。'Planning by Production' 视图显示工单间的依赖关系。

![[1-odoo17-3814-a4fec004.png]]

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
