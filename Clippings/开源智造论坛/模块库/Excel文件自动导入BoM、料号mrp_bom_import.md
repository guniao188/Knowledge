---
title: "Excel文件自动导入BoM、料号mrp_bom_import"
source: "http://www.thinkltd.cn/forum/2/excelbommrp-bom-import-3473"
forum: "模块库"
author: "肖相扶"
published: 2023-10-09
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/模块库
---

# Excel文件自动导入BoM、料号mrp_bom_import

> [!info] 来源
> 开源智造论坛 · 模块库 | 作者:肖相扶 | 2023-10-09
> <http://www.thinkltd.cn/forum/2/excelbommrp-bom-import-3473>

2023年10月09日备注：此模块不再需要，已经被更通用的模块替代，参考  [带参数执行服务器动作/上传Excel文件服务器动作进行处理base_server_action_params](http://www.thinkltd.cn/forum/2/excelbase-server-action-params-3583)

模块链接：OSCG_SVN\odoo_ecommerce\14.0SRC\生产制造\mrp_bom_import

【模块功能】

1.  制造模块中增加“BoM导入”菜单，上传Excel格式的BoM设计文件，自动导入产品、产品分类、产品供应商，工作中心、BoM、工艺路线

2.  2021/8/3日，新增产品图像导入功能。此功能要求Excel中有产品图像，且有一列“图文名” 指定产品图像文件在Excel中的文件名（image1, image2, image3 等等）。Excel中的图片数据提取方法参考：

【功能截图】

![[2-excelbommrp-bom-import-3473-5c479dd2.png]]

![[2-excelbommrp-bom-import-3473-10da444b.png]]

Excel文件示例

![[2-excelbommrp-bom-import-3473-450a3369.png]]

## 补充/答案 1

导入时会报错
```python
    Odoo Server Error

    Traceback (most recent call last):
      File "D:\odoo\odoo14\odoo-server14\odoo\addons\base\models\ir_http.py", line 237, in _dispatch
        result = request.dispatch()
      File "D:\odoo\odoo14\odoo-server14\odoo\http.py", line 683, in dispatch
        result = self._call_function(**self.params)
      File "D:\odoo\odoo14\odoo-server14\odoo\http.py", line 359, in _call_function
        return checked_call(self.db, *args, **kwargs)
      File "D:\odoo\odoo14\odoo-server14\odoo\service\model.py", line 94, in wrapper
        return f(dbname, *args, **kwargs)
      File "D:\odoo\odoo14\odoo-server14\odoo\http.py", line 347, in checked_call
        result = self.endpoint(*a, **kw)
      File "D:\odoo\odoo14\odoo-server14\odoo\http.py", line 912, in __call__
        return self.method(*args, **kw)
      File "D:\odoo\odoo14\odoo-server14\odoo\http.py", line 531, in response_wrap
        response = f(*args, **kw)
      File "d:\odoo\odoo14\odoo-server14\addons\web\controllers\main.py", line 1393, in call_button
        action = self._call_kw(model, method, args, kwargs)
      File "d:\odoo\odoo14\odoo-server14\addons\web\controllers\main.py", line 1381, in _call_kw
        return call_kw(request.env[model], method, args, kwargs)
      File "D:\odoo\odoo14\odoo-server14\odoo\api.py", line 396, in call_kw
        result = _call_kw_multi(method, model, args, kwargs)
      File "D:\odoo\odoo14\odoo-server14\odoo\api.py", line 383, in _call_kw_multi
        result = method(recs, *args, **kwargs)
      File "d:\odoo\add\mrp_bom_import\wizard\bom_import_wizard.py", line 343, in bom_import
        self.product_create(products)
      File "d:\odoo\add\mrp_bom_import\wizard\bom_import_wizard.py", line 116, in product_create
        categs = self.categ_create(products)
      File "d:\odoo\add\mrp_bom_import\wizard\bom_import_wizard.py", line 85, in categ_create
        categ = self.env["product.category"].search([('name', '=', cname), ('parent_id', '=', parent)])
      File "D:\odoo\odoo14\odoo-server14\odoo\models.py", line 1708, in search
        res = self._search(args, offset=offset, limit=limit, order=order, count=count)
      File "D:\odoo\odoo14\odoo-server14\odoo\models.py", line 4494, in _search
        query = self._where_calc(args)
      File "D:\odoo\odoo14\odoo-server14\odoo\models.py", line 4250, in _where_calc
        return expression.expression(domain, self).query
      File "D:\odoo\odoo14\odoo-server14\odoo\osv\expression.py", line 442, in __init__
        self.parse()
      File "D:\odoo\odoo14\odoo-server14\odoo\osv\expression.py", line 863, in parse
        expr, params = self.__leaf_to_sql(leaf, model, alias)
      File "D:\odoo\odoo14\odoo-server14\odoo\osv\expression.py", line 942, in __leaf_to_sql
        assert not isinstance(right, BaseModel),
    Exception
    The above exception was the direct cause of the following exception:
    Traceback (most recent call last):
      File "D:\odoo\odoo14\odoo-server14\odoo\http.py", line 639, in _handle_exception
        return super(JsonRequest, self)._handle_exception(exception)
      File "D:\odoo\odoo14\odoo-server14\odoo\http.py", line 315, in _handle_exception
        raise exception.with_traceback(None) from new_cause
    AssertionError: Invalid value product.category(12,) in domain term ('parent_id', '=', product.category(12,))
```

---

相关:[[Clippings/开源智造论坛/模块库/00-模块库索引.md|← 模块库索引]]
