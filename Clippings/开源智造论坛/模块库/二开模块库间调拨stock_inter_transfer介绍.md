---
title: "二开模块库间调拨stock_inter_transfer介绍"
source: "http://www.thinkltd.cn/forum/2/stock-inter-transfer-2476"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 二开模块库间调拨stock_inter_transfer介绍

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/stock-inter-transfer-2476>

模块存放位置： OSCG_SVN\odoo_ecommerce\12.0SRC\stock_inter_transfer
13.0版本： OSCG_SVN\odoo_ecommerce\13.0SRC\stock_inter_transfer

- l  仓内调拨：Odoo现有功能中，调拨单是直接从源库位调拨到目标库位，仓内调拨（例如，存储位置优化），这样是OK的，也很方便。

- l  跨仓调拨：跨仓调拨的情况，就不能直接从源库位调拨到目标库位了。这里涉及几个问题，其一是，在途库存管理：如果在途时间较长，希望知道在途库存有多少； 其二是调出仓、运输方、接收仓责任区分问题。如果接收时候发现货物错误，调出仓、运输方、接收仓，谁的责任？

- l  两步调拨：本模块解决跨仓调拨问题，新建调拨单，输入要调出仓、调入仓，调拨类型（一步调拨、两步调拨），调拨货物明细，系统自动生成Odoo调拨单。 如果是两步调拨，系统生成两个Odoo调拨单，一个从源库位到在途库位的调出单，一个从在途库位到目的库位的调入单。

- l  按批次箱号调拨：调拨明细上可以指定批次、箱号，生成Odoo调拨单时候，自动按指定的批次、箱号锁货。系统提供一键批次库存查询功能

- l  预配调拨类型：例如“市场借料”调拨类型，可以预配调出库、调入库、调出类型、调入类型、在途时数等。当调拨单上选择“市场借料”类型时候，系统自动填写其他字段，方便用户操作。

- l  预配调拨菜单：例如，预配“市场借料”菜单，该菜单的调拨类型默认为“市场借料”

## 补充/答案 1

按这里的 12到13的通用升级方法处理之后即可在13.0中安装使用：[/forum/1/question/odoo12odoo13-461](http://www.thinkltd.cn/forum/1/question/odoo12odoo13-461)

处理好以后的版本放到了SVN上  OSCG_SVN\odoo_ecommerce\13.0SRC\stock_inter_transfer

## 补充/答案 2

14.0版本：OSCG_SVN\odoo_ecommerce\14.0SRC\stock_inter_transfer

## 补充/答案 3

【功能截图】Odoo14.0

![[2-stock-inter-transfer-2476-95bc5db1.png]]

![[2-stock-inter-transfer-2476-a4d93069.png]]

![[2-stock-inter-transfer-2476-d8effc3c.png]]

![[2-stock-inter-transfer-2476-be490670.png]]

如果需要包裹移动，作业类型上要勾选“移动整个包裹”

![[2-stock-inter-transfer-2476-89da1843.png]]


## 原帖外链配图

![[2-stock-inter-transfer-2476-x194038c2.png]]
<small>原始地址: /web/image/637/st1.png?access_token=9153a867-e8a7-41a5-b22f-f015c4cd4168</small>

![[2-stock-inter-transfer-2476-x194038c2.png]]
<small>原始地址: /web/image/639/st2.png?access_token=002de567-f27b-4f57-9041-d085922732de</small>

![[2-stock-inter-transfer-2476-x194038c2.png]]
<small>原始地址: /web/image/641/st3.png?access_token=eae10c8d-1c16-4e95-8f22-a7a8a90dcd4d</small>

![[2-stock-inter-transfer-2476-x194038c2.png]]
<small>原始地址: /web/image/643/st4.png?access_token=aca2a236-fdb3-40ab-a3c2-fc85d9f62992</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
