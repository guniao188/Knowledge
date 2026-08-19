---
title: "聚复MemoryError问题解析"
source: "http://www.thinkltd.cn/forum/1/memoryerror-3975"
forum: "求助台"
author: "肖相扶"
published: 2024-09-19
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# 聚复MemoryError问题解析

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:肖相扶 | 2024-09-19
> <http://www.thinkltd.cn/forum/1/memoryerror-3975>

【问题现象】

1.  客户环境聚复，在变体菜单下直接新建变体，手选产品（字段product_tmpl_id）、以及属性值(字段 product_template_attribute_value_ids)，保存，系统报MemoryError错误。
2.  每次出错的代码行还不固定。如下面是截取的两次出错的报错信息，一次出错点在 File "/opt/odoo/odoo16/odoo-server/odoo/tools/misc.py", line 1255, in unique，另一次出错点在  File "/opt/odoo/odoo16/odoo-server/odoo/api.py", line 1107, in insert_missing

【问题原因】

1.  从报错信息分析，应该是变体创建时候，系统自动创建/修改了产品(字段 product_tmpl_id )，而产品的修改触发了很多地方的计算型字段的重新计算，大量的重新计算导致内存报错！
2.  从下面截图的报错信息来看，一个是触发到 stocking_picking_backorder_oscg/models/stock_picking.py,_compute_product_uom_qty_total 时候报错，一个是触发到 addons/delivery/models/sale_order.py,_get_lines_impacting_invoice_status 时报错。

【问题解决】

1.  当给定产品（字段product_tmpl_id）、以及属性值(字段 product_template_attribute_value_ids)时候，应该调用product.template的方法 _create_product_variant( ) 创建变体，而不是直接用 product.product的create方法创建。后者会触发 product.template的创建/修改，从而触发大量的计算型字段重新计算。
2.  参考模块  [产品模板上增加变体配置按钮product_configure](http://www.thinkltd.cn/forum/2/product-configure-3553)，在产品上增加属性配置按钮，点击按钮弹窗显示属性配置画面，配置属性值，创建变体。
3.  参考代码（重写product\models\product_product.py 中的 create 方法）：

```python
        @api.model_create_multi
        def create(self, vals_list):
            products = self.env['product.product']
            for vals in vals_list:
                self.product_tmpl_id._sanitize_vals(vals)

                tmplate_id =  vals.get('product_tmpl_id')
                ptav = vals.get('product_template_attribute_value_ids')
                if tmplate_id and ptav:
                    ptav_ids = ptav[0][2]
                    prt_tmp = self.env['product.template'].browse(tmplate_id)
                    ptav_ids = self.env['product.template.attribute.value'].browse(ptav_ids)
                    product_variant = prt_tmp._get_variant_for_combination(ptav_ids)
                    if not product_variant:
                        product_variant = prt_tmp._create_product_variant(ptav_ids)
                    products |= product_variant

            if not products:
                products = super(ProductProduct, self.with_context(create_product_product=True)).create(vals_list)
```

            # `_get_variant_id_for_combination` depends on existing variants
```python
            self.clear_caches()
            return products

    报错信息一：
    RPC_ERROR
    Odoo Server Error
    Traceback (most recent call last):
      File "/opt/odoo/odoo16/odoo-server/odoo/api.py", line 997, in get
        cache_value = field_cache[record._ids[0]]
    KeyError: 1672759

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
      File "/opt/odoo/odoo16/odoo-server/odoo/fields.py", line 1161, in __get__
        value = env.cache.get(record, self)
      File "/opt/odoo/odoo16/odoo-server/odoo/api.py", line 1004, in get
        raise CacheMiss(record, field)
    odoo.exceptions.CacheMiss: 'stock.move(1672759,).product_id'

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
      File "/opt/odoo/odoo16/odoo-server/odoo/http.py", line 1638, in _serve_db
        return service_model.retrying(self._serve_ir_http, self.env)
      File "/opt/odoo/odoo16/odoo-server/odoo/service/model.py", line 133, in retrying
        result = func()
      File "/opt/odoo/odoo16/odoo-server/odoo/http.py", line 1665, in _serve_ir_http
        response = self.dispatcher.dispatch(rule.endpoint, args)
      File "/opt/odoo/odoo16/odoo-server/odoo/http.py", line 1869, in dispatch
        result = self.request.registry['ir.http']._dispatch(endpoint)
      File "/opt/odoo/odoo16/odoo-server/addons/website/models/ir_http.py", line 237, in _dispatch
        response = super()._dispatch(endpoint)
      File "/opt/odoo/odoo16/odoo-server/odoo/addons/base/models/ir_http.py", line 154, in _dispatch
        result = endpoint(**request.params)
      File "/opt/odoo/odoo16/odoo-server/odoo/http.py", line 700, in route_wrapper
        result = endpoint(self, *args, **params_ok)
      File "/opt/odoo/odoo16/odoo-server/addons/web/controllers/dataset.py", line 42, in call_kw
        return self._call_kw(model, method, args, kwargs)
      File "/opt/odoo/odoo16/odoo-server/addons/web/controllers/dataset.py", line 33, in _call_kw
        return call_kw(request.env[model], method, args, kwargs)
      File "/opt/odoo/odoo16/odoo-server/odoo/api.py", line 466, in call_kw
        result = _call_kw_model_create(method, model, args, kwargs)
      File "/opt/odoo/odoo16/odoo-server/odoo/api.py", line 444, in _call_kw_model_create
        result = method(recs, *args, **kwargs)
      File "", line 2, in create
      File "/opt/odoo/odoo16/odoo-server/odoo/api.py", line 414, in _model_create_multi
        return create(self, [arg])
      File "/mnt/odoo/odoo16/custom_llctest/addons/common_connector_library/models/product_product.py", line 48, in create
        res = super(ProductProduct, self).create(vals_list)
      File "", line 2, in create
      File "/opt/odoo/odoo16/odoo-server/odoo/api.py", line 415, in _model_create_multi
        return create(self, arg)
      File "/opt/odoo/odoo16/odoo-server/addons/product/models/product_product.py", line 300, in create
        products = super(ProductProduct, self.with_context(create_product_product=True)).create(vals_list)
      File "", line 2, in create
      File "/opt/odoo/odoo16/odoo-server/odoo/api.py", line 415, in _model_create_multi
        return create(self, arg)
      File "/opt/odoo/odoo16/odoo-server/addons/mail/models/mail_thread.py", line 258, in create
        threads = super(MailThread, self).create(vals_list)
      File "", line 2, in create
      File "/opt/odoo/odoo16/odoo-server/odoo/api.py", line 415, in _model_create_multi
        return create(self, arg)
      File "/opt/odoo/odoo16/odoo-server/odoo/addons/base/models/ir_fields.py", line 670, in create
        recs = super().create(vals_list)
      File "", line 2, in create
      File "/opt/odoo/odoo16/odoo-server/odoo/api.py", line 415, in _model_create_multi
        return create(self, arg)
      File "/opt/odoo/odoo16/odoo-server/odoo/models.py", line 3964, in create
        parent.write(data['inherited'][model_name])
      File "/mnt/odoo/odoo16/custom_llctest/addons/shopify_ept/models/product.py", line 25, in write
        res = super(ProductTemplate, self).write(vals)
      File "/mnt/odoo/odoo16/custom_llctest/addons/common_connector_library/models/product_template.py", line 40, in write
        res = super(ProductTemplate, self).write(vals)
      File "/opt/odoo/odoo16/odoo-server/addons/stock_landed_costs/models/product.py", line 23, in write
        return super().write(vals)
      File "/opt/odoo/odoo16/odoo-server/addons/stock_account/models/product.py", line 52, in write
        res = super(ProductTemplate, self).write(vals)
      File "/opt/odoo/odoo16/odoo-server/addons/mrp/models/product.py", line 84, in write
        return super().write(values)
      File "/opt/odoo/odoo16/odoo-server/addons/stock/models/product.py", line 908, in write
        return super(ProductTemplate, self).write(vals)
      File "/opt/odoo/odoo16/odoo-server/addons/product/models/product_template.py", line 455, in write
        self._create_variant_ids()
      File "/opt/odoo/odoo16/odoo-server/addons/product/models/product_template.py", line 619, in _create_variant_ids
        self.env.flush_all()
      File "/opt/odoo/odoo16/odoo-server/odoo/api.py", line 745, in flush_all
        self._recompute_all()
      File "/opt/odoo/odoo16/odoo-server/odoo/api.py", line 741, in _recompute_all
        self[field.model_name]._recompute_field(field)
      File "/opt/odoo/odoo16/odoo-server/odoo/models.py", line 6274, in _recompute_field
        field.recompute(records)
      File "/opt/odoo/odoo16/odoo-server/odoo/fields.py", line 1370, in recompute
        apply_except_missing(self.compute_value, recs)
      File "/opt/odoo/odoo16/odoo-server/odoo/fields.py", line 1343, in apply_except_missing
        func(records)
      File "/opt/odoo/odoo16/odoo-server/odoo/fields.py", line 1392, in compute_value
        records._compute_field_value(self)
      File "/opt/odoo/odoo16/odoo-server/addons/mail/models/mail_thread.py", line 403, in _compute_field_value
        return super()._compute_field_value(field)
      File "/opt/odoo/odoo16/odoo-server/odoo/models.py", line 4232, in _compute_field_value
        fields.determine(field.compute, self)
      File "/opt/odoo/odoo16/odoo-server/odoo/fields.py", line 98, in determine
        return needle(*args)
      File "/mnt/odoo/odoo16/custom_llctest/addons/stocking_picking_backorder_oscg/models/stock_picking.py", line 31, in _compute_product_uom_qty_total
        move_line_demand = dem.move_ids.filtered(lambda d: d.product_id.type == 'product')
      File "/opt/odoo/odoo16/odoo-server/odoo/models.py", line 5444, in filtered
        return self.browse([rec.id for rec in self if func(rec)])
      File "/opt/odoo/odoo16/odoo-server/odoo/models.py", line 5444, in
        return self.browse([rec.id for rec in self if func(rec)])
      File "/mnt/odoo/odoo16/custom_llctest/addons/stocking_picking_backorder_oscg/models/stock_picking.py", line 31, in
        move_line_demand = dem.move_ids.filtered(lambda d: d.product_id.type == 'product')
      File "/opt/odoo/odoo16/odoo-server/odoo/fields.py", line 2804, in __get__
        return super().__get__(records, owner)
      File "/opt/odoo/odoo16/odoo-server/odoo/fields.py", line 1187, in __get__
        recs._fetch_field(self)
      File "/opt/odoo/odoo16/odoo-server/odoo/models.py", line 3201, in _fetch_field
        self._read(fnames)
      File "/opt/odoo/odoo16/odoo-server/odoo/models.py", line 3307, in _read
        self.env.cache.insert_missing(fetched, field, values)
      File "/opt/odoo/odoo16/odoo-server/odoo/api.py", line 1107, in insert_missing
        field_cache.setdefault(id_, val)
    MemoryError

    The above server error caused the following client error:
    null

    出错信息二：
    RPC_ERROR
    Odoo Server Error
    Traceback (most recent call last):
      File "/opt/odoo/odoo16/odoo-server/odoo/api.py", line 997, in get
        cache_value = field_cache[record._ids[0]]
    KeyError: 401341

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
      File "/opt/odoo/odoo16/odoo-server/odoo/fields.py", line 1161, in __get__
        value = env.cache.get(record, self)
      File "/opt/odoo/odoo16/odoo-server/odoo/api.py", line 1004, in get
        raise CacheMiss(record, field)
    odoo.exceptions.CacheMiss: 'sale.order.line(401341,).is_delivery'

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
      File "/opt/odoo/odoo16/odoo-server/odoo/http.py", line 1638, in _serve_db
        return service_model.retrying(self._serve_ir_http, self.env)
      File "/opt/odoo/odoo16/odoo-server/odoo/service/model.py", line 133, in retrying
        result = func()
      File "/opt/odoo/odoo16/odoo-server/odoo/http.py", line 1665, in _serve_ir_http
        response = self.dispatcher.dispatch(rule.endpoint, args)
      File "/opt/odoo/odoo16/odoo-server/odoo/http.py", line 1869, in dispatch
        result = self.request.registry['ir.http']._dispatch(endpoint)
      File "/opt/odoo/odoo16/odoo-server/addons/website/models/ir_http.py", line 237, in _dispatch
        response = super()._dispatch(endpoint)
      File "/opt/odoo/odoo16/odoo-server/odoo/addons/base/models/ir_http.py", line 154, in _dispatch
        result = endpoint(**request.params)
      File "/opt/odoo/odoo16/odoo-server/odoo/http.py", line 700, in route_wrapper
        result = endpoint(self, *args, **params_ok)
      File "/opt/odoo/odoo16/odoo-server/addons/web/controllers/dataset.py", line 42, in call_kw
        return self._call_kw(model, method, args, kwargs)
      File "/opt/odoo/odoo16/odoo-server/addons/web/controllers/dataset.py", line 33, in _call_kw
        return call_kw(request.env[model], method, args, kwargs)
      File "/opt/odoo/odoo16/odoo-server/odoo/api.py", line 466, in call_kw
        result = _call_kw_model_create(method, model, args, kwargs)
      File "/opt/odoo/odoo16/odoo-server/odoo/api.py", line 444, in _call_kw_model_create
        result = method(recs, *args, **kwargs)
      File "", line 2, in create
      File "/opt/odoo/odoo16/odoo-server/odoo/api.py", line 414, in _model_create_multi
        return create(self, [arg])
      File "/mnt/odoo/odoo16/custom_llctest/addons/common_connector_library/models/product_product.py", line 48, in create
        res = super(ProductProduct, self).create(vals_list)
      File "", line 2, in create
      File "/opt/odoo/odoo16/odoo-server/odoo/api.py", line 415, in _model_create_multi
        return create(self, arg)
      File "/opt/odoo/odoo16/odoo-server/addons/product/models/product_product.py", line 300, in create
        products = super(ProductProduct, self.with_context(create_product_product=True)).create(vals_list)
      File "", line 2, in create
      File "/opt/odoo/odoo16/odoo-server/odoo/api.py", line 415, in _model_create_multi
        return create(self, arg)
      File "/opt/odoo/odoo16/odoo-server/addons/mail/models/mail_thread.py", line 258, in create
        threads = super(MailThread, self).create(vals_list)
      File "", line 2, in create
      File "/opt/odoo/odoo16/odoo-server/odoo/api.py", line 415, in _model_create_multi
        return create(self, arg)
      File "/opt/odoo/odoo16/odoo-server/odoo/addons/base/models/ir_fields.py", line 670, in create
        recs = super().create(vals_list)
      File "", line 2, in create
      File "/opt/odoo/odoo16/odoo-server/odoo/api.py", line 415, in _model_create_multi
        return create(self, arg)
      File "/opt/odoo/odoo16/odoo-server/odoo/models.py", line 3964, in create
        parent.write(data['inherited'][model_name])
      File "/mnt/odoo/odoo16/custom_llctest/addons/shopify_ept/models/product.py", line 25, in write
        res = super(ProductTemplate, self).write(vals)
      File "/mnt/odoo/odoo16/custom_llctest/addons/common_connector_library/models/product_template.py", line 40, in write
        res = super(ProductTemplate, self).write(vals)
      File "/opt/odoo/odoo16/odoo-server/addons/stock_landed_costs/models/product.py", line 23, in write
        return super().write(vals)
      File "/opt/odoo/odoo16/odoo-server/addons/stock_account/models/product.py", line 52, in write
        res = super(ProductTemplate, self).write(vals)
      File "/opt/odoo/odoo16/odoo-server/addons/mrp/models/product.py", line 84, in write
        return super().write(values)
      File "/opt/odoo/odoo16/odoo-server/addons/stock/models/product.py", line 908, in write
        return super(ProductTemplate, self).write(vals)
      File "/opt/odoo/odoo16/odoo-server/addons/product/models/product_template.py", line 455, in write
        self._create_variant_ids()
      File "/opt/odoo/odoo16/odoo-server/addons/product/models/product_template.py", line 619, in _create_variant_ids
        self.env.flush_all()
      File "/opt/odoo/odoo16/odoo-server/odoo/api.py", line 745, in flush_all
        self._recompute_all()
      File "/opt/odoo/odoo16/odoo-server/odoo/api.py", line 741, in _recompute_all
        self[field.model_name]._recompute_field(field)
      File "/opt/odoo/odoo16/odoo-server/odoo/models.py", line 6274, in _recompute_field
        field.recompute(records)
      File "/opt/odoo/odoo16/odoo-server/odoo/fields.py", line 1370, in recompute
        apply_except_missing(self.compute_value, recs)
      File "/opt/odoo/odoo16/odoo-server/odoo/fields.py", line 1343, in apply_except_missing
        func(records)
      File "/opt/odoo/odoo16/odoo-server/odoo/fields.py", line 1392, in compute_value
        records._compute_field_value(self)
      File "/opt/odoo/odoo16/odoo-server/addons/base_automation/models/base_automation.py", line 444, in _compute_field_value
        _compute_field_value.origin(self, field)
      File "/opt/odoo/odoo16/odoo-server/addons/sale/models/sale_order.py", line 1408, in _compute_field_value
        super()._compute_field_value(field)
      File "/opt/odoo/odoo16/odoo-server/addons/mail/models/mail_thread.py", line 403, in _compute_field_value
        return super()._compute_field_value(field)
      File "/opt/odoo/odoo16/odoo-server/odoo/models.py", line 4232, in _compute_field_value
        fields.determine(field.compute, self)
      File "/opt/odoo/odoo16/odoo-server/odoo/fields.py", line 98, in determine
        return needle(*args)
      File "/opt/odoo/odoo16/odoo-server/addons/delivery/models/sale_order.py", line 153, in _compute_invoice_status
        order_lines = order._get_lines_impacting_invoice_status()
      File "/opt/odoo/odoo16/odoo-server/addons/delivery/models/sale_order.py", line 158, in _get_lines_impacting_invoice_status
        return self.order_line.filtered(
      File "/opt/odoo/odoo16/odoo-server/odoo/models.py", line 5444, in filtered
        return self.browse([rec.id for rec in self if func(rec)])
      File "/opt/odoo/odoo16/odoo-server/odoo/models.py", line 5444, in
        return self.browse([rec.id for rec in self if func(rec)])
      File "/opt/odoo/odoo16/odoo-server/addons/delivery/models/sale_order.py", line 160, in
        not line.is_delivery
      File "/opt/odoo/odoo16/odoo-server/odoo/fields.py", line 1185, in __get__
        recs = record._in_cache_without(self)
      File "/opt/odoo/odoo16/odoo-server/odoo/models.py", line 5974, in _in_cache_without
        ids = self.env.cache.get_missing_ids(self.browse(ids), field)
      File "/opt/odoo/odoo16/odoo-server/odoo/models.py", line 5145, in browse
        ids = tuple(ids)
      File "/opt/odoo/odoo16/odoo-server/odoo/models.py", line 272, in expand_ids
        for id_ in ids:
      File "/opt/odoo/odoo16/odoo-server/odoo/tools/misc.py", line 1255, in unique
        seen.add(e)
    MemoryError

    The above server error caused the following client error:
    null
```

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
