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

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
