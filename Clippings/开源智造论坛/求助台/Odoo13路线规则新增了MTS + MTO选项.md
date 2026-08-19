---
title: "Odoo13路线规则新增了MTS + MTO选项"
source: "http://www.thinkltd.cn/forum/1/odoo13mts-mto-428"
forum: "求助台"
author: "肖相扶"
published: 2022-12-15
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Odoo13路线规则新增了MTS + MTO选项

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2022-12-15
> <http://www.thinkltd.cn/forum/1/odoo13mts-mto-428>

![[1-odoo13mts-mto-428-6d7095ad.png]]

## 补充/答案 1

经测试，这个路线规则是：系统检查库存数量及需求数量，如果库存数量（预测数量）大于等于需求数量，按MTS逻辑补货，否则按MTO逻辑补货。更期望的逻辑应该是：库存数量（预测数量）小于需求数量，有库存部分按MTS逻辑，不足部分按MTO逻辑。

代码文件 Odoo13\source\odoo\addons\stock\models\stock_rule.py 方法 def _run_pull(self, procurements):  替换成下述代码即可改成期望逻辑。

![[1-odoo13mts-mto-428-cdedca4c.png]]

```python
    @api.model
    def _run_pull(self, procurements):
        moves_values_by_company = defaultdict(list)
        mtso_products_by_locations = defaultdict(list)
```

        # To handle the `mts_else_mto` procure method, we do a preliminary loop to
        # isolate the products we would need to read the forecasted quantity,
        # in order to to batch the read. We also make a sanitary check on the
        # `location_src_id` field.
```python
        for procurement, rule in procurements:
            if not rule.location_src_id:
                msg = _('No source location defined on stock rule: %s!') % (rule.name, )
                raise UserError(msg)

            if rule.procure_method == 'mts_else_mto':
                mtso_products_by_locations[rule.location_src_id].append(procurement.product_id.id)
```

        # Get the forecasted quantity for the `mts_else_mto` procurement.
```python
        forecasted_qties_by_loc = {}
        for location, product_ids in mtso_products_by_locations.items():
            products = self.env['product.product'].browse(product_ids).with_context(location=location.id)
            forecasted_qties_by_loc[location] = {product.id: product.virtual_available for product in products}
```

        # Prepare the move values, adapt the `procure_method` if needed.
```python
        for procurement, rule in procurements:
            procure_method = rule.procure_method
            product_uom_qty = procurement.product_qty
            if rule.procure_method == 'mts_else_mto':
                qty_needed = procurement.product_uom._compute_quantity(procurement.product_qty, procurement.product_id.uom_id)
                qty_available = forecasted_qties_by_loc[rule.location_src_id][procurement.product_id.id]
                if float_compare(qty_needed, qty_available, precision_rounding=procurement.product_id.uom_id.rounding)  0 \\
                        and float_compare(qty_available, 0, precision_rounding=procurement.product_id.uom_id.rounding) > 0:
                        move_values = rule._get_stock_move_values(*procurement)
                        move_values['procure_method'] = 'make_to_stock'
                        move_values['product_uom_qty'] = qty_available
                        forecasted_qties_by_loc[rule.location_src_id][procurement.product_id.id] -= qty_available
                        moves_values_by_company[procurement.company_id.id].append(move_values)
                        product_uom_qty -= qty_available

            move_values = rule._get_stock_move_values(*procurement)
            move_values['procure_method'] = procure_method
            if rule.procure_method == 'mts_else_mto':
                move_values['product_uom_qty'] = product_uom_qty
            moves_values_by_company[procurement.company_id.id].append(move_values)
```

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
