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


## 原帖外链配图

![[2-odoomrpplm-3009-x194038c2.png]]
<small>原始地址: /web/image/1443/snipaste_20190309_210840.png?access_token=f588c37c-a90b-4163-b6c8-84a1838c9272</small>

![[2-odoomrpplm-3009-x194038c2.png]]
<small>原始地址: /web/image/1445/snipaste_20190309_205838.png?access_token=19a192db-5b74-4205-873b-8037aa1aa3ee</small>

![[2-odoomrpplm-3009-x194038c2.png]]
<small>原始地址: /web/image/1447/snipaste_20190309_210510.png?access_token=b44f3dfd-54f5-46c3-b9f8-e33984841087</small>

![[2-odoomrpplm-3009-x194038c2.png]]
<small>原始地址: /web/image/1449/snipaste_20190309_215658.png?access_token=a92de477-dcb5-4618-99a1-f7b308f442c1</small>

![[2-odoomrpplm-3009-x194038c2.png]]
<small>原始地址: /web/image/1451/snipaste_20190309_214009.png?access_token=9122cc82-594b-47d5-b9e2-f8bb9481229a</small>

![[2-odoomrpplm-3009-x194038c2.png]]
<small>原始地址: /web/image/1453/snipaste_20190309_214044.png?access_token=c8c0852b-048f-460b-9c65-cfa75e9e5ce1</small>

![[2-odoomrpplm-3009-x194038c2.png]]
<small>原始地址: /web/image/1455/snipaste_20190309_220152.png?access_token=deea91da-ab17-4af0-a860-518a69f1a129</small>

![[2-odoomrpplm-3009-x194038c2.png]]
<small>原始地址: /web/image/1617/snipaste_20190502_194831.png?access_token=fb015f57-7613-4872-89cc-19fdff6a4f67</small>

![[2-odoomrpplm-3009-x194038c2.png]]
<small>原始地址: /web/image/1619/snipaste_20190502_200149.png?access_token=e267ad0e-ef18-43b7-a6b2-55b4cd4ef219</small>

![[2-odoomrpplm-3009-x194038c2.png]]
<small>原始地址: /web/image/1621/snipaste_20190502_200302.png?access_token=4dfff2db-37e9-4315-82ca-43d0b9f25c8c</small>

![[2-odoomrpplm-3009-x194038c2.png]]
<small>原始地址: /web/image/1623/snipaste_20190502_200344.png?access_token=193dc2b0-86dc-45d4-bb5f-a589eec5fe18</small>

![[2-odoomrpplm-3009-x194038c2.png]]
<small>原始地址: /web/image/1625/snipaste_20190502_200418.png?access_token=c046302d-56d6-4e1c-aeaf-baec83f07a92</small>

![[2-odoomrpplm-3009-x194038c2.png]]
<small>原始地址: /web/image/1627/snipaste_20190502_200455.png?access_token=baafdd09-fc35-49c2-8f73-979289585331</small>

![[2-odoomrpplm-3009-x194038c2.png]]
<small>原始地址: /web/image/1629/snipaste_20190502_201215.png?access_token=114eb225-f4ce-4ca4-ba6d-cfc808428f37</small>

![[2-odoomrpplm-3009-x194038c2.png]]
<small>原始地址: /web/image/1631/snipaste_20190502_201906.png?access_token=7c7ebb71-5f2d-4beb-91cf-d092a5d38100</small>

![[2-odoomrpplm-3009-x194038c2.png]]
<small>原始地址: /web/image/1633/snipaste_20190502_201953.png?access_token=83aa4d98-5cbd-44b9-9c93-5f5c06b6e59f</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
