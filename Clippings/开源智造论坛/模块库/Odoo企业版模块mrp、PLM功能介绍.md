---
title: "Odoo企业版模块mrp、PLM功能介绍"
source: "http://www.thinkltd.cn/forum/2/odoomrpplm-3009"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Odoo企业版模块mrp、PLM功能介绍

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/odoomrpplm-3009>

一、制造类型的Rule设置，该Rule产生MO

二、BoM表设置

三、MO生产单操作

四、工作中心及IoT设备

五、WO车间生产操作

## 补充/答案 1

生产外协加工的实现方案：

1.  设置外协车间、外协供应商、外协加工Service产品

2.  需要外协加工的产品/半成品，其BoM表中添加外协加工Service产品作为原料。参考 [外协加工/forum/2/question/ocamrp-production-service-2636](http://www.thinkltd.cn/forum/2/question/ocamrp-production-service-2636)

3.  设置外协加工路线：当Stock需要外协加工品时候，从外协车间移动过来；当外协车间需要加工品时候，Manufacture制造出来。

4.  设置外协发料路线：当虚拟生产库位需要原料时候，从外协车间移动过去，并设置为MTO；当外协车间需要原料时候，从Stock移动过去。

如此设置后，当Stock有外协品需求时候，系统自动产生：1) 外协车间到Stock的外协成品调拨单；2) 外协品生产单MO；3) 从Stock到外协车间的发料单；4) 外协加工的Service产品采购单

## 补充/答案 2

生产工单的质量检查点quality_mrp_iot 功能：

1.  生产工序上可以定义多个质量检查点；

2.  质量检查点的类型有：拍照（Take  a picture）、测量(Measure)、手册查看（Text）、记录物料消耗（Register Cosumed Materials）、通过/不通过（Pass - Fail）

3.  不同的质量检查类型，对应的工单操作界面不同

4.

不同质量检查类型对应的工单操作界面：

拍照：

记录物料消耗

查看文本

通过/不通过

测量

## 补充/答案 3

工作中心（WorkCenter）与Odoo IoT之间的数据接口。

1.  工作中心与IoT之间有两个接口，一个是ERP向工作中心发指令（传数据），一个是工作中心向ERP发指令（传数据）；

2.  向工作中心发指令的方法是，调用IoT Box hw_drivers 模块的 /hw_drivers/action 接口。工作中心Driver实现此接口处理不同指令；

3.  工作中心向ERP发指令的接口是IoT Box hw_drivers 模块的 /hw_drivers/event ，ERP端 js 通过polling机制频繁调用/hw_drivers/event接口，获取设备变化信息。

4.  polling机制获取到/hw_drivers/event的输入值后，首先匹配工作中心上预定义的Trigger键值动作。如果匹配上设备、键值，则自动调用对应的动作。

5.

工作中心Trigger 定义：

Trigger对应的动作：

IoT Box 扫描枪Driver示例代码。

## 补充/答案 4

工作中心，在操作完一个工序后，上面成品的序列号，在下一个工序上如何体现出来？或者上一工序完成了，如何查找这个原来录过的成品序列号？

我测试后发现这个序列号在完工的前一道工序上找不到了。

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
