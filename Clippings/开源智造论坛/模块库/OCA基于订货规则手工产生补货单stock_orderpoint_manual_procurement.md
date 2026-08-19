---
title: "OCA基于订货规则手工产生补货单stock_orderpoint_manual_procurement"
source: "http://www.thinkltd.cn/forum/2/ocastock-orderpoint-manual-procurement-2858"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA基于订货规则手工产生补货单stock_orderpoint_manual_procurement

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/ocastock-orderpoint-manual-procurement-2858>

模块链接：

当安全库存不太准确时候，系统自动计算的订货数量容易脱离实际。本模块增加手工发起订货的功能（而不是总是自动订货）。安全库存规则（再订货规则）上，显示系统计算出来的理论订货数量，允许手工修改订货数量，手工启动订货流程。

本模块在12.0可以安装，但需要修改两处代码：一个是文件 stock_warehouse_orderpoint_view.xml 代码行 icon="fa fa-cogs" 改成 icon="fa-cogs" ，另一个是文件 wizards/make_procurement_orderpoint.py 代码行  comodel_name='product.uom') 改为 comodel_name='uom.uom')

推荐数量增加补货单位计算：

This module allows users to manually start procurements from the list of reordering rules, based on the quantity that is recommended to be procured.

###

### Configuration

If you want users to be able to change the recommended quantity to procure, you should assign them to the security group 'Change quantity in manual procurements from reordering rules', under 'Settings / Users / Users'.

###

### Usage

Go to 'Inventory > Master Data > Reordering Rules' and review the quantity recommended to be procured. You can now start the procurement for a single or a list of reordering rules.

The recommended quantity to procure is adjusted to the procurement unit of measure indicated in the reordering rule.

## 补充/答案 1

心得：

1.记得把安排的动作的调度器关了。

2.odoo12，要把单位的表名称改改，product.uom --> uom.uom

3.那个icon在odoo12失效了，自己换个icon好看一点儿。其实我这个也不是很好表达。

![[2-ocastock-orderpoint-manual-procurement-2858-9c566969.png]]

4.用在什么场景呢？

智立方希望库存低于最小数量的时候可以报警。

这个模块虽然不能报警，但是可查对吧.

或者大家有什么好想法好的模块推荐。

谢谢。

## 补充/答案 2

这个模块有个测试用下来反馈的问题，计算有点问题，另外小数点精度较高时，会自动四舍五入，当企业对小数点精度要求较高，或小数点位数较多时，mrp运算会有问题。


## 原帖外链配图

![[2-ocastock-orderpoint-manual-procureme-x194038c2.png]]
<small>原始地址: /web/image/1355/snipaste_20190215_124647.png?access_token=afff1ec4-df4a-419f-a1c4-7c63b7e7176d</small>

![[2-ocastock-orderpoint-manual-procureme-x194038c2.png]]
<small>原始地址: /web/image/1357/snipaste_20190215_125401.png?access_token=db0bae42-fb40-462c-80d5-90c3bac6ce67</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
