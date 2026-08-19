---
title: "如何在Odoo16的Form表单上增加条码功能"
source: "http://www.thinkltd.cn/forum/1/odoo16form-3671"
forum: "求助台"
author: "肖相扶"
published: 2023-04-06
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 如何在Odoo16的Form表单上增加条码功能

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2023-04-06
> <http://www.thinkltd.cn/forum/1/odoo16form-3671>

【业务背景】

需求案例1：销售订单上，扫描产品条码，系统自动将该产品添加到订单明细上，或者对应该产品的明细行数量自动加1。

【实现方法】

1.  Odoo自带的模块 barcodes ，该模块提供了扫码的基础功能，可以在Odoo的任意Form表单上增加条码扫描功能。实现案例参考文件 enterprise\stock_barcode\models\stock_scrap.py ，该文件在报废单的Form视图上增加扫码功能：扫描报废产品条码，报废数量自动加1 。
2.  实现方法：1) 模块依赖 barcodes  ；2) 模型继承 barcodes.barcode_events_mixin ； 3) XML的Form表头上增加字段 _barcode_scanned 的定义： field name="_barcode_scanned" widget="barcode_handler" ；4) 模型py代码中实现方法 def on_barcode_scanned(self, barcode):  该方法接受扫描的条码，对该条码进行业务处理，例如增加一个明细行。

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
