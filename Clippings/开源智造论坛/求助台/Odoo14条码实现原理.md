---
title: "Odoo14条码实现原理"
source: "http://www.thinkltd.cn/forum/1/odoo14-698"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo14条码实现原理

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo14-698>

【条码原理】

1) 模型定义时候，继承 barcodes.barcode_events_mixin，参考代码：odoo\enterprise\mrp_workorder\models\mrp_workorder.py

```python
class MrpProductionWorkcenterLine(models.Model):

    _name = 'mrp.workorder'

    _inherit = ['mrp.workorder', 'barcodes.barcode_events_mixin']
```

2) 模型上重写条码处理方法 def on_barcode_scanned(self, barcode) ，该方法处理条码，或者返回 warning message （条码有误时）

3) 业务条码的处理：Form定义上，加上字段 _barcode_scanned，参考代码：odoo\enterprise\mrp_workorder\views\mrp_workorder_views.xml

4) 命令条码的处理：button定义上加上属性barcode_trigger，如下例，表示条码“O-BTN.validate” 触发button_validate。参考代码：odoo\enterprise\stock_barcode\views\stock_picking_views.xml

                validate

 命令条码实例：

![[1-odoo14-698-53e725d7.png]]

5) 系统下述模型带有条码处理功能。

odoo\enterprise\delivery_barcode\models\stock_picking.py(10):     _inherit = ['stock.picking', 'barcodes.barcode_events_mixin']

odoo\enterprise\mrp_workorder\models\mrp_workorder.py(26):     _inherit = ['mrp.workorder', 'barcodes.barcode_events_mixin']

odoo\enterprise\stock_barcode\models\stock_picking.py(12):     _inherit = ['stock.move.line', 'barcodes.barcode_events_mixin']

odoo\enterprise\stock_barcode\models\stock_picking.py(27):     _inherit = ['stock.picking', 'barcodes.barcode_events_mixin']

odoo\enterprise\stock_barcode\models\stock_scrap.py(9):     _inherit = ['stock.scrap', 'barcodes.barcode_events_mixin']

odoo\enterprise\stock_barcode\wizard\stock_barcode_lot.py(10):     _inherit = ['barcodes.barcode_events_mixin']

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
