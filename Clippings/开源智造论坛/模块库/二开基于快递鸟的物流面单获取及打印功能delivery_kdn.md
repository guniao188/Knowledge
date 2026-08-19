---
title: "二开基于快递鸟的物流面单获取及打印功能delivery_kdn"
source: "http://www.thinkltd.cn/forum/2/delivery-kdn-3389"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开基于快递鸟的物流面单获取及打印功能delivery_kdn

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/delivery-kdn-3389>

模块位置：OSCG_SVN\odoo_ecommerce\14.0SRC\仓库物流

其中 delivery_kdn 是快递鸟接口，delivery_kdn_sf 是顺丰速运接口

模块安装前先安装快递鸟的Python接口包：pip3 install kdn_sdk>=0.1.0

【模块功能】

1.  Picking单上如果指定了物流公司（如顺丰速运），Picking验证时候，系统自动调用快递鸟接口获取电子面单，获取到的面单文件以附件形式存在Picking的Message区域

2.  该模块取Picking上的Partner作为收货地址，该Partner省市区街道地址、电话或手机号码必须填写完整

3.  该模块取当前公司的Partner作为发货地址，该Partner省市区街道地址、电话或手机号码必须填写完整

4.  点击Picking右上角的Tacking按钮，自动跳转到物流公司的物流单号查询页面

5.  delivery_kdn_sf 模块中增加了顺丰包装箱类型。启用Odoo的打包功能后，打包时候可以选择快递包装类型，并填写包裹重量。

6.  支持子母件快递面单的获取及打印

7.  参考资料：快递鸟API：

【功能截图】

![[2-delivery-kdn-3389-5c4316a7.png]]

![[2-delivery-kdn-3389-6387fa16.png]]

![[2-delivery-kdn-3389-83b2689d.png]]

![[2-delivery-kdn-3389-6e71e6cb.png]]

## 补充/答案 1

【快递面单自动打印】

1.  模块delivery_kdn 中集成了 Lodop 自动打印快递面单。实现方法是在stock.picking上增加了方法：def print_delivery_kdnlabel(self) 。

2.  模块delivery_kdn_sf 的功能是，Picking验证时候，自动连接快递鸟接口，获取顺丰速运面单，并自动打印面单。

3.  自动打印面单的实现原理是：通过bus.bus 将面单文件发送给客户端，客户端调用 Lodop接口打印面单。Lodop功能参见这里：

4.  Lodop的安装方法：从Lodop官网下载安装CLodop，而后使用此网页检测是否安装成功

5.

【子母件快递面单】

1.  Stock Picking上增加了字段“快递包裹数”，默认值是0。

2.  获取快递面单时候，如果“快递包裹数”大于0，系统按“快递包裹数” 获取子母件的快递面单。否则，系统自动计算该Picking的包裹数量，以包裹数量自动填写到“快递包裹数”。如果没有包裹数量，则“快递包裹数”为1，即没有子母件。

3.  子母件的情况，系统自动获取多个快递面单（一个母单，多个子单）

![[2-delivery-kdn-3389-8e98877f.png]]

![[2-delivery-kdn-3389-4fc1079c.png]]

![[2-delivery-kdn-3389-b4a38f15.png]]

## 补充/答案 2

测试发现，快递包裹数填写大于3，打印出来也只有3张面单

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
