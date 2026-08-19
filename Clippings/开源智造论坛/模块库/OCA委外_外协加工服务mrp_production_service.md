---
title: "OCA委外/外协加工服务mrp_production_service"
source: "http://www.thinkltd.cn/forum/2/oca-mrp-production-service-2636"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# OCA委外/外协加工服务mrp_production_service

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/oca-mrp-production-service-2636>

模块链接：

依赖模块：

Odoo 12.0修改点：

- mrp_production_service 不用修改，直接可以用

- subcontracted_service的文件__manifest__.py的模块依赖改为purchase_stock 。 11.0版本是 purchase

- subcontracted_service 的修改点，文件 subcontracted_service\models\warehouse.py  四处修改，如下图。修改后的文件

reates procurement orders from manufacturing orders, for services included in the Bill of Materials.

This allows users to include additional services that are to be procured as part of the manufacturing process.

## Subcontracted services

This module allows a user to indicate that a service is subcontracted. It provides the ability to create purchases from procurement processes.

This is a base module, upon specific modules for sale / manufacuturing, modules will need to rely on. By itself it does not provide any function to the end user.

Possible uses of this module can be:

- Add subcontracted services to BOMs. When a manufacturing order is created a PO is triggered for the service to be subcontracted. See
- Add subcontracted services to sales order. When the SO is confirmed, it creates a PO for the service.

###

### Configuration

To configure this module, you need to:

1.  Configure your service product with the flag `property_subcontracted_service` in product form if this product should trigger a procurement.
2.  Add supplier in your product form.
3.  Additionally and despite a predefined rule is created in each warehouse, you can configure the 'Subcontracting_service procurement rule' for each warehouse through 'Inventory / Configuration / Warehouse Management / Warehouse'.

## 补充/答案 1

V13版有自带委外应用，学习参考：

https://www.odoo.com/documentation/user/13.0/manufacturing/management/subcontracting.html


## 附件

- [[附件/forum/2-oca-mrp-production-service-2636-Copy of VAT invoice information_.xlsx|Copy of VAT invoice information_.xlsx]] (36 KB)


## 原帖外链配图

![[2-oca-mrp-production-service-2636-x194038c2.png]]
<small>原始地址: /web/image/1636/snipaste_20190503_173413.png?access_token=dc4815a4-c7f4-4a5c-989c-e6e91f75439d</small>

![[2-oca-mrp-production-service-2636-x194038c2.png]]
<small>原始地址: /web/image/952/snipaste_20190120_194108.png?access_token=a3fad1de-c4c4-4a4f-8a56-6f6755810d7b</small>

![[2-oca-mrp-production-service-2636-x194038c2.png]]
<small>原始地址: /web/image/954/snipaste_20190120_194716.png?access_token=2d425719-d298-436c-ae54-b52fd548262f</small>

![[2-oca-mrp-production-service-2636-x194038c2.png]]
<small>原始地址: /web/image/956/snipaste_20190120_194727.png?access_token=b19ee66f-5d66-420a-bce0-4403a3cd8f0b</small>

![[2-oca-mrp-production-service-2636-x194038c2.png]]
<small>原始地址: /web/image/958/snipaste_20190120_194202.png?access_token=ec5fec8f-cad7-4b60-992c-771cfb0336e5</small>

![[2-oca-mrp-production-service-2636-x194038c2.png]]
<small>原始地址: /web/image/960/snipaste_20190120_194448.png?access_token=49521872-ec46-40b9-a2c9-ce324764ea4f</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
