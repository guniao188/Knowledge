---
title: "第三方产品定制化系列模块odoo-product-configurator"
source: "http://www.thinkltd.cn/forum/2/odoo-product-configurator-3026"
forum: "模块库"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# 第三方产品定制化系列模块odoo-product-configurator

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/2/odoo-product-configurator-3026>

模块链接：

【Odoo 12.0升级方法】

1) 文件 product_configurator\wizard\product_configurator.py", line 4,  按下述方法修改

#from odoo.addons.base.ir.ir_model import FIELD_TYPES
from odoo.addons.base.models.ir_model import FIELD_TYPES

2) 文件 product_configurator\static\js\data_manager.js , line 14 按下述方法修改：

            //if (params.context.eval()['view_cache'] == false) {
            if (params.context['view_cache'] == false) {

3) 将下述代码中的 product.attribute.line 替换为 product.template.attribute.line （全局替换）

F:\Odoo12\myaddons\product_configurator\demo\product_attribute.xml(242):
F:\Odoo12\myaddons\product_configurator\demo\product_attribute.xml(252):
F:\Odoo12\myaddons\product_configurator\demo\product_attribute.xml(270):
F:\Odoo12\myaddons\product_configurator\demo\product_attribute.xml(285):
F:\Odoo12\myaddons\product_configurator\demo\product_attribute.xml(296):
F:\Odoo12\myaddons\product_configurator\demo\product_attribute.xml(307):
F:\Odoo12\myaddons\product_configurator\demo\product_attribute.xml(318):
F:\Odoo12\myaddons\product_configurator\demo\product_attribute.xml(329):
F:\Odoo12\myaddons\product_configurator\models\product_attribute.py(131):     _inherit = 'product.attribute.line'
F:\Odoo12\myaddons\product_configurator\models\product_attribute.py(206):         comodel_name='product.attribute.line',
F:\Odoo12\myaddons\product_configurator\models\product_config.py(158):         comodel_name='product.attribute.line',
F:\Odoo12\myaddons\product_configurator\models\product_config.py(262):         comodel_name='product.attribute.line',
F:\Odoo12\myaddons\product_configurator\wizard\product_configurator.py(259):         comodel_name='product.attribute.line',

## 补充/答案 1

1) 权限配置

2) 产品定制步骤

3) 定制化选项配置

## 补充/答案 2

product_configurator_sale：


## 原帖外链配图

![[2-odoo-product-configurator-3026-x194038c2.png]]
<small>原始地址: /web/image/1524/snipaste_20190327_113851.png?access_token=60107d42-c8d2-4dad-b20f-f19ef6b2500e</small>

![[2-odoo-product-configurator-3026-x194038c2.png]]
<small>原始地址: /web/image/1526/snipaste_20190327_114118.png?access_token=b2edcd36-39c7-4059-ac62-9fad66ecae64</small>

![[2-odoo-product-configurator-3026-x194038c2.png]]
<small>原始地址: /web/image/1528/snipaste_20190327_114237.png?access_token=fe952d39-0489-43f5-ac02-e81c5c16f42d</small>

![[2-odoo-product-configurator-3026-x194038c2.png]]
<small>原始地址: /web/image/1530/snipaste_20190327_114308.png?access_token=08d65c08-ec29-4d3a-a391-51bf491ebe1a</small>

![[2-odoo-product-configurator-3026-x194038c2.png]]
<small>原始地址: /web/image/1532/snipaste_20190327_114335.png?access_token=064d9c51-bf18-4b35-92ea-001c30d031ce</small>

![[2-odoo-product-configurator-3026-x194038c2.png]]
<small>原始地址: /web/image/1534/snipaste_20190327_114407.png?access_token=aeda3525-8d52-4fd0-adf5-575f9c621737</small>

![[2-odoo-product-configurator-3026-x194038c2.png]]
<small>原始地址: /web/image/1536/snipaste_20190327_150413.png?access_token=ec382d7c-94e5-46bd-b61d-205de4467834</small>

![[2-odoo-product-configurator-3026-x194038c2.png]]
<small>原始地址: /web/image/1538/snipaste_20190327_150729.png?access_token=5b76adf9-9757-4024-b431-46be433e7236</small>

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
